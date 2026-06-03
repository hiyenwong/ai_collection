---
name: leggett-garg-neural-dynamics
description: Leggett-Garg inequality testing methodology for neural dynamics — probing non-diffusive stochastic structure in single neurons using temporal correlations. Based on arXiv:2605.12126 (May 2026).
---

# Leggett-Garg Tests in Neural Dynamics

## Overview

Methodology for probing non-diffusive stochastic structure in single neurons using Leggett-Garg-type temporal correlation tests. Bridges quantum physics temporal inequalities with neural dynamics analysis.

## Core Theory

### Leggett-Garg Inequalities (LGI)
- Temporal analog of Bell inequalities
- Test for macroscopic realism vs quantum-like temporal correlations
- **Diffusive processes** (Wiener/cable equation) always satisfy LGI
- **Persistent stochastic processes** (Kac-type, Telegrapher's equation) can violate LGI

### Key Distinction
- **Diffusive dynamics**: Memoryless, Wiener process, satisfies LGI
- **Persistent stochastic dynamics**: Finite-velocity, memory-bearing, Telegrapher's equation, can violate LGI
- **Violation interpretation**: NOT evidence of quantum coherence, but evidence against simple diffusive description

## Methodology

### 1. Temporal Correlation Analysis
- Define measurement sequence Q(t₁), Q(t₂), Q(t₃) for neural observables
- Compute two-time correlation functions: C(tᵢ, tⱼ) = ⟨Q(tᵢ)Q(tⱼ)⟩
- Form Leggett-Garg parameter: K = C(t₁,t₂) + C(t₂,t₃) - C(t₁,t₃)

### 2. LGI Violation Detection
- Classical bound: K ≤ 1 (for macroscopic realism)
- K > 1 indicates non-diffusive temporal structure
- Oscillatory temporal correlations are key to violation

### 3. Kac Process Framework
- Finite-velocity random walk (telegraph process)
- Velocity alternates between ±v with switching rate λ
- Converges to Wiener process as v→∞, λ→∞ (diffusive limit)
- At finite parameters: persistent correlations, memory effects

### 4. Analytic Continuation
- Kac processes connect to Dirac-like envelope equations
- Finite-velocity transport → non-diffusive temporal correlations
- Natural mechanism for contextual temporal structure

## Applications

- **Neural dynamics characterization**: Distinguish membrane noise types
- **Non-Markovian structure detection**: Probe memory in neuronal signaling
- **Contextual temporal analysis**: Identify history-dependent neural processing
- **Single-neuron probing**: Requires single-neuron resolution measurements
- **Quantum-classical boundary**: Conservative interpretation avoids quantum brain claims

## Implementation Steps

1. **Data Collection**: Record single-neuron activity with high temporal resolution
2. **Observable Definition**: Choose binary/thresholded neural observable Q(t)
3. **Correlation Computation**: Calculate two-time correlation functions
4. **LGI Parameter**: Compute K = C(t₁,t₂) + C(t₂,t₃) - C(t₁,t₃)
5. **Statistical Testing**: Determine if K exceeds classical bound with significance
6. **Model Comparison**: Fit diffusive vs persistent stochastic models

## Triggers
- leggett-garg, neural dynamics, temporal correlations, non-diffusive, persistent stochastic
- Kac process, Telegrapher's equation, macroscopic realism
- single-neuron dynamics, membrane noise characterization

## References
- Ghose, P. (2026). "Leggett--Garg Tests in Neural Dynamics: Probing Non-Diffusive Stochastic Structure in Single Neurons." arXiv:2605.12126 [quant-ph]
