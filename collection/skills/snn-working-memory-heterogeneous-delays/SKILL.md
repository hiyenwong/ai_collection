---
name: snn-working-memory-heterogeneous-delays
description: Working memory implementation in recurrent spiking neural networks using heterogeneous synaptic delays for precise temporal pattern storage
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [snn, working-memory, heterogeneous-delays, temporal-patterns, recurrent]
    source_paper: "Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays (arXiv:2604.14096)"
    authors: "Laurent U Perrinet"
    published: "2026-04-15"
    category: "neuroscience"
---

# Working Memory in SNNs with Heterogeneous Delays

## Overview
Implements working memory in recurrent Spiking Neural Networks using heterogeneous synaptic delays (D=41 distinct delays). This approach enables precise temporal pattern storage and recall without complex architectures, leveraging delay diversity as a natural memory mechanism.

## Key Concepts

### Heterogeneous Delay Mechanism
- Each synapse has a different transmission delay
- D=41 distinct delays create rich temporal dynamics
- Delays act as natural memory traces

### Recurrent Architecture
```
Input --> [N Neurons with D Delays] --> Output
          |<---- Recurrent Connections ----|
          
Each synapse (i,j) has unique delay d_ij in {1, 2, ..., D}
```

## Implementation Pattern

```python
import numpy as np

class SNNWorkingMemory:
    """Recurrent SNN with heterogeneous synaptic delays."""
    
    def __init__(self, n_neurons=100, max_delay=41, dt=0.001):
        self.n = n_neurons
        self.d = max_delay
        self.dt = dt
        self.v_mem = np.zeros(n_neurons)
        self.threshold = 1.0
        self.refractory = np.zeros(n_neurons)
        
        # Heterogeneous delay matrix
        self.delays = np.random.randint(1, max_delay + 1, (n_neurons, n_neurons))
        self.weights = np.random.randn(n_neurons, n_neurons) * 0.1
        
        # Delay buffers for each unique delay
        self.spike_buffers = {}
        for d in range(1, max_delay + 1):
            self.spike_buffers[d] = np.zeros((n_neurons, d))
    
    def step(self, external_input):
        """Advance network by one timestep."""
        spikes = np.zeros(self.n)
        
        for i in range(self.n):
            if self.refractory[i] > 0:
                self.refractory[i] -= 1
                continue
            
            # Collect delayed spikes from all neurons
            recurrent_input = 0
            for j in range(self.n):
                delay = self.delays[i, j]
                delayed_spike = self.spike_buffers[delay][j, -1]
                recurrent_input += self.weights[i, j] * delayed_spike
            
            # Update membrane potential
            self.v_mem[i] += self.dt * (-self.v_mem[i] + recurrent_input + external_input[i])
            
            # Spike if threshold crossed
            if self.v_mem[i] >= self.threshold:
                spikes[i] = 1
                self.v_mem[i] = 0
                self.refractory[i] = 5  # Refractory period
        
        # Update delay buffers
        for d in range(1, self.d + 1):
            self.spike_buffers[d] = np.roll(self.spike_buffers[d], 1, axis=1)
            self.spike_buffers[d][:, 0] = spikes
        
        return spikes
```

## Applications
- Temporal sequence memory
- Short-term working memory in neuromorphic systems
- Pattern completion
- Time-series prediction

## References
- Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays
- Authors: Laurent U Perrinet
- arXiv: 2604.14096 (2026-04-15)

## Activation
- snn working memory
- heterogeneous synaptic delays
- temporal pattern storage
- recurrent spiking networks
- 脉冲神经网络工作记忆
- 异质突触延迟
