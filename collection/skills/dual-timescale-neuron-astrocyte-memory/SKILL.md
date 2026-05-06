---
name: dual-timescale-neuron-astrocyte-memory
description: >
  Dual-timescale memory mechanism in spiking neuron-astrocyte networks for efficient navigation.
  Models complementary learning systems: long-term memory via astrocytic regulation + short-term
  suppression via spike-frequency adaptation. Use for neuromorphic navigation, spatial memory SNNs,
  bio-inspired RL, and partial observability tasks.
  Triggers: dual-timescale, neuron-astrocyte, spatial memory, navigation SNN, astrocyte memory,
  complementary learning, 双时程记忆, 星形胶质细胞
version: 1.0.0
metadata:
  hermes:
    source_paper: "Dual-Timescale Memory in a Spiking Neuron-Astrocyte Network for Efficient Navigation (arXiv:2604.15391)"
    tags: [snn, astrocyte, navigation, memory, spiking, neuromorphic]
---

# Dual-Timescale Memory in Spiking Neuron-Astrocyte Network

## Overview

Biological agents combine long-term memory of successful actions with short-term suppression of
recently visited locations. This skill implements a bio-inspired dual-timescale memory system
using spiking neuron-astrocyte networks for efficient navigation under partial observability.

## Core Architecture

### Two Complementary Memory Timescales

1. **Short-term memory (STM)**: Spike-frequency adaptation (SFA)
   - Temporarily suppresses recently activated neurons
   - Prevents revisiting recent locations (~seconds scale)
   - Acts as "working memory" for exploration

2. **Long-term memory (LTM)**: Astrocytic calcium dynamics
   - Astrocytes detect neural activity patterns via IP3 signaling
   - Modulate synaptic weights through gliotransmitter release
   - Consolidates successful navigation paths (~minutes+ scale)

### Key Mechanism

- **SFA**: Adaptive threshold increases after spiking, decays exponentially
- **Astrocyte**: IP3 accumulation → calcium release → synaptic modulation
- **Interaction**: STM guides exploration; LTM consolidates learned paths

## Implementation Pattern

```python
import numpy as np

class DualTimescaleSNN:
    def __init__(self, n_neurons, tau_sfa=50, tau_astro=500):
        self.n = n_neurons
        self.tau_sfa = tau_sfa   # Short-term adaptation time constant
        self.tau_astro = tau_astro  # Long-term astrocyte time constant
        
        # State variables
        self.adaptation = np.zeros(n_neurons)  # STM: spike-frequency adaptation
        self.astrocyte = np.zeros(n_neurons)   # LTM: astrocytic calcium
        self.threshold = np.ones(n_neurons)    # Adaptive thresholds
        
    def step(self, input_current, dt=1.0):
        # Update adaptation (short-term memory)
        self.adaptation *= np.exp(-dt / self.tau_sfa)
        
        # Update astrocyte (long-term memory)
        self.astrocyte *= np.exp(-dt / self.tau_astro)
        
        # Adaptive threshold = base + adaptation - astrocyte modulation
        effective_threshold = 1.0 + self.adaptation - 0.5 * self.astrocyte
        
        # Spiking logic
        membrane = input_current
        spikes = (membrane > effective_threshold).astype(float)
        
        # Update states after spiking
        self.adaptation += 0.3 * spikes  # Increase adaptation
        self.astrocyte += 0.1 * spikes   # Accumulate astrocyte signal
        
        return spikes
```

## Navigation Application

```python
def navigate_with_dual_memory(agent, grid, start, goal, max_steps=200):
    pos = start
    visited = set()
    
    for step in range(max_steps):
        # Get local sensory input (partial observability)
        local_view = get_local_view(grid, pos)
        
        # SNN decides action
        input_current = encode_view(local_view)
        spikes = agent.step(input_current)
        action = decode_action(spikes)
        
        # Execute action
        new_pos = move(pos, action)
        
        # STM prevents immediate return (SFA suppression)
        # LTM reinforces successful paths (astrocyte modulation)
        
        if new_pos == goal:
            return True
        pos = new_pos
    
    return False
```

## Advantages

- **Efficient exploration**: SFA prevents looping back to recent locations
- **Path consolidation**: Astrocyte dynamics reinforce successful routes
- **Partial observability**: Works without full environment map
- **Energy efficiency**: Sparse spiking + local computation
- **Bio-plausibility**: Matches complementary learning systems theory

## Parameters

| Parameter | Typical Range | Effect |
|-----------|---------------|--------|
| tau_sfa | 20-100 ms | STM decay speed |
| tau_astro | 200-1000 ms | LTM consolidation speed |
| SFA_strength | 0.1-0.5 | Suppression intensity |
| Astro_modulation | 0.1-0.3 | LTM influence on threshold |

## Related Skills

- dual-timescale-memory-astrocyte
- dual-timescale-memory-spiking-neuron-astrocyte-network-efficient
