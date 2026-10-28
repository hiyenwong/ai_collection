---
name: counterfactual-brain-network-augmentation
description: Use when building counterfactual brain network augmentation.
category: ai_collection
trigger: counterfactual brain network, fMRI augmentation, ASD diagnosis, module-number constraint, Laplacian spectral similarity, label-altered augmentation, ABIDE, self-explainable diagnosis
---

# CFBrainAug — Counterfactual Brain Network Augmentation for fMRI Diagnosis

Methodology from arXiv:2610.32184 (Qiao & Li, UVA, Oct 2026, cs.LG): unify data augmentation and
ounterfactual explanation by learning **label-altered** brain networks. A lightweight SVM pipeline with
counterfactual augmentation matches recent graph deep learning (BrainGNN/STGCN/GoFormer/Miniformer) on
small-sample rs-fMRI classification (ABIDE I ASD: 74.1% ACC / 79.2% AUC on NYU site), while the
factual↔counterfactual connectivity difference ∆A provides intrinsic (non-post-hoc) explanations.

## Core definitions
- **Counterfactual brain network**: `G_cf = argmin_{G'} d(G, G')` s.t. `f(G') ≠ f(G)` and G' satisfies prior P
- **Counterfactual explanation**: `∆A = A_cf − A` — the minimal connectivity changes that switch the diagnosis

## Pipeline

### 1. Brain network construction
`A_ij = |Pearson r_ij|`, `A_ii = 0` (non-negative weights → PSD graph Laplacian). Node features X = BOLD
time series per ROI (AAL-116 or CC200-200 parcellation).

### 2. Candidate counterfactual retrieval
For subject G with label y, retrieve the **label-opposite** (1−y) training sample closest in **graph Laplacian
similarity**. Per-site retrieval controls site/scanner confounds (candidate shares acquisition protocol).

### 3. Multi-constraint refinement (Transformer + MLP, end-to-end)
Transformer layers map retrieved candidate → node features X_cf; an MLP on paired node features → sigmoid
edge probabilities A_cf. Objective:

`L_ref = L_mod + λ1·L_topo + λ2·L_sem`   — **no classifier term** (label flip comes from the
opposite-label initialization and is maintained by L_sem, not by a classifier in the loop)

1. **Module-number constraint** (neurobiological plausibility — brain nets are dense intra-/sparse inter-module):
   `L_mod = min_{F∈R^{m×k}, FᵀF=I} Tr(Fᵀ L_cf F)`
   By Ky Fan's theorem this equals the sum of the k smallest Laplacian eigenvalues; a non-negative graph has
   ≥k connected components iff its k smallest Laplacian eigenvalues are zero. Pushes toward k modules (k=8).
2. **Individual topology preservation**: `L_topo = Σ_{i=1}^{M} |λᵢ(L̃) − λᵢ(L̃_cf)|` on NORMALIZED Laplacian
   eigenvalues — anchors the counterfactual to this subject's global spectrum, preventing drift to other subjects.
3. **Counterfactual semantic consistency**: `L_sem = ‖X_cf − X_ε‖_F + BCE(A_cf, A_ε)` — keep label-opposite semantics
   of the retrieved candidate (both A_cf and A_ε in [0,1] so BCE is well-defined).

### 4. Counterfactual-enhanced diagnosis
Augmented training set = factual + counterfactual, balanced by sample weights `W_total = W_orig + λ·W_cf` (λ=1).
Features: vectorized upper-triangular adjacency → SelectKBest (K=100) → RBF-SVM (C=0.5).
Explanations: group-level average |∆A| and per-ROI perturbation strength `sᵢ = Σⱼ |∆A_ij|`.

## Verified results (ABIDE I, 10× stratified 5-fold CV, per-site)
| Site | ACC | AUC | vs. best baseline |
|------|-----|-----|-------------------|
| NYU | 74.1% | 79.2% | GoFormer 72.5% |
| UM | 75.5% | 78.9% | TimeWarping 73.3% |
| LEUVEN | 72.4% | 78.6% | NodeDropping 69.8% |

- Beats label-preserving augmentations (window slicing, time warping, node dropping, edge perturbation)
  AND counterfactual baselines (CF-GNNExplainer edge-deletion, Abrate & Bonchi nearest opposite-class search)
  — those minimal-edit counterfactuals stay too close to the original and barely help (66-68% on NYU).
- Ablations (NYU ACC): full 74.1 / w/o ModularConstraint 66.8 / w/o Refine 67.4 / w/o CounterfactualAug 66.3 —
  every component matters; the modular prior is the largest single contributor.
- Counterfactual quality: Label-Flipping Rate 66.9% (encouraged, not enforced), Topological Similarity 87.1%,
  Module-Number Preservation 60.0%.
- Biomarkers recovered: insula, SMA, precentral (group-level); top-10 connections in sensorimotor, DMN,
  subcortical–cerebellar circuits — consistent with ASD literature.
- Hyperparameters: ACC/AUC peak at k = 8 modules (small k under-constrains, large k over-fragments), λ = 1.

## When to use
- Small-sample brain-network classification (fMRI/EEG connectomes) where GNNs overfit
- Augmentation that must cross the decision boundary (label-altered) rather than re-sample intra-class variability
- Self-explainable diagnosis: “which minimal connectivity changes would flip this subject's label?”
- Generating candidate biomarkers (|∆A| ranking) for clinical follow-up

## Implementation notes
- Restrict the retrieval pool to the training fold (no test leakage in retrieval/refinement).
- Even-degree spectral terms: use normalized Laplacian L̃ = I − D^(−1/2) A D^(−1/2) for L_topo; PSD raw L for L_mod.
- k-module trace minimization: compute eigendecomposition of L_cf, sum k smallest eigenvalues (differentiable via torch.linalg.eigh low-k or LOBPCG for scale).
- Class imbalance (NC-majority) biases toward specificity; report SEN/SPE separately (CFBrainAug SPE-best, SEN not).

## Pitfalls
- Label flip is NOT guaranteed (LFR 66.9%) — classifier-free objective is a soft constraint; add a classifier-guided
  flip term if hard flips are needed (paper's own future work).
- Module constraint trades off against L_topo/L_sem (MPR 60%) — adaptive loss weighting can improve it.
- Validated within-site only (64-184 subjects/site); multi-site generalization unverified.
- BCE on A requires both matrices in [0,1] — raw correlations must be absolute-valued (|r_ij|), not signed.

## References
- arXiv:2610.32184 — CFBrainAug source paper
- Ky Fan 1949 — trace minimization = sum of k smallest eigenvalues
- Abrate & Bonchi 2021 — counterfactual graphs for brain-network explanation (post-hoc only)
- CF-GNNExplainer 2022 — edge-deletion counterfactuals for GNNs
- Han et al. 2026 — do graph DL models help small functional connectome datasets? (motivates SVM choice)
