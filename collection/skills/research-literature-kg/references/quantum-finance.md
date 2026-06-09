# Quantum Finance Patterns

Reusable patterns from quantum computing applied to finance, economics, and investment.

## QAOA for Portfolio Optimization

### QUBO Formulation
Map portfolio mean-variance optimization to QUBO:
```
H_C = -μ^T w + λ w^T Σ w + A(Σ w_i - B)²
```
- Budget constraint via penalty A or XY-mixer
- Cardinality constraint: Σ z_i = K (binary asset selection)

### Mixer Selection
- **X-mixer**: Unconstrained, explores full Hilbert space — budget constraint via penalty
- **XY-mixer**: Preserves Hamming weight — enforces cardinality natively, no penalty distortion
- **Trotterization**: XY-mixer requires Trotter decomposition; trade depth vs accuracy

### Counterdiabatic QAOA (CCD-QAOA)
- Add CD terms: H_CD ≈ Σ α_j [H_C, [H_C, H_M]] (nested commutators)
- Approximates adiabatic gauge potentials
- Improves convergence speed and solution quality at fixed depth p

## Information-Theoretic Portfolio Selection

CRRA utility portfolio selection via information geometry:
```
CE_growth = D_α(p_portfolio || p_market) + H_α(p_risk_tilted) + log(Z)
```
- Renyi order α = investor's risk aversion coefficient
- Single-period: decompose into divergence + entropy + partition terms
- Multi-period: extend with temporal information flow constraints

## Hybrid Classical-Quantum Trading Pipeline

1. **Covariance estimation**: Ledoit-Wolf shrinkage (robust, handles N > T)
2. **Correlation clustering**: Hierarchical clustering → decorrelated asset groups
3. **Asset selection**: Pick top asset per cluster → reduced universe (e.g., 500 → 10)
4. **Weight optimization**: QAOA on QUBO or classical GA baseline
5. **Walk-forward evaluation**: Rolling train/test, no look-ahead bias

## Noise Characterization

- **Landscape Span Compression (LSC)**: Device-agnostic metric; measures how noise flattens QAOA energy landscape
- LSC → 1 as landscape collapses to barren plateau
- IBM Heron r2: noise compresses landscape by 24-30% without displacing global minimum
- ZNE (Zero Noise Extrapolation): mixed results (+7%/+9%/-4%)

## Quantum Advantage Assessment

- **Expert Analysis Evaluation**: Financial professional judgment as independent benchmark
- Gap between algorithmic metrics and financial applicability
- NISQ constraint: 100+ asset problems need decomposition or hot-starting
- **Hot-starting**: Continuous relaxation → compact Hilbert space → ~50 qubits vs ~700
