---
name: hot-start-quantum-portfolio-optimization
description: Hot-starting methodology for quantum portfolio optimization using continuous relaxation to construct compact Hilbert space, reducing qubit requirements for QUBO formulations. Based on arXiv:2510.11153v1.
category: quantum-finance
trigger_words: hot-start quantum portfolio, quantum warm-start, QUBO portfolio optimization, continuous relaxation quantum, compact Hilbert space portfolio
arxiv_id: "2510.11153"
authors: Sebastian Schlütter, Tomislav Maras, Alexander Dotterweich, Nico Piatkowski
source: arxiv
---

# Hot-Starting Quantum Portfolio Optimization

## Overview

Novel hot-starting approach for quantum portfolio optimization that leverages continuous relaxation solutions to construct a compact Hilbert space, dramatically reducing qubit requirements for QUBO formulations.

## Core Methodology

### Problem Setting
- Discrete mean-variance portfolio optimization: assets must be traded in integer quantities
- Objective function is smooth and convex
- Optimal continuous solution can be computed efficiently classically

### Hot-Starting Strategy

1. **Solve Continuous Relaxation**: Find optimal solution to the continuous (non-discrete) version efficiently
2. **Construct Compact Hilbert Space**: Restrict quantum search to discrete solutions near the continuous optimum
3. **QUBO Reformulation**: Encode only the neighborhood region, not the full search space
4. **Qubit Reduction**: The number of qubits scales with the neighborhood size, not the total asset space

### Key Innovation

Previous warm-start strategies for gate-based quantum optimization did not explicitly integrate continuous relaxation insights into the QUBO formulation. This method constructs a restricted search space around the continuous optimum, making quantum optimization tractable for larger portfolios.

## Implementation Pipeline

```
Continuous Solution → Neighborhood Definition → Compact Hilbert Space → QUBO Encoding → Quantum Solver
```

### Step 1: Continuous Relaxation
- Solve the smooth convex portfolio optimization problem classically
- Obtain optimal continuous weights w*

### Step 2: Neighborhood Construction
- Define discrete grid around w*
- Size determined by acceptable deviation from continuous optimum
- Trade-off: smaller neighborhood = fewer qubits but potentially suboptimal

### Step 3: Binary Encoding
- Map discrete variables in the neighborhood to binary variables
- Use compact encoding schemes (logarithmic in neighborhood size)

### Step 4: QUBO Formulation
- Express portfolio objective as Quadratic Unconstrained Binary Optimization
- Constraints encoded as penalty terms

### Step 5: Quantum Solving
- Deploy on quantum annealer (D-Wave Advantage) or gate-based QAOA
- Compare with classical baselines

## Advantages

- **Qubit Efficiency**: Reduces required qubits from O(n) to O(log(neighborhood_size))
- **Solution Quality**: Outperforms state-of-the-art techniques on both software solvers and D-Wave Advantage
- **Scalability**: Enables larger portfolio problems on NISQ hardware

## When to Use

- Portfolio optimization with integer quantity constraints
- QUBO problems with smooth convex objectives
- Scenarios where continuous relaxation is efficiently solvable
- NISQ-era quantum optimization with limited qubit budgets

## References

- arXiv:2510.11153v1 "Hot-Starting Quantum Portfolio Optimization"
