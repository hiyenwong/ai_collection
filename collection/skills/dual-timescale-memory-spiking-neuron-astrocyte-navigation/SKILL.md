---
name: dual-timescale-memory-spiking-neuron-astrocyte-navigation
category: ai_collection
description: "Dual-timescale memory in spiking neuron-astrocyte networks for efficient navigation - combines STDP-based long-term memory and astrocyte-mediated short-term suppression of recently visited locations. Based on arXiv:2604.15391."
source_paper: "arXiv:2604.15391v1"
paper_title: "Dual-Timescale Memory in a Spiking Neuron-Astrocyte Network for Efficient Navigation"
authors: "Yuliya Tsybina, Evgenia Antonova, Sergey Shchanikov"
date: "2026-04-16"
keywords: ["spiking neural networks", "astrocytes", "working memory", "navigation", "dual timescale", "STDP", "short-term suppression", "reinforcement learning"]
trigger: ["dual-timescale memory", "spiking neuron astrocyte", "navigation SNN", "astrocyte navigation", "short-term suppression", "STDP long-term memory"]
---

# Dual-Timescale Memory in Spiking Neuron-Astrocyte Networks

## Source Paper
- **Title**: Dual-Timescale Memory in a Spiking Neuron-Astrocyte Network for Efficient Navigation
- **arXiv**: 2604.15391v1
- **Date**: April 16, 2026
- **Categories**: q-bio.QM
- **PDF**: https://arxiv.org/pdf/2604.15391v1.pdf

## Overview

Biological agents navigate complex environments by combining **long-term memory** of successful actions with **short-term suppression** of recently visited locations — a capability difficult to replicate in artificial systems, especially under partial observability. This paper proposes a **spiking neuron-astrocyte network** that implements this dual-timescale memory mechanism for efficient navigation.

## Core Concepts

### Dual-Timescale Memory
- **Long-term memory**: STDP-based learning of successful navigation sequences
- **Short-term memory**: Astrocyte-mediated suppression of recently visited locations
- **Integration**: Combined mechanism enables efficient exploration and exploitation

### Spiking Neuron Architecture
- **Excitatory neurons**: Encode spatial locations and actions
- **Inhibitory neurons**: Provide lateral inhibition and pattern separation
- **Astrocytes**: Slow modulatory signals for short-term suppression

### Astrocyte Role
- **Gliotransmitter release**: ATP, glutamate, D-serine modulate neural activity
- **Short-term depression**: Astrocyte-mediated suppression lasts ~seconds
- **Spatial spread**: Astrocyte processes cover multiple synapses
- **Energy metabolism**: Glucose-lactate shuttle supports neural activity

## Network Architecture

```
Input Layer (Sensory)
    ↓
Excitatory Neurons (Location/Action encoding)
    ↓ ↓
    ├→→→ Lateral inhibition (Inhibitory neurons)
    ↓
Astrocytes (Short-term suppression)
    ↓
Output Layer (Navigation decisions)
```

### Neuron Models

