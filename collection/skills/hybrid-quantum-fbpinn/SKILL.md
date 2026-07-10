---
name: hybrid-quantum-fbpinn
description: "Hybrid quantum-classical FBPINN methodology for wave-based inverse problems. Uses parameterized quantum circuits (PQCs) as differentiable JAX statevector simulators in domain-decomposed physics-informed neural networks. Achieves 8x faster convergence with 33% fewer parameters. Activation: hybrid quantum-classical neural networks, physics-informed neural networks, full waveform inversion, quantum machine learning for PDEs, differentiable quantum circuits, JAX quantum simulation, wave-based inverse problems, domain-decomposed PINNs, FBPINN quantum"
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2606.01110"
  published: "2026-05-31"
  authors: "Hoang Anh Nguyen, Divakar Vashisth, Ali Tura"
  tags: ["quantum computing", "machine learning", "physics-informed neural networks", "full waveform inversion", "hybrid quantum-classical", "JAX", "inverse problems"]
---

# Hybrid Quantum-Classical FBPINN for Wave-Based Inverse Problems

## Overview

Methodology from arXiv:2606.01110 (May 2026). Hybrid quantum-classical finite-basis physics-informed neural network (FBPINN) for acoustic full waveform inversion (FWI). Combines quantum computing with domain-decomposed PINNs using parameterized quantum circuits (PQCs) as differentiable components.

**Key result**: Quantum hybrid reaches lower L1 velocity error than classical FBPINN baseline in ~8x fewer training iterations with ~33% fewer trainable parameters. Outperforms all 15 classical hyperparameter variants tested.

## Architecture Pattern

```
┌──────────────────────────────────────────────────────────────┐
│                    Hybrid Quantum-Classical FBPINN            │
├─────────────────────┬────────────────────────────────────────┤
│   Classical PINN    │          Quantum Layer                 │
│   (FBP decomposition│   ┌─────────────────────┐              │
│    + velocity net)  │   │  PQC (statevector)   │              │
│                     │   │  - Differentiable    │              │
│  Input → Features ──┼──►│  - JAX simulator     │              │
│                     │   │  - End-to-end AD     │              │
│                     │   └─────────┬───────────┘              │
│                     │             ▼                          │
│                     │     Physics-informed loss              │
└─────────────────────┴────────────────────────────────────────┘
```

### Core Design Principles

1. **Classical-to-Quantum Pipeline**: Decomposed wavefield network (classical FBPINN) + global velocity network (classical) → features → PQC → output
2. **Differentiable JAX Statevector**: PQCs implemented as JAX statevector simulators, enabling end-to-end automatic differentiation through classical PINN → quantum circuit → physics loss
3. **Domain Decomposition**: FBPINN's subdomain approach reduces problem complexity; quantum layer operates on compressed feature representations
4. **Physics-Informed Loss**: PDE residuals computed with automatic differentiation through quantum layer

## Implementation Pipeline

### Step 1: Classical FBPINN Setup
```python
import jax
import jax.numpy as jnp

# Domain-decomposed FBPINN
class ClassicalFBPINN:
    def __init__(self, subdomains, basis_functions):
        self.subdomains = subdomains
        self.basis_functions = basis_functions
    
    def forward(self, x):
        # Decomposed wavefield approximation
        # Global velocity field approximation
        pass
    
    def physics_loss(self, params, x):
        # Wave equation PDE residual via autodiff
        u = self.forward(x)
        # Compute ∇²u - (1/c²)∂²u/∂t² = 0
        pass
```

### Step 2: Quantum Layer Integration
```python
# PQC as differentiable JAX layer
class DifferentiablePQC:
    def __init__(self, n_qubits, n_layers):
        self.n_qubits = n_qubits
        self.n_layers = n_layers
    
    @jax.jit
    def forward(self, features, params):
        # Statevector simulation with parameterized gates
        # Rotation gates encode features
        # Entangling layers create correlations
        # Measurement yields output
        pass
    
    # Automatic differentiation through quantum circuit
    # Gradients flow: loss → PQC params → classical PINN params
```

### Step 3: End-to-End Training
```python
def hybrid_loss(classical_params, quantum_params, data):
    # Forward pass: classical → quantum
    features = classical_fbpinn(classical_params, data)
    output = pqc(quantum_params, features)
    
    # Physics-informed loss
    physics_residual = compute_pde_residual(output, data)
    
    # Data fidelity loss
    data_loss = jnp.mean((output - data.targets) ** 2)
    
    return physics_residual + data_loss

# Joint optimization
grad_fn = jax.grad(hybrid_loss, argnums=(0, 1))
```

## Key Results

| Metric | Classical FBPINN | Hybrid Quantum-Classical | Improvement |
|--------|------------------|-------------------------|-------------|
| Training iterations | ~8000 | ~1000 | 8x fewer |
| Trainable parameters | ~100% | ~67% | 33% fewer |
| L1 velocity error | Baseline | Lower | Better accuracy |
| Hyperparameter variants | 15 tested | Single config | Outperforms all 15 |

## Applicability

This methodology extends beyond geophysics to:
- **Medical ultrasound tomography**
- **Non-destructive evaluation**
- **Any wave-based inverse problem** (seismic, acoustic, electromagnetic)
- **PDE-constrained optimization** with quantum-enhanced feature representations

## Reusable Patterns

1. **Differentiable Quantum Simulator**: JAX statevector simulation enables seamless autodiff through quantum circuits
2. **Classical-Quantum Feature Pipeline**: Classical network extracts features → PQC processes compressed representation
3. **Domain Decomposition + Quantum**: FBPINN's subdomain approach reduces dimensionality before quantum processing
4. **Physics-Informed Quantum Loss**: PDE residuals computed with gradients flowing through quantum layer

## Pitfalls

1. **Simulation vs Hardware**: Paper uses statevector simulation; NISQ hardware will introduce noise requiring error mitigation
2. **Scalability**: Statevector simulation is limited to ~30 qubits; practical deployment requires quantum hardware or tensor network approximations
3. **JAX Integration**: Custom JAX primitives needed for quantum gate operations to maintain autodiff compatibility
4. **Convergence**: Quantum layer may introduce optimization landscape changes; monitor training dynamics carefully

## Activation

Hybrid quantum-classical neural networks, physics-informed neural networks, full waveform inversion, quantum machine learning for PDEs, differentiable quantum circuits, JAX quantum simulation, wave-based inverse problems, domain-decomposed PINNs

## Related Skills

- [[physics-guided-neural-networks]] - PINN design patterns
- [[pinn-quantum-pulse-optimization]] - PINNs for quantum control
- [[quantum-neural-hybrid]] - Hybrid classical-quantum neural network development
- [[hybrid-quantum-classical-nn]] - General hybrid quantum-classical neural network design
- [[qadr-distributed-entanglement-reduction]] - Distributed QML framework (arXiv:2606.01291)

## References

- **arXiv**: [2606.01110](https://arxiv.org/abs/2606.01110) (2026-05-31)
- Authors: Hoang Anh Nguyen, Divakar Vashisth, Ali Tura
- Subjects: Geophysics (physics.geo-ph); Machine Learning (cs.LG); Quantum Physics (quant-ph)
