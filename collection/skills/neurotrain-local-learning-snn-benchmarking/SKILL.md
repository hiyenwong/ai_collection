---
name: neurotrain-local-learning-snn-benchmarking
description: "NeuroTrain: Open benchmarking framework for surveying local learning rules in Spiking Neural Networks. Enables systematic comparison of biologically-plausible local learning rules (STDP, Hebbian, three-factor, eligibility propagation) on standardized tasks. Activation: local learning rules, SNN benchmarking, NeuroTrain, surrogate gradient comparison, biologically plausible learning, spiking neural network training evaluation."
---

# NeuroTrain: Local Learning Rules SNN Benchmarking

> Open benchmarking framework for systematic evaluation of local learning rules in Spiking Neural Networks.

## Metadata
- **Source**: arXiv:2605.15058
- **Authors**: Alessio Caviglia, Filippo Marostica, Roberta Bardini, Alessandro Savino, Stefano Di Carlo
- **Published**: 2026-05-15

## Core Methodology

### Problem
SNNs support diverse local learning rules (STDP, Hebbian, three-factor, surrogate gradients, eligibility propagation), but no unified framework exists for systematic comparison across tasks, datasets, and evaluation metrics.

### Framework Design
- **Unified API** for plugging in different local learning rules
- **Standardized benchmark suite** covering static images (MNIST, CIFAR), neuromorphic datasets (N-MNIST, N-CALTECH), and temporal tasks
- **Evaluation metrics**: accuracy, energy efficiency, convergence speed, memory footprint
- **Reproducibility**: fixed seeds, standardized preprocessing, consistent network architectures

### Local Learning Rules Covered
1. **STDP variants**: pair-based, triplet, voltage-dependent
2. **Hebbian rules**: Oja's rule, BCM theory
3. **Three-factor rules**: reward-modulated, eligibility trace-based
4. **Surrogate gradient**: differentiable approximations of spike function
5. **Eligibility propagation**: e-prop, local approximations of BPTT

## Implementation Guide

### Architecture Pattern
```
BenchmarkSuite
├── Dataset (static/neuromorphic/temporal)
├── Network Architecture (feedforward/recurrent/convolutional)
├── LearningRule (STDP/Hebbian/three-factor/SG/e-prop)
├── Trainer (handles training loop, logging, evaluation)
└── Metrics (accuracy/energy/convergence/memory)
```

### Key Design Principles
- **Rule-agnostic trainer**: same training loop for all rules
- **Dataset converters**: unified format for rate-coded and event-based data
- **Energy model**: configurable neuromorphic hardware energy estimation
- **Fair comparison**: same hyperparameter search budget per rule

## Applications
- Selecting optimal learning rule for specific SNN deployment scenarios
- Research: systematic analysis of learning rule trade-offs
- Education: comparative study of biologically-plausible learning
- Hardware co-design: matching learning rules to neuromorphic constraints

## Pitfalls
- Local rules often require different hyperparameter ranges — fair comparison needs per-rule tuning
- Event-based datasets need careful temporal binning for rate-coded rules
- Energy estimates depend heavily on assumed hardware ( Loihi vs SpiNNaker vs custom)
- Reproducibility requires fixing random seeds for spike generation, weight initialization, and data ordering

## Related Skills
- snn-learning-survey
- three-factor-snn-learning
- surrogate-gradient-snn-training
- decolle-snn-learning
- spike-driven-large-language-model-sdllm
- spiking-neural-network-analysis
