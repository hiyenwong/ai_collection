---
name: sqdr-cnn-spiking-quantum
description: SQDR-CNN methodology — joint training of convolutional SNNs and quantum circuits with surrogate gradient and quantum data-reupload for parameter-efficient hybrid models.
category: ai_collection
---

# SQDR-CNN: Spiking-Quantum Data Re-upload Convolutional Neural Network

## Overview

SQDR-CNN is a parameter-efficient hybrid architecture that enables **joint training** of convolutional Spiking Neural Networks (SNNs) and quantum circuits within a single backpropagation framework, using **surrogate gradients** and **quantum data-reupload**.

**Source**: arXiv:2512.03895 (Published in PeerJ Computer Science, 2026)
**Authors**: Luu Trong Nhan, Luu Trung Duong, Pham Ngoc Nam, Truong Cong Thang

## Core Methodology

### 1. Joint Backpropagation Framework
- Unlike prior SQNN implementations requiring **pretrained SNN encoders**, SQDR-CNN trains end-to-end
- Convolutional SNN encoder + quantum circuit share gradients
- **Surrogate gradient** technique makes non-differentiable spiking activity trainable
  - Uses smooth approximation (e.g., sigmoid, fast sigmoid) of Heaviside spike function
  - Gradient flows through spike generation during backprop

### 2. Quantum Data Re-upload
- Input data is encoded into quantum circuit **multiple times** across layers
- Each re-upload layer applies:
  1. Data encoding (rotation gates based on input features)
  2. Variational ansatz (parameterized entangling gates)
  3. Measurement (expectation values as output)
- Theoretical advantage: single-qubit circuit with N re-uploads ≈ N-qubit expressivity

### 3. Architecture Design
```
Input → ConvSNN (spike encoder) → Flatten spikes → 
  Data Re-upload Layer 1 (encode + variational) → 
  Data Re-upload Layer 2 (encode + variational) → 
  ... → 
  Measurement → Classification
```

### 4. Noise-Robust Training
- Evaluate under **noisy simulated quantum environments**
- Test different training algorithm-initialization combinations
- Deploy on actual quantum hardware (IBM Q)

## Performance Results

- **86% of SOTA SNN baseline accuracy** with only **0.5% of parameters**
- Converges without pretrained spiking encoders
- Works without dataset subsetting
- Robust under noisy quantum simulation

## Implementation Steps

1. **ConvSNN encoder design**:
   - Convolutional layers with spiking neurons (LIF or Izhikevich)
   - Surrogate gradient function for backprop (e.g., straight-through estimator)
   - Temporal dimension: simulate over T timesteps

2. **Quantum circuit design**:
   - Choose number of qubits based on flattened spike features
   - Design data re-upload schedule (how many times to re-encode)
   - Select variational ansatz (RY-RZ-CNOT ladder, etc.)

3. **Hybrid training loop**:
   - Forward: SNN → spikes → quantum encoding → measurement
   - Backward: classical loss → quantum gradient (parameter-shift) → SNN surrogate gradient
   - Use hybrid optimizers (Adam for classical, gradient descent for quantum)

4. **Noise simulation**:
   - Add depolarizing, dephasing, or amplitude damping noise
   - Use IBM Qiskit noise models for realistic simulation

## Pitfalls

- **Surrogate gradient choice**: Different functions (sigmoid, arctan, triangle) significantly affect training stability
- **Temporal steps**: Too few → poor SNN dynamics; too many → slow training
- **Data re-upload depth**: More layers = more expressivity but also more noise sensitivity
- **Qubit-feature matching**: Number of features may exceed available qubits — use dimensionality reduction
- **Pretraining dependency**: Prior SQNN required pretrained SNN; SQDR-CNN removes this but needs careful initialization
- **Hardware deployment**: Real quantum devices have limited qubits and high error rates

## Activation Keywords

spiking quantum neural network, SQNN, surrogate gradient, quantum data-reupload, hybrid quantum-classical, SNN backpropagation, convolutional SNN, parameter-efficient, neuromorphic quantum, joint training, SQDR-CNN, noise-robust quantum

## References

- arXiv:2512.03895 — Parameter efficient hybrid spiking-quantum convolutional neural network with surrogate gradient and quantum data-reupload
- PeerJ Computer Science 12 (2026): e3554
