---
name: hcq-alzheimer-classification-vae-quantum-kernels
description: Hybrid Classical-Quantum pipeline for Alzheimer's classification using supervised β-VAE and quantum kernels (arXiv:2606.14194)
category: quantum-medical
---

# Hybrid Classical-Quantum Alzheimer's Classification

Methodology from arXiv:2606.14194 (June 2026). Two-stage HCQ pipeline for binary AD classification from 3D structural MRI volumes.

## Core Pattern

Classical and quantum components designed to **complement** rather than operate independently:
1. **Supervised 3D β-VAE** compresses MRI volumes into latent code using voxel-wise reconstruction + KL-divergence + focal classification losses
2. **PLS regression** selects disease-separating components and rescales into rotation angles
3. **ZZ quantum feature map** encodes onto qubit register
4. **Precomputed-kernel SVM** on quantum Gram matrix for classification

## Key Findings

- **72.1% accuracy, 0.799 AUC** on 308 ADNI-1 subjects (AD vs CN)
- Cross-fold variance **halved** with stability-enhanced variant
- Novelty: quantum kernel operates on **disease-aware features** learned end-to-end by supervised autoencoder
- 3D Grad-CAM validates model focus on Alzheimer's-linked brain regions

## Implementation Steps

1. Resize 3D MRI volumes to standard dimensions (96×96×96)
2. Train supervised 3D β-VAE with reconstruction + KL + focal losses
3. Extract 64-dimensional latent codes
4. Apply PLS to select 6 components best separating classes
5. Encode components as rotation angles via ZZ quantum feature map
6. Compute N×N Gram matrix from quantum state overlaps
7. Train SVM on Gram matrix for classification
8. Validate with 3D Grad-CAM for biological plausibility

## When to Use

- Binary classification from 3D medical imaging
- Scenarios where classical methods struggle with high-dimensional data
- Need for interpretable, biologically-grounded quantum ML
- Diagnostic classification across biomedical imaging domains

## References

- arXiv: 2606.14194v1
- Authors: Tia Tiwari, Vamshi Krishna Kancharla, Neelam Sinha
