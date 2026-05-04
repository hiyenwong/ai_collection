---
name: event-driven-eligibility-propagation
description: "Biologically plausible extension of eligibility propagation (e-prop) learning rule for recurrent spiking neural networks with event-driven computation. Efficiency shaped by biological realism — sparse connectivity, local learning, and energy-efficient mechanisms. Keywords: e-prop, eligibility traces, recurrent SNN, event-driven learning, biological plausibility, local learning rules, neuromorphic training."
---

# Event-Driven Eligibility Propagation in Large Sparse Networks

## Metadata
- **Source**: arXiv:2511.21674
- **Authors**: Agnes Korcsak-Gorzo, Jesús A. Espinoza Valverde, Jonas Stapmanns, Hans Ekkehard Plesser, David Dahmen, Matthias Bolten, Sacha J. van Albada, Markus Diesmann
- **Published**: 2025-11-26
- **Categories**: cs.LG, q-bio.NC

## Core Methodology

### Problem Statement
Despite remarkable technological advances, AI systems may still benefit from biological principles such as recurrent connectivity and energy-efficient mechanisms. Standard backpropagation through time (BPTT) is biologically implausible and computationally expensive for large recurrent networks.

### Key Innovation
A biologically plausible extension of the **eligibility propagation (e-prop)** learning rule for recurrent spiking neural networks, specifically designed for **large sparse networks** with **event-driven computation**.

### Core Concepts

1. **Eligibility Traces**: Local synaptic traces that capture the contribution of each synapse to the network output over time
2. **Event-Driven Computation**: Updates only occur when spikes arrive, exploiting sparse activity
3. **Biological Plausibility**: Local learning rules compatible with known neuroscience mechanisms
4. **Sparse Network Efficiency**: Computational cost scales with actual spike events, not network size

### Algorithm Overview

```
For each synapse (i → j):
  1. Maintain eligibility trace e_ij(t)
  2. On pre-synaptic spike: update eligibility
  3. On post-synaptic spike: compute learning signal
  4. Weight update: Δw_ij ∝ learning_signal × eligibility

Eligibility trace dynamics:
  de/dt = -e/τ + f(pre_spike, post_spike)
```

### Efficiency Gains

The efficiency of event-driven e-prop is shaped by biological realism:
- **Sparse connectivity**: Only active synapses contribute to computation
- **Sparse activity**: Most neurons are silent most of the time
- **Local updates**: No global error signal propagation needed
- **Event-driven**: Computation triggered by spikes, not clock cycles

## Implementation Guide

```python
import numpy as np

class EventDrivenEprop:
    """Event-driven eligibility propagation for sparse recurrent SNNs"""
    
    def __init__(self, n_neurons, tau_e=20.0, learning_rate=0.001):
        self.n = n_neurons
        self.tau_e = tau_e  # Eligibility trace time constant (ms)
        self.lr = learning_rate
        
        # Eligibility traces
        self.eligibility = np.zeros((n_neurons, n_neurons))
        
        # Synaptic weights (sparse)
        self.weights = np.random.randn(n_neurons, n_neurons) * 0.1
        
        # Learning signals (local approximations of global error)
        self.learning_signals = np.zeros(n_neurons)
        
    def on_pre_spike(self, pre_idx, t):
        """Update eligibility traces when pre-synaptic neuron spikes"""
        # Eligibility decay
        self.eligibility *= np.exp(-1.0 / self.tau_e)
        
        # Update traces for outgoing synapses
        self.eligibility[pre_idx, :] += 1.0
        
    def on_post_spike(self, post_idx, t):
        """Compute learning signal and update weights"""
        # Weight update: eligibility × learning signal
        delta_w = self.lr * self.eligibility[:, post_idx] * self.learning_signals[post_idx]
        self.weights[:, post_idx] += delta_w
        
        # Decay eligibility
        self.eligibility[:, post_idx] *= 0.5
        
    def update_learning_signals(self, error_grad):
        """Update local learning signals from error gradient"""
        # In biological implementation, this could be 
        # approximated by neuromodulatory signals
        self.learning_signals = error_grad
        
    def step(self, pre_spikes, post_spikes, error_grad=None):
        """Process one event-driven step"""
        if error_grad is not None:
            self.update_learning_signals(error_grad)
            
        for pre_idx in pre_spikes:
            self.on_pre_spike(pre_idx, 0)
            
        for post_idx in post_spikes:
            self.on_post_spike(post_idx, 0)
```

## Applications

- Large-scale recurrent SNN training
- Neuromorphic hardware deployment
- Continual learning in spiking networks
- Biologically plausible AI systems

## When to Use

- Training large recurrent SNNs where BPTT is impractical
- Deploying on neuromorphic hardware with event-driven constraints
- Research requiring biologically plausible learning rules
- Scenarios with sparse neural activity patterns

## Pitfalls

- Eligibility trace time constant (τ_e) must match task timescales
- Learning signal approximation may limit performance on complex tasks
- Sparse networks benefit most; dense networks see less advantage
- Requires careful hyperparameter tuning for stability

## Related Skills
- three-factor-snn-learning
- snn-learning-survey
- decolle-snn-learning
- snn-universal-approximation

## References
- Korcsak-Gorzo, A., et al. "Event-driven eligibility propagation in large sparse networks: efficiency shaped by biological realism." arXiv:2511.21674, 2025.
- Bellec, G., et al. "A solution to the learning dilemma for recurrent networks of spiking neurons." Nature Communications, 2020. (Original e-prop)
