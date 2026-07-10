---
name: quantum-linear-system-residual
description: "Residual-based quantum linear system algorithm with dynamic stopping methodology. Use when solving linear systems Ax=b on quantum computers, implementing HHL-type algorithms, quantum PDE solvers, or designing efficient quantum algorithms with adaptive precision control."
---

# Quantum Linear System Solver with Residual-Based Dynamic Stopping

> A quantum linear system algorithm (QLSA) that uses residual-based error estimation with dynamic stopping criteria, applied to elliptic partial differential equations.

## Metadata
- **Source**: arXiv:2605.06414
- **Authors**: Xiantao Li
- **Published**: 2026-05-07
- **Categories**: quant-ph

## Core Methodology

### Key Innovation
Introduces a residual-based approach for estimating solution quality in quantum linear system algorithms, enabling dynamic stopping when sufficient precision is achieved without over-computing. Applied to elliptic PDEs, demonstrating practical advantage for scientific computing applications.

### Technical Framework

#### Step 1: Problem Formulation
Given linear system Ax = b where A is an N×N Hermitian matrix:
- Encode b as quantum state |b⟩
- Goal: prepare |x⟩ = A^{-1}|b⟩ / ||A^{-1}|b⟩||

#### Step 2: Residual Estimation
Instead of fixed iteration count, compute the residual:
```
r_k = b - Ax_k
```
Estimate ||r_k|| using quantum amplitude estimation:
- Prepare state |r_k⟩ using oracle queries
- Use amplitude estimation to estimate norm
- Stop when ||r_k|| / ||b|| < ε (target precision)

#### Step 3: Dynamic Stopping Criterion
```
while estimated_residual > tolerance:
    perform_one_qsvt_iteration()
    update_residual_estimate()
```

#### Step 4: QSVT Implementation
Using Quantum Singular Value Transformation (QSVT):
- Construct polynomial approximation of 1/x
- Apply block-encoding of A
- Use phase estimation for eigenvalue filtering
- Dynamic stopping adapts polynomial degree to needed precision

#### Step 5: Application to Elliptic PDEs
- Discretize PDE to obtain linear system
- Apply residual-based QLSA
- Complexity scales polylogarithmically in condition number

## Implementation Guide

### Prerequisites
- Qiskit, Pennylane, or equivalent quantum SDK
- Block encoding of the system matrix A
- State preparation oracle for |b⟩

### Step-by-Step
1. Block-encode the matrix A using quantum circuits
2. Prepare the initial state |b⟩ using state preparation circuits
3. Construct QSVT polynomial for matrix inversion
4. Implement residual estimation circuit
5. Run adaptive iterations with dynamic stopping
6. Measure solution properties from final quantum state

### Code Example (Conceptual)
```python
from qiskit import QuantumCircuit
from qiskit.circuit.library import QSVT
import numpy as np

def residual_based_qsvt(block_encode_a, state_b, tolerance=1e-3):
    """Residual-based QSVT for linear system solving."""
    max_iterations = 100
    for k in range(max_iterations):
        # Apply QSVT step
        circuit = QSVT(block_encode_a, polynomial_degree=k)
        
        # Estimate residual using amplitude estimation
        residual_norm = estimate_residual(circuit, state_b)
        
        if residual_norm < tolerance:
            print(f"Converged at iteration {k}")
            return circuit
        
    return circuit

def estimate_residual(circuit, state_b):
    """Estimate residual norm using amplitude estimation."""
    # Prepare |r⟩ = |b⟩ - A|x_k⟩
    # Use Hadamard test or amplitude estimation
    # Returns ||r|| / ||b||
    pass
```

## Applications
- **Scientific computing**: Solving discretized PDEs on quantum computers
- **Financial modeling**: Portfolio optimization via linear systems
- **Machine learning**: Quantum linear regression, kernel methods
- **Engineering**: Finite element analysis on quantum hardware

## Pitfalls
- Residual estimation requires additional quantum resources (ancilla qubits)
- Block encoding of large matrices can be expensive
- Dynamic stopping overhead must be balanced against fixed-iteration approaches
- Condition number of A critically affects convergence speed
- Current implementations assume fault-tolerant quantum hardware

## Related Skills
- quantum-circuit-builder
- quantum-distributed-snapshot
- quantum-tensor-network-ml
