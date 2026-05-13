---
name: multi-timescale-conductance-snn
description: >
  Multi-Timescale Conductance Spiking Networks (MTCSN) — a sparse, gradient-trainable SNN framework
  with rich firing dynamics for enhanced temporal processing. Neurons shaped by fast/slow/ultra-slow
  conductances enabling exact BPTT without surrogate gradients. Use when designing spiking neural
  networks for temporal tasks, neuromorphic regression, energy-aware computing, or when needing
  controllably diverse firing regimes (tonic/phasic/bursting) in a single model.
  arXiv: 2605.11835 (cs.NE, cs.AI, cs.LG). Fulleda-Garcia, Soldado-Magraner, Margarit-Taulé.
---

# Multi-Timescale Conductance Spiking Networks

Gradient-trainable SNN framework using multi-timescale conductance dynamics for rich,
controllable firing behavior and enhanced temporal processing.

**Source**: arXiv 2605.11835v1 (2026-05-12), cs.NE / cs.AI / cs.LG. IEEE Neuro-IC 2026.

## Core Problem

Standard SNN neuron models (LIF, AdLIF) face a trilemma:

1. **Trainability** — surrogate gradients are approximations, degrading optimization
2. **Dynamical richness** — simple phenomenological models lack firing diversity
3. **Sparsity** — dense firing wastes energy, undermining SNN efficiency

This is especially critical for **regression tasks** where spike discretization and
approximation error severely degrade continuous-valued outputs.

## Conductance-Based Neuron Model

### Multi-Timescale Current-Voltage Shaping

The key insight: neural dynamics emerge from shaping the **I-V curve** by tuning
multiple conductances operating at different timescales:

```
C dV/dt = -g_leak(V - E_leak) - Σ g_i(t)(V - E_i) + I_syn(t)
```

where conductances g_i(t) operate at:
- **Fast** (ms): immediate synaptic responses
- **Slow** (10s of ms): adaptation, spike-frequency adaptation
- **Ultra-slow** (100s of ms): longer-term modulation

### Emergent Firing Regimes

A single neuron model produces diverse firing patterns by tuning conductance parameters:

| Regime | Description | Typical conductance config |
|--------|-------------|---------------------------|
| **Tonic** | Sustained firing during stimulation | Balanced fast/slow |
| **Phasic** | Transient burst at stimulus onset | Strong slow conductance |
| **Bursting** | Clusters of spikes separated by silence | Ultra-slow modulation |

## Exact Backpropagation Through Time

### Key Advantage over Surrogate Gradients

Standard SNNs use surrogate gradients because the spike function is non-differentiable.
MTCSN derives a **discrete-time formulation** where the dynamics are fully differentiable,
enabling **exact BPTT** without approximation.

### Discrete-Time Formulation

```python
# Simplified discrete-time update
def mtcsn_step(state, inputs, params):
    # Update fast conductance
    g_fast = decay_fast * g_fast + syn_fast * inputs
    # Update slow conductance  
    g_slow = decay_slow * g_slow + syn_slow * inputs
    # Update ultra-slow conductance
    g_ultraslow = decay_uslow * g_ultraslow + syn_uslow * inputs
    # Compute membrane potential
    V = update_potential(state.V, g_fast, g_slow, g_ultraslow, inputs, params)
    # Spike generation (differentiable formulation)
    spike, state = compute_spike(V, state, params)
    return state, spike
```

This enables gradient flow through the entire temporal trajectory without the
information loss introduced by surrogate gradient approximations.

## Performance Results

### Mackey-Glass Time-Series Regression

Evaluated at the **predictability limit** (maximally difficult regime):

| Model | Performance | Sparsity |
|-------|-------------|----------|
| LIF   | Baseline    | Moderate |
| AdLIF | Improved    | Moderate |
| **MTCSN** | **Best** | **Highest** |

- Outperforms both LIF and AdLIF baselines
- Substantially sparser activity (both communication and computational sparsity)
- Suitable for analog circuit implementation

## When to Use This Framework

1. **Temporal regression tasks** — time-series prediction, continuous-valued outputs
2. **Neuromorphic hardware design** — conductance model maps naturally to analog circuits
3. **Energy-constrained deployment** — higher sparsity reduces communication costs
4. **When surrogate gradients are insufficient** — need exact gradients for optimization quality

## Comparison with Standard SNN Models

| Feature | LIF | AdLIF | MTCSN |
|---------|-----|-------|-------|
| Trainable via exact BPTT | ❌ | ❌ | ✅ |
| Multiple firing regimes | ❌ | Limited | ✅ |
| Controllable dynamics | ❌ | Single parameter | Multiple conductances |
| Hardware-friendly | ✅ | ✅ | ✅ (analog) |
| Activity sparsity | Moderate | Moderate | High |

## Activation Keywords

- multi-timescale conductance, MTCSN, conductance SNN
- exact BPTT spiking network, gradient-trainable SNN
- surrogate gradient alternative, rich firing dynamics
- neuromorphic regression, temporal processing SNN
- tonic phasic bursting neuron, energy-aware SNN

## Tools Used

- Custom neuron model implementation (PyTorch/JAX compatible)
- BPTT through discrete-time conductance dynamics
- Standard SNN benchmarks (Mackey-Glass, event-based vision)

## Related Skills

- `surrogate-gradient-snn-training` — the approach MTCSN replaces
- `spiking-neural-network-analysis` — general SNN analysis patterns
- `snn-performance-analysis` — evaluation methodology for SNNs
- `snn-fpga-hardware-software-codesign` — neuromorphic implementation patterns
- `multi-timescale-conductance-snn` — same model, different angle
