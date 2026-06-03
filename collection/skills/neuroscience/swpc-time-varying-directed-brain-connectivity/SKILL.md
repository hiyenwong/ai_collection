---
name: swpc-time-varying-directed-brain-connectivity
description: "Sliding-Window Prediction Correlation (SWpC) for time-varying directed functional connectivity in brain networks. Embeds directional LTI model within sliding windows to estimate directed information flow. Validated on concurrent LFP-fMRI, HCP task fMRI, and clinical vestibular dysfunction. Activation: directed connectivity, time-varying FC, sliding window, information flow, dynamic brain connectivity."
---

# Time-Varying Directed Interactions via Sliding-Window Prediction Correlation (SWpC)

> SWpC introduces a directional LTI model within sliding windows to estimate time-varying directed functional connectivity, yielding both strength and duration measures of information transfer.

## Metadata
- **Source**: arXiv:2602.16004
- **Authors**: Nan Xu, Xiaodi Zhang, Wen-Ju Pan, Jeremy L. Smith, Eric H. Schumacher, Jason W. Allen, Vince D. Calhoun, Shella D. Keilholz
- **Published**: 2026-02-17
- **Category**: q-bio.NC

## Core Methodology

### Key Innovation
Sliding-Window Prediction Correlation (SWpC) extends traditional SWC by embedding a **directional linear time-invariant (LTI) model** within each window:
- **Prediction Correlation (strength)**: How well past of region X predicts present of region Y
- **Duration Measure**: How long directed information transfer persists within each window
- These two complementary descriptors capture both the magnitude and temporal persistence of directed interactions

### Technical Framework

1. **LTI Model**: For each window, fit X(t) = Σ a_k·Y(t-k) + noise, where the prediction correlation R²(X|Y) measures directed influence Y→X

2. **Sliding Window**: Apply LTI model within overlapping temporal windows (typical: 30-60s for fMRI, shorter for electrophysiology)

3. **Directionality**: Unlike correlation, the prediction model is asymmetric — R²(X|Y) ≠ R²(Y|X)

4. **Statistical Validation**: Permutation testing to assess significance of directed connections

### Validation Results
- **Concurrent LFP-fMRI**: Stable directionality in both band-limited LFP power and BOLD
- **HCP Motor Task**: Detects task-evoked directed FC changes with higher sensitivity than SWC
- **Clinical (PCVD)**: Reveals vestibular-multisensory brain-state shifts, improves patient discrimination

## Implementation Guide

### Prerequisites
- Time-series neuroimaging data (fMRI BOLD, EEG, LFP, MEG)
- Python: numpy, scipy, sklearn, nilearn

### Step-by-Step
1. **Preprocessing**: Standard neuroimaging preprocessing (motion correction, filtering, parcellation)
2. **Window specification**: Choose window length and step size
3. **LTI fitting**: For each window and region pair, fit autoregressive prediction model
4. **Prediction correlation**: Compute R² of prediction for both directions (X→Y, Y→X)
5. **Duration estimation**: Track persistence of significant directed connections across windows
6. **Statistical testing**: Permutation-based significance assessment

### Code Example
```python
import numpy as np
from sklearn.linear_model import LinearRegression
from scipy.stats import pearsonr

def swpc(time_series_x, time_series_y, window_size=30, step=1, max_lag=5):
    # Sliding-Window Prediction Correlation for directed connectivity.
    # Returns prediction correlation for Y->X (how well Y predicts X).
    n_timepoints = len(time_series_x)
    n_windows = (n_timepoints - window_size) // step + 1
    strength = []
    duration = 0
    
    for w in range(n_windows):
        start = w * step
        end = start + window_size
        x = time_series_x[start:end]
        y = time_series_y[start:end]
        
        # Build lagged prediction matrix: predict x(t) from y(t-1),...,y(t-max_lag)
        X_pred = np.column_stack([y[max_lag-l:window_size-l] for l in range(max_lag)])
        y_target = x[max_lag:]
        
        if len(y_target) < max_lag + 2:
            continue
        reg = LinearRegression().fit(X_pred, y_target)
        predicted = reg.predict(X_pred)
        r, _ = pearsonr(y_target, predicted)
        strength.append(r ** 2)
        if r ** 2 > 0.1:
            duration += 1
    
    return {
        'mean_strength': np.mean(strength),
        'strength_timeseries': strength,
        'duration': duration / n_windows
    }

# Usage: directed connectivity matrix
n_regions = 50
directed_fc = np.zeros((n_regions, n_regions))
for i in range(n_regions):
    for j in range(n_regions):
        if i != j:
            result = swpc(data[i], data[j])
            directed_fc[i, j] = result['mean_strength']
```

## Applications
- **Dynamic directed connectivity**: Track information flow direction in real-time
- **Task-evoked connectivity**: Detect directional changes during cognitive tasks
- **Clinical biomarkers**: Improved patient-group discrimination in vestibular dysfunction
- **Multimodal validation**: Works across fMRI, LFP, and EEG modalities
- **Network neuroscience**: Identify directed communication pathways in brain networks

## Pitfalls
- Window size choice affects temporal resolution vs. estimation reliability tradeoff
- LTI assumption may not hold for strongly nonlinear neural interactions
- Autoregressive order (max_lag) needs careful selection via AIC/BIC
- Higher computational cost than simple SWC (O(n_regions²) model fittings per window)

## Related Skills
- time-varying-brain-connectivity
- brain-network-controllability
- task-aware-brain-connectivity
- dynamic-functional-connectivity-integration-segregation
