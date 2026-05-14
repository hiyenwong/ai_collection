---
name: fits-interpretable-spiking-neuron
description: >
  FiTS (Frequency Selectivity and Temporal Shaping) interpretable spiking neuron methodology.
  Factorizes temporal computation within each spiking neuron into Frequency Selectivity (FS)
  and Temporal Shaping (TS) modules. FS parameterizes each neuron's target frequency as the
  maximizer of its subthreshold magnitude response; TS reshapes when frequency components
  contribute to membrane voltage accumulation through group-delay modulation.
  Use when designing interpretable SNN neurons, auditory processing SNNs, frequency-selective
  spiking models, or when needing neuron-level interpretability in temporal SNNs.
  Trigger words: FiTS, frequency selectivity spiking neuron, interpretable SNN, temporal shaping,
  group-delay modulation SNN, auditory spiking neural network, SHD SSC benchmarks.
---

# FiTS: Interpretable Spiking Neurons via Frequency Selectivity and Temporal Shaping

**Paper**: Choi & Chung (KAIST), arXiv:2605.13071, May 2026

## Core Idea

FiTS factorizes neuron-level temporal computation into two explicit mechanisms:

1. **Frequency Selectivity (FS)**: Parameterizes each neuron's target frequency as the maximizer
   of its subthreshold magnitude response. Motivated by intrinsic neuronal resonance.
2. **Temporal Shaping (TS)**: Reshapes *when* frequency components contribute to pre-spike
   membrane voltage through group-delay modulation.

This allows individual neurons to specialize in specific frequency bands and timing roles,
providing interpretable neuron-level summaries without requiring recurrent connections or
network-level delays.

## FiTS Neuron Architecture

### FS Module (Frequency Selectivity)

The FS module uses a resonator-style update that creates a bandpass frequency response:

```
V0[k+1] = (1 - μΔt)·V[k] - ηΔt·a[k] + I[k]    # resonant membrane
a[k+1]  = (1 - ρΔt)·a[k] + γΔt·V0[k+1]         # adaptive variable
```

- The **target frequency** f* is the maximizer of the subthreshold magnitude response
- Learnable parameters control the resonant frequency per neuron
- Each neuron specializes to a specific frequency band

### TS Module (Temporal Shaping)

The TS module applies cascaded delays with learnable group-delay shifts:

```
Vm[k+1] = βm·(Vm[k] - Vm-1[k+1]) + Vm-1[k]     for m = 1..M
Ṽm[k+1] = (1 - λm)·Ṽm-1[k+1] + λm·Vm[k+1]     delay modulation
```

- M cascaded stages create a delay chain
- λm parameters modulate group delay, reshaping temporal contributions
- Provides explicit control over timing of frequency component contributions

### Spike Generation

```
S[k+1] = Θ(eVM[k+1] - Vth)     # threshold crossing
V[k+1] = eVM[k+1] - S[k+1]·Vth # reset
```

## Discrete-Time Update Algorithm

```
Input:  V[k], a[k], {Vm[k]}m=0..M, I[k]
Output: V[k+1], a[k+1], {Vm[k+1]}m=0..M, S[k+1]

FS module:
  1. V0[k+1] ← (1-μΔt)V[k] - ηΔt·a[k] + I[k]
  2. a[k+1]  ← (1-ρΔt)a[k] + γΔt·V0[k+1]

TS module:
  3. Ṽ0[k+1] ← V0[k+1]
  4. for m = 1 to M:
       Vm[k+1]  ← βm(Vm[k] - Vm-1[k+1]) + Vm-1[k]
       Ṽm[k+1] ← (1-λm)Ṽm-1[k+1] + λm·Vm[k+1]

Spike:
  5. S[k+1] ← Θ(eVM[k+1] - Vth)
  6. V[k+1] ← eVM[k+1] - S[k+1]·Vth
```

## Key Advantages

- **Interpretability**: Learned target frequencies and group-delay shifts provide explicit
  neuron-level summaries of frequency/timing organization
- **No recurrence needed**: Outperforms LIF in feedforward networks without recurrent connections
- **Competitive with strong baselines**: Matches recurrent SNNs with delay mechanisms on auditory tasks
- **Simple architecture**: Works with basic feedforward SNNs

## Benchmarks

| Dataset | Description |
|---------|-------------|
| SHD | Spiking Heidelberg Digits (20-class, 10ms resolution) |
| SSC | Spiking Speech Commands |
| GSC | Google Speech Commands (non-spiking) |

## Implementation Guide

### When to Use FiTS

- Auditory/speech processing tasks with temporal structure
- Needing interpretable frequency-selective neurons
- Feedforward SNNs where recurrence/delays are undesirable
- Analyzing frequency organization learned by SNNs

### Comparison with Baselines

| Model | Recurrence | Delays | Key Difference |
|-------|-----------|--------|----------------|
| LIF | No | No | Simple leaky integrator |
| RadLIF | Yes | No | Recurrent LIF |
| SE-adLIF | Yes | No | Adaptive LIF with state expansion |
| **FiTS** | **No** | **No** | **FS + TS within each neuron** |

### Training

- Train with standard backpropagation through time (BPTT)
- Surrogate gradients for spike function (e.g., sigmoid surrogate)
- Target frequencies and group delays are learned end-to-end

## Activation Keywords

- FiTS, fits-interpretable-spiking-neuron
- frequency selectivity spiking neuron
- interpretable SNN, temporal shaping SNN
- group-delay modulation spiking
- auditory spiking neural network
- SHD SSC benchmarks SNN
- neuron-level interpretability temporal SNN