```python
import numpy as np
from typing import Tuple, List

class DualTimescaleNavigationNetwork:
    """Spiking neuron-astrocyte network for navigation."""
    
    def __init__(
        self,
        n_sensory: int = 100,
        n_excitatory: int = 200,
        n_inhibitory: int = 50,
        n_astrocytes: int = 40,
        dt: float = 1.0,  # ms
    ):
        self.dt = dt
        
        # Network dimensions
        self.n_s = n_sensory
        self.n_e = n_excitatory
        self.n_i = n_inhibitory
        self.n_a = n_astrocytes
        
        # Neuron states
        self.v_e = np.zeros(n_excitatory)  # Membrane potential (excitatory)
        self.v_i = np.zeros(n_inhibitory)  # Membrane potential (inhibitory)
        
        # Spike tracking
        self.spikes_e = np.zeros(n_excitatory)
        self.spikes_i = np.zeros(n_inhibitory)
        
        # Synaptic weights (long-term)
        self.W_se = np.random.randn(n_sensory, n_excitatory) * 0.01
        self.W_ee = np.random.randn(n_excitatory, n_excitatory) * 0.01
        self.W_ie = np.random.randn(n_inhibitory, n_excitatory) * 0.05
        self.W_ei = np.random.randn(n_excitatory, n_inhibitory) * 0.05
        
        # Astrocyte states (short-term)
        self.ca_a = np.zeros(n_astrocytes)  # Calcium concentration
        self.gt_a = np.zeros(n_astrocytes)  # Gliotransmitter level
        
        # Astrocyte-neuron connectivity
        self.W_ae = np.random.rand(n_astrocytes, n_excitatory) * 0.1
        self.W_ea = np.random.rand(n_excitatory, n_astrocytes) * 0.1
        
        # Time constants
        self.tau_m_e = 20.0  # ms (membrane time constant, excitatory)
        self.tau_m_i = 10.0  # ms (membrane time constant, inhibitory)
        self.tau_ca = 1000.0  # ms (astrocyte calcium, ~1 second)
        self.tau_gt = 500.0  # ms (gliotransmitter, ~0.5 second)
        
        # Thresholds
        self.v_th_e = -50.0  # mV
        self.v_th_i = -50.0  # mV
        self.v_reset = -70.0  # mV
        
        # STDP parameters (long-term learning)
        self.A_plus = 0.01
        self.A_minus = 0.01
        self.tau_plus = 20.0
        self.tau_minus = 20.0
        
        # Eligibility traces
        self.pre_trace = np.zeros(n_excitatory)
        self.post_trace = np.zeros(n_excitatory)
        
        # Recently visited suppression (astrocyte-mediated)
        self.visited_mask = np.zeros(n_excitatory)
        
    def step(self, sensory_input: np.ndarray, reward: float = 0.0) -> Tuple[np.ndarray, np.ndarray]:
        """Single network step.
        
        Args:
            sensory_input: Current sensory observation
            reward: Reward signal (for learning)
            
        Returns:
            output_spikes: Spikes from output neurons
            astrocyte_activity: Current astrocyte calcium levels
        """
        # --- Astrocyte dynamics (short timescale) ---
        # Calcium elevation from neural activity
        ca_input = np.dot(self.W_ea, self.spikes_e)
        self.ca_a += self.dt / self.tau_ca * (-self.ca_a + ca_input)
        
        # Gliotransmitter release
        self.gt_a += self.dt / self.tau_gt * (-self.gt_a + self.ca_a)
        
        # --- Neuron dynamics ---
        # Synaptic currents to excitatory neurons
        I_sensory = np.dot(sensory_input, self.W_se)
        I_recurrent = np.dot(self.spikes_e, self.W_ee)
        I_inhibitory = np.dot(self.spikes_i, self.W_ei)
        
        # Astrocyte-mediated suppression (short-term)
        I_astrocyte = -np.dot(self.gt_a, self.W_ae)
        
        # Total input to excitatory neurons
        I_e = I_sensory + I_recurrent + I_inhibitory + I_astrocyte + self.visited_mask
        
        # Excitatory neuron integration (LIF)
        dv_e = self.dt / self.tau_m_e * (-self.v_e + I_e)
        self.v_e += dv_e
        
        # Spike detection (excitatory)
        new_spikes_e = (self.v_e >= self.v_th_e).astype(float)
        self.v_e = np.where(new_spikes_e, self.v_reset, self.v_e)
        self.spikes_e = new_spikes_e
        
        # Inhibitory neuron dynamics
        I_i = np.dot(self.spikes_e, self.W_ie)
        dv_i = self.dt / self.tau_m_i * (-self.v_i + I_i)
        self.v_i += dv_i
        
        new_spikes_i = (self.v_i >= self.v_th_i).astype(float)
        self.v_i = np.where(new_spikes_i, self.v_reset, self.v_i)
        self.spikes_i = new_spikes_i
        
        # --- STDP-based learning (long timescale) ---
        if reward != 0:
            self._stdp_update(reward)
        
        # Update traces
        self.pre_trace += self.dt / self.tau_plus * (-self.pre_trace + self.spikes_e)
        self.post_trace += self.dt / self.tau_minus * (-self.post_trace + self.spikes_e)
        
        return self.spikes_e, self.ca_a
    
    def _stdp_update(self, reward: float):
        """Apply STDP with reward modulation.
        
        Long-term learning: potentiate synapses between co-active neurons.
        """
        # Pre-post STDP
        for i in range(self.n_e):
            for j in range(self.n_e):
                if self.spikes_e[j] > 0:  # Pre-synaptic spike
                    # Potentiation
                    self.W_ee[i, j] += self.A_plus * self.post_trace[i] * reward
                if self.spikes_e[i] > 0:  # Post-synaptic spike
                    # Depression
                    self.W_ee[i, j] -= self.A_minus * self.pre_trace[j] * reward
        
        # Keep weights bounded
        self.W_ee = np.clip(self.W_ee, 0, 1)
    
    def mark_visited(self, location_idx: int, duration: float = 2000.0):
        """Mark location as recently visited (astrocyte-like suppression).
        
        Args:
            location_idx: Index of visited location
            duration: Duration of suppression in ms
        """
        self.visited_mask[location_idx] = -10.0  # Strong inhibition
        
        # Decay over time
        self.visited_mask *= np.exp(-self.dt / duration)
    
    def navigate(self, env, max_steps: int = 1000) -> dict:
        """Navigate environment using dual-timescale memory.
        
        Args:
            env: Navigation environment (must have reset(), step(action), get_observation())
            max_steps: Maximum navigation steps
            
        Returns:
            results: Navigation statistics
        """
        obs = env.reset()
        trajectory = []
        total_reward = 0.0
        
        for step in range(max_steps):
            # Get network response
            spikes, _ = self.step(obs)
            
            # Decode action from spikes (e.g., most active neuron)
            action = np.argmax(spikes)
            
            # Mark current location as visited (short-term memory)
            self.mark_visited(action)
            
            # Execute action
            obs, reward, done, info = env.step(action)
            total_reward += reward
            
            trajectory.append({
                'step': step,
                'action': action,
                'observation': obs,
                'reward': reward,
                'spikes': spikes.copy(),
                'astrocyte_ca': self.ca_a.copy()
            })
            
            # Learning signal on reward
            if reward > 0:
                self._stdp_update(reward)
            
            if done:
                break
        
        return {
            'trajectory': trajectory,
            'total_reward': total_reward,
            'steps': step + 1,
            'success': info.get('success', False)
        }


class SimpleNavigationEnvironment:
    """Simple grid navigation environment for testing."""
    
    def __init__(self, grid_size: int = 10, n_goals: int = 3):
        self.grid_size = grid_size
        self.n_goals = n_goals
        self.state = (0, 0)
        self.goals = []
        
    def reset(self):
        self.state = (0, 0)
        self.visited_goals = set()
        # Random goal locations
        self.goals = [
            (np.random.randint(0, self.grid_size), 
             np.random.randint(0, self.grid_size))
            for _ in range(self.n_goals)
        ]
        return self._get_observation()
    
    def _get_observation(self):
        # Encode position as sensory input
        obs = np.zeros(self.grid_size * self.grid_size)
        idx = self.state[0] * self.grid_size + self.state[1]
        obs[idx] = 1.0
        return obs
    
    def step(self, action: int):
        # Decode action: 0=up, 1=down, 2=left, 3=right
        x, y = self.state
        if action == 0: x = max(0, x-1)
        elif action == 1: x = min(self.grid_size-1, x+1)
        elif action == 2: y = max(0, y-1)
        elif action == 3: y = min(self.grid_size-1, y+1)
        
        self.state = (x, y)
        
        # Check for goal
        reward = 0.0
        done = False
        if self.state in self.goals and self.state not in self.visited_goals:
            reward = 1.0
            self.visited_goals.add(self.state)
            if len(self.visited_goals) == self.n_goals:
                done = True
        
        info = {'success': len(self.visited_goals) == self.n_goals}
        return self._get_observation(), reward, done, info
```

