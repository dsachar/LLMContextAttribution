import math
import itertools
from typing import List, Callable

# Import helper functions from attribution.py
from attribution import (
    format_prompt,
    generate_response,
    compute_semantic_similarity,
    compute_log_likelihood,
    compute_log_likelihood_unweighted,
    compute_log_likelihood_wod,
    compute_log_likelihood_wod_unweighted,
    compute_v,
)


class CharacteristicFunction:
    """Computes and caches the characteristic function v(S) for subsets of sentences."""

    def __init__(
        self,
        model,
        tokenizer,
        question,
        sentences,
        response,
        *,
        backend,
        base_sentences=None,
        distractor=None,
        v_type="logprob_difference",
        v_func=None,
        similarity_fn=None,
        max_gen_tokens=128,
    ):
        self.model = model
        self.tokenizer = tokenizer
        self.question = question
        self.sentences = sentences
        self.response = response
        self.backend = backend
        self.base_sentences = base_sentences if base_sentences is not None else []
        self.distractor = distractor
        self.v_type = v_type
        self.v_func = v_func
        self.similarity_fn = similarity_fn
        self.max_gen_tokens = max_gen_tokens

        self.n = len(sentences)
        self.is_similarity = v_type.startswith("similarity") or similarity_fn is not None

        if self.is_similarity:
            grand_prompt = format_prompt(tokenizer, question, self.base_sentences + sentences)
            self.response = generate_response(model, tokenizer, grand_prompt, backend=backend, max_tokens=max_gen_tokens)

            empty_prompt = format_prompt(tokenizer, question, self.base_sentences)
            r_empty = generate_response(model, tokenizer, empty_prompt, backend=backend, max_tokens=max_gen_tokens)
            self.empty_sim = compute_semantic_similarity(model, tokenizer, self.response, r_empty, v_type, backend=backend, similarity_fn=similarity_fn)
        else:
            self.empty_sim = None

        # Precompute log-likelihood values for base / empty coalition
        if v_type == "logprob_wod_difference":
            self.base_ll = compute_log_likelihood_wod(model, tokenizer, question, self.base_sentences, self.response, backend=backend)
        elif v_type == "logprob_wod_unweighted_difference":
            self.base_ll = compute_log_likelihood_wod_unweighted(model, tokenizer, question, self.base_sentences, self.response, backend=backend)
        elif v_type in ["logprob_unweighted_difference", "logprob_bow_unweighted_difference"]:
            self.base_ll = compute_log_likelihood_unweighted(model, tokenizer, question, self.base_sentences, self.response, backend=backend)
        else:
            self.base_ll = compute_log_likelihood(model, tokenizer, question, self.base_sentences, self.response, backend=backend)

        self.base_ll_dist = None
        if distractor is not None:
            if v_type in ["logprob_unweighted_difference", "logprob_wod_unweighted_difference", "logprob_bow_unweighted_difference"]:
                self.base_ll_dist = compute_log_likelihood_unweighted(model, tokenizer, question, self.base_sentences, distractor, backend=backend)
            else:
                self.base_ll_dist = compute_log_likelihood(model, tokenizer, question, self.base_sentences, distractor, backend=backend)

        self.cache = {}

    def evaluate(self, subset_indices):
        """Evaluate the characteristic function v(S) for the given subset of sentence indices."""
        subset_indices = frozenset(subset_indices)
        if subset_indices not in self.cache:
            subset_sents = [self.sentences[i] for i in sorted(subset_indices)]
            self.cache[subset_indices] = compute_v(
                self.model,
                self.tokenizer,
                self.question,
                subset_sents,
                self.response,
                self.base_ll,
                backend=self.backend,
                base_sentences=self.base_sentences,
                distractor=self.distractor,
                empty_ll_dist=self.base_ll_dist,
                v_type=self.v_type,
                v_func=self.v_func,
                similarity_fn=self.similarity_fn,
                max_gen_tokens=self.max_gen_tokens,
                empty_sim=self.empty_sim,
            )
        return self.cache[subset_indices]

    def compute_ll_full(self):
        n = self.n
        if n == 0:
            return self.base_ll

        all_indices = frozenset(range(n))
        all_sents = self.base_sentences + self.sentences
        if n > 1:
            lls = []
            for perm in itertools.permutations(self.sentences):
                if self.v_type == "logprob_wod_difference":
                    ll = compute_log_likelihood_wod(self.model, self.tokenizer, self.question, self.base_sentences + list(perm), self.response, backend=self.backend)
                elif self.v_type == "logprob_wod_unweighted_difference":
                    ll = compute_log_likelihood_wod_unweighted(self.model, self.tokenizer, self.question, self.base_sentences + list(perm), self.response, backend=self.backend)
                elif self.v_type in ["logprob_unweighted_difference", "logprob_bow_unweighted_difference"]:
                    ll = compute_log_likelihood_unweighted(self.model, self.tokenizer, self.question, self.base_sentences + list(perm), self.response, backend=self.backend)
                else:
                    ll = compute_log_likelihood(self.model, self.tokenizer, self.question, self.base_sentences + list(perm), self.response, backend=self.backend)
                lls.append(ll)
            return sum(lls) / len(lls)
        else:
            if self.v_type == "logprob_wod_difference":
                return compute_log_likelihood_wod(self.model, self.tokenizer, self.question, all_sents, self.response, backend=self.backend)
            elif self.v_type == "logprob_wod_unweighted_difference":
                return compute_log_likelihood_wod_unweighted(self.model, self.tokenizer, self.question, all_sents, self.response, backend=self.backend)
            elif self.v_type in ["logprob_unweighted_difference", "logprob_bow_unweighted_difference"]:
                return compute_log_likelihood_unweighted(self.model, self.tokenizer, self.question, all_sents, self.response, backend=self.backend)
            else:
                return compute_log_likelihood(self.model, self.tokenizer, self.question, all_sents, self.response, backend=self.backend)


