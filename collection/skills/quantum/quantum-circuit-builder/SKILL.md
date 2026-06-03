---
name: quantum-circuit-builder
description: Machine learning approaches for building quantum circuits for sets of matrices. Use when designing quantum circuits, implementing quantum matrix operations, variational quantum algorithms, or applying ML to quantum circuit synthesis and optimization.
---

# Quantum Circuit Builder via ML

## Description
ML-driven approach to constructing quantum circuits that implement sets of target matrices. Combines parameterized quantum circuits with classical optimization to synthesize quantum gates and matrix transformations.

## Core Methodology

### 1. Parameterized Quantum Circuit (PQC) Design
- Use rotation gates (RX, RY, RZ) and entangling gates (CNOT, CZ)
- Parameterize all rotation angles as trainable variables
- Structure: layer-wise ansatz with alternating single-qubit rotations and entangling gates

### 2. Loss Function
- Matrix fidelity: L = 1 - |Tr(U_target† * U_circuit)| / N
- Circuit depth penalty: λ * depth(U_circuit)
- Gate count regularization for NISQ efficiency

### 3. Optimization Pipeline
```
1. Define target matrix set {M₁, M₂, ..., Mₙ}
2. Initialize parameterized ansatz
3. Compute unitary U(θ) via statevector simulation
4. Calculate fidelity loss
5. Optimize θ using gradient descent (Adam) or parameter-shift rule
6. Compile optimized circuit to target backend gateset
```

### 4. Circuit Compilation
- Map optimized parameters to hardware-native gates
- Apply transpilation for connectivity constraints
- Validate compiled circuit fidelity against target

## Key Considerations
- Barren plateau mitigation: layer-wise training, careful initialization
- Expressibility vs. trainability tradeoff
- NISQ-aware: limit depth to < 20 for current devices
- Multi-matrix support: shared parameterization across matrix set

## When to Use
- Synthesizing quantum gates for specific unitaries
- Designing circuits for quantum chemistry (Hamiltonian simulation)
- Automated quantum circuit compilation
- Variational quantum eigensolver (VQE) ansatz design
