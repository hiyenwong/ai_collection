---
name: quantum-optimal-transport-entanglement
description: "Bipartite entanglement measurement via minimal quantum Wasserstein distance to separable states — Lipschitz dual formulation, entanglement witness connection, and experimental detection framework."
category: quantum
---

# Quantum Optimal Transport Entanglement Measure

## Context

Based on arXiv:2606.04969 (Shao, Chen, He, Jun 2026). Proposes a bipartite entanglement measure defined as the minimal order-1 quantum Wasserstein distance from a state to the set of separable states.

## Core Methodology

1. **Define entanglement measure**: E(ρ) = min_{σ separable} W_1(ρ, σ) — the minimal quantum Wasserstein distance to the separable set
2. **Verify axioms**: Owing to universal data-processing inequality of Wasserstein metric, satisfies all fundamental entanglement axioms within a single geometric framework
3. **Lipschitz dual formulation**: Derive explicit lower bounds for pure and mixed states using the dual variational problem
4. **Two-qubit sharp constant**: Establish sharp constant for two-qubit systems
5. **Haar-random expected value**: Compute expected entanglement value for Haar-random pure states
6. **Witness connection**: Prove that any negative witness expectation certifies a lower bound on E; dual variational bound equals maximal violation by Lipschitz-1 witness
7. **Subadditivity and trace-distance estimates**: Establish bounds on local observables and point toward large-deviation conjectures

## Implementation Steps

1. Define the quantum Wasserstein distance W_1 on the state space
2. Identify the set of separable states as the reference set
3. Solve the minimization problem: min_{σ ∈ Separable} W_1(ρ, σ)
4. Use the Lipschitz dual formulation to compute lower bounds efficiently
5. For experimental detection: construct Lipschitz-1 witnesses and measure their expectation values
6. The maximal witness violation provides a certified lower bound on entanglement

## Key Results

- Single geometric framework satisfies all entanglement measure axioms
- Lipschitz dual gives computable lower bounds for both pure and mixed states
- Sharp constant established for two-qubit systems
- Quantitative connection to entanglement witnesses: negative witness → certified lower bound on E
- Natural subadditivity and trace-distance estimates

## Pitfalls

- Computing the exact minimum over separable states is generally hard; use dual bounds in practice
- The Wasserstein metric definition depends on the choice of underlying geometry
- Large-deviation conjectures remain open — current results provide bounds, not exact asymptotics

## Verification

- For known entangled states (Bell states), verify E > 0
- For separable states, verify E = 0
- Check that the measure does not increase under LOCC (local operations and classical communication)
- Compare witness-based lower bounds against known entanglement measures (concurrence, negativity)

## Activation

- quantum optimal transport, entanglement measure, Wasserstein distance, Lipschitz witness, separable states
- 量子最优传输, 纠缠度量,  Wasserstein距离, Lipschitz见证
