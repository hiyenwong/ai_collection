---
name: eeg-source-imaging-fem
version: 1.0.0
description: "Forward-Inverse interplay analysis in FEM-based EEG source imaging. Studies how forward models and inverse methods interact to affect spatial distribution of reconstructed brain activity. Proposes distributional signatures for evaluating source imaging reliability. arXiv:2604.20448."
date: 2026-04-23
arxiv_id: "2604.20448"
authors: "Santtu Söderholm, Joonas Lahtinen, Sampsa Pursiainen"
categories: "math.NA"
activation:
  - EEG source imaging
  - FEM forward model
  - inverse problem
  - source localization
  - brain activity reconstruction
  - dipole estimation
  - forward-inverse interplay
---

# Forward-Inverse Interplay in FEM-Based EEG Source Imaging

## Overview
EEG source imaging aims to infer brain activity from scalp potentials. This paper studies the critical interplay between forward models (FEM-based) and inverse solvers, focusing not only on source localization accuracy but also on the **spatial distribution** of reconstructed activity (distributional signatures).

## Key Methodology

### Forward Model (FEM)
- Finite Element Method models electrical potential propagation through head tissues
- Accurate geometry from MRI: scalp, skull, CSF, gray matter, white matter
- Lead field matrix L maps source configurations to scalp measurements

### Inverse Methods
- Minimum Norm Estimate (MNE): minimizes L2 norm of sources
- LORETA: smoothness-constrained minimum norm
- Beamforming: adaptive spatial filtering

### Distributional Signatures
- Evaluate not just *where* activity peaks, but *how it spreads*
- Forward model choice affects spatial spread of inverse solutions
- Different inverse methods produce characteristically different distributions even with same forward model

### Implementation Steps
1. Construct FEM head model from structural MRI
2. Compute lead field matrix for source space
3. Select inverse method and regularization parameters
4. Analyze distributional properties (spread, focality, depth bias)
5. Validate forward-inverse combination against known source configurations

## Key Insights
- Forward and inverse choices are not independent — their interplay determines result quality
- Distributional analysis reveals systematic biases invisible to peak-localization metrics
- Essential for clinical applications (epilepsy focus localization, pre-surgical planning)

## Pitfalls
- FEM mesh quality strongly affects forward model accuracy
- Skull conductivity values are often uncertain
- Regularization parameter selection is critical and often subjective
- Distributional signatures require ground truth for validation

## References
- arXiv: [2604.20448](https://arxiv.org/abs/2604.20448)
- Key terms: EEG, source imaging, FEM, inverse problem, forward model, dipole localization, brain activity mapping
