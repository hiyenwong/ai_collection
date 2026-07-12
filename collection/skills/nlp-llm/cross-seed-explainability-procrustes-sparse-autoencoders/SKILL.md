---
name: cross-seed-explainability-procrustes-sparse-autoencoders
description: "Procrustes-conditioned Joint End-to-end Top-K SAE for extracting cross-seed universal features from independently trained BERT models. Combines Top-K sparsity, end-to-end optimization, and dead-feature revival. Pearson r ≥ 0.70 across seeds. Activation: sparse autoencoder, cross-seed universality, Procrustes alignment, mechanistic interpretability, feature universality."
metadata:
  arxiv_id: "2607.08499"
  published: "2026-07-09"
  authors: "Bendegúz Váradi, Zoltán Kmetty"
  tags: [sparse-autoencoder, cross-seed-universality, procrustes-alignment, mechanistic-interpretability, feature-universality]
---

# Cross-seed Explainability using Procrustes-conditioned Joint End-to-end Top-K Sparse Autoencoders

## Overview

Cross-seed feature universality is a fundamental challenge in mechanistic interpretability: independently trained networks learn misaligned feature spaces due to random initialization. This paper presents a Procrustes-conditioned Joint End-to-end Top-K Sparse Autoencoder (SAE) that addresses this by computing an orthogonal Procrustes rotation before joint SAE training.

## Key Innovations

### Procrustes-Conditioned Alignment
- Computes orthogonal Procrustes rotation between seeds' activation spaces before joint training
- Aligns feature spaces that differ by random initialization
- Enables meaningful cross-seed feature comparison

### Joint End-to-End Top-K SAE
- Combines Top-K sparsity for representational efficiency
- End-to-end downstream optimization for task-relevant features
- Auxiliary dead-feature revival loss based on prior SAE literature

### Universal Feature Extraction
- Evaluated on five independent seed pairs (ten BERT models)
- Three benchmark datasets: SST-2, Stanford Politeness, TweetEval Emotion
- Produces more universal features (Pearson r ≥ 0.70 across seeds) than post-hoc alignment
- High-universality features encode interpretable sociolinguistic patterns

## Methodology

1. **Procrustes Rotation**: Compute orthogonal rotation between seed activation spaces
2. **Joint SAE Training**: Train Top-K SAE end-to-end with aligned activations
3. **Dead-Feature Revival**: Auxiliary loss to prevent feature death
4. **Universality Evaluation**: Measure cross-seed Pearson correlation
5. **Qualitative Analysis**: Verify interpretable patterns in high-universality features

## Implications

- Feature universality across seeds is achievable with proper alignment
- Procrustes conditioning is more effective than post-hoc alignment
- Universal features encode meaningful sociolinguistic patterns
- Advances mechanistic interpretability toward reliable cross-model comparison

## Pitfalls

- Procrustes rotation assumes linear alignment which may not hold for all layers
- Top-K sparsity introduces a hyperparameter that affects feature quality
- Evaluation limited to BERT models — generalization to other architectures unclear
- Qualitative analysis is minimal and needs broader validation

## Activation Keywords

sparse autoencoder, cross-seed universality, Procrustes alignment, mechanistic interpretability, feature universality, Top-K SAE, BERT, dead-feature revival

## Paper Reference

arXiv:2607.08499 - "Cross-seed Explainability using Procrustes-conditioned Joint End-to-end Top-K Sparse Autoencoders" (Jul 2026)
