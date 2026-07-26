---
name: stochastic-quantum-spiking-neural-networks
title: Stochastic Quantum Spiking Neural Networks with Quantum Memory and Local Learning
description: Novel stochastic quantum spiking (SQS) neuron model with multi-qubit quantum circuits for internal quantum memory, enabling event-driven probabilistic spike generation and hardware-friendly local learning without backpropagation.
authors: ["Jiechen Chen", "Bipin Rajendran", "Osvaldo Simeone"]
arxiv_id: "2506.21324"
categories: ["quantum-computing", "neuromorphic-computing", "spiking-neural-networks", "quantum-machine-learning"]
date: "2026-07-23"
version: "1.0"
---

# Stochastic Quantum Spiking Neural Networks with Quantum Memory and Local Learning

## Overview
This methodology proposes a novel stochastic quantum spiking (SQS) neuron model that addresses key limitations of existing quantum spiking models. The SQS neuron uses multi-qubit quantum circuits to realize spiking units with internal quantum memory, enabling event-driven probabilistic spike generation in a single shot during inference. Networks of SQS neurons (SQSNN) can be trained via hardware-friendly local learning rules, eliminating the need for global classical backpropagation.

## Core Methodology

### SQS Neuron Architecture
- **Multi-qubit quantum circuits**: Realize internal quantum memory mechanisms beyond single-qubit classical memory
- **Single-shot inference**: Event-driven probabilistic spike generation without repeated measurements
- **Quantum memory integration**: Internal state preservation through quantum coherence and entanglement
- **Hardware-friendly design**: Compatible with neuromorphic integrated sensing and communications (N-ISAC)

### SQS Neural Networks (SQSNN)
- **Local learning rules**: Hardware-friendly training without global backpropagation
- **Event-driven computation**: Energy consumption only upon input events
- **Tensor-product composition**: Exponential state space growth with qubit count
- **Superposition and entanglement**: Quantum states across basis states and subsystems

### Training Methodology
- **Local learning rule**: Eliminates need for conventional backpropagation
- **Parameter efficiency**: Improved performance when fixing total trainable parameters
- **Hardware compatibility**: Designed for implementation on quantum neuromorphic platforms

## Applications

### Neuromorphic Integrated Sensing and Communications (N-ISAC)
- Event-driven applications requiring real-time processing
- Low-power quantum neuromorphic systems
- Hybrid quantum-classical edge computing

### Time Series Processing
- Efficient temporal data processing through sparse, event-driven computation
- Quantum-enhanced pattern recognition in time series
- Real-time decision making with quantum speedup

### Quantum Machine Learning
- Parameter-efficient quantum neural networks
- Hardware-native quantum ML architectures
- Hybrid quantum-classical learning systems

## Implementation Guidelines

### System Requirements
- Multi-qubit quantum processor with circuit capabilities
- Event-driven input interface compatible with neuromorphic sensors
- Quantum memory coherence preservation mechanisms
- Local learning rule implementation infrastructure

### Key Components
- **SQS neuron units**: Multi-qubit circuits with quantum memory
- **Network connectivity**: Spiking neural network topology
- **Local learning rules**: Hardware-implemented weight updates
- **Event-driven I/O**: Sparse input/output processing

### Performance Optimization
- **Qubit allocation**: Balance between memory capacity and computational overhead
- **Circuit depth**: Minimize decoherence while maintaining functionality  
- **Learning rate tuning**: Optimize local learning rule convergence
- **Event sparsity**: Leverage sparse computation for energy efficiency

## Verification Steps

1. **Single-shot inference validation**: Confirm probabilistic spike generation without repeated measurements
2. **Quantum memory functionality**: Verify internal state preservation through quantum operations
3. **Local learning convergence**: Demonstrate training effectiveness without backpropagation
4. **Performance comparison**: Benchmark against classical and previous quantum spiking models
5. **Parameter efficiency analysis**: Validate improved performance with fixed parameter count

## Experimental Results
- **Superior performance**: SQSNN outperforms previous quantum spiking neural networks
- **Classical comparison**: Better performance than classical counterparts with same parameter count
- **Dataset validation**: Tested on both conventional and neuromorphic datasets
- **Application suitability**: Highlighted potential for N-ISAC applications

## Activation Keywords
stochastic quantum spiking, SQS neuron, quantum memory, local learning, neuromorphic computing, event-driven, single-shot inference, quantum neural networks, N-ISAC, backpropagation-free, multi-qubit circuits, tensor-product composition

## References
- arXiv:2506.21324 [cs.NE]
- DOI: 10.48550/arXiv.2506.21324
- Published in IEEE Journal on Selected Areas in Communications
- Subjects: Neural and Evolutionary Computing, Machine Learning