---
name: quacod-quantum-optimization
description: "QUACOD methodology: Quantum Optimization via Coordinate Descent for scalable constrained optimization. Decomposes large optimization problems into subproblems solved via quantum circuits under qubit constraints. Use when: solving combinatorial optimization (portfolio optimization, scheduling, routing), scaling quantum algorithms to NISQ devices, applying coordinate descent to QUBO/Ising problems, or designing hardware-efficient quantum circuits for optimization."
---

# QUACOD: Quantum Optimization via Coordinate Descent

## Overview

QUACOD (Quantum Optimization via Coordinate Descent) addresses the core bottleneck of NISQ-era quantum optimization: limited qubit counts prevent solving large-scale real-world problems. By decomposing a high-complexity optimization problem into smaller subproblems via coordinate descent, each subproblem fits within available qubits and is solved quantumly.

**Key result**: 5x more drones, 35x more routes vs. SOTA quantum scheduling methods.

## Core Algorithm

### Step 1: Problem Formulation

Express the optimization as a QUBO/Ising model:

```
minimize f(x) = x^T Q x + c^T x
subject to: x ∈ {0,1}^n, Ax ≤ b
```

### Step 2: Coordinate Decomposition

Partition the n-bit variable vector into blocks of size k (where k ≤ available qubits):

```python
def coordinate_descent_quacod(Q, c, n, k, max_iterations=100):
    """
    Q: QUBO matrix (n×n)
    c: linear coefficients
    k: block size (≤ available qubits)
    """
    x = np.random.randint(0, 2, n)
    
    for iteration in range(max_iterations):
        # Select block of k variables (greedy or random)
        block = select_block(x, Q, k)
        
        # Fix variables outside block, optimize block quantumly
        sub_Q = Q[np.ix_(block, block)]
        sub_c = c[block] + 2 * Q[np.ix_(block, ~block)] @ x[~block]
        
        # Solve subproblem on quantum hardware
        x_block = quantum_optimize(sub_Q, sub_c)
        x[block] = x_block
        
        # Check convergence
        if converged(x):
            break
    
    return x
```

### Step 3: Quantum Subproblem Solver

For each subproblem, use hardware-efficient circuits:

- **Ansatz**: Alternating layers of single-qubit rotations + entangling gates
- **Cost function**: ⟨ψ(θ)|H_sub|ψ(θ)⟩ where H_sub encodes the QUBO
- **Optimizer**: Classical gradient-free (COBYLA, SPSA)

### Step 4: Block Selection Strategy

Critical for convergence speed:

| Strategy | When to Use |
|----------|------------|
| Greedy (max |Q_ij|) | Strong variable coupling |
| Random | Weak/no coupling structure |
| Graph-based (max-cut) | Sparse Q matrices |
| Adaptive | Unknown structure |

## Convergence Guarantees

- **Monotone descent**: Each quantum subproblem solve improves (or maintains) objective
- **Finite convergence**: For discrete problems, converges in finite iterations
- **Local optimality**: Converges to k-local optimum

## Application Patterns

### Portfolio Optimization

```python
# Mean-variance portfolio with cardinality constraint
# Q = λΣ - μμ^T, x ∈ {0,1}^n (asset selection)
# Cardinality: sum(x) = K

quacod_solve(Q, c, n, k=available_qubits, 
             constraints={'cardinality': K, 'budget': 1.0})
```

### Scheduling/Assignment

```python
# Job-shop scheduling → QUBO formulation
# Time-slot variables: x_{job, machine, time} ∈ {0,1}
quacod_solve(scheduling_qubo, n_jobs * n_machines * n_times, k=20)
```

### Feature Selection

```python
# Sparse model selection → L0-regularized regression
# Q_ij = X_i^T X_j, c_i = -2 X_i^T y
quacod_solve(feature_qubo, p_features, k=available_qubits)
```

## Hardware-Efficient Circuit Design

For NISQ devices, use shallow circuits:

```
┌─────────┐     ┌─────────┐
┤ RY(θ_0) ├─────┤ RY(θ_4) ├──■──
├─────────┤     ├─────────┤  │
┤ RY(θ_1) ├─────┤ RY(θ_5) ├──■──
├─────────┤     ├─────────┤     │
┤ RY(θ_2) ├─────┤ RY(θ_6) ├──■──
├─────────┤     ├─────────┤  │
┤ RY(θ_3) ├─────┤ RY(θ_7) ├──■──
└─────────┘     └─────────┘
```

**Depth**: O(k) for k qubits — fits NISQ coherence windows.

## Scaling Analysis

| Method | Max Variables | Qubits Needed |
|--------|---------------|---------------|
| Full QAOA | ~20 | n |
| QUACOD | ~100+ | k ≪ n |
| Classical CD | Unlimited | 0 |

QUACOD bridges the gap: quantum quality for subproblems, classical scaling for problem size.

## Key Insights

1. **Decomposition > brute force**: Better quantum results on small subproblems than poor results on oversized ones
2. **Hardware efficiency matters**: Shallow, native-gate circuits outperform deep theoretical circuits on real hardware
3. **Coordinate selection is critical**: Exploit problem structure for faster convergence

## Related Papers

- arXiv:2605.14001 — QUACOD: Quantum Optimization via Coordinate Descent (Nguyen et al., 2026)
