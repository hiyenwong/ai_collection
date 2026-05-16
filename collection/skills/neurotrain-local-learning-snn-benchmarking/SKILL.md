---
name: neurotrain-local-learning-snn-benchmarking
description: "NeuroTrain methodology for surveying and benchmarking local learning rules in Spiking Neural Networks (SNNs). Comprehensive taxonomy of SNN training algorithms spanning surrogate-gradient backpropagation, local and three-factor learning rules, biologically inspired plasticity mechanisms, ANN-to-SNN conversion pipelines, and non-standard optimization strategies. Use when: designing SNN training algorithms, comparing local learning rules, benchmarking SNN training approaches, implementing biologically plausible learning, or working with snnTorch framework."
---

# NeuroTrain: Local Learning SNN Benchmarking

## Overview

arXiv:2605.15058 | Caviglia, Marostica, Bardini, Savino, Di Carlo (May 2026)

SNNs have proliferated with diverse training algorithms differing in biological inspiration, computational structure, and hardware suitability. NeuroTrain provides a unified taxonomy and open-source benchmarking framework.

## SNN Training Taxonomy

### 1. Surrogate-Gradient Backpropagation
- Replace non-differentiable spike function with smooth surrogate during backward pass
- Common surrogates: sigmoid, arctan, triangular, Gaussian
- Enables gradient-based training while preserving spiking dynamics
- Used in frameworks: snnTorch, SpyTorch, Norse

### 2. Local Learning Rules
- Update rules depend only on pre- and post-synaptic activity (local information)
- Hebbian: strengthen connections between co-active neurons
- Anti-Hebbian: decorrelate neuron responses
- STDP (Spike-Timing Dependent Plasticity): timing-based weight updates

### 3. Three-Factor Learning Rules
- Extend two-factor Hebbian with global modulatory signal (third factor)
- Formula: dw = pre x post x modulator
- Modulators: reward signals, attention, dopamine-like neuromodulators
- Bridge between local plasticity and global optimization

### 4. Biologically Inspired Plasticity
- Homeostatic plasticity: maintain activity within target range
- Synaptic scaling: global weight normalization
- Structural plasticity: create/prune connections
- Metaplasticity: plasticity of plasticity (sliding threshold)

### 5. ANN-to-SNN Conversion
- Train standard ANN, convert to SNN via rate coding
- Advantages: leverage ANN training infrastructure
- Challenges: latency, accuracy gap, timestep selection

### 6. Non-Standard Optimization
- Evolutionary algorithms, reinforcement learning
- Gradient-free approaches for non-differentiable components

## NeuroTrain Framework

### Key Components
- Built on snnTorch (LIF neuron implementations)
- Modular architecture: interchangeable learning rules, datasets, architectures
- Unified API for consistent benchmarking

### Benchmarking Dimensions
- Datasets: static images (MNIST, CIFAR) + neuromorphic (N-MNIST, DVS)
- Architectures: feedforward, convolutional, recurrent SNNs
- Training Regimes: supervised, unsupervised, hybrid

## Implementation Guide

```python
import snntorch as snn
import snntorch.functional as SF
import torch
import torch.nn as nn

# LIF neuron with surrogate gradient
lif = snn.Leaky(beta=0.9, threshold=0.5, spike_grad=SF.surrogate.atan())

# Three-factor learning example
def three_factor_update(pre_spike, post_spike, reward, learning_rate=0.01):
    dw = learning_rate * pre_spike * post_spike * reward
    return dw

# Surrogate gradient training loop
def train_step(model, data, target, optimizer):
    optimizer.zero_grad()
    spk_rec, mem_rec = model(data)
    loss = SF.mse_count_loss()(spk_rec, target)
    loss.backward()  # surrogate gradients flow through spikes
    optimizer.step()
    return loss.item()
```

## Comparison Criteria

| Criterion | Surrogate-GD | Local Rules | Three-Factor | ANN-to-SNN |
|-----------|-------------|-------------|--------------|------------|
| Biological plausibility | Low | High | Medium | Low |
| Hardware efficiency | Medium | High | High | High |
| Accuracy | High | Low-Medium | Medium | High |
| Training speed | Fast | Fast | Medium | Slow (2-phase) |
| Scalability | High | High | High | High |

## Open Challenges

1. Taxonomy gaps: No unified classification across biological/computational boundaries
2. Hardware constraints: Local rules need specialized neuromorphic hardware
3. Accuracy gap: SNNs still lag ANNs on complex vision/language tasks
4. Standardization: No agreed benchmark suite or evaluation metrics
5. Hybrid approaches: Combining multiple learning paradigms effectively

## Activation

- neurotrain, snn benchmark, local learning SNN, SNN training comparison
- surrogate gradient snn, three-factor learning, STDP benchmarking
- snnTorch framework, biologically plausible learning, ANN-to-SNN conversion
