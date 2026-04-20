---
name: snn-working-memory-heterogeneous-delays
description: "Working memory implementation in recurrent spiking neural networks using heterogeneous axonal delays. Demonstrates how structured delay distributions enable temporal pattern storage without continuous activation. Activation: snn working memory, heterogeneous delays, temporal pattern memory, recurrent spiking network, axonal delay."
version: 1.0.0
metadata:
  hermes:
    source_paper: "Working Memory in Recurrent SNN With Heterogeneous Delays (arXiv:2604.14096)"
    tags: [neuroscience, spiking, working-memory, delays, recurrent]
---

# Working Memory in Recurrent SNN with Heterogeneous Delays

## Source Paper
- **Title**: Working Memory in Recurrent SNN With Heterogeneous Delays
- **arXiv**: 2604.14096
- **PDF**: https://arxiv.org/pdf/2604.14096

## Overview

Working memory — the ability to store and recall precise temporal patterns of neural activity — remains an open challenge for spiking neural networks. This paper demonstrates that **heterogeneous axonal delays** (rather than just synaptic weights) can serve as a powerful mechanism for temporal pattern storage in recurrent SNNs.

The key insight: axonal delays create a distributed temporal buffer where different signal paths arrive at different times, enabling the network to maintain temporal information without requiring sustained neural firing.

## Core Concepts

### Heterogeneous Delay Distributions
- Biological neurons have varying axonal conduction delays (0.5-20ms)
- Uniform delays limit temporal storage capacity
- Heterogeneous (structured) delays create a rich temporal basis set
- Delays act as "memory traces" with different time constants

### Temporal Pattern Storage Mechanism
1. Input pattern arrives at time t=0
2. Signals propagate through paths with different delays
3. Recurrent feedback creates sustained temporal interference
4. The superposition of delayed signals reconstructs the stored pattern
5. Readout layer decodes the temporal state at any point in time

### Advantages Over Persistent Activity
- **Energy efficient**: No continuous firing required for memory maintenance
- **Higher capacity**: Multiple patterns stored in delay structure
- **Robust**: Tolerant to individual neuron failures
- **Biologically plausible**: Matches observed delay distributions in cortex

## Implementation Pattern

```python
import numpy as np

class DelayedRecurrentSNN:
    """Recurrent SNN with heterogeneous axonal delays."""
    
    def __init__(self, n_neurons, n_delays=20, max_delay_ms=20):
        self.n_neurons = n_neurons
        self.max_delay = max_delay_ms
        
        # Heterogeneous delay distribution (log-normal, as in biology)
        self.delays = np.random.lognormal(
            mean=np.log(5), sigma=0.5, size=(n_neurons, n_neurons, n_delays)
        ).clip(1, max_delay_ms).astype(int)
        
        # Delay-specific synaptic weights
        self.W = np.random.randn(n_neurons, n_neurons, n_delays) * 0.05
        
        # Spike history buffer
        self.spike_history = np.zeros((n_neurons, max_delay_ms + 1))
        
        # Membrane potentials
        self.v = np.zeros(n_neurons)
        
    def step(self, input_spikes, dt=1.0):
        """Advance network by one timestep."""
        # Compute recurrent input from delayed spikes
        recurrent = np.zeros(self.n_neurons)
        for d_idx in range(self.delays.shape[-1]):
            delay_val = self.delays[:, :, d_idx]
            # Gather spikes from history at appropriate delays
            for i in range(self.n_neurons):
                for j in range(self.n_neurons):
                    d = delay_val[i, j]
                    if d <= self.max_delay:
                        recurrent[i] += self.W[i, j, d_idx] * self.spike_history[j, min(d, self.max_delay)]
        
        # Update membrane potential (LIF neuron)
        self.v = 0.95 * self.v + input_spikes + recurrent
        spikes = (self.v > 1.0).astype(float)
        self.v *= (1 - spikes)  # Reset after spike
        
        # Update spike history
        self.spike_history = np.roll(self.spike_history, 1, axis=1)
        self.spike_history[:, 0] = spikes
        
        return spikes
    
    def store_pattern(self, pattern):
        """Store a temporal pattern in the delay structure."""
        # Pattern is a sequence of spike vectors
        for t, spikes in enumerate(pattern):
            self.step(spikes)
    
    def recall(self, cue, n_steps=50):
        """Recall stored pattern from a partial cue."""
        recalled = []
        self.step(cue)
        for _ in range(n_steps):
            spikes = self.step(np.zeros(self.n_neurons))
            recalled.append(spikes.copy())
        return np.array(recalled)
```

## Training Strategy
- **Delay-aware backpropagation**: Gradient flows through delay paths
- **DECOLLE-style learning**: Local learning with eligibility traces
- **Delay optimization**: Fine-tune delay distributions for specific temporal tasks

## Applications
- **Temporal sequence prediction**: Predicting next elements in time series
- **Motor control**: Maintaining movement trajectories
- **Speech processing**: Phoneme sequence recognition
- **Neuromorphic hardware**: Low-power temporal computing

## Key Parameters
| Parameter | Description | Typical Value |
|-----------|-------------|---------------|
| n_delays | Number of discrete delay channels | 10-50 |
| max_delay_ms | Maximum axonal delay | 10-50 ms |
| tau_mem | Membrane time constant | 10-20 ms |
| delay_distribution | Distribution type | Log-normal (biological) |

## Limitations
- Memory capacity scales with delay diversity, not just neuron count
- Requires precise delay calibration for optimal performance
- Training with delays is computationally intensive

## Related Skills
- [[convolution-delay-recurrent-snn]]
- [[dual-timescale-neuron-astrocyte-memory]]
- [[spiking-neural-network-training]]
