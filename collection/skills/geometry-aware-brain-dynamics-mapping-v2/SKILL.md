---
name: geometry-aware-brain-dynamics-mapping-v2
description: "Geometric Basis Functions (GBF) v2 framework for noninvasive whole human brain dynamics mapping. Incorporates individual cortical geometry for accurate spatiotemporal reconstruction at orders of magnitude faster than deep learning."
---

# Geometry-Aware Framework for Whole Human Brain Dynamics Mapping v2

> Enhanced geometric basis functions (GBF) framework for modeling whole-brain cortical dynamics with individual anatomical geometry, achieving orders of magnitude speedup over deep learning while maintaining high reconstruction accuracy.

## Metadata
- **Source**: arXiv:2604.25592
- **Authors**: Song Wang, Kexin Lou, Chen Wei
- **Published**: 2026-04-28

## Core Methodology

### Key Innovation
Non-invasive electrophysiology (EEG, fMEG) lacks methods that accurately reconstruct whole-brain spatiotemporal dynamics while incorporating individual cortical geometry. The GBF v2 framework:
1. Uses geometric basis functions to model cortical surface dynamics
2. Incorporates individual anatomical geometry via cortical surface parameterization
3. Achieves real-time reconstruction without deep learning overhead
4. Maintains interpretability through explicit geometric modeling

### Technical Framework
1. **Cortical Geometry Parameterization**: Individual anatomical surfaces to geometric basis
2. **Spatiotemporal Basis Functions**: Separable spatial and temporal components
3. **Source Reconstruction**: Direct solution without iterative optimization
4. **Real-time Processing**: Efficient matrix operations enable online analysis

## Implementation Guide

### Prerequisites
- MNE-Python for EEG/fMEG processing
- Surface mesh processing (nibabel, trimesh)
- Linear algebra libraries (scipy, numpy)

### Step-by-Step
1. Load individual anatomy (MRI-derived cortical surface)
2. Compute geometric basis functions on cortical mesh
3. Project sensor data to geometric basis coefficients
4. Reconstruct cortical dynamics via basis superposition
5. Visualize spatiotemporal patterns on individual anatomy

### Code Example
```python
import numpy as np
import scipy.sparse.linalg

def compute_geometric_basis(surface_mesh, n_basis=100):
    """Compute geometric basis functions on cortical surface using Laplace-Beltrami"""
    L = compute_laplacian_matrix(surface_mesh)
    eigenvalues, eigenvectors = scipy.sparse.linalg.eigsh(L, k=n_basis, sigma=0)
    return eigenvectors

def reconstruct_dynamics(sensor_data, forward_model, basis_funcs):
    """Reconstruct cortical dynamics using GBF"""
    G = forward_model @ basis_funcs
    coefficients = np.linalg.lstsq(G, sensor_data, rcond=None)[0]
    cortical_activity = basis_funcs @ coefficients
    return cortical_activity
```

## Applications
- Real-time brain monitoring: Clinical applications requiring immediate feedback
- Individual neuroanatomy: Personalized medicine with subject-specific models
- Large-scale studies: Efficient processing of population datasets
- BCI applications: Low-latency decoding for neuroprosthetics

## Pitfalls
- Requires individual anatomical MRI for optimal geometry incorporation
- Basis function count trades off between accuracy and computational cost
- May underperform for highly focal sources

## Related Skills
- geometric-brain-dynamics-mapping
- geometric-brain-dynamics-mapping-gbf
- geometric-brain-dynamics-mapping-v3
