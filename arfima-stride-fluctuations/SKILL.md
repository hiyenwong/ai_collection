---
name: arfima-stride-fluctuations
description: "ARFIMA decomposition of stride-to-stride fluctuations in human walking for sensorimotor control analysis. Activation triggers: stride fluctuations, human gait, DFA, ARFIMA, fractal analysis, sensorimotor control"
---

# ARFIMA Decomposition of Stride-to-Stride Fluctuations

> Distinguishing true long-memory dynamics from short-memory processes in human gait using ARFIMA models, resolving the persistent/anti-persistent dichotomy under cueing conditions.

## Metadata
- **Source**: arXiv:2604.24365v1
- **Authors**: Philippe Terrier
- **Published**: 2026-04-27
- **Category**: q-bio.QM (Quantitative Methods)

## Core Methodology

### Problem Statement
Human walking exhibits **fractal correlations** in stride-to-stride fluctuations:
- **Self-paced gait**: Persistent correlations (positive long-range dependence)
- **Cued gait** (metronome/visual): Anti-persistent correlations (negative long-range dependence)

**Problem**: Detrended Fluctuation Analysis (DFA) cannot distinguish:
- True long-memory (fractional processes)
- Short-memory autoregressive moving-average (ARMA) processes

### Key Innovation
Use **ARFIMA (Autoregressive Fractionally Integrated Moving Average)** models to:
1. Distinguish short-memory (ARMA) from long-memory (fractional integration)
2. Identify the true correlation structure in stride fluctuations
3. Link findings to closed-loop sensorimotor control theory

### Background

#### DFA Limitations
DFA computes a scaling exponent α:
- α > 0.5: Persistent (long-range positive correlation)
- α = 0.5: Uncorrelated (random walk)
- α < 0.5: Anti-persistent (long-range negative correlation)

**BUT**: ARMA processes can produce the same α values without true long-memory.

#### ARFIMA Model
```
φ(B)(1 - B)^d y_t = θ(B)ε_t

Where:
- φ(B): AR polynomial
- (1 - B)^d: Fractional differencing (long-memory component)
- θ(B): MA polynomial
- d: Fractional integration parameter
```

**Interpretation of d**:
- d = 0: Short memory (ARMA)
- 0 < d < 0.5: Long memory, persistent
- -0.5 < d < 0: Long memory, anti-persistent

## Implementation Guide

### Prerequisites
- Python with `statsmodels`, `fracdiff`, or R with `forecast`
- Gait data: stride interval time series
- DFA implementation for comparison

### Step-by-Step

1. **Data Preparation**
```python
import numpy as np
import pandas as pd

def load_stride_data(file_path):
    """Load stride interval time series"""
    # Stride interval = time between consecutive foot strikes
    data = pd.read_csv(file_path)
    stride_intervals = data['stride_time'].values
    return stride_intervals

def detrend(stride_intervals):
    """Remove linear trend"""
    x = np.arange(len(stride_intervals))
    slope, intercept = np.polyfit(x, stride_intervals, 1)
    detrended = stride_intervals - (slope * x + intercept)
    return detrended
```

2. **DFA for Comparison**
```python
def dfa(stride_intervals, scales=None):
    """
    Detrended Fluctuation Analysis
    Returns: scaling exponent α
    """
    if scales is None:
        scales = np.unique(np.logspace(np.log10(4), 
                                       np.log10(len(stride_intervals)//4), 
                                       20).astype(int))
    
    fluctuations = []
    
    for scale in scales:
        # Divide into windows
        n_windows = len(stride_intervals) // scale
        
        F = 0
        for i in range(n_windows):
            window = stride_intervals[i*scale:(i+1)*scale]
            # Fit and detrend
            x = np.arange(scale)
            slope, intercept = np.polyfit(x, window, 1)
            trend = slope * x + intercept
            # Compute RMS fluctuation
            F += np.mean((window - trend)**2)
        
        fluctuations.append(np.sqrt(F / n_windows))
    
    # Fit power law
    log_scales = np.log(scales)
    log_fluct = np.log(fluctuations)
    alpha, _ = np.polyfit(log_scales, log_fluct, 1)
    
    return alpha, scales, fluctuations
```

