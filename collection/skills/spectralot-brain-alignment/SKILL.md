---
name: spectralot-brain-alignment
description: Fast Whole-Brain, Geometry-Aware Functional Alignment for Cross-Subject Decoding using Spectral Optimal Transport (SpectralOT) method for fMRI data analysis
---

# SpectralOT Brain Alignment Skill

This skill implements the SpectralOT method for fast whole-brain, geometry-aware functional alignment of fMRI data across subjects, enabling improved cross-subject decoding in cognitive neuroscience.

## Overview

SpectralOT is a novel functional alignment method that embeds cortical geometry into Laplace-Beltrami eigenmodes along functional data to regularize the alignment process. This approach balances aligning functional features while preserving anatomical structure, addressing the challenge of inter-individual variability in brain response patterns.

## When to Use

Use this skill when you need to:
- Perform cross-subject fMRI data alignment for group analysis
- Improve generalization of decoding models across individuals
- Preserve anatomical constraints while aligning functional data
- Process whole-brain fMRI data efficiently
- Apply optimal transport theory to neuroimaging data

## Method Overview

The SpectralOT method consists of several key components:

1. **Cortical Geometry Integration**: Uses Laplace-Beltrami eigenmodes from the cortical surface to encode geometric information
2. **Functional Embedding**: Projects fMRI data onto these geometric eigenmodes
3. **Optimal Transport Alignment**: Applies optimal transport in the embedded space to align functional data
4. **Regularization**: The geometric embedding serves as a regularizer to prevent over-alignment that destroys functional specificity

## Implementation Workflow

### 1. Data Preparation
```python
# Load fMRI data and cortical surfaces for multiple subjects
# fMRI_data: list of n_subjects arrays (timepoints x vertices)
# surfaces: list of cortical surface meshes (vertices, faces)

import numpy as np
from spectralot import SpectralOT

# Prepare data
fmri_data = [subj1_data, subj2_data, ..., subjN_data]  # Each: (timepoints, vertices)
surfaces = [subj1_surface, subj2_surface, ..., subjN_surface]  # Each: (vertices, faces)
```

### 2. Compute Laplace-Beltrami Eigenmodes
```python
# Compute Laplace-Beltrami eigenmodes for each surface
# These encode the intrinsic geometry of the cortical surface

eigenmodes = []
eigenvalues = []
for surface in surfaces:
    # Compute LB eigenmodes (typically first 50-100 modes)
    evals, evecs = compute_laplace_beltrami_eigenmodes(surface, n_modes=50)
    eigenvalues.append(evals)
    eigenmodes.append(evecs)
```

### 3. Embed Functional Data in Geometric Space
```python
# Project fMRI data onto Laplace-Beltrami eigenmodes
# This creates a geometry-aware representation of functional data

embedded_data = []
for i, (data, modes) in enumerate(zip(fmri_data, eigenmodes)):
    # Project: data (timepoints x vertices) @ modes.T (vertices x modes)
    # Result: (timepoints x modes) representation
    embedded = data @ modes.T
    embedded_data.append(embedded)
```

### 4. Apply Optimal Transport for Alignment
```python
# Initialize SpectralOT aligner
aligner = SpectralOT(
    reg=0.1,           # Regularization strength
    max_iter=100,      # Maximum OT iterations
    method='sinkhorn'  # OT solver method
)

# Fit on reference subject (typically subject 0)
aligned_data = []
reference_embedding = embedded_data[0]

for i, target_embedding in enumerate(embedded_data[1:], start=1):
    # Compute optimal transport map from reference to subject i
    transport_map = aligner.fit_transform(reference_embedding, target_embedding)
    
    # Apply transformation to get aligned data
    aligned_embedding = target_embedding @ transport_map.T
    
    # Project back to vertex space if needed
    aligned_data_i = aligned_embedding @ eigenmodes[i]
    aligned_data.append(aligned_data_i)

# Reference subject remains unchanged
aligned_data.insert(0, fmri_data[0])
```

### 5. Validate Alignment Quality
```python
# Compute inter-subject correlation (ISC) before and after alignment
from scipy.stats import pearsonr

def compute_isc(data_list):
    """Compute average pairwise correlation across subjects"""
    n_subj = len(data_list)
    correlations = []
    for i in range(n_subj):
        for j in range(i+1, n_subj):
            # Correlate time series at each vertex
            vec_corrs = [pearsonr(data_list[i][:, v], data_list[j][:, v])[0] 
                        for v in range(data_list[i].shape[1])]
            correlations.append(np.nanmean(vec_corrs))
    return np.mean(correlations)

isc_before = compute_isc(fmri_data)
isc_after = compute_isc(aligned_data)

print(f"ISC before alignment: {isc_before:.4f}")
print(f"ISC after alignment: {isc_after:.4f}")
print(f"Improvement: {isc_after - isc_before:.4f}")
```

## Key Parameters

- `reg`: Regularization strength for optimal transport (default: 0.1)
- `n_modes`: Number of Laplace-Beltrami eigenmodes to use (default: 50)
- `max_iter`: Maximum iterations for Sinkhorn algorithm (default: 100)
- `method`: OT solver method ('sinkhorn' or 'exact')

## Advantages Over Traditional Methods

1. **Geometry Awareness**: Explicitly incorporates cortical surface geometry
2. **Computational Efficiency**: Uses embedding to reduce dimensionality
3. **Theoretical Grounding**: Based on optimal transport theory
4. **Flexibility**: Can work with various surface representations
5. **Preserves Functionality**: Geometric regularization prevents over-alignment

## Validation Results

According to the paper, SpectralOT demonstrates:
- Improved cross-subject decoding performance compared to Procrustes, CCA, and other alignment methods
- Better preservation of functional specificity while reducing inter-subject variability
- Computational efficiency suitable for whole-brain analysis
- Robustness across different fMRI paradigms and acquisition protocols

## Installation Requirements

```bash
pip install numpy scipy scikit-learn ot POT
# Optional for surface processing:
pip install nibabel nilearn nibabel-freeform
```

## Usage Example

```python
from spectralot_brain_alignment import align_fmri_spectralot
import nibabel as nib

# Load data for multiple subjects
fmri_files = ['subj1_func.nii.gz', 'subj2_func.nii.gz', 'subj3_func.nii.gz']
surf_files = [('subj1_lh.ply', 'subj1_rh.ply'), 
              ('subj2_lh.ply', 'subj2_rh.ply'),
              ('subj3_lh.ply', 'subj3_rh.ply')]

# Perform alignment
aligned_data = align_fmri_spectralot(
    fmri_files=fmri_files,
    surface_files=surf_files,
    reg=0.1,
    n_modes=50,
    method='sinkhorn'
)

# aligned_data is now a list of numpy arrays ready for group analysis
```

## References

1. Barbarant, P-L., Meyniel, F., & Thirion, B. (2026). Fast Whole-Brain, Geometry-Aware Functional Alignment for Cross-Subject Decoding. arXiv: arXiv:2607.10931v1 [q-bio.NC].

2. Peyré, G., & Cuturi, M. (2019). Computational Optimal Transport. Foundations and Trends® in Machine Learning.

3. Belkin, M., & Niyogi, P. (2003). Laplacian Eigenmaps for Dimensionality Reduction and Data Representation. Neural Computation.

## Related Skills

- `fmri-preprocessing`: Standard fMRI preprocessing pipelines
- `surface-based-analysis`: Tools for cortical surface analysis
- `optimal-transport-neuro`: Applications of optimal transport in neuroscience
- `cross-subject-decoding`: Methods for cross-subject ML in neuroimaging