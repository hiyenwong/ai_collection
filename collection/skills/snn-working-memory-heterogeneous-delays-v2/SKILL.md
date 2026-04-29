---
name: snn-working-memory-heterogeneous-delays-v2
description: "Working memory implementation in recurrent spiking neural networks using heterogeneous synaptic delays. Heterogeneous delays enable stable persistent activity for memory maintenance without external input. Activation: working memory, snn, spiking neural network, heterogeneous delays, persistent activity, recurrent, memory maintenance"
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    source_paper: "Working Memory in Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays (arXiv:2604.14096v1)"
    citations: 0
    tags: [snn, working-memory, heterogeneous-delays, recurrent-network, persistent-activity]
---

# Working Memory in Recurrent Spiking Neural Networks with Heterogeneous Synaptic Delays

## Source Paper
- **Title**: Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays
- **Authors**: [See arXiv:2604.14096v1]
- **arXiv**: 2604.14096v1
- **Published**: 2026-04-19
- **PDF**: https://arxiv.org/pdf/2604.14096v1

## Overview

This paper demonstrates that heterogeneous synaptic delays in recurrent spiking neural networks (RSNNs) enable stable working memory functionality. Unlike homogeneous delay networks, heterogeneous delays create diverse temporal response patterns that allow persistent neural activity to be maintained without external input — mimicking the biological mechanism by which the brain holds information in working memory.

## Key Concepts

### Heterogeneous Synaptic Delays
Real biological synapses have varying transmission delays (1-20ms) depending on distance, myelination, and synapse type. This heterogeneity is often ignored in computational models but is crucial for:
- **Temporal diversity**: Different pathways process information at different speeds
- **Activity stabilization**: Delays create reverberating loops that sustain activity
- **Memory maintenance**: Persistent activity without drift or decay

### Working Memory Mechanism
1. **Stimulus encoding**: Brief input activates a subset of neurons
2. **Persistent activity**: Heterogeneous delays create reverberating loops
3. **Stable maintenance**: Activity pattern remains stable over time
4. **Readout**: Downstream neurons decode the maintained state

### Comparison with Homogeneous Delays
- Homogeneous delays: activity quickly decays or becomes chaotic
- Heterogeneous delays: stable persistent activity emerges naturally
- The key is the **distribution of delays** across the network

## Implementation

```python
import numpy as np
import torch

class RSNNWithHeterogeneousDelays:
    """
    Recurrent Spiking Neural Network with heterogeneous synaptic delays
    for working memory maintenance.
    """
    
    def __init__(self, n_neurons, n_synapses, max_delay=20, dt=1.0):
        self.n_neurons = n_neurons
        self.dt = dt
        self.max_delay = int(max_delay / dt)
        
        # Heterogeneous delay distribution
        self.delays = np.random.choice(
            range(1, self.max_delay + 1),
            size=(n_neurons, n_neurons)
        )
        
        # Synaptic weights
        self.weights = np.random.randn(n_neurons, n_neurons) * 0.1
        
        # Neuron parameters (LIF)
        self.tau_mem = 20.0  # membrane time constant (ms)
        self.threshold = 1.0
        self.refractory = 5  # refractory period (ms)
        
        # State
        self.v_mem = np.zeros(n_neurons)
        self.spike_buffer = {}  # spike history for delay lines
        self.refractory_count = np.zeros(n_neurons)
    
    def _lif_step(self, v_mem, input_current, refractory_count):
        """Leaky Integrate-and-Fire neuron update."""
        dv = (-v_mem + input_current) / self.tau_mem * self.dt
        new_v = v_mem + dv
        spikes = (new_v >= self.threshold) & (refractory_count == 0)
        new_v[spikes] = 0.0
        new_refractory = np.maximum(0, refractory_count - 1)
        new_refractory[spikes] = self.refractory
        return new_v, spikes, new_refractory
    
    def step(self, external_input):
        """One simulation step."""
        recurrent_input = np.zeros(self.n_neurons)
        for i in range(self.n_neurons):
            for j in range(self.n_neurons):
                delay = self.delays[i, j]
                if j in self.spike_buffer and delay in self.spike_buffer[j]:
                    recurrent_input[i] += self.weights[i, j] * self.spike_buffer[j][delay]
        
        total_input = recurrent_input + external_input
        new_v, spikes, new_refractory = self._lif_step(
            self.v_mem, total_input, self.refractory_count
        )
        self.v_mem = new_v
        self.refractory_count = new_refractory
        
        for i in range(self.n_neurons):
            if i not in self.spike_buffer:
                self.spike_buffer[i] = {}
            self.spike_buffer[i][1] = float(spikes[i])
            for d in list(self.spike_buffer[i].keys()):
                self.spike_buffer[i][d + 1] = self.spike_buffer[i].pop(d)
                if d + 1 > self.max_delay:
                    del self.spike_buffer[i][d + 1]
        
        return spikes
    
    def working_memory_trial(self, stimulus, stimulus_duration=100, 
                            maintenance_duration=500):
        """Simulate a working memory trial."""
        total_steps = stimulus_duration + maintenance_duration
        activity = np.zeros((total_steps, self.n_neurons))
        
        for t in range(stimulus_duration):
            spikes = self.step(stimulus)
            activity[t] = spikes
        
        for t in range(stimulus_duration, total_steps):
            spikes = self.step(np.zeros(self.n_neurons))
            activity[t] = spikes
        
        return activity

# Usage
n = 100
net = RSNNWithHeterogeneousDelays(n, n * n)
stimulus = np.zeros(n)
stimulus[:int(0.2 * n)] = 0.5
activity = net.working_memory_trial(stimulus, stimulus_duration=100, maintenance_duration=500)
maintenance_activity = activity[100:, :int(0.2 * n)]
print(f"Persistent activity rate: {maintenance_activity.mean():.4f}")
```

## Applications

### Working Memory Tasks
- Delayed-match-to-sample tasks
- N-back tasks
- Spatial memory maintenance

### Cognitive Modeling
- Modeling prefrontal cortex persistent activity
- Understanding attention and working memory deficits
- Neuromodulation effects on memory stability

## Limitations
- Requires careful tuning of delay distribution parameters
- Scaling to large networks increases computational cost
- Biological plausibility of delay distributions needs validation

## References

- Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays. arXiv:2604.14096v1, 2026.

## Related Skills
- [[snn-working-memory-delays]]
- [[snn-working-memory-heterogeneous-delays]]
- [[snn-learning-rules-dynamics]]

## Activation Keywords
- working memory
- snn
- spiking neural network
- heterogeneous delays
- persistent activity
- recurrent network
- memory maintenance
- synaptic delays
- RSNN
