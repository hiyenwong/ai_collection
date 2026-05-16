---
name: qaoa-constrained-portfolio-optimization
description: Methodology for constrained portfolio optimization using Constrained Counterdiabatic QAOA (CCD-QAOA). Incorporates approximate adiabatic gauge potentials via nested commutators into variational ansatz for improved optimization under budget and risk constraints. Use when optimizing portfolios with quantum algorithms, implementing QAOA with constraints, designing quantum mixers for finance, or applying counterdiabatic driving to combinatorial optimization. Covers QUBO formulation, XY-mixer constraints, CD terms, and real-device deployment.
---

# QAOA Constrained Portfolio Optimization

Constrained Counterdiabatic QAOA (CCD-QAOA) for portfolio optimization under realistic budget and risk constraints.

## Core Methodology

### Problem Formulation

Portfolio optimization maps to QUBO:
```
H_C = -μ^T w + λ w^T Σ w  (minimize risk-adjusted return)
```
with constraints:
- Budget: Σ w_i = B
- Cardinality: Σ z_i = K (number of assets)
- Bounds: w_min ≤ w_i ≤ w_max

### CCD-QAOA Ansatz

Standard QAOA: U(β,γ) = ∏ exp(-iβ_k H_M) exp(-iγ_k H_C)

CCD-QAOA adds counterdiabatic terms:
```
H_CD ≈ Σ α_j [H_C, [H_C, H_M]]  (nested commutators)
```

The CD terms approximate adiabatic gauge potentials, improving convergence speed and solution quality.

### XY-Mixer for Constraints

Use Hamming weight-preserving XY mixer to restrict evolution to feasible subspace:
```
H_XY = Σ (X_i X_j + Y_i Y_j)
```
This naturally preserves budget constraints without penalty terms.

## Implementation Steps

1. **Formulate QUBO**: Convert portfolio problem to Ising Hamiltonian
2. **Design Mixer**: Choose XY-mixer to preserve constraints
3. **Compute CD Terms**: Generate nested commutators [H_C, [H_C, H_M]]
4. **Construct Ansatz**: U(β,γ,α) = ∏ exp(-iβ_k H_M) exp(-iγ_k H_C) exp(-iα_k H_CD)
5. **Optimize Parameters**: Classical optimizer minimizes ⟨ψ|H_C|ψ⟩
6. **Sample Solutions**: Measure to get portfolio configurations

## Key Considerations

- **Trotterization errors**: XY-mixer implementation requires Trotter decomposition; balance depth vs accuracy
- **Noise characterization**: Use Landscape Span Compression (LSC) metric to quantify hardware noise impact
- **Parameter initialization**: Warm-start from classical solution improves convergence
- **Depth vs Performance**: QAOA depth p trades circuit depth for solution quality

## Activation

quantum portfolio optimization, QAOA, counterdiabatic, XY-mixer, constrained optimization, QUBO finance, quantum trading algorithm
