# Neuromorphic Quantum Kernels (arXiv: 2507.07018)

## Paper Details
- **Title**: Quantum Spectral Clustering: Comparing Parameterized and Neuromorphic Quantum Kernels
- **Published**: 2025-07-09
- **Category**: quant-ph, cs.LG

## Two Quantum Kernel Paradigms

### pQK (Parameterized Quantum Kernel)
- Angle encoding: feature values mapped to rotation angles
- Parametric scaling of rotation angles
- Grid search optimization for kernel-target alignment
- Best for high-dimensional data (50+ features)

### QLIF (Quantum Leaky Integrate-and-Fire) Neuromorphic Kernel
- Population coding: data dimensions to spike trains
- Temporal distance metrics:
  - Victor-Purpura kernel: spike timing edit distance
  - van Rossum kernel: convolution-based spike distance
- Best for low-dimensional data (under 10 features)

## Spectral Clustering Pipeline (Both)
1. Build kernel matrix K
2. Compute graph Laplacian L = D - K
3. Eigen-decomposition to get embedded coordinates
4. K-means clustering in embedded space
5. Elbow-curve analysis for optimal cluster count

## Decision Rule
- Dimension < 10: QLIF with Victor-Purpura kernel
- Dimension > 50: pQK with angle encoding
- Intermediate: test both, pick by kernel-target alignment score
