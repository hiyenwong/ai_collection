---
name: neurotrain-local-learning-snn-benchmarking
description: >
  Comprehensive survey and open benchmarking framework for local learning
  rules in Spiking Neural Networks. Provides unified taxonomy of SNN training
  algorithms: surrogate-gradient backpropagation, local and three-factor
  learning rules, biologically inspired plasticity, ANN-to-SNN conversion,
  and non-standard optimization. Includes NeuroTrain, an open-source
  snnTorch-based benchmarking framework.
  Use when: surveying SNN training methods, implementing local learning rules,
  benchmarking SNN algorithms, comparing surrogate gradients vs local rules,
  three-factor learning, biologically plausible plasticity, reproducible SNN research.
  Keywords: neurotrain, local learning, SNN training, surrogate gradient,
  three-factor learning, snntorch, benchmarking, taxonomy, plasticity rules.
---

# NeuroTrain: Surveying Local Learning Rules for SNNs

**arXiv**: 2605.15058
**Authors**: Alessio Caviglia, Filippo Marostica, Roberta Bardini,
  Alessandro Savino, Stefano Di Carlo

## Problem Statement

The rapid expansion of SNNs has led to a proliferation of training algorithms
that differ widely in biological inspiration, computational structure, and
hardware suitability. The field lacks a unified, fine-grained taxonomy that
systematically organizes these approaches.

## Taxonomy of SNN Training Algorithms

### 1. Surrogate-Gradient Backpropagation
- Uses surrogate functions to approximate spike derivative
- Enables standard backprop through non-differentiable spiking neurons
- Common surrogates: straight-through, sigmoid, triangle, exponential
- Trade-off: performance vs biological plausibility

### 2. Local Learning Rules
- Synaptic updates depend only on pre/post-synaptic activity
- No global error signal required
- Examples: STDP, anti-STDP, Hebbian rules
- Biologically plausible, hardware-friendly

### 3. Three-Factor Learning Rules
- Pre-synaptic × post-synaptic × modulatory signal
- Bridges local plasticity with global objectives
- Modulatory signals: reward, eligibility traces, dopamine-like
- Enables reinforcement learning in SNNs

### 4. Biologically Inspired Plasticity
- Homeostatic plasticity, synaptic scaling
- Metaplasticity (plasticity of plasticity)
- Structural plasticity (connection creation/pruning)
- Short-term plasticity (facilitation, depression)

### 5. ANN-to-SNN Conversion
- Train ANN, convert weights to spiking equivalent
- Preserves performance through rate coding
- Trade-offs: latency, accuracy, energy

### 6. Non-Standard Optimization
- Evolutionary strategies
- Direct policy search
- Meta-learning approaches

## NeuroTrain Benchmarking Framework

### Architecture
- Built on snnTorch
- Unified, modular, extendable design
- Consistent benchmarking across:
  - Datasets (static and neuromorphic)
  - Architectures (CNN, RNN, Transformer)
  - Training regimes

### Key Features
- Implement representative algorithms from each category
- Enable fair comparison with identical experimental setup
- Support custom algorithm extension
- Reproducible research pipelines

## Analysis Dimensions

For each algorithm class, evaluate:
1. **Computational principles**: How learning signals are computed
2. **Learning signals**: What drives synaptic updates
3. **Locality properties**: How much local vs global information is needed
4. **Biological plausibility**: Alignment with neuroscience findings
5. **Hardware suitability**: Compatibility with neuromorphic chips
6. **Scalability**: Performance on large-scale tasks

## Open Challenges

- Scalable local learning for deep networks
- Bridging performance gap with backpropagation
- Hardware-software co-design
- Standardized evaluation benchmarks
- Theoretical foundations for local learning convergence

## When to Apply

- Surveying SNN training landscape
- Selecting appropriate learning rule for a task
- Implementing biologically plausible learning
- Benchmarking new SNN algorithms
- Neuromorphic hardware deployment
- Research on local vs global learning trade-offs
