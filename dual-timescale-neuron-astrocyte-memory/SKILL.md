---
name: dual-timescale-neuron-astrocyte-memory
description: "Dual-timescale memory in spiking neuron-astrocyte networks combining fast spiking dynamics with slow astrocytic modulation for efficient spatial navigation. Implements ATP-mediated gliotransmission with short-term suppression and long-term potentiation. Use for: neuromorphic navigation, astrocyte-neuron modeling, spiking network memory, energy-efficient pathfinding. Activation: astrocyte memory, neuron-astrocyte, dual-timescale, gliotransmission, spatial navigation SNN, ATP modulation, neuromorphic navigation."
---

# Dual-Timescale Neuron-Astrocyte Memory

## Source
**Paper:** Dual-Timescale Memory in a Spiking Neuron-Astrocyte Network for Efficient Navigation
**arXiv:** 2604.15391v1
**Categories:** q-bio.NC, cs.NE, q-bio.QM

## Overview

Biological agents navigate complex environments by combining long-term memory of successful actions with short-term suppression of recently visited locations. This paper implements this capability in a spiking neuron-astrocyte network where:
- **Fast timescale** (spiking neurons): Short-term suppression of recently visited locations
- **Slow timescale** (astrocytic modulation): Long-term memory of successful navigation paths
- **ATP-mediated gliotransmission**: Astrocytes modulate synaptic efficacy through ATP release and adenosine feedback

## Core Mechanism

### Two-Timescale Architecture

```
Input Layer (Sensory) → Hidden Layer (Processing) → Output Layer (Action Selection)
                              ↕
                    Astrocyte Network (Slow Modulation)
```

**Fast pathway** (ms scale):
- Leaky Integrate-and-Fire (LIF) neurons process sensory input
- Spike-timing dependent plasticity (STDP) for immediate learning
- Short-term depression suppresses recently active pathways

**Slow pathway** (seconds-minutes scale):
- Astrocytes detect neuronal activity via calcium signaling
- ATP release modulates synaptic weights globally
- Adenosine accumulation provides negative feedback (heterosynaptic depression)

### ATP-Mediated Modulation

```python
def astrocyte_modulation(pre_spike, post_spike, atp_concentration, w):
    """
    Astrocyte-mediated synaptic modulation.
    
    ATP release depends on local neuronal activity.
    Adenosine (ATP breakdown product) provides slow negative feedback.
    """
    # Fast STDP component
    dw_stdp = stdp_rule(pre_spike, post_spike)
    
    # Slow astrocytic component
    atp_release = activity_to_atp(pre_spike + post_spike)
    adenosine = atp_decay(atp_concentration, tau_adenosine=5.0)  # seconds
    
    # Combined weight update
    dw = dw_stdp * (1 - adenosine) + astrocyte_potentiation(atp_release)
    
    return w + dw
```

## Implementation

### Network Architecture

```python
import numpy as np

class NeuronAstrocyteNetwork:
    def __init__(self, n_neurons, n_astrocytes, dt=0.001):
        self.n_neurons = n_neurons
        self.n_astrocytes = n_astrocytes
        self.dt = dt
        
        # Neuron state
        self.V = np.zeros(n_neurons)  # membrane potential
        self.refractory = np.zeros(n_neurons)  # refractory counter
        
        # Synaptic weights
        self.W = np.random.randn(n_neurons, n_neurons) * 0.1
        
        # Astrocyte state (slow dynamics)
        self.Ca = np.zeros(n_astrocytes)  # calcium concentration
        self.ATP = np.zeros(n_astrocytes)  # ATP concentration
        self.adenosine = np.zeros(n_astrocytes)  # adenosine concentration
        
        # Timescale parameters
        self.tau_membrane = 0.020  # 20ms
        self.tau_calcium = 1.0     # 1s
        self.tau_atp = 5.0         # 5s
        self.tau_adenosine = 10.0  # 10s
    
    def step(self, input_current):
        # Fast: neuron dynamics (ms scale)
        dV = (-self.V + input_current) * self.dt / self.tau_membrane
        self.V += dV
        
        spikes = self.V > 1.0
        self.V[spikes] = 0.0
        self.refractory[spikes] = 5  # 5ms refractory
        
        # Slow: astrocyte dynamics (seconds scale)
        dCa = (-self.Ca + np.sum(spikes, axis=0)) * self.dt / self.tau_calcium
        self.Ca += dCa
        
        # ATP release triggered by calcium
        self.ATP += self.dt * (self.Ca > 0.5) / self.tau_atp
        self.ATP *= (1 - self.dt / self.tau_atp)
        
        # Adenosine from ATP breakdown
        self.adenosine += self.dt * self.ATP / self.tau_adenosine
        self.adenosine *= (1 - self.dt / self.tau_adenosine)
        
        # Modulate synaptic weights
        modulation = 1.0 - self.adenosine
        self.W *= modulation[:, np.newaxis]
        
        return spikes
```

### Navigation Task Integration

```python
class SpatialNavigation:
    def __init__(self, network, maze_size=20):
        self.network = network
        self.maze_size = maze_size
        self.position = (0, 0)
        self.visited = set()
        self.reward_map = np.zeros((maze_size, maze_size))
        
    def choose_action(self, sensory_input):
        """Network selects navigation action based on current state."""
        spikes = self.network.step(sensory_input)
        
        # Decode action from output spikes
        action_probs = self.decode_spikes(spikes)
        
        # Suppress recently visited directions (short-term memory)
        for direction in self.recent_directions:
            action_probs[direction] *= 0.1
        
        return np.argmax(action_probs)
    
    def update_reward(self, action, reward):
        """Long-term memory: update reward associations."""
        # Astrocyte-mediated slow consolidation
        self.network.ATP += reward * 0.1
```

## Applications

1. **Neuromorphic Navigation**: Energy-efficient robot pathfinding on edge hardware
2. **Spatial Memory Modeling**: Studying hippocampal-entorhinal navigation circuits
3. **Multi-Scale Learning**: Combining fast adaptation with slow consolidation
4. **Gliotransmission Research**: Modeling astrocyte contributions to learning

## Key Parameters

| Parameter | Typical Value | Role |
|-----------|--------------|------|
| τ_membrane | 20ms | Neuron integration timescale |
| τ_calcium | 1s | Astrocyte calcium dynamics |
| τ_ATP | 5s | ATP release/decay |
| τ_adenosine | 10s | Slow feedback inhibition |
| STDP window | ±20ms | Fast synaptic plasticity |

## Related Skills
- [[astrocyte-resource-diffusion-neural-fields]]
- [[atp-hysteresis-tripartite-synapse]]
- [[spiking-neural-network-training]]
