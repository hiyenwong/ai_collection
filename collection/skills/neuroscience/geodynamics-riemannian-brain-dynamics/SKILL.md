---
name: geodynamics-riemannian-brain-dynamics
description: "GeoDynamics: Riemannian manifold framework for brain dynamics analysis. Models dynamic functional connectivity as geodesics on Riemannian manifolds, enabling geometry-aware analysis of brain state transitions. Activation: Riemannian geometry, brain dynamics, geodesic, functional connectivity, manifold learning, brain state transition."
---

# GeoDynamics: Brain Dynamics on Riemannian Manifolds

> GeoDynamics frames brain dynamics as geodesic flows on Riemannian manifolds, enabling geometry-aware analysis of dynamic functional connectivity and brain state transitions.

## Metadata
- **Source**: arXiv:2601.13570
- **Authors**: H. Wu, Y. Chen, L. Wang, D. Zhu
- **Published**: 2026-01-22
- **Category**: q-bio.NC

## Core Methodology

### Key Innovation
Traditional dynamic functional connectivity (dFC) analysis treats connectivity states as discrete or Euclidean objects. GeoDynamics reinterprets brain dynamics through **Riemannian geometry**:
1. **SPD manifold**: Covariance matrices of fMRI time series lie naturally on the symmetric positive definite (SPD) manifold
2. **Geodesic dynamics**: Brain state transitions modeled as geodesic paths rather than linear interpolation
3. **Curvature-aware metrics**: Uses Riemannian metrics (log-Euclidean, affine-invariant) that respect the geometry of connectivity space

### Technical Framework

**Step 1: SPD Matrix Extraction**
- Sliding window covariance estimation from fMRI BOLD signals
- Regularization (Ledoit-Wolf shrinkage) to ensure positive definiteness
- Result: Sequence of SPD matrices {C₁, C₂, ..., Cₜ} on the manifold

**Step 2: Riemannian Manifold Operations**
- **Log-Euclidean metric**: Log(C) maps SPD matrices to tangent space for linear operations
- **Affine-invariant metric**: Logᵪ(A, B) = logm(A^{-1/2} B A^{-1/2}) for true geodesic distance
- **Parallel transport**: Move connectivity patterns between tangent spaces preserving geometry

**Step 3: Geodesic Brain State Modeling**
- Brain state transitions follow geodesics: γ(t) = C^{1/2}(C^{-1/2} D C^{-1/2})^t C^{1/2}
- Geodesic speed ∝ distance between states (slower near stable states)
- Curvature of trajectory indicates transition abruptness

**Step 4: Geometry-Aware Clustering**
- K-means in tangent space (Fréchet mean as centroid)
- Geodesic distance-based clustering on SPD manifold
- Captures true connectivity state geometry

### Key Results
- Riemannian geodesics capture brain state transitions more accurately than Euclidean methods
- Curvature of transition paths correlates with cognitive task demands
- SPD manifold clustering reveals connectivity states missed by correlation-based methods
- Applicable to both resting-state and task-based fMRI

## Implementation Guide

### Prerequisites
- fMRI time series data (preprocessed BOLD signals)
- Python: numpy, scipy, geomstats or pyriemann for Riemannian geometry
- Understanding of differential geometry basics

### Step-by-Step
1. **Covariance estimation**: Sliding window covariances from BOLD signals
2. **SPD regularization**: Apply shrinkage to ensure positive definiteness
3. **Tangent space mapping**: Log-map covariance matrices to tangent space
4. **Geodesic computation**: Compute geodesic paths between connectivity states
5. **Transition analysis**: Analyze geodesic speed, curvature, and distance
6. **Clustering**: Riemannian k-means for state identification

### Code Example
```python
import numpy as np
from scipy.linalg import sqrtm, logm, expm

def ensure_spd(C, shrinkage=0.1):
    # Apply Ledoit-Wolf-style shrinkage to ensure SPD property.
    d = C.shape[0]
    target = np.trace(C) / d * np.eye(d)
    return (1 - shrinkage) * C + shrinkage * target

def affine_invariant_distance(A, B):
    # Affine-invariant Riemannian distance between SPD matrices.
    M = np.linalg.inv(sqrtm(A)) @ B @ np.linalg.inv(sqrtm(A))
    eigvals = np.real(np.linalg.eigvalsh(M))
    eigvals = np.maximum(eigvals, 1e-10)
    return np.sqrt(np.sum(np.log(eigvals) ** 2))

def log_map(base, point):
    # Logarithmic map from SPD manifold to tangent space at base point.
    S = np.linalg.inv(sqrtm(base))
    M = S @ point @ S
    M = ensure_spd(M)
    L = np.real(logm(M))
    return sqrtm(base) @ L @ sqrtm(base)

def exp_map(base, tangent):
    # Exponential map from tangent space at base point to SPD manifold.
    S = np.linalg.inv(sqrtm(base))
    M = S @ tangent @ S
    E = np.real(expm(M))
    return sqrtm(base) @ E @ sqrtm(base)

def geodesic(A, B, t):
    # Compute point at parameter t along geodesic from A to B.
    S = np.linalg.inv(sqrtm(A))
    M = S @ B @ S
    M = ensure_spd(M)
    L = np.real(logm(M))
    G = np.real(expm(t * L))
    return sqrtm(A) @ G @ sqrtm(A)

def riemannian_kmeans(spdmats, k=5, max_iter=50):
    # K-means clustering on SPD manifold using Fréchet mean.
    n = len(spdmats)
    labels = np.random.randint(0, k, n)
    
    for iteration in range(max_iter):
        # Compute Fréchet mean for each cluster
        centroids = []
        for c in range(k):
            cluster = [spdmats[i] for i in range(n) if labels[i] == c]
            if not cluster:
                centroids.append(spdmats[np.random.randint(n)])
                continue
            # Approximate Fréchet mean via iterative log-map averaging
            mean = cluster[0]
            for _ in range(10):
                tangent_mean = np.mean([log_map(mean, p) for p in cluster], axis=0)
                mean = exp_map(mean, 0.1 * tangent_mean)
            centroids.append(mean)
        
        # Reassign by geodesic distance
        new_labels = np.zeros(n, dtype=int)
        for i in range(n):
            dists = [affine_invariant_distance(spdmats[i], centroids[c]) for c in range(k)]
            new_labels[i] = np.argmin(dists)
        
        if np.array_equal(labels, new_labels):
            break
        labels = new_labels
    
    return labels, centroids
```

## Applications
- **Dynamic FC analysis**: Geometry-aware brain state identification
- **Brain state transition modeling**: Predict cognitive state changes via geodesic paths
- **Neuropsychiatric biomarkers**: Detect abnormal connectivity dynamics in disorders
- **Task fMRI**: Track learning-related connectivity changes on the manifold
- **Cross-subject alignment**: Use parallel transport for group-level analysis

## Pitfalls
- SPD assumption requires careful regularization of covariance estimates
- Matrix logarithm/exponential is numerically unstable for ill-conditioned matrices
- Computational cost O(n³) per matrix operation limits scalability
- Choice of Riemannian metric (log-Euclidean vs. affine-invariant) affects results
- Sliding window parameters (width, stride) still affect manifold geometry

## Related Skills
- geodynamics-geometric-state-space
- brain-state-transition-network-control
- dynamic-functional-connectivity-integration-segregation
- brain-network-controllability
