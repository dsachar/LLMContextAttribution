"""
Backend abstraction for cross-platform model inference.

Provides a uniform interface for model loading, forward passes, and text
generation so that the attribution logic in attribution.py remains
framework-agnostic.

Usage:
    from backends import create_backend
    backend = create_backend()            # auto-detect best available
    backend = create_backend("mlx")       # force MLX
    backend = create_backend("pytorch")   # force PyTorch
"""

import sys

# ---------------------------------------------------------------------------
# Well-known model name mappings: MLX repo  <->  HuggingFace repo
# ---------------------------------------------------------------------------
_MODEL_MAP_MLX_TO_HF = {
    "mlx-community/gemma-2-2b-it-4bit": "google/gemma-2-2b-it",
    "mlx-community/gemma-2-9b-it-4bit": "google/gemma-2-9b-it",
    "mlx-community/Qwen2.5-0.5B-Instruct-4bit": "Qwen/Qwen2.5-0.5B-Instruct",
}
_MODEL_MAP_HF_TO_MLX = {v: k for k, v in _MODEL_MAP_MLX_TO_HF.items()}


def _translate_model_name(model_name, target_backend):
    """Translate a model name to the format expected by *target_backend*.

    If the name is already in the right format or no mapping exists, return
    the name unchanged.
    """
    if target_backend == "mlx":
        return _MODEL_MAP_HF_TO_MLX.get(model_name, model_name)
    else:  # pytorch
        return _MODEL_MAP_MLX_TO_HF.get(model_name, model_name)


# =========================================================================
# MLX Backend
# =========================================================================
class MLXBackend:
    """Backend using Apple's MLX framework (macOS only)."""

    name = "mlx"
    default_model = "mlx-community/gemma-2-2b-it-4bit"

    def load_model(self, model_name):
        from mlx_lm import load
        model_name = _translate_model_name(model_name, self.name)
        model, tokenizer = load(model_name)
        return model, tokenizer

    def forward(self, model, token_ids):
        """Run forward pass. Returns logits with shape [1, seq_len, vocab]."""
        import mlx.core as mx
        x = mx.array(token_ids)[None]
        return model(x)

    def log_softmax(self, logits):
        """Compute log-softmax along the last axis."""
        import mlx.core as mx
        return logits - mx.logsumexp(logits, axis=-1, keepdims=True)

    def get_value(self, tensor, batch, seq, tok):
        """Index into a tensor and return a Python float."""
        return tensor[batch, seq, tok].item()

    def generate(self, model, tokenizer, prompt, max_tokens=128):
        from mlx_lm import generate
        return generate(model, tokenizer, prompt, max_tokens=max_tokens, verbose=False)


# =========================================================================
# PyTorch / HuggingFace Backend
# =========================================================================
class PyTorchBackend:
    """Backend using PyTorch + HuggingFace Transformers (Linux/Windows/macOS)."""

    name = "pytorch"
    default_model = "google/gemma-2-2b-it"

    def __init__(self):
        self._device = None

    @property
    def device(self):
        if self._device is None:
            import torch
            if torch.cuda.is_available():
                self._device = torch.device("cuda")
            elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
                self._device = torch.device("mps")
            else:
                self._device = torch.device("cpu")
        return self._device

    def load_model(self, model_name):
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer

        model_name = _translate_model_name(model_name, self.name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16 if self.device.type != "cpu" else torch.float32,
            device_map="auto",
        )
        model.eval()
        return model, tokenizer

    def forward(self, model, token_ids):
        """Run forward pass. Returns logits with shape [1, seq_len, vocab]."""
        import torch
        x = torch.tensor([token_ids], dtype=torch.long, device=self.device)
        with torch.no_grad():
            outputs = model(x)
        return outputs.logits  # [1, seq_len, vocab]

    def log_softmax(self, logits):
        """Compute log-softmax along the last axis."""
        import torch
        return torch.log_softmax(logits, dim=-1)

    def get_value(self, tensor, batch, seq, tok):
        """Index into a tensor and return a Python float."""
        return tensor[batch, seq, tok].item()

    def generate(self, model, tokenizer, prompt, max_tokens=128):
        import torch

        inputs = tokenizer(prompt, return_tensors="pt").to(self.device)
        with torch.no_grad():
            output_ids = model.generate(
                **inputs,
                max_new_tokens=max_tokens,
                do_sample=False,
            )
        # Decode only the newly generated tokens
        new_tokens = output_ids[0, inputs["input_ids"].shape[1]:]
        return tokenizer.decode(new_tokens, skip_special_tokens=True)


# =========================================================================
# Factory
# =========================================================================
_BACKENDS = {
    "mlx": MLXBackend,
    "pytorch": PyTorchBackend,
}


def create_backend(name=None):
    """Create and return a backend instance.

    Parameters
    ----------
    name : str or None
        ``"mlx"``, ``"pytorch"``, or ``None`` for auto-detection.
        Auto-detection tries MLX first (macOS-only), then falls back to PyTorch.

    Returns
    -------
    MLXBackend or PyTorchBackend
    """
    if name is not None:
        name = name.lower()
        if name not in _BACKENDS:
            raise ValueError(f"Unknown backend '{name}'. Choose from: {list(_BACKENDS.keys())}")
        return _BACKENDS[name]()

    # Auto-detect
    if sys.platform == "darwin":
        try:
            import mlx.core  # noqa: F401
            return MLXBackend()
        except ImportError:
            pass

    try:
        import torch  # noqa: F401
        return PyTorchBackend()
    except ImportError:
        pass

    raise RuntimeError(
        "No supported backend found. Install either:\n"
        "  • mlx + mlx-lm    (macOS with Apple Silicon)\n"
        "  • torch + transformers  (any platform)\n"
    )
