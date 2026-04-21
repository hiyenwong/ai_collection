---
name: dual-timescale-memory-spiking-neuron-astrocyte-network-efficient
description: >
  Dual-timescale memory in spiking neuron-astrocyte network for efficient navigation under
  partial observability. STDP reinforces successful actions on long timescale while astrocytic
  calcium transients suppress recently visited states on short timescale. Includes hardware
  mapping to memristive VTEAM models. Use when: spiking neural networks for navigation,
  astrocyte-inspired computing, dual-timescale memory, neuromorphic robotics, edge-AI navigation,
  STDP with astrocytic modulation, memristive implementations, exploration-exploitation trade-off.
  Activation: dual-timescale, SNAN, neuron-astrocyte, astrocytic modulation, STDP navigation,
  topological-context memory, memristive VTEAM, neuromorphic navigation, exploration suppression.
version: 1.0.0
metadata:
  hermes:
    tags: [spiking-neural-networks, astrocyte, dual-timescale, navigation, memristive, neuromorphic, STDP, working-memory]
    source_paper: "Dual-Timescale Memory in a Spiking Neuron-Astrocyte Network for Efficient Navigation (arXiv:2604.15391)"
    date: 2026-04-16
---

# Dual-Timescale Memory in Spiking Neuron-Astrocyte Networks

## Overview

Biological agents navigate by combining long-term memory of successful actions with short-term
suppression of recently visited locations. This skill implements a spiking neuron-astrocyte network
(SNAN) where two complementary timescales emerge naturally:

1. **Long-term (STDP)**: Spike-timing-dependent plasticity reinforces successful action sequences
2. **Short-term (astrocytic)**: Calcium transients suppress recently visited states

This dual-timescale mechanism resolves exploration-exploitation trade-off as an emergent property,
enabling efficient navigation under extreme partial observability.

**Source Paper**: Tsybina et al., "Dual-Timescale Memory in a Spiking Neuron-Astrocyte Network for
Efficient Navigation" (arXiv:2604.15391, 2026-04-16)

## Core Architecture

### Network Components

```
┌──────────────────────────────────────────────┐
│              SNAN Architecture               │
├──────────────────────────────────────────────┤
│  Sensory Neurons → Action Neurons            │
│       ↕ (STDP: long-term plasticity)          │
│  Astrocytic Units (Ca²⁺ transients)          │
│       ↕ (short-term suppression)              │
│  Memristive Crossbar (hardware mapping)       │
└──────────────────────────────────────────────┘
```

### Dual-Timescale Mechanism

| Timescale | Biological Basis | Function | Duration |
|-----------|-----------------|----------|----------|
| Long-term | STDP | Reinforce successful action sequences | Persistent |
| Short-term | Astrocytic Ca²⁺ | Suppress recently visited states | Transient |

## Implementation Pattern

