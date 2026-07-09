---
name: qcnn-with-rough-path-signature-kernels
description: 'Time series analysis plays a vital role across a wide range of scientific and engineering domains but poses substantial computational challenges. A major difficulty arises from the time reparameteriza. Based on arXiv:2607.07634.'
---

# QCNN with Rough Path Signature Kernels

**arXiv**: 2607.07634 | **Authors**: Leonardo Nogueira Falabella, Vasily Sazonov | **Utility**: 0.85

## Overview

Time series analysis plays a vital role across a wide range of scientific and engineering domains but poses substantial computational challenges. A major difficulty arises from the time reparameterization invariance of time series data, which complicates the extraction of meaningful temporal features. In this work, we address the problem of time series classification by exploring the application of quantum computation techniques. We propose a hybrid quantum-classical architecture that integrates recent advances in quantum neural networks with the mathematical framework of path signatures, mitigating the impact of time reparametrization invariance. The architecture employs feature layers that compute a signature kernel between pairs of input paths, consisting of a reference path and a target path for classification, using either classical or quantum variational linear solvers (VQLS). These feature layers are followed by a Quantum Convolutional Neural Network (QCNN) to perform downstream learning tasks. We evaluate several realizations of the proposed architecture, differing in QCNN configurations, on a binary classification task involving time series representations of handwritten digits. Our experiments demonstrate the potential advantages of implementing path signature kernel layers within quantum circuits and provide an analysis of the computational limitations associated with the VQLS component.

## Key Contributions

1. Time series analysis plays a vital role across a wide range of scientific and engineering domains but poses substantial computational challenges.
2. A major difficulty arises from the time reparameterization invariance of time series data, which complicates the extraction of meaningful temporal features.
3. In this work, we address the problem of time series classification by exploring the application of quantum computation techniques.
4. We propose a hybrid quantum-classical architecture that integrates recent advances in quantum neural networks with the mathematical framework of path signatures, mitigating the impact of time reparametrization invariance.

## Implementation Notes

- **Keywords**: quantum
- **Categories**: quant-ph, cs.AI
- **Published**: 2026-07-08

## Activation Criteria

Use this skill when working on tasks involving: quantum.
