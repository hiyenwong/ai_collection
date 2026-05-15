---
name: chaos-synchrony-ei-networks
description: "Dynamical mean-field theory framework for analyzing chaos-to-synchrony transitions in recurrent excitatory-inhibitory (E-I) networks with target-specific inhibition. Extends the seminal Sompolinsky-Crisanti-Sommers (SCS) theory to two-population firing-rate networks with segregated E/I neurons. Use when: (1) analyzing phase transitions in recurrent neural networks, (2) studying E/I balance and target-specific inhibition, (3) deriving dynamical mean-field equations for neural population dynamics, (4) investigating coherent oscillations vs asynchronous chaos, (5) researching stability criteria for neural circuits."
---

# Chaos to Synchrony in E-I Networks

## Overview

Extends the seminal SCS (Sompolinsky-Crisanti-Sommers) theory of random recurrent networks to two-population firing-rate networks with segregated excitatory and inhibitory neurons and target-specific inhibitory couplings. Identifies target-specific inhibition as a key control parameter organizing the phase diagram.

**Paper**: Martorell et al., "From Chaos to Synchrony in Recurrent Excitatory-Inhibitory Networks with Target-Specific Inhibition" (arXiv: 2605.14916)

## Key Contributions

### 1. Generalized SCS Framework

The original SCS theory showed random recurrent networks undergo a transition from quiescence to **asynchronous chaos**. This work extends to:

- Two-population (E/I) firing-rate networks
- Target-specific inhibitory couplings that break E-I balance
- Dynamical mean-field theory (DMFT) derivation for macroscopic statistics

### 2. Phase Diagram: Three Qualitative Classes

Target-specific inhibition organizes the network into three regimes:

| Regime | Conditions | Dynamics |
|--------|-----------|----------|
| **Inhibition-dominated / Strictly balanced** | Strong inhibition | Quiescent activity OR asynchronous chaos |
| **Excitation-dominated** | Strong excitation | Persistent activity + **synchronous chaos** (non-vanishing mean) |
| **Excitation-dominated (oscillatory)** | Eigenvalue conditions met | **Coherent oscillations** — chaos suppressed |

### 3. Chaos Suppression by Coherent Oscillations

Critical finding: **coherent oscillations do not coexist with chaotic fluctuations**. When oscillations emerge, they suppress the chaotic component around the periodic mean trajectory — reminiscent of input-induced suppression of chaos.

### 4. Stability Criteria

DMFT yields self-consistent equations for:
- Macroscopic mean activities
- Autocorrelation functions
- Stability criteria distinguishing **mean-driven** vs **fluctuation-driven** instabilities

## Mathematical Framework

### Network Dynamics

Two-population firing-rate network:
```
dhᵢ/dt = -hᵢ + Σⱼ Jᵢⱼ φ(hⱼ) + external input
```

Where:
- `hᵢ` = input current to neuron i
- `Jᵢⱼ` = connectivity matrix with E/I structure
- `φ(·)` = transfer function (e.g., tanh, ReLU)
- Target-specific inhibition: inhibitory couplings depend on target population

### Dynamical Mean-Field Theory (DMFT)

Key steps:
1. Assume thermodynamic limit (N → ∞)
2. Average over disorder (random connectivity)
3. Derive self-consistent equations for order parameters:
   - Mean activity: `m(t) = ⟨φ(h(t))⟩`
   - Autocorrelation: `C(t,t') = ⟨h(t)h(t')⟩`
   - Response function via fluctuation-dissipation

### Stability Analysis

Linearize around fixed points / periodic orbits:
- **Mean-driven instability**: eigenvalue of stability matrix crosses threshold
- **Fluctuation-driven instability**: chaotic fluctuations grow despite stable mean
- Boundary determined by spectral properties of J matrix

## Activation Keywords

- chaos synchrony E-I networks
- target-specific inhibition
- SCS theory extension
- dynamical mean-field neural networks
- excitation-inhibition balance
- asynchronous chaos
- coherent oscillations neural
- phase diagram neural networks
- mean-field theory neuroscience
- recurrent network dynamics
- 2605.14916

## Related Skills

- `snn-working-memory-heterogeneous-delays` — working memory in recurrent SNNs
- `neural-code-dynamics-analysis` — neural coding dynamics framework
- `spiking-oscillation-mapping` — oscillatory states in balanced spiking networks
- `multi-timescale-conductance-snn` — multi-timescale conductance SNNs

## References

- **Original SCS paper**: Sompolinsky, Crisanti & Sommers (1988) — chaos in random neural networks
- **Related**: `partial-annealing-pattern-decorrelation` (arXiv: 2605.10304) — Hopfield model annealing
- **DMFT foundations**: Coolen (2005) — Statistical Mechanics of Recurrent Neural Networks