```python
import numpy as np

class AstrocyticUnit:
    """Astrocyte model with calcium dynamics for short-term memory."""
    
    def __init__(self, tau_ca=2.0, threshold=0.5, decay_rate=0.1):
        self.tau_ca = tau_ca  # Calcium decay time constant
        self.threshold = threshold  # Suppression threshold
        self.decay_rate = decay_rate
        self.ca_level = 0.0  # Current calcium concentration
    
    def update(self, spike_input, dt=0.001):
        """
        Update calcium dynamics.
        
        Args:
            spike_input: Binary spike indicator
            dt: Time step
        
        Returns:
            Suppression signal (1 = suppress, 0 = no suppression)
        """
        # Calcium accumulation from spikes
        if spike_input:
            self.ca_level += 1.0
        
        # Exponential decay
        self.ca_level *= np.exp(-dt / self.tau_ca)
        
        # Suppression signal when calcium above threshold
        return 1.0 if self.ca_level > self.threshold else 0.0
    
    def reset(self):
        self.ca_level = 0.0


class STDPConnection:
    """Spike-timing-dependent plasticity for long-term memory."""
    
    def __init__(self, n_pre, n_post, lr=0.01, tau_stdp=20.0):
        self.weights = np.random.randn(n_pre, n_post) * 0.1
        self.lr = lr
        self.tau_stdp = tau_stdp
        self.pre_trace = np.zeros(n_pre)  # Pre-synaptic trace
        self.post_trace = np.zeros(n_post)  # Post-synaptic trace
    
    def update(self, pre_spikes, post_spikes, dt=0.001):
        """
        Update weights via STDP rule.
        
        Potentiation: pre before post (causal)
        Depression: post before pre (anti-causal)
        """
        # Update traces
        self.pre_trace *= np.exp(-dt / self.tau_stdp)
        self.post_trace *= np.exp(-dt / self.tau_stdp)
        
        if pre_spikes.any():
            self.pre_trace += pre_spikes.astype(float)
            # Depression: post was active before pre
            self.weights -= self.lr * np.outer(pre_spikes.astype(float), self.post_trace)
        
        if post_spikes.any():
            self.post_trace += post_spikes.astype(float)
            # Potentiation: pre was active before post
            self.weights += self.lr * np.outer(self.pre_trace, post_spikes.astype(float))
        
        # Weight bounds
        self.weights = np.clip(self.weights, 0, 1.0)


class SNAN:
    """Spiking Neuron-Astrocyte Network for Navigation."""
    
    def __init__(self, n_states, n_actions, n_hidden=64):
        # STDP connections for long-term action-value learning
        self.state_to_hidden = STDPConnection(n_states, n_hidden)
        self.hidden_to_action = STDPConnection(n_hidden, n_actions)
        
        # Astrocytic units for short-term visit suppression
        self.astrocytes = [AstrocyticUnit(tau_ca=2.0) for _ in range(n_states)]
        
        # Network state
        self.hidden_state = np.zeros(n_hidden)
        self.visit_history = {}
    
    def select_action(self, state, legal_actions):
        """
        Select action using dual-timescale memory.
        
        Args:
            state: Current state index
            legal_actions: Available actions
        
        Returns:
            Selected action index
        """
        # Short-term suppression: discourage recently visited states
        astrocytic_suppression = self.astrocytes[state].update(1.0)
        
        # Long-term: STDP-based action values
        action_values = self._compute_action_values(state, legal_actions)
        
        # Apply astrocytic suppression
        if astrocytic_suppression > 0:
            action_values *= 0.1  # Strong suppression
        
        # Epsilon-greedy with suppressed values
        return self._epsilon_greedy(action_values, legal_actions)
    
    def _compute_action_values(self, state, actions):
        """Compute action values through STDP-weighted connections."""
        values = np.zeros(len(actions))
        for i, action in enumerate(actions):
            values[i] = np.sum(
                self.state_to_hidden.weights[state] * 
                self.hidden_to_action.weights[:, action]
            )
        return values
    
    def _epsilon_greedy(self, values, actions, epsilon=0.1):
        if np.random.random() < epsilon:
            return np.random.choice(actions)
        return actions[np.argmax(values)]
    
    def reinforce(self, state, action, reward):
        """Reinforce successful action via STDP."""
        if reward > 0:
            # Simulate pre-post spike pairing for potentiation
            pre_spikes = np.zeros(self.state_to_hidden.weights.shape[0])
            pre_spikes[state] = 1.0
            post_spikes = np.zeros(self.hidden_to_action.weights.shape[1])
            post_spikes[action] = 1.0
            self.state_to_hidden.update(pre_spikes, np.zeros_like(pre_spikes))
            self.hidden_to_action.update(np.zeros_like(post_spikes), post_spikes)
```

## Memristive Hardware Mapping

Map STDP to memristive VTEAM model for crossbar implementation:

```python
def vteam_update(conductance, voltage_pulse, duration):
    """
    VTEAM memristive model update.
    
    Args:
        conductance: Current conductance state
        voltage_pulse: Applied voltage
        duration: Pulse duration
    
    Returns:
        Updated conductance
    """
    k_on = 10.0  # ON state parameter
    k_off = 10.0  # OFF state parameter
    w_c = 0.1  # Critical window
    
    # Window function
    window = 1.0 - (conductance / 1.0) ** 2 if voltage_pulse > 0 else conductance ** 2
    
    # Conductance change
    dg = k_on * voltage_pulse * window * duration
    conductance = np.clip(conductance + dg, 0.0, 1.0)
    
    return conductance
```

## Performance Metrics

| Metric | SNAN | Baseline |
|--------|------|----------|
| Path length reduction | up to 6× | 1× |
| Goal completion rate | High | Low |
| Speed per area (memristive) | 10× CPU | 1× CPU |
| Energy per decision (memristive) | 10× CPU | 1× CPU |

## Applications

- **Neuromorphic robotics**: Efficient navigation on edge devices
- **Edge-AI systems**: Low-power autonomous agents
- **SLAM variants**: Exploration with memory constraints
- **Topological-context memory**: New working memory paradigm

## Related Skills

- spiking-neural-network-analysis — SNN paper analysis
- snn-working-memory-heterogeneous-delays — Working memory in SNNs
- neuromorphic-spiking-ring-attractor-v2 — Neuromorphic ring attractor

