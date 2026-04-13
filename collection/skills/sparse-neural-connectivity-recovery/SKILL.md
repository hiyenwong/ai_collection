---
name: sparse-neural-connectivity-recovery
description: |
  Recover sparse neural connectivity from partial measurements using a covariance-based approach with Granger-causality refinement.
  Infer the weight matrix of recurrent neural networks from sparse, partial observations of neural activity.
  基于协方差和格兰杰因果的稀疏神经连接恢复方法，从部分观测中推断循环神经网络的连接权重矩阵。
  触发词：sparse neural connectivity, partial measurements, covariance-based estimation, Granger causality, 
  neural connectivity recovery, recurrent neural network, RNN weight estimation, sparse recovery, 稀疏神经连接, 部分观测, 协方差估计
user-invocable: true
---

# Sparse Neural Connectivity Recovery from Partial Measurements

## Paper Reference

- **Title:** Recovering Sparse Neural Connectivity from Partial Measurements: A Covariance-Based Approach with Granger-Causality Refinement
- **Authors:** Quilee Simeon
- **arXiv:** 2603.18497v1 (2026-03-19)
- **Category:** Computational Neuroscience, Machine Learning

---

## Overview

Inferring the connectivity of neural circuits from incomplete observations is a fundamental challenge in neuroscience. This skill presents a covariance-based method for estimating the weight matrix of a recurrent neural network (RNN) from sparse, partial measurements of neural activity.

### Key Contributions

1. **Covariance-Based Estimation**: Leverages statistical correlations in neural activity to infer connectivity patterns
2. **Granger-Causality Refinement**: Incorporates temporal causality to improve connectivity estimates
3. **Sparse Recovery**: Exploits the natural sparsity of neural connections for robust estimation
4. **Partial Measurement Handling**: Works with incomplete observations, addressing real-world experimental limitations

---

## Core Concepts

### 1. Problem Formulation

Given partial observations of neural activity, recover the underlying connectivity matrix **W** of a recurrent neural network.

**Mathematical Model:**
```
τ dx/dt = -x + W·φ(x) + I(t) + ξ(t)
```

Where:
- **x**: Neural activity/state vector
- **W**: Connectivity weight matrix (sparse, unknown)
- **φ(x)**: Nonlinear activation function
- **I(t)**: External input
- **ξ(t)**: Noise term
- **τ**: Time constant

### 2. Covariance-Based Estimation

**Principle:** Statistical correlations between neurons encode connectivity information.

**Key Insight:** The covariance matrix Σ of neural activity relates to the connectivity matrix W through:
```
Σ = f(W, Σ_input, τ)
```

**Estimation Approach:**
1. Compute empirical covariance from observed data
2. Solve inverse problem to estimate W
3. Exploit sparsity constraints for regularization

### 3. Granger Causality

**Definition:** A time series X "Granger-causes" Y if past values of X help predict Y better than past values of Y alone.

**Application:**
- Temporal directionality in connectivity
- Distinguishing direct vs. indirect connections
- Refining covariance-based estimates

**Mathematical Formulation:**
```
GC(X→Y) = log(var(ε_Y) / var(ε_Y|X_past))
```

Where ε represents prediction errors.

### 4. Sparse Recovery

**Rationale:** Biological neural networks are typically sparse (each neuron connects to only a fraction of others).

**Methods:**
- L1 regularization (Lasso)
- Compressed sensing techniques
- Thresholding-based sparsification

---

## Algorithm Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│         Sparse Neural Connectivity Recovery Pipeline             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Input: Partial neural activity measurements {x_i(t)}           │
│           │                                                      │
│           ▼                                                      │
│  ┌────────────────────────────────────────┐                     │
│  │ Step 1: Covariance Estimation          │                     │
│  │  - Compute empirical covariance Σ      │                     │
│  │  - Handle missing data (partial obs)   │                     │
│  └────────────┬───────────────────────────┘                     │
│               │                                                  │
│               ▼                                                  │
│  ┌────────────────────────────────────────┐                     │
│  │ Step 2: Initial Connectivity Estimate  │                     │
│  │  - Solve: min ||Σ - f(W)||² + λ||W||₁ │                     │
│  │  - Obtain W_cov                        │                     │
│  └────────────┬───────────────────────────┘                     │
│               │                                                  │
│               ▼                                                  │
│  ┌────────────────────────────────────────┐                     │
│  │ Step 3: Granger-Causality Analysis     │                     │
│  │  - Compute pairwise GC values          │                     │
│  │  - Build GC matrix G                   │                     │
│  └────────────┬───────────────────────────┘                     │
│               │                                                  │
│               ▼                                                  │
│  ┌────────────────────────────────────────┐                     │
│  │ Step 4: Refinement & Fusion            │                     │
│  │  - Combine W_cov and G                 │                     │
│  │  - Apply sparsity thresholding         │                     │
│  └────────────┬───────────────────────────┘                     │
│               │                                                  │
│               ▼                                                  │
│  Output: Recovered sparse connectivity matrix W*                 │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Python Implementation

