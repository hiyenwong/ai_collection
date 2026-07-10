---
name: merlin-photonic-qml
description: "MerLin discovery engine for photonic and hybrid quantum machine learning. Embeds linear optical circuit simulation into PyTorch/scikit-learn for end-to-end differentiable training of quantum layers. Use when: (1) building hybrid quantum-classical ML models, (2) reproducing photonic QML benchmarks, (3) designing quantum layer architectures, (4) benchmarking QML against classical baselines, (5) hardware-aware quantum ML testing. Activation: merlin, photonic qml, hybrid quantum machine learning, quantum benchmarking, photonic simulation, quantum layer, end-to-end quantum training."
metadata:
  arxiv_id: "2602.11092"
  published: "2026-02-11"
  authors: "Cassandre Notton, Benjamin Stott, Philippe Schoeb"
  tags: [quantum, machine-learning, photonic, benchmarking, pytorch, hybrid]
---

# MerLin: Photonic & Hybrid QML Discovery Engine

## Core Concept

MerLin integrates optimized strong simulation of linear optical circuits into standard PyTorch and scikit-learn workflows, enabling end-to-end differentiable training of quantum layers within established ML ecosystems.

## Architecture Patterns

### 1. Quantum Layer in PyTorch Pipeline

```
Classical Preprocessing → Quantum Layer (linear optical) → Classical Postprocessing → Loss
```

- Quantum layers are differentiable via strong simulation
- Gradients flow through quantum circuits back to classical layers
- Use PennyLane-compatible interfaces for circuit definition

### 2. Hybrid Transfer Learning

- Pre-train classical feature extractor (ResNet, ViT, etc.)
- Freeze early layers, replace final layer with quantum circuit
- Fine-tune only quantum layer parameters + final classical layer
- Benefits from classical pretraining + quantum expressivity

### 3. Photonic QML Reproduction

MerLin reproduces 18 SOTA photonic/hybrid QML works across:
- Kernel methods
- Reservoir computing
- Convolutional and recurrent architectures
- Generative models
- Modern training paradigms

## Methodology

### Step 1: Define Quantum Circuit
- Use parameterized linear optical circuits
- Define encoding scheme (amplitude, phase, etc.)
- Specify measurement operators

### Step 2: Embed in ML Pipeline
- Wrap quantum circuit as differentiable module
- Connect to PyTorch autograd
- Enable gradient flow through simulation

### Step 3: Train End-to-End
- Standard PyTorch training loop
- Adam/SGD optimizer
- Mini-batch compatible

### Step 4: Benchmark
- Compare against classical baselines
- Test on same datasets
- Report parameter efficiency, accuracy, training time

## Hardware-Aware Features

- Simulate beyond current hardware capabilities
- Test on available quantum hardware
- Co-design: algorithms ↔ benchmarks ↔ hardware

## Pitfalls

- **Simulation cost**: Strong simulation scales exponentially with qubit count; limit to ~20-25 qubits
- **Gradient noise**: Quantum layer gradients can be noisy; use larger batch sizes
- **Barren plateaus**: Deep quantum circuits suffer from vanishing gradients; keep circuits shallow
- **Encoding bottleneck**: Poor data encoding limits quantum advantage; experiment with multiple encoding schemes

## References

- arXiv: 2602.11092v2
- Framework: MerLin (open-source)
- Reproduced works: 18 SOTA photonic/hybrid QML papers
