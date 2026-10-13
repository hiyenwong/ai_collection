---
name: polytopal-neural-network-archetypal-layers
description: Use when building intrinsically interpretable nets or VQ without STE. Polytope-constrained layers.
category: ai_collection
---

# Polytopal Neural Network (PNN) — Archetypal-Analysis-Constrained Layers

arXiv 2610.12004 (Wedenborg, Nørskov, Dorszewski, Wickstrøm, Mørup — DTU/UiT, 8 Oct 2026)

## Core Method

Enforce every constrained layer's representation to lie on a **learned polytope**: each activation is a convex combination of K archetypes (extremal corpus points). Interpretability is *intrinsic* — the explaining coordinates ARE the coordinates the next layer receives, not post-hoc.

### Layer operator
After layer ℓ, insert projection `Δ_C^ℓ`:
- `Z^ℓ` = pre-projection activations (N×d^ℓ)
- Archetypes `A^ℓ = C^ℓ Z^ℓ`, with `C^ℓ` row-stochastic (softmax logits → end-to-end trainable)
- `S^ℓ = argmin_S ||Z^ℓ − S·A^ℓ||²_F` s.t. simplex rows (convex QP per sample)
- Projected rep `R^ℓ = S^ℓ A^ℓ` feeds the next layer — **explanations = computation**.

### Scaling (the two tricks that make it deep-learning-viable)
1. **Corpus streaming**: decouple archetypes from full dataset via learned corpus `X_c = C_c X` (N_c ≪ N). Mini-batch update (Eq 4): batch sums carry gradients; non-batch sums recomputed from stored logits in chunks. Memory scales O(N_c|B|) not O(N).
2. **Amortized simplex inference**: learn `g_φ(h_n)` on archetype correlations `h = z(A)^T`; output `ŝ = softmax(g_φ(h))`. Trained ONLY on projection residual `||z − ŝA||²` with z, A detached (cannot deform encoder); refit every 10 epochs; K batched SMO warm-start rounds refine at test time. Replaces O(K³)→O(K²) exact QP.

### Theory anchors
- **Lemma 1**: G = AA^T positive definite (needs K ≤ d) → unique, continuous piecewise-affine projection Φ.
- **Theorem 1**: Φ(h) = sparsemax(f_θ(h)) exactly representable by finite ReLU net → the polytope projection is a ReLU-computable map.

### Token-level variant (pretrained backbones)
Polytope on spatial tokens (layer-norm + linear to 256d, shared polytope A). Linear head on token-mean: logits = mean of per-token logits → **exact additive per-token attribution** (Fig 5-6: hognose snake head tokens vote via snake-scale archetype).

## Generalizations (same constraint family)
- **PNN-VQ**: simplex → one-hot. Centroids C = (S^⊤S)^{-1}S^⊤; direct gradient training, **no STE, no commitment loss, no EMA** (vs VQ-VAE). Encoder learns through corpus features Z_c.
- **PNN-PL**: unconstrained S → closed-form normal-equation projection (Eq 12) = classic subspace projection layers as special case.

## Key Results
| Setting | Unconstrained | PNN | Kept |
|---|---|---|---|
| ImageNet-100 ConvNeXt-T (K=25) | 94.6% | 91.7% | 96.9% |
| ImageNet-1k ConvNeXt-T (K=128) | 81.2% | 78.6% | 96.9% |
| CIFAR-10 compact ViT (K=10) | 94.47% | 94.46% | 100.0% |

- PNN-AE beats DirVAE on reconstruction MSE across 5 datasets; PNN-VQ matches/beats VQ-VAE.
- PathMNIST 89.1%, BloodMNIST 98.1% (K=25).
- Archetypes emerge semantically without labels (FashionMNIST K=3: footwear/lower/upper body).

## Reuse Patterns
1. **Intrinsic interpretability**: constrain latents so explanation coordinates are the forward-pass coordinates — never post-hoc probe.
2. **VQ without heuristics**: one-hot simplex + softmax-parameterized codebook = gradient-trained VQ, eliminating STE/commitment/EMA triad.
3. **Amortizer discipline**: train the fast approximator on a detached residual objective so it can never leak gradients into the main model.
4. **Corpus trick**: any "express learned components as combos of data points" method scales by streaming corpus statistics from stored logits, not from full-dataset passes.

## Contrasts
- vs corpus-XAI (Crabbe 2021): corpus learned end-to-end, not user-fixed; enforced during training not after.
- vs ProtoPNet/Pip-Net: archetypes are polytope vertices the token lives inside (own coordinates), no prototype-similarity losses or class assignment.
- vs DirVAE: learned polytope, not fixed standard-simplex projection.
- vs deep-AA (AAnet etc.): constraint at EVERY chosen layer (sequential polytopes), not single bottleneck penalty.

## Implementation Notes
- softmax vs sparsemax amortizer: similar quality under same refinement protocol (Table 11).
- Numerical stability: subtract row max of corpus logits before exp (Eq 4).
- Refine amortizer with K SMO rounds per forward at eval for CNN/AE; ImageNet token models run amortizer only.