class AttributionMethod:
    """Base class for all context attribution methods."""

    def attribute(
        self,
        model,
        tokenizer,
        question: str,
        sentences: list,
        response: str,
        *,
        backend,
        base_sentences=None,
        distractor=None,
        v_type="logprob_difference",
        v_func=None,
        similarity_fn=None,
        max_gen_tokens=128,
    ) -> dict:
        raise NotImplementedError


class ShapleyAttribution(AttributionMethod):
    """Computes Shapley values and Faith-Shapley Interaction Indices."""

    def attribute(
        self,
        model,
        tokenizer,
        question: str,
        sentences: list,
        response: str,
        *,
        backend,
        base_sentences=None,
        distractor=None,
        v_type="logprob_difference",
        v_func=None,
        similarity_fn=None,
        max_gen_tokens=128,
    ) -> dict:
        cf = CharacteristicFunction(
            model=model,
            tokenizer=tokenizer,
            question=question,
            sentences=sentences,
            response=response,
            backend=backend,
            base_sentences=base_sentences,
            distractor=distractor,
            v_type=v_type,
            v_func=v_func,
            similarity_fn=similarity_fn,
            max_gen_tokens=max_gen_tokens,
        )

        n = cf.n

        # Evaluate v(S) for all subsets
        v_cache = {}
        for r_bits in range(1 << n):
            subset_indices = frozenset(i for i in range(n) if r_bits & (1 << i))
            v_cache[subset_indices] = cf.evaluate(subset_indices)

        # Compute Shapley values
        phi = [0.0] * n
        for i in range(n):
            others = [j for j in range(n) if j != i]
            for r_bits in range(1 << len(others)):
                S_indices = frozenset(others[k] for k in range(len(others)) if r_bits & (1 << k))
                S_with_i = S_indices | {i}
                s = len(S_indices)
                weight = math.factorial(s) * math.factorial(n - s - 1) / math.factorial(n)
                phi[i] += weight * (v_cache[S_with_i] - v_cache[S_indices])

        # Compute pairwise Faith-Shapley interaction indices
        interactions = {}
        for i in range(n):
            for j in range(i + 1, n):
                others = [k for k in range(n) if k != i and k != j]
                I_ij = 0.0
                for r_bits in range(1 << len(others)):
                    S_indices = frozenset(others[k] for k in range(len(others)) if r_bits & (1 << k))
                    s = len(S_indices)
                    weight = math.factorial(s) * math.factorial(n - s - 2) / math.factorial(n - 1)
                    I_ij += weight * (
                        v_cache[S_indices | {i, j}]
                        - v_cache[S_indices | {i}]
                        - v_cache[S_indices | {j}]
                        + v_cache[S_indices]
                    )
                interactions[(i, j)] = I_ij

        # Build results dict
        result = {
            "response": cf.response,
            "ll_base": cf.base_ll,
            "ll_full": cf.compute_ll_full(),
        }

        # v values for all subsets
        for subset, val in v_cache.items():
            if not subset:
                continue
            key = "v_{" + ",".join(str(i+1) for i in sorted(subset)) + "}"
            result[key] = val

        phi_sum = sum(phi)
        for i in range(n):
            result[f"phi_{i+1}"] = phi[i]
            result[f"phi_normalized_{i+1}"] = phi[i] / phi_sum if abs(phi_sum) > 1e-9 else 1.0 / n

        for (i, j), val in interactions.items():
            result[f"I_{i+1}{j+1}"] = val

        # Legacy keys for backward compatibility with 2-player code
        if n == 2:
            result["v_1"] = v_cache[frozenset([0])]
            result["v_2"] = v_cache[frozenset([1])]
            result["v_12"] = v_cache[frozenset([0, 1])]
            result["I_12"] = interactions[(0, 1)]

        return result


