---
name: multi-timescale-conductance-snn
description: >
  Multi-Timescale Conductance Spiking Networks (MTCSN) methodology. A gradient-trainable
  SNN framework where neural dynamics emerge from shaping the I-V curve via fast, slow,
  and ultra-slow conductances. Enables rich firing regimes (tonic, phasic, bursting) with
  direct backpropagation through time — no surrogate gradients needed.
  Outperforms LIF and AdLIF on temporal regression with sparser activity.
  Trigger: multi-timescale spiking, conductance SNN, gradient-trainable SNN,
  temporal processing SNN, Mackey-Glass SNN, I-V curve shaping.
---

# Multi-Timescale Conductance Spiking Networks (MTCSN)

## Source
- **Paper**: Multi-Timescale Conductance Spiking Networks: A Sparse, Gradient-Trainable Framework with Rich Firing Dynamics for Enhanced Temporal Processing
- **arXiv**: 2605.11835v1
- **Date**: 2026-05-12

## Core Innovation

Traditional SNNs face a fundamental trilemma: gradient-based trainability, dynamical richness, and high activity sparsity are mutually incompatible. Most SOTA SNNs use simple phenomenological dynamics (LIF/AdLIF) trained with surrogate gradients, offering limited control over spiking diversity and sparsity.

MTCSN resolves this by modeling neural dynamics through **multi-timescale conductance shaping**:

### Key Insight
Neural excitability emerges from the current-voltage (I-V) curve, which can be systematically controlled by tuning three conductance components:
- **Fast conductance**: Immediate response, spike initiation
- **Slow conductance**: Adaptation, refractory behavior
- **Ultra-slow conductance**: Long-term modulation, bursting patterns

This allows a **single model** to exhibit tonic, phasic, and bursting responses — firing regimes that typically require separate neuron models.

## Methodology

### 1. Multi-Timescale Conductance Formulation

```
I_total = g_fast * (V - E_fast) + g_slow * (V - E_slow) + g_ultra_slow * (V - E_ultra)
```

Where each conductance g_i evolves on its own timescale τ_i:
- τ_fast ~ 1-5 ms (membrane dynamics)
- τ_slow ~ 10-50 ms (adaptation)
- τ_ultra_slow ~ 100-500 ms (bursting/modulation)

### 2. Discrete-Time Differentiable Dynamics

Unlike traditional SNNs requiring surrogate gradients for spike differentiability, MTCSN derives a **discrete-time formulation** that is inherently differentiable:

```python
# Pseudo-code for one timestep
V_t = V_{t-1} + dt/C * (I_syn - I_conductance_fast - I_conductance_slow - I_conductance_ultra_slow)
g_fast_t = g_fast_{t-1} * exp(-dt/τ_fast) + Δg_fast(spike)
g_slow_t = g_slow_{t-1} * exp(-dt/τ_slow) + Δg_slow(spike)
g_ultra_slow_t = g_ultra_slow_{t-1} * exp(-dt/τ_ultra_slow) + Δg_ultra_slow(spike)
```

### 3. Direct Backpropagation Through Time (BPTT)

- **No surrogate gradient approximation needed** — the discretized dynamics are differentiable by construction
- Spikes emerge naturally from the conductance dynamics rather than being imposed by a threshold function
- Gradient flow is stable due to the natural timescale separation (ultra-slow conductances prevent vanishing gradients)

### 4. I-V Curve Parametrization

The conductance parameters directly shape the I-V curve, providing interpretable control over:
- **Rheobase current** (minimum current to spike)
- **Firing rate adaptation** (via slow conductance)
- **Bursting patterns** (via ultra-slow conductance resonance)
- **Spike-frequency adaptation**

## Advantages

| Property | LIF | AdLIF | MTCSN |
|----------|-----|-------|-------|
| Gradient trainability | Surrogate | Surrogate | Direct BPTT |
| Firing regime diversity | Single | Limited | Rich (tonic/phasic/bursting) |
| Activity sparsity | Moderate | Moderate | High |
| Circuit implementability | Yes | Yes | Yes (analog) |
| Interpretability | Low | Low | High (conductance parameters) |

## Evaluation Results

- **Task**: Mackey-Glass time-series regression (at predictability limit)
- **Baseline**: LIF and AdLIF networks
- **Result**: MTCSN outperforms both baselines with **substantially sparser activity**
- Sparsity benefit is dual: communication (fewer spikes transmitted) and computation (fewer active neurons)

## Applications

1. **Temporal regression tasks**: Time-series prediction, system identification
2. **Neuromorphic hardware**: Analog circuit implementation (conductance-based design maps naturally to physical components)
3. **Energy-aware computing**: Sparse activity reduces energy consumption
4. **Neuroscience modeling**: Biophysically interpretable parameters for studying neural coding

## Implementation Notes

### When to Use
- Temporal processing tasks requiring rich dynamics
- When surrogate gradient instability is a concern
- When activity sparsity is critical (edge/neuromorphic deployment)
- When interpretability of neuron dynamics matters

### When Not to Use
- Simple classification tasks where LIF suffices
- When computational overhead of multi-timescale dynamics is prohibitive
- When the task doesn't benefit from diverse firing patterns

### Key Parameters to Tune
- Timescale ratios (τ_slow/τ_fast, τ_ultra_slow/τ_fast)
- Conductance strengths relative to membrane capacitance
- Number of conductance types (3 is minimum for rich dynamics)

## Activation Keywords
- multi-timescale spiking
- conductance SNN
- gradient-trainable SNN
- temporal processing SNN
- Mackey-Glass SNN
- I-V curve shaping
- conductance-based neuron model
- direct BPTT SNN
- multi-timescale conductance

## Related Skills
- spiking-neural-network-analysis
- spikingjelly-framework
- surrogate-gradient-snn-training
- snn-performance-analysis
