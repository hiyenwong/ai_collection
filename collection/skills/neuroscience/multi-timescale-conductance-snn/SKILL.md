---
name: multi-timescale-conductance-snn
description: >
  Multi-Timescale Conductance Spiking Networks (MTC-SNN) methodology for energy-aware temporal
  processing. Introduces gradient-trainable spiking neurons using fast/slow/ultra-slow conductances
  to shape I-V curves, enabling direct backpropagation through time (no surrogate gradients).
  Rich firing regimes (tonic, phasic, bursting) within single model. Outperforms LIF and AdLIF
  on Mackey-Glass time-series regression with substantially sparser activity.
  Activation: multi-timescale conductance, MTC-SNN, conductance spiking, gradient-trainable SNN,
  I-V curve shaping, spiking neuron dynamics, temporal processing SNN, surrogate-free SNN training
---

# Multi-Timescale Conductance Spiking Networks (MTC-SNN)

## Overview

MTC-SNN (arXiv:2605.11835) introduces a gradient-trainable spiking neural network framework
where neural dynamics emerge from shaping the current-voltage (I-V) curve via tunable
fast, slow, and ultra-slow conductances. Published at IEEE Neuro-Inspired Computational
Elements Conference (NeuroInspire 2026, Atlanta, USA).

**Authors**: Alex Fulleda-Garcia, Saray Soldado-Magraner, Josep Maria Margarit-Taulé

## Core Problem

Standard SNN neuron models (LIF, AdLIF) face a fundamental trade-off:
- Gradient-based trainability vs dynamical richness vs activity sparsity
- Acute in regression: approximation error, noise, spike discretization degrade continuous outputs
- SOTA SNNs rely on simple phenomenological dynamics + surrogate gradients
- Limited control over spiking diversity and sparsity

## Key Innovation: Conductance-Based Neurons

### Multi-Timescale Conductance Parametrization

Neural dynamics emerge from I-V curve shaping via three conductance timescales:
- **Fast conductance**: rapid response dynamics
- **Slow conductance**: medium-term adaptation
- **Ultra-slow conductance**: long-term behavioral modulation

Benefits:
- Systematic control over excitability
- Efficient analog circuit implementation
- Rich firing regimes in single model: tonic, phasic, bursting

### Discrete-Time Differentiable Formulation

- Derive discrete-time version of conductance dynamics
- Direct backpropagation through time (BPTT) — **no surrogate-gradient approximations**
- End-to-end gradient training of neuron parameters

## Performance Results

### Mackey-Glass Time-Series Regression (predictability limit)

- Outperforms both LIF and SOTA AdLIF baselines
- Substantially sparser activity (communication + computational perspectives)
- Energy-aware temporal processing suitable for neuromorphic deployment

### Sparsity Metrics

- Communication sparsity: fewer spikes for equivalent task performance
- Computational sparsity: sparse internal state updates

## Implementation Pattern

```python
# Conceptual structure of MTC neuron
class MTCNeuron:
    """Multi-timescale conductance neuron."""
    def __init__(self):
        self.g_fast = ...    # Fast conductance parameter
        self.g_slow = ...    # Slow conductance parameter  
        self.g_ultra_slow = ... # Ultra-slow conductance parameter
        self.v_membrane = 0.0
        self.spike_threshold = 1.0
    
    def step(self, input_current, dt):
        # Update membrane potential via conductance-based dynamics
        # Shape I-V curve through g_fast, g_slow, g_ultra_slow
        # Emit spike if v_membrane > threshold
        # Differentiable for BPTT
        pass
```

### Training

```python
# Standard BPTT — no surrogate gradients needed
loss = criterion(predicted, target)
loss.backward()  # gradients flow through conductance dynamics
optimizer.step()
```

## When to Use

- Temporal processing tasks (time-series, sequence modeling)
- Energy-efficient / neuromorphic deployment
- Regression tasks where spike discretization is problematic
- Applications requiring diverse firing patterns (tonic/phasic/bursting)
- Analog neuromorphic hardware implementation

## Comparison with Alternatives

| Model | Trainability | Firing Richness | Sparsity |
|-------|-------------|-----------------|----------|
| LIF | Surrogate gradient | Limited (tonic only) | Low |
| AdLIF | Surrogate gradient | Moderate | Moderate |
| **MTC-SNN** | **Direct BPTT** | **Rich (3 regimes)** | **High** |

## Related Papers from Same Search

- **FiTS** (2605.13071): Interpretable spiking neurons via frequency selectivity
- **LSFormer** (2605.13887): Breaking self-attention bottlenecks in transformer-SNNs
- **NeuroTrain** (2605.15058): Survey + benchmark of local learning rules for SNNs
- **SpikeProphecy** (2605.12992): Benchmark for autoregressive neural population forecasting

## Pitfalls

- Conductance parameters require careful initialization
- Analog circuit implementation needs precise conductance tuning
- Discrete-time formulation introduces discretization error — validate timestep sensitivity