class BanzhafAttribution(AttributionMethod):
    """Computes Banzhaf index attribution."""

    def attribute(
        self,
        model,
        tokenizer,
        question: str,
        sentences: list,
        response: str,
        *,
        backend,
        base_sentences=None,
        distractor=None,
        v_type="logprob_difference",
        v_func=None,
        similarity_fn=None,
        max_gen_tokens=128,
    ) -> dict:
        cf = CharacteristicFunction(
            model=model,
            tokenizer=tokenizer,
            question=question,
            sentences=sentences,
            response=response,
            backend=backend,
            base_sentences=base_sentences,
            distractor=distractor,
            v_type=v_type,
            v_func=v_func,
            similarity_fn=similarity_fn,
            max_gen_tokens=max_gen_tokens,
        )

        n = cf.n

        # Evaluate v(S) for all subsets
        v_cache = {}
        for r_bits in range(1 << n):
            subset_indices = frozenset(i for i in range(n) if r_bits & (1 << i))
            v_cache[subset_indices] = cf.evaluate(subset_indices)

        # Compute Banzhaf indices
        phi = [0.0] * n
        for i in range(n):
            others = [j for j in range(n) if j != i]
            for r_bits in range(1 << len(others)):
                S_indices = frozenset(others[k] for k in range(len(others)) if r_bits & (1 << k))
                S_with_i = S_indices | {i}
                phi[i] += (v_cache[S_with_i] - v_cache[S_indices])
            phi[i] /= (1 << len(others))  # 2^(n-1)

        result = {
            "response": cf.response,
            "ll_base": cf.base_ll,
            "ll_full": cf.compute_ll_full(),
        }

        for subset, val in v_cache.items():
            if not subset:
                continue
            key = "v_{" + ",".join(str(i+1) for i in sorted(subset)) + "}"
            result[key] = val

        phi_sum = sum(phi)
        for i in range(n):
            result[f"phi_{i+1}"] = phi[i]
            result[f"phi_normalized_{i+1}"] = phi[i] / phi_sum if abs(phi_sum) > 1e-9 else 1.0 / n

        return result


