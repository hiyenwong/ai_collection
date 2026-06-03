---
name: hybrid-quantum-classical-trading
description: Hybrid classical-quantum trading framework combining classical asset selection (Ledoit-Wolf shrinkage covariance, hierarchical correlation clustering) with quantum optimization (QAOA) for portfolio rebalancing. Uses walk-forward evaluation, GPU-accelerated GA for weight optimization, and QUBO scheduling. Use when building algorithmic trading systems with quantum components, hybrid portfolio rebalancing, walk-forward QUBO evaluation, or integrating classical finance with quantum optimization.
---

# Hybrid Quantum-Classical Trading Framework

End-to-end portfolio construction and rebalancing combining classical finance with quantum optimization.

## Architecture

### Phase 1: Classical Asset Selection

1. **Covariance Estimation**: Ledoit-Wolf shrinkage for robust covariance matrix
2. **Correlation Clustering**: Hierarchical clustering to identify asset groups
3. **Decorrelation**: Select n assets from each cluster (e.g., S&P 500 → 10 decorrelated stocks)
4. **Survivorship-Bias-Free**: Use point-in-time universe data

### Phase 2: Portfolio Weight Optimization

**Classical baselines:**
- Minimum variance (closed-form)
- Equal weight
- Entropy-regularized Genetic Algorithm (GPU-accelerated)

**Quantum optimization:**
- Map to QUBO: minimize w^T Σ w subject to Σ w_i = 1
- Solve via QAOA with appropriate mixer
- Hybrid classical-quantum loop

### Phase 3: Walk-Forward Evaluation

```
for t in training_windows:
    train on [t-window, t]
    test on [t, t+holding_period]
    record Sharpe, returns, drawdown
```

## QUBO Formulation

For portfolio optimization:
```
min w^T Σ w - λ μ^T w + A(Σ w_i - 1)²
```

Key design choices:
- Discretize weights to binary variables
- Penalty coefficient A must be large enough but not too large
- Use constraint-preserving mixers (XY-mixer) when possible

## Implementation Notes

- **Walk-forward**: Critical for realistic backtesting; avoid look-ahead bias
- **GPU acceleration**: Entropy-regularized GA runs efficiently on GPU
- **QAOA depth**: p=1-3 for NISQ devices; higher p for simulation
- **Benchmarking**: Always compare against classical baselines

## Activation

quantum trading, hybrid portfolio, walk-forward evaluation, QUBO scheduling, Ledoit-Wolf, correlation clustering, algorithmic trading quantum, QAOA trading