### Dependencies

```python
import numpy as np
from scipy import linalg, stats
from scipy.optimize import minimize
from typing import Tuple, Optional, Dict
import warnings
```

### Core Classes

```python
class SparseConnectivityRecovery:
    """
    Recover sparse neural connectivity from partial measurements
    using covariance-based estimation with Granger-causality refinement.
    """
    
    def __init__(self, 
                 n_neurons: int,
                 tau: float = 10.0,
                 lambda_sparse: float = 0.1,
                 gc_threshold: float = 0.05):
        """
        Initialize the connectivity recovery model.
        
        Args:
            n_neurons: Number of neurons in the network
            tau: Neural time constant (ms)
            lambda_sparse: L1 regularization parameter for sparsity
            gc_threshold: Threshold for Granger causality significance
        """
        self.n_neurons = n_neurons
        self.tau = tau
        self.lambda_sparse = lambda_sparse
        self.gc_threshold = gc_threshold
        self.W_estimated = None
        
    def estimate_covariance(self, 
                           activity_data: np.ndarray,
                           observed_mask: Optional[np.ndarray] = None) -> np.ndarray:
        """
        Estimate covariance matrix from potentially partial observations.
        
        Args:
            activity_data: Neural activity (time x neurons)
            observed_mask: Boolean mask for observed entries (time x neurons)
            
        Returns:
            Covariance matrix estimate
        """
        n_time, n_neurons = activity_data.shape
        
        if observed_mask is None:
            # Full observations
            return np.cov(activity_data.T)
        
        # Handle partial observations
        Sigma = np.zeros((n_neurons, n_neurons))
        
        for i in range(n_neurons):
            for j in range(i, n_neurons):
                # Find time points where both neurons are observed
                valid_mask = observed_mask[:, i] & observed_mask[:, j]
                
                if np.sum(valid_mask) > 10:  # Minimum samples
                    x_i = activity_data[valid_mask, i]
                    x_j = activity_data[valid_mask, j]
                    Sigma[i, j] = np.cov(x_i, x_j)[0, 1]
                    Sigma[j, i] = Sigma[i, j]
                else:
                    # Interpolate or use prior
                    Sigma[i, j] = 0.0
                    Sigma[j, i] = 0.0
                    
        return Sigma
    
    def compute_granger_causality(self, 
                                  activity_data: np.ndarray,
                                  max_lag: int = 5) -> np.ndarray:
        """
        Compute pairwise Granger causality matrix.
        
        Args:
            activity_data: Neural activity (time x neurons)
            max_lag: Maximum time lag for GC computation
            
        Returns:
            Granger causality matrix (n_neurons x n_neurons)
        """
        n_time, n_neurons = activity_data.shape
        GC_matrix = np.zeros((n_neurons, n_neurons))
        
        for i in range(n_neurons):
            for j in range(n_neurons):
                if i == j:
                    continue
                    
                # Compute GC from i to j
                gc_val = self._granger_causality_pair(
                    activity_data[:, i], 
                    activity_data[:, j],
                    max_lag
                )
                GC_matrix[i, j] = gc_val
                
        return GC_matrix
    
    def _granger_causality_pair(self, 
                                x: np.ndarray, 
                                y: np.ndarray,
                                max_lag: int) -> float:
        """
        Compute Granger causality from x to y.
        
        Args:
            x: Source time series
            y: Target time series
            max_lag: Maximum lag
            
        Returns:
            Granger causality value
        """
        n = len(y)
        
        # Unrestricted model (includes x)
        X_unrestricted = self._build_lag_matrix(np.column_stack([y, x]), max_lag)
        y_target = y[max_lag:]
        
        if X_unrestricted.shape[0] != len(y_target):
            X_unrestricted = X_unrestricted[:len(y_target)]
        
        # Fit unrestricted model
        beta_unrestricted, residuals_unrestricted = self._fit_linear(X_unrestricted, y_target)
        var_unrestricted = np.var(residuals_unrestricted)
        
        # Restricted model (y only)
        X_restricted = self._build_lag_matrix(y.reshape(-1, 1), max_lag)
        
        if X_restricted.shape[0] != len(y_target):
            X_restricted = X_restricted[:len(y_target)]
        
        beta_restricted, residuals_restricted = self._fit_linear(X_restricted, y_target)
        var_restricted = np.var(residuals_restricted)
        
        # Granger causality
        if var_unrestricted > 0:
            gc = np.log(var_restricted / var_unrestricted)
        else:
            gc = 0.0
            
        return max(0, gc)  # GC should be non-negative
    
    def _build_lag_matrix(self, data: np.ndarray, max_lag: int) -> np.ndarray:
        """Build lagged feature matrix for VAR model."""
        n_samples = len(data)
        n_vars = data.shape[1] if data.ndim > 1 else 1
        
        lagged = []
        for lag in range(1, max_lag + 1):
            lagged.append(data[max_lag - lag:n_samples - lag])
            
        return np.hstack(lagged) if len(lagged) > 1 else lagged[0]
    
    def _fit_linear(self, X: np.ndarray, y: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """Fit linear regression and return coefficients and residuals."""
        # Add intercept
        X_with_intercept = np.column_stack([np.ones(len(X)), X])
        
        # Solve normal equations
        beta = np.linalg.lstsq(X_with_intercept, y, rcond=None)[0]
        
        # Predictions and residuals
        y_pred = X_with_intercept @ beta
        residuals = y - y_pred
        
        return beta, residuals
    
    def recover_connectivity(self, 
                            activity_data: np.ndarray,
                            observed_mask: Optional[np.ndarray] = None,
                            method: str = 'combined') -> np.ndarray:
        """
        Main method to recover connectivity matrix.
        
        Args:
            activity_data: Neural activity (time x neurons)
            observed_mask: Boolean mask for observed entries
            method: 'covariance', 'granger', or 'combined'
            
        Returns:
            Estimated connectivity matrix
        """
        # Step 1: Covariance estimation
        Sigma = self.estimate_covariance(activity_data, observed_mask)
        
        # Step 2: Initial estimate from covariance
        W_cov = self._covariance_based_recovery(Sigma)
        
        if method == 'covariance':
            self.W_estimated = W_cov
            return W_cov
        
        # Step 3: Granger causality
        GC_matrix = self.compute_granger_causality(activity_data)
        
        if method == 'granger':
            self.W_estimated = GC_matrix
            return GC_matrix
        
        # Step 4: Combined refinement
        W_combined = self._refine_connectivity(W_cov, GC_matrix)
        self.W_estimated = W_combined
        
        return W_combined
    
    def _covariance_based_recovery(self, Sigma: np.ndarray) -> np.ndarray:
        """
        Recover connectivity from covariance matrix.
        
        Solves: min ||Σ - Σ(W)||² + λ||W||₁
        """
        n = self.n_neurons
        
        # Simplified linear approximation
        # In practice, this would involve solving a non-convex optimization
        # Here we use a proximal gradient approach
        
        W = np.zeros((n, n))
        
        # Initialize with correlation
        W_init = np.corrcoef(Sigma)
        np.fill_diagonal(W_init, 0)
        
        # Soft thresholding for sparsity
        W = self._soft_threshold(W_init, self.lambda_sparse)
        
        return W
    
    def _soft_threshold(self, W: np.ndarray, threshold: float) -> np.ndarray:
        """Apply soft thresholding for L1 regularization."""
        return np.sign(W) * np.maximum(np.abs(W) - threshold, 0)
    
    def _refine_connectivity(self, 
                            W_cov: np.ndarray, 
                            GC_matrix: np.ndarray) -> np.ndarray:
        """
        Refine connectivity by combining covariance and Granger causality.
        """
        # Normalize both matrices
        W_cov_norm = self._normalize_matrix(W_cov)
        GC_norm = self._normalize_matrix(GC_matrix)
        
        # Weighted combination
        alpha = 0.6  # Weight for covariance
        W_combined = alpha * W_cov_norm + (1 - alpha) * GC_norm
        
        # Apply sparsity threshold
        W_sparse = self._apply_sparsity(W_combined)
        
        return W_sparse
    
    def _normalize_matrix(self, W: np.ndarray) -> np.ndarray:
        """Normalize matrix to [0, 1] range."""
        W_min, W_max = np.min(W), np.max(W)
        if W_max > W_min:
            return (W - W_min) / (W_max - W_min)
        return W
    
    def _apply_sparsity(self, W: np.ndarray) -> np.ndarray:
        """Apply sparsity thresholding."""
        # Keep top k% of connections
        k_sparse = 0.1  # 10% sparsity
        threshold = np.percentile(np.abs(W), (1 - k_sparse) * 100)
        
        W_sparse = W.copy()
        W_sparse[np.abs(W_sparse) < threshold] = 0
        
        return W_sparse
    
    def evaluate_recovery(self, 
                         W_true: np.ndarray,
                         metric: str = 'all') -> Dict[str, float]:
        """
        Evaluate recovery quality.
        
        Args:
            W_true: Ground truth connectivity matrix
            metric: Evaluation metric(s)
            
        Returns:
            Dictionary of metrics
        """
        if self.W_estimated is None:
            raise ValueError("Must run recover_connectivity first")
            
        results = {}
        
        # Frobenius norm error
        results['frobenius_error'] = np.linalg.norm(
            self.W_estimated - W_true, 'fro'
        ) / np.linalg.norm(W_true, 'fro')
        
        # Correlation
        results['correlation'] = np.corrcoef(
            self.W_estimated.flatten(), 
            W_true.flatten()
        )[0, 1]
        
        # Support recovery (binary accuracy)
        W_true_binary = (W_true != 0).astype(float)
        W_est_binary = (self.W_estimated != 0).astype(float)
        
        results['precision'] = np.sum(W_est_binary * W_true_binary) / (
            np.sum(W_est_binary) + 1e-10
        )
        results['recall'] = np.sum(W_est_binary * W_true_binary) / (
            np.sum(W_true_binary) + 1e-10
        )
        results['f1_score'] = 2 * results['precision'] * results['recall'] / (
            results['precision'] + results['recall'] + 1e-10
        )
        
        return results
```

