---
name: sparse-neural-connectivity-recovery
description: Covariance-based method with Granger-causality refinement for recovering sparse neural connectivity from partial measurements.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [connectivity-inference, granger-causality, sparse-recovery, neural-circuits, partial-observation, neuroscience]
    source_paper: "Recovering Sparse Neural Connectivity from Partial Measurements: A Covariance-Based Approach with Granger-Causality Refinement (arXiv:2603.18497v1)"
---

# Sparse Neural Connectivity Recovery

## Overview
Inferring neural circuit connectivity from incomplete observations is a fundamental challenge in neuroscience. This approach combines covariance-based weight matrix estimation with Granger-causality refinement to recover sparse connectivity patterns even when only a subset of neurons are observable.

## Core Concepts

### Covariance-Based Estimation
- Uses observed neural activity covariance to estimate connectivity
- Handles partial observability through matrix completion techniques
- Exploits sparsity of real neural circuits (most connections are zero)

### Granger-Causality Refinement
- Granger causality tests directional influence between neurons
- Refines covariance estimates by testing temporal precedence
- Reduces false positives from indirect connections

### Partial Measurement Handling
- Works with subset of neurons observed
- Uses low-rank structure of covariance for completion
- Iterative refinement between observed and latent variables

## Implementation Pattern
```python
from sklearn.covariance import GraphicalLasso

class SparseConnectivityRecovery:
    def __init__(self, n_observed, sparsity_lambda=0.1):
        self.n_obs = n_observed
        self.lambda_ = sparsity_lambda
    
    def covariance_estimate(self, neural_data):
        model = GraphicalLasso(alpha=self.lambda_)
        model.fit(neural_data)
        W_init = -model.precision_
        np.fill_diagonal(W_init, 0)
        return W_init
    
    def granger_refinement(self, neural_data, W_init, max_lag=5):
        n, T = neural_data.shape
        W_refined = W_init.copy()
        for i in range(n):
            for j in range(n):
                if i == j: continue
                granger_score = self._granger_test(
                    neural_data[j], neural_data[i], max_lag
                )
                if granger_score < 0.05:
                    W_refined[i, j] *= 0
        return W_refined
    
    def recover(self, neural_data):
        W_init = self.covariance_estimate(neural_data)
        return self.granger_refinement(neural_data, W_init)
```

## Applications
- Neural circuit mapping from electrophysiology
- Brain connectivity inference from fMRI/EEG
- Computational connectomics
- Neuroprosthetic interface design

## Activation Keywords
- neural connectivity inference, sparse connectivity recovery, Granger causality brain, partial observation neural, connectome estimation, 神经连接推断, 稀疏连接恢复

## References
- Recovering Sparse Neural Connectivity from Partial Measurements: A Covariance-Based Approach with Granger-Causality Refinement
- Authors: Quilee Simeon
- Published: 2026-03-19
- arXiv: https://arxiv.org/abs/2603.18497v1