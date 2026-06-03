---
name: neuroimaging-feature-whitening
version: 1.0.0
description: "Feature whitening approach for improving clinical interpretability of linear neuroimaging models. Decorrelates input brain region features before model fitting so weights reflect individual region contributions rather than shared correlations. Enables clinically meaningful biomarker maps. arXiv:2604.20675."
date: 2026-04-23
arxiv_id: "2604.20675"
authors: "Sara Petiton, Antoine Grigis, Raphaël Vock, Edouard Duchesnay"
categories: "cs.LG"
activation:
  - neuroimaging interpretability
  - feature whitening
  - linear model biomarker
  - brain region correlation
  - clinical neuroimaging
  - MRI weight interpretation
  - decorrelation brain
---

# Improving Clinical Interpretability of Linear Neuroimaging Models Through Feature Whitening

## Overview
Linear models in computational neuroimaging suffer from weight interpretability issues due to inherent correlations between brain regions (e.g., bilateral homologous structures). This paper proposes **feature whitening** applied prior to model fitting to decorrelate input features, enabling weights that reflect individual region contributions.

## Key Methodology

### The Problem
- Linear model weights in neuroimaging reflect shared correlations between brain regions
- Homologous left/right hemisphere structures are strongly correlated
- Weights don't yield clinically meaningful region-specific insights

### Feature Whitening Solution
1. **Compute covariance matrix** of input features (brain region measurements)
2. **Apply ZCA whitening transform**: `X_whitened = X @ Σ^(-1/2)` where Σ is the covariance matrix
3. **Fit linear model** on whitened features
4. **Interpret weights** as individual region contributions

### Algorithm Steps
1. Standardize features (zero mean, unit variance)
2. Compute empirical covariance matrix Σ
3. Eigen-decompose: Σ = U Λ U^T
4. Whitening transform: W = U Λ^(-1/2) U^T (ZCA) or W = Λ^(-1/2) U^T (PCA whitening)
5. Transform inputs: X_w = X @ W
6. Fit linear model on X_w
7. Map weights back to original space for interpretation

## Implementation Guidance
- Use ZCA whitening (Mahalanobis) to preserve spatial proximity of features
- Regularize covariance inversion with small epsilon to handle near-singular matrices
- Validate on held-out clinical data with known ground-truth biomarkers

## Advantages
- Clinically meaningful weight maps
- No change to model architecture — preprocessing only
- Applicable to any linear model (SVM, logistic regression, linear regression)
- Preserves predictive performance while improving interpretability

## Pitfalls
- Whitening amplifies noise in low-variance directions
- Requires careful regularization of covariance inversion
- May not generalize well across scanners/sites without harmonization
- Interpretation still requires clinical domain expertise

## References
- arXiv: [2604.20675](https://arxiv.org/abs/2604.20675)
- Key terms: neuroimaging, feature whitening, linear models, biomarker discovery, clinical interpretability, brain regions
