---
name: ak-mcs-conformal-failure-probability
description: "Active Kriging Monte Carlo Simulation with conformal certification for failure probability estimation in structural reliability. Uses adaptive cross-conformal strategy for small-sample settings with J+GP conformal estimator. Provides distribution-free guarantees on prediction errors for improved classification near limit-state surfaces. arXiv:2606.20191. Activates: failure probability, structural reliability, active learning, kriging monte carlo, conformal prediction, AK-MCS, J+GP estimator, rare event estimation."
metadata:
  arxiv_id: "2606.20191"
  published: "2026-06-18"
  authors: "Edgar Jaber, Vincent Chabridon, Mathilde Mougeot"
  tags: ["statistics", "machine-learning", "reliability", "conformal", "kriging", "monte-carlo"]
---

## Context

AK-MCS-C2 integrates Active Kriging Monte Carlo Simulation (AK-MCS) with conformal prediction for failure probability estimation in structural reliability analysis. Unlike standard AK-MCS, it provides distribution-free guarantees on prediction errors.

## Core Methodology

1. **Build kriging surrogate** (Gaussian Process) of the limit-state function
2. **Apply J+GP conformal estimator** for distribution-free prediction intervals
3. **Adaptive cross-conformal strategy** specifically designed for small-sample settings
4. **Active learning loop**: select most informative samples near limit-state surface
5. **Improved uncertainty quantification** → more reliable classification of boundary samples
6. **Failure probability estimation** with certified error bounds

## Key Results

- Distribution-free guarantees on prediction errors (no assumptions on GP residuals)
- Enhanced accuracy and robustness for rare-event regimes
- Validated on well-established benchmarks with reproducible results

## Implementation Steps

```python
from sklearn.gaussian_process import GaussianProcessRegressor
import numpy as np

def ak_mcs_c2(limit_state_fn, n_mc=10000, n_init=10, alpha=0.05):
    """AK-MCS with conformal certification for failure probability."""
    # Initialize with small design of experiments
    X_train = lhs_sample(n_init, dim)
    y_train = limit_state_fn(X_train)
    
    # Fit GP surrogate
    gp = GaussianProcessRegressor().fit(X_train, y_train)
    
    # Conformal calibration (J+GP estimator)
    residuals = np.abs(y_train - gp.predict(X_train))
    conformal_quantile = np.quantile(residuals, 1 - alpha)
    
    # Active learning: enrich near limit-state
    for _ in range(max_iterations):
        X_mc = np.random.randn(n_mc, dim)
        mu, sigma = gp.predict(X_mc, return_std=True)
        
        # Uncertainty near boundary
        U = (np.abs(mu) + conformal_quantile + sigma) 
        x_new = X_mc[np.argmin(U)]
        
        # Evaluate and update
        y_new = limit_state_fn(x_new.reshape(1, -1))
        X_train = np.vstack([X_train, x_new.reshape(1, -1)])
        y_train = np.concatenate([y_train, y_new])
        gp.fit(X_train, y_train)
    
    # Estimate failure probability with conformal bounds
    pf = np.mean(gp.predict(X_mc) < 0)
    return pf, conformal_quantile
```

## Pitfalls

- **Small-sample conformal**: standard conformal requires large calibration sets; J+GP estimator addresses this
- **GP kernel selection**: Matérn 5/2 recommended for engineering limit-state functions
- **Cross-conformal split**: ensure balanced splits to avoid calibration bias
- **Rare events**: may require importance sampling augmentation for very low failure probabilities (< 1e-6)

## Verification

- Compare with standard AK-MCS on benchmark (e.g., 4D cantilever beam) → should achieve similar accuracy with certified bounds
- Verify conformal coverage: fraction of true values within prediction intervals ≥ 1 - α
- Test on rare-event regime (Pf < 1e-4) → verify robustness

## Activation

failure probability, structural reliability, active learning, kriging monte carlo, conformal prediction, AK-MCS, J+GP estimator, rare event estimation, distribution-free guarantees, Edgar Jaber
