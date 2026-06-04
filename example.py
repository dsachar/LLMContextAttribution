from attribution import load_model_and_tokenizer, compute_attribution
from backends import create_backend

def run_example():
    # 1. Load the model and tokenizer using the PyTorch/HuggingFace backend
    model_name = "google/gemma-2-2b-it"
    print(f"Loading {model_name} via PyTorch/HuggingFace...")
    backend = create_backend("pytorch")
    model, tokenizer, backend = load_model_and_tokenizer(model_name, backend=backend)
    
    # 2. Define the QA setup (The Study Room Example)
    question = "In which room is the treasure hidden? Answer in one sentence and use only the context provided."
    response = "The treasure is hidden in the study room."
    
    s1 = "The treasure is the first edition of the bible."
    s2 = "All books are located in the study room."
    s3b = "The study room is nicely decorated."  # Syntactic distractor
    
    sentences = [s1, s2, s3b]
    
    print("\n--- Example Setup ---")
    print(f"Question : {question}")
    print(f"Response : {response}")
    print(f"Context Sentences:")
    print(f"  S1: {s1} (Cooperative Core)")
    print(f"  S2: {s2} (Cooperative Core)")
    print(f"  S3: {s3b} (Syntactic Distractor)")
    
    # 3. Compute attribution using log-likelihood difference and Shapley values
    print("\nComputing Shapley values...")
    results = compute_attribution(
        model=model,
        tokenizer=tokenizer,
        question=question,
        sentences=sentences,
        response=response,
        backend=backend,
        v_type="logprob_difference",
        method="shapley"
    )
    
    # 4. Print results
    print("\n--- Results ---")
    for i in range(1, 4):
        val = results[f"phi_{i}"]
        norm_val = results[f"phi_normalized_{i}"]
        print(f"Sentence {i} Shapley Value : {val:.4f} (Normalized: {norm_val:.4f})")

if __name__ == "__main__":
    run_example()
