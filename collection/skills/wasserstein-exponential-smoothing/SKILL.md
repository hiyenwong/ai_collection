---
name: wasserstein-exponential-smoothing
description: "Wasserstein Exponential Smoothing methodology from arXiv:2606.05560 — extends classical exponential smoothing to distributional time series in Wasserstein space. Provides consistent parameter estimation via Wasserstein distance minimization, applicable to high-frequency financial returns, electricity demand, and any distribution-valued time series forecasting. Activation: wasserstein exponential smoothing, distributional time series, Wasserstein forecasting, distributional forecasting, 分布时间序列, Wasserstein 指数平滑."
---

## Context

Classical Exponential Smoothing (ES) is one of the most effective techniques for time series forecasting, consistently winning forecasting competitions. However, it operates on scalar observations in R. This paper (arXiv:2606.05560, June 2026) extends ES to **distributional time series** — where each observation is itself a probability distribution on R. The extension operates in the **Wasserstein space** and preserves the exceptional parsimony of classical ES (one smoothing parameter).

## Core Methodology

### 1. Wasserstein Space Generalization of ES

Classical ES: `s_t = α * y_t + (1-α) * s_{t-1}` (weighted average)

Wasserstein ES: `s_t = Exp_{s_{t-1}}(α * Log_{s_{t-1}}(y_t))`

Where:
- `y_t` is a probability distribution (not a scalar)
- `Exp` and `Log` are the exponential and logarithmic maps in Wasserstein space
- `α` is the smoothing parameter (same interpretation as classical ES)
- The weighted average becomes a **Wasserstein barycenter** (Fréchet mean)

### 2. Consistent Parameter Estimation

The smoothing parameter α can be **consistently estimated** by minimizing the Wasserstein distance between forecasts and observations:

```
α* = argmin_α Σ W_2²(Forecast_α(t), y_t)
```

Where W_2 is the 2-Wasserstein distance. This is a principled estimation procedure with theoretical guarantees.

### 3. Distributional Time Series Applications

Applicable when observations are distributions:
- **High-frequency financial returns**: Return distributions over rolling windows
- **Household electricity demand**: Demand distribution patterns
- **Any histogram-valued or quantile-valued time series**

## Implementation Steps

### Step 1: Convert Time Series to Distributional Format

```python
import numpy as np
from scipy.stats import gaussian_kde

def to_distribution(time_series, window_size=100):
    """Convert rolling windows to probability distributions."""
    distributions = []
    for i in range(len(time_series) - window_size + 1):
        window = time_series[i:i+window_size]
        kde = gaussian_kde(window)
        x_grid = np.linspace(window.min(), window.max(), 100)
        distributions.append((x_grid, kde(x_grid)))
    return distributions
```

### Step 2: Compute Wasserstein Distance Between Distributions

```python
from scipy.optimize import linear_sum_assignment
from scipy.stats import wasserstein_distance

def wasserstein_2d(x1, p1, x2, p2):
    """Compute W_2 distance between two 1D distributions."""
    # For 1D: W_2^2 = integral of (F1^{-1}(u) - F2^{-1}(u))^2 du
    # Using quantile functions
    cdf1 = np.cumsum(p1) / np.sum(p1)
    cdf2 = np.cumsum(p2) / np.sum(p2)
    
    # Interpolate inverse CDFs at common quantile levels
    u = np.linspace(0, 1, 100)
    q1 = np.interp(u, cdf1, x1)
    q2 = np.interp(u, cdf2, x2)
    
    return np.sqrt(np.mean((q1 - q2)**2))
```

### Step 3: Wasserstein Exponential Smoothing

```python
def wasserstein_es(distributions, alpha):
    """Apply Wasserstein exponential smoothing to distributional time series."""
    smoothed = [distributions[0]]
    for i in range(1, len(distributions)):
        # Wasserstein barycenter of two distributions
        x_curr, p_curr = distributions[i]
        x_prev, p_prev = smoothed[-1]
        
        # Quantile-based barycenter for 1D
        cdf_prev = np.cumsum(p_prev) / np.sum(p_prev)
        cdf_curr = np.cumsum(p_curr) / np.sum(p_curr)
        
        u = np.linspace(0.01, 0.99, 100)
        q_prev = np.interp(u, cdf_prev, x_prev)
        q_curr = np.interp(u, cdf_curr, x_curr)
        
        # Weighted quantile average (Wasserstein barycenter)
        q_smooth = alpha * q_curr + (1 - alpha) * q_prev
        
        # Convert back to distribution
        # (use KDE or parametric fit)
        smoothed.append((q_smooth, np.ones_like(q_smooth) / len(q_smooth)))
    
    return smoothed
```

### Step 4: Optimize Smoothing Parameter

```python
from scipy.optimize import minimize_scalar

def optimize_alpha(distributions):
    """Find optimal alpha by minimizing Wasserstein forecast error."""
    def loss(alpha):
        smoothed = wasserstein_es(distributions[:-1], alpha)
        total_w2 = 0
        for i in range(len(smoothed)):
            w2 = wasserstein_2d(*smoothed[i], *distributions[i+1])
            total_w2 += w2**2
        return total_w2
    
    result = minimize_scalar(loss, bounds=(0.01, 0.99), method='bounded')
    return result.x
```

## Pitfalls

- **1D Restriction (2026-06-07 verified)**: The Wasserstein ES methodology is developed for 1D distributions (distributions on R). Extension to multidimensional distributions requires computing Wasserstein barycenters in higher dimensions, which is computationally expensive (requires solving optimal transport). **Workaround**: For multidimensional data, apply ES marginally to each dimension or use PCA to reduce to 1D.
- **Consistent Estimation Requires Stationarity**: The consistency proof for α estimation assumes the distributional time series is stationary. For non-stationary series (trending, seasonal), the estimated α may not converge. **Fix**: Apply to differenced or seasonally-adjusted distributional series.
- **Window Size Trade-off**: Converting point observations to distributions requires a rolling window. Too small → noisy distributions; too large → smoothed over interesting dynamics. **Rule of thumb**: window_size ≈ sqrt(N) for N total observations.

## Verification

1. **α in (0, 1)**: Optimized smoothing parameter should be between 0 and 1
2. **Wasserstein Distance Decreases**: Compare W_2 error of Wasserstein ES vs. naive baseline
3. **Consistency Check**: Re-estimate α on held-out data; should be similar to training estimate
4. **Forecast Quality**: Compare distributional forecasts using Energy Score or CRPS

## Activation

wasserstein exponential smoothing, distributional time series, Wasserstein forecasting, distributional forecasting, 分布时间序列, Wasserstein 指数平滑, probability distribution forecasting, histogram time series, quantile forecasting, wasserstein barycenter