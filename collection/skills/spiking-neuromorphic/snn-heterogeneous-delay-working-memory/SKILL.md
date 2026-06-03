---
name: snn-heterogeneous-delay-working-memory
description: "Working memory implementation in recurrent spiking neural networks using heterogeneous synaptic delays. Enables energy-efficient neuromorphic storage and recall of precise temporal spike patterns."
category: neuroscience
tags: [snn, spiking-neural-network, working-memory, neuromorphic, recurrent-network, synaptic-delays]
trigger_keywords: [working memory, synaptic delays, spike patterns, recurrent SNN, heterogeneous delays, neuromorphic memory]
related_papers:
  - title: "Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays"
    authors: Laurent U Perrinet
    arxiv_id: "2604.14096v1"
    published: "2026-04-15"
---

# SNN Heterogeneous Delay Working Memory

Working memory implementation using recurrent spiking neural networks (SNNs) with heterogeneous synaptic delays, enabling precise temporal pattern storage and recall.

## Overview

Working memory—the ability to store and recall precise temporal patterns of neural activity—remains an open challenge for spiking neural networks (SNNs). This methodology proposes a recurrent SNN architecture with heterogeneous synaptic delays modeled as weight tensors, trained end-to-end using surrogate-gradient backpropagation through time.

## Key Innovation

**Heterogeneous Synaptic Delays**: Each synapse is equipped with $D$ delays (typically $D=41$), modeled as a weight tensor $\mathbf{W} \in \mathbb{R}^{N 	imes N 	imes D}$, where:
- $N$ = number of neurons
- $D$ = number of delay steps
- Each synapse can transmit spikes with different temporal offsets

## Architecture

### Network Components

```
┌─────────────────────────────────────────────────────────────┐
│                  Recurrent SNN with Delays                  │
├─────────────────────────────────────────────────────────────┤
│  Input Layer → Hidden Layer (N neurons) → Output Layer      │
│                    ↓                                        │
│         ┌──────────────────┐                                │
│         │  Weight Tensor W  │  ∈ ℝ^(N×N×D)                   │
│         │  D = 41 delays    │                                │
│         └──────────────────┘                                │
│                    ↓                                        │
│         Spiking Motif Representation                        │
└─────────────────────────────────────────────────────────────┘
```

### Spiking Motifs

- Patterns represented as sequential chains of overlapping **Spiking Motifs**
- Each motif: contiguous window of length $D$ that predicts spikes at the next time step
- Enables unique temporal pattern encoding

## Training Methodology

### Surrogate-Gradient Backpropagation Through Time (BPTT)

```python
# Conceptual training loop
for epoch in range(num_epochs):
    # Forward pass with heterogeneous delays
    spikes = forward_pass_snn(inputs, weight_tensor_W)
    
    # Compute loss on spike timing
    loss = spike_timing_loss(spikes, target_patterns)
    
    # Backprop with surrogate gradients
    loss.backward()
    optimizer.step()
```

### Training Parameters (Benchmark)

| Parameter | Value |
|-----------|-------|
| Neurons (N) | 512 |
| Delays (D) | 41 |
| Patterns (M) | 16 |
| Time Steps (T) | 1000 |
| Mean F1 Score | 1.0 |

## Implementation Guide

### Step 1: Define Delayed Synapse

```python
import torch
import torch.nn as nn

class DelayedSynapse(nn.Module):
    """Synapse with multiple delay channels."""
    
    def __init__(self, n_neurons, n_delays=41):
        super().__init__()
        self.n_delays = n_delays
        # Weight tensor: [n_neurons, n_neurons, n_delays]
        self.W = nn.Parameter(torch.randn(n_neurons, n_neurons, n_delays))
        
    def forward(self, spike_history):
        """
        spike_history: [batch, n_neurons, n_delays] - recent spike history
        Returns: weighted input current
        """
        # Compute delayed weighted sum
        current = torch.sum(spike_history * self.W, dim=(1, 2))
        return current
```

### Step 2: Recurrent SNN Cell

