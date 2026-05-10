---
name: multi-scale-info-geometry-neural
category: ai_collection
description: Multi-scale information geometry framework for analyzing neural population codes. Extends Fisher information metric to capture encoding structure from fine stimulus details to coarse global distinctions. Relates representational geometry to mutual information via diffusion model estimation.
created: 2026-05-09
updated: 2026-05-11
source: arXiv 2605.06304
---

# Multi-Scale Information Geometry for Neural Population Analysis

## Overview

Methodology from arXiv:2605.06304 (Azeglio, Laquitaine, Ferrari & Chalk, 2026) that derives a unique Riemannian representational geometry from first principles of how information contracts under stimulus coarse-graining. Provides a principled, information-theoretic framework for characterizing neural population codes.

**arXiv**: 2605.06304 (May 2026)

## Core Problem

Neural population coding analysis faces a fundamental ambiguity: different constructions of representational distances lead to qualitatively different conclusions about the neural code. There is no principled way to choose the "right" geometry for analyzing how populations encode stimuli.

## Key Insight

A **unique Riemannian representational geometry** emerges from first principles: distances should contract predictably as stimulus resolution is lost through coarse-graining. This yields a multi-scale extension of the Fisher information metric that:

1. **Is uniquely determined** by how information contracts under coarse-graining
2. **Directly relates to mutual information**: well-encoded stimulus directions are expanded, poorly encoded directions are contracted
3. **Is practically estimable** using diffusion models for large populations and high-dimensional stimuli
4. **Yields interpretable features**: eigenvectors of the metric tensor identify stimulus variations contributing most to information transmission

## Mathematical Framework

### Fisher Information Metric (Classical)

For a parametric neural response model p(r|s):

```
g_ij(s) = E_p(r|s)[∂log p(r|s)/∂s_i · ∂log p(r|s)/∂s_j]
```

This defines a local distance on stimulus space based on how distinguishable nearby stimuli are from neural responses.

### Multi-Scale Extension

The multi-scale geometry extends the Fisher metric across scales:

```
G(s, σ) = coarse-grained Fisher metric at scale σ
```

Where σ parameterizes the degree of stimulus coarse-graining. As σ → 0, recovers the classical Fisher metric. As σ increases, captures global stimulus structure.

### Information-Geometry Relationship

The metric tensor eigenvalues directly relate to mutual information:

```
I(S; R) ≈ (1/2) · E[log det G(s)] + const
```

- **Large eigenvalues** → well-encoded directions → contribute more to mutual information
- **Small eigenvalues** → poorly encoded directions → contracted in the geometry

### Diffusion Model Estimation

For large neural populations and high-dimensional stimuli, the metric tensor can be estimated using diffusion models (score-based approach):

```python
def estimate_metric_tensor(neural_responses, stimuli):
    """Estimate the multi-scale Fisher information metric tensor.
    Uses diffusion models to approximate the local geometry without explicit density estimation."""
    # 1. Fit diffusion model to neural response distribution
    # 2. Estimate score function ∇_s log p(r|s)
    # 3. Compute Fisher information: g_ij = E[∂_i log p · ∂_j log p]
    # 4. Apply multi-scale coarse-graining
    # 5. Return metric tensor and spectral decomposition
    pass
```

## Key Contributions

1. **Unique Geometry**: Riemannian metric uniquely determined by coarse-graining principles
2. **Information Link**: Direct relationship between geometry and mutual information
3. **Practical Estimation**: Diffusion model-based approach for large populations
4. **Interpretable Features**: Eigenvectors identify stimulus dimensions with highest information transmission

## Application Triggers

Use this skill when:
- Characterizing neural population codes with principled geometry
- Identifying which stimulus dimensions carry most information
- Comparing information structure across brain areas or species
- Evaluating DNN-brain alignment at the information-geometric level
- Analyzing how coding changes with learning, development, or disease

## Key Concepts

- Fisher information metric
- Statistical manifolds
- Coarse-graining in neural systems
- Multi-scale analysis
- Neural population dynamics
- Information geometry
- Representational geometry
- Mutual information decomposition
- Diffusion model estimation

## Related Skills

- `neural-population-dynamics`
- `neural-code-dynamics-analysis`
- `geometric-brain-dynamics-mapping-v7`
- `decoding-encoding-alignment-critique` (complementary: decoding vs encoding analysis)