class LeaveOneOutAttribution(AttributionMethod):
    """Computes Leave-One-Out (ablation) attribution."""

    def attribute(
        self,
        model,
        tokenizer,
        question: str,
        sentences: list,
        response: str,
        *,
        backend,
        base_sentences=None,
        distractor=None,
        v_type="logprob_difference",
        v_func=None,
        similarity_fn=None,
        max_gen_tokens=128,
    ) -> dict:
        cf = CharacteristicFunction(
            model=model,
            tokenizer=tokenizer,
            question=question,
            sentences=sentences,
            response=response,
            backend=backend,
            base_sentences=base_sentences,
            distractor=distractor,
            v_type=v_type,
            v_func=v_func,
            similarity_fn=similarity_fn,
            max_gen_tokens=max_gen_tokens,
        )

        n = cf.n

        grand_indices = frozenset(range(n))
        v_grand = cf.evaluate(grand_indices)

        v_cache = {grand_indices: v_grand}
        phi = [0.0] * n
        for i in range(n):
            subset_indices = grand_indices - {i}
            v_subset = cf.evaluate(subset_indices)
            v_cache[subset_indices] = v_subset
            phi[i] = v_grand - v_subset

        result = {
            "response": cf.response,
            "ll_base": cf.base_ll,
            "ll_full": cf.compute_ll_full(),
        }

        for subset, val in v_cache.items():
            if not subset:
                continue
            key = "v_{" + ",".join(str(i+1) for i in sorted(subset)) + "}"
            result[key] = val

        phi_sum = sum(phi)
        for i in range(n):
            result[f"phi_{i+1}"] = phi[i]
            result[f"phi_normalized_{i+1}"] = phi[i] / phi_sum if abs(phi_sum) > 1e-9 else 1.0 / n

        return result


class IndividualAttribution(AttributionMethod):
    """Computes Independent single-sentence contribution attribution."""

    def attribute(
        self,
        model,
        tokenizer,
        question: str,
        sentences: list,
        response: str,
        *,
        backend,
        base_sentences=None,
        distractor=None,
        v_type="logprob_difference",
        v_func=None,
        similarity_fn=None,
        max_gen_tokens=128,
    ) -> dict:
        cf = CharacteristicFunction(
            model=model,
            tokenizer=tokenizer,
            question=question,
            sentences=sentences,
            response=response,
            backend=backend,
            base_sentences=base_sentences,
            distractor=distractor,
            v_type=v_type,
            v_func=v_func,
            similarity_fn=similarity_fn,
            max_gen_tokens=max_gen_tokens,
        )

        n = cf.n

        empty_indices = frozenset()
        v_empty = cf.evaluate(empty_indices)

        v_cache = {empty_indices: v_empty}
        phi = [0.0] * n
        for i in range(n):
            subset_indices = frozenset([i])
            v_subset = cf.evaluate(subset_indices)
            v_cache[subset_indices] = v_subset
            phi[i] = v_subset - v_empty

        result = {
            "response": cf.response,
            "ll_base": cf.base_ll,
            "ll_full": cf.compute_ll_full(),
        }

        for subset, val in v_cache.items():
            if not subset:
                continue
            key = "v_{" + ",".join(str(i+1) for i in sorted(subset)) + "}"
            result[key] = val

        phi_sum = sum(phi)
        for i in range(n):
            result[f"phi_{i+1}"] = phi[i]
            result[f"phi_normalized_{i+1}"] = phi[i] / phi_sum if abs(phi_sum) > 1e-9 else 1.0 / n

        return result


