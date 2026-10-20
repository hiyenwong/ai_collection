---
name: geometry-capacity-associative-memory
description: "Hebbian memory capacity from embedding geometry, fit-free."
category: ai_collection
---

# A Geometry-Based Capacity Theory for Finite-Feature Associative Memory

**Source**: arXiv:2610.09056 (Zhang et al., Univ. of Calgary + Huazhong, cs.LG, 6 Oct 2026)

## When to Use
- Designing or sizing compressed Hebbian / linear-attention / fast-weight associative memories
- Diagnosing whether poor retrieval needs more features or a different representation
- Predicting memory capacity from embedding geometry before training
- Analyzing retrieval interference in key-value memory systems (KV-cache-like compression, cross-modal retrieval)

## Core Idea

For exact-key retrieval in compressed finite-feature Hebbian memory, retrieval interference **separates into two terms with different remedies**:

1. **Finite-feature noise** ~ (N−1)/R — Monte-Carlo variance of the random-feature kernel estimate; decreases as feature dimension R grows. Fix: **increase R (more memory)**.
2. **Structural interference** I_struct,i = Σ_{j≠i} K_ij² — squared kernel overlap among stored keys; **persists in the infinite-feature limit**. Fix: **change the representation/kernel/organization**.

This yields a fit-free prediction of retrieval quality and a design rule: identify which term dominates, then apply the matching remedy.

## Theory

Store N key–value pairs {(k_i, v_i)} with unit-normalized random feature map φ_R (R features). Hebbian matrix M = Σ_j φ_R(k_j) v_j^T. Exact-key query q=k_i retrieves v̂_i = M^T φ_R(k_i) = Σ_j K̂_ij v_j.

**Normalized retrieval cosine law** (random-value model):

C_i(R) ≈ [1 + Σ_{j≠i} K_ij² + (N−1)/R]^(−1/2)

- K_ij = K(k_i, k_j) — the exact kernel; K̂ — R-feature estimate.
- For RBF random Fourier features, per-pair variance is (1−K_ij²)/R; general shift-invariant: [1+κ(2Δ_ij)−2K_ij²]/R.
- **Infinite-R ceiling**: C_i,∞ ≈ [1 + Σ_{j≠i} K_ij²]^(−1/2) — exact for mutually orthogonal unit values.

**Correlated values** (real embeddings): retrieval depends jointly on key kernel AND value Gram matrix G_jℓ = ⟨v_j, v_ℓ⟩:
- a_i = Σ_j K_ij G_ji (numerator), b_i = Σ_{j,ℓ} K_ij K_iℓ G_jℓ (denominator)
- C_i,∞ = a_i / √b_i (exact, infinite features)
- C_i(R) ≈ a_i / √(b_i + (N−1)/R) (finite-R approximation)
- Covariance-aware variant: replace (N−1)/R with exact noise energy 2D_i/R where E‖ε_i‖² = 2D_i/m; improves aligned-value crossover prediction (84.5% MAE reduction) but overcorrects permuted values — use only for close design comparisons.

**Capacity boundary**: for target cosine C*, solve R/N ≈ (1−1/N)/(1/C*² − 1). E.g. C*=0.95 → R/N ≈ 9.26 large-N. With heterogeneous structural interference, solve the item-wise mean numerically. The boundary converts measured representation geometry into an explicit memory-sizing estimate; the infinite-R ceiling identifies targets unreachable by increasing R alone.

## Key Experimental Findings

1. **Geometry, not nominal dimension, controls the ceiling**: PCA whitening REDUCES nominal dimension 2048→256 while RAISING the infinite-R ceiling from ~0.65 to ~1.0 (ResNet50 embeddings). Effective rank alone is insufficient — same effective rank can have different structural interference; kernel scale can reverse capacity at unchanged rank.
2. **Validated fit-free**: predictions match empirical retrieval across i.i.d./clustered/low-rank/anisotropic synthetic keys; ResNet50, ViT-B/16, DINOv2, CLIP embeddings under RAW / CENTERED / WHITENED interventions; CIFAR-10/100, STL-10.
3. **Medical stress test**: SynthRAD2023 MRI–CT (brain+pelvis) and 445 clinical NCCT–CTA pairs. Clustered storage (5 adjacent slices from 24 patients vs 1 center slice from 120 patients, matched N=120) → predicted and observed structural-interference increase; theory correctly identifies when WHITENED beats RAW.
4. **Crossover prediction**: covariance-aware theory brackets empirical crossover in ALL 20 subsets: r_cov ≤ r_empirical ≤ r_simple; MAE −84.5% vs simple theory.
5. **Design-regret experiments**: ranking candidate preprocessing/kernel choices by predicted capacity curves achieves lower design regret than fixed RAW default.

## Reusable Methodology Patterns

- **Interference decomposition**: split retrieval error into budget-dependent noise vs geometry-dependent structural term — the two have opposite remedies (more features vs different representation).
- **Measure Σ K_ij² on your embedding set** before building a memory: it directly predicts the asymptotic retrieval ceiling, no training needed.
- **Whitening as capacity intervention**: mean subtraction + PCA whitening + row-normalization can raise the ceiling while shrinking dimension — counterintuitive but validated.
- **Kernel-scale sensitivity**: changing kernel bandwidth γ reverses capacity ranking of representations; tune γ per representation.
- **Joint key–value geometry**: with correlated values, analyze K and G jointly (a_i, b_i formulas) — key-only analysis mispredicts cross-modal retrieval.
- **Fit-free validation protocol**: predict the full retrieval curve from measured geometry of an unseen condition, no fitted coefficients.

## Connection to Other Memory Models

- Correlation-matrix / linear heteroassociative memories: same additive outer-product rule, but with finite random-feature keys.
- Fast-weight programmers / linearized attention (Schlag et al.): capacity limit when too many nonorthogonal key features accumulate in finite fast-weight matrix — this theory refines the dimension/orthogonality picture into a graded Σ K_ij² prediction plus separate finite-R noise.
- LoLA: self-recall error detects poorly-remembered KV pairs → sparse cache (complementary engineering fix).
- KATA: spherical-packing + Welch interference floor view of recall capacity (different observable).
- Modern Hopfield networks / attention: retain explicit items; here the object is a fixed-size compressed matrix.

## Activation

associative memory capacity, Hebbian memory, random features, kernel geometry, memory interference, retrieval quality prediction, fast weights, linear attention capacity, representation whitening, memory sizing, cross-modal retrieval, value Gram matrix, MRI CT retrieval