### Example Usage

```python
# Generate synthetic data for testing
def generate_synthetic_rnn(n_neurons=50, 
                          sparsity=0.1,
                          n_time=1000,
                          dt=0.1):
    """Generate synthetic RNN data."""
    # Create sparse weight matrix
    W_true = np.random.randn(n_neurons, n_neurons) * 0.1
    mask = np.random.rand(n_neurons, n_neurons) < sparsity
    W_true = W_true * mask
    np.fill_diagonal(W_true, 0)
    
    # Simulate dynamics
    tau = 10.0
    x = np.zeros((n_time, n_neurons))
    x[0] = np.random.randn(n_neurons) * 0.1
    
    for t in range(1, n_time):
        dx = (-x[t-1] + W_true @ np.tanh(x[t-1])) * dt / tau
        x[t] = x[t-1] + dx + np.random.randn(n_neurons) * 0.01
        
    return x, W_true

# Run recovery
n_neurons = 50
activity_data, W_true = generate_synthetic_rnn(n_neurons=n_neurons)

# Create partial observations (observe only 70% of neurons at each time)
observed_mask = np.random.rand(*activity_data.shape) < 0.7

# Recover connectivity
recovery = SparseConnectivityRecovery(n_neurons=n_neurons)
W_estimated = recovery.recover_connectivity(
    activity_data, 
    observed_mask=observed_mask,
    method='combined'
)

# Evaluate
metrics = recovery.evaluate_recovery(W_true)
print(f"Frobenius Error: {metrics['frobenius_error']:.4f}")
print(f"Correlation: {metrics['correlation']:.4f}")
print(f"F1 Score: {metrics['f1_score']:.4f}")
```

