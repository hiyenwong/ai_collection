---
name: geometry-aware-brain-dynamics-mapping-v7
description: "Enhanced Geometry-Aware Brain Dynamics Mapping using Geometric Basis Functions (GBF) for noninvasive whole-brain spatio-temporal dynamics mapping. Covers basis function construction on brain manifolds, spectral decomposition for multi-scale neural dynamics, and handling of individual anatomical variability. Use when: working with noninvasive brain mapping, fMRI/MEG/EEG source localization, geometric basis functions, brain manifold analysis, whole-brain spatio-temporal modeling, or individual anatomy-aware neural dynamics."
---

# Geometry-Aware Brain Dynamics Mapping v7 (GBF)

Enhanced framework for noninvasive whole-brain spatio-temporal mapping using geometric basis functions derived from brain manifold structure.

## Paper Reference

**Title:** A geometry aware framework enhances noninvasive mapping of whole human brain dynamics
**arXiv:** 2604.25592v1
**Authors:** Song Wang, Kexin Lou, Chen Wei, et al.
**Published:** 2026-04-28

## Core Methodology

### Geometric Basis Functions (GBF)

GBFs are constructed from the brain manifold geometry:

1. **Manifold Construction**: Extract cortical surface mesh from structural MRI
2. **Laplace-Beltrami Operator**: Compute eigenfunctions of the LB operator on the manifold
3. **Basis Selection**: Select GBFs that optimally capture target spatial scales
4. **Spectral Projection**: Project neural activity onto GBF basis for compact representation

### Spectral Decomposition

Multi-scale neural dynamics are decomposed using GBF spectrum:

- **Low-frequency GBFs**: Capture large-scale global brain patterns
- **Mid-frequency GBFs**: Represent mesoscale network interactions
- **High-frequency GBFs**: Encode fine-grained local activity

### Key Advantages over v6

- Improved individual anatomical variability handling
- Enhanced spectral decomposition for multi-scale dynamics
- Better regularization for ill-posed inverse problems
- More efficient basis function selection strategy

## Implementation Steps

### Step 1: Manifold Extraction

```python
import nibabel as nib
import numpy as np

# Load structural MRI
mri = nib.load('structural.nii.gz')
# Extract cortical surface (using FreeSurfer or similar)
# vertices, faces = extract_surface(mri)
```

### Step 2: Laplace-Beltrami Eigenfunctions

```python
from scipy.sparse.linalg import eigsh

# Build LB operator from mesh (cotangent weights)
# L = build_laplacian(vertices, faces)
# eigenvalues, eigenvectors = eigsh(L, k=n_basis, which='SM')
# GBFs = eigenvectors  # Each column is a basis function
```

### Step 3: Neural Activity Projection

```python
# Project fMRI/MEG data onto GBF basis
# activity: (n_vertices, n_timepoints)
# coefficients = GBFs.T @ activity  # (n_basis, n_timepoints)
# Reconstruct: reconstructed = GBFs @ coefficients
```

### Step 4: Multi-scale Analysis

```python
# Split GBFs by frequency bands
# low_freq = GBFs[:, :k1]   # Global patterns
# mid_freq = GBFs[:, k1:k2]  # Network-level
# high_freq = GBFs[:, k2:]   # Local details

# Analyze temporal dynamics at each scale separately
```

## Use Cases

- **fMRI source localization**: Map scalp/voxel data to cortical manifold
- **MEG/EEG inverse problem**: Solve using GBF-regularized approach
- **Individual variability**: Account for anatomical differences in group studies
- **Multi-scale dynamics**: Analyze brain activity at different spatial resolutions

## Mathematical Foundation

The Laplace-Beltrami operator on a manifold M:

$$\Delta_M f = \text{div}(\nabla_M f)$$

Eigenvalue problem: $\Delta_M \phi_k = -\lambda_k \phi_k$

The GBFs $\{\phi_k\}$ form an orthonormal basis for $L^2(M)$.

## Related Skills

- [[geometric-brain-dynamics-mapping]] (v1)
- [[geometric-brain-dynamics-mapping-v2]] (v2)
- [[brain-dit-fmri-foundation-model]] (fMRI foundation models)
