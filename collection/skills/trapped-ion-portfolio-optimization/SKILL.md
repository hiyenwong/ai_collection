---
name: trapped-ion-portfolio-optimization
description: "Large-scale portfolio optimization on trapped-ion quantum computers. End-to-end pipeline for portfolio selection with cardinality constraints using hardware-aware decomposition on trapped-ion quantum processors. Use when: trapped-ion quantum computing, portfolio optimization with cardinality constraints, hardware-aware quantum decomposition, NISQ-era financial optimization, quantum asset selection, quantum computing finance benchmark, arXiv:2602.23976."
---

# Trapped-Ion Portfolio Optimization

## Description

Large-scale portfolio optimization demonstrated on trapped-ion quantum processors. Addresses cardinality-constrained portfolio selection via hardware-aware decomposition, enabling quantum advantage on current NISQ devices for realistic financial problems.

## Core Methodology

### 1. Problem Formulation

Map mean-variance portfolio optimization with cardinality constraints to QUBO/Ising:

```
min w^T Σ w - λ μ^T w + γ (Σ w_i - 1)^2 + ρ (Σ z_i - k)^2
```

Where:
- `w_i`: portfolio weights (continuous)
- `z_i`: binary selection indicators (asset included or not)
- `k`: cardinality constraint (max assets to hold)
- `λ`: risk aversion parameter
- `γ, ρ`: penalty coefficients

### 2. Hardware-Aware Decomposition

Key innovation: decompose large portfolio problems to fit trapped-ion hardware limits.

**Decomposition Pipeline:**
1. **Classical pre-screening**: Filter assets by Sharpe ratio / liquidity
2. **Subproblem partitioning**: Split remaining assets into subsets matching qubit count
3. **Quantum optimization**: Solve each subproblem on trapped-ion QPU
4. **Classical aggregation**: Merge sub-solutions with global constraint enforcement

### 3. Trapped-Ion Advantages

- **All-to-all connectivity**: No SWAP overhead, direct qubit interactions
- **High-fidelity gates**: >99.9% single-qubit, >99% two-qubit
- **Native Mølmer-Sørensen gates**: Efficient for portfolio QUBO terms
- **Flexible qubit count**: Scale from 10s to 100s of qubits

### 4. Cardinality Constraint Handling

Two approaches demonstrated:
- **Penalty method**: Add `ρ(Σ z_i - k)^2` to Hamiltonian
- **Constraint-preserving mixer**: XY-mixer that maintains valid cardinality

## Activation Keywords

- trapped-ion portfolio optimization
- hardware-aware quantum decomposition
- cardinality constraints portfolio quantum
- quantum asset selection trapped ion
- NISQ portfolio optimization
- 2602.23976

## Key Findings

1. End-to-end quantum advantage demonstrated on real trapped-ion hardware
2. Hardware-aware decomposition enables solving 100+ asset problems
3. Cardinality constraints handled efficiently via penalty or mixer methods
4. Quantum solutions competitive with classical heuristics at small scale

## Related Skills

- [[quantum-portfolio-optimization]] - General QAOA portfolio optimization
- [[cd-qaoa-portfolio-optimization]] - Counterdiabatic QAOA
- [[two-step-qaoa-portfolio]] - Two-step QAOA approach
- [[quantum-finance-portfolio]] - Comprehensive quantum finance
