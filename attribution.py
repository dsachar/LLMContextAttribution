from backends import create_backend
import math
import itertools
from dataclasses import dataclass
from typing import List, Callable

@dataclass
class Example:
    question: str
    sentences: List[str]
    response: str

def load_model_and_tokenizer(model_name=None, backend=None):
    """Load a model and tokenizer using the specified backend.

    Parameters
    ----------
    model_name : str or None
        Model identifier. If None, uses the backend's default model.
    backend : Backend or None
        Backend instance. If None, auto-detects the best available backend.

    Returns
    -------
    tuple of (model, tokenizer, backend)
    """
    if backend is None:
        backend = create_backend()
    if model_name is None:
        model_name = backend.default_model
    model, tokenizer = backend.load_model(model_name)
    return model, tokenizer, backend

def format_prompt(tokenizer, question, sentences):
    context = " ".join(sentences)
    if context.strip():
        user_content = f"Question: {question}\n\nContext:\n{context}"
    else:
        user_content = f"Question: {question}"
        
    messages = [{"role": "user", "content": user_content}]
    
    if hasattr(tokenizer, "apply_chat_template"):
        prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    else:
        prompt = user_content + "\n\nAnswer:\n"
        
    return prompt

def compute_log_likelihood_unweighted(model, tokenizer, question, sentences, response, *, backend):
    prompt = format_prompt(tokenizer, question, sentences)
    prompt_tokens = tokenizer.encode(prompt)
    response_tokens = tokenizer.encode(response, add_special_tokens=False)
    if not response_tokens:
        return 0.0
    all_tokens = prompt_tokens + response_tokens
    logits = backend.forward(model, all_tokens)
    log_probs = backend.log_softmax(logits)
    ll = 0.0
    for i in range(len(prompt_tokens), len(all_tokens)):
        logit_idx = i - 1
        target_token = all_tokens[i]
        token_log_prob = backend.get_value(log_probs, 0, logit_idx, target_token)
        ll += token_log_prob
    return ll

def compute_log_likelihood(model, tokenizer, question, sentences, response, *, backend):
    """
    Computes the prefix-weighted log likelihood of 'response' given 'question' and 'sentences'.
    """
    prompt = format_prompt(tokenizer, question, sentences)
    prompt_tokens = tokenizer.encode(prompt)
    response_tokens = tokenizer.encode(response, add_special_tokens=False)
    
    if not response_tokens:
        return 0.0
        
    all_tokens = prompt_tokens + response_tokens
    logits = backend.forward(model, all_tokens)
    log_probs = backend.log_softmax(logits)
    
    N = len(response_tokens)
    ll = 0.0
    for i in range(len(prompt_tokens), len(all_tokens)):
        logit_idx = i - 1
        target_token = all_tokens[i]
        token_log_prob = backend.get_value(log_probs, 0, logit_idx, target_token)
        
        idx_in_response = i - len(prompt_tokens)
        weight = N - idx_in_response
        ll += weight * token_log_prob
        
    return ll

def compute_log_likelihood_wod_unweighted(model, tokenizer, question, sentences, response, *, backend, alpha=1.0):
    from collections import Counter
    context_text = " ".join(sentences)
    context_tokens = tokenizer.encode(context_text, add_special_tokens=False)
    token_counts = Counter(context_tokens)
    
    prompt = format_prompt(tokenizer, question, sentences)
    prompt_tokens = tokenizer.encode(prompt)
    response_tokens = tokenizer.encode(response, add_special_tokens=False)
    
    if not response_tokens:
        return 0.0
        
    all_tokens = prompt_tokens + response_tokens
    logits = backend.forward(model, all_tokens)
    log_probs = backend.log_softmax(logits)
    
    STOPWORDS = {"is", "the", "in", "of", "and", "a", "to", "are", "on", "at", "for", "with", "it", "this", "that", "an", "be"}
    PUNCTUATION = {".", ",", "?", "!", ";", ":", "-", "\"", "'", "(", ")", "[", "]", "{", "}"}
    
    ll = 0.0
    for i in range(len(prompt_tokens), len(all_tokens)):
        logit_idx = i - 1
        target_token = all_tokens[i]
        token_log_prob = backend.get_value(log_probs, 0, logit_idx, target_token)
        
        count = token_counts.get(target_token, 0)
        if count > 0:
            decoded = tokenizer.decode([target_token]).strip().lower()
            if decoded and decoded not in STOPWORDS and decoded not in PUNCTUATION and len(decoded) > 1:
                penalty = alpha * math.log(1 + count)
                token_log_prob -= penalty
                
        ll += token_log_prob
        
    return ll

