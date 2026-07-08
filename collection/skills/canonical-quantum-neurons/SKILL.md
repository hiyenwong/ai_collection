---
name: canonical-quantum-neurons
description: Methodology for canonical quantization of classical computational primitives (neurons, activation functions, energy-based models) into quantum ML models. Use when designing quantum neural architectures, constructing quantum Hamiltonians from classical energy functions, or developing hybrid quantum-classical training algorithms. Trigger words: canonical quantization, quantum neurons, quantum activation, quantum Hamiltonian, quantum machine learning primitives.
---

# Canonical Quantization of Computational Primitives

Methodology from arXiv:2607.05000 (July 2026) — applying canonical quantization to construct quantum models from classical computational primitives.

## Core Methodology

1. **Classical → Quantum Mapping**: View a classical primitive as composition of energy function E(x) and activation function σ. Replace E(x) with quantum Hamiltonian H, apply σ via matrix functional calculus: O = σ(H).

2. **Activation Observable**: The resulting operator O is measurable on an input quantum state |ψ⟩. Measurement yields quantum-enhanced computation.

3. **Hybrid Training Algorithms**:
   - Gradient estimation via: classical random sampling, Hadamard test, Hamiltonian simulation
   - Squared loss error estimation with quantum measurement protocols
   - Hybrid quantum-classical optimization loop

4. **Key Quantum Primitives Required**:
   - Hadamard test for observable measurement
   - Hamiltonian simulation for time evolution e^{-iHt}
   - Power of one qumode protocol
   - Schroedingerization technique

## Application Patterns

### Function Approximation
- Objective: learn unknown observable from labeled quantum data
- Training: hybrid gradient descent with quantum measurement
- Advantage: enhanced expressivity over classical counterparts

### Architecture Design
- Start from any classical energy-based model
- Quantize the energy function → quantum Hamiltonian
- Apply classical activation via functional calculus
- Result: quantum activation observable

## Implementation Notes
- Works with any classical activation function (ReLU, sigmoid, etc.)
- Matrix functional calculus requires spectral decomposition of H
- Numerical experiments show enhanced expressive capabilities
- Foundation for developing full quantum neural architectures

## Activation
canonical quantization, quantum neurons, quantum activation function, quantum Hamiltonian, quantum machine learning primitives, function approximation, quantum data, hybrid quantum-classical algorithms
