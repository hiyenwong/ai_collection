---
name: qae-mri-anomaly-detection
description: Quantum autoencoder (QAE) for compression-driven anomaly detection in brain MRI data - angle encoding into quantum states, variational encoder-decoder with trash qubits, achieving 0.95 slice-level ROC-AUC.
category: quantum
created: 2026-07-06
source: arXiv:2606.27411
---

# Compression-Driven Anomaly Detection in Brain MRI Using Quantum Autoencoder

## Source

arXiv:2606.27411 - "Compression-Driven Anomaly Detection in Brain MRI Using an Interpretable Quantum Autoencoder" by Santanu Ganguly, Xing Liang, Dimitrios Makris (2026-06-25)

## Overview

A quantum autoencoder (QAE) approach for compression-driven anomaly detection in brain MRI data. Leverages angle encoding to map image patches into quantum states, followed by variational encoder-decoder architecture.

## Core Methodology

1. **Angle Encoding**: Map image patches into quantum states using angle encoding.

2. **Variational Encoder-Decoder Architecture**: Train to discard information via auxiliary trash qubits. The encoder compresses, the decoder reconstructs, and trash qubits absorb noise/irrelevant information.

3. **Anomaly Scoring**: Anomaly scores reflect the degree to which inputs resist compression relative to normal data. Higher scores = deviations from the learned normal manifold.

4. **Interpretability**: Analysis of learned parameters reveals encoder-decoder asymmetry where effective anomaly detection correlates with parameter patterns.

## Key Results

- **Slice-level ROC-AUC**: ~0.95
- **Patch-level ROC-AUC**: ~0.813
- **Outperforms**: Classical autoencoder and PCA baselines
- **Datasets**: Publicly available brain MRI DICOM datasets

## Applications

- Brain tumor detection via anomaly detection
- Neurological disease screening on MRI
- Medical imaging quality control
- Unsupervised pathology detection

## Trigger Words

quantum autoencoder, brain MRI, anomaly detection, compression, trash qubits, angle encoding, variational quantum circuit, ROC-AUC, medical imaging

## Activation

When working with:
- Quantum machine learning for medical imaging
- Anomaly detection on MRI or medical scans
- Quantum autoencoder architectures
- Unsupervised medical diagnosis
- Compression-based anomaly scoring