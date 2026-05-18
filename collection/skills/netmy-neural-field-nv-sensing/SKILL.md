---
name: netmy-neural-field-nv-sensing
description: "NeTMY: Coordinate neural field methodology for nitrogen-vacancy (NV) center quantum inverse sensing. Uses physics-faithful neural fields with annealed positional encoding, multiscale optimization, and spectrum-fidelity losses for quantum sensor data reconstruction."
tags: ["quantum", "sensing", "neural-field", "inverse-problem", "NV-center", "physics-informed"]
---

# NeTMY: Neural Fields for NV-Center Inverse Sensing

## Description

NeTMY is a coordinate neural field methodology for inverse problems in nitrogen-vacancy (NV) center quantum sensing. NV centers in diamond measure magnetic-noise spectra from sparse spin sources, and the goal is to reconstruct the spatial and spectral structure of these sources from the measurements.

## Activation Keywords

- NV center sensing
- neural field inverse problem
- quantum sensor reconstruction
- NeTMY
- dipolar operator sensing
- coordinate neural field
- physics-faithful neural inverse

## Key Problem

### Forward Model Fidelity Issue
- Common scalar/coherent forward approximations fail for nonlinear, spectrally coupled systems
- Tensor power-summed dipolar operator changes inverse landscape
- Exposes center-collapse failure mode in free-density optimization

### Center-Collapse Pathology
- Free-density optimization causes solutions to collapse to center
- Mechanism: raw density-space gradient without parameter smoothing
- NeTMY mitigates this through its parameterization

## NeTMY Architecture

### Coordinate Neural Field
- Amortization-free: learns each inverse problem independently
- Coupled to differentiable NV forward model
- No need for large training datasets

### Key Components

1. **Annealed Positional Encoding**
   - Gradually increases frequency content during optimization
   - Prevents high-frequency artifacts
   - Enables coarse-to-fine reconstruction

2. **Multiscale Optimization**
   - Progressive refinement from global to local structure
   - Avoids local minima in complex inverse landscapes

3. **Sparsity/Gating**
   - Encodes physical prior that spin sources are sparse
   - Automatic relevance determination

4. **Spectrum-Fidelity Losses**
   - Ensures reconstructed sources match measured spectra
   - Physics-constrained optimization

## Optimization Geometry

### Key Insight
NeTMY does NOT directly execute raw density-space gradient updates. Its parameterization:
- Smooths updates across spatial coordinates
- Redistributes gradient information
- Mitigates center-collapse pathology

### Forward Operator Correction
- Replace scalar/coherent approximation with tensor power-summed dipolar operator
- This correction is essential for faithful reconstruction
- Without correction, optimization geometry leads to systematic errors

## Applications

1. **NV Center Noise Sensing**: Reconstruct spin source distributions
2. **Quantum Metrology**: Enhanced magnetic field imaging
3. **Materials Characterization**: Alpha-RuCl3 cross-validation demonstrated
4. **General Scientific ML**: Physics-faithful neural inverse problems

## Error Handling

### Center-Collapse
- Use NeTMY parameterization instead of free-density optimization
- Include sparsity regularization

### Forward Model Mismatch
- Use tensor power-summed dipolar operator
- Validate forward model against physical measurements

### Overfitting
- Use multiscale curriculum learning
- Apply annealed positional encoding schedule

## References

- arXiv:2605.13988 - "Neural Fields for NV-Center Inverse Sensing" (May 2026)
