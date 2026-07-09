---
name: qcnn-rough-path-signatures
description: Quantum Convolutional Neural Network with Rough Path Signature Kernels for time series classification. Hybrid quantum-classical architecture using path signatures to handle time reparameterization invariance.
tags: [quantum, neural-network, time-series, path-signatures, qcnn, variational-quantum]
created: 2026-07-09
---

# QCNN with Rough Path Signature Kernels

## Overview
Hybrid quantum-classical architecture for time series classification that integrates Quantum Convolutional Neural Networks (QCNN) with rough path signature kernels to address time reparameterization invariance.

## Core Methodology

### Path Signature Kernels
- Computes signature kernel between pairs of input paths (reference path vs target path)
- Mitigates impact of time reparametrization invariance in time series data
- Feature layers use either classical or quantum variational linear solvers (VQLS)

### Architecture Components
1. **Signature Kernel Layer**: Computes path signatures using classical or quantum VQLS
2. **QCNN Layer**: Performs downstream learning tasks with quantum convolutional operations
3. **Hybrid Integration**: Classical preprocessing + quantum feature extraction + quantum classification

### Key Innovations
- First application of rough path theory to quantum neural networks
- Handles time warping/reparameterization without explicit alignment
- Leverages quantum advantage for high-dimensional feature spaces

## Implementation Details

### Signature Kernel Computation
```
For input paths X, Y:
1. Compute iterated integrals (signature) up to depth N
2. Inner product in signature space: <S(X), S(Y)>
3. Use as kernel for quantum circuit encoding
```

### Quantum Circuit Design
- Variational quantum linear solver (VQLS) for signature computation
- QCNN architecture with pooling layers for hierarchical feature extraction
- Parameterized quantum circuits for classification

## Applications
- Time series classification with temporal warping
- Handwritten digit recognition from temporal sequences
- Any sequential data with reparameterization invariance

## Limitations
- VQLS component has computational limitations for deep signatures
- Requires careful choice of signature truncation depth
- Quantum hardware constraints on circuit depth

## Activation Keywords
quantum CNN, rough paths, signature kernels, time series classification, VQLS, path signatures, temporal invariance, quantum neural networks

## Reference
arXiv:2607.07634 - "QCNN with Rough Path Signature Kernels"
