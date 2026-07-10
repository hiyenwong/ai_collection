---
name: qnn-survey-design-patterns
description: "Quantum Neural Network (QNN) design patterns and architecture selection guide — comprehensive survey methodology for selecting, designing, and evaluating QNN architectures based on task requirements. Covers fully connected QNNs, quantum CNNs, equivariant QNNs, quantum Hopfield networks, quantum Boltzmann machines, quantum reservoir computing, and composite networks. Activation: QNN survey, quantum neural network design, QNN architecture selection, quantum machine learning survey, 量子神经网络综述"
---

## Overview

Comprehensive QNN design patterns extracted from the survey paper "Research progress on quantum neural networks and quantum machine learning" (arXiv:2605.30724, May 2026). This skill provides a practical decision framework for selecting QNN architectures based on task requirements, hardware constraints, and performance goals.

## arXiv Reference

- **ID**: 2605.30724
- **Title**: Research progress on quantum neural networks and quantum machine learning
- **Authors**: Yifan Sun, Boyuan Sun, Jiameng Tian, Xiangdong Zhang
- **Published**: May 2026
- **Categories**: quant-ph

## QNN Architecture Selection Matrix

### By Task Type

| Task Type | Recommended QNN | Why |
|-----------|----------------|-----|
| Image/Pattern Recognition | Quantum CNN (QCNN) | Hierarchical feature extraction via quantum pooling |
| Sequence/Time-Series | Fully Connected QNN (FC-QNN) | Direct mapping of temporal features to qubits |
| Associative Memory | Quantum Hopfield Network | Quantum superposition enables exponential memory capacity |
| Optimization/Combinatorial | Quantum Boltzmann Machine | Energy-based formulation for combinatorial search |
| Chaotic/Dynamic Systems | Quantum Reservoir Computing | Fixed random quantum circuit, only readout trained |
| Symmetry-Preserving Tasks | Equivariant QNN | Built-in symmetry guarantees via group representations |
| Reinforcement Learning | Composite QNN-RL | QNN as policy/value function approximator |
| Generative Modeling | Composite QNN-GL | Quantum circuits for probability amplitude encoding |
| Transfer Learning | Composite QNN-TL | Pre-trained quantum feature extractors |

### By Resource Constraints

| Constraint | Recommended Approach | Notes |
|------------|---------------------|-------|
| Few qubits (NISQ, <20) | FC-QNN, QRC | Minimal depth circuits |
| Moderate qubits (20-50) | QCNN, Equivariant QNN | Structured ansatze |
| Many qubits (>50) | Full QBM, Deep QNN | Requires error mitigation |
| Limited circuit depth | QRC, FC-QNN shallow | Reservoir has fixed random circuit |
| Can train classically | Hybrid QNN-Classical | Classical optimizer + quantum circuit |

## Key Design Patterns

### Pattern 1: Parameterized Quantum Circuit (PQC) Encoding
```
Classical Data → Encoding Circuit (Rx, Ry, Rz) → Variational Layer → Measurement → Classical Output
```
- **Encoding**: Amplitude, angle, or basis encoding of classical data
- **Variational**: Alternating layers of parameterized single-qubit gates + entangling gates
- **Measurement**: Expectation values of observables as output

### Pattern 2: Quantum Convolution + Pooling
```
Input State → [Quantum Convolution (entangling gates) → Quantum Pooling (measurement + post-selection)]^n → Classification
```
- Hierarchical feature extraction analogous to classical CNN
- Pooling via mid-circuit measurement and qubit reuse

### Pattern 3: Quantum Reservoir Computing
```
Input → Fixed Random Quantum Circuit (reservoir) → Measurement → Classical Readout (trained)
```
- Only the classical readout layer is trained
- Quantum circuit is fixed and random
- Exploits quantum dynamics as rich feature space

### Pattern 4: Hybrid Classical-Quantum
```
Classical NN Feature Extractor → Quantum Circuit (nonlinear transformation) → Classical Classifier
```
- Classical layers extract features
- Quantum circuit provides quantum advantage in feature space
- Classical classifier on measured outputs

## Barren Plateaus Mitigation

The survey identifies barren plateaus as a critical training challenge. Key solutions:

1. **Structured Ansatz Design**: Use problem-inspired ansatze rather than hardware-efficient random circuits
2. **Layer-by-Layer Training**: Train QNN layers sequentially rather than all-at-once
3. **Local Cost Functions**: Use local observables instead of global ones
4. **Parameter Initialization**: Initialize near identity or use classical pre-training
5. **Adaptive Learning Rates**: Use quantum natural gradient or adaptive methods

## Performance Comparison Summary

| QNN Type | Training Speed | Expressivity | NISQ-Friendly | Scalability |
|----------|---------------|-------------|---------------|-------------|
| FC-QNN | Fast | High | Yes | Moderate |
| QCNN | Moderate | High | Yes | Good |
| Equivariant QNN | Slow | Very High | Moderate | Good |
| QHN | Moderate | Very High | Limited | Poor |
| QBM | Slow | Very High | Limited | Poor |
| QRC | Very Fast | Moderate | Yes | Excellent |

## Practical Implementation Guidelines

1. **Start Simple**: Begin with FC-QNN or QRC for proof of concept
2. **Match Symmetry**: Use equivariant QNN when the problem has known symmetries
3. **Consider Data Loading**: The state preparation bottleneck is critical — use neural network encoding (see `nn-quantum-state-encoding` skill) to avoid variational optimization per data point
4. **Hybrid Approach**: For near-term, hybrid classical-quantum architectures are most practical
5. **Monitor Expressivity**: Use effective rank or entanglement entropy to measure QNN expressivity during training
6. **Avoid Barren Plateaus**: Use structured ansatze and local cost functions

## Related Skills

- `nn-quantum-state-encoding` — Neural network encoding for quantum state preparation (arXiv:2605.31006)
- `quantum-neural-barren-plateau` — Barren plateau mitigation techniques
- `quantum-neural-architecture` — General QNN architecture design
- `quantum-reservoir-computing` — Quantum reservoir computing methodology
- `qml-framework-agnostic-design` — Framework-agnostic QML design

## Activation

Use this skill when:
- Designing quantum neural network architectures
- Comparing QNN types for a specific task
- Evaluating quantum machine learning approaches
- Selecting between classical and quantum neural networks
- Surveying QNN literature or writing QNN-related code
