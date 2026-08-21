---
name: pca-dmd-neural-dynamics-reconstruction
description: "PCA-DMD for neural dynamics reconstruction."
metadata:
  arxiv_id: "2608.16569v1"
  published: "2026-08-17"
  authors: "Anima Kujur, Zahra Monfared"
  tags: [neural-dynamics, pca-dmd, koopman-operator, dmd, lfp-reconstruction, cross-subject-generalization]
license: Complete terms in LICENSE.txt
---

# PCA-DMD Neural Dynamics Reconstruction

## Overview

PCA-DMD is a scalable operator-theoretic framework for reconstructing high-dimensional neural dynamics from local field potential (LFP) recordings. The method segments LFP recordings into overlapping windows, projects them into a compact PCA space, learns linear Koopman evolution in the latent space, and reconstructs continuous signals through inverse projection and overlap-add aggregation.

Key advantages:
- **Zero-shot cross-subject generalization**: Achieves correlations of 0.9504-0.9800 across subjects without target-subject fine-tuning
- **Scalability**: Stable performance from 400,000 to 900,000 samples with predictable computational cost increase
- **Interpretability**: Koopman spectral and mode analyses reveal dominant eigenvalues concentrated near the unit circle
- **External validation**: Successfully validated on independent Allen Neuropixels recordings (mean correlation: 0.7427)

## Methodology

### Core Algorithm Steps

1. **Window Segmentation**: Divide LFP recordings into overlapping temporal windows
2. **PCA Projection**: Project each window into a compact principal component space
3. **Koopman Learning**: Learn linear evolution operator in the latent PCA space using Dynamic Mode Decomposition
4. **Signal Reconstruction**: Reconstruct continuous signals via inverse PCA projection and overlap-add aggregation

### Implementation Guidelines

For implementing PCA-DMD:

```python
# Pseudocode for PCA-DMD implementation
import numpy as np
from sklearn.decomposition import PCA
from pydmd import DMD

def pca_dmd_reconstruction(lfp_data, window_size=1000, overlap=500, n_components=50):
    """
    Reconstruct LFP data using PCA-DMD framework
    
    Args:
        lfp_data: [n_channels, n_samples] LFP recording
        window_size: Size of temporal windows
        overlap: Overlap between consecutive windows  
        n_components: Number of PCA components to retain
    
    Returns:
        reconstructed_signal: Reconstructed LFP signal
    """
    # Step 1: Segment into overlapping windows
    windows = segment_overlapping_windows(lfp_data, window_size, overlap)
    
    # Step 2: Apply PCA projection
    pca = PCA(n_components=n_components)
    projected_windows = [pca.fit_transform(window.T).T for window in windows]
    
    # Step 3: Learn Koopman operator with DMD
    reconstructed_windows = []
    for proj_window in projected_windows:
        dmd = DMD(svd_rank=n_components)
        dmd.fit(proj_window)
        reconstructed_proj = dmd.reconstructed_data
        reconstructed_windows.append(reconstructed_proj)
    
    # Step 4: Inverse projection and overlap-add
    final_reconstruction = overlap_add_inverse_pca(
        reconstructed_windows, pca, window_size, overlap
    )
    
    return final_reconstruction
```

## Performance Metrics

The original paper reports the following performance metrics:

- **Within-subject reconstruction**: KLD=0.0761, HD=0.0847 on 200,000-sample hippocampal recordings
- **Cross-subject zero-shot**: Correlations 0.9504-0.9800, HD=0.0010-0.0072, KLD=0.0005-0.0022
- **Out-of-sample prediction**: Close one-step agreement on temporally held-out LFP segments
- **Scalability**: Mean correlation remains ~0.965-0.968 from 400k to 900k samples
- **External validation**: Mean correlation 0.7427, median 0.7990 on Allen Neuropixels data

## Use Cases

### When to Use PCA-DMD

- **Neural signal reconstruction**: Reconstructing missing or corrupted LFP/EEG segments
- **Cross-subject transfer**: Applying models trained on one subject to another without fine-tuning  
- **Long-duration analysis**: Processing extended neural recordings (100k+ samples)
- **Interpretable dynamics**: Analyzing Koopman eigenvalues and modes for neural dynamics insights
- **Real-time applications**: Scalable framework suitable for online processing

### Comparison with Alternatives

PCA-DMD outperforms several DMD variants:
- Classical DMD
- SpDMD (Sparse DMD)
- MrDMD (Multi-resolution DMD) 
- HODMD (Higher-order DMD)

The key differentiator is the combination of PCA dimensionality reduction with DMD learning, which enables both scalability and generalizability.

## Pitfalls and Considerations

### Parameter Selection

- **PCA components**: Balance between reconstruction fidelity and computational efficiency
- **Window size**: Should capture relevant neural dynamics timescales
- **Overlap ratio**: Higher overlap provides smoother reconstruction but increases computation

### Limitations

- Assumes approximately linear dynamics in the PCA-projected space
- Performance may degrade for highly nonlinear neural phenomena
- Requires sufficient data for stable PCA estimation

## References

- Original paper: [Learning Generalizable Reconstruction of High-Dimensional Neural Dynamics](https://arxiv.org/abs/2608.16569v1)
- Koopman operator theory: Budisic et al., "Applied Koopmanism" (2012)
- Dynamic Mode Decomposition: Tu et al., "On Dynamic Mode Decomposition" (2014)
- PyDMD library: https://github.com/mathLab/PyDMD

## Activation Keywords

- pca-dmd
- neural dynamics reconstruction
- koopman operator neuroscience
- cross-subject neural generalization
- lfp signal reconstruction
- high-dimensional neural dynamics
- dmd neuroscience