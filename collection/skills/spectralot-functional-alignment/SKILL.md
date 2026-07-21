---
name: spectralot-functional-alignment
description: "Method for geometry-aware functional alignment of fMRI data using SpectralOT to improve cross-subject decoding by embedding cortical geometry into Laplace-Beltrami eigenmodes."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2607.10931"
  authors: ["Pierre-Louis Barbarant", "Florent Meyniel", "Bertrand Thirion"]
  submitted: "2026-07-12"
  comment: "Proceedings of the 9th Conference on Cognitive Computational Neuroscience, New York, NY, USA, 2026"
---

# SpectralOT Functional Alignment

## When to Use This Skill

Use this skill when you need to:
- Perform functional alignment of fMRI data across subjects for improved cross-subject decoding
- Incorporate cortical geometry into functional alignment procedures
- Work with surface-based fMRI data (cortical surfaces) and functional maps
- Implement geometry-aware regularization in neuroimaging analysis pipelines

## Overview

SpectralOT introduces a novel functional alignment method for fMRI data that embeds cortical geometry into Laplace-Beltrami eigenmodes to regularize the alignment process. This approach balances functional feature alignment with anatomical structure preservation while maintaining computational efficiency. The method improves cross-subject decoding performance by leveraging the spectral decomposition of the Laplace-Beltrami operator on the cortical surface.

## Methodology

### Core Concept

The method addresses the challenge of inter-individual variability in brain response patterns by aligning functional data across individuals before training population-level decoders. Unlike traditional approaches that may distort anatomical structure, SpectralOT incorporates geometric constraints directly into the alignment framework.

### Mathematical Formulation

1. **Laplace-Beltrami Eigenmodes**: Compute eigenmodes of the Laplace-Beltrami operator on each subject's cortical surface mesh, capturing intrinsic geometric properties.

2. **Spectral Embedding**: Project functional data (e.g., fMRI activation maps) onto the Laplace-Beltrami eigenbasis to obtain spectral coefficients that represent functional patterns in a geometry-aware basis.

3. **Optimal Transport Alignment**: Solve an optimal transport problem in the spectral domain to find the mapping that minimizes discrepancies between subjects' functional representations while respecting geometric constraints.

4. **Geometric Regularization**: The use of Laplace-Beltrami eigenmodes inherently regularizes the alignment to preserve cortical topology, preventing excessive warping that could distort anatomical correspondence.

### Workflow

1. **Preprocessing**: 
   - Extract cortical surface meshes from structural MRI for each subject
   - Preprocess fMRI data to obtain functional maps on the cortical surface

2. **Spectral Decomposition**:
   - Compute Laplace-Beltrami eigenmodes for each surface mesh
   - Project functional maps onto the eigenbasis to obtain spectral coefficients

3. **Alignment Optimization**:
   - Formulate optimal transport problem between spectral coefficients of source and target subjects
   - Solve for optimal coupling matrix using Sinkhorn algorithm or similar
   - Apply the learned transformation to align functional data

4. **Validation**:
   - Evaluate alignment quality using cross-subject decoding accuracy
   - Assess preservation of anatomical landmarks and functional boundaries

## Implementation Notes

- Requires surface reconstruction tools (e.g., FreeSurfer) to obtain cortical meshes
- Functional data should be sampled on the cortical surface (e.g., via surface-based smoothing)
- Choice of truncation level for Laplace-Beltrami eigenbasis affects trade-off between geometric detail and computational cost
- The method is compatible with various functional modalities (fMRI, EEG source localization, etc.) when mapped to cortical surface

## Expected Outcomes

When applied correctly, this skill should enable:
- Improved cross-subject decoding accuracy compared to alignment-free or geometry-unaware methods
- Better preservation of topographically organized functional areas
- Reduced inter-subject variability in functional responses post-alignment
- Computationally efficient alignment suitable for large datasets

## References

- Barbarant, P.-L., Meyniel, F., & Thirion, B. (2026). Fast Whole-Brain, Geometry-Aware Functional Alignment for Cross-Subject Decoding. arXiv:2607.10931.
- Proceedings of the 9th Conference on Cognitive Computational Neuroscience, New York, NY, USA, 2026.

## Activation Keywords

- spectralot
- functional alignment
- laplace beltrami
- cortical geometry
- fmri alignment
- cross-subject decoding
- geometry-aware