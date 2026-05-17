---
name: photonic-qnn-hilbert-expansion
description: >
  Implement deep quantum neural networks on integrated photonic platforms using
  Hilbert space expansion via input replication and mode expansion for effective
  nonlinear activation without ancillary qubits. Use when designing photonic QNNs,
  implementing nonlinear quantum activation functions, building energy-efficient
  quantum deep learning systems, creating scalable photonic quantum circuits for
  machine learning, or optimizing quantum neural network expressivity.
---

## Overview

Photonic quantum neural networks (QNNs) offer energy-efficient computation with
programmability and scalability. The core challenge is implementing non-unitary,
nonlinear activation functions on linear quantum photonic systems.

## Core Insight: Hilbert Space Expansion

Traditional QNNs use ancillary qubits + measurement for nonlinearity, incurring
high resource costs and poor cascadability. Instead:

```
Input → Replicate + Mode Expansion → Expanded Hilbert Space → Nonlinear Effect
```

- Replicate input modes to create larger effective Hilbert space
- Use mode expansion to enable effective non-unitary transformations
- Nonlinearity emerges from the expanded space structure, not measurement
- Eliminates need for physical ancillary qubits and measurement devices

## Architecture

### Input Layer
- Encode classical data into photonic qubit states
- Use amplitude or phase encoding depending on task
- Replicate input modes for expansion

### Hidden Layers
- Each layer is a programmable interferometric network
- Use Mach-Zehnder interferometer (MZI) meshes for unitary operations
- Apply mode expansion between layers for effective nonlinearity
- Two-hidden-layer architecture demonstrated in hardware

### Output Layer
- Measure output modes for task-specific predictions
- For classification: softmax over measurement probabilities
- For generation: sample from output distribution

## Hardware Implementation

### Photonic Chip Components
- **Entanglement sources**: High-quality spontaneous four-wave mixing (SFWM) sources
- **Programmable interferometer**: Reconfigurable MZI mesh
- **Detectors**: Single-photon detectors for readout
- **Phase shifters**: Thermal or electro-optic for programmability

### Key Advantages Over Traditional QNN
1. **No ancillary qubits**: Reduced resource cost
2. **No measurement-induced consumption**: Qubits not destroyed
3. **Excellent cascadability**: Layers stack naturally
4. **Dimension-enhanced expressivity**: More expressive than same-size traditional QNN

## Training Protocol

1. Initialize circuit parameters randomly or with domain knowledge
2. Use gradient-based optimization (parameter-shift rule)
3. For classical tasks: backprop through measurement expectation values
4. Monitor expressivity: compare output distribution coverage vs classical baseline

## Tasks Demonstrated

- Nonlinear classification
- Image generation
- Quantum Gibbs state preparation
- Pattern recognition

## Performance Metrics

- **Expressivity**: Compare output space coverage with traditional QNN of same size
- **Resource cost**: Count qubits, measurement devices, overhead components
- **Scalability**: How architecture complexity grows with problem size
- **Fidelity**: State preparation accuracy for quantum tasks

## Activation
- photonic quantum neural network, photonic QNN, quantum photonics ML
- Hilbert space expansion, mode expansion, nonlinear quantum activation
- integrated photonic chip quantum, MZI mesh quantum, programmable quantum optics
- energy-efficient quantum computing, quantum deep learning hardware
- ancilla-free quantum neural network, cascadable quantum circuit
