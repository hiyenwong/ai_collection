---
name: multi-timescale-conductance-spiking-networks
description: >
  Multi-Timescale Conductance (MTC) Spiking Networks — gradient-trainable framework
  with rich firing dynamics for enhanced temporal processing. Conductance-based neuron
  model with fast/slow/ultra-slow timescales enables tonic, phasic, and bursting
  responses within a single model. Trainable via standard BPTT without surrogate gradients.
  Activation: multi-timescale conductance, MTC spiking network, conductance-based neuron,
  spiking neural network regression, surrogate-free SNN training, I-V curve shaping,
  neuromorphic analog circuits, Mackey-Glass forecasting SNN
---

# Multi-Timescale Conductance (MTC) Spiking Networks

Paper: arXiv:2605.11835v1 (May 12, 2026)
Authors: Alex Fulleda-Garcia, Saray Soldado-Magraner, Josep Maria Margarit-Taulé
Affiliations: IMB-CNM/CSIC (Spain), UCLA (USA)

## Core Problem

Standard SNN neuron models (LIF, AdLIF) face a fundamental trade-off:
- **Gradient trainability** — requires smooth dynamics
- **Dynamical richness** — biological neurons exhibit diverse firing modes
- **Activity sparsity** — energy efficiency requires sparse spiking

LIF models sacrifice biophysical realism; surrogate gradients create forward-backward mismatch,
especially damaging for continuous-valued temporal regression.

## MTC Neuron Model

### Circuit Foundation

Based on Ribar & Sepulchre (2019) conductance-based framework. Neuron excitability controlled
by shaping the I-V (current-voltage) curve via parallel conductance elements at different timescales.

### Governing Equations

**State variables (filtered voltages):**
```
τx · dUx/dt = -Ux + Um  (for each timescale x)
Ix±(t) = ±αx± · tanh(Ux - δx±)
```

**Membrane potential dynamics:**
```
τm · dUm/dt = -(Um - Urest) + R·Iin(t) - R·Σ Ix±(t)
```

### Three Timescale Conductances

| Timescale | Role | Effect |
|-----------|------|--------|
| **Fast (τf)** | Negative conductance If− | Creates negative differential resistance → drives rapid depolarization (upstroke) |
| **Slow (τs)** | Positive conductance Is+ | Damping force → recovery + refractory period |
| **Ultra-slow (τus)** | Slow negative + ultra-slow positive | Enables bursting, higher-order temporal processing |

### Firing Regimes

By tuning conductance parameters, the same model produces:
- **Tonic Spiking** — sustained firing to constant input
- **Tonic Bursting** — sustained clusters of spikes
- **Phasic Spiking** — transient response to input onset
- **Phasic Bursting** — transient burst responses

## Key Innovation: Differentiable Spiking

Unlike LIF's hybrid continuous-discrete nature (hard threshold + reset),
MTC produces spikes through **fully derivable nonlinear dynamics**.

### Signal Conditioning (Semi-Digital Communication)
```
s(t) = min(ReLU(Um(t) - Uth) / (Usat - Uth), 1)
```

This provides:
1. **Signal standardization** — normalizes spike amplitudes to [0,1]
2. **Semi-digital sparsity** — suppresses sub-threshold activity while retaining continuous slope
   information during rising phase (needed for exact gradients)
3. **Synaptic transduction model** — approximates nonlinear neurotransmitter release

## Training: No Surrogate Gradients Needed

- **MTC**: Standard BPTT through continuous conductance state variables
- **LIF**: Requires surrogate gradient (ArcTan derivative in snnTorch)
- **AdLIF**: Requires SLAYER surrogate gradient (α=5)

The conductance states provide smooth internal representations, avoiding the
spike discretization problem that necessitates surrogate gradients.

## Experimental Results: Mackey-Glass Time Series

**Task**: Chaotic time series forecasting at predictability horizon (1 Lyapunov time)
**Architecture**: Feedforward SNN, 4 stages (input projection → spiking hidden layer → linear readout → low-pass filter)

**Key findings**:
- MTC outperforms LIF and SOTA AdLIF baselines in regression accuracy
- MTC operates in considerably sparser regime (both rate and duty-cycle dimensions)
- Dynamic sparsity emerges from single-neuron excitability tuning, not loss regularization
- Aligns with neuromorphic vision of energy-efficient intelligent perception

## Hardware Implementation Advantages

1. **Analog circuit compatible** — conductance elements implementable with compact transconductance blocks (subthreshold MOS)
2. **I-V curves need not be exact tanh** — any approximately monotone nonlinearity works
3. **Multi-timescale dynamics** naturally map to neuromorphic hardware with different RC constants
4. **No surrogate gradient overhead** — eliminates backward pass approximation circuitry

## Comparison with Baselines

| Property | LIF | AdLIF | MTC (this work) |
|----------|:---:|:-----:|:---:|
| Firing regimes | Tonic only | Tonic + some adaptation | Tonic, phasic, bursting |
| Surrogate gradient needed | ✓ | ✓ | ✗ |
| Timescale control | 1 (membrane) | 2 (membrane + adaptation) | 3+ (fast, slow, ultra-slow) |
| I-V curve shaping | No | No | Yes |
| Analog circuit mapping | Simple | Moderate | Natural |
| Sparsity mechanism | Threshold/loss reg | Threshold/loss reg | Intrinsic excitability |

## Activation Context

Use this skill when:
- Designing neuron models with rich firing dynamics for temporal processing
- Building SNNs that avoid surrogate gradient approximations
- Implementing neuromorphic circuits with conductance-based dynamics
- Tackling continuous-valued temporal regression with spiking networks
- Studying the trade-off between trainability, dynamical richness, and sparsity