def compute_log_likelihood_wod(model, tokenizer, question, sentences, response, *, backend, alpha=1.0):
    """
    Computes the Word-Overlap Discounted (WOD) log likelihood of 'response'
    given 'question' and 'sentences'.
    Subtracts a penalty from the logprob of tokens that are present in the context.
    """
    from collections import Counter
    context_text = " ".join(sentences)
    context_tokens = tokenizer.encode(context_text, add_special_tokens=False)
    token_counts = Counter(context_tokens)
    
    prompt = format_prompt(tokenizer, question, sentences)
    prompt_tokens = tokenizer.encode(prompt)
    response_tokens = tokenizer.encode(response, add_special_tokens=False)
    
    if not response_tokens:
        return 0.0
        
    all_tokens = prompt_tokens + response_tokens
    logits = backend.forward(model, all_tokens)
    log_probs = backend.log_softmax(logits)
    
    STOPWORDS = {"is", "the", "in", "of", "and", "a", "to", "are", "on", "at", "for", "with", "it", "this", "that", "an", "be"}
    PUNCTUATION = {".", ",", "?", "!", ";", ":", "-", "\"", "'", "(", ")", "[", "]", "{", "}"}
    
    N = len(response_tokens)
    ll = 0.0
    for i in range(len(prompt_tokens), len(all_tokens)):
        logit_idx = i - 1
        target_token = all_tokens[i]
        token_log_prob = backend.get_value(log_probs, 0, logit_idx, target_token)
        
        count = token_counts.get(target_token, 0)
        if count > 0:
            decoded = tokenizer.decode([target_token]).strip().lower()
            if decoded and decoded not in STOPWORDS and decoded not in PUNCTUATION and len(decoded) > 1:
                penalty = alpha * math.log(1 + count)
                token_log_prob -= penalty
                
        idx_in_response = i - len(prompt_tokens)
        weight = N - idx_in_response
        ll += weight * token_log_prob
        
    return ll

def get_overlap_words(sentences, response):
    import re
    context_text = " ".join(sentences).lower()
    context_words = set(re.findall(r'\b\w+\b', context_text))
    response_words = set(re.findall(r'\b\w+\b', response.lower()))
    
    STOPWORDS = {"is", "the", "in", "of", "and", "a", "to", "are", "on", "at", "for", "with", "it", "this", "that", "an", "be"}
    overlap = context_words.intersection(response_words) - STOPWORDS
    return sorted(list(overlap))

def compute_log_likelihood_bow_baseline(model, tokenizer, question, sentences, response, *, backend):
    overlap = get_overlap_words(sentences, response)
    if not overlap:
        return compute_log_likelihood(model, tokenizer, question, [], response, backend=backend)
    else:
        baseline_context = [" ".join(overlap)]
        return compute_log_likelihood(model, tokenizer, question, baseline_context, response, backend=backend)

def compute_log_likelihood_bow_baseline_unweighted(model, tokenizer, question, sentences, response, *, backend):
    overlap = get_overlap_words(sentences, response)
    if not overlap:
        return compute_log_likelihood_unweighted(model, tokenizer, question, [], response, backend=backend)
    else:
        baseline_context = [" ".join(overlap)]
        return compute_log_likelihood_unweighted(model, tokenizer, question, baseline_context, response, backend=backend)


_bert_model = None
_bert_tokenizer = None

def compute_llm_similarity(model, tokenizer, r_grand, r_coalition, *, backend):
    if r_grand.strip() == r_coalition.strip():
        return 1.0
    prompt = (
        "Instructions: Rate the semantic similarity between Response A and Response B on a scale from 0.0 to 1.0.\n"
        "A score of 1.0 means they express the exact same meaning/information.\n"
        "A score of 0.0 means they are completely unrelated.\n"
        "You must respond with ONLY a single float number between 0.0 and 1.0, and nothing else.\n\n"
        f"Response A: {r_grand}\n"
        f"Response B: {r_coalition}\n\n"
        "Similarity Score (0.0 to 1.0):"
    )
    messages = [{"role": "user", "content": prompt}]
    if hasattr(tokenizer, "apply_chat_template"):
        prompt_templated = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    else:
        prompt_templated = prompt + "\nScore: "
        
    out = backend.generate(model, tokenizer, prompt_templated, max_tokens=10)
    import re
    match = re.search(r"([0-9]*\.[0-9]+|[0-9]+)", out)
    if match:
        try:
            val = float(match.group(1))
            return min(max(val, 0.0), 1.0)
        except ValueError:
            pass
    return 0.5

def get_bert_similarity(r_grand, r_coalition, model_name="sentence-transformers/all-mpnet-base-v2"):
    global _bert_model, _bert_tokenizer
    if r_grand.strip() == r_coalition.strip():
        return 1.0
        
    try:
        import torch
    except ImportError:
        raise ImportError(
            "PyTorch (torch) is required for 'bert' similarity. "
            "Please run `pip install torch` or use v_type='similarity_llm_difference'."
        )
        
    from transformers import AutoTokenizer, AutoModel
    
    if _bert_model is None:
        _bert_tokenizer = AutoTokenizer.from_pretrained(model_name)
        _bert_model = AutoModel.from_pretrained(model_name)
        _bert_model.eval()
        
    inputs = _bert_tokenizer([r_grand, r_coalition], padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        outputs = _bert_model(**inputs)
        attention_mask = inputs['attention_mask']
        token_embeddings = outputs[0]
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        sum_embeddings = torch.sum(token_embeddings * input_mask_expanded, 1)
        sum_mask = torch.clamp(input_mask_expanded.sum(1), min=1e-9)
        embeddings = sum_embeddings / sum_mask
        
        cos = torch.nn.CosineSimilarity(dim=0)
        similarity = cos(embeddings[0], embeddings[1]).item()
        return float(similarity)

def compute_semantic_similarity(model, tokenizer, r_grand, r_coalition, v_type, *, backend, similarity_fn=None):
    if similarity_fn is not None:
        return similarity_fn(r_grand, r_coalition)
    if "llm" in v_type:
        return compute_llm_similarity(model, tokenizer, r_grand, r_coalition, backend=backend)
    else:
        return get_bert_similarity(r_grand, r_coalition)

def generate_response(model, tokenizer, prompt, *, backend, max_tokens=128):
    return backend.generate(model, tokenizer, prompt, max_tokens=max_tokens)

def compute_v(model, tokenizer, question, subset_sentences, response, empty_ll, *, backend, base_sentences=None, distractor=None, empty_ll_dist=None, v_type="logprob_difference", v_func=None, similarity_fn=None, max_gen_tokens=128, empty_sim=None):
    """
    Computes v(S) using the specified characteristic function type or custom function.
    
    v_type options:
      - "logprob_difference" (default): v(S) = LL(S) - LL(empty)
      - "probability_difference": v(S) = P(S) - P(empty)
      - "logprob": v(S) = LL(S)
      - "probability": v(S) = P(S)
      - "similarity_llm_difference": v(S) = sim_llm(R_grand, R_S) - sim_llm(R_grand, R_empty)
      - "similarity_llm": v(S) = sim_llm(R_grand, R_S)
      - "similarity_bert_difference": v(S) = sim_bert(R_grand, R_S) - sim_bert(R_grand, R_empty)
      - "similarity_bert": v(S) = sim_bert(R_grand, R_S)
      
    If distractor is provided, uses contrastive formulation.
    If |S| > 1, it averages the values over all permutations of S to avoid position bias.
    base_sentences are always prepended and never permuted.
    """
    if base_sentences is None:
        base_sentences = []
        
    is_similarity = v_type.startswith("similarity") or similarity_fn is not None
    
    if is_similarity:
        if not subset_sentences:
            raw_sim = empty_sim
        else:
            if len(subset_sentences) > 1:
                sims = []
                for perm in itertools.permutations(subset_sentences):
                    prompt = format_prompt(tokenizer, question, base_sentences + list(perm))
                    r_perm = generate_response(model, tokenizer, prompt, backend=backend, max_tokens=max_gen_tokens)
                    sims.append(compute_semantic_similarity(model, tokenizer, response, r_perm, v_type, backend=backend, similarity_fn=similarity_fn))
                raw_sim = sum(sims) / len(sims)
            else:
                prompt = format_prompt(tokenizer, question, base_sentences + list(subset_sentences))
                r_s = generate_response(model, tokenizer, prompt, backend=backend, max_tokens=max_gen_tokens)
                raw_sim = compute_semantic_similarity(model, tokenizer, response, r_s, v_type, backend=backend, similarity_fn=similarity_fn)
                
        if v_func is not None:
            return v_func(raw_sim, None, empty_sim, None)
            
        if "difference" in v_type or v_type == "similarity_difference":
            return raw_sim - empty_sim
        return raw_sim
    
    if not subset_sentences:
        if v_func is not None:
            return v_func(empty_ll, empty_ll_dist, empty_ll, empty_ll_dist)
        if v_type in ["logprob_difference", "probability_difference", "logprob_wod_difference", "logprob_bow_difference",
                      "logprob_unweighted_difference", "logprob_wod_unweighted_difference", "logprob_bow_unweighted_difference"]:
            return 0.0
        elif v_type == "logprob":
            if distractor is not None:
                return empty_ll - empty_ll_dist
            return empty_ll
        elif v_type == "probability":
            if distractor is not None:
                return math.exp(empty_ll) - math.exp(empty_ll_dist)
            return math.exp(empty_ll)
        else:
            raise ValueError(f"Unknown v_type: {v_type}")
    
    if len(subset_sentences) > 1:
        lls = []
        lls_dist = []
        for perm in itertools.permutations(subset_sentences):
            all_sents = base_sentences + list(perm)
            if v_type == "logprob_wod_difference":
                ll = compute_log_likelihood_wod(model, tokenizer, question, all_sents, response, backend=backend)
            elif v_type == "logprob_wod_unweighted_difference":
                ll = compute_log_likelihood_wod_unweighted(model, tokenizer, question, all_sents, response, backend=backend)
            elif v_type == "logprob_bow_difference":
                ll_std = compute_log_likelihood(model, tokenizer, question, all_sents, response, backend=backend)
                ll_base = compute_log_likelihood_bow_baseline(model, tokenizer, question, all_sents, response, backend=backend)
                ll = ll_std - ll_base
            elif v_type == "logprob_bow_unweighted_difference":
                ll_std = compute_log_likelihood_unweighted(model, tokenizer, question, all_sents, response, backend=backend)
                ll_base = compute_log_likelihood_bow_baseline_unweighted(model, tokenizer, question, all_sents, response, backend=backend)
                ll = ll_std - ll_base
            elif v_type == "logprob_unweighted_difference":
                ll = compute_log_likelihood_unweighted(model, tokenizer, question, all_sents, response, backend=backend)
            else:
                ll = compute_log_likelihood(model, tokenizer, question, all_sents, response, backend=backend)
            lls.append(ll)
            if distractor is not None:
                ll_d = compute_log_likelihood(model, tokenizer, question, all_sents, distractor, backend=backend)
                lls_dist.append(ll_d)
        ll = sum(lls) / len(lls)
        if distractor is not None:
            ll_dist = sum(lls_dist) / len(lls_dist)
        else:
            ll_dist = None
    else:
        all_sents = base_sentences + list(subset_sentences)
        if v_type == "logprob_wod_difference":
            ll = compute_log_likelihood_wod(model, tokenizer, question, all_sents, response, backend=backend)
        elif v_type == "logprob_wod_unweighted_difference":
            ll = compute_log_likelihood_wod_unweighted(model, tokenizer, question, all_sents, response, backend=backend)
        elif v_type == "logprob_bow_difference":
            ll_std = compute_log_likelihood(model, tokenizer, question, all_sents, response, backend=backend)
            ll_base = compute_log_likelihood_bow_baseline(model, tokenizer, question, all_sents, response, backend=backend)
            ll = ll_std - ll_base
        elif v_type == "logprob_bow_unweighted_difference":
            ll_std = compute_log_likelihood_unweighted(model, tokenizer, question, all_sents, response, backend=backend)
            ll_base = compute_log_likelihood_bow_baseline_unweighted(model, tokenizer, question, all_sents, response, backend=backend)
            ll = ll_std - ll_base
        elif v_type == "logprob_unweighted_difference":
            ll = compute_log_likelihood_unweighted(model, tokenizer, question, all_sents, response, backend=backend)
        else:
            ll = compute_log_likelihood(model, tokenizer, question, all_sents, response, backend=backend)
        if distractor is not None:
            ll_dist = compute_log_likelihood(model, tokenizer, question, all_sents, distractor, backend=backend)
        else:
            ll_dist = None
        
    if v_func is not None:
        return v_func(ll, ll_dist, empty_ll, empty_ll_dist)
        
    if v_type in ["logprob_difference", "logprob_wod_difference", "logprob_unweighted_difference", "logprob_wod_unweighted_difference"]:
        if distractor is not None:
            margin = ll - ll_dist
            base_margin = empty_ll - empty_ll_dist
            return margin - base_margin
        return ll - empty_ll
        
    elif v_type in ["logprob_bow_difference", "logprob_bow_unweighted_difference"]:
        return ll
        
    elif v_type == "probability_difference":
        if distractor is not None:
            margin = math.exp(ll) - math.exp(ll_dist)
            base_margin = math.exp(empty_ll) - math.exp(empty_ll_dist)
            return margin - base_margin
        return math.exp(ll) - math.exp(empty_ll)
        
    elif v_type == "logprob":
        if distractor is not None:
            return ll - ll_dist
        return ll
        
    elif v_type == "probability":
        if distractor is not None:
            return math.exp(ll) - math.exp(ll_dist)
        return math.exp(ll)
        
    else:
        raise ValueError(f"Unknown v_type: {v_type}")

def compute_attribution(
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
    method="shapley",
):
    """Computes context attribution using the specified method."""
    from methods import ATTRIBUTION_METHODS, AttributionMethod

    if isinstance(method, str):
        method_name = method.lower()
        if method_name not in ATTRIBUTION_METHODS:
            raise ValueError(f"Unknown attribution method '{method}'. Choose from: {list(ATTRIBUTION_METHODS.keys())}")
        method_instance = ATTRIBUTION_METHODS[method_name]()
    elif isinstance(method, AttributionMethod):
        method_instance = method
    elif hasattr(method, "attribute"):
        method_instance = method
    else:
        raise TypeError("method must be a string (key in registry), an instance of AttributionMethod, or an object with an 'attribute' method.")

    return method_instance.attribute(
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
