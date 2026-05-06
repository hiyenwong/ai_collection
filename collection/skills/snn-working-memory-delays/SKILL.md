---
name: snn-working-memory-delays
description: >
  Working memory implementation in recurrent spiking neural networks with
  heterogeneous delays. Uses diverse synaptic delay distributions to create
  multiple timescales, enabling storage and recall of precise temporal patterns
  in SNNs. Solves the temporal credit assignment problem in spiking networks.
  Activation: SNN working memory, spiking neural network memory, heterogeneous delays,
  temporal pattern storage, recurrent SNN, 脉冲神经网络工作记忆, 异质延迟
version: 1.0.0
metadata:
  hermes:
    source_paper: "Working Memory in Recurrent Spiking Neural Networks With Heterogeneous Delays"
    arxiv_id: "2604.14096"
    tags: [snn, working-memory, recurrent, delays, temporal-processing]
---

# SNN Working Memory with Heterogeneous Delays

## Overview

Implements working memory in recurrent spiking neural networks using heterogeneous synaptic delays. Different delay distributions create multiple timescales within the network, enabling the storage and recall of precise temporal patterns.

## Core Mechanism

### Heterogeneous Delay Distribution
- Synaptic delays sampled from a distribution (e.g., uniform, exponential)
- Short delays → fast dynamics (milliseconds)
- Long delays → slow dynamics (hundreds of ms to seconds)
- Combined → multi-timescale temporal memory

### Network Architecture
```python
class WorkingMemorySNN:
    def __init__(self, n_neurons, delay_distribution='exponential'):
        self.weights = nn.Parameter(torch.randn(n_neurons, n_neurons))
        # Heterogeneous delays
        self.delays = sample_delays(n_neurons, n_neurons, delay_distribution)
        self.memory_buffer = SpikeBuffer(max_delay=max(self.delays))
    
    def forward(self, spikes, timestep):
        # Collect spikes from different past timesteps based on delays
        delayed_input = self.memory_buffer.retrieve(self.delays)
        current = torch.matmul(self.weights, delayed_input)
        return self.neuron_model(current)
```

## Key Findings

1. **Delay diversity is critical**: Uniform delays fail; heterogeneous delays enable memory
2. **Optimal distribution**: Exponential or power-law delay distributions work best
3. **Memory capacity**: Scales with delay range and network size
4. **Temporal precision**: Can recall patterns with millisecond accuracy

## Training Approach

- surrogate gradient descent through time
- delay parameters can be learned or fixed
- regularization prevents runaway excitation

## Applications

- Temporal sequence prediction
- Spatio-temporal pattern recognition
- Event-based vision processing
- Neuromorphic control systems

## Related Skills

- snn-learning-survey, snn-working-memory-heterogeneous-delays, adaptive-spiking-neurons-asn
