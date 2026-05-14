---
name: multi-timescale-conductance-snn
description: >
  Multi-Timescale Conductance Spiking Networks (MTCSN) methodology — gradient-trainable SNN
  framework with rich firing dynamics. Neural dynamics emerge from shaping the I-V curve by
  tuning fast, slow, and ultra-slow conductances. Supports tonic, phasic, and bursting firing
  regimes within a single model. Discrete-time differentiable formulation enables direct BPTT
  without surrogate gradients. Outperforms LIF and AdLIF on Mackey-Glass time-series regression
  with substantially sparser activity. Use when designing SNNs for regression tasks, neuromorphic
  analog circuits, temporal processing with sparse firing, or when needing differentiable dynamics
  without surrogate gradients. Trigger words: MTCSN, multi-timescale conductance, conductance-based SNN,
  I-V curve shaping SNN, differentiable spiking dynamics, surrogate-gradient-free, Mackey-Glass SNN,
  tonic phasic bursting spiking, AdLIF alternative, energy-aware temporal processing.
---

# Multi-Timescale Conductance Spiking Networks (MTCSN)

**Paper**: Fulleda-Garcia, Soldado-Magraner, Margarit-Taulé (IMB-CNM/CSIC, UCLA), arXiv:2605.11835, May 2026

## Core Problem

Standard SNN neuron models trade off three critical properties:
1. **Gradient-based trainability**
2. **Dynamical richness** (diverse firing patterns)
3. **High activity sparsity**

This is especially acute in **regression tasks**, where approximation error, noise, and spike
discretization degrade continuous-valued outputs. Most SOTA SNNs use simple phenomenological
dynamics with surrogate gradients, offering limited control over spiking diversity and sparsity.

## MTCSN Solution

MTCSN shapes neural dynamics through **multi-timescale conductances**:

- **Fast conductance**: Rapid current response
- **Slow conductance**: Medium-timescale adaptation
- **Ultra-slow conductance**: Long-timescale modulation

The I-V (current-voltage) curve is shaped by tuning these conductances, allowing:
- Systematic control over neuron excitability
- Rich firing regimes: tonic, phasic, bursting within a single model
- Efficient analog circuit implementation

## Key Innovation: Differentiable Without Surrogate Gradients

MTCSN derives a **discrete-time formulation** of conductance-based dynamics that is
**directly differentiable**, enabling:

- Direct backpropagation through time (BPTT)
- No surrogate-gradient approximations needed
- Exact gradient computation through spike generation

This is significant because most conductance-based SNNs require surrogate gradients due
to non-differentiable threshold functions.

## Architecture

### Conductance Dynamics

The membrane voltage dynamics emerge from the shaped I-V curve:

```
C·dV/dt = -g_fast·(V - E_fast) - g_slow·(V - E_slow) - g_ultraslow·(V - E_ultraslow) + I_ext
```

Each conductance has its own timescale:
- τ_fast: Fast synaptic/leak dynamics
- τ_slow: Medium adaptation
- τ_ultraslow: Slow modulatory processes

### Discrete-Time Formulation

The continuous dynamics are discretized for BPTT:
- Euler or higher-order integration scheme
- Spike generation as differentiable event
- Gradient flows through conductance parameters

### Firing Regimes

By tuning conductance parameters, a single MTCSN neuron can exhibit:

| Regime | Behavior | Biological Analog |
|--------|----------|-------------------|
| Tonic | Regular spiking | Cortical pyramidal neurons |
| Phasic | Burst then silence | Thalamic relay neurons |
| Bursting | Clusters of spikes | Thalamic/cortical bursting cells |

## Performance

Evaluated on **Mackey-Glass time-series regression** at the predictability limit:

- **Outperforms** baseline LIF networks
- **Outperforms** SOTA AdLIF (Adaptive LIF) networks
- **Substantially sparser** activity (both communication and computational sparsity)

## Implementation Guide

### When to Use MTCSN

- Time-series regression tasks with SNNs
- Needing diverse firing patterns without architectural changes
- Neuromorphic analog circuit implementations
- Energy-aware temporal processing
- When surrogate gradients are undesirable
- When sparsity is critical

### Comparison with Baselines

| Model | Trainability | Firing Diversity | Sparsity | Surrogate Needed |
|-------|-------------|------------------|----------|------------------|
| LIF | Good | Low (tonic only) | Moderate | Yes |
| AdLIF | Good | Moderate | Moderate | Yes |
| **MTCSN** | **Good** | **High (tonic/phasic/bursting)** | **High** | **No** |

### Training

1. Define conductance parameters (g_fast, g_slow, g_ultraslow) with their timescales
2. Discretize dynamics for BPTT
3. Train with standard MSE/MAE loss for regression
4. Conductance parameters are learned end-to-end

### Hardware Considerations

- Efficiently implementable in **analog neuromorphic circuits**
- Conductance parameters map to physical circuit elements
- Natural fit for memristive or conductance-based neuromorphic chips

## Activation Keywords

- MTCSN, multi-timescale-conductance-snn
- conductance-based spiking neural network
- I-V curve shaping SNN
- differentiable spiking dynamics without surrogate
- tonic phasic bursting spiking neuron
- Mackey-Glass time-series SNN
- AdLIF alternative, energy-aware SNN
- neuromorphic analog circuit SNN
- sparse spiking regression
