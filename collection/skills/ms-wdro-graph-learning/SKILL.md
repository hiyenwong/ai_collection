---
name: ms-wdro-graph-learning
version: 1.0.0
description: MS-WDRO for heterogeneous brain connectivity learning.
trigger_words:
  - ms-wdro
  - multi-source wasserstein graph learning
  - heterogeneous brain connectivity
  - distributionally robust graph learning
---

# Multi-Source Wasserstein Distributionally Robust Graph Learning (MS-WDRO)

## Overview
MS-WDRO is a multi-source Wasserstein distributionally robust graph learning framework that fuses heterogeneous sources via their weighted Wasserstein barycenter, preserving each source's intrinsic geometry while building an ambiguity ball to hedge residual uncertainty. This methodology is particularly valuable for neuroscience applications where target-domain samples are scarce but heterogeneous source-domain data are abundant (e.g., multi-site fMRI studies).

## Core Contributions
- **Geometric Fusion**: Uses Wasserstein metric's distribution-preserving properties to counter heterogeneity while preserving intrinsic geometry of each source
- **Wasserstein Barycenter**: Fuses heterogeneous sources via weighted Wasserstein barycenter as a geometrically principled nominal distribution  
- **Distributional Robustness**: Builds ambiguity ball around barycenter to hedge residual uncertainty through worst-case risk minimization
- **Tractable Estimation**: Yields regularized Laplacian estimator solved efficiently via provably convergent ADMM scheme
- **Theoretical Guarantees**: Provides non-asymptotic bounds including finite-sample concentration, pooling bias lower bound, and out-of-sample excess risk
- **Differentiable Architecture**: Unrolls solver into differentiable architecture for end-to-end hyperparameter calibration

## Use Cases
- Multi-site neuroimaging analysis (ABIDE, ADNI datasets)
- Brain connectivity inference with scarce target samples
- Heterogeneous graph signal processing
- Federated learning scenarios with divergent data distributions
- Sample-scarce regime graph recovery

## Implementation Steps
1. **Data Preparation**: Organize heterogeneous source domains and scarce target domain samples
2. **Wasserstein Barycenter Computation**: Calculate weighted Wasserstein barycenter of source distributions
3. **Ambiguity Ball Construction**: Define uncertainty set around barycenter based on desired robustness level
4. **Regularized Laplacian Estimation**: Solve distributionally robust optimization problem via ADMM
5. **Hyperparameter Calibration**: Train differentiable unrolled solver end-to-end for adaptive parameter selection
6. **Graph Recovery**: Extract final graph topology from optimized Laplacian

## Performance Characteristics
- Consistently outperforms 7+ baselines in graph recovery accuracy
- Superior sample efficiency, especially in sample-scarce regimes
- Enhanced downstream diagnostic utility in neuroimaging applications
- Parametric convergence rate with logarithmic dependence on source count

## Key Parameters
- **Robustness radius**: Controls size of ambiguity ball
- **Sparsity regularization**: Balances graph density vs. interpretability  
- **Source fusion weights**: Determines contribution of each heterogeneous source
- **ADMM convergence tolerance**: Affects computational efficiency vs. solution accuracy

## References
- arXiv:2608.19914v1 (August 20, 2026)
- ABIDE~I neuroimaging dataset validation
- Non-asymptotic theoretical guarantees with finite-sample bounds

## Activation
Use when dealing with heterogeneous multi-source graph learning problems in neuroscience, particularly when target samples are limited but multiple source domains are available with potential distributional divergence.