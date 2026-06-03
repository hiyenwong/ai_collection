---
name: spiking-phase-quantum-encoding
description: SPATE methodology for quantum machine learning — spiking-phase adaptive temporal encoding that converts real-valued features into LIF spike trains and maps spike statistics to quantum rotations.
category: ai_collection
---

# SPATE: Spiking-Phase Adaptive Temporal Encoding for Quantum Machine Learning

## Overview

SPATE (Spiking-Phase Adaptive Temporal Encoding) is a spike-driven temporal encoding method for Quantum Machine Learning (QML) that addresses the limitation of static encodings (angle/amplitude maps) in handling temporal information.

**Source**: arXiv:2604.11022 (Accepted at IJCNN 2026)
**Authors**: Nouhaila Innan, Rachmad Vidya Wicaksana Putra, Muhammad Shafique

## Core Methodology

### 1. Spike Train Generation
- Convert real-valued tabular features into **Leaky Integrate-and-Fire (LIF)** spike trains
- Each feature becomes a temporal spike pattern rather than a static value
- Temporal dynamics capture feature relationships over time

### 2. Spike-to-Phase Mapping
- Map spike statistics (firing rate, timing, inter-spike intervals) to **quantum rotation angles**
- Use controlled phase operations to encode temporal structure
- Augment with a small set of **temporal qubits** that track spike history

### 3. Encoding-Centric Evaluation Protocol
Assess representation quality independently of the classifier:
- **CKTA** (Centered Kernel-Target Alignment): Measures alignment with target kernel
- **Fisher separability**: Class separation in feature space
- **Inter/intra-class distance ratios**: Discriminative power
- **Silhouette score**: Cluster quality
- **Normalized entropy**: Information content
- **TVpair collapse indicators**: Detect representation collapse

### 4. Hybrid QNN Integration
- SPATE features feed into variational quantum circuits
- Works within fixed qubit budget constraints
- Compatible with any QML classifier architecture

## Performance Results

| Dataset | CKTA (SPATE) | CKTA (Angle) | Fisher (SPATE) | Fisher (Angle) |
|---------|-------------|-------------|---------------|---------------|
| Blobs   | 0.966       | 0.632       | 7.37          | 0.70          |
| Moons   | 0.506       | 0.015       | -             | -             |

| Task    | Accuracy | AUC    |
|---------|----------|--------|
| Wine    | 0.826    | 0.978  |
| Moons   | 0.840    | 0.923  |

## Implementation Steps

1. **Feature normalization**: Scale features to [0, 1] range
2. **LIF neuron simulation**: Convert each feature to spike train using LIF dynamics
   - Membrane potential: τ·dV/dt = -(V - V_rest) + R·I(t)
   - Spike when V > V_threshold, then reset
3. **Spike statistics extraction**: Compute firing rate, mean ISI, coefficient of variation
4. **Phase encoding**: Map statistics to quantum rotation gates R_z(θ)
5. **Temporal qubits**: Add auxiliary qubits with controlled phase operations
6. **Variational circuit**: Apply parameterized quantum circuit on encoded state

## Pitfalls

- **Spike train length**: Too short → loss of temporal info; too long → decoherence
- **LIF parameter tuning**: τ (time constant) and V_threshold must be calibrated per dataset
- **Temporal qubit overhead**: Each temporal qubit doubles circuit depth — use sparingly
- **CKTA computation**: O(n²) in number of data points — use subsampling for large datasets
- **Noisy hardware**: Real quantum devices may degrade SPATE advantages — use error mitigation

## Activation Keywords

spike encoding, quantum machine learning, temporal encoding, LIF neuron, spiking neural network, QML encoding, phase encoding, quantum feature representation, SPATE, spike-to-phase, variational quantum circuit, quantum data encoding, IJCNN, neuromorphic quantum, spike train, leaky integrate-and-fire

## References

- arXiv:2604.11022 — SPATE: Spiking-Phase Adaptive Temporal Encoding for Quantum Machine Learning
