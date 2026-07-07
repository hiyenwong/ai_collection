---
name: temporal-interference-stimulation-mathematical
description: "Mathematical framework for analyzing Temporal Interference Stimulation (TIS) using FitzHugh-Nagumo model with phase-plane analysis and geometric singular perturbation theory. Use when: modeling non-invasive neuromodulation, analyzing TIS neural activation, designing deep brain stimulation protocols, bifurcation analysis of driven neurons, phase-plane analysis of oscillatory stimulation. Activation: temporal interference stimulation, TIS neuromodulation, FitzHugh-Nagumo TIS, geometric singular perturbation neural, deep brain stimulation mathematical, beat frequency neuron activation."
---

# Mathematical Characterization of Temporal Interference Stimulation

> Mathematical framework integrating phase-plane analysis and geometric singular perturbation theory to characterize when TIS elicits action potentials in FitzHugh-Nagumo neurons, mapping amplitude-frequency parameter space to quiescent/transient/tonic firing regimes.

## Metadata
- **Source**: arXiv:2605.16761
- **Authors**: Esteban Paduro, Antoine Chaillet, Mario Sigalotti
- **Published**: 2026-05-16
- **MSC Classes**: 37N25, 92-10

## Core Problem

TIS uses two high-frequency sinusoidal currents with slightly different frequencies to generate a low-frequency envelope that activates deep neural structures non-invasively. What mathematical conditions determine whether TIS elicits sustained neural activation?

## Methodology: Phase-Plane + Geometric Singular Perturbation

### Key Innovation
First rigorous mathematical framework (beyond simulation) for analyzing TIS-induced neural activation using dynamical systems theory.

### FitzHugh-Nagumo + TIS Driving

The standard FHN system is driven by the TIS beat signal:
- Two high-frequency currents: ω₁ and ω₂ (ω₁ ≈ ω₂)
- Beat frequency: Δω = |ω₁ - ω₂| (low-frequency envelope)
- Envelope amplitude depends on both input amplitudes

### Three Firing Regimes

Mathematical analysis reveals three distinct regimes based on (amplitude, beat frequency) parameters:

1. **Quiescent**: Neuron remains at rest — envelope too weak to cross activation threshold
2. **Transient**: Brief response but no sustained firing — envelope crosses threshold momentarily
3. **Tonic (Persistent)**: Sustained firing — envelope maintains neuron in oscillatory regime

### Analysis Tools

**Phase-Plane Analysis**
- Nullcline geometry reveals bifurcation boundaries
- Fixed point stability analysis determines activation threshold
- Limit cycle emergence marks transition to tonic firing

**Geometric Singular Perturbation**
- Separates fast (membrane potential) and slow (recovery) timescales
- Slow manifold analysis reveals critical transitions
- Canavard explosion boundaries between regimes

## Implementation Guide

### Prerequisites
- Python with scipy, numpy
- Understanding of dynamical systems theory

### Step-by-Step

1. **Model Setup**
   ```python
   def fhn_tis(v, w, t, params):
       # FHN dynamics + TIS driving
       eps, a, b = params['eps'], params['a'], params['b']
       A1, A2, w1, w2 = params['A1'], params['A2'], params['w1'], params['w2']
       
       tis_signal = A1*np.sin(w1*t) + A2*np.sin(w2*t)
       dv = (v - v**3/3 - w + tis_signal) / eps
       dw = v + a - b*w
       return dv, dw
   ```

2. **Parameter Space Exploration**
   ```python
   # Sweep amplitude and beat frequency
   for A in amplitude_range:
       for dw in beat_freq_range:
           regime = classify_firing_regime(A, dw)
           # quiescent / transient / tonic
   ```

3. **Bifurcation Analysis**
   ```python
   # Use AUTO or PyDSTool for continuation
   # Track fixed point stability vs TIS parameters
   # Identify Hopf/saddle-node bifurcation boundaries
   ```

## Applications
- Non-invasive deep brain stimulation protocol design
- Optimizing TIS parameters for specific neural targets
- Understanding neural activation thresholds
- Computational neuroscience education

## Pitfalls
- **FHN simplification**: Single-neuron model ignores network effects
- **Sinusoidal assumption**: Real TIS may have non-ideal waveforms
- **Parameter sensitivity**: Small changes near bifurcation boundaries cause regime switches
- **No validation**: Mathematical framework needs experimental verification

## Related Skills
- neural-dynamics-decision-making
- tms-eeg-biomarkers
- rl-closed-loop-eeg-tms