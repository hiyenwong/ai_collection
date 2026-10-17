---
name: dp-pac-bayes-dirichlet-process
description: "Dimension-free PAC-Bayes generalization certificates for deep nets: move the prior from parameter space to data-distribution space via Dirichlet Process, bound parameter-space relative entropy by DP divergence via Data Processing Inequality (closed form via Digamma), and certify non-vacuous bounds invariant to width/depth. Use when PAC-Bayes weight-space bounds are vacuous for overparameterized nets, or when certifying generalization of large D models."
---

# DP-PAC-Bayes: Dimension-Free PAC-Bayes via Dirichlet Process Priors

**Source**: Dimension-Free PAC-Bayes Generalization for Deep Neural Networks via Dirichlet Processes (arXiv: 2610.21340, math.ST, 2026-10-15)

## Problem

Classical PAC-Bayes places the prior P over Euclidean parameter space Θ ⊆ ℝ^D.
The KL(Posterior‖Prior) term scales with network dimension D. For overparameterized
networks (D ≫ n, e.g. 4.2M parameters), the bound exceeds 940% — vacuous.

## Core Move: Prior on Data Distributions, Not Parameters

Shift prior specification from internal parameters θ ∈ ℝ^D to the non-parametric
space of data distributions M₁(Z) via a **Dirichlet Process prior** DP(α, F₀).
Parameter distributions are induced by **push-forward measures** under the
(deterministic) learning algorithm A: data-draws → weights.

## Key Chain: Data Processing Inequality

The fundamental inequality that kills the D-dependence:

```
KL( Q(θ) ‖ P(θ) )  ≤  KL_dp( Q_data ‖ DP(α, F₀) )
```

Parameter-space relative entropy is strictly bounded by the data-space DP
divergence because θ = A(data) is a (possibly deterministic) function of the
data — and DPI means processing cannot increase relative entropy.

### Closed-form DP divergence

For n i.i.d. draws with empirical measure P̂ₙ, the KL between the posterior
DP(P̂ₙ) and prior DP(α, F₀) is exact and closed-form via **Digamma functions**:

```
KL_dp ≈ n·ψ(α+n) − ... (Digamma terms)   — O(n), no D anywhere
```

The certificate is therefore strictly invariant to parameter count D, width, and depth.

## Minimax Rates on Submanifolds

When data lie on an intrinsic d*-dimensional submanifold, optimal partition
scaling recovers the non-parametric minimax rate:

```
bound = O( n^{-1/(d*+2)} · √(ln n) )
```

This is the classical non-parametric density-estimation rate — the DP-PAC-Bayes
certificate is minimax-optimal in the intrinsic dimension, not the ambient one.

## Empirical Anchors

- Architectures scaling D = 7,850 → 4,203,522 on full MNIST
- Classical weight-space PAC-Bayes: >940% (vacuous)
- DP-PAC-Bayes certificate: stable **8.8%–9.4%**, non-vacuous at every scale

## Reusable Pattern: "DPI-Lifted Priors"

General recipe when a complexity measure over X is unusable but a push-forward
structure exists:

1. Put the prior on the *source* space (data, prompts, seeds) where a natural
   non-parametric prior exists (DP, GP, normalized measure).
2. Induce the induced measure on the *target* space (weights) via push-forward
   through the learning algorithm.
3. Bound target-space divergence by source-space divergence via DPI.
4. Exploit closed-form conjugacy (Dirichlet ↔ multinomial / GP ↔ Gaussian)
   to get exact, cheap certificates.

This applies beyond generalization: certification of model soups/merges,
Bayesian fine-tuning with prompt-space priors, and RL policy certificates
where the "parameter" is a trajectory of environment interactions.

## Limitations

- Requires the learning algorithm to be a measurable map data→weights
  (fine for standard training pipelines).
- DP(α, F₀) choice of F₀ still matters — poor F₀ inflates the constant.
- Empirical evaluation on MNIST-scale; ImageScale-scale certification open.
- Bound quality depends on intrinsic-dimension d* estimates of real data.

## Related Skills

- `sae-optimality-structures-dictionaries` — optimality conditions structure representations
- `wta-spiking-transformer-language` — another math.ST/theory-side certification pattern
