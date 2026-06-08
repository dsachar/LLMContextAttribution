import sys
import os
import re
import math
import argparse

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from attribution import load_model_and_tokenizer, compute_attribution, save_cache
from biases.eval_rules import evaluate_example


def parse_examples_markdown(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Markdown file not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    examples = []
    current_ex = None

    # Matches lines like: ### Example 1: Astronomy / Planet
    header_pattern = re.compile(r"^##+\s+Example\s+(\d+):\s*(.+)$")
    # Matches lines like: - **Question**: "What chemical..."
    field_pattern = re.compile(r"^-\s*\*\*(Question|Target Response|S1|S2|S3a \(Adversarial\)|S3b \(Syntactic\)|S3c \(Semantic\))\*\*:\s*(.*)$")

    for line in lines:
        line_str = line.strip()
        if not line_str:
            continue

        header_match = header_pattern.match(line_str)
        if header_match:
            if current_ex:
                examples.append(current_ex)
            current_ex = {
                "id": int(header_match.group(1)),
                "name": header_match.group(2).strip(),
                "distractors": {}
            }
            continue

        if current_ex is None:
            continue

        field_match = field_pattern.match(line_str)
        if field_match:
            field_name = field_match.group(1)
            val = field_match.group(2).strip()

            # Clean up outer quotes if they exist
            if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                val = val[1:-1].strip()

            if field_name == "Question":
                current_ex["question"] = val
            elif field_name == "Target Response":
                current_ex["target_resp"] = val
            elif field_name == "S1":
                current_ex["s1"] = val
            elif field_name == "S2":
                current_ex["s2"] = val
            elif "S3a" in field_name:
                current_ex["distractors"]["a"] = val
            elif "S3b" in field_name:
                current_ex["distractors"]["b"] = val
            elif "S3c" in field_name:
                current_ex["distractors"]["c"] = val

    if current_ex:
        examples.append(current_ex)

    # Validate that all required fields are present
    required_fields = ["question", "target_resp", "s1", "s2"]
    for ex in examples:
        for fld in required_fields:
            if fld not in ex:
                raise ValueError(f"Example {ex.get('id', 'unknown')} is missing required field: {fld}")
        for case in ["a", "b", "c"]:
            if case not in ex["distractors"]:
                raise ValueError(f"Example {ex['id']} is missing distractor case: S3{case}")

    return examples


def get_generated_responses(tokenizer, question, sentences):
    import itertools
    from attribution import format_prompt, _PERSISTENT_CACHE
    
    subsets = {
        "Empty": [],
        "S1 Only": [sentences[0]],
        "S2 Only": [sentences[1]],
        "S3 Only": [sentences[2]],
        "S1, S2": [sentences[0], sentences[1]],
        "S1, S3": [sentences[0], sentences[2]],
        "S2, S3": [sentences[1], sentences[2]],
        "S1, S2, S3": sentences
    }
    
    responses = {}
    for name, subset in subsets.items():
        if not subset:
            prompt = format_prompt(tokenizer, question, [])
            cache_key = f"generate::{prompt}::48"
            gen = _PERSISTENT_CACHE.get(cache_key, "(not found)")
            responses[name] = {"": gen}
        elif len(subset) == 1:
            prompt = format_prompt(tokenizer, question, subset)
            cache_key = f"generate::{prompt}::48"
            gen = _PERSISTENT_CACHE.get(cache_key, "(not found)")
            responses[name] = {"": gen}
        else:
            perms_dict = {}
            for perm in itertools.permutations(subset):
                prompt = format_prompt(tokenizer, question, list(perm))
                cache_key = f"generate::{prompt}::48"
                gen = _PERSISTENT_CACHE.get(cache_key, "(not found)")
                
                perm_names = []
                for s in perm:
                    if s == sentences[0]:
                        perm_names.append("S1")
                    elif s == sentences[1]:
                        perm_names.append("S2")
                    else:
                        perm_names.append("S3")
                perm_key = ", ".join(perm_names)
                perms_dict[perm_key] = gen
            responses[name] = perms_dict
            
    return responses


def main():
    parser = argparse.ArgumentParser(description="Evaluate synthetic examples from a markdown file.")
    parser.add_argument("input_file", help="Path to the input markdown file (e.g. biases/examples_v1.md)")
    args = parser.parse_args()

    input_path = args.input_file
    if not input_path.endswith(".md"):
        print("Error: Input file must be a markdown (.md) file.")
        sys.exit(1)

    # Determine output path: examples_vx.md -> examples_vx_eval.md
    dir_name = os.path.dirname(input_path)
    base_name = os.path.basename(input_path)
    base_no_ext, ext = os.path.splitext(base_name)
    output_path = os.path.join(dir_name, f"{base_no_ext}_eval{ext}")

    print(f"Reading examples from: {input_path}")
    try:
        examples = parse_examples_markdown(input_path)
    except Exception as e:
        print(f"Failed to parse markdown: {e}")
        sys.exit(1)

    print(f"Parsed {len(examples)} examples successfully.")
    
    print("Loading model and tokenizer...", flush=True)
    model, tokenizer, backend = load_model_and_tokenizer("mlx-community/gemma-2-9b-it-4bit")
    print("Loaded model successfully.", flush=True)

    methods = {
        "Unweighted LL": "logprob_unweighted_difference",
        "BERT Similarity": "similarity_bert_difference"
    }

    all_results = {}
    total_examples = len(examples)

    for ex_idx, ex in enumerate(examples):
        ex_id = ex["id"]
        all_results[ex_id] = {}

        print(f"--- Processing Example {ex_id}/{total_examples}: {ex['name']} ---", flush=True)

        for case_key, s3_text in ex["distractors"].items():
            print(f"  Running Case {case_key.upper()}...", flush=True)
            all_results[ex_id][case_key] = {}
            sentences = [ex["s1"], ex["s2"], s3_text]

            for m_name, v_type in methods.items():
                print(f"    Evaluating Method: {m_name}", flush=True)
                try:
                    res = compute_attribution(
                        model, tokenizer, ex["question"], sentences,
                        response=ex["target_resp"], v_type=v_type,
                        backend=backend, max_gen_tokens=48
                    )
                    all_results[ex_id][case_key][m_name] = {
                        "phi_normalized_1": res.get("phi_normalized_1", 1.0/3.0),
                        "phi_normalized_2": res.get("phi_normalized_2", 1.0/3.0),
                        "phi_normalized_3": res.get("phi_normalized_3", 1.0/3.0)
                    }
                except Exception as e:
                    print(f"      ERROR running {m_name}: {e}", flush=True)
                    all_results[ex_id][case_key][m_name] = {
                        "phi_normalized_1": 0.0, "phi_normalized_2": 0.0, "phi_normalized_3": 0.0
                    }
        print(f"--- Example {ex_id} ({ex['name']}) fully processed. ---\n", flush=True)
        save_cache()

    # Pre-calculate diagnostics for all examples to print them in the summary table
    diagnostics = {}
    for ex in examples:
        ex_id = ex["id"]

        def get_vals(case, method):
            r = all_results[ex_id][case].get(method, {"phi_normalized_1": 0.0, "phi_normalized_2": 0.0, "phi_normalized_3": 0.0})
            return (r["phi_normalized_1"], r["phi_normalized_2"], r["phi_normalized_3"])

        ull_b = get_vals("b", "Unweighted LL")
        bert_b = get_vals("b", "BERT Similarity")
        ull_c = get_vals("c", "Unweighted LL")
        bert_c = get_vals("c", "BERT Similarity")

        passed_all, score, checks = evaluate_example(ull_b, bert_b, ull_c, bert_c)
        diagnostics[ex_id] = {
            "passed_all": passed_all,
            "score": score,
            "checks": checks,
            "checks_passed": sum(1 for passed, _ in checks if passed),
            "checks_total": len(checks)
        }

    print(f"Writing evaluation report to: {output_path}", flush=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# Evaluation Results: {base_name}\n\n")
        f.write(f"Evaluation of the {len(examples)} examples using Gemma-2-9B-IT.\n\n")

        f.write("## Per-Example Diagnostic Summary\n\n")
        f.write("| Example | ULL S3(B) | ULL S3(C) | ULL Margin | BERT S3(B) | BERT S3(C) | BERT Margin | Checks Passed | Quality Score | Good? |\n")
        f.write("| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n")

        for ex in examples:
            ex_id = ex["id"]
            ull_b = all_results[ex_id]["b"].get("Unweighted LL", {}).get("phi_normalized_3", 0.0)
            ull_c = all_results[ex_id]["c"].get("Unweighted LL", {}).get("phi_normalized_3", 0.0)
            bert_b = all_results[ex_id]["b"].get("BERT Similarity", {}).get("phi_normalized_3", 0.0)
            bert_c = all_results[ex_id]["c"].get("BERT Similarity", {}).get("phi_normalized_3", 0.0)
            ull_margin = ull_b - ull_c
            bert_margin = bert_c - bert_b

            diag = diagnostics[ex_id]
            good_str = "Yes ✅" if diag["passed_all"] else "No ❌"
            f.write(f"| {ex['name']} | {ull_b:.4f} | {ull_c:.4f} | {ull_margin:+.4f} | {bert_b:.4f} | {bert_c:.4f} | {bert_margin:+.4f} | {diag['checks_passed']}/{diag['checks_total']} | {diag['score']:.4f} | {good_str} |\n")
        f.write("\n")

        f.write("## Individual Example Results\n\n")
        for ex in examples:
            ex_id = ex["id"]
            diag = diagnostics[ex_id]
            status_suffix = "✅ (Good)" if diag["passed_all"] else "❌ (Failed)"
            f.write(f"### {ex['name']} (Example {ex_id}) — {diag['checks_passed']}/{diag['checks_total']} checks passed {status_suffix}\n")
            f.write(f"**Quality score**: {diag['score']:.4f}\n\n")

            f.write("**Diagnostic checks:**\n")
            for passed, description in diag["checks"]:
                icon = "✅" if passed else "❌"
                f.write(f"- {icon} {description}\n")
            f.write("\n")

            f.write(f"- **Q**: *\"{ex['question']}\"*\n")
            f.write(f"- **R**: *\"{ex['target_resp']}\"*\n")
            f.write(f"- **S1**: *\"{ex['s1']}\"*\n")
            f.write(f"- **S2**: *\"{ex['s2']}\"*\n\n")

            for case_key, case_name in [("a", "Adversarial Distractor"), ("b", "Syntactic Distractor"), ("c", "Semantic Distractor")]:
                f.write(f"#### Case {case_key.upper()} ({case_name})\n")
                f.write(f"- **S3**: *\"{ex['distractors'][case_key]}\"*\n\n")

                f.write("| Method | S1 ($\\phi_{\\text{norm}, 1}$) | S2 ($\\phi_{\\text{norm}, 2}$) | S3 ($\\phi_{\\text{norm}, 3}$) |\n")
                f.write("| :--- | :---: | :---: | :---: |\n")

                for m_name in methods.keys():
                    res = all_results[ex_id][case_key].get(m_name, {"phi_normalized_1": 0.0, "phi_normalized_2": 0.0, "phi_normalized_3": 0.0})
                    f.write(f"| {m_name} | {res['phi_normalized_1']:.4f} | {res['phi_normalized_2']:.4f} | {res['phi_normalized_3']:.4f} |\n")
                f.write("\n")

                f.write("##### Generated Responses per Coalition:\n")
                sentences = [ex["s1"], ex["s2"], ex["distractors"][case_key]]
                resps = get_generated_responses(tokenizer, ex["question"], sentences)
                for name, perms in resps.items():
                    if len(perms) == 1:
                        gen_val = list(perms.values())[0].replace("<end_of_turn>", "").replace("\n", " ").strip()
                        f.write(f"- **{name}**: `\"{gen_val}\"`\n")
                    else:
                        f.write(f"- **{name}**:\n")
                        for perm_key, gen_val in perms.items():
                            gen_val_clean = gen_val.replace("<end_of_turn>", "").replace("\n", " ").strip()
                            f.write(f"  - `[{perm_key}]`: `\"{gen_val_clean}\"`\n")
                f.write("\n")
            f.write("---\n\n")

    print(f"Done! Results written successfully to {output_path}.", flush=True)


if __name__ == "__main__":
    main()
