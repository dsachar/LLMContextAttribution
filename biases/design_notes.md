# Design Notes: Synthetic Context Attribution Benchmark

This document outlines the core definitions, diagnostic rules, and design principles for creating synthetic examples that pass the context attribution diagnostics.

---

## Core Definitions

Each benchmark example consists of:
*   **Question (Q)**: The query posed to the model.
*   **Target Response (R)**: The correct answer containing the specific target entity.
*   **Logical Premises (S1, S2)**: Two discrete pieces of the puzzle that are collectively required to answer Q. Neither S1 nor S2 alone should be sufficient to answer Q.
*   **Adversarial Distractor (S3a)**: A fact that is completely unrelated to Q and R, establishing a baseline.
*   **Syntactic Distractor (S3b)**: Mentions the target entity but in a context semantically irrelevant to Q/R. It primes the token probability (fools Unweighted Log-Likelihood) but does not match the meaning (does not fool BERT).
*   **Semantic Distractor (S3c)**: Semantically close to the target response (R) itself, describing the action/event of R but omitting the target entity name so it does not give the answer away. It matches the meaning (fools BERT) but does not prime the exact tokens (does not fool ULL).

---

## The 5 Diagnostic Rules

Diagnostic checks evaluate the normalized Shapley values of $S_1, S_2, S_3$ under two value functions: **ULL** (Unweighted Log-Likelihood of R) and **BERT Similarity** (semantic similarity of the model's generated response to R).

| Rule | Case | Check | What It Means |
| :--- | :--- | :--- | :--- |
| **1** | All | $|v| \le 1.5$ for all normalized values | No extreme/degenerate attributions. |
| **2** | B (Syntactic) | $\text{ULL}(S_{3b}) \ge \max(\text{ULL}(S_1), \text{ULL}(S_2)) - 0.15$ | $S_{3b}$ fools ULL (entity name primes token prob). |
| **3** | B (Syntactic) | $\text{BERT}(S_{3b}) \le \min(\text{BERT}(S_1), \text{BERT}(S_2)) + 0.15$ | $S_{3b}$ does not fool BERT (meaning is irrelevant). |
| **4** | C (Semantic) | $\text{BERT}(S_{3c}) \ge \max(\text{BERT}(S_1), \text{BERT}(S_2)) - 0.15$ | $S_{3c}$ fools BERT (describes the same event). |
| **5** | C (Semantic) | $\text{ULL}(S_{3c}) \le \min(\text{ULL}(S_1), \text{ULL}(S_2)) + 0.15$ | $S_{3c}$ does not fool ULL (different surface tokens). |

---

## General Intuition & What Works

### 1. S1/S2 Balance (Avoiding Dominance)
If one premise dominates (typically $S_2$ containing the entity link), its Shapley value becomes extremely high. Under Rule 2, the threshold for $S_{3b}$ to pass becomes unreachable ($S_{3b} \ge \max(S_1, S_2) - 0.15$). 
*   **Fix**: Structure the question and premises so that the model must combine both discrete pieces to answer. Avoid background knowledge leaks in $S_2$ that allow the model to guess the answer independently.

### 2. S3b (Syntactic Distractor) Design
Simply stating that the entity "is stored in a box" works for fictional entities, but fails for common real-world entities.
*   **What works**: Use an action-oriented sentence with **structural parallelism** to the target response (e.g., using the same verb as R but with a different object/context). This drives ULL up without raising BERT.

### 3. S3c (Semantic Distractor) Design
To fool BERT (Rule 4), $S_{3c}$ must be close to the target response (R) itself rather than S1. 
*   **What works**: Write $S_{3c}$ to describe the exact action/outcome of R, but replace the entity name with a generic category descriptor (e.g., Q: "Which weapon pierced the armor?", R: "The crossbow pierced...", $S_{3c}$: "A mechanical bolt-launching weapon pierced the knight's armor during the battle").
*   **Crucial constraint**: Avoid leaking specific target tokens or keywords from R (like "coronation", "crucible") into $S_{3c}$, which would cause a ULL leak and violate Rule 5.

### 4. Fictional vs. Real-World Entities
*   **Fictional Entities** (e.g., `Compound NP-8`, `Strain H7-Alpha`) are highly robust because the model has no pre-training associations with them. The mere presence of the unique tokens in $S_{3b}$ provides strong ULL priming.
*   **Real-world Entities** (e.g., `Saturn`, `microwave`) are more challenging because they carry background knowledge. S2 dominance is harder to avoid, and S3b requires active, domain-relevant contexts.

---

## Common Pitfalls

1.  **ULL Token Leakage in S3c**: Reusing distinct words from R in S3c makes the model generate R's exact tokens, violating Rule 5.
2.  **Over-dominant S2**: S2 is too informative on its own, pushing the Rule 2 threshold too high.
3.  **Vague S3c**: Making S3c too generic or detached from R's action prevents the model from generating a semantically similar response, violating Rule 4.
4.  **Static S3b for Real Entities**: Using "is stored in..." or "is a..." for real-world entities provides insufficient ULL priming. Use action-oriented context instead.

---

## Strategy for Discovering More Examples

When expanding the benchmark, follow this step-by-step methodology to discover and refine passing examples:

### 1. Focus on Specialized/Narrow Domains
Brainstorm fields with highly specific terminology (e.g., Seismology, Therapeutics, Cryptography, Acoustics). In these domains:
*   **S1** can define the general concept or category (e.g., *a compressional longitudinal wave*).
*   **S2** establishes the link to the target entity (e.g., *the only compressional longitudinal wave is the primary wave*).
The narrow mapping prevents S2 from dominating, keeping the Shapley values balanced.

### 2. Leverage Fictional Identifiers
If a real-world entity (e.g., *Saturn*, *beaver*) persistently fails due to S2 dominance from pre-training associations, use fictional identifiers or codes (e.g., *Runner 104*, *Flight Alpha-9*, *Module AC-4*, *Agent GL-4*). This guarantees that the model must rely strictly on S1 and S2 to answer the question, avoiding pre-training bias.

### 3. Debugging Failed Diagnostic Rules
If a drafted example fails during evaluation, check the specific rule violation to apply the appropriate fix:
*   **Rule 2 Fails (Case B ULL not fooled)**: S3b needs stronger target entity token-priming. Make S3b longer or more descriptive, using the target entity name near the end or in a similar syntactic structure to R.
*   **Rule 3 Fails (Case B BERT fooled)**: S3b is semantically too close to R. Change the action in S3b to be completely unrelated to the event in R.
*   **Rule 4 Fails (Case C BERT not fooled)**: S3c is too vague or fails to match the action in R. Rewrite S3c to mirror the main action, verb, and outcome of R, only substituting the entity name.
*   **Rule 5 Fails (Case C ULL fooled)**: S3c is leaking tokens from R. Scan S3c and remove/replace any distinct keywords that also appear in R.

---

## Evaluation Scripts & Input Structure

### 1. Python Scripts
*   **[`eval_rules.py`](file:///Users/dimitris/Documents/code/python/shapley/biases/eval_rules.py)**: Contains the implementation of the 5 diagnostic checks. It receives the normalized Shapley values from case B (syntactic) and case C (semantic) under the ULL and BERT Similarity value functions and determines if the example passes all criteria, calculating a consolidated quality score.
*   **[`run_eval.py`](file:///Users/dimitris/Documents/code/python/shapley/biases/run_eval.py)**: The main runner script. It parses an input markdown file of synthetic examples, loads the target model (`mlx-community/gemma-2-9b-it-4bit`), runs the attribution pipeline sequentially (utilizing `llm_cache.json` caching to avoid redundant model inferences), logs the generated response for all coalition subsets, applies the diagnostic checks, and writes a detailed evaluation report.

### 2. Expected Input Markdown Structure
The runner parses markdown files based on regex matches. The input file (e.g. `final_examples.md`) must adhere to the following structure:
*   Each example block begins with a header (level 3 or more): `### Example {ID}: {Domain / Title}`.
*   Followed by a bulleted list where keys and format must match exactly:
    *   `- **Question**: "The question text..."`
    *   `- **Target Response**: "The target response..."`
    *   `- **S1**: "The first logical premise..."`
    *   `- **S2**: "The second logical premise..."`
    *   `- **S3a (Adversarial)**: "The adversarial distractor..."`
    *   `- **S3b (Syntactic)**: "The syntactic distractor..."`
    *   `- **S3c (Semantic)**: "The semantic distractor..."`
*   Each example block is separated by a horizontal rule `---`.


