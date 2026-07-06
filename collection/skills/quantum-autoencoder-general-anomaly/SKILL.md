---
name: quantum-autoencoder-general-anomaly
description: Quantum convolutional autoencoder (QCAE) for reconstruction-based anomaly detection using QCNN architectures - semi-supervised training on normal samples with reconstruction error as anomaly score.
category: quantum
created: 2026-07-06
source: arXiv:2607.02135
---

# Quantum Convolutional Autoencoders for Anomaly Detection

## Source

arXiv:2607.02135 - "Quantum Convolutional Autoencoders for Reconstruction-Based Anomaly Detection" by Donovan Slabbert, Francesco Petruccione (2026-07-02)

## Overview

Quantum convolutional neural networks (QCNNs) adapted into quantum autoencoder (QAE) framework for reconstruction-based anomaly detection. Models trained semi-supervised on normal samples with reconstruction error as anomaly score.

## Core Methodology

1. **QCNN-to-QAE Architecture**: Adapt quantum convolutional neural network architecture into autoencoder framework. Hierarchical representation of quantum information enables efficient compression.

2. **Two Architecture Variants**: Models differ in treatment of latent information:
   - Architecture A: Direct latent encoding
   - Architecture B: Modified latent space handling

3. **Semi-Supervised Training**: Train on normal samples only to reconstruct feature-extracted and dimensionally reduced time-series data.

4. **Reconstruction Error Scoring**: Use reconstruction error as anomaly score - anomalies resist compression, producing higher reconstruction errors.

## Key Findings

- QCNNs provide efficient parameterization for anomaly detection
- Hierarchical quantum representations capture data structure effectively
- Semi-supervised approach works well with limited normal data
- Two architecture variants offer different tradeoffs
- Applicable to scientific data analysis across domains

## Applications

- Anomaly detection in time-series data
- Scientific data analysis
- Quantum machine learning pipelines
- Semi-supervised classification tasks
- Dimensionality reduction for anomaly detection

## Trigger Words

quantum convolutional autoencoder, anomaly detection, QCNN, semi-supervised, reconstruction error, time-series analysis, quantum machine learning

## Activation

When:
- Building anomaly detection systems with quantum circuits
- Working with quantum convolutional architectures
- Designing semi-supervised learning pipelines
- Analyzing time-series data for anomalies
- Exploring quantum advantage in unsupervised learning