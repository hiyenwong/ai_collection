---
name: split-ensemble-qrc-training
category: quantum-finance
description: Split-ensemble training methodology for quantum reservoir computing that reorganizes measurement shot records to create more training examples without additional quantum hardware cost.
trigger_words: ["split-ensemble training", "quantum measurement records", "shot reorganization", "QRC training efficiency", "finite-shot noise", "quantum time series"]
---

# Split-Ensemble Training for Quantum Reservoir Computing

## Paper Reference
arXiv:2604.28160 — "Reorganizing Quantum Measurement Records Improves Time-Series Prediction"
Authors: Markus Baumann, Maximilian Zorn, Thomas Gabor, Claudia Linnhoff-Popien, Jonas Stein (2026-04-30)

## Core Methodology

### Problem
Standard QRC averages all shots from one labeled timestep into a single feature vector:
- Reduces finite-shot noise ✓
- But gives readout only ONE training example per timestep ✗
- With limited timesteps, readout is severely undertrained

### Solution: Split-Ensemble Training
1. Execute circuit with N shots per timestep (e.g., 512 shots)
2. **Split shots into K groups** (e.g., 512 → 8 groups × 64 shots each)
3. **Each group average** becomes a separate feature vector for the SAME target
4. Readout sees K× more training examples without additional circuit executions

### Key Insight
- Each group average is a **partially denoised** estimate of the true expectation value
- Groups are independent samples → readout learns from multiple noisy views
- Strongest gains observed on **real hardware** where noise is structured

## Implementation

```python
import numpy as np

def split_ensemble_features(shots_data, n_groups=8):
    """Split measurement shots into groups, return group averages"""
    # shots_data: (n_timesteps, n_shots, n_observables)
    n_timesteps, n_shots, n_obs = shots_data.shape
    group_size = n_shots // n_groups
    
    # Reshape: split shots into groups
    reshaped = shots_data[:, :n_groups * group_size, :].reshape(
        n_timesteps, n_groups, group_size, n_obs
    )
    
    # Average within each group
    group_averages = reshaped.mean(axis=2)  # (n_timesteps, n_groups, n_obs)
    
    # Flatten: each group becomes a separate training example
    X_split = group_averages.reshape(n_timesteps * n_groups, n_obs)
    y_split = np.repeat(y_targets, n_groups)  # Same target for all groups
    
    return X_split, y_split

# Usage
X_split, y_split = split_ensemble_features(measurement_data, n_groups=8)
readout.fit(X_split, y_split)
```

## When to Use

| Condition | Recommendation |
|-----------|---------------|
| Few training timesteps (< 100) | Use split-ensemble with K≥4 groups |
| Real hardware deployment | Strongest benefit — use K≥8 groups |
| Simulator with many timesteps (> 500) | Standard averaging sufficient |
| Very low shot count (< 64 per group) | May add too much noise — limit K |

## Pitfalls
1. **Groups must be independent** — don't reuse shots across groups
2. **Too many groups with too few shots** → excessive noise per group
3. **Not a substitute for more data** — only helps when the bottleneck is training sample count, not feature quality

## Related
- Combine with **post-training quantization** (quantum-reservoir-forecasting-resource-efficient) for deployment
- Combine with **distributed QRC** (arXiv:2605.04991) for scaling

## Activation
Keywords: split-ensemble training, quantum measurement records, shot reorganization, QRC training efficiency, finite-shot quantum ML, quantum time series training, measurement shot grouping, near-term quantum learning
