---
name: neurotrain-local-learning-snn-benchmarking
description: "Comprehensive survey and open benchmarking framework for local learning rules in Spiking Neural Networks (SNNs). Use when: evaluating SNN training algorithms, comparing local vs backprop learning rules, selecting biologically-plausible learning methods for neuromorphic hardware, benchmarking SNN performance across tasks, or researching energy-efficient neural network training. Trigger: neurotrain, local learning rules, SNN benchmarking, surrogate gradient, eligibility traces, Hebbian learning SNN, biologically-plausible training, neuromorphic training, SpikingJelly training, Three-Phase learning. arXiv: 2605.15058 (May 2026)"
---

# NeuroTrain: Open Benchmarking Framework for Local Learning in SNNs

## Overview

NeuroTrain (arXiv:2605.15058, May 2026) provides the first unified benchmarking framework for local learning rules in Spiking Neural Networks. It systematically compares biological-inspired local learning methods against backpropagation-based approaches across diverse tasks, datasets, and architectures.

## Key Findings

### Local Learning Rule Taxonomy

Local learning rules are categorized into three families:

1. **Hebbian-Based Rules**: STDP, BCM, Oja's rule variants
2. **Three-Phase Learning**: Local error signals via forward-forward, equilibrium propagation, predictive coding
3. **Eligibility Trace Methods**: e-prop, DECOLLE, SuperSpike variants

### Benchmark Results

- **Surrogate gradient backpropagation** still achieves highest accuracy on most benchmarks
- **Three-phase learning** (Forward-Forward, Equilibrium Propagation) narrows the gap significantly on classification tasks
- **Eligibility trace methods** (e-prop) excel at temporal tasks and spatio-temporal pattern recognition
- **Hebbian methods** remain competitive for unsupervised feature learning and energy-constrained settings

### Key Insights

- No single local learning rule dominates across all task types
- Task-structure matching is critical: temporal tasks favor eligibility traces, spatial tasks favor three-phase learning
- Hardware deployment considerations ( Loihi 2, SpiNNaker 2) strongly influence rule selection
- Energy-accuracy tradeoff curves reveal local rules can achieve 90-95% of backprop accuracy at fraction of energy cost

## When to Use

### Select Local Learning When:

- Deploying on neuromorphic hardware without backprop support
- Energy efficiency is primary constraint (edge/IoT deployment)
- Online/continual learning scenarios where batch training is infeasible
- Biological plausibility requirement exists

### Rule Selection Guide:

| Task Type | Recommended Rule | Rationale |
|-----------|-----------------|-----------|
| Image classification | Three-Phase (FF/EP) | High accuracy, spatial processing |
| Temporal pattern recognition | Eligibility Traces (e-prop) | Native temporal credit assignment |
| Unsupervised feature learning | Hebbian/STDP variants | No labels required, online |
| Continual learning | Three-Phase + consolidation | Catastrophic forgetting mitigation |

## Implementation Resources

### Core Libraries

- **SpikingJelly**: Primary framework for SNN training with surrogate gradients
- **Norse**: PyTorch-native SNN with local learning support
- **Lava-Loihi**: Intel's framework for neuromorphic deployment

### Key Parameters for Reproduction

- Neuron model: LIF (Leaky Integrate-and-Fire) with reset-by-subtraction
- Surrogate function: Arctangent or Multi-Gaussian for gradient estimation
- Time steps: 10-50 for static images, 100+ for temporal tasks
- Learning rate scheduling: cosine annealing with warmup

## Comparison with Existing Surveys

This benchmark extends beyond previous SNN surveys by:
- Providing standardized evaluation protocol across 8 datasets
- Including hardware deployment metrics (energy, latency)
- Comparing 12+ local learning methods in unified codebase
- Releasing reproducible benchmark suite

## Activation Keywords

- neurotrain
- local learning rules SNN
- SNN benchmarking
- surrogate gradient comparison
- eligibility traces spiking
- three-phase learning
- biologically-plausible SNN training
- neuromorphic hardware training
- spikingjelly benchmark
