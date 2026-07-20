# VQE+WCVaR+CMA-ES Portfolio Optimization

## Source
arXiv:2508.18625 — "Achieving High-Quality Portfolio Optimization with the Variational Quantum Eigensolver" (Lv, Ma, Wang, Wang, 2025)

## Methodology

### Pipeline
```
Portfolio Data → QUBO Matrix → Hamiltonian → VQE(WCVaR + CMA-ES) → Binary Allocation
```

### Key Components

**WCVaR (Weighted Conditional Value-at-Risk)**
- Integrates CVaR over multiple confidence levels: WCVaR = ∫₀¹ CVaR_α · w(α) dα
- More robust tail-risk assessment than single-level CVaR
- Encoded in QUBO via auxiliary variables for tail scenarios

**CMA-ES Optimizer**
- Covariance Matrix Adaptation Evolution Strategy replaces gradient-based optimizers
- Population size: 4 + ⌊3·ln(n_params)⌋
- Advantages: gradient-free (avoids barren plateaus), adaptive covariance, global exploration

**QUBO Formulation**
- x^T Q x where Q encodes returns (linear), covariance (quadratic), constraints (penalty)
- Budget/cardinality constraints as penalty terms

### Comparison with Existing Approaches
| Approach | Optimizer | Risk Measure | Key Differentiator |
|----------|-----------|--------------|-------------------|
| QAOA | Quantum annealing | Mean-variance | Hardware-native but limited depth |
| QAOA-ZNE | Quantum + ZNE | Mean-variance | Error mitigation focus |
| Dicke State | VQE | Constraint-preserving | Feasibility-preserving ansatz |
| **VQE-WCVaR-CMAES** | **CMA-ES** | **WCVaR (multi-level)** | **Tail-risk + gradient-free optimization** |

## Implementation Notes
- CMA-ES is robust to noisy quantum evaluations (important for NISQ hardware)
- WCVaR requires more qubits than mean-variance (auxiliary variables)
- Warm-start from classical solution improves convergence

## Related Skills
- [[quantum-portfolio-optimizer]] — QAOA-based portfolio
- [[qaoa-zne-portfolio]] — QAOA with error mitigation
- [[dicke-state-ansatz-vqe]] — Feasibility-preserving VQE ansatz
- [[vqe-cvar-portfolio]] — Full skill for this methodology
