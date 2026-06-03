---
name: logq-quantum-inspired-optimization
description: "LogQ algorithm reformulated as classical non-linear continuous relaxation for QUBO problems. Use when: solving portfolio optimization, fleet optimization, charging station placement, or any QUBO combinatorial problem; implementing quantum-inspired classical algorithms; reducing qubit requirements from quantum formulations; eliminating Pauli decomposition overhead; applying gradient-inspired methods to discrete optimization. Keywords: quantum-inspired, logq, qubo, portfolio optimization, continuous relaxation, binary optimization"
---

# LogQ Quantum-Inspired Optimization

## Core Concept

The LogQ algorithm was originally developed for quantum combinatorial optimization, drastically reducing qubit count and circuit depth. It has been reformulated as a **classical heuristic** using non-linear continuous relaxation of binary variables, eliminating the need for Pauli decomposition and quantum measurement overhead.

## When to Use

- QUBO problems in finance (portfolio optimization), logistics (fleet optimization), or infrastructure (charging stations)
- When quantum circuit depth or qubit count is prohibitive
- When gradient-inspired parameter optimization is beneficial
- As a classical baseline before deploying quantum hardware

## Algorithm Steps

1. **Formulate as QUBO**: Express the problem as minimize x^T Q x where x ∈ {0,1}^n
2. **Continuous Relaxation**: Relax binary constraints x ∈ {0,1} to x ∈ [0,1]
3. **LogQ Encoding**: Apply logarithmic encoding to reduce variable dimensionality
4. **Gradient-Inspired Optimization**: Use gradient-like methods on the relaxed continuous variables
5. **Rounding**: Map continuous solution back to binary via thresholding or randomized rounding

## Key Patterns

### Pattern 1: Non-linear Continuous Relaxation

Instead of standard linear relaxation, LogQ uses non-linear transformation:
```
f(x) = log(x + ε) / log(2)  # maps [0,1] → [-∞, 0]
```
This creates sharper gradients near boundaries, accelerating convergence to binary solutions.

### Pattern 2: Gradient-Inspired Parameter Updates

After relaxation, parameters can be optimized using gradient-like methods:
- Momentum-based updates for faster convergence
- Adaptive learning rates per parameter
- No Pauli decomposition required (classical-only)

### Pattern 3: Quantum-to-Classical Translation

When a quantum algorithm shows promise but hardware limitations exist:
1. Identify the quantum-specific components (Pauli terms, measurements)
2. Replace with equivalent classical mathematical operations
3. Preserve the algorithmic structure and convergence properties
4. Validate against quantum simulation results

## Pitfalls

- **Non-convexity**: The relaxed problem may have local minima; use multiple restarts
- **Rounding loss**: Continuous-to-binary rounding may lose solution quality
- **Parameter sensitivity**: LogQ encoding parameters (ε, temperature) require tuning

## Comparison

| Approach | Qubits Needed | Circuit Depth | Solution Quality |
|----------|--------------|---------------|-----------------|
| Original LogQ | O(log n) | O(log² n) | High |
| LogQ Classical | 0 | N/A | Comparable |
| Standard QUBO solver | N/A | N/A | Variable |

## References

- arXiv: 2604.12925 - "From quantum to quantum-inspired: the LogQ algorithm"
