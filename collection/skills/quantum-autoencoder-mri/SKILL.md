---
name: quantum-autoencoder-mri
description: Quantum autoencoder (QAE) methodology for compression-driven anomaly detection in brain MRI using angle encoding and trash qubits.
trigger_words: ["quantum autoencoder", "MRI anomaly detection", "compression anomaly detection", "trash qubits", "brain MRI quantum"]
category: quantum-medical
arxiv_id: "2606.27411"
created: "2026-07-01"
---

# Quantum Autoencoder for MRI Anomaly Detection

## Overview
Compression-driven anomaly detection in brain MRI using a quantum autoencoder (QAE) with variational encoder-decoder architecture and trash qubits.

## Core Methodology

### 1. Data Encoding
- **Angle encoding**: Map MRI image patches into quantum states
- Each pixel value → rotation angle on qubit
- Patch-based processing for manageable qubit count

### 2. Architecture
- Variational encoder circuit compresses input state
- **Trash qubits**: Auxiliary qubits for discarding redundant information
- Decoder reconstructs compressed representation
- Training minimizes reconstruction error on normal data

### 3. Anomaly Detection
- Trained on healthy/normal brain MRI data
- Anomalies produce higher reconstruction error
- Compression fidelity serves as anomaly score
- Interpretable: trash qubit measurements reveal compressed features

## Advantages
- Quantum compression may capture non-classical correlations in MRI data
- Trash qubits provide interpretable compression bottleneck
- Angle encoding preserves continuous-valued image information
- Variational circuits trainable on near-term quantum hardware

## Implementation
- Angle encoding for image patches
- Parameterized quantum circuits (encoder + decoder)
- Classical optimizer for variational parameters
- Reconstruction threshold for anomaly classification

## Activation
quantum autoencoder, MRI anomaly detection, trash qubits, compression anomaly detection, brain MRI quantum, angle encoding