class ContextCiteAttribution(AttributionMethod):
    """Computes context attribution by fitting a sparse linear surrogate model (Lasso/Ridge regression)."""

    def __init__(self, num_samples=100, p_keep=0.5, regularization="lasso", alpha=0.1):
        self.num_samples = num_samples
        self.p_keep = p_keep
        self.regularization = regularization.lower()
        self.alpha = alpha

    def attribute(
        self,
        model,
        tokenizer,
        question: str,
        sentences: list,
        response: str,
        *,
        backend,
        base_sentences=None,
        distractor=None,
        v_type="logprob_difference",
        v_func=None,
        similarity_fn=None,
        max_gen_tokens=128,
    ) -> dict:
        import numpy as np

        cf = CharacteristicFunction(
            model=model,
            tokenizer=tokenizer,
            question=question,
            sentences=sentences,
            response=response,
            backend=backend,
            base_sentences=base_sentences,
            distractor=distractor,
            v_type=v_type,
            v_func=v_func,
            similarity_fn=similarity_fn,
            max_gen_tokens=max_gen_tokens,
        )

        n = cf.n
        if n == 0:
            return {
                "response": cf.response,
                "ll_base": cf.base_ll,
                "ll_full": cf.compute_ll_full(),
            }

        # Generate samples (features X)
        # If n is small enough, we can generate all possible 2^n configurations
        if n <= 5:
            samples = []
            for r_bits in range(1 << n):
                samples.append([1 if (r_bits & (1 << i)) else 0 for i in range(n)])
            X = np.array(samples)
        else:
            np.random.seed(42)  # For reproducibility
            X = np.random.binomial(1, self.p_keep, size=(self.num_samples, n))
            # Ensure empty and full configurations are included
            empty = np.zeros((1, n))
            full = np.ones((1, n))
            X = np.vstack([empty, full, X])
            X = np.unique(X, axis=0)

        M = X.shape[0]
        y = np.zeros(M)

        # Evaluate characteristic function for each configuration (target y)
        for idx in range(M):
            subset_indices = frozenset(i for i in range(n) if X[idx, i] == 1)
            y[idx] = cf.evaluate(subset_indices)

        # Fit linear surrogate model y ~ w * X + c
        if self.regularization == "ridge":
            # Center X and y
            X_mean = np.mean(X, axis=0)
            y_mean = np.mean(y)
            X_c = X - X_mean
            y_c = y - y_mean
            A = np.dot(X_c.T, X_c) + self.alpha * M * np.eye(n)
            b = np.dot(X_c.T, y_c)
            w = np.linalg.solve(A, b)
        else:  # lasso
            # Center X and y
            X_mean = np.mean(X, axis=0)
            y_mean = np.mean(y)
            X_c = X - X_mean
            y_c = y - y_mean
            w = np.zeros(n)
            norms = np.sum(X_c**2, axis=0)
            max_iter = 1000
            tol = 1e-4
            for iteration in range(max_iter):
                w_old = w.copy()
                for j in range(n):
                    if norms[j] < 1e-9:
                        continue
                    pred = np.dot(X_c, w)
                    r_j = y_c - pred + X_c[:, j] * w[j]
                    rho = np.dot(X_c[:, j], r_j)
                    threshold = self.alpha * M
                    if rho < -threshold:
                        w[j] = (rho + threshold) / norms[j]
                    elif rho > threshold:
                        w[j] = (rho - threshold) / norms[j]
                    else:
                        w[j] = 0.0
                if np.max(np.abs(w - w_old)) < tol:
                    break

        phi = list(w)
        result = {
            "response": cf.response,
            "ll_base": cf.base_ll,
            "ll_full": cf.compute_ll_full(),
        }

        # v values for all evaluated subsets in cache
        for subset, val in cf.cache.items():
            if not subset:
                continue
            key = "v_{" + ",".join(str(i+1) for i in sorted(subset)) + "}"
            result[key] = val

        phi_sum = sum(phi)
        for i in range(n):
            result[f"phi_{i+1}"] = phi[i]
            result[f"phi_normalized_{i+1}"] = phi[i] / phi_sum if abs(phi_sum) > 1e-9 else 1.0 / n

        return result


# Global registry for methods
ATTRIBUTION_METHODS = {
    "shapley": ShapleyAttribution,
    "loo": LeaveOneOutAttribution,
    "leave_one_out": LeaveOneOutAttribution,
    "individual": IndividualAttribution,
    "independent": IndividualAttribution,
    "banzhaf": BanzhafAttribution,
    "context_cite": ContextCiteAttribution,
    "contextcite": ContextCiteAttribution,
}
