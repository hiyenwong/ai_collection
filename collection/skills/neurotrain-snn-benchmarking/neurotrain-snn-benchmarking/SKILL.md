---
name: neurotrain-snn-benchmarking
description: >
  NeuroTrain survey and benchmarking framework for Spiking Neural Network (SNN) training algorithms.
  Comprehensive taxonomy of SNN training: surrogate-gradient backpropagation, local/three-factor learning,
  biologically inspired plasticity, ANN-to-SNN conversion, and non-standard optimization.
  Includes open-source snnTorch-based unified benchmarking framework.
  Use when: researching SNN training methods, comparing local learning rules, benchmarking spiking networks,
  designing biologically plausible training pipelines, or selecting training algorithms for SNN deployment.
  Keywords: neurotrain, SNN training, local learning rules, surrogate gradient, snnTorch, benchmarking,
  spiking neural network training, three-factor learning, STDP, ANN-to-SNN conversion.
---

# NeuroTrain: SNN Training Survey & Benchmarking Framework

arXiv: 2605.15058 | Caviglia et al. (May 2026)

## Core Contribution

Comprehensive taxonomy of SNN training algorithms + open-source `NeuroTrain` benchmarking framework built on snnTorch.

## Taxonomy of SNN Training Methods

### 1. Surrogate-Gradient Backpropagation
- Replace non-differentiable spike with smooth surrogate for gradient flow
- Key variants: super-spike, sigmoid, arc-tangent, triangle surrogates
- Trade-off: accuracy vs. biological plausibility

### 2. Local Learning Rules
- Synaptic updates use only locally available information
- Includes: Hebbian learning, STDP, three-factor rules
- No global error signal required

### 3. Three-Factor Learning
- Combines pre/post activity with modulatory third factor (reward, error, dopamine-like signal)
- Bridges local learning with global objectives
- Biologically plausible credit assignment

### 4. Biologically Inspired Plasticity
- Homeostatic plasticity, metaplasticity, synaptic scaling
- Incorporates biological constraints for stability

### 5. ANN-to-SNN Conversion
- Train ANN, convert to equivalent SNN via weight scaling/threshold tuning
- High accuracy but latency overhead

### 6. Non-Standard Optimization
- Evolutionary methods, direct reward optimization, gradient-free approaches

## Benchmarking with NeuroTrain Framework

### Setup
```python
import neurotrain  # snnTorch-based framework
# Unified interface for comparing training algorithms
```

### Key Dimensions for Comparison
1. **Learning signal**: global gradient vs. local vs. three-factor
2. **Locality**: weight update depends on pre-synaptic, post-synaptic, and/or modulatory signals
3. **Biological inspiration**: degree of neuroscience grounding
4. **Hardware suitability**: compatibility with neuromorphic chips (Loihi, TrueNorth)
5. **Accuracy-efficiency trade-off**: task performance vs. spike sparsity

## When to Use Which Method

| Scenario | Recommended Approach |
|----------|---------------------|
| Maximum accuracy | Surrogate-gradient backprop |
| Neuromorphic deployment | Local/three-factor learning |
| Biological modeling | Biologically inspired plasticity |
| Quick prototyping | ANN-to-SNN conversion |
| Edge hardware | Non-standard/gradient-free |

## Activation

- neurotrain, SNN training benchmark
- 脉冲神经网络训练, 局部学习规则
- Compare SNN training algorithms
- surrogate gradient, three-factor learning
- snnTorch benchmarking