## Key Findings

### 1. Navigation Performance
- **Dual-timescale memory** significantly improves navigation efficiency
- **Short-term suppression** prevents revisiting recently explored locations
- **Long-term learning** enables exploitation of successful paths
- Combined mechanism outperforms single-timescale approaches

### 2. Astrocyte Dynamics
- Astrocyte calcium elevation correlates with location visits
- Gliotransmitter release creates transient suppression (~seconds)
- Suppression decays exponentially, allowing eventual revisits
- Spatial distribution of astrocytes enables graded suppression

### 3. STDP Learning
- Long-term potentiation encodes successful navigation sequences
- Reward-modulated STDP accelerates learning
- Synaptic weights stabilize after ~100 trials
- Path encoding shows sequence-specific activation patterns

### 4. Energy Efficiency
- Astrocyte-mediated suppression reduces redundant exploration
- Combined memory reduces total steps to goal by ~40%
- Energy savings scale with environment complexity
- Particularly effective in partially observable environments

## Applications

### 1. Robotic Navigation
```python
# Robot navigation with dual-timescale memory
network = DualTimescaleNavigationNetwork(
    n_sensory=robot.sensor_dim,
    n_excitatory=500,
    n_astrocytes=100
)

results = network.navigate(robot_env, max_steps=10000)
```

### 2. Autonomous Exploration
- Planetary exploration rovers
- Underwater autonomous vehicles
- Search and rescue robots
- Warehouse automation

### 3. Reinforcement Learning
- Combining SNNs with RL algorithms
- Sample-efficient navigation learning
- Bio-inspired exploration strategies
- Multi-agent coordination

## Related Skills
- [[astrocyte-resource-diffusion-neural-fields]]
- [[astrocyte-mediated-working-memory]]
- [[snn-working-memory-heterogeneous-delays]]
- [[working-memory-heterogeneous-delays]]

## References
- Tsybina et al. (2026). Dual-Timescale Memory in a Spiking Neuron-Astrocyte Network for Efficient Navigation. arXiv:2604.15391v1.
- Araque et al. (2014). Gliotransmitters travel in time and space. Neuron.
- Volman et al. (2011). Calcium dynamics in astrocyte networks.
