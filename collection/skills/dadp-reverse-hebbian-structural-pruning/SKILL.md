---
name: dadp-reverse-hebbian-structural-pruning
description: Use when pruning nets without layer budgets or retraining. Activity×gradient threshold.
category: ai_collection
---

# DADP — Dynamic Activity-Dependent Pruning (Reverse Hebbian)

arXiv 2610.11853 (Bhushan Deshpande, 8 Oct 2026; code: github.com/bhushan1729/hebbian_learning)

## Core Idea

Single global threshold + importance = expected |pre-synaptic activation × post-synaptic error gradient|. No per-layer sparsity budgets, no prune-retrain cycles, no regrowth. Inspired by activity-dependent synapse elimination (developmental pruning): connections survive only if the pre neuron fires AND the post target is actively reducing error.

## Method

### Importance metric (reverse Hebbian)
`I_ij^l = E[ |a_i^{l−1} · ∂L/∂y_j^l| ]` — expectation over temporal window ΔT (~100–500 steps; filters single-batch noise). By chain rule this is the accumulated expected weight-gradient magnitude. **Reverse of Hebb**: kill the connection if either factor ≈ 0 (silent pre-activation OR error-insensitive post target).

**Theorem 1**: `I_ij` = magnitude of the first-order Taylor loss change from zeroing w_ij, normalized per unit weight magnitude. So it's a gradient-saliency measure, not a weight-size measure.

### Mask update (permanent, single-pass)
`M_ij(t) = M_ij(t−ΔT) · 𝟙[I_ij(t) ≥ τ]` — one GLOBAL threshold τ swept in [1e-6, 1e-3]; sparsity emerges, never hardcoded. Pruning is permanent (no regrowth), integrated into standard training.

### Self-regulating negative feedback loop
Loss ↓ → gradients shrink → scores fall below τ → pruning event → transient loss bounce → gradients re-elevate on surviving paths → re-fine-tune → stabilize → repeat. Network only sheds capacity when features have stabilized (sparsity equilibrium, Thm 2).

### Emergent structured death
Unstructured element-wise pruning cascades into structure automatically:
- Neuron dead ⇔ all incoming OR all outgoing connections pruned (no forward activation → all its incoming scores collapse to 0 next interval; no gradient → scores collapse too).
- Conv filter dead ⇔ all connections zero → physically delete filter slice + BN params + contract next-layer input channels (real compression, not just masks).
- ResNet skip/downsample paths retain 60–80% capacity organically (gradient flow preserved).

## Key Results (Table 1)
| Model / Task | DADP sparsity | Acc vs baselines |
|---|---|---|
| ResNet-18 CIFAR-10, τ=5e-4 | 99.35% | 72.28% — beats SNIP 71.44, RigL 63.85, Magnitude 66.42 |
| MiniBERT SST-2, τ=3e-6 | 96.03% | 80.85% — Magnitude collapses to 50.92 |
| VGG-16 CIFAR-10, τ=6e-6 | 91.65% | 82.65% (≈SNIP, RigL worse) |
| MLP MNIST, τ=1e-6 | 84.9% | 97.91% |
| BiLSTM-CRF CoNLL, τ=5e-5 | 95.0% | 84.28 F1 (−0.88) |

Robustness: stable across 50× pruning-interval range (ΔT ∈ [100, 5000]) and Kaiming/Xavier/Orthogonal init without retuning τ.

## Domain-Adaptive Sparsity Allocation (the surprising finding)
- **Vision (ResNet/VGG)**: "Foundational Feature Lock" — early layers stay dense (0% sparsity), deep layers prune to 98-99%. Early filters have consistently large activation×gradient products.
- **Sequence (MiniBERT/BiLSTM)**: **INVERTED** — early embedding/context-free projections pruned to 95%, deep attention/decision heads stay dense (75-85% active). Task-loss gradients concentrate in final decision layers.
No schedule enforces this — it emerges from the metric's interaction with information flow per domain.

## Representation-Quality Verification (first for dynamic pruning)
Matrix-based metrics on activation Gram spectra, no probes needed:
- Normalized Shannon entropy `S_norm = −Σ p_i log2(p_i)/log2(N)` (p_i = eigenvalue fractions of centered Gram K = (Z−Z̄)(Z−Z̄)^T)
- Effective rank `EffRank = exp(−Σ p_i ln(p_i))`
DADP keeps S_norm > 0.85 at >97% sparsity; mid-depth layers EXCEED dense-baseline EffRank (pruning correlated noise raises geometric rank). Surviving weights keep continuous zero-centered bell distribution (no bimodal split at zero like magnitude/RigL) — small weights with high activity survive, large inactive weights die.

## Reuse Patterns
1. **Global-threshold dynamic pruning**: replace per-layer budgets with one τ + self-correcting feedback when you don't know each layer's natural capacity.
2. **Activity×gradient saliency**: for any "importance" score, multiply forward usage by backward sensitivity — catches weights magnitude misses (large-but-inactive dies; small-but-high-gradient survives).
3. **Emergent structured compression**: prune at weight level, then garbage-collect dead neurons/filters (check all-in OR all-out) for physical speedup without group-lasso penalties.
4. **Gram-spectrum QA**: verify any compression method preserves feature diversity via S_norm/EffRank on layer activations — catches representation collapse that accuracy metrics miss.
5. **Domain check before layer-uniform sparsity**: vision front-loads redundancy deep; transformers invert it. Never assume a schedule transfers across modalities.
