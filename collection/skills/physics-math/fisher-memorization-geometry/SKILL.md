---
name: fisher-memorization-geometry
description: Fisher projection de-memorizes networks layer by layer.
category: ai_collection
---

# Fisher Information Geometry of Memorization

**Source**: Bernstein, Goddard, Ngampruetikorn, Di Carlo, Schwab — "Fisher information and the geometry of memorization in neural networks" (arXiv: 2610.16161, Princeton/Sydney/CUNY, 12 Oct 2026)

**Trigger words**: fisher information, memorization, de-memorization, generalization vs memorization, fisher eigenspectrum projection, label noise recovery, in-context learning overfitting, participation ratio, benign overfitting

## Core Idea

The population Fisher decomposes as an average of per-sample Fishers: F = (1/N)Σ F_x. Directions encoding generalizing features align across samples and add coherently; directions encoding single-sample memorization are near-orthogonal in parameter space and suppressed by ~1/N in the average. Therefore the TOP of the Fisher eigenspectrum holds generalizing structure and the BOTTOM holds memorized content — and projecting a trained network's per-layer weights onto the top-k Fisher eigenvectors performs **de-memorization**: it selectively destroys recall of memorized samples while preserving task performance.

## De-memorization Procedure

1. Train to 100% train accuracy on data containing forced-memorization content (Gaussian-noise images with random labels, or flipped labels).
2. Compute the EXACT per-layer Fisher: F(θ*) = (1/N)Σ_i Σ_c p(c|x_i) s_ic s_ic^T, s_ic = ∇_θ log p_θ(c|x_i)|θ*. (No K-FAC needed at ResNet-20 scale; F is the Hessian of KL divergence.)
3. Diagonalize F per layer, keep top-k eigenvectors, project that layer's weights onto their span (zero the complement).
4. Sweep k; monitor clean train/test accuracy vs memorized-sample accuracy (under assigned AND true labels).

## Key Results

- **Layer dependence (Gaussian-input memorization, ResNet-20, CIFAR-10 + 1% noise)**: first layer separates at k≈45 — near-max CIFAR accuracy while Gaussian-sample accuracy <30%; the LAST layer shows NO separation at any k (memorized and structured representations merged). Nearly all final-layer predictive information sits in the top ~5% eigendirections. Memorization is both diffuse and localizable.
- **Label noise (10% flips)**: penultimate conv layer separates when the Fisher is computed on CLEAN data only; separation collapses when computed on the full noisy training set. Fisher geometry is data-dependent — compute it on denoised data.
- **Block-diagonal whole-model Fisher**: clean-data Fisher separates memorization from task; full-data Fisher mixes them — then only layerwise analysis works.
- **ICL task memorization (3-block GPT-2 on linear regression, M latent task vectors)**: transformer first generalizes to held-out tasks, then overfits by memorizing training tasks (transient ICL). Projecting the SECOND block's MLP onto its top Fisher subspace improves held-out generalization, closing ~half the gap to the early-stopped model, at the cost of memorized-task performance. Attention-layer projection hurts everything. Confirms MLP = task-memorization locus, stored in low-Fisher-eigenvalue components.

## Participation Ratio Diagnostics

Per-mode participation: Ψ_k = (Σ_i c_ik)² / (n Σ_i c_ik²), with per-sample contribution c_ik = u_k^T F_i u_k.
- Ψ_k ≈ 1 → mode shared across samples (generalizing); Ψ_k ≈ 1/n → single-sample mode (memorized).
- Restricted ratios Ψ^CIFAR_k, Ψ^Gauss_k: input-noise setting → clean images dominate top modes, Gaussian noise relegated to bottom (drop ~1 order of magnitude top→bottom); label-noise setting → corrupted and uncorrupted samples contribute in a CONSTANT ratio across the whole spectrum (no spectral separation for label noise, yet layerwise projection still works).
- Single-sample Fisher projection ("sample projection"): project out top eigenvectors of F_i to remove one sample. Self-hit rates drop faster for noisy samples; flipped-label samples recover TRUE labels above chance, non-monotonically in k. Side effect: removing one Gaussian sample degrades the whole Gaussian set (100% → 75.6% at k=9) — memorized content shares a subspace.

## Barcode Model (Closed Form)

Linear model isolating label-noise memorization:
- x = [s; z] ∈ R^(r+d): signal s_i = μ_i u_i (u ~ Uniform{−1,+1}^r latent signs), barcode z ~ N(0, I_d) uninformative features.
- Clean label y_i = a_i u_i; corrupted ỹ_i = η_i y_i, P(η_i=−1)=ρ_i; decomposes ỹ_i = η̄_i y_i + ξ_i with η̄_i = 1−2ρ_i (shrunk signal + zero-mean noise, Var[ξ_i|y] = a_i²(1−η̄_i²)).
- Barcode coefficient: Θ̂_z = Ξ Π_S⊥ Z^T (Z Π_S⊥ Z^T)^{-1} — pure finite-sample correlation between noise features and label noise (Π_S⊥ = complement of informative row space); vanishes as n→∞.
- **Risk reduction from post-hoc barcode deletion**: ΔR = Tr Σ_ξ · d/(n−r−d−1), valid for n−r>d+1 — exactly the variance a d-dimensional regression accumulates fitting pure noise with n−r effective samples. Verified vs simulation at (n,r,d)=(500,4,250), 200 replicates.
- **Interior-optimal rank**: when an informative feature's population variance μ_j² falls below the spectral separation threshold 1 + d/(n−r), its empirical eigenvector merges into the barcode bulk. At high flip rates an interior-optimal retained rank emerges (deleting barcode directions removes more memorization variance than the signal it sacrifices); at low flip rates full rank is best.

## Practical Recipes

- Audit for memorization: diagonalize per-layer Fishers on CLEAN held-out data; plot accuracy vs k for clean vs suspect-memorized samples; separation in EARLY layers = memorized content stored there.
- De-memorize without retraining: project early/penultimate layers onto the top-k Fisher span; skip the last layer (no separation there).
- Recover true labels of flipped samples: top-k Fisher projection raises true-label accuracy above chance.
- Remove one specific sample: single-sample Fisher eigenvector removal (partial; subspace shared with other memorized samples).
- Caveats: de-memorization ≠ unlearning (no fine-grained per-sample deletion); ignores cross-layer correlations; may not transfer qualitatively to LLM scale or semantic/compositional memorization.

## Connection Map

- Merullo et al. 2025 (arXiv:2510.24256): top Fisher modes = reasoning structure, low-curvature modes = memorized samples in LMs — this work extends controlled-noise validation to vision + ICL.
- Adversarial memorizing-vs-generalizing circuits in ICL transformers: interference "hides" generalization capacity; Fisher projection partially releases it WITHOUT retraining.
- Benign overfitting: barcode model is a controlled instance — fitting pure noise adds variance d/(n−r−d−1); deleting uninformative directions after fitting reduces risk.
- Hyperribbon geometry: the non-local parameter-space projection may be a small perturbation in function space via soft directions (open hypothesis).

**Activation**: fisher information, memorization, de-memorization, fisher eigenspectrum projection, label noise recovery, in-context learning overfitting, participation ratio, benign overfitting, model editing, task memorization, single-sample fisher