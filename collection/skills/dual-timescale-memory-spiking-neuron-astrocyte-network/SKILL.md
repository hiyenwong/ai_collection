---
name: dual-timescale-memory-spiking-neuron-astrocyte-network
description: "Dual-timescale memory in spiking neuron-astrocyte networks for efficient navigation. Combines STDP (long-term) with astrocytic calcium transients (short-term) to create Topological-Context Memory. Applicable to neuromorphic robotics, edge AI, and efficient exploration. Activation: astrocyte memory, neuron-astrocyte network, dual-timescale memory, topological context memory, snan navigation, spiking astrocyte, memristive navigation"
---

# Dual-Timescale Memory in Spiking Neuron-Astrocyte Network for Efficient Navigation

## Overview

Biological agents navigate complex environments by combining long-term memory of successful actions with short-term suppression of recently visited locations. This skill implements a Spiking Neuron-Astrocyte Network (SNAN) where:
- **Long-term memory**: STDP reinforces successful action sequences on a distant time scale
- **Short-term memory**: Astrocytic calcium transients suppress recently visited states on a short time scale

This dual-timescale mechanism creates emergent "Topological-Context Memory" that biases agents toward unexplored regions, resolving the exploration-exploitation trade-off through local dynamics.

## Source Paper

- **Title**: Dual-Timescale Memory in a Spiking Neuron-Astrocyte Network for Efficient Navigation
- **Authors**: See arXiv:2604.15391
- **arXiv**: https://arxiv.org/abs/2604.15391
- **Published**: 2026-04-16
- **Categories**: q-bio.NC, cs.NE

## Core Concepts

### 1. Dual-Timescale Memory Architecture

The SNAN architecture operates on two complementary timescales:

| Timescale | Mechanism | Function | Biological Basis |
|-----------|-----------|----------|------------------|
| Long-term | STDP (Spike-Timing-Dependent Plasticity) | Reinforce successful action sequences | Synaptic plasticity |
| Short-term | Astrocytic calcium transients | Suppress recently visited states | Astrocyte calcium signaling |

### 2. Topological-Context Memory

A novel form of working memory emerging from local astrocytic modulation:
- Recently visited spatial locations are suppressed via astrocytic calcium buildup
- The agent naturally avoids revisiting these locations
- Exploration emerges as a side effect of local suppression
- No global statistics or explicit exploration bonuses required

### 3. Memristive Hardware Mapping

STDP is mapped to memristive VTEAM (Vanderbilt TEAM) model:
- Crossbar array implementation
- Order-of-magnitude gains in speed per area
- Energy-efficient decision making for edge AI

## Implementation

