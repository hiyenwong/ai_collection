---
name: canonical-quantization-neurons
category: quantum-computing
description: Canonical quantization methodology for constructing quantum neuron models from classical Hamiltonians — a principled framework for quantum machine learning primitives
trigger_words: canonical quantization, quantum neurons, quantum machine learning, activation observable, Hamiltonian simulation, power of one qumode, Schroedingerization, quantum function approximation
arxiv_id: "2607.05000"
date: "2026-07-07"
---

# Canonical Quantization of Neurons

## Paper
**Title:** Canonical quantization of neurons
**arXiv:** 2607.05000
**Date:** 2026-07-06
**Category:** quant-ph, cs.LG

## Core Methodology

Applies canonical quantization — a systematic procedure for constructing quantum models from classical Hamiltonians — to the fundamental ML primitive: the neuron.

### Key Innovation
- **Neuron as composition:** Views a neuron as composition of an energy function and an activation function
- **Quantization step:** Replaces energy function with quantum Hamiltonian and applies activation function through matrix functional calculus
- **Activation observable:** Results in an activation observable that can be measured on input quantum state
- **Function approximation:** Learns unknown observable from labeled quantum data

### Training Algorithms
Hybrid quantum-classical algorithms for:
- **Measuring activation observable** using: power of one qumode, Schroedingerization
- **Gradient estimation** using: classical random sampling, Hadamard test, Hamiltonian simulation
- **Squared loss error** estimation via quantum algorithms

### Results
- Quantized neurons exhibit enhanced expressive capabilities vs classical neurons
- Principled framework for constructing quantum ML primitives
- Foundation for quantum neural architectures

## Implementation Pattern
```
1. Define classical neuron: σ(E(x)) where E is energy, σ is activation
2. Quantize energy: E → Ĥ (quantum Hamiltonian)
3. Apply activation via matrix functional calculus: σ(Ĥ)
4. Measure activation observable on input quantum state |ψ⟩
5. Train using hybrid quantum-classical optimization
```

## Reusable Patterns
- **Canonical quantization as design principle:** Systematic procedure for quantum ML primitives
- **Matrix functional calculus for activation:** Applying nonlinear functions to quantum operators
- **Hybrid training primitives:** Hadamard test, power of one qumode, Schroedingerization
- **Observable-based learning:** Learning unknown observables from labeled quantum data
