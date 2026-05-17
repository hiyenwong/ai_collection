---
name: neural-fields-nv-sensing
description: >
  Neural field methodology for quantum sensor inverse problems, specifically
  nitrogen-vacancy (NV) center noise sensing in diamond. Based on NeTMY framework
  from arXiv:2605.13988v1 (Zhao et al., 2026-05-13). Use when: NV-center quantum
  sensing, neural inverse problems, physics-faithful neural fields, magnetic noise
  sensing, spin source localization, differentiable forward models, coordinate-based
  neural fields, quantum sensor inverse problems.
---

# Neural Fields for NV-Center Inverse Sensing

NeTMY framework: amortization-free coordinate neural field coupled to differentiable NV forward model for quantum sensor inverse problems. Based on arXiv:2605.13988v1.

## Problem

NV centers in diamond measure magnetic-noise spectra from sparse spin sources. The inverse problem is challenging because:
- Forward model is nonlinear and spectrally coupled
- Scalar/coherent approximations cause center-collapse failure in free-density optimization
- Need physics-faithful reconstruction without training amortization

## NeTMY Architecture

### Core Components

1. **Coordinate Neural Field**: Maps spatial coordinates to source density
   - Input: 3D position (x, y, z)
   - Output: spin density at that location

2. **Differentiable NV Forward Model**: Tensor power-summed dipolar operator
   - Replaces scalar/coherent approximation
   - Computes expected measurement given source configuration

3. **Annealed Positional Encoding**: Multi-scale frequency annealing for stable optimization

### Loss Functions

```
L = L_spectrum + λ₁·L_sparsity + λ₂·L_gating
```

- **Spectrum-fidelity loss**: Match predicted vs measured noise spectra
- **Sparsity loss**: Encourage sparse spin source distribution
- **Gating loss**: Prevent degenerate solutions

## Key Innovations

1. **Tensor Power-Summed Dipolar Operator**: Corrects forward model approximation errors
2. **Center-Collapse Mitigation**: Parameterization smooths and redistributes optimization updates
3. **Amortization-Free**: No need for pre-training on simulated data
4. **Physics-Faithful**: Neural network respects physical constraints of NV sensing

## Implementation Pattern

```python
# Pseudocode for NeTMY workflow

# 1. Build differentiable NV forward model
def nv_forward_model(source_density, positions):
    """Compute predicted noise spectra from spin source distribution."""
    # Tensor power-summed dipolar operator
    # Replaces scalar/coherent approximation
    return compute_dipolar_coupling(source_density, positions)

# 2. Coordinate neural field
def neural_field(coords, params):
    """Map 3D coordinates to spin density."""
    # Annealed positional encoding
    encoded = annealed_encoding(coords)
    # MLP with sparsity gating
    return mlp(encoded, params)

# 3. Optimization loop
def optimize(measured_spectra, n_steps=10000):
    """Optimize neural field parameters to match measurements."""
    for step in range(n_steps):
        density = neural_field(query_points, params)
        predicted = nv_forward_model(density, nv_positions)
        
        loss = spectrum_loss(predicted, measured_spectra)
        loss += sparsity_penalty(density)
        loss += gating_penalty(params)
        
        params = gradient_step(params, loss)
```

## Applications

- Quantum sensing with NV centers in diamond
- Spin source localization at nanoscale
- Magnetic noise spectroscopy
- Physics-informed neural inverse problems
- Beyond NV: any quantum sensor with known forward model

## Reference

Zhixuan Zhao et al., "Neural Fields for NV-Center Inverse Sensing", arXiv:2605.13988v1, 2026-05-13.
