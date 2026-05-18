---
name: kap-cpd
description: >
  KAP-CPD methodology for kernel aggregation-based change-point detection in
  dynamic networks, including brain functional connectivity networks. Aggregates
  information from multiple kernels to adapt to diverse change patterns without
  assuming specific network distributions. Includes KAPf-CPD, a fast analytic
  testing procedure that substantially reduces computation time for long network
  sequences. Use when detecting structural changes in dynamic brain networks,
  identifying state transitions in fMRI time-varying connectivity, kernel-based
  change-point detection, dynamic network analysis, or functional connectivity
  state detection. Triggers: change-point detection, dynamic brain networks,
  kernel aggregation, time-varying connectivity, network state transitions,
  KAP-CPD, functional connectivity dynamics.
  arXiv: 2605.14463 (Sun & Chen, 2026).
---

# KAP-CPD: Kernel Aggregation for Change-Point Detection in Dynamic Networks

Kernel-agnostic change-point detection framework that aggregates information from
multiple kernels, achieving strong empirical power across diverse network change
patterns. Includes a fast analytic variant (KAPf-CPD) for scalable processing.

## Problem Statement

Kernel-based change-point detection methods depend sensitively on kernel choice.
When the underlying change pattern is unknown, selecting an appropriate kernel is
challenging. KAP-CPD solves this by aggregating across multiple kernels.

## Core Framework

### Multi-Kernel Aggregation

Instead of relying on a single kernel:
```
KAP-CPD = Aggregate(K₁, K₂, ..., K_m)
```

Where each kernel K_i captures different change patterns:
- Linear kernels: detect mean shifts
- RBF/Gaussian kernels: detect distributional changes
- Graph kernels: detect structural changes in connectivity
- Custom kernels: domain-specific patterns

### Test Statistic

The aggregated test statistic combines evidence across all kernels:
```
T_aggregated = Σ w_i · T(K_i)
```

where T(K_i) is the test statistic for kernel K_i and w_i are data-driven weights.

### Distribution-Free

The method does not assume specific underlying network distributions, making it
applicable to diverse data types including:
- Brain functional connectivity networks
- Social communication networks
- Financial correlation networks
- Any time-varying graph-structured data

## KAPf-CPD: Fast Analytic Variant

For long network sequences, permutation-based testing is computationally expensive.
KAPf-CPD provides:
- **Analytic null distribution** approximation
- **Substantially reduced computation time**
- **Comparable statistical power** to permutation-based approach
- **Scalable to long sequences** where permutation tests are infeasible

## Application to Brain Networks

### Change-Point Detection in fMRI

1. **Extract time-varying FC matrices** using sliding window or other methods
2. **Apply KAP-CPD** to detect significant state transitions
3. **Identify connectivity states** between change points
4. **Analyze state characteristics** (which connections change, how much)

### Brain-Specific Considerations

- FC matrices are correlation/covariance matrices
- Change patterns include: community reorganization, hub switching, global
  connectivity shifts, localized connection changes
- Multiple kernels capture different types of neural state transitions

## Implementation Pattern

```python
import numpy as np
from sklearn.metrics.pairwise import rbf_kernel, linear_kernel

def kap_cpd_test(network_sequence, kernels=None, n_permutations=1000):
    """
    KAP-CPD: Kernel Aggregation Change-Point Detection.
    
    Args:
        network_sequence: list of adjacency matrices [A_1, A_2, ..., A_T]
        kernels: list of kernel functions (default: [linear, RBF])
        n_permutations: number of permutations for null distribution
    """
    T = len(network_sequence)
    
    if kernels is None:
        kernels = [linear_kernel, rbf_kernel]
    
    # Compute test statistic for each kernel
    kernel_stats = []
    for K_fn in kernels:
        # Flatten networks into feature vectors
        features = np.array([A[np.triu_indices(A.shape[0])] 
                            for A in network_sequence])
        # Compute kernel matrix
        K_mat = K_fn(features)
        # Compute CUSUM-based test statistic
        stat = compute_cusum_stat(K_mat, T)
        kernel_stats.append(stat)
    
    # Aggregate across kernels
    aggregated_stat = np.mean(kernel_stats)
    
    # Permutation test (or use KAPf-CPD analytic approximation)
    null_stats = []
    for _ in range(n_permutations):
        permuted = permute_networks(network_sequence)
        # ... compute permuted statistic
        null_stats.append(permuted_stat)
    
    p_value = np.mean([s >= aggregated_stat for s in null_stats])
    return aggregated_stat, p_value
```

## Key Contributions

1. **Kernel-agnostic approach**: Adapts to diverse change patterns automatically
2. **Distribution-free**: No assumptions about network distribution
3. **Strong empirical power**: Validated across multiple change scenarios
4. **Fast analytic variant**: KAPf-CPD for scalable long-sequence analysis
5. **Validated on brain FC networks**: Tested on real functional connectivity data

## Activation Keywords

- KAP-CPD, change-point detection dynamic networks, kernel aggregation, brain
  network state transitions, time-varying functional connectivity, dynamic network
  analysis, KAPf-CPD, FC change detection, network state detection
