---
name: snn-working-memory-heterogeneous-delays-v2
description: "Working memory implementation in recurrent spiking neural networks with heterogeneous synaptic delays. Implements D=41 delay steps per synapse using 3D weight tensors and eligibility propagation learning. Aligns with prefrontal cortex dynamics. Activation: working memory SNN, heterogeneous synaptic delays, eligibility propagation, temporal pattern storage, neuromorphic memory."
---

# Working Memory in Recurrent SNN with Heterogeneous Synaptic Delays

Implementation of working memory in recurrent spiking neural networks using heterogeneous synaptic delays, based on arXiv:2604.14096v1 (2026-04-15).

## Core Concept

Working memory - the ability to store and recall precise temporal patterns of neural activity - implemented through:
- **Heterogeneous synaptic delays**: Each synapse equipped with D=41 delay steps
- **3D weight tensor**: $\mathbf{W} \in \mathbb{R}^{N \times N \times D}$ for recurrent connections
- **Eligibility propagation**: Supervised learning for spatiotemporal pattern storage
- **Biological plausibility**: Aligns with prefrontal cortex neural dynamics

## Architecture

### Network Structure
```
Recurrent SNN with N neurons
  ↓
Each synapse has D=41 delays
  ↓
Weight tensor: W ∈ R^(N×N×D)
  ↓
Eligibility trace computation
  ↓
Working memory pattern storage
```

### Key Components

1. **Delay Distribution**: Each synapse has multiple discrete delays (0 to D-1 time steps)
2. **Spike Timing**: Precise temporal patterns encoded in spike sequences
3. **Recurrent Dynamics**: Self-sustaining activity through recurrent connections
4. **Eligibility Traces**: Local learning signals for temporal credit assignment

## Implementation Guide

### Step 1: Network Initialization
```python
import numpy as np
import torch
import torch.nn as nn

class WorkingMemorySNN(nn.Module):
    def __init__(self, n_neurons=100, n_delays=41, tau_mem=20.0):
        super().__init__()
        self.N = n_neurons
        self.D = n_delays
        self.tau_mem = tau_mem  # Membrane time constant (ms)
        
        # 3D weight tensor: (post, pre, delay)
        self.W = nn.Parameter(torch.randn(n_neurons, n_neurons, n_delays) * 0.1)
        
        # Membrane potentials
        self.v = torch.zeros(n_neurons)
        self.v_th = 1.0  # Firing threshold
        
        # Delay buffers (circular)
        self.delay_buffers = [[] for _ in range(n_delays)]
        self.buffer_ptr = 0
        
    def reset(self):
        self.v.zero_()
        self.delay_buffers = [[] for _ in range(self.D)]
        self.buffer_ptr = 0
```

### Step 2: Forward Dynamics with Delays
```python
def forward_step(self, input_spikes):
    # Aggregate delayed inputs
    delayed_input = torch.zeros(self.N)
    
    for d in range(self.D):
        buffer_idx = (self.buffer_ptr - d) % self.D
        past_spikes = self.delay_buffers[buffer_idx]
        if past_spikes:
            # Sum contributions from delay d
            delayed_input += torch.sum(
                self.W[:, :, d] @ torch.tensor(past_spikes).float()
            )
    
    # Update membrane potential (leaky integrate-and-fire)
    self.v = self.v * (1 - 1/self.tau_mem) + delayed_input + input_spikes
    
    # Generate spikes
    spikes = (self.v >= self.v_th).float()
    self.v[spikes > 0] = 0  # Reset after spike
    
    # Store current spikes in delay buffer
    self.delay_buffers[self.buffer_ptr] = spikes.tolist()
    self.buffer_ptr = (self.buffer_ptr + 1) % self.D
    
    return spikes
```

### Step 3: Eligibility Propagation Learning
```python
def compute_eligibility(self, pre_spikes, post_spikes, delay):
    """Compute eligibility trace for synaptic update."""
    # Pre-synaptic trace (low-pass filter)
    pre_trace = self.pre_trace * 0.9 + pre_spikes
    
    # Post-synaptic trace
    post_trace = self.post_trace * 0.9 + post_spikes
    
    # Eligibility: correlation at specific delay
    eligibility = pre_trace.unsqueeze(-1) * post_trace.unsqueeze(0)
    
    return eligibility

def update_weights(self, eligibility, reward, learning_rate=0.001):
    """Update weights using eligibility propagation."""
    delta_W = learning_rate * reward * eligibility
    self.W.data += delta_W
    self.W.data = torch.clamp(self.W.data, -10, 10)
```

### Step 4: Pattern Storage and Replay
```python
def store_pattern(self, pattern_spikes, duration):
    """Store a spatiotemporal pattern in working memory."""
    self.reset()
    
    for t in range(duration):
        input_t = torch.zeros(self.N)
        for (spike_time, neuron_id) in pattern_spikes:
            if spike_time == t:
                input_t[neuron_id] = 1.0
        
        output = self.forward_step(input_t)
        target = input_t
        error = target - output
        eligibility = self.compute_eligibility(input_t, output, delay=0)
        self.update_weights(eligibility, error)

def replay_pattern(self, duration, cue_input=None):
    """Replay stored pattern from working memory."""
    self.reset()
    replayed_spikes = []
    
    for t in range(duration):
        input_t = cue_input if cue_input is not None and t == 0 else torch.zeros(self.N)
        spikes = self.forward_step(input_t)
        replayed_spikes.append(spikes)
    
    return torch.stack(replayed_spikes)
```

## Key Insights

### Why Heterogeneous Delays Matter

1. **Temporal Capacity**: Multiple delays enable storage of complex temporal patterns
2. **Pattern Separation**: Different delays encode different temporal features
3. **Stability**: Distributed delays prevent catastrophic interference
4. **Biological Alignment**: Matches observed synaptic delay distributions in cortex

### Memory Capacity

```
Capacity ∝ N × D × τ_mem

Where:
- N: number of neurons
- D: number of delay steps (41 in paper)
- τ_mem: membrane time constant
```

## Applications

- **Cognitive Robotics**: Store and replay motor sequences
- **Temporal Pattern Recognition**: Multiple pattern storage and cued recall
- **Neuromorphic Computing**: Low-power, real-time processing

## References

- Perrinet, L. U. (2026). Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays. arXiv:2604.14096v1

## Activation Keywords

- working memory SNN
- heterogeneous synaptic delays
- eligibility propagation
- temporal pattern storage
- neuromorphic memory
- recurrent spiking network
