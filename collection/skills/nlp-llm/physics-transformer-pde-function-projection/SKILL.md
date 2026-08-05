---
name: physics-transformer-pde-function-projection
version: 1.0.0
description: Physics Transformer methodology for PDE prediction using function-projection-based tokenization. Treats physical fields as continuous functions with adaptive local basis functions and locality-preserving spatial patches.
trigger_words:
  - physics transformer
  - PDE function projection
  - physical field tokenization
  - adaptive basis functions
---

# Physics Transformer: Function-Projection-Based Architecture for PDE Prediction

## Overview
Transformer architectures for solving partial differential equations (PDEs) require special consideration since physical fields are finite samples of underlying infinite-dimensional functions. Physics Transformer addresses this by treating physical fields as continuous functions and using function-projection-based tokenization to create physically expressive tokens from arbitrary discretizations.

## Core Methodology

### 1. Locality-Preserving Spatial Patches
- Partition discretized physical field into spatial patches that preserve locality
- Maintain fine-scale spatial structures within each patch
- Enable efficient global interaction across patches

### 2. Adaptive Local Basis Functions
- Dynamically learn set of basis functions within each spatial patch
- Project sampled field onto these adaptive bases to obtain compact tokens
- Capture diverse latent physical states while preserving spatial information

### 3. Factorized Attention Mechanism
- Separate attention across space and physical states dimensions
- Enable efficient global interaction through factorized computation
- Support arbitrary query location decoding from projected representation

## Implementation Guidelines

### Step 1: Spatial Patching
```python
# Given discretized field u(x_i) at points x_i
patches = partition_spatial_domain(x_points, patch_size)
patched_fields = [u[patch_indices] for patch_indices in patches]
```

### Step 2: Adaptive Basis Learning
```python
# For each patch, learn basis functions φ_j(x)
for patch_field in patched_fields:
    basis_functions = learn_adaptive_basis(patch_field, num_bases=K)
    tokens = project_onto_basis(patch_field, basis_functions)
```

### Step 3: Physics Token Construction
- Each token represents projection coefficients onto local basis
- Tokens capture latent physical states compactly
- Preserve both global structure and fine-scale details

### Step 4: Factorized Attention
- Apply attention separately across spatial patches and basis dimensions
- Reduce computational complexity from O(N²) to O(N_patch² + N_basis²)
- Enable scaling to large discretizations

## Benefits
- Accurately captures fine-grained physical structures
- Achieves state-of-the-art predictive performance on diverse PDEs
- Handles irregular discretizations naturally
- Supports efficient decoding at arbitrary query locations
- Scales to industrial-scale 3D CFD simulations

## Applications
- Two-dimensional PDE dynamics prediction
- Three-dimensional computational fluid dynamics (CFD)
- General physical field prediction tasks
- Irregular mesh PDE solving
- Multi-scale physical simulation

## Evaluation Benchmarks
- Diverse 2D PDE dynamics datasets
- Industrial-scale 3D CFD simulations
- Fine-grained structure preservation metrics
- State-of-the-art comparison baselines

## References
- arXiv:2607.24513 [cs.LG]
- Authors: Guoze Sun, Rui Zhang, Jiankai Tang, Mengtao Yan, Runze Mao, Zhi X. Chen, Hao Sun