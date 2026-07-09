---
name: qcnn-rough-path-signature
category: quantum-machine-learning
description: Hybrid quantum-classical architecture combining path signature kernels with QCNN for time series classification, addressing time reparameterization invariance. (arXiv: 2607.07634)
activation: QCNN, signature kernel, quantum convolutional neural network, time series classification, rough path signature, VQLS, quantum machine learning time series
---

# QCNN with Rough Path Signature Kernels

## Overview

This paper proposes a hybrid quantum-classical architecture integrating Quantum Convolutional Neural Networks (QCNN) with rough path signature kernels for time series classification. The approach mitigates time reparameterization invariance — a major challenge in time series analysis.

**Paper**: "QCNN with Rough Path Signature Kernels" (arXiv:2607.07634, 2026-07-08)

## Core Methodology

### Architecture
1. **Signature Kernel Layer**: Computes kernel between input path and reference path using classical or quantum VQLS
2. **QCNN Layer**: Performs downstream classification on signature features

### Rough Path Signatures
Path signatures capture sequential information in a time-reparameterization invariant way. For a time series path X(t), the signature is the infinite sequence of iterated integrals:
- Level 1: ∫dX (total displacement)
- Level 2: ∫∫dX⊗dX (area swept)
- Level n: n-fold iterated integrals

### Quantum Integration
- **VQLS**: Variational Quantum Linear Solver for computing signature kernels
- **QCNN**: Quantum convolutional layers for hierarchical feature extraction
- Tested on binary classification of handwritten digit time series

## Implementation Pattern

```python
def signature_kernel_layer(path_x, path_y, method="classical"):
    """Compute signature kernel between paths"""
    if method == "classical":
        return classical_signature_kernel(path_x, path_y)
    elif method == "quantum":
        # Use VQLS to solve linear system for kernel
        return vqls_signature_kernel(path_x, path_y)

def qcnn_signature_classifier(time_series, reference_paths):
    """Full pipeline: signature → QCNN → classification"""
    # Compute signature features
    features = [signature_kernel_layer(ts, ref) 
                for ref in reference_paths]
    # QCNN classification
    return qcnn_forward(features)
```

## Key Findings
- Path signature kernels provide time-reparameterization invariance
- QCNN architectures can leverage signature features effectively
- VQLS implementation faces computational limitations at scale
- Classical signature kernel computation is more practical for current hardware

## Pitfalls
- **VQLS limitations**: Variational quantum linear solvers face scalability challenges
- **Truncation depth**: Signature computation requires truncation; deeper truncation increases computational cost
- **Reference path selection**: Choice of reference paths affects kernel quality
- **Quantum advantage unclear**: Classical signatures may be sufficient for many practical applications

## References
- arXiv:2607.07634 — QCNN with Rough Path Signature Kernels
