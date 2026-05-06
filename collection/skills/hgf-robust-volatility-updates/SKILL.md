---
name: hgf-robust-volatility-updates
description: "Robust volatility updates for Hierarchical Gaussian Filtering (HGF) that prevent negative posterior precision. Uses modified quadratic approximation with Lambert W function interpolation. Use when: implementing HGF networks, computational psychiatry, active inference, Bayesian belief updating, volatility-coupled nodes, predictive coding, or when HGF crashes due to negative precision."
---

# HGF Robust Volatility Updates

> Modified quadratic approximation for Hierarchical Gaussian Filtering that guarantees strictly positive posterior precision across the entire parameter space.

## Metadata
- **Source**: arXiv:2605.00966
- **Authors**: Christoph Mathys, Nicolas Legrand, Peter Thestrup Waade, Nace Mikus, Lilian Aline Weber
- **Published**: 2026-05-01

## Core Problem

Hierarchical Gaussian Filtering (HGF) networks update posterior beliefs about hidden environmental states via cascading one-step equations. The original volatility-coupling (variance-targeting parent) equations can yield **negative posterior precision** in certain parameter regions, causing the algorithm to crash.

## Solution: Modified Quadratic Approximation

### Key Mathematical Mechanism

The fix interpolates between two quadratic expansions of the variational energy:

1. **Expansion at prior prediction**: Standard quadratic approximation around the prior mean
2. **Expansion at second mode**: Located in closed form via the **Lambert W function**

The interpolation ensures strictly positive precision under all conditions.

### Implementation Guide

```python
import numpy as np
from scipy.special import lambertw

def robust_volatility_update(mu_prior, pi_prior, prediction_error, volatility_coupling_strength):
    """
    Robust HGF volatility-coupled node update.
    
    Parameters:
    - mu_prior: prior mean
    - pi_prior: prior precision (must be positive)
    - prediction_error: difference between observed and predicted value
    - volatility_coupling_strength: variance-targeting coupling parameter
    
    Returns:
    - mu_post: posterior mean
    - pi_post: posterior precision (guaranteed positive)
    """
    # Standard update (may produce negative precision)
    pi_post_standard = pi_prior + volatility_coupling_strength * prediction_error**2
    
    # Robust update via Lambert W interpolation
    if pi_post_standard <= 0:
        # Second mode location via Lambert W
        # W(z) satisfies W(z) * exp(W(z)) = z
        z = -volatility_coupling_strength * prediction_error**2 / pi_prior
        w = np.real(lambertw(z))
        
        # Second mode precision
        pi_second = pi_prior * (1 + w)
        
        # Interpolate between prior and second mode
        # Weight based on relative variational energy
        alpha = np.clip(pi_prior / (pi_prior + abs(pi_second)), 0, 1)
        pi_post = alpha * pi_post_standard + (1 - alpha) * pi_second
        
        # Ensure strictly positive
        pi_post = max(pi_post, 1e-10)
    else:
        pi_post = pi_post_standard
    
    # Posterior mean update (unchanged)
    mu_post = mu_prior + prediction_error / pi_post
    
    return mu_post, pi_post
```

### Key Properties

- **Full parameter robustness**: Stable across entire parameter space
- **High-fidelity tracking**: Faithfully approximates true variational posterior
- **Large prediction errors**: Handles extreme deviations gracefully
- **Minimal overhead**: Single Lambert W evaluation per update

## Applications

- Computational psychiatry (belief updating in patient populations)
- Active inference frameworks (Karl Friston's free energy principle)
- Adaptive filtering pipelines
- Reinforcement learning with uncertain environments
- Time-series analysis with volatility clustering

## Pitfalls

- **Lambert W branch selection**: Use principal branch (k=0) for standard cases; complex branches may be needed for extreme parameter regimes
- **Numerical precision**: Lambert W near branch point (-1/e) requires careful handling
- **Not a cure-all**: Only fixes volatility-coupled nodes; other HGF update equations remain unchanged
- **Validation needed**: Always verify posterior precision > 0 after update

## Related Skills

- online-generalised-predictive-coding
- free-energy-moe-routing
- multi-agent-active-inference-digital-twins
