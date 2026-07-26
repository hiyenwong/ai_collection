# QUBO Formulation Guide

## Mathematical Framework for Quantum Portfolio Optimization

### Standard Markowitz Formulation

The classical Markowitz mean-variance optimization:

```
min w'Σw - μ'w
s.t. Σ w_i = 1
     w_i ≥ 0
```

Where:
- w: weight vector
- Σ: covariance matrix
- μ: expected returns

### Binary QUBO Conversion

For quantum optimization, convert to binary variables:

```
Let x_i ∈ {0, 1} represent selection of asset i
(1 = selected, 0 = not selected)

QUBO: min x'Qx

Where Q = -μ + λΣ (combining returns and risk)
```

### Penalty Method for Constraints

Add constraint violations as penalty terms:

```
Q_total = Q_objective + P * (constraint_penalty)

Example for cardinality constraint (k assets):
Penalty = (Σ x_i - k)^2
```

### Higher-Order Moments (QUBO Extension)

From arxiv:2509.01496:

**Skewness term** (3rd order):
```
S_ijk = E[(r_i - μ_i)(r_j - μ_j)(r_k - μ_k)]

Objective includes: -γ Σ_ijk S_ijk x_i x_j x_k
```

**Kurtosis term** (4th order):
```
K_ijkl = E[(r_i - μ_i)(r_j - μ_j)(r_k - μ_k)(r_l - μ_l)]

Objective includes: δ Σ_ijkl K_ijkl x_i x_j x_k x_l
```

### Encoding Higher-Order Terms

Higher-order terms must be reduced to quadratic:

```
x_i x_j x_k → x_ij x_k + penalty

Where x_ij is auxiliary variable representing x_i AND x_j
```

### Parameter Selection Guidelines

| Parameter | Range | Purpose |
|-----------|-------|---------|
| λ (risk) | 0.1 - 1.0 | Risk aversion |
| γ (skewness) | 0.01 - 0.1 | Skewness preference |
| δ (kurtosis) | 0.01 - 0.1 | Tail risk control |
| P (penalty) | 10 - 100 | Constraint enforcement |

### Practical Tips

1. **Normalization**: Scale returns and covariance to similar magnitudes
2. **Positive Q**: Ensure Q matrix is suitable for minimization
3. **Problem size**: Keep variables ≤ 20 for current quantum hardware
4. **Hybrid approach**: Use classical pre-filtering for large problems

## References

- arxiv:2509.01496 - Higher-Order Portfolio Optimization with QAOA
- arxiv:2006.14510 - Quantum Computing for Finance
- arxiv:2504.08843 - End-to-End Portfolio Optimization