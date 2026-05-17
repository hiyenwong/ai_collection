---
name: neural-fields-quantum-sensing
description: Neural field methodology for quantum sensor inverse problems using amortization-free coordinate neural fields coupled to differentiable physics forward models. Use when solving inverse problems for quantum sensors (NV centers, atomic magnetometers), physics-faithful neural inverse problems, or quantum sensing reconstruction. Triggered by: NV center sensing, quantum sensor inverse problem, neural field physics, differentiable quantum model.
---

# Neural Fields for Quantum Sensing

## Description
NeTMY: Amortization-free coordinate neural field coupled to differentiable
quantum sensor forward model for inverse problems in NV-center-based sensing.

## Activation Keywords
- NV center sensing
- quantum sensor inverse problem
- neural field physics
- differentiable quantum model
- diamond quantum sensing
- magnetic noise sensing

## Architecture

### NeTMY Components
1. **Coordinate Neural Field**: Maps spatial coordinates to spin density
2. **Differentiable Forward Model**: Tensor power-summed dipolar operator
3. **Annealed Positional Encoding**: Multi-scale frequency annealing
4. **Sparsity/Gating**: Enforces physical sparsity constraints
5. **Spectrum-Fidelity Loss**: Ensures spectral accuracy

### Forward Model
Replace scalar/coherent approximation with:
```
B(r) = Σ_i (μ_0 / 4π) * [3(r-r_i)(m·(r-r_i)) - m|r-r_i|²] / |r-r_i|⁵
```
Tensor power-summed dipolar operator prevents center-collapse failure.

### Training Pipeline
```python
def train_netmy(coordinates, measured_spectra, forward_model):
    # Initialize neural field
    field = CoordinateNeuralField(encoding='annealed')
    
    # Optimization loop
    for step in range(max_steps):
        # Forward pass
        predicted = forward_model(field(coordinates))
        
        # Multi-scale loss
        loss = (
            spectrum_loss(predicted, measured_spectra) +
            sparsity_loss(field.weights) +
            gating_loss(field.gates)
        )
        
        loss.backward()
        optimizer.step()
```

## Key Features
- **Amortization-free**: Each reconstruction trains from scratch
- **Multiscale optimization**: Coarse-to-fine frequency annealing
- **Center-collapse mitigation**: Parameterization smooths and redistributes updates
- **Physics-faithful**: Forward model respects physical constraints

## Applications
- NV-center magnetic noise sensing
- Atomic magnetometer reconstruction
- Quantum sensor array processing

## Error Handling
- Monitor for center-collapse: check if density concentrates at origin
- Validate forward model accuracy against analytical solutions
- Use sparsity constraints to prevent overfitting

## References
- Paper: arXiv:2605.13988 (Zhao et al., 2026-05-13)
- NV centers: nitrogen-vacancy defects in diamond
