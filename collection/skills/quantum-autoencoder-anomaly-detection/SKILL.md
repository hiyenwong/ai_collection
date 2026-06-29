---
name: quantum-autoencoder-anomaly-detection
description: Quantum autoencoder (QAE) methodology for compression-driven anomaly detection in brain MRI and medical imaging. Uses angle encoding, variational encoder-decoder with trash qubits, and incompressibility-based anomaly scoring.
category: quantum-ml
trigger_words: quantum autoencoder, QAE, anomaly detection, medical imaging, brain MRI, compression-driven detection, trash qubits, variational encoder-decoder, ROC-AUC anomaly
source: arXiv:2606.27411
---

# Quantum Autoencoder for Compression-Driven Anomaly Detection

## Overview

This methodology uses Quantum Autoencoders (QAE) for anomaly detection by leveraging the principle that anomalous data resists compression relative to normal data. The approach maps data patches into quantum states and trains a variational encoder-decoder to discard information via trash qubits, with anomaly scores based on reconstruction fidelity.

## Key Insight

**Incompressibility as Anomaly Signal**: Normal data compresses well under the learned latent representation; anomalies resist compression. The degree of incompressibility serves as a natural, interpretable anomaly score.

## Core Components

### 1. Angle Encoding
- Map image patches into quantum states
- Each pixel/feature mapped to rotation angle on qubit
- Parameter-efficient compared to amplitude encoding

### 2. Variational Encoder-Decoder Architecture
- Encoder: compresses input into latent quantum state
- Trash qubits: auxiliary qubits that absorb discarded information
- Decoder: reconstructs from latent state
- Trained to minimize reconstruction error on normal data

### 3. Anomaly Scoring
- Score = 1 - reconstruction fidelity
- Higher scores = more anomalous
- Threshold selection based on compression-reconstruction trade-off

### 4. Encoder-Decoder Asymmetry
- Effective anomaly detection arises from structured information compression in encoder
- Not driven by increased parameter magnitude or decoder expressivity
- Provides interpretable mechanism for detection

## Performance

- Slice-level ROC-AUC: ~0.95 (brain MRI)
- Patch-level ROC-AUC: ~0.813
- Outperforms classical autoencoder and PCA baselines
- Produces spatially localized anomaly heatmaps

## Implementation Pattern

```
1. Prepare normal training data (patches/images)
2. Encode data using angle encoding into quantum states
3. Train variational encoder-decoder with trash qubits
   - Minimize reconstruction error on normal data
   - Optimize trash qubit discard pattern
4. For inference:
   a. Encode test data
   b. Measure reconstruction fidelity
   c. Compute anomaly score = 1 - fidelity
   d. Apply threshold for classification
5. Generate anomaly heatmaps from local reconstruction errors
```

## Pitfalls

- **Training data quality**: Requires clean, representative normal data; contaminated training set degrades detection
- **Patch size**: Too small patches lose context; too large patches exceed qubit capacity
- **Threshold selection**: Operating regime supports principled threshold selection, but requires calibration data
- **Noise sensitivity**: Quantum hardware noise affects reconstruction; error mitigation needed for real deployment

## Applications

- Brain MRI anomaly detection (tumors, lesions)
- General medical imaging anomaly detection
- Industrial defect detection
- Any domain where normal data manifold is well-defined

## Activation

Use when: quantum autoencoder for anomaly detection, medical imaging anomaly detection, compression-based anomaly scoring, quantum machine learning for medical diagnosis, brain MRI analysis, variational quantum encoder-decoder.
