# HCQ Pipeline: Supervised β-VAE + Quantum Kernel SVM

**arXiv**: 2606.14194 (2026-06-12)
**Authors**: Tia Tiwari, Vamshi Krishna Kancharla, Neelam Sinha
**Categories**: cs.CV, cs.LG

## Pipeline Overview

Two-stage hybrid classical-quantum medical image classification:

### Stage 1: Supervised 3D β-VAE Feature Extraction
- Input: 3D T1-weighted MRI volumes (152×184×152 → resized to 96×96×96)
- Output: 64-dimensional latent code
- Training losses (end-to-end):
  1. Voxel-wise reconstruction loss — anatomical fidelity
  2. KL-divergence loss — latent space regularization
  3. Focal classification loss — disease-discriminative features

### Stage 2: Quantum Classification
- PLS regression: selects 6 most discriminative components from 64-dim latent code
- Feature rescaling: map PLS components to rotation angles
- ZZ quantum feature map: encode onto 6-qubit register → quantum states
- Gram matrix: N×N pairwise state overlaps
- Precomputed-kernel SVM: classifies AD vs CN

## Key Results
- Dataset: 308 ADNI-1 subjects (137 AD, 171 CN)
- Baseline: 67.2% accuracy, 0.759 AUC
- Stability-enhanced: 72.1% accuracy, 0.799 AUC
- Cross-fold variance halved with stability protocol
- 3D Grad-CAM validates brain region focus (Alzheimer's-linked regions)

## Design Principles
1. Disease-aware features (not generic compression)
2. PLS for quantum dimension matching
3. Precomputed kernel — avoids repeated quantum evaluations during training
4. Generalizable to any biomedical imaging (MRI, CT, PET, ultrasound)

## Implementation Notes
- Qubit limitation: n_components must match available qubits (≤10 for NISQ)
- VAE three-loss training can be unstable — use gradual loss weighting
- Gram matrix is O(N²) — for large datasets, use Nyström approximation
- Quantum kernels excel on small-medium datasets (hundreds of samples)
