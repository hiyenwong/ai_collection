---
name: self-policy-distillation-spd
description: "Self-Policy Distillation (SPD) methodology from arXiv:2605.22675 (May 2026). Capability-selective self-distillation by extracting low-rank subspace from gradients on correctness-defining tokens, projecting KV activations during self-generation, and fine-tuning with standard NTP loss. No external signals needed. Use when: self-distillation, self-improvement of LLMs, capability-selective training, activation subspace projection, generalizable self-training."
---

# Self-Policy Distillation (SPD) via Capability-Selective Subspace Projection

**Paper:** arXiv:2605.22675 (May 2026)
**Authors:** [Authors from the paper — typically anonymous at submission]

---

## Overview

Self-Policy Distillation (SPD) is a **fully self-supervised** method for improving LLMs without any external signals — no correctness filtering, no execution feedback, no reward model, no human annotations. The core insight is that a model already possesses latent capability signals within its own weights and activations; SPD extracts these signals and uses them to selectively reinforce high-quality self-generated tokens.

**Key innovation:** Instead of filtering outputs by an external criterion (correctness, reward score), SPD defines *correctness* intrinsically: a token is "correct" if the model's own gradient with respect to the loss on that token has high magnitude and consistent direction within a low-dimensional subspace. This subspace is extracted from the model's own gradients and captures the model's latent notion of "what correct generation looks like."

**No external signals — the model distills its own best behavior.**

---

## Capability Subspace Extraction

Given an input sequence, SPD extracts a **low-rank capability subspace** from the model's own gradients using the following procedure:

### 1. Gradient Computation per Token

For each token position \( t \) in the training sequence, compute the gradient of the next-token prediction (NTP) loss with respect to the **intermediate key-value (KV) activations** at a selected layer \( \ell \):

\[
\mathbf{g}_t = \nabla_{\mathbf{A}_\ell(t)} \mathcal{L}_{\text{NTP}}(x_t, \hat{x}_t)
\]

where \( \mathbf{A}_\ell(t) \) is the KV activation at layer \( \ell \) for token position \( t \), and \( \mathcal{L}_{\text{NTP}} \) is the standard cross-entropy loss.

### 2. Correctness-Defining Token Selection

Tokens are classified into **correctness-defining** vs. correctness-irrelevant based on gradient properties:

- **Correctness-defining tokens:** Tokens where the gradient norm \( \|\mathbf{g}_t\|_2 \) exceeds a threshold \( \tau_{\text{grad}} \). These are tokens where the model's loss signals are informative — high gradient magnitude indicates the model "cares" about this prediction.
- **Correctness-irrelevant tokens:** Tokens where the gradient norm is below threshold (e.g., stop words, repetitive tokens where the model is already confident).

> **Intuition:** The model inherently knows which tokens matter for getting the answer right. Tokens with high gradient magnitude are precisely those where getting them wrong would meaningfully impact overall generation quality.

### 3. Low-Rank Subspace via SVD

Let \( \mathbf{G} = [\mathbf{g}_{t_1}, \mathbf{g}_{t_2}, \ldots, \mathbf{g}_{t_k}] \) be the matrix of gradients from correctness-defining tokens. Perform **singular value decomposition (SVD)**:

\[
\mathbf{G} = \mathbf{U} \boldsymbol{\Sigma} \mathbf{V}^\top
\]

The **capability subspace** \( \mathcal{S} \) is defined as the top-\( r \) right singular vectors:

\[
\mathcal{S} = \text{span}(\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_r)
\]

where \( r \) is a small rank hyperparameter (typically \( r \ll d_{\text{model}} \), e.g., \( r = 32 \) or \( r = 64 \)).

**Properties of the capability subspace:**
- **Low-rank:** Captures the most structured, shared patterns across correctness-defining tokens
- **Model-intrinsic:** Derived entirely from the model's own gradient signals
- **Layer-specific:** Extracted at a specific transformer layer — typically an early-to-middle layer
- **Task-agnostic:** The same procedure works for any domain or task without modification

---

## KV Activation Projection

During **self-generation**, SPD modifies the model's forward pass by projecting KV activations into the learned capability subspace:

### Subspace Projection Operator

Define the projection matrix:

\[
\mathbf{P}_{\mathcal{S}} = \mathbf{V}_r \mathbf{V}_r^\top
\]

where \( \mathbf{V}_r = [\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_r] \in \mathbb{R}^{d \times r} \).

During autoregressive generation, for each token position, the KV activation at layer \( \ell \) is projected:

\[
\tilde{\mathbf{A}}_\ell(t) = \mathbf{P}_{\mathcal{S}} \, \mathbf{A}_\ell(t)
\]

This means: **zero out all components of the KV activations that lie outside the capability subspace.** Only the components aligned with the model's own definition of "correct" generation are retained.

### Effect on Generation

- **Retains:** Activations aligned with the capability subspace → semantically important, correctness-relevant features
- **Suppresses:** Activations orthogonal to the subspace → noise, spurious correlations, low-confidence predictions
- **Result:** The model generates higher-quality tokens, constrained to its own latent notion of correctness

### Why KV Activations?

The paper selects **key-value (KV) activations** at a specific transformer layer because:

1. KV activations mediate the attention mechanism — they directly control which information flows between tokens
2. They are computationally efficient to project (no need to modify all parameters)
3. They naturally separate into "retrieved information" (keys) and "contributed information" (values) from earlier context
4. Projecting them modifies generation behavior without altering the trained weights of the model

---

## Training Process

SPD follows a **self-distillation** loop with three stages:

### Stage 1: Capability Subspace Extraction

```
For each batch of training data:
  1. Forward pass on input x → compute NTP loss per token
  2. Backward pass → extract gradients ∇_{A_ℓ} L for each token
  3. Filter: keep only tokens with ||g_t||₂ > τ_grad
  4. Stack gradients → matrix G
  5. SVD(G) → top-r singular vectors V_r → capability subspace S
```

- Performed once per epoch (or once every k steps)
- Subspace can be periodically updated as the model improves

### Stage 2: Self-Generation with KV Projection

```
For each input x in training data:
  1. Load subspace projection matrix P_S = V_r V_r^T
  2. Autoregressive generation:
     For t = 1, 2, ...:
       a. Forward pass through layer ℓ
       b. Project KV activation: A_ℓ(t) ← P_S A_ℓ(t)
       c. Continue forward pass
       d. Sample next token y_t from projected distribution
     → Collect full output sequence y = (y_1, ..., y_T)
```

- No temperature scaling or special decoding needed — standard sampling
- The projection itself enforces quality constraints
- Generates **raw outputs** — no filtering or post-processing

### Stage 3: Fine-Tuning on Self-Generated Outputs

```
For each pair (x, y) where y is the SPD-generated output:
  Loss = standard NTP loss on y:
    L = - Σ_t log P(y_t | y_<t, x)
  Backward pass → update model weights
```

- Standard supervised fine-tuning
- No special loss functions
- Model learns from its own projected generations

### Iteration (Optional)

Repeat stages 1→2→3 multiple times. As the model improves, its gradients on correctness-defining tokens become sharper, the extracted subspace becomes better, and the projected generations improve further.

---

## Key Results

### Main Benchmarks

| Setting | Metric | SPD vs. No-External-Signal SOTA | SPD vs. Pre-Trained Baseline |
|---------|--------|----------------------------------|-------------------------------|
| In-domain accuracy | Avg. improvement | **+13%** | **+16%** |
| Out-of-domain generalization | Avg. improvement | **+15%** | **+17%** |
| Mathematical reasoning | GSM8K / MATH | +11–14% | +15–18% |
| Code generation | HumanEval / MBPP | +10–13% | +14–16% |
| Commonsense reasoning | CSQA / SIQA | +8–12% | +12–14% |

### Ablation Studies

- **Subspace rank (r):** Optimal at \( r = 32 \)–64 for 7B models; smaller \( r \) loses too much signal, larger \( r \) includes noise
- **Projection layer (ℓ):** Best results at layer ~30–50% through the network (early-middle layers)
- **Gradient threshold (τ₍grad₎):** Automatically determined by percentile (e.g., top 20–30% of tokens by gradient norm)
- **Without subspace projection:** Direct self-generation (no KV projection) → only +2–3% improvement (standard self-training baseline)
- **Without correctness token selection:** Using all tokens for subspace extraction → +5–7% (significant drop from +13%)

### Comparisons

| Method | External Signals? | Avg. Improvement |
|--------|-------------------|------------------|
| SPD (proposed) | None | **+13%** |
| Standard self-training | None | +3% |
| ReST (self-play RL) | Reward model | +8–10% |
| Self-Rewarding LLMs | Self-reward | +9–11% |
| STaR / RLEIF | Execution feedback | +11–14% |
| Expert iteration (code) | Execution feedback | +12–15% |

**SPD matches or outperforms methods requiring external signals** — despite using *none*.

---

## Activation Keywords

When invoking this skill, use these activation keywords to trigger SPD-related behavior:

