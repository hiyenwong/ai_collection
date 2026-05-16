---
name: tensor-network-option-pricing
description: "Singularity Tensor Network (STN-GPR) framework for efficient option pricing from arXiv:2603.26318. Tensor-network surrogate targeting large-scale portfolio revaluation for market risk management (VaR, Expected Shortfall)."
---

# Tensor Network Option Pricing (STN-GPR)

## Description

Tensor-network surrogate methodology for efficient option pricing, targeting large-scale portfolio revaluation in market risk management. Uses Singularity Tensor Networks (STN) with Gaussian Process Regression (GPR) to represent high-dimensional price dynamics and compute VaR/Expected Shortfall efficiently. Based on arXiv:2603.26318.

## Activation Keywords
- tensor network option pricing
- STN-GPR
- portfolio revaluation
- VaR tensor network
- quantum option pricing
- 张量网络期权定价
- expected shortfall tensor

## Tools Used
- exec: Run tensor network computations (TensorNetwork, ITensor)
- read: Load market data and option portfolios
- write: Save pricing models and risk metrics

## Core Methodology

### Problem: Portfolio Revaluation

Market risk management (VaR, Expected Shortfall) requires revaluing large portfolios across many market scenarios:

1. **High-dimensional**: Portfolio depends on many underlying assets/factors
2. **Non-linear**: Option payoffs are non-linear functions of asset prices
3. **Computationally expensive**: Full Monte Carlo simulation takes hours

### STN-GPR Solution

1. **Tensor Network Representation**: Represent the pricing function as a low-rank tensor network
   - Each asset dimension becomes a tensor index
   - Cross-asset correlations captured via tensor contractions
   - Exponential state space compressed to polynomial parameters

2. **Gaussian Process Regression**: Use GPR to interpolate the pricing function
   - Training data from sparse Monte Carlo simulations
   - GP provides uncertainty estimates
   - Active learning selects most informative training points

3. **Singularity Handling**: Special treatment for discontinuities
   - Option payoffs have kinks at strike prices
   - STN adaptively refines near singularities
   - GPR kernel designed for non-smooth functions

### Algorithm Steps

```
1. Generate sparse training data via Monte Carlo (N ~ 10^3-10^4 points)
2. Fit tensor network to training data (low-rank decomposition)
3. Train GPR on residuals (captures what TN misses)
4. Evaluate combined model on risk scenarios (M ~ 10^6 points)
5. Compute VaR/ES from revalued portfolio distribution
```

### Complexity Advantage

| Method | Complexity | Accuracy |
|--------|-----------|----------|
| Full Monte Carlo | O(M × N_assets) | High |
| STN-GPR | O(M × poly(d, r)) | High |
| Linear approximation | O(M × N_assets) | Low (non-linear missing) |

Where d = tensor dimension, r = tensor rank, M = scenario count.

## Key Findings

1. **STN-GPR** achieves Monte Carlo-level accuracy with 100x fewer evaluations
2. **Tensor networks** efficiently capture cross-asset correlations in high dimensions
3. **GPR residuals** handle pricing function irregularities that TN alone cannot
4. **Scalable to portfolios** with 50+ assets where full Monte Carlo is prohibitive

## Implementation Pattern

```python
# Simplified STN-GPR for option pricing
import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor

def stn_gpr_pricing(strike, spot, vol, rate, expiry, scenarios):
    """Price options across scenarios using STN-GPR surrogate."""
    
    # Step 1: Sparse training data
    n_train = 1000
    train_points = generate_sparse_scenarios(n_train)
    train_prices = black_scholes_batch(train_points)
    
    # Step 2: Tensor network fit (low-rank CP decomposition)
    tn_model = fit_tensor_network(train_points, train_prices, rank=10)
    
    # Step 3: GPR on residuals
    tn_preds = tn_model.predict(train_points)
    residuals = train_prices - tn_preds
    gpr = GaussianProcessRegressor().fit(train_points, residuals)
    
    # Step 4: Evaluate on risk scenarios
    tn_scenario = tn_model.predict(scenarios)
    gpr_scenario = gpr.predict(scenarios)
    prices = tn_scenario + gpr_scenario
    
    # Step 5: Compute risk metrics
    var_95 = np.percentile(prices, 5)
    es_95 = np.mean(prices[prices <= var_95])
    
    return prices, var_95, es_95
```

## When to Use

- **Large-scale portfolio revaluation** (1000s of options)
- **Market risk management** (VaR, Expected Shortfall computation)
- **High-dimensional** pricing problems (multi-asset options)
- **Real-time risk** where Monte Carlo is too slow
- **Stress testing** requiring many scenario evaluations

## Error Handling

- **Tensor rank selection**: Too low → approximation error; too high → overfitting. Use cross-validation.
- **GPR scalability**: Standard GPR is O(N^3); use sparse GPR or inducing points for N > 10^4
- **Singularity detection**: Automatic detection of payoff discontinuities needed for STN refinement
- **Extrapolation risk**: TN-GPR accurate within training domain; warn when scenarios go out-of-sample

## Resources
- arXiv: 2603.26318 - "STN-GPR: A Singularity Tensor Network Framework for Efficient Option Pricing"
- Dominic Gribben, Carolina Allende, Alba Villarino, Aser Cortines, Mazen Ali
