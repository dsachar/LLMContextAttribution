# Rules defining what constitutes a "good result" for LLM context attribution.

# Reject examples where any normalized attribution has |value| > this.
MAX_ABSOLUTE_VALUE = 1.5

# Tolerance for "comparable". When we say S3 should be "at least comparable
# with the best of S1/S2", we mean S3 >= max(S1, S2) - FOOLED_TOLERANCE.
# When we say S3 should be "at most comparable with the worst of S1/S2",
# we mean S3 <= min(S1, S2) + FOOLED_TOLERANCE.
FOOLED_TOLERANCE = 0.15


def evaluate_example(ull_b, bert_b, ull_c, bert_c):
    """
    Evaluate an example against the "good result" criteria.

    Parameters
    ----------
    ull_b : tuple of (float, float, float)
        S1, S2, S3 normalized attributions for Case B (Syntactic Distractor) under Unweighted LL.
    bert_b : tuple of (float, float, float)
        S1, S2, S3 normalized attributions for Case B (Syntactic Distractor) under BERT Similarity.
    ull_c : tuple of (float, float, float)
        S1, S2, S3 normalized attributions for Case C (Semantic Distractor) under Unweighted LL.
    bert_c : tuple of (float, float, float)
        S1, S2, S3 normalized attributions for Case C (Semantic Distractor) under BERT Similarity.

    Returns
    -------
    passed_all : bool
        True if all 5 diagnostic checks pass.
    score : float
        Quality score (sum of margins). Higher is better.
    checks : list of tuple (bool, str)
        List of checks where each entry is (passed, description).
    """
    all_values = list(ull_b) + list(bert_b) + list(ull_c) + list(bert_c)
    checks = []
    passed_all = True

    # ------------------------------------------------------------------
    # 1. No extreme values
    # ------------------------------------------------------------------
    extremes = [v for v in all_values if abs(v) > MAX_ABSOLUTE_VALUE]
    if extremes:
        checks.append((False, f"Extreme value(s) detected: {[f'{v:.4f}' for v in extremes]} (|v| > {MAX_ABSOLUTE_VALUE})"))
        passed_all = False
    else:
        checks.append((True, f"All values within [-{MAX_ABSOLUTE_VALUE}, {MAX_ABSOLUTE_VALUE}]"))

    # ------------------------------------------------------------------
    # 2. Case B — ULL fooled: S3 high (>= best of S1/S2 - tolerance)
    # ------------------------------------------------------------------
    ull_b_best = max(ull_b[0], ull_b[1])
    ull_b_threshold = ull_b_best - FOOLED_TOLERANCE
    if ull_b[2] >= ull_b_threshold:
        checks.append((True, f"Case B ULL fooled: S3={ull_b[2]:.4f} >= best(S1,S2)={ull_b_best:.4f} - {FOOLED_TOLERANCE}"))
    else:
        checks.append((False, f"Case B ULL NOT fooled: S3={ull_b[2]:.4f} < best(S1,S2)={ull_b_best:.4f} - {FOOLED_TOLERANCE} = {ull_b_threshold:.4f}"))
        passed_all = False

    # ------------------------------------------------------------------
    # 3. Case B — BERT not fooled: S3 low (<= worst of S1/S2 + tolerance)
    # ------------------------------------------------------------------
    bert_b_worst = min(bert_b[0], bert_b[1])
    bert_b_threshold = bert_b_worst + FOOLED_TOLERANCE
    if bert_b[2] <= bert_b_threshold:
        checks.append((True, f"Case B BERT not fooled: S3={bert_b[2]:.4f} <= worst(S1,S2)={bert_b_worst:.4f} + {FOOLED_TOLERANCE}"))
    else:
        checks.append((False, f"Case B BERT fooled (bad): S3={bert_b[2]:.4f} > worst(S1,S2)={bert_b_worst:.4f} + {FOOLED_TOLERANCE} = {bert_b_threshold:.4f}"))
        passed_all = False

    # ------------------------------------------------------------------
    # 4. Case C — BERT fooled: S3 high (>= best of S1/S2 - tolerance)
    # ------------------------------------------------------------------
    bert_c_best = max(bert_c[0], bert_c[1])
    bert_c_threshold = bert_c_best - FOOLED_TOLERANCE
    if bert_c[2] >= bert_c_threshold:
        checks.append((True, f"Case C BERT fooled: S3={bert_c[2]:.4f} >= best(S1,S2)={bert_c_best:.4f} - {FOOLED_TOLERANCE}"))
    else:
        checks.append((False, f"Case C BERT NOT fooled: S3={bert_c[2]:.4f} < best(S1,S2)={bert_c_best:.4f} - {FOOLED_TOLERANCE} = {bert_c_threshold:.4f}"))
        passed_all = False

    # ------------------------------------------------------------------
    # 5. Case C — ULL not fooled: S3 low (<= worst of S1/S2 + tolerance)
    # ------------------------------------------------------------------
    ull_c_worst = min(ull_c[0], ull_c[1])
    ull_c_threshold = ull_c_worst + FOOLED_TOLERANCE
    if ull_c[2] <= ull_c_threshold:
        checks.append((True, f"Case C ULL not fooled: S3={ull_c[2]:.4f} <= worst(S1,S2)={ull_c_worst:.4f} + {FOOLED_TOLERANCE}"))
    else:
        checks.append((False, f"Case C ULL fooled (bad): S3={ull_c[2]:.4f} > worst(S1,S2)={ull_c_worst:.4f} + {FOOLED_TOLERANCE} = {ull_c_threshold:.4f}"))
        passed_all = False

    # ------------------------------------------------------------------
    # Compute quality score
    # ------------------------------------------------------------------
    ull_fooled_margin = ull_b[2] - ull_b_best          # Case B: S3 vs best(S1,S2)
    bert_not_fooled_margin = bert_b_worst - bert_b[2]  # Case B: worst(S1,S2) vs S3
    bert_fooled_margin = bert_c[2] - bert_c_best       # Case C: S3 vs best(S1,S2)
    ull_not_fooled_margin = ull_c_worst - ull_c[2]      # Case C: worst(S1,S2) vs S3

    score = (ull_fooled_margin + bert_not_fooled_margin +
             bert_fooled_margin + ull_not_fooled_margin)

    return passed_all, score, checks