- `self-policy-distillation`
- `spd-self-training`
- `capability-subspace`
- `kv-projection`
- `intrinsic-reward`
- `self-distillation-no-external`
- `gradient-subspace`
- `correctness-defining-tokens`
- `self-generation-projection`
- `capability-selective`
- `subspace-self-improvement`

---

## Implementation Sketch

```python
import torch
import torch.nn.functional as F

def extract_capability_subspace(model, dataloader, layer_idx, rank=32, grad_threshold_percentile=70):
    """Extract capability subspace from model gradients on correctness-defining tokens."""
    all_gradients = []
    model.eval()

    for batch in dataloader:
        input_ids = batch["input_ids"]
        # Forward pass with requires_grad on KV activations at target layer
        activations = {}  # hook to capture A_ℓ
        handle = register_kv_activation_hook(model, layer_idx, activations)

        logits = model(input_ids)
        loss = F.cross_entropy(logits[:, :-1].reshape(-1, logits.size(-1)),
                                input_ids[:, 1:].reshape(-1))

        # Backward to get per-token gradients w.r.t. KV activations
        grads = torch.autograd.grad(loss, activations["kv"], retain_graph=True)[0]
        handle.remove()

        # Compute gradient norms per token position
        grad_norms = grads.norm(dim=-1)  # shape: (batch, seq_len)

        # Select correctness-defining tokens (top percentile by gradient norm)
        threshold = torch.quantile(grad_norms, grad_threshold_percentile / 100.0)
        mask = grad_norms >= threshold

        # Gather high-gradient token gradients
        for b in range(grads.size(0)):
            selected = grads[b, mask[b]]
            all_gradients.append(selected)

    # Stack and perform SVD
    G = torch.cat(all_gradients, dim=0)  # (n_tokens, d_model)
    U, S, Vt = torch.linalg.svd(G, full_matrices=False)
    subspace = Vt[:rank]  # top-r right singular vectors
    return subspace  # shape: (rank, d_model)


def generate_with_projection(model, input_ids, subspace, layer_idx, max_new_tokens=256):
    """Generate tokens with KV activations projected into capability subspace."""
    P = subspace.T @ subspace  # (d_model, d_model) projection matrix
    generated = input_ids.clone()
    model.eval()

    # Register forward hook to project KV activations
    def projection_hook(module, input, output):
        # output is (batch, seq_len, d_model) for K or V
        return output @ P.T  # project into subspace

    handle = register_kv_projection_hook(model, layer_idx, projection_hook)

    for _ in range(max_new_tokens):
        with torch.no_grad():
            logits = model(generated)
            next_token = torch.multinomial(F.softmax(logits[:, -1, :], dim=-1), 1)
            generated = torch.cat([generated, next_token], dim=-1)

    handle.remove()
    return generated


def spd_train_step(model, optim, batch, subspace, layer_idx):
    """Single SPD training step: generate with projection, then NTP fine-tune."""
    # Stage 2: Self-generation with KV projection
    with torch.no_grad():
        self_gen = generate_with_projection(model, batch["input_ids"], subspace, layer_idx)

    # Stage 3: Fine-tune on self-generated outputs
    logits = model(self_gen)
    loss = F.cross_entropy(logits[:, :-1].reshape(-1, logits.size(-1)),
                            self_gen[:, 1:].reshape(-1))

    optim.zero_grad()
    loss.backward()
    optim.step()
    return loss.item()
```

---

## Usage Guidance

**When to use SPD:**
- You want to improve an LLM without any external data, labels, rewards, or correctness filtering
- You want a fully self-supervised improvement loop that doesn't depend on task-specific heuristics
- You need improved out-of-domain generalization from self-training
- You want to avoid the complexity and brittleness of reward model training or execution feedback loops

**When NOT to use SPD:**
- When high-quality external signals are cheaply available (supervised fine-tuning may be simpler)
- On very small models where gradient signals may be noisy (subspace extraction degrades)
- When raw throughput matters more than quality (KV projection adds compute during generation)

**Hyperparameter recommendations:**
- **Subspace rank r:** 32–64 for 7B models, scale roughly as sqrt(d_model)
- **Gradient percentile:** Top 20–30% of tokens by gradient norm
- **Projection layer:** ~30–50% of total layers (early-middle)
- **Update frequency:** Recompute subspace every epoch or every 1k–5k steps
- **Iterations:** 2–3 rounds of SPD typically sufficient; diminishing returns beyond

---

## References

- arXiv:2605.22675 — Self-Policy Distillation (SPD) via Capability-Selective Subspace Projection (May 2026)
- Related: self-training, self-distillation, activation subspace methods, self-improving LLMs
