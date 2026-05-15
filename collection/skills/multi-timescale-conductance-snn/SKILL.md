---
name: multi-timescale-conductance-snn
description: "Multi-timescale conductance spiking neural network methodology for gradient-trainable SNNs with rich firing dynamics. Shapes current-voltage (I-V) curve by tuning fast, slow and ultra-slow conductances, enabling systematic control over excitability, tonic/phasic/bursting responses, and direct backpropagation through time without surrogate gradients. Use when: (1) training SNNs for temporal processing or regression tasks, (2) designing gradient-trainable spiking neurons, (3) controlling firing diversity and sparsity, (4) neuromorphic hardware implementation, (5) comparing conductance-based neurons to LIF/AdLIF models."
---

# Multi-Timescale Conductance Spiking Networks

## Overview

Multi-timescale conductance spiking networks (MTCSN) provide a gradient-trainable SNN framework where neural dynamics emerge from shaping the I-V curve via tunable conductances at multiple timescales. Yields rich firing regimes (tonic, phasic, bursting) and enables direct BPTT without surrogate gradients.

**Paper**: Fulleda-Garcia et al., "Multi-Timescale Conductance Spiking Networks: A Sparse, Gradient-Trainable Framework with Rich Firing Dynamics for Enhanced Temporal Processing" (arXiv: 2605.11835)

## Key Contributions

### 1. Conductance-Based Neuron Model

Instead of fixed phenomenological dynamics, neuron behavior emerges from:
- **Fast conductance**: rapid depolarization (spike initiation)
- **Slow conductance**: adaptation / recovery
- **Ultra-slow conductance**: long-term excitability modulation

Each conductance has:
- Reversal potential `E_rev`
- Time constant `τ`
- Conductance strength `g`

### 2. I-V Curve Shaping

By tuning conductance parameters, the I-V curve is systematically shaped to produce:
- **Tonic firing**: sustained regular spiking
- **Phasic firing**: transient response then silence
- **Bursting**: clusters of spikes separated by silent periods

This provides rich dynamical repertoire from a **single unified model**.

### 3. Discrete-Time Differentiable Formulation

Key innovation: derive discrete-time formulation enabling **direct backpropagation through time (BPTT)** without surrogate gradient approximations.

Standard SNN training uses surrogate gradients because the spike function is non-differentiable. MTCSN circumvents this by:
- Expressing dynamics as differentiable recurrence
- Treating membrane potential evolution as continuous differentiable function
- Spike generation as event from the differentiable trajectory

### 4. Performance Results

Evaluated on **Mackey-Glass time-series regression** (predictability limit):
- **Outperforms LIF networks** significantly
- **Outperforms SOTA AdLIF networks**
- **Substantially sparser activity** from both communication and computational perspectives

## Mathematical Framework

### Conductance Dynamics

```
C dV/dt = -g_L(V - E_L) - Σ_k g_k(t)(V - E_k) + I_syn + I_ext
```

Where each conductance evolves:
```
τ_k dg_k/dt = -g_k + Σ_j w_kj · spike_j(t) + g_k_baseline
```

### Discrete-Time BPTT

1. Discretize continuous dynamics: `V[t+1] = f(V[t], g[t], I[t])`
2. Compute gradients: `∂L/∂w = Σ_t (∂L/∂V[t]) · (∂V[t]/∂w)`
3. Chain rule through the differentiable recurrence
4. No surrogate gradient needed — the membrane potential trajectory is smooth

## Implementation Guide

### Core Components

```python
# Simplified pseudocode
class MTCSNeuron:
    def __init__(self, tau_fast, tau_slow, tau_ultra_slow):
        self.conductances = {
            'fast':   {'tau': tau_fast,   'E_rev': E_Na,  'g': 0.0},
            'slow':   {'tau': tau_slow,   'E_rev': E_K,   'g': 0.0},
            'ultra':  {'tau': tau_ultra,  'E_rev': E_slow, 'g': 0.0},
        }
    
    def step(self, V, input_current, dt):
        # Update each conductance
        for name, params in self.conductances.items():
            params['g'] += dt/params['tau'] * (-params['g'] + synaptic_input[name])
        
        # Update membrane potential
        I_leak = g_L * (V - E_L)
        I_cond = sum(p['g'] * (V - p['E_rev']) for p in self.conductances.values())
        dV = dt/C * (-I_leak - I_cond + input_current)
        V_new = V + dV
        
        # Spike generation
        spike = V_new > V_threshold
        if spike: V_new = V_reset
        return V_new, spike
```

### Training Loop

```python
def train_mtcsn(network, data, epochs=100, lr=1e-3):
    for epoch in range(epochs):
        V_states = []
        spikes = []
        
        # Forward pass (differentiable)
        V, g = init_state()
        for t in range(seq_len):
            V, spike = network.step(V, g, input[t])
            V_states.append(V)
            spikes.append(spike)
        
        # Compute loss on membrane potentials / spike counts
        loss = criterion(V_states, target)
        
        # Backward pass (standard BPTT)
        loss.backward()
        optimizer.step()
```

## Comparison: MTCSN vs LIF vs AdLIF

| Property | LIF | AdLIF | MTCSN |
|----------|-----|-------|-------|
| Firing regimes | Tonic only | Limited adaptation | Tonic, phasic, bursting |
| Gradient training | Surrogate | Surrogate | **Direct BPTT** |
| Sparsity | Moderate | Moderate | **High** |
| Hardware mapping | Simple | Moderate | **Analog circuit friendly** |
| Parameter count | Low | Medium | Medium-High |
| Expressivity | Low | Medium | **High** |

## Activation Keywords

- multi-timescale conductance SNN
- conductance spiking network
- gradient-trainable SNN
- direct BPTT spiking neurons
- I-V curve shaping
- tonic phasic bursting SNN
- surrogate gradient alternative
- 2605.11835
- MTCSN

## Related Skills

- `surrogate-gradient-snn-training` — standard SNN training approach (MTCSN provides alternative)
- `snn-learning-survey` — comprehensive SNN learning survey
- `spiking-computational-neuroscience-survey` — SNN applications survey
- `chaos-synchrony-ei-networks` — E/I network dynamics
- `three-factor-snn-learning` — three-factor learning rules
