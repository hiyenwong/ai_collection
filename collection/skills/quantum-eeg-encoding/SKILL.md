---
name: quantum-eeg-encoding
description: >
  Quantum-EEGNet (QEEGNet) methodology for hybrid quantum-classical EEG signal encoding
  and classification. Combines classical EEGNet convolutional architecture with quantum
  variational layers for enhanced cross-task and cross-dataset generalization. Use when:
  designing hybrid quantum-classical neural networks for EEG/brain signals, implementing
  quantum layers in biomedical signal processing, optimizing quantum advantage in
  neuroimaging, or building cross-dataset EEG encoders. Triggers: QEEGNet, quantum EEG,
  quantum brain signal, quantum biomedical, quantum-classical hybrid neural network,
  EEG quantum layers, variational quantum EEG.
---

# Quantum-EEGNet (QEEGNet) Methodology

Hybrid quantum-classical architecture for EEG encoding derived from arXiv:2503.00080.

## Architecture

```
Raw EEG → EEGNet (Conv layers) → Feature Embeddings → Quantum Variational Layer → Classification
```

### EEGNet Backbone

Standard EEGNet components:
1. Temporal convolution (1D filters for frequency analysis)
2. Depthwise spatial convolution (captures spatial patterns across electrodes)
3. Separable convolution (temporal + spatial separation)
4. Output: compact feature embeddings

### Quantum Variational Layer

- Encodes EEGNet embeddings into quantum states
- Applies parameterized quantum gates (variational circuit)
- Measures quantum state for classical output
- Circuit depth and qubit count must balance expressivity vs. trainability

## Key Findings

1. **Cross-task generalization**: QEEGNet tested on cognitive and motor task datasets
2. **Cross-dataset transfer**: Performance varies across different EEG datasets
3. **Optimization challenge**: Hybrid architectures require careful tuning to achieve
   quantum advantage over purely classical baselines
4. **Parameter efficiency**: Quantum layers can achieve comparable results with
   fewer classical parameters, but quantum circuit training adds complexity

## Implementation Guide

### Step 1: Prepare EEG Data

```python
# Standard EEG preprocessing
- Bandpass filter (0.5-50 Hz typical)
- Epoch extraction around events
- Baseline correction
- Standardization per channel
```

### Step 2: Build EEGNet Encoder

```python
# Standard EEGNet architecture
# Input: (batch, channels, time)
# Output: (batch, embedding_dim)
```

### Step 3: Add Quantum Layer

```python
# Encode embeddings into quantum states
# Use angle encoding or amplitude encoding
# Design variational circuit with trainable parameters
# Measure observables for classification
```

### Step 4: Hybrid Training

```python
# Loss = classical_loss(quantum_output, targets)
# Gradients flow through quantum layer (parameter-shift rule)
# Optimize classical + quantum parameters jointly
```

## Pitfalls

- **Barren plateaus**: Deep quantum circuits suffer from vanishing gradients
- **Cross-dataset gap**: Models trained on one EEG dataset may not generalize
- **Quantum simulation overhead**: Classical simulation of quantum layers is slow
- **Noise sensitivity**: Real quantum hardware adds noise that can degrade EEG features

## Related Skills

- `quantum-neuroscience-patterns`: Broader quantum neuroscience methodology
- `quantum-eeg-foundation`: Quantum-enhanced EEG signal analysis
