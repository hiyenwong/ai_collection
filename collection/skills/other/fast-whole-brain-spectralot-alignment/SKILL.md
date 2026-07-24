---
name: fast-whole-brain-spectralot-alignment
description: "Functional alignment method for fMRI using SpectralOT to embed cortical geometry into Laplace-Beltrami eigenmodes for cross-subject decoding"
metadata:
  arxiv_id: "2607.10931"
  authors: ["Pierre-Louis Barbarant", "Florent Meyniel", "Bertrand Thirion"]
  published: "2026-07-12"
  categories: ["q-bio.NC", "cs.LG", "stat.ML"]
  journal_ref: "Proceedings of the 9th Conference on Cognitive Computational Neuroscience, New York, NY, USA, 2026"
  doi: "10.32470/gn6tuko"
license: Complete terms in LICENSE.txt
---

# Fast Whole-Brain, Geometry-Aware Functional Alignment for Cross-Subject Decoding

This skill implements the SpectralOT method for functional alignment of fMRI data across subjects, as described in arXiv:2607.10931.

## Core Concept

The SpectralOT method addresses inter-individual variability in brain response patterns by aligning functional data across individuals before training population-level decoders. It embeds cortical geometry into Laplace-Beltrami eigenmodes along functional data to regularize the alignment, balancing functional feature preservation with anatomical structure maintenance.

## When to Use This Skill

Use this skill when:
- Working with fMRI data from multiple subjects
- Need to align functional data across subjects for population-level analysis
- Want to preserve anatomical structure while aligning functional features
- Seeking computationally efficient functional alignment methods
- Building decoders that need to generalize across individuals

## Methodology Overview

The SpectralOT approach consists of:

1. **Cortical Geometry Embedding**: Compute Laplace-Beltrami eigenmodes from cortical surface data to capture intrinsic geometry
2. **Functional Data Alignment**: Align functional MRI data across subjects using optimal transport in the embedded space
3. **Regularization**: Use the geometric embedding to regularize the alignment, preventing overfitting to noise
4. **Decoder Training**: Train population-level decoders on the aligned data

## Implementation Steps

### Step 1: Data Preparation
- Preprocess fMRI data for each subject (motion correction, spatial normalization, etc.)
- Extract cortical surface meshes for each subject
- Ensure functional data is sampled on the cortical surface

### Step 2: Compute Laplace-Beltrami Eigenmodes
- For each subject's cortical surface, compute the Laplace-Beltrami operator
- Extract the first k eigenmodes (typically k=10-50) as geometric descriptors
- These eigenmodes form a basis for representing cortical geometry

### Step 3: Functional Alignment via SpectralOT
- For each functional feature (voxel/vertex), compute its representation in the eigenmode basis
- Apply optimal transport to align these representations across subjects
- The geometric embedding serves as a regularizer in the optimal transport problem

### Step 4: Validate Alignment
- Check preservation of functional properties (e.g., temporal smoothness)
- Verify anatomical structure maintenance
- Assess improved cross-subject generalization in decoding tasks

## Key Advantages

1. **Geometric Awareness**: Explicitly incorporates cortical geometry into the alignment process
2. **Computational Efficiency**: Leverages the spectral decomposition for efficient computation
3. **Balance**: Strikes optimal balance between functional alignment and anatomical preservation
4. **Generality**: Improved generalization of decoders trained on aligned data

## Validation Metrics

When implementing this method, validate using:
- Procrustes alignment error between aligned and target shapes
- Functional similarity correlation (e.g., voxel-wise correlation of time series)
- Decoding accuracy improvement on held-out subjects
- Geometric distortion measures (local area, angle preservation)

## References

- Barbarant, P.-L., Meyniel, F., & Thirion, B. (2026). Fast Whole-Brain, Geometry-Aware Functional Alignment for Cross-Subject Decoding. arXiv:2607.10931 [q-bio.NC].
- Proceedings of the 9th Conference on Cognitive Computational Neuroscience, New York, NY, USA, 2026.
- DOI: 10.32470/gn6tuko

## Related Skills

- spectral-optimal-transport-alignment: Core optimal transport implementation
- laplace-beltrami-eigenmodes: Spectral geometry processing
- fmri-preprocessing-pipeline: Standard fMRI preprocessing steps