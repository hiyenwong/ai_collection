---
name: hybrid-quantum-neural-phase-recognition
description: "Hybrid quantum-classical neural network for quantum phase recognition - jointly trains shallow parameterized quantum circuit with classical neural network, reduces sample complexity by ~10x, distinguishes topological phases on superconducting hardware"
tags: [quantum, neural-network, phase-recognition, topological-phase, hybrid-quantum-classical, surface-code, sample-efficient, superconducting-hardware, measurement-basis, trainable-transformation]
---

# Hybrid Quantum Neural Network for Phase Recognition

## Paper Summary
**Title**: Hybrid quantum-classical neural network for sample-efficient recognition of topological phases
**arXiv**: 2606.28199 (and companion paper 2606.28201)
**Authors**: Markus K. Hoffmann, Leon C. Sander, Colin Scarato et al. (ETH Zurich / Wallraff group)
**Date**: June 26, 2026

## Core Innovation
A hybrid quantum-classical neural network that combines a shallow parameterized quantum circuit with a classical neural network for sample-efficient recognition of quantum phases. The parameterized quantum circuit performs a nonlocal transformation of the measurement basis, jointly trained with the classical neural network to maximize statistical distance between measurements of different quantum states.

## Key Results

### Sample Efficiency
- **Training sample complexity**: Reduced by ~10x compared to classical neural network on randomized Pauli measurements
- **Inference sample complexity**: Also reduced by ~10x
- **Shallow quantum circuit**: Compatible with existing quantum computers (no deep circuits needed)

### Phase Recognition Performance
- **Topological phase recognition**: Distinguishes surface code topological phase from symmetry-enriched topological phase and random product states
- **Single-shot accuracy**: >85%
- **Averaged accuracy (10 measurements)**: >99%
- **Error resilience**: Distinguishes topological states even with single-qubit Pauli errors

### Hardware Implementation
- **Platform**: Superconducting quantum hardware
- **System size**: Surface code lattices up to 4x4 sites in magnetic field
- **Real hardware loop**: Joint training with actual quantum processor in optimization loop

## Technical Architecture

### Hybrid Neural Network Components
1. **Parameterized Quantum Circuit (PQC)**: Shallow circuit performing nonlocal measurement basis transformation
2. **Measurement layer**: Projects quantum state to classical data
3. **Classical Neural Network**: Feedforward network processing measurement outcomes

### Training Process
- **Joint optimization**: PQC parameters and classical NN weights trained together
- **Objective**: Maximize statistical distance between data from different quantum states
- **Supervised learning**: Labeled examples from known quantum phases

### Advantages Over Pure Classical Approach
- **Nonlocal feature extraction**: Quantum circuit captures nonlocal correlations inaccessible to local measurements
- **Reduced measurement overhead**: Fewer measurements needed for same accuracy
- **Shallow circuit**: No need for deep quantum circuits that exceed coherence times

## When to Use
- Characterizing quantum states on near-term quantum devices
- Recognizing topological phases of matter
- Scenarios where classical methods have unfavorable sample complexity scaling
- Experimental quantum state characterization
- Distinguishing topological from trivial phases

## Implementation Considerations
- Quantum circuit must be shallow enough for hardware coherence times
- Statistical distance metric choice affects training stability
- Measurement basis optimization is key to sample efficiency
- Joint classical-quantual training requires hardware-in-the-loop

## Pitfalls
- Requires access to quantum hardware for training
- Shallow circuit limits expressivity
- Measurement shot noise affects training convergence
- Scaling to larger systems needs further validation

## Related Skills
- `hybrid-quantum-classical-nn` - General hybrid QNN patterns
- `unsupervised-quantum-ml-phase-detection` - Unsupervised phase detection
- `qml-expressivity-trainability` - QNN expressivity analysis
- `quantum-neural-measurement-dynamics` - Measurement dynamics in QNNs

## References
- arXiv:2606.28199 - Sample-efficient phase recognition
- arXiv:2606.28201 - Experimental demonstration on superconducting hardware