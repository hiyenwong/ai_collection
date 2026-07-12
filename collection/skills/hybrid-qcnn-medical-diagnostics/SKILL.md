---
name: hybrid-qcnn-medical-diagnostics
description: Hybrid classical-quantum diagnostic framework using QCNNs for multi-class medical image classification
version: "1.0"
source: "arXiv:2511.12386"
arxiv_id: "2511.12386"
authors: "Shabnam Sodagari, Tommy Long"
published: "2025-11-15"
categories: "cs.CV"
created: "2026-07-08"
trigger_words:
  - quantum diagnostics
  - QCNN
  - quantum medical
  - quantum classification
  - medical image quantum
  - hybrid quantum medical
  - quantum convolutional neural network
---

# Hybrid QCNN Medical Diagnostics

## Overview

Hybrid classical-quantum diagnostic framework for multi-class medical image classification. Uses pretrained classical encoders to extract features, then embeds them into quantum states processed by Quantum Convolutional Neural Networks (QCNNs).

**Paper**: "Leveraging Quantum-Based Architectures for Robust Diagnostics" (arXiv:2511.12386)

## Results

- Kidney CT classification: 99% accuracy
- Cervical cell (pap smear) classification: 97% accuracy
- Brain tumor (MRI) classification: 99% accuracy
- Consistently outperforms classical CNN baselines with fewer trainable parameters

## Architecture Pattern

1. Medical Image -> Pretrained Encoder -> Quantum Encoding (Angle/Amplitude) -> QCNN -> Classification

### Three-Stage Pipeline

1. **Preprocessing**: Dataset-specific preprocessing and transfer learning
2. **Feature Extraction**: Pretrained encoder extracts latent features from medical images
3. **Quantum Processing**: Features embedded into quantum states via angle or amplitude encoding, processed by QCNN

### Encoding Strategies

- **Angle Encoding**: Maps features to rotation angles of qubits
- **Amplitude Encoding**: Maps features to amplitudes of quantum state vectors

### QCNN Design

- Quantum convolutional layers for hierarchical feature extraction
- Quantum pooling for dimensionality reduction
- Measurement-based classification output

## Implementation Notes

- Hybrid models achieve strong and stable convergence across diverse medical imaging tasks
- Fewer trainable parameters than classical CNN baselines
- Angle encoding works well for lower-dimensional feature spaces
- Amplitude encoding suitable for higher-dimensional representations (requires log(N) qubits for N features)

## Key Insights

1. Quantum-enhanced architectures show promise for medical diagnostics with compact models
2. Transfer learning + quantum processing is an effective hybrid strategy
3. QCNNs generalize across multiple medical imaging modalities (CT, MRI, microscopy)
4. Quantum models can match or exceed classical performance with fewer parameters

## When to Use

- Multi-class medical image classification tasks
- Settings requiring compact, expressive models
- Hybrid classical-quantum pipeline design
- Medical diagnostics with limited training data (transfer learning helps)
