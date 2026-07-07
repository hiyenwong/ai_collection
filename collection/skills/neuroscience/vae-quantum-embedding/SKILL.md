---
name: vae-quantum-embedding
description: "Variational Autoencoder (VAE) framework for learning task-specific quantum embeddings of classical data. Compresses high-dimensional datasets (including ImageNet) into compact quantum representations (e.g., 13-qubit) while remaining reconstructable through a learned decoder. Achieves polynomial-measurement reconstruction (vs. full tomography for amplitude embeddings or circuit inversion for angle embeddings). Validated on IBM quantum hardware with stable embeddings under real device noise. Use when encoding classical data for quantum machine learning, designing quantum data embeddings, or building quantum autoencoders."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2606.26312"
  published: "2026-06-24"
  authors: "Aldo Lamarre, Dominik Šafránek"
  tags: [quantum, machine-learning, vae, data-encoding, quantum-embedding, autoencoder, image-classification]
---

# VAE-Based Task-Specific Quantum Embeddings for QML

## Paper Summary

**Title**: Tailor Made Embeddings for Quantum Machine Learning
**arXiv**: 2606.26312
**Date**: June 24, 2026
**Authors**: Aldo Lamarre, Dominik Šafránek

## Core Innovation

Autoencoders transformed classical ML by solving the curse of dimensionality, enabling principled weight initialization and learning compact, structured representations. This paper **extends the autoencoder paradigm to quantum machine learning** by introducing a **variational autoencoder (VAE) framework** that learns **task-specific quantum embeddings** of classical data.

### Key Achievements

- **ImageNet compressed into 13-qubit quantum representation** while remaining reconstructable
- **MNIST (3 vs 5): 98.5% validation accuracy** using circuit-centric quantum classifier
  - Within 1.2 percentage points of classical NN baseline (99.7%)
  - **30+ percentage points above naive amplitude-embedding** approach
- **Polynomial-measurement reconstruction** — unlike amplitude embeddings (full tomography) or angle embeddings (circuit inversion)
- **Validated on IBM quantum hardware** — stable and reconstructable under real device noise

## Architecture

### VAE Framework

```
Classical Data → Encoder VQC → Quantum Latent State → Decoder VQC → Reconstructed Data
                      ↓                ↓
                 Task-specific     Compact quantum
                 features           representation
```

### Comparison with Standard Embeddings

| Embedding Type | Qubit Requirements | Reconstruction | Stability |
|---------------|-------------------|----------------|-----------|
| **Amplitude** | O(2^n) for n features | Full quantum state tomography | Poor under noise |
| **Angle** | O(n) for n features | Circuit inversion (restrictive) | Moderate |
| **VAE (Proposed)** | Task-specific (learned) | **Polynomial measurements** | **Stable on hardware** |

### Key Advantages

1. **Dimensionality Reduction**: Learns the minimum qubits needed for the task
2. **Task-Specific**: Embeddings are optimized for the downstream classification task
3. **Reconstructable**: Original data recoverable from polynomial number of measurements
4. **Hardware-Validated**: Stable under real quantum device noise

## Implementation

### Training Pipeline

```python
# 1. Classical encoder → quantum latent
def encode_to_quantum(x, encoder_params):
    """Map classical data x to quantum state via parameterized circuit."""
    # Use angle encoding for input features
    state = angle_encoding(x)
    # Apply variational encoder circuit
    state = variational_circuit(state, encoder_params)
    return state

# 2. Quantum decoder → classical reconstruction
def decode_to_classical(quantum_state, decoder_params, n_measurements):
    """Reconstruct classical data from quantum state via measurements."""
    # Perform polynomial number of measurements
    measurements = measure_observables(quantum_state, decoder_params, n_measurements)
    # Classical post-processing
    reconstruction = classical_decoder(measurements, decoder_params)
    return reconstruction

# 3. Joint training
def train_vae(x, encoder_params, decoder_params, task_classifier):
    """Joint optimization of encoder, decoder, and task classifier."""
    q_state = encode_to_quantum(x, encoder_params)
    recon = decode_to_classical(q_state, decoder_params)
    pred = task_classifier(q_state)
    
    loss = reconstruction_loss(x, recon) + task_loss(y, pred)
    return loss
```

### Polynomial Measurement Strategy

Unlike amplitude embedding (requires O(4^n) measurements for full tomography):

```python
def polynomial_measurement(quantum_state, observable_set):
    """
    Reconstruct data using only polynomial number of measurements.
    Key insight: not all observables are needed — only task-relevant ones.
    """
    results = {}
    for obs in observable_set:  # |observable_set| = poly(n)
        results[obs] = expectation_value(quantum_state, obs)
    return results
```

### Hardware Validation

- **Platform**: IBM quantum hardware
- **Result**: Learned embeddings remain stable and reconstructable under real device noise
- **Implication**: VAE embeddings are more robust than naive embedding strategies on NISQ devices

## Performance Results

### MNIST Classification (3 vs 5)

| Method | Accuracy | Notes |
|--------|----------|-------|
| VAE + Circuit-centric QNN | **98.5%** | Task-specific embedding |
| Classical NN baseline | 99.7% | Upper bound |
| Amplitude embedding QNN | ~68% | Naive approach |

### ImageNet Compression

- **Input**: High-dimensional ImageNet features
- **Quantum latent**: 13-qubit representation
- **Reconstruction**: Faithful via polynomial measurements

## When to Use

- **High-dimensional data compression**: Reduce classical data to compact quantum representation
- **Task-specific QML**: Optimize embeddings for specific classification tasks
- **Hardware deployment**: Need embeddings stable under NISQ device noise
- **Reconstruction needed**: Must be able to recover classical data from quantum state

## Activation Keywords

- VAE quantum embedding, task-specific quantum embedding
- quantum autoencoder encoding
- quantum data compression
- polynomial measurement reconstruction
- ImageNet quantum representation
- quantum classifier embedding
- quantum encoder decoder
- quantum representation learning

## Pitfalls

- **Training complexity**: Joint optimization of encoder, decoder, and classifier — may require careful initialization
- **Measurement selection**: Choosing the right observable set for polynomial reconstruction is critical
- **Circuit depth**: Deep encoder/decoder circuits may be hard to train on hardware
- **Task specificity**: Embeddings are task-specific — may not transfer well to different tasks without retraining
- **Hardware noise**: While more robust than naive methods, noise still affects performance — consider error mitigation

## Resources

- arXiv:2606.26312 — "Tailor Made Embeddings for Quantum Machine Learning"
- PennyLane/Qiskit for VQC implementation
- IBM Quantum hardware for validation

## Related Skills

- `quantum-autoencoder-anomaly-detection` — QAE for anomaly detection via compression
- `fid-quantum-autoencoder-fraud` — Fidelity-driven QAE for anomaly detection
- `qml-feature-encoding` — QML feature encoding survey
- `quantum-ml-data-loading` — Quantum ML data loading optimization
- `hybrid-quantum-classical-framework` — Hybrid quantum-classical computing patterns