---
name: quantum-coordinate-descent
description: >
  Quantum optimization via coordinate descent (QUACOD) methodology for scalable
  scheduling and combinatorial optimization problems. Decomposes large QUBO/Ising
  problems into coordinate-wise quantum subroutines. Use when: quantum optimization,
  QUBO problems, coordinate descent quantum, scheduling optimization, large-scale
  quantum algorithms. Trigger words: QUACOD, coordinate descent quantum, quantum scheduling,
  QUBO decomposition, scalable quantum optimization.
---

# QUACOD: Quantum Coordinate Descent Optimization

Decompose large combinatorial optimization problems into coordinate-wise quantum
subroutines for scalable execution on NISQ and fault-tolerant devices.

## Core Idea

Standard QAOA/VQE struggle with >100 qubits. QUACOD partitions the problem:

1. Select coordinate subset S (small enough for quantum device)
2. Optimize x_S while fixing x_{not S} (classical context)
3. Iterate over coordinates until convergence

## Algorithm

### Problem Setup

min f(x) = x^T Q x + c^T x   (QUBO form)

Where x in {0,1}^n, Q is n x n matrix.

### QUACOD Iteration

For each iteration t:

1. **Coordinate Selection**:
   - Random: Pick k coordinates uniformly
   - Greedy: Pick coordinates with largest |gradient_i|
   - Quantum: Use quantum sampling from importance distribution

2. **Subproblem Solve**:
   Fix x_{not S} to current values, solve:
   min f_S(x_S) = x_S^T Q_SS x_S + (2 Q_S,notS x_notS + c_S)^T x_S

   Using QAOA or exact quantum solver on |S| qubits.

3. **Update**:
   Replace x_S with solution, keep x_notS fixed.

### Convergence

- **Monotone**: f(x^{t+1}) <= f(x^t) by construction
- **Rate**: O(1/sqrt(T)) for convex relaxation
- **Practical**: Converges in 10-50 iterations for typical problems

## Coordinate Selection Strategies

### Strategy 1: Block Coordinate
Partition variables into blocks B_1, ..., B_m
Cycle through blocks sequentially.

### Strategy 2: Gradient-Guided
Select coordinates with largest partial derivative magnitude:
|i| = |partial f / partial x_i|

Approximate derivative using finite differences.

### Strategy 3: Quantum Importance Sampling
Use quantum amplitude estimation to estimate importance:
p_i proportional to |partial f / partial x_i|^2

Sample k coordinates from this distribution.

## Scalability Analysis

| Method | Max Variables | Circuit Depth | Qubits |
|--------|--------------|---------------|--------|
| Full QAOA | ~50 | O(p*n^2) | n |
| QUACOD (k=10) | 10000 | O(p*k^2) | k |
| Classical CD | Unlimited | O(n) | 0 |

## Pitfalls

- **Local minima**: Coordinate descent can get stuck; add random restarts
- **Coupling strength**: Strong Q_ij coupling reduces decomposition benefit
- **Communication overhead**: Classical-quantum interface latency matters

## Applications

- Drone scheduling and routing
- Portfolio optimization
- Resource allocation in cloud computing
- Protein folding (contact map optimization)