```python
class RecurrentSNNCell(nn.Module):
    """Recurrent SNN with heterogeneous delays."""
    
    def __init__(self, n_neurons, n_delays=41, tau_mem=20.0):
        super().__init__()
        self.n_neurons = n_neurons
        self.n_delays = n_delays
        self.tau_mem = tau_mem
        
        # Delayed recurrent weights
        self.recurrent = DelayedSynapse(n_neurons, n_delays)
        
        # Surrogate gradient for backprop
        self.surrogate = SurrogateGradient()
        
    def forward(self, x_t, mem, spike_history):
        """
        Forward step with membrane dynamics.
        
        Args:
            x_t: input at time t
            mem: membrane potential
            spike_history: [batch, n_neurons, n_delays] buffer
        """
        # Compute recurrent input with delays
        rec_input = self.recurrent(spike_history)
        
        # Update membrane potential (leaky integrator)
        mem = mem + (1 / self.tau_mem) * (-mem + x_t + rec_input)
        
        # Spike generation with surrogate gradient
        spike = self.surrogate.spike_function(mem)
        
        # Reset membrane after spike
        mem = mem * (1 - spike)
        
        return spike, mem
```

### Step 3: Surrogate Gradient

```python
class SurrogateGradient(torch.autograd.Function):
    """Straight-Through Estimator with derivative of fast sigmoid."""
    
    @staticmethod
    def forward(ctx, input):
        ctx.save_for_backward(input)
        return (input > 0).float()  # Heaviside spike
    
    @staticmethod
    def backward(ctx, grad_output):
        input, = ctx.saved_tensors
        # Fast sigmoid derivative as surrogate
        grad = grad_output / (1 + input.abs())**2
        return grad

# Convenience function
spike_function = SurrogateGradient.apply
```

### Step 4: Pattern Storage

```python
def train_pattern_storage(model, patterns, n_epochs=100):
    """
    Train network to store multiple spike patterns.
    
    Args:
        model: RecurrentSNN
        patterns: List of target spike trains [time, neurons]
    """
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    
    for epoch in range(n_epochs):
        total_loss = 0
        
        for pattern in patterns:
            # Initialize with clamped pattern start
            mem = torch.zeros(n_neurons)
            spike_history = initialize_history(pattern[:D])
            
            # Unroll network
            output_spikes = []
            for t in range(T):
                spike, mem = model(pattern[t], mem, spike_history)
                output_spikes.append(spike)
                spike_history = update_history(spike_history, spike)
            
            # Compute spike timing loss
            loss = compute_spike_loss(output_spikes, pattern)
            
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            total_loss += loss.item()
```

## Memory Recall Dynamics

### Recall Process

1. **Initialization**: Clamp initial window of target pattern
2. **Propagation**: Network autonomously recalls pattern forward in time
3. **Emergence**: Recall emerges first near initialization, propagates forward

### Performance Metrics

| Metric | Value |
|--------|-------|
| Mean F1 Score | 1.0 (perfect recall) |
| Pattern Capacity | 16 patterns |
| Energy Efficiency | High (sparse spike coding) |

## Applications

1. **Neuromorphic Edge Computing**: Energy-efficient working memory for IoT devices
2. **Brain-Computer Interfaces**: Temporal pattern storage for neural decoding
3. **Cognitive Robotics**: Working memory for robotic control systems
4. **Temporal Sequence Learning**: Speech/music pattern recognition

## Advantages

- **Energy Efficiency**: Spike-based computation, event-driven processing
- **Temporal Precision**: Precise spike timing representation
- **Hardware Compatibility**: Suitable for neuromorphic chips (Loihi, TrueNorth)
- **Scalability**: Weight tensor structure enables parallel computation

## Limitations

- Requires surrogate gradients for training
- Memory buffer needed for delay history
- Pattern capacity limited by network size

## Extensions

1. **Adaptive Delays**: Learn optimal delay distributions
2. **Hierarchical Memory**: Multi-scale temporal representations
3. **Attention Mechanisms**: Selective pattern retrieval
4. **Online Learning**: Continuous pattern incorporation

## References

- Perrinet, L. U. (2026). Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays. arXiv:2604.14096v1.
- Bellec et al. (2020). A solution to the learning dilemma for recurrent networks of spiking neurons.
- Neftci et al. (2019). Surrogate gradient learning in spiking neural networks.

## Related Skills

- adaptive-spiking-neuron-asn
- ember-hybrid-snn-llm-architecture
- meta-learning-in-context-brain-decoding
- brain-dit-fmri-foundation-model