```python
import numpy as np

class SpikingNeuronAstrocyteNetwork:
    """
    Spiking Neuron-Astrocyte Network (SNAN) for navigation.
    
    Combines STDP-based long-term memory with
    astrocytic short-term spatial suppression.
    """
    
    def __init__(self, n_neurons, n_actions, 
                 tau_astro=100, tau_stdp=1000, 
                 astro_threshold=0.5, astro_max=1.0):
        self.n_neurons = n_neurons
        self.n_actions = n_actions
        
        # STDP parameters (long-term)
        self.tau_stdp = tau_stdp  # Slow plasticity timescale
        self.trace = np.zeros(n_neurons)  # Spike trace for STDP
        
        # Astrocyte parameters (short-term)
        self.tau_astro = tau_astro  # Fast calcium decay timescale
        self.astro_state = np.zeros(n_neurons)  # Calcium concentration
        self.astro_threshold = astro_threshold
        self.astro_max = astro_max
        
        # Network weights (spike-timing dependent)
        self.W = np.random.randn(n_neurons, n_actions) * 0.1
        
        # Memristive state (for hardware mapping)
        self.memristor_state = np.zeros_like(self.W)  # VTEAM model state
    
    def astrocytic_suppression(self, visited_location_idx):
        """
        Astrocytic calcium transient for visited location suppression.
        Creates short-term memory of recently visited states.
        """
        # Immediate calcium increase at visited location
        self.astro_state[visited_location_idx] = np.clip(
            self.astro_state[visited_location_idx] + 0.5,
            0, self.astro_max
        )
    
    def evolve_astrocyte(self, dt=1.0):
        """
        Astrocytic calcium decay (short-term memory fading).
        Exponential decay with timescale tau_astro.
        """
        decay = np.exp(-dt / self.tau_astro)
        self.astro_state *= decay
    
    def apply_astrocytic_modulation(self, potential_weights):
        """
        Modulate neuron firing based on astrocytic state.
        Suppresses recently visited locations.
        """
        suppression = np.where(
            self.astro_state > self.astro_threshold,
            1.0 - self.astro_state,  # Strong suppression
            1.0  # No suppression
        )
        return potential_weights * suppression
    
    def stdp_update(self, pre_spike, post_spike, learning_rate=0.01):
        """
        Spike-Timing-Dependent Plasticity for long-term memory.
        
        Potentiates synapses when pre-spike precedes post-spike.
        Depresses synapses when post-spike precedes pre-spike.
        """
        # Update pre-synaptic trace
        self.trace *= np.exp(-1.0 / self.tau_stdp)
        self.trace[pre_spike] += 1.0
        
        # Weight update
        delta_W = learning_rate * np.outer(
            pre_spike, 
            post_spike * self.trace[post_spike > 0]
        )
        self.W += delta_W
    
    def select_action(self, state, epsilon=0.1):
        """
        Action selection with astrocytic suppression.
        Biases toward unexplored (non-suppressed) locations.
        """
        # Compute potential from spiking network
        potentials = np.dot(state, self.W)
        
        # Apply astrocytic suppression (Topological-Context Memory)
        modulated = self.apply_astrocytic_modulation(potentials)
        
        # Softmax action selection
        exp_mod = np.exp(modulated - np.max(modulated))
        probs = exp_mod / (exp_mod.sum() + 1e-8)
        
        return np.random.choice(self.n_actions, p=probs)
    
    def memristive_map(self, W):
        """
        Map STDP weights to VTEAM memristive model.
        For neuromorphic hardware implementation.
        """
        # VTEAM dynamics: dx/dt = (V/R_on)^alpha * (1 - x/W_c) for V > 0
        # Simplified discrete mapping
        k_on = 1e-3  # Device parameter
        alpha = 3    # Nonlinearity
        w_c = 1.0    # Critical resistance width
        
        voltage = np.tanh(W * 5)  # Map weight to voltage [-1, 1]
        dx = k_on * (voltage / 1.0) ** alpha * (1 - self.memristor_state / w_c)
        self.memristor_state = np.clip(
            self.memristor_state + dx, 0, w_c
        )
        return self.memristor_state


# === Navigation Agent Example ===
class SNANNavigator:
    """Navigation agent using SNAN for grid-world exploration."""
    
    def __init__(self, grid_size=20, goal=(19, 19)):
        self.grid_size = grid_size
        self.goal = goal
        self.n_locations = grid_size * grid_size
        self.snan = SpikingNeuronAstrocyteNetwork(
            n_neurons=self.n_locations,
            n_actions=4,  # up, down, left, right
            tau_astro=50,   # Fast: short-term suppression
            tau_stdp=500    # Slow: long-term learning
        )
    
    def position_to_idx(self, pos):
        return pos[0] * self.grid_size + pos[1]
    
    def idx_to_position(self, idx):
        return (idx // self.grid_size, idx % self.grid_size)
    
    def step(self, position):
        """Take one navigation step."""
        idx = self.position_to_idx(position)
        
        # Encode position as input
        state = np.zeros(self.n_locations)
        state[idx] = 1.0
        
        # Select action (biased by astrocytic suppression)
        action = self.snan.select_action(state)
        
        # Move
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        new_pos = (
            np.clip(position[0] + moves[action][0], 0, self.grid_size-1),
            np.clip(position[1] + moves[action][1], 0, self.grid_size-1)
        )
        
        # Update astrocytic state (suppress visited location)
        self.snan.astrocytic_suppression(idx)
        self.snan.evolve_astrocyte(dt=1.0)
        
        # STDP update for successful moves
        if np.random.random() < 0.3:  # Reward signal
            self.snan.stdp_update(
                pre_spike=state,
                post_spike=np.eye(4)[action]
            )
        
        return new_pos
```

## Practical Applications

### 1. Neuromorphic Robotics
Deploy SNAN on memristive crossbar arrays for autonomous exploration robots that:
- Efficiently explore unknown environments without explicit mapping
- Use order-of-magnitude less energy than CPU-based navigation
- Resolve exploration-exploitation trade-off naturally

### 2. Edge AI Navigation Systems
Implement lightweight navigation for resource-constrained devices:
- No global statistics or SLAM required
- Local dynamics only (scalable)
- Memristive hardware compatible

### 3. Spatial Memory Modeling
Model biological spatial memory mechanisms:
- Hippocampal place cell dynamics with astrocytic modulation
- Grid cell navigation with dual-timescale memory
- Biological plausibility for memory-augmented AI

## Performance Metrics

From the paper's grid-world experiments:
- **Path length reduction**: Up to 6x shorter than baseline
- **Goal completion rate**: Drastically improved vs. baseline agents
- **Energy efficiency**: Order-of-magnitude improvement over CPU
- **Parameter savings**: Memristive implementation uses minimal area

## Key Insights

1. **Emergent Exploration**: The exploration-exploitation trade-off is resolved as an emergent property of local astrocytic suppression — no explicit exploration bonus needed
2. **Hardware Feasibility**: Mapping to VTEAM memristive model validates real-world deployment potential
3. **Biological Inspiration**: Directly inspired by complementary neural/astrocytic timescales in biological systems
4. **Topological-Context Memory**: A novel working memory type arising from local spatial suppression

## Related Skills
- [[astrocyte-mediated-working-memory]]
- [[snn-working-memory-heterogeneous-delays-v3]]
- [[working-memory-recurrent-spiking-neural-networks]]
- [[dual-timescale-memory-spiking-neuron-astrocyte-network-efficient]]

## Activation Keywords
- astrocyte memory
- neuron-astrocyte network
- dual-timescale memory
- topological context memory
- SNAN navigation
- spiking astrocyte
- memristive navigation
- STDP astrocyte
- exploration suppression
