---
name: neural-encoding-evaluation-ground-truth
description: Ground-truth approximation framework for evaluating neural encoding models without held-out data. Uses split-time-point and noise-ceiling methods to provide reliable goodness-of-fit estimates when data is limited. Applicable to MEEG, fMRI, and neural recording analysis. Trigger words: neural encoding, evaluation, ground-truth, encoding model, MEEG, fMRI, noise ceiling, split-time, goodness-of-fit
version: 1.0.0
metadata:
  hermes:
    source_paper: "Ground-truth approximation for evaluating neural encoding models (arXiv:2512.19201v1)"
    date: "2025-12-22"
    tags: [neuroscience, encoding-models, evaluation, methodology]
---

# Ground-Truth Approximation for Neural Encoding Evaluation

## Overview
Framework for evaluating neural encoding models (mapping stimuli to neural responses) without requiring held-out data. Provides reliable goodness-of-fit estimates when data collection is limited or expensive.

## Core Methods

### Split-Time-Point Evaluation
Split recording time into odd/even samples, train on one, test on other. Correlate predictions to get unbiased estimate.

### Noise Ceiling Estimation
Upper bound on achievable prediction accuracy given neural noise. Compute by correlating trial-averaged responses across repetitions.

### Implementation
```python
import numpy as np
from sklearn.linear_model import Ridge

def split_timepoint_eval(X, y, alpha=1.0):
    '''Split-time-point evaluation for neural encoding.'''
    odd_mask = np.arange(len(y)) % 2 == 0
    even_mask = ~odd_mask
    
    model = Ridge(alpha=alpha)
    model.fit(X[odd_mask], y[odd_mask])
    y_pred = model.predict(X[even_mask])
    
    from scipy.stats import pearsonr
    r, _ = pearsonr(y[even_mask], y_pred)
    return r

def noise_ceiling(trial_data):
    '''Estimate noise ceiling from trial repetitions.'''
    # trial_data: shape (n_trials, n_timepoints)
    means = trial_data.mean(axis=0)
    # Cross-validate across trials
    r_vals = []
    for i in range(len(trial_data)):
        others = np.delete(trial_data, i, axis=0).mean(axis=0)
        from scipy.stats import pearsonr
        r, _ = pearsonr(trial_data[i], others)
        r_vals.append(r)
    return np.mean(r_vals)
```

## References
- Ground-truth approximation for evaluating neural encoding models (arXiv:2512.19201v1)