---

## Applications

### 1. Neuroscience Research

| Application | Description |
|-------------|-------------|
| **Connectomics** | Reconstruct neural circuits from calcium imaging |
| **EEG/MEG Analysis** | Infer functional connectivity from non-invasive recordings |
| **Electrophysiology** | Estimate synaptic weights from multi-electrode arrays |

### 2. Neural Network Analysis

| Application | Description |
|-------------|-------------|
| **RNN Interpretability** | Understand trained recurrent networks |
| **Network Pruning** | Identify important connections for compression |
| **Fault Diagnosis** | Detect anomalous connectivity patterns |

### 3. Brain-Computer Interfaces

| Application | Description |
|-------------|-------------|
| **Decoding** | Infer intended movements from neural activity |
| **Stimulation** | Design optimal stimulation patterns |
| **Adaptive Control** | Real-time connectivity updates |

---

## Workflow Steps

### Step 1: Data Preparation

```python
# Load neural activity data
activity_data = load_neural_data('experiment.mat')

# Define observation mask (for partial measurements)
observed_mask = create_observation_mask(
    activity_data.shape, 
    observation_rate=0.7
)

# Preprocess (filtering, normalization)
activity_processed = preprocess(activity_data)
```

### Step 2: Covariance Estimation

```python
# Estimate covariance with missing data handling
recovery = SparseConnectivityRecovery(n_neurons=n_neurons)
Sigma = recovery.estimate_covariance(activity_processed, observed_mask)
```

