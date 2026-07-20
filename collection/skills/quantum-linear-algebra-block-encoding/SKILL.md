---
name: quantum-linear-algebra-block-encoding
description: "Design and implement quantum algorithms using block encoding methodology for quantum linear algebra. Block encoding embeds a matrix as a sub-block of a larger unitary, enabling quantum singular value transformation (QSVT), quantum linear system solvers, and Hamiltonian simulation. Use when implementing quantum linear algebra algorithms, building matrix arithmetic circuits, or working with QSVT/HHL-style algorithms. Trigger words: block encoding, quantum linear algebra, QSVT, quantum singular value transformation, matrix encoding quantum, quantum matrix arithmetic."
---

# Quantum Linear Algebra via Block Encoding

Design quantum algorithms using block encoding methodology. Block encoding embeds a non-unitary matrix A as a sub-block of a larger unitary U, enabling composition of matrix operations without low-level circuit construction.

## Core Concept

A block encoding of matrix A is a unitary U where:
```
U = [A/α  · ]
    [ ·   · ]
```
α is the normalization factor (subnormalization), ensuring ||A|| ≤ α.

## Key Operations

### 1. Arithmetic Composition

Block encodings compose via standard operations:

| Operation | Subnormalization | Qubit Overhead |
|-----------|-----------------|----------------|
| Addition A + B | α + β | O(1) ancilla |
| Multiplication A·B | α·β | O(1) ancilla |  
| Tensor product A⊗B | α·β | 0 ancilla |
| Linear combination Σ cᵢAᵢ | Σ|cᵢ|αᵢ | O(log n) ancilla |

### 2. Quantum Singular Value Transformation (QSVT)

Apply polynomial P to singular values of A:
```
QSVT: U → polynomial(P, U) = [P(A/α)  ·]
                              [ ·      ·]
```

Common polynomials:
- **Matrix inversion**: P(x) ≈ 1/x (for HHL-style solvers)
- **Matrix exponential**: P(x) ≈ e^{ixt} (Hamiltonian simulation)
- **Projection**: P(x) ≈ step function (eigenvalue filtering)

### 3. Input Models

| Input Model | Block Encoding Cost | Use Case |
|------------|-------------------|----------|
| Sparse matrix | O(1) queries | Sparse linear systems |
| LCU (Linear Combination of Unitaries) | O(1) state prep | Hamiltonian simulation |
| QRAM access | O(1) queries | Dense matrix operations |
| Quantum RAM state prep | O(log n) | Data loading |

## Design Patterns

### Pattern 1: Quantum Linear System Solver

To solve Ax = b:
1. Block encode A with normalization α
2. Use QSVT with polynomial P(x) ≈ 1/x
3. Apply to state |b⟩
4. Result: |x⟩ ∝ A⁻¹|b⟩

Complexity: O(κ·α·polylog(n)/ε) where κ = condition number

### Pattern 2: Hamiltonian Simulation

To simulate e^{-iHt}:
1. Block encode H with normalization α
2. Use QSVT with polynomial approximating e^{-iαtx}
3. Query complexity: O(αt + log(1/ε))

### Pattern 3: Matrix Function Evaluation

For any function f:
1. Block encode A
2. Construct polynomial approximation of f
3. Apply QSVT

### Pattern 4: Resource Estimation

Before circuit execution:
- Gate count: Track per composition step
- Qubit count: log(d) + ancilla per operation
- Normalization: Product of α factors (critical for success probability)

## Implementation Checklist

- [ ] Identify input model (sparse, LCU, QRAM)
- [ ] Determine block encoding construction
- [ ] Compute subnormalization α
- [ ] Design polynomial approximation for target function
- [ ] Estimate resource requirements (qubits, gates, depth)
- [ ] Verify normalization factors at each composition step
- [ ] Account for amplitude amplification overhead (probability ~ 1/α²)

## Common Pitfalls

1. **Normalization blowup**: Each composition multiplies α → track carefully
2. **Polynomial degree**: Higher accuracy → higher degree → more queries
3. **Condition number dependence**: Linear system solving scales with κ
4. **Ancilla qubits**: Composition requires fresh ancilla per step

## References

- **Unitaria**: Python library for block encoding composition (arXiv: 2605.10768)
- **Gilyén et al.**: Quantum Singular Value Transformation (2019)
- **Childs et al.**: Quantum Linear Systems algorithms

## Activation

- block encoding quantum
- quantum linear algebra
- QSVT quantum singular value transformation
- quantum matrix arithmetic
- quantum HHL algorithm
- quantum linear system solver
- Hamiltonian simulation block encoding
