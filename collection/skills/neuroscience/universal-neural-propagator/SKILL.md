---
name: universal-neural-propagator
description: >
  Universal Neural Propagator (UNP) methodology for learning time evolution in many-body
  quantum systems. A single self-supervised model that maps driving protocols to time-evolution
  propagators, predicting dynamics across a function space of driving protocols and an exponentially
  large Hilbert space of initial states simultaneously. Use when: (1) modeling quantum system
  time evolution under varying Hamiltonians, (2) learning propagator mappings from driving protocols,
  (3) self-supervised training for quantum dynamics prediction, (4) many-body quantum system simulation
  with neural networks, (5) transfer learning across quantum initial states and protocols.
  Activation: universal neural propagator, UNP, quantum dynamics learning, time evolution propagator,
  driving protocol mapping, many-body quantum ML, self-supervised quantum dynamics,
  通用神经传播子.
---

# Universal Neural Propagator (UNP)

A single, unified model that learns the functional mapping from **driving protocols** to
**time-evolution propagators** for many-body quantum systems.

## Key Insight

Traditional approaches require separate models for each Hamiltonian or initial state. UNP learns
a **universal functional mapping** that works across a **function space of driving protocols** AND
an **exponentially large Hilbert space of initial states** simultaneously, trained entirely
self-supervised.

## Core Architecture

### Input Encoding

- **Driving Protocol**: Time-dependent parameters `g(t)` that control the Hamiltonian
- **Initial State**: Quantum state `|ψ₀⟩` encoded in a suitable representation
- **Time**: Evolution duration `t`

```
Input = [encoding(g(t)), encoding(|ψ₀⟩), t]
```

### Propagator Learning

The model learns the mapping:

```
U(t; g) = UNP(g(t), |ψ₀⟩, t)
```

Where `U(t; g)` is the time-evolution propagator such that `|ψ(t)⟩ = U(t; g)|ψ₀⟩`.

### Self-Supervised Training

- **No labeled data required**: Training uses the Schrödinger equation as the supervisory signal
- **Physics-informed loss**: Residual of the time-dependent Schrödinger equation
- **Loss function**: `L = ||iℏ ∂ψ/∂t - H(g(t))ψ||²`

## Advantages Over Traditional Methods

| Approach | Limitation | UNP Advantage |
|----------|-----------|---------------|
| Exact diagonalization | Exponential scaling | Learns compact representation |
| Time-evolving block decimation | Limited entanglement | No entanglement bottleneck |
| Separate models per Hamiltonian | No transfer learning | Single universal model |
| Neural ODE solvers | Per-protocol training | Cross-protocol generalization |

## Key Design Principles

1. **Self-supervised**: No need for ground-truth evolved states
2. **Universal**: Works across protocol families and initial states
3. **Transferable**: Knowledge transfers to unseen protocols and states
4. **Scalable**: Handles exponentially large Hilbert spaces

## Implementation Considerations

- **State representation**: Choose appropriate encoding (wavefunction amplitudes, density matrix, etc.)
- **Protocol parameterization**: How to represent time-dependent driving functions
- **Network architecture**: Must respect unitarity constraints
- **Training stability**: Physics-informed losses can be stiff; use appropriate regularization

## Related Skills

- `neural-dynamics-universal-translator` - Cross-model dynamics alignment
- `quantum-reservoir-computing` - Alternative quantum dynamics approach
- `physics-guided-neural-networks` - PINN methodology
- `pinn-neuronal-parameter-estimation` - PINN for parameter estimation
