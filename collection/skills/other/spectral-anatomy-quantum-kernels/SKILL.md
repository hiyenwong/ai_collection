---
name: spectral-anatomy-quantum-kernels
description: "Spectral entropy diagnostic S(K)/log n for quantum Gaussian process kernels. Unified framework showing dequantization and posterior pathologies governed by same quantity. Proves Cauchy-Schwarz tail bound on Nystrom error, variance-contraction identity, target-dependent optimal entropy. Verified on IBM Heron hardware. Activation: quantum Gaussian process, spectral entropy, quantum kernel diagnostic, Nystrom approximation, kernel Gram matrix, quantum dequantization, Bach degrees of freedom"
metadata:
  arxiv_id: "2605.30952"
  published: "2026-05-28"
  authors: "Jian Xu, Chao Li, Guang Lin, Yuning Qiu, Delu Zeng, John Paisley, Qibin Zhao"
  tags: [quantum, gaussian-process, kernel-methods, spectral-analysis, bayesian-optimization]
---

## Core Insight: Spectral Entropy Unifies QGP Phenomena

Two seemingly unrelated QGP failures are governed by the same quantity:

1. **Dequantization**: HHL-based QGP regression loses exponential speedup in well-conditioned regime
2. **Posterior pathology**: Highly expressive quantum kernels break Bayesian optimization

Both are controlled by the **normalized spectral entropy** of the kernel Gram matrix:

$$S(K) / \log n = -\frac{1}{\log n} \sum_i \lambda_i \log \lambda_i$$

where $\lambda_i$ are normalized eigenvalues of the kernel Gram matrix $K$.

## Key Theoretical Results

### 1. Cauchy-Schwarz Tail Bound on Nystrom Error
Bounds approximation error in terms of spectral tail decay. Fast-decaying spectra (low entropy) → small Nystrom error → classical methods competitive.

### 2. Finite-Sample Variance-Contraction Identity
$$\text{Var}[\hat{f}] = \text{function of Bach's degrees of freedom } d_\sigma(K)$$

Relates kernel effective dimension to posterior variance contraction rate.

### 3. Target-Dependent Optimal Entropy
- **Smooth targets**: NLL sweet spot at HIGH spectral entropy
- **Band-limited quantum data**: NLL sweet spot at LOW spectral entropy

The optimal kernel choice depends on target function's intrinsic dimension in the kernel eigenbasis.

## Universal Diagnostic

The spectral entropy diagnostic is **kernel-agnostic**:

- Hardware-efficient ansatz
- Matchgate circuits
- IQP circuits
- RBF/Matern kernels
- Random Fourier Features
- Deep kernels

All collapse onto identical $S/\log n$ curves for dequantization, ECE, and variance-contraction panels.

## Hardware Verification

Verified on IBM Heron backends:
- Median absolute error: 3.2% in $S/\log n$
- Mean error: 5.2% across 24 configurations at $n_q = 4$
- Transfers to $n_q = 6$ with mean error 1.7%
- No error mitigation applied

## Practical Usage

```python
# Compute spectral entropy diagnostic
import numpy as np
from scipy.linalg import eigh

def spectral_entropy_diagnostic(K):
    """Compute normalized spectral entropy of kernel Gram matrix."""
    eigenvalues = eigh(K, eigvals_only=True)
    eigenvalues = eigenvalues[eigenvalues > 1e-10]  # Filter numerical zeros
    eigenvalues = eigenvalues / eigenvalues.sum()   # Normalize
    S = -np.sum(eigenvalues * np.log(eigenvalues))
    return S / np.log(len(eigenvalues))

# Interpretation:
# S/log(n) ≈ 0 → Low entropy (localized kernel, few dominant eigenvectors)
# S/log(n) ≈ 1 → High entropy (delocalized kernel, many contributing eigenvectors)
```

## When to Apply

- Diagnosing QGP kernel choice before expensive quantum circuit execution
- Understanding why a quantum kernel underperforms classical alternatives
- Selecting kernel family based on target function characteristics
- Hardware validation: comparing simulator vs real-device spectral behavior

## Pitfalls

- **Outlier runs**: Calibration drift can cause 30% outliers in spectral entropy → rerun
- **No error mitigation needed**: Diagnostic is robust to noise without mitigation
- **Target dependency**: No single "best" entropy; optimal value depends on target function
