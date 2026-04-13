---
name: neural-population-decoding
description: "Methods for decoding neural population activity and analyzing latent dynamics. Covers dimensionality reduction, manifold analysis, and decoding algorithms. Activation: neural decoding, population coding, manifold, latent dynamics, dimensionality reduction."
---

# Neural Population Decoding and Encoding

## Overview

Neural population decoding extracts information from collective activity of neuron ensembles. This skill covers dimensionality reduction, manifold identification, and decoding algorithms.

## Key Concepts

### Population Coding

Information distributed across many neurons:
- **Rate coding**: Information in firing rates
- **Temporal coding**: Information in spike timing

### Dimensionality Reduction

High-dimensional neural activity lives on low-dimensional manifolds.

## Methodology

### Preprocessing

```python
import numpy as np
from scipy.stats import zscore

def preprocess_spikes(spike_times, bin_size=0.02):
    """Preprocess spike data for population analysis."""
    all_spikes = np.concatenate(spike_times)
    t_min, t_max = all_spikes.min(), all_spikes.max()
    
    bins = np.arange(t_min, t_max + bin_size, bin_size)
    n_neurons = len(spike_times)
    n_bins = len(bins) - 1
    rates = np.zeros((n_bins, n_neurons))
    
    for i, spikes in enumerate(spike_times):
        counts, _ = np.histogram(spikes, bins=bins)
        rates[:, i] = counts / bin_size
    
    rates = zscore(rates, axis=0, nan_policy='omit')
    return rates
```

### PCA

```python
from sklearn.decomposition import PCA

def apply_pca(rates, n_components=10):
    """Apply PCA to neural population activity."""
    pca = PCA(n_components=n_components)
    projected = pca.fit_transform(rates)
    return pca, projected, pca.explained_variance_ratio_
```

### Kalman Filter Decoder

```python
class KalmanFilterDecoder:
    """Kalman filter for neural decoding."""
    
    def __init__(self):
        self.A = None
        self.C = None
    
    def fit(self, rates, kinematics):
        """Fit Kalman filter parameters."""
        self.C = np.linalg.lstsq(kinematics, rates, rcond=None)[0].T
        x_prev = kinematics[:-1]
        x_next = kinematics[1:]
        self.A = np.linalg.lstsq(x_prev, x_next, rcond=None)[0]
    
    def decode(self, rates):
        """Decode kinematics using Kalman filtering."""
        n_time = rates.shape[0]
        n_dims = self.A.shape[0]
        states = np.zeros((n_time, n_dims))
        
        for t in range(1, n_time):
            x_pred = self.A @ states[t-1]
            K = np.linalg.solve(self.C @ self.C.T, self.C)
            states[t] = x_pred + K @ (rates[t] - self.C @ x_pred)
        
        return states
```

## References

- Cunningham, J. P., & Yu, B. M. (2014). Dimensionality reduction for large-scale neural recordings. *Nature Neuroscience*, 17(11), 1500-1509.
- Gallego, J. A., et al. (2017). Neural manifolds for the control of movement. *Neuron*, 94(5), 978-984.

## Activation Keywords

- neural decoding
- population coding
- manifold
- latent dynamics
- dimensionality reduction


## Instructions for Agents

使用此技能时遵循以下流程：

1. **理解问题**：分析输入需求和约束条件
2. **选择方法**：根据场景选择合适的技术方案
3. **执行操作**：按照方法论实施具体步骤
4. **验证结果**：检查结果是否符合预期

## Examples

### Example 1: Basic Usage

**User:** 请帮我应用此技能

**Agent:** 我将按照标准流程执行...

### Example 2: Advanced Usage

**User:** 有更复杂的场景需要处理

**Agent:** 针对复杂场景，我将采用以下策略...

## Tools Used

- `exec`
- `read`
- `write`
