---
name: parametric-oscillator-reservoir-computing
description: Neuromorphic reservoir computing using parametrically-driven oscillators and frequency combs. Covers oscillator-based RC, 2:1 parametric resonance regimes, and bifurcation-driven computational capability mapping.
category: neuromorphic-computing
---

# Parametric Oscillator Reservoir Computing

## Overview

This methodology covers neuromorphic computing using **parametrically driven oscillators** as reservoir computers. The key insight is that nonlinear mode coupling and intrinsic dynamics in oscillators enable both memory and high-dimensional transformation — the two essential ingredients of reservoir computing.

**Paper**: "Neuromorphic Computing Based on Parametrically-Driven Oscillators and Frequency Combs" (arXiv:2604.21861, April 2026)

## Trigger Words

- parametric oscillator reservoir computing, frequency comb neuromorphic
- 2:1 parametric resonance, oscillator-based RC
- bifurcation computational capability, physical reservoir computing

## Core Methodology

### 1. Two-Mode Parametric System

The system exhibits **2:1 parametric resonance** where:
- A pump drive at frequency 2ω excites subharmonic oscillations at ω
- Two coupled modes interact through nonlinear coupling
- Input signals encoded into drive amplitude

### 2. Dynamical Regimes

The system operates in distinct regimes, each with different computational properties:

| Regime | Characteristics | Computational Performance |
|--------|---------------|-------------------------|
| **Sub-threshold** | No sustained oscillation | Poor — insufficient nonlinearity |
| **Parametric Resonance** | Stable oscillations, nonlinear interactions active | **Optimal** — nonlinearity + temporal coherence |
| **Frequency Comb** | Multi-mode spectral states | Variable — spectral dimensionality ↑ but phase coherence ↓ |
| **Chaotic Comb** | Loss of phase coherence | Poor — too much chaos |

### 3. Reservoir Computing Pipeline

#### Encoding
- Input signals → drive amplitude modulation
- Temporal encoding of time-series data

#### Reservoir State
- Sample temporal response: oscillator amplitudes over time
- Sample spectral response: frequency comb components

#### Readout
- Linear readout layer trained on reservoir states
- One-step ahead prediction of chaotic systems

### 4. Benchmark Tasks

Standard chaotic system prediction:
- **Mackey-Glass**: Delay differential equation, tunable chaos
- **Rössler**: 3D chaotic attractor
- **Lorenz**: Classic butterfly attractor

### 5. Bifurcation-Performance Mapping

Key finding: **computational capability directly maps to bifurcation structure**
- Low-error regions align with parametric resonance boundary
- Prediction error mapped over parameter space reveals optimal operating zones

## Control Parameters

Four parameters systematically control accessible dynamical regimes:

1. **Input modulation depth**: Controls signal injection strength
2. **Detuning from frequency matching**: Shifts operating point on bifurcation diagram
3. **Damping ratio**: Controls oscillation decay, affects memory depth
4. **Input data rate**: Determines temporal resolution vs. computational load

## Implementation Guide

### Step 1: Define Oscillator Model
```python
# Two-mode parametrically driven oscillator
# x'' + 2*β*x' + ω₀²*(1 + h*cos(2*ω*t))*x + nonlinear_terms = input
```

### Step 2: Parameter Sweep
```python
# Sweep across parameter space to map bifurcation diagram
params = {
    'drive_amplitude': np.linspace(...),
    'detuning': np.linspace(...),
    'damping': np.linspace(...)
}
```

### Step 3: Reservoir State Collection
```python
# Collect temporal + spectral states
temporal_states = oscillator_amplitudes(t)
spectral_states = fft(oscillator_response)
reservoir_state = concatenate([temporal_states, spectral_states])
```

### Step 4: Train Readout
```python
# Linear regression on reservoir states
W = ridge_regression(reservoir_states, target_outputs)
prediction = W @ reservoir_states
```

## Pitfalls

1. **Chaotic regime trap**: Frequency comb states may appear rich but lose phase coherence → poor prediction. Stay near parametric resonance boundary.
2. **Insufficient memory**: Too high damping → reservoir forgets input too quickly. Balance damping for task timescale.
3. **Spectral vs. temporal trade-off**: More spectral modes ≠ better performance. Phase coherence matters more than dimensionality.
4. **Hardware sensitivity**: Physical implementations sensitive to parameter drift. Need calibration routines.

## Related Skills
- neuromorphic-spacecraft-pose-event-camera: Event-camera neuromorphic computing
- spikingjelly-framework: SNN training framework
- parametrically-driven-oscillator-neuromorphic: Related oscillator RC work
