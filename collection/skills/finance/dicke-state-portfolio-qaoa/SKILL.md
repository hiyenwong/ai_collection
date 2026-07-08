---
name: dicke-state-portfolio-qaoa
description: "Feasibility-preserving mixed Dicke state ansatz for Hamming weight constrained combinatorial optimization via variational quantum eigensolver (VQE). Eliminates penalty terms by structurally encoding equality and inequality constraints. Use when: building quantum circuits for portfolio optimization, constraint-preserving quantum algorithms, penalty-free QAOA, VQE for combinatorial finance."
metadata:
  arxiv_id: "2606.08504"
  published: "2026-06-07"
  authors: "various"
  tags: [quantum, portfolio, optimization, dicke-state, vqe, qaoa, finance, constraint-preserving]
---

# Dicke State Portfolio QAOA

## Overview

Feasibility-preserving mixed Dicke state ansatz for Hamming weight constrained combinatorial optimization. Extends density matrix formalism to structurally encode equality and inequality constraints into quantum circuits, eliminating the need for penalty terms in the objective function. Validated on combinatorial portfolio optimization with CMA-ES optimizer on IBM NISQ processors.

## Core Methodology

### Problem Mapping

Combinatorial portfolio optimization requires satisfying constraints (e.g., exactly k assets selected, sector limits). Standard approaches add quadratic penalty terms with tunable Lagrange multipliers, which:
- Bloat the objective landscape
- Require careful parameter tuning
- Degrade quantum circuit performance

### Mixed Dicke State Ansatz

1. **Pure Dicke State Ansatz**: Handles equality constraints (fixed Hamming weight). Constructs superposition of all states with exactly k qubits active.
2. **Mixed Dicke State Extension**: Handles inequality constraints via density matrix formalism. Generalizes pure states to mixtures over valid Hamming weight ranges.
3. **Tensor Product Composition**: Multiple constraint groups handled via tensor products of individual pure/mixed Dicke states.

### Circuit Structure

- Initial state prepared as Dicke state (feasible subspace only)
- Mixer preserves feasibility by construction (never leaves feasible subspace)
- Objective function = portfolio energy + linear bias (no quadratic penalties)
- CMA-ES optimizer for classical parameter tuning

## Application to Portfolio Optimization

### Step 1: Problem Formulation
- Map N assets to N qubits
- Define objective: minimize risk, maximize return
- Encode constraints as Hamming weight conditions

### Step 2: Ansatz Selection
- Single cardinality constraint → Pure Dicke state
- Range constraints (e.g., 3-5 assets) → Mixed Dicke state
- Multiple sectors → Tensor product of Dicke states

### Step 3: Optimization
- Use CMA-ES or similar gradient-free optimizer
- Compare against random search restricted to feasible subspace
- Advantage grows with feasible search space size

### Step 4: Hardware Deployment
- Apply noise mitigation techniques
- Optimize circuit transpilation for target backend
- Expect reduced fidelity on NISQ hardware vs simulation

## Key Advantages

1. **No penalty terms**: Constraints satisfied by circuit structure
2. **Eliminates hyperparameter tuning**: No Lagrange multipliers needed
3. **Handles both equality and inequality**: Unified framework
4. **Scalable to multiple constraints**: Via tensor products

## Pitfalls

- **NISQ noise**: Hardware experiments show noise mitigation and transpilation remain challenges
- **Ansatz depth**: Dicke state preparation can require deep circuits for large n
- **Optimizer choice**: CMA-ES outperforms random search but may still struggle on noisy hardware
- **Not quantum advantage**: Classical solvers still competitive for current problem sizes

## Related Papers

- 2606.10098v1: VQA for Dynamic Portfolio Optimization (hardware-aware ansatz design)
- 2606.07727v1: Expressibility-Coherence Trade-off for CVaR Portfolio
- 2606.03515v1: PQC for Bayesian Games (correlated equilibrium)