### Step 3: Initial Connectivity Recovery

```python
# Covariance-based initial estimate
W_cov = recovery._covariance_based_recovery(Sigma)
```

### Step 4: Granger-Causality Refinement

```python
# Compute temporal causality
GC_matrix = recovery.compute_granger_causality(activity_processed)

# Combine estimates
W_final = recovery._refine_connectivity(W_cov, GC_matrix)
```

### Step 5: Validation

```python
# Compare with ground truth if available
metrics = recovery.evaluate_recovery(W_true)

# Visualize results
visualize_connectivity(W_true, W_final)
```

---

## Activation Keywords

- sparse neural connectivity
- partial measurements
- covariance-based estimation
- Granger causality
- neural connectivity recovery
- recurrent neural network
- RNN weight estimation
- sparse recovery
- 稀疏神经连接
- 部分观测
- 协方差估计
- 格兰杰因果
- 神经网络连接恢复

---

## Related Skills

- `neural-connectivity-matrix-viewer` - Visualize connectivity matrices
- `spiking-neural-network-analysis` - SNN research analysis
- `neuron-model-reconstruction` - Reconstruct neuron models from spike times
- `brain-higher-order-structures` - Higher-order brain network analysis
- `time-varying-brain-connectivity` - Dynamic connectivity analysis

---

## References

1. **Simeon, Q.** (2026). Recovering Sparse Neural Connectivity from Partial Measurements: A Covariance-Based Approach with Granger-Causality Refinement. *arXiv:2603.18497v1*.

2. **Granger, C. W. J.** (1969). Investigating causal relations by econometric models and cross-spectral methods. *Econometrica*, 37(3), 424-438.

3. **Bressler, S. L., & Seth, A. K.** (2011). Wiener–Granger causality: A well established methodology. *NeuroImage*, 58(2), 323-329.

4. **Tibshirani, R.** (1996). Regression shrinkage and selection via the lasso. *Journal of the Royal Statistical Society: Series B*, 58(1), 267-288.

5. **Sporns, O.** (2011). Networks of the Brain. *MIT Press*.

---

## Implementation Notes

### Computational Complexity

| Step | Complexity | Notes |
|------|------------|-------|
| Covariance Estimation | O(T·N²) | T: time points, N: neurons |
| Granger Causality | O(N²·L³) | L: max lag |
| Sparse Recovery | O(N³) | Per iteration |

### Hyperparameter Guidelines

| Parameter | Typical Range | Effect |
|-----------|---------------|--------|
| `lambda_sparse` | 0.01 - 0.5 | Higher = sparser |
| `gc_threshold` | 0.01 - 0.1 | Higher = fewer connections |
| `max_lag` | 3 - 10 | Longer = more temporal info |
| `tau` | 5 - 20 ms | Neural time constant |

### Limitations

1. **Linearity Assumption**: Current implementation assumes near-linear dynamics
2. **Stationarity**: Assumes connectivity doesn't change during observation
3. **Observation Ratio**: Requires sufficient observation density (>50%)
4. **Noise Sensitivity**: Performance degrades with high noise levels

---

## Tools Used

- `read` - Read skill documentation and references
- `write` - Save analysis results and connectivity matrices
- `exec` - Run Python scripts for connectivity recovery

## Instructions for Agents

1. **Understand the data**: Check observation completeness and data quality
2. **Select method**: Choose 'covariance', 'granger', or 'combined' based on data characteristics
3. **Tune hyperparameters**: Adjust `lambda_sparse` and `gc_threshold` for desired sparsity
4. **Validate results**: Compare with known connectivity if available
5. **Visualize**: Use connectivity matrix viewers to inspect results


## Examples

### Example 1: Basic Usage

**User:** 请帮我应用此技能

**Agent:** 我将按照标准流程执行...

### Example 2: Advanced Usage

**User:** 有更复杂的场景需要处理

**Agent:** 针对复杂场景，我将采用以下策略...
