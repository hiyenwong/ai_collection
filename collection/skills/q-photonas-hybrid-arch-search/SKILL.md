---
name: q-photonas-hybrid-arch-search
description: Q-PhotoNAS methodology — Hybrid Quantum Neural Architecture Search framework for photonic quantum-classical models using genetic algorithm-based NAS with learnable quantum phase encoding.
category: quantum-computing
version: 1.1.0
tags: [quantum, nas, photonic, qml, architecture-search, hybrid-quantum-classical, genetic-algorithm]
trigger: quantum architecture search, photonic quantum computing, Q-PhotoNAS, quantum NAS, hybrid quantum neural architecture, quantum phase encoding, genetic algorithm quantum, photonic QPU, Quandela
---

# Q-PhotoNAS: Hybrid Quantum Neural Architecture Search Framework on Photonic Devices

## Source
- arXiv: 2605.22097v1
- Authors: Farah Elnakhal, Alberto Marchisio, Nouhaila Innan, Gabriel Falcao, Muhammad Shafique
- Category: quant-ph

## Overview

Q-PhotoNAS is a neural architecture search (NAS) framework specifically designed for hybrid photonic quantum-classical machine learning models. It addresses the challenge of designing effective architectures that account for the collaboration between classical preprocessing, quantum phase encoding, and photonic circuit structure.

## Core Methodology

### 1. Gene-Based Architecture Encoding

The framework encodes **19 hyperparameters** organized into **6 gene groups**:

| Gene Group | Parameters | Description |
|---|---|---|
| Classical Preprocessing | Number of layers, activation, units | Classical feature extraction |
| Phase Encoding | Encoding type, rotation angles | Quantum data encoding strategy |
| Photonic Circuit | Circuit depth, width, connectivity | Photonic QPU configuration |
| Measurement | Measurement basis, shots | Readout configuration |
| Post-processing | Classical layers after quantum | Hybrid readout processing |
| Training | Learning rate, optimizer, epochs | Training hyperparameters |

### 2. Genetic Algorithm-Based Search

**Evolutionary Strategy:**
- **Population initialization**: Random sampling from the joint design space
- **Group-based crossover**: Crossover operates at gene-group level, preserving coherent architectural blocks
- **Per-gene mutation**: Individual gene mutation within each group
- **Elitism**: Top performers preserved across generations
- **Evaluation budget**: Short training budget for candidate evaluation before full retraining

### 3. Learnable Quantum Phase Encoding

Quantum phase encoding is treated as a learnable component within the search space, allowing the NAS to discover optimal encoding strategies that complement the photonic circuit architecture.

### 4. Quantum Contribution Analysis

Post-search analysis verifies that the photonic layer extracts **non-redundant features orthogonal to the classical pathway**, providing measurable accuracy advantage over classical-only baselines.

## Key Results

| Benchmark | Accuracy | Inference Time (projected) |
|---|---|---|
| Digits | 99.44% | 67 ms (Quandela Ascella QPU) |
| MNIST | 98.78% | 149 ms (Quandela Ascella QPU) |

## When to Use

Use this skill when:
- Designing hybrid quantum-classical ML architectures for photonic devices
- Automating architecture search for quantum neural networks
- Exploring the joint design space of classical preprocessing + quantum circuits
- Evaluating quantum advantage over classical baselines with orthogonal feature extraction
- Working with photonic quantum computing platforms (Quandela, Xanadu, etc.)

## Implementation Steps

1. **Define gene groups**: Encode architecture parameters into 6 logical gene groups
2. **Initialize population**: Sample diverse architectures from the design space
3. **Evaluate candidates**: Short training runs (few epochs) for fitness estimation
4. **Evolve population**: Apply group-based crossover, per-gene mutation, elitism
5. **Full retrain**: Retrain the best-found architecture with full training budget
6. **Validate quantum advantage**: Verify photonic layer contributes orthogonal features
7. **Deploy**: Project inference times on target photonic QPU

## Pitfalls

- Manual architecture tuning fails to account for classical-quantum collaboration
- Without quantum contribution analysis, redundant quantum features waste resources
- Short evaluation budget must be representative — too short leads to false positives
- Hardware constraints (connectivity, coherence) must be encoded in the search space
- Genetic search may converge prematurely — maintain population diversity

## Related Papers

- Q-SpiRL (arXiv:2605.20801) — Quantum spiking reinforcement learning
- Quantum circuit design via dynamic Pauli constraints (arXiv:2605.22744)
- Software Between Quantum and ML — Down to Pulses (arXiv:2605.21286)
