---
name: spiking-quantum-encoding
description: SPATE (Spiking-Phase Adaptive Temporal Encoding) methodology for quantum machine learning — spike-driven temporal encoding converting real-valued features into quantum rotations. Use when encoding temporal data for quantum ML, designing QML feature maps, or building spiking-quantum hybrid systems.
---

# SPATE: Spiking-Phase Adaptive Temporal Encoding for QML

## Core Concept

Convert real-valued tabular features into leaky integrate-and-fire spike trains and map spike statistics to quantum rotations, augmented with temporal qubits through controlled phase operations.

## Technical Approach

1. **Spike Train Generation**: LIF neuron model converts features to spike trains
2. **Spike Statistics → Quantum Rotations**: Map spike timing/frequency to rotation angles
3. **Temporal Qubits**: Additional qubits encode temporal structure via controlled-phase operations
4. **Evaluation Protocol**: CKTA, Fisher separability, silhouette score, TVpair collapse

## Key Results

- CKTA: 0.966 (SPATE) vs 0.632 (angle encoding) on Blobs
- Fisher score: 7.37 (SPATE) vs 0.70 (angle encoding)
- Wine accuracy: 0.826, AUC: 0.978 with fixed qubit budget
- Moons accuracy: 0.840, AUC: 0.923

## Activation Keywords
- SPATE quantum encoding
- spiking-phase adaptive temporal encoding
- spike-driven quantum feature map
- temporal quantum encoding
- quantum machine learning encoding
- LIF spike quantum rotation
