---
name: quantum-grover-admm-optimization
description: "Hybrid quantum-classical optimization methodology combining Grover-based quantum search with ADMM (Alternating Direction Method of Multipliers) for cardinality-constrained binary optimization. Achieves exponential improvement over unstructured Grover search. Use when solving constrained binary optimization, portfolio optimization with cardinality constraints, feature selection, or any problem combining Grover search with classical decomposition methods."
---

# Quantum Grover-ADMM Optimization

Methodology from arXiv:2603.14744 — exponential quantum improvements for cardinality-constrained binary optimization via Grover + ADMM hybrid framework.

## Core Algorithm

### Quantum Oracle for Fixed-Cardinality Subspace

For binary optimization with cardinality constraint `||x||_0 = k`:

1. **Exploit subspace structure**: Search space reduced from 2^n to C(n,k)
2. **Grover rotation complexity**: O(sqrt(C(n,k) / M)) where M = degeneracy of optima
3. **Exponential improvement** over unstructured search over {0,1}^n when k << n

### Hybrid Framework: ADMM + Grover

```
1. Decompose: Split problem via ADMM into subproblems
   - Quadratic subproblem → Grover oracle
   - Linear/constraint subproblem → classical solver

2. Alternate:
   a. Quantum step: Solve quadratic oracle via Grover search
   b. Classical step: Update dual variables and penalty terms
   c. Check convergence: ||x^{k+1} - z^{k+1}|| <= tolerance

3. Output: ε-approximate solution with consistency tolerance ε+δ
```

**Query complexity**: O(sqrt(C(n,k)) * n^6 * k^(3/2) / (sqrt(M) * ε² * δ))
**Classical overhead**: O(n^6 * k^(3/2) / (ε² * δ))

## Implementation Pattern

### Step 1: Problem Formulation

Express optimization as:
```
min x^T Q x + c^T x
s.t. ||x||_0 = k, x ∈ {0,1}^n
```

### Step 2: ADMM Decomposition

Introduce auxiliary variable z:
```
min f(x) + g(z)
s.t. x = z
```
- f(x): quadratic objective (quantum)
- g(z): cardinality constraint + penalties (classical)

### Step 3: Grover Oracle Construction

- Encode objective into phase oracle
- Prepare uniform superposition over fixed-cardinality subspace
- Apply Grover iterations: O(sqrt(C(n,k)/M))

### Step 4: Classical ADMM Update

- z-update: Project onto cardinality constraint (keep top-k elements)
- Dual update: u ← u + (x - z)
- Penalty parameter scheduling

## When to Use

- Cardinality-constrained portfolio optimization
- Sparse feature selection in ML
- Compressed sensing with sparsity constraints
- Any binary optimization where solution has known cardinality

## Key Advantages

1. **Exponential speedup** in Grover iterations vs. full-space search
2. **Guaranteed convergence** to ε-approximate solution
3. **Practical quantum resource usage** — only quadratic oracle needs quantum hardware
4. **Scalable** — C(n,k) grows polynomially for fixed k, exponentially for k ~ n/2

## Activation Keywords

- Grover optimization
- ADMM quantum
- cardinality constraint optimization
- binary optimization quantum
- constrained quantum search
- hybrid quantum-classical ADMM
- portfolio optimization quantum
- sparse optimization Grover

## Resources

- arXiv:2603.14744 — "Towards Exponential Quantum Improvements in Solving Cardinality-Constrained Binary Optimization"
