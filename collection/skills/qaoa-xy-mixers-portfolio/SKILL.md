---
name: qaoa-xy-mixers-portfolio
description: "Constraint-preserving QAOA formulation using Dicke state initialization and XY-mixer Hamiltonian for direct indexing portfolio optimization. Use when: implementing QAOA with hard cardinality constraints; designing constraint-preserving quantum ansatzes; mitigating barren plateaus via Trotterized initialization; comparing quantum vs classical portfolio optimization (SA, HRP); Direct Indexing with ESG constraints. Keywords: qaoa, xy-mixer, dicke state, portfolio optimization, constraint-preserving, direct indexing, barren plateau, hamming weight"
---

# QAOA with XY-Mixers for Constrained Portfolio Optimization

## Core Concept

Standard QAOA with transverse field mixers fails to enforce hard cardinality constraints, requiring soft penalties that distort the energy landscape. This formulation uses **XY-mixer Hamiltonians** that strictly preserve Hamming weight, ensuring only valid portfolios of size K are explored.

## Key Innovation: Constraint Preservation

### Standard QAOA (fails for constraints)
```
H_mixer = Σ X_i  # Transverse field
```
Mixes all bitstrings → violates cardinality constraint K

### XY-Mixer QAOA (preserves constraints)
```
H_mixer = Σ (X_i X_j + Y_i Y_j)  # For adjacent pairs
```
Conserves total magnetization → preserves Hamming weight K

## Algorithm Steps

### Step 1: Dicke State Initialization

Initialize in a Dicke state |D(n,K)⟩ with exactly K qubits in |1⟩:
- Encodes the cardinality constraint from the start
- Inspired by adiabatic quantum computing
- Avoids the "all-zeros" barren plateau

### Step 2: Trotterized Parameter Schedule

Use adiabatic-inspired parameter initialization:
```
γ_p = (p/P) * γ_max   # Problem Hamiltonian
β_p = (1 - p/P) * β_max  # Mixer Hamiltonian
```
This mimics adiabatic evolution, reducing barren plateaus.

### Step 3: QAOA Circuit Construction

```
|ψ⟩ = ∏_p [exp(-i β_p H_XY) · exp(-i γ_p H_cost)] |D(n,K)⟩
```

### Step 4: Measurement and Portfolio Selection

- Measure the final state
- Select the bitstring with minimum energy
- The K assets with bit=1 form the portfolio

## Performance Benchmarks

| Method | Sharpe Ratio | Turnover |
|--------|-------------|----------|
| QAOA (XY-mixer) | 1.81 | 76.8% |
| Simulated Annealing | 1.31 | - |
| Hierarchical Risk Parity | 0.98 | - |

Backtested on 10 US equities over 2025.

## Pattern: Constraint-Preserving Ansatz Design

When quantum algorithms must respect hard constraints:
1. Identify the conserved quantity (e.g., Hamming weight = K)
2. Design a mixer Hamiltonian that preserves it
3. Initialize in a state that satisfies the constraint
4. Verify constraint preservation throughout the circuit

## Comparison: XY-Mixer vs Transverse Field

| Property | XY-Mixer | Transverse Field |
|----------|----------|-----------------|
| Hamming weight | Preserved | Not preserved |
| Search space | C(n,K) valid states | 2^n all states |
| Penalty terms | Not needed | Required (distorts landscape) |
| Circuit complexity | O(n²) gates | O(n) gates |

## Operational Considerations

- **High turnover** (76.8%): Trade-off between theoretical optimality and implementation costs
- **Transaction costs**: Must factor into backtesting
- **Institutional constraints**: ESG mandates, sector limits
- **Rebalancing frequency**: Weekly vs monthly impacts costs

## Pitfalls

- **Barren plateaus**: Without Trotterized initialization, gradients vanish
- **Gate overhead**: XY-mixer requires O(n²) gates vs O(n) for transverse field
- **NISQ limitations**: Deep circuits suffer from noise
- **Classical comparison**: Ensure fair comparison with tuned classical baselines

## References

- arXiv: 2602.14827 - "Constrained Portfolio Optimization via QAOA with XY-Mixers"