3. **ARFIMA Model Fitting**
```python
try:
    from fracdiff import fdiff, fdiff_coef
    from statsmodels.tsa.arima.model import ARIMA
except ImportError:
    print("Install with: pip install fracdiff statsmodels")

def estimate_arfima(stride_intervals, max_p=2, max_q=2):
    """
    Fit ARFIMA(p,d,q) model
    Returns: d (fractional integration parameter), AIC
    """
    from scipy.optimize import minimize
    
    def arfima_likelihood(d, y, p=1, q=1):
        """Compute ARIMA likelihood with fractional d"""
        try:
            # Fractional difference the data
            y_diff = fdiff(y, d, axis=0)
            
            # Fit ARMA to differenced data
            model = ARIMA(y_diff, order=(p, 0, q))
            result = model.fit(method='css-mle', disp=False)
            return result.aic
        except:
            return np.inf
    
    # Grid search for d
    d_range = np.linspace(-0.5, 0.5, 50)
    aics = []
    
    for d in d_range:
        aic = arfima_likelihood(d, stride_intervals)
        aics.append(aic)
    
    best_idx = np.argmin(aics)
    d_estimate = d_range[best_idx]
    
    return d_estimate, aics[best_idx]

# Simpler approach using Hurst exponent
from scipy.stats import linregress

def hurst_exponent(ts):
    """
    R/S analysis for Hurst exponent
    H > 0.5: Persistent
    H = 0.5: Random
    H < 0.5: Anti-persistent
    """
    lags = range(2, 100)
    tau = [np.std(np.subtract(ts[lag:], ts[:-lag])) for lag in lags]
    
    reg = linregress(np.log(lags), np.log(tau))
    H = reg.slope
    
    return H
```

4. **Interpretation Framework**
```python
def interpret_correlation(d, H):
    """
    Interpret correlation structure
    """
    results = {
        'd': d,
        'H': H,
        'memory_type': None,
        'persistence': None
    }
    
    # Memory type
    if abs(d) < 0.1:
        results['memory_type'] = 'short_memory (ARMA)'
    else:
        results['memory_type'] = 'long_memory (ARFIMA)'
    
    # Persistence
    if H > 0.55:
        results['persistence'] = 'persistent'
    elif H < 0.45:
        results['persistence'] = 'anti_persistent'
    else:
        results['persistence'] = 'uncorrelated'
    
    return results

def compare_conditions(self_paced_d, cued_d, self_paced_H, cued_H):
    """
    Compare self-paced vs cued gait
    """
    print("=== Condition Comparison ===")
    print(f"\nSelf-paced gait:")
    print(f"  d = {self_paced_d:.3f}")
    print(f"  H = {self_paced_H:.3f}")
    print(f"  Interpretation: {interpret_correlation(self_paced_d, self_paced_H)}")
    
    print(f"\nCued gait:")
    print(f"  d = {cued_d:.3f}")
    print(f"  H = {cued_H:.3f}")
    print(f"  Interpretation: {interpret_correlation(cued_d, cued_H)}")
    
    print(f"\nKey finding: Cuing shifts from persistent to anti-persistent fluctuations")
    print(f"This suggests stronger negative feedback in closed-loop control")
```

## Theoretical Interpretation

### Sensorimotor Control Perspective
- **Self-paced**: Weak feedback → persistent drift → d > 0
- **Cued**: Strong external feedback → error correction → d < 0

### Closed-Loop Control Model
```
Error(t) = Reference(t) - Feedback(t)
Correction(t) = Controller(Error(t))
Next Stride = Previous Stride + Correction(t) + Noise
```

Under cued conditions, the controller gain increases, producing anti-persistent fluctuations (overshoot correction).

## Applications
- **Clinical gait analysis**: Detect impaired sensorimotor control
- **Aging studies**: Monitor changes in gait stability
- **Rehabilitation**: Assess intervention effectiveness
- **Falls risk**: Predict falls from fluctuation patterns

## Pitfalls
- **Data length**: ARFIMA requires long time series (>500 strides)
- **Stationarity**: Gait must be steady-state
- **Discretization**: Stride detection errors affect results
- **Individual differences**: Large inter-subject variability

## Related Skills
- biomechanical-signal-analysis
- fractal-analysis-biological
- gait-dynamics-neurological
- dfa-long-range-correlations

## References
- arXiv:2604.24365v1
- Beran, "Statistics for Long-Memory Processes" (1994)
- Hausdorff et al., "Fractal dynamics of human gait" (1996)
