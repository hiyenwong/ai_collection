---
name: hybrid-quantum-fbpinn
description: "Hybrid quantum-classical domain-decomposed Physics-Informed Neural Network (FBPINN) architecture for full waveform inversion and complex field reconstruction. Use when accelerating PINNs with quantum circuits for scientific computing, geophysics, and PDE-solving tasks."
metadata:
  arxiv_id: "2606.01110"
  published: "2026-05-31"
  authors: []
  tags: [quantum-machine-learning, physics-informed-neural-networks, full-waveform-inversion, hybrid-quantum-classical, FBPINN, domain-decomposition]
---

# Hybrid Quantum FBPINN

## Core Framework

This paper presents a hybrid quantum-classical Finite-Basis Physics-Informed Neural Network (FBPINN) architecture that combines domain decomposition with quantum circuits to solve complex physics problems. The key insight is that quantum circuits can serve as enhanced subdomain representors within the FBPINN framework, capturing complex spatial patterns that classical networks struggle with.

### Architecture

1. **Domain Decomposition**: Physical space divided into overlapping subdomains, each handled by a local network
2. **Hybrid Subdomain Networks**: Each subdomain network uses classical layers + quantum variational circuits
3. **Quantum Feature Encoding**: Input coordinates encoded into quantum states via amplitude or angle encoding
4. **Variational Quantum Layers**: Parameterized quantum circuits with entangling layers for non-linear representation
5. **Classical Output Layer**: Measurement results fed through classical linear/nonlinear layers for final output

### Key Advantages

- **Quantum expressivity**: Quantum circuits provide exponentially large Hilbert space for representing complex field patterns
- **Domain decomposition scalability**: FBPINN structure allows parallel training across subdomains
- **Physics constraints**: PDE residuals enforced at collocation points across all subdomains
- **Hybrid efficiency**: Only critical subdomains use quantum circuits, rest remain classical

### Application to Full Waveform Inversion (FWI)

FWI reconstructs subsurface velocity models from seismic data. The hybrid quantum FBPINN approach:
- Decomposes the geological domain into subdomains
- Each subdomain uses quantum circuits to capture complex velocity variations
- Physics constraints (wave equation residuals) enforced at collocation points
- Classical networks handle smoother regions, quantum handles complex geological features

## Implementation Patterns

### Pattern 1: Hybrid Quantum-Classical FBPINN for Scientific Computing

```
Physical Domain → Decompose into subdomains → 
For each subdomain:
  Classical layers → Quantum encoding → Variational QC → Classical output
Enforce PDE residuals at collocation points → Loss = PDE + BC + IC
```

### Pattern 2: Quantum Subdomain for Complex Features

```
Complex region detected → Allocate quantum circuit to subdomain
  Angle encoding: x → RY(π·x) ⊗ RZ(π·x)
  Variational: CNOT layers + RY/RZ rotation parameters
  Measurement: ⟨Z⟩ expectation values
  Classical post-processing → Subdomain output
Smooth region → Classical subdomain only
```

## Activation

- hybrid quantum PINN, quantum FBPINN, domain decomposition quantum
- full waveform inversion quantum, 量子物理信息神经网络
- quantum-classical PDE solver, hybrid quantum scientific computing
- 量子波动方程反演, quantum geophysics

## Pitfalls

- **Qubit limitations**: Current NISQ devices limit quantum circuit depth and qubit count; use classical simulation for research
- **Barren plateaus**: Quantum circuits in PINN context may suffer from vanishing gradients; use layer-wise training or parameter initialization strategies
- **Domain boundary handling**: Overlapping subdomains require careful weight functions to ensure smooth transitions
- **Quantum noise**: On real hardware, noise affects gradient estimation; use error mitigation techniques
- **Computational overhead**: Quantum circuit evaluation is slower than classical forward passes; only apply to complex subdomains where expressivity gain justifies cost

## References

- arXiv: 2606.01110 - "Accelerating physics-informed neural networks for full waveform inversion using a hybrid quantum-classical finite-basis architecture"
- Related: hybrid-quantum-pinn-nonlinear-pde (broader quantum PINN methodology)
