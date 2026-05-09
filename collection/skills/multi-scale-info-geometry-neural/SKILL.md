---
name: multi-scale-info-geometry-neural
description: Multi-scale information geometry framework for analyzing neural population codes using Riemannian geometry. Extends Fisher information metric across scales via coarse-graining, relates geometry to mutual information, and uses diffusion models for estimation. Use when analyzing neural encoding, representational geometry, mutual information in neural data, Fisher information metric, population coding, or coarse-graining in neural systems.
---

# Multi-Scale Information Geometry for Neural Populations

Based on: *Azeglio, Laquitaine, Ferrari, Chalk (2026)* — arXiv:2605.06304

## Overview

This framework defines a unique **Riemannian representational geometry** on stimulus space where distances reflect encoding fidelity, derived from first principles of how information contracts under coarse-graining.

## Core Theory

### Multi-Scale Fisher Information Metric

Standard representational geometries use arbitrary distance measures. This framework shows a **unique Riemannian metric** emerges from coarse-graining axioms:

1. Define stimulus space metric at scale α
2. Coarse-graining contracts distances monotonically
3. The resulting metric is a multi-scale extension of the Fisher information metric:

```
g_μν(θ) = E[∂_μ log p(x|θ) · ∂_ν log p(x|θ)]
```

where the metric at each scale captures encoding structure from fine details to global distinctions.

### Mutual Information Duality

The metric tensor is **exactly related to mutual information**:
- **Well-encoded directions** (high MI contribution) → expanded in geometry
- **Poorly-encoded directions** (low MI contribution) → contracted in geometry

This provides direct geometric interpretation of information transmission.

### Diffusion Model Estimation

For large populations, estimate the metric tensor using **diffusion models**:

```python
def estimate_metric_from_diffusion(neural_data, stimulus_labels):
    """
    Estimate Fisher information metric tensor from neural population data.
    
    Args:
        neural_data: N x T matrix of neural responses
        stimulus_labels: T x D matrix of stimulus features
    
    Returns:
        metric_tensor: D x D Fisher information metric at each scale
        eigenvalues: Eigenvectors sorted by information contribution
    """
    # 1. Train diffusion model on neural-stimulus pairs
    # 2. Compute score function ∇_θ log p(x|θ)
    # 3. Metric = E[score · score^T] via Monte Carlo
    pass
```

## Workflow

### 1. Data Preparation
- Neural population responses (spike counts, calcium, etc.)
- Stimulus labels/features
- Define coarse-graining scales (resolution levels)

### 2. Metric Estimation
- Fit probabilistic model p(response|stimulus)
- Compute Fisher information at each scale
- Extract eigenvalues/eigenvectors of metric tensor

### 3. Interpretation
- **Principal eigenvectors**: Stimulus variations contributing most to information
- **Eigenvalue spectrum**: Distribution of encoding precision across directions
- **Scale dependence**: How encoding changes with resolution

### 4. Validation
- Robustness to modeling choices
- Comparison across brain regions/conditions
- Information-theoretic bounds verification

## Key Results

Applied to **visual cortical responses to natural images**:
- Eigenvectors identify interpretable, information-carrying stimulus features
- Results robust to modeling choices
- Framework bridges encoding models with information theory

## Practical Applications

| Task | Method |
|------|--------|
| Compare neural codes | Compare metric tensors across populations |
| Identify informative features | Top eigenvectors of metric |
| Quantify information loss | Trace of metric under coarse-graining |
| Optimize stimuli | Gradient ascent on information metric |

## References

- [arXiv:2605.06304](https://arxiv.org/abs/2605.06304) — Full paper
- Related: `information-geometry`, `neural-coding`, `representational-similarity`

## Activation Keywords

`information geometry`, `Fisher information`, `neural coding`, `representational geometry`, `mutual information`, `coarse-graining`, `Riemannian metric`, `population coding`, `diffusion model estimation`
