---
name: "riemannian-fmri-correlation-manifolds"
title: "Riemannian Geometry for fMRI: Modeling Correlation Manifolds and Eigenvector Subspaces"
arxiv_id: "2605.22334"
authors: "Mario Severino, Manuela Moretto, Robert A. McCutcheon, Mattia Veronese"
published: "2026-05-21"
category: "cs.LG"
type: "research"
description: "Scalable geometric framework for fMRI functional connectivity analysis using the Off-log Riemannian metric on correlation manifolds and Grassmannian subspace discrimination for eigenvector analysis. Validated on Parkinson's, psychosis, and ageing datasets."
activation: "fMRI functional connectivity, Riemannian geometry, correlation manifold, Off-log metric, Grassmannian discriminant analysis, brain network analysis"
---

# Riemannian Geometry for fMRI: Correlation Manifolds and Eigenvector Subspaces

Methodology from arXiv:2605.22334 — a scalable Riemannian-geometric framework for fMRI brain network analysis using the Off-log metric on correlation matrices and Grassmannian subspace discrimination.

## Overview

Standard analysis of fMRI correlation matrices treats entries independently, ignoring the curved geometry of correlation space. This paper introduces two complementary geometric tools:

1. **Off-log metric**: A smooth, closed-form transformation mapping correlation matrices to symmetric zero-diagonal matrices, enabling standard Euclidean statistics on correlation data without complex manifold optimization.
2. **Grassmannian subspace discrimination**: Compares subjects via principal-angle distances between eigenvector subspaces, resolving sign and basis ambiguities.

Validated on Parkinson's disease, psychosis, and three ageing fMRI cohorts.

## Key Components

### 1. Off-log Metric on the Correlation Manifold

**Problem**: Correlation matrices (elliptope) have curved geometry — Euclidean averages of correlation matrices don't stay in correlation space.

**Off-log solution**: A log-Euclidean-style metric that:
- Maps correlation matrix C → S = Off-log(C) = log(C) - diag(log(C))
- Produces symmetric zero-diagonal matrices (off-log space)
- Enables closed-form expressions for:
  - Geodesic distances
  - Fréchet means (geometric averages)
  - Linear models on correlation data
- Permutation-invariant: independent of ROI ordering
- No complex manifold optimization required

### 2. Grassmannian Subspace Discrimination

**Problem**: Eigenvector comparisons suffer from sign ambiguity and basis rotation ambiguity.

**Grassmannian solution**: Treat principal subspaces (first k eigenvectors) as points on a Grassmannian manifold:
- Compare via principal angles between subspaces
- Natural distance metrics: projection distance, Bures distance
- Removes sign and basis ambiguities
- Applied to graph Laplacian eigenvectors from fMRI correlation matrices

### 3. Validation Results

**Hypothesis testing** (permutation tests):
- Off-log metric increases sensitivity by 2-3x over Euclidean baseline
- Detects significant group differences where Euclidean methods fail

**Brain age prediction**:
- Off-log comparable to Riemannian and Euclidean baselines
- Riemannian metrics excel in 2 of 3 cohorts

**Classification** (Parkinson's, psychosis):
- Off-log matches or exceeds baselines
- Grassmannian method consistently outperforms Euclidean

**Grassmannian discriminant analysis**:
- Consistently outperformed Euclidean baselines
- Highlights disease-relevant brain networks
- Reveals interpretable spatial patterns

## Datasets Used

1. **Parkinson's disease**: Clinical cohort (22 PD, 22 controls)
2. **Non-affective psychosis**: Clinical cohort (26 psychosis, 26 controls)
3. **Healthy ageing (3 cohorts)**: 
   - Cambridge (120 young, 120 old)
   - OASIS (286 young, 134 old)
   - IXI (175 young, 214 old)

## Implementation Guide

### Off-log Metric

```python
import numpy as np
from scipy.linalg import logm

def off_log_metric(C):
    """Map correlation matrix C to off-log space."""
    # C must be a valid correlation matrix (SPD, unit diagonal)
    L = logm(C)  # Matrix logarithm
    S = L - np.diag(np.diag(L))  # Remove diagonal
    return S  # Symmetric zero-diagonal matrix

def off_log_distance(C1, C2):
    """Compute geodesic distance between two correlation matrices."""
    S1, S2 = off_log_metric(C1), off_log_metric(C2)
    return np.linalg.norm(S1 - S2, 'fro')

def off_log_frechet_mean(matrices):
    """Compute Frechet mean of correlation matrices."""
    S_list = [off_log_metric(C) for C in matrices]
    S_mean = np.mean(S_list, axis=0)
    return S_mean
```

### Grassmannian Discriminant Analysis

```python
from scipy.linalg import svd

def grassmannian_distance(U1, U2):
    """Compute principal-angle distance between subspaces."""
    # U1, U2 are orthonormal basis matrices (n x k)
    _, s, _ = svd(U1.T @ U2)  # Principal angles
    # Projection distance
    return np.sqrt(len(s) - np.sum(s**2))
```

## Key Findings

1. **Geometry-aware representations** improve sensitivity and predictive performance in fMRI analysis
2. **Off-log metric** provides a scalable, closed-form alternative to full Riemannian optimization
3. **Grassmannian method** reveals disease-relevant network patterns invisible to Euclidean methods
4. **Both methods** integrate seamlessly into standard ML workflows

## Applications

- Functional connectivity analysis (rs-fMRI)
- Clinical biomarker discovery (PD, psychosis, ageing)
- Brain age prediction
- Group comparison studies
- Disease classification from functional networks
- Subspace comparison for connectome harmonics
- Longitudinal brain network analysis

## References

- Correlation manifold (elliptope): Bhatia (2007)
- SPD manifolds: Pennec et al. (2006)
- Off-log metric: Thanwerdas & Pennec (2023)
- Grassmannian geometry: Edelman et al. (1998)
