---
name: fourier-lcu-quantum-optimization
description: "Fourier-based Linear Combination of Unitaries (LCU) methodology for efficient quantum circuit decomposition in optimization algorithms. Covers ancilla-free LCU constructions, Fourier decomposition of diagonal/non-diagonal unitaries, formal connection to Lagrangian relaxation, and hardware-friendly gate layer simplification. Activation: LCU, linear combination of unitaries, Fourier quantum, quantum optimization decomposition, constraint penalty, XY-mixer, cardinality constraint, ancilla-free quantum, sampling overhead, circuit complexity tradeoff"
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.18985"
  published: "2026-05-18"
  authors: "Almudena Carrera Vazquez, Daniel J. Egger, Stefan Woerner"
  tags: ["LCU", "Fourier", "quantum-optimization", "QAOA", "constraint-handling", "ancilla-free", "Lagrangian-relaxation"]
---

# Fourier-Based LCU for Quantum Optimization

Efficient circuit decomposition via Fourier-based Linear Combination of Unitaries (LCU) for quantum optimization algorithms.

## Context

Quantum optimization algorithms (QAOA, VQE) require complex multi-qubit interactions that are expensive to implement. LCU provides a framework for approximating these circuits by decomposing unitaries into simpler components with polynomial sampling overhead.

## Core Methodology

### 1. Fourier-Based LCU Decomposition

Decompose complex unitaries U = exp(-iH) via Fourier series:

```
U ≈ Σ_k c_k · V_k
```

where V_k are simple single-qubit or low-connectivity gate layers, and c_k are Fourier coefficients.

### 2. Ancilla-Free Sampling Pattern

Key insight: when the goal is sampling high-quality bitstrings (not reproducing full output distribution), ancilla qubits can be eliminated:

- Classically evaluate candidate solutions
- Sample from the decomposed distribution
- Trade circuit complexity for polynomial sampling overhead
- No ancilla qubits needed → more available qubits for problem encoding

### 3. Constraint Handling via Fourier Penalties

Fourier-based penalty constructions handle constraints efficiently:

- **Cardinality constraints**: Decompose into single-qubit gate layers
- **Fully connected XY-mixer**: Replace multi-qubit interactions with simpler structures
- **Formal connection**: Fourier penalties ≡ Lagrangian relaxation (unified view of quantum and classical constraint handling)

### 4. Hardware-Friendly Implementation

Replace highly connected qubit interactions with:
- Single-qubit gate layers (O(n) gates)
- Significantly simpler structures (O(n log n) vs O(n²))
- Maintained performance guarantees vs fully coherent implementations

## Implementation Steps

1. **Identify complex unitary**: Find highly connected terms in Hamiltonian (e.g., fully connected penalties, XY-mixers)
2. **Compute Fourier decomposition**: Express as sum of simpler unitaries with known coefficients
3. **Implement sampling circuit**: Build ancilla-free circuit that samples from decomposed distribution
4. **Classical evaluation loop**: Evaluate sampled bitstrings classically, keep high-quality solutions
5. **Budget tradeoff**: Balance circuit depth reduction against sampling overhead multiplier

## Pitfalls

- **Sampling overhead grows polynomially**: For very high precision requirements, fully coherent implementation may still be better
- **Not for state preparation**: This pattern works for optimization (sampling) but NOT for algorithms requiring exact state preparation
- **Fourier series convergence**: Number of terms depends on function smoothness — discontinuous penalties need more terms
- **Classical evaluation bottleneck**: Requires efficient classical evaluation of objective function

## Verification

- Compare solution quality: Fourier-LCU vs fully coherent on same problem
- Validate constraint satisfaction: Check that penalties enforce constraints correctly
- Measure resource savings: Gate count reduction vs sampling overhead ratio
