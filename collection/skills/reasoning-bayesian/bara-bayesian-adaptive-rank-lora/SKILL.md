---
name: bara-bayesian-adaptive-rank-lora
description: "BaRA — Bayesian Adaptive Rank Allocation for LoRA fine-tuning. Dynamically allocates per-instance effective rank via sparse activation of disentangled latent factors, with complexity-theoretic generalization bounds depending on learned joint effective rank rather than max rank."
tags: [LoRA, parameter-efficient-fine-tuning, Bayesian, adaptive-rank, uncertainty-calibration, sparse-adaptation]
source: "arXiv:2606.29184"
trigger: "LoRA, adaptive rank, Bayesian LoRA, PEFT, rank allocation, uncertainty calibration, sparse adaptation, overconfident predictions"
---

# BaRA: Bayesian Adaptive Rank Allocation for PEFT

## Problem
Standard LoRA uses a fixed low-rank subspace for all inputs, leading to:
- Overconfident predictions and miscalibrated uncertainty (especially in low-data regimes)
- Either under-parameterization (too rigid) or over-parameterization (wasted capacity)
- Existing Bayesian LoRA variants use fixed/heuristic ranks, missing context-dependent capacity needs

## Core Methodology

### Probabilistic Topic Model Inspiration
BaRA treats adaptation capacity like topic proportions in a document:
- Maintain a set of **disentangled latent factors** (analogous to topics)
- Per-instance **global-local gate** activates a **sparse, context-dependent subset**
- Effective rank varies per input — easy instances use few factors, complex ones use many

### Bayesian Formulation
- Priors over factor activations encourage sparsity
- Posterior inference yields data-driven capacity control
- Avoids over-parameterization while preserving input-dependent expressiveness

### Complexity-Theoretic Generalization Analysis
**Key theorem**: Generalization gap depends on learned joint effective rank `s̄_{Φ,θ}` induced by the global-local gate, NOT on the maximum rank `r`.

This explains *why* sparse adaptive rank allocation helps:
- Reduces effective hypothesis complexity
- Preserves expressiveness where needed
- Tighter bounds than uniform-rank alternatives

## Implementation Pattern
```
class BaRA_LoRA(nn.Module):
    def __init__(self, base_rank, n_factors, local_dim):
        self.factors = nn.ParameterList([LowRankFactor(...) for _ in range(n_factors)])
        self.global_gate = GlobalGate(base_rank)  # instance-level
        self.local_gate = LocalGate(local_dim)     # feature-level

    def forward(self, x):
        gate_weights = self.global_gate(x) * self.local_gate(x)  # sparse
        active_factors = topk(gate_weights, k=effective_k(x))
        return sum(w * f(x) for w, f in zip(active_factors, self.factors))
```

## Results
- Consistently improves predictive performance, robustness, and uncertainty calibration vs LoRA and Bayesian LoRA variants
- Better calibrated confidence (lower ECE) on diverse NLP benchmarks
- Generalization gap shrinks as effective rank decreases (validates theory)

## Pitfalls
- Sparse gate must be differentiable (straight-through or Gumbel-Softmax)
- Too aggressive sparsity → capacity collapse on complex tasks; monitor validation loss
- Effective rank measurement requires careful trace normalization; naive counting overestimates
- Training cost higher than vanilla LoRA due to gate overhead (~15-20% more FLOPs)

## When to Use
- Low-data fine-tuning where uncertainty matters (medical, legal, scientific)
- Tasks with heterogeneous difficulty distribution
- When deploying to settings requiring calibrated confidence (not just accuracy)

## Activation
BaRA, Bayesian LoRA, adaptive rank, PEFT, uncertainty calibration, sparse adaptation, effective rank, overconfident predictions, low-data fine-tuning
