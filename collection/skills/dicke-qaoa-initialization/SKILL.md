---
name: dicke-qaoa-initialization
description: "QAOA barren plateau mitigation via Dicke state initialization and Trotterized adiabatic parameter schedule. Use when designing constraint-preserving QAOA for portfolio optimization, direct indexing, or any NISQ combinatorial problem where standard transverse-field mixers fail to enforce hard constraints. Covers Dicke state preparation, XY-mixer Hamiltonians, adiabatic-inspired parameter initialization, and Sharpe ratio backtesting methodology."
---

# QAOA with Dicke State Initialization & Trotterized Adiabatic Scheduling

## Methodology

Standard QAOA with transverse-field mixers fails to strictly enforce hard constraints (e.g., cardinality K-of-N). This approach solves both barren plateaus and constraint violations simultaneously.

### Dicke State Initialization

Prepare the initial state as a Dicke state (uniform superposition of all Hamming weight K states):

```
|D(n, K)⟩ = (1/√C(n,K)) Σ_{|x|=K} |x⟩
```

This ensures the quantum evolution stays in the feasible subspace from the start, not just approximately.

### XY-Mixer Hamiltonian

Replace transverse field mixer with XY-mixer that strictly preserves Hamming weight:

```
H_XY = Σ_{i<j} (X_i X_j + Y_i Y_j)
```

This guarantees only valid portfolios of exactly size K are explored during evolution.

### Trotterized Adiabatic Parameter Schedule

Initialize QAOA parameters (γ, β) using a Trotterized schedule inspired by adiabatic quantum computing:

```
γ_k = Δt · s(k/p) · f_C
β_k = Δt · (1 - s(k/p)) · f_M
```

where s(t) is a smooth interpolation (e.g., linear or sine ramp) from 0 to 1, p is QAOA depth, and Δt is the Trotter step size.

This mitigates barren plateaus by starting near the adiabatic path, providing good initial parameters for classical optimization.

## Implementation Steps

1. **Dicke State Preparation**:
   - Use the Grover-Rudolph or quantum signal processing approach
   - For small n (≤20), prepare via cascaded controlled-rotations
   - Validate: measure Hamming weight distribution, expect all samples at K

2. **XY-Mixer Construction**:
   - Decompose H_XY into native gates: CNOT + RY rotations
   - Use Trotter-Suzuki decomposition for time evolution: exp(-iβ H_XY) ≈ (∏ exp(-iβ/N X_i X_j + Y_i Y_j))^N
   - Balance Trotter steps vs circuit depth for NISQ hardware

3. **Adiabatic Parameter Initialization**:
   - Set initial γ, β from the discretized adiabatic schedule
   - Use classical optimizer (COBYLA, SPSA) to refine from this warm start
   - For direct indexing: initialize with HRP or minimum-variance classical solution

4. **Backtesting & Validation**:
   - Compare Sharpe Ratio against SA and HRP baselines
   - Analyze turnover rate (76.8% observed in 10-stock backtest)
   - Evaluate implementation costs vs theoretical optimality trade-off

## Key Results (Mancilla et al., 2026)

- **Sharpe Ratio**: QAOA 1.81 vs SA 1.31 vs HRP 0.98 (10 US equities, 2025)
- **Turnover**: 76.8% (high — discuss implementation cost implications)
- **Depth**: Works at p ≤ 5 on NISQ-era devices
- **Constraints**: Strictly enforced (no penalty terms needed)

## When to Use

- Constrained portfolio optimization (cardinality, ESG, sector limits)
- Direct indexing with K-of-N asset selection
- Any QAOA problem with hard combinatorial constraints
- Mitigating barren plateaus in variational quantum algorithms

## Pitfalls

- **High turnover**: Theoretical optimality may have high implementation costs in institutional settings
- **Trotter errors**: XY-mixer requires Trotter decomposition; too few steps → constraint drift
- **Dicke state depth**: Preparation circuit depth grows with n; use approximate methods for n > 20
- **Hardware noise**: NISQ noise floors limit achievable solution quality; use error mitigation

## References

- arXiv:2602.14827 — Constrained Portfolio Optimization via QAOA with XY-Mixers and Trotterized Initialization
