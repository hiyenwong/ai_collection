---
name: quantum-probability-flow
description: >
  Hydrodynamic probability-flow analysis for studying quantum decoherence
  in matter-wave interference patterns. Uses probability current decomposition
  to quantify coherence loss in Talbot-Lau interferometry. Use when: quantum
  decoherence analysis, matter-wave interferometry, probability current,
  Talbot effect, quantum-to-classical transition. Trigger words: decoherence,
  Talbot interference, probability flow, hydrodynamic quantum, matter-wave.
---

# Quantum Probability Flow Analysis

Analyze quantum decoherence through hydrodynamic probability-flow decomposition
in matter-wave interference experiments.

## Core Framework

The quantum probability current j = (hbar/m) Im(psi* nabla psi) provides
a hydrodynamic picture of quantum evolution. Decoherence manifests as
redistribution of probability flow patterns.

## Talbot Interference Setup

For a grating of period d and wavelength lambda:

1. **Talbot distance**: z_T = 2d^2 / lambda (self-imaging distance)
2. **Fractional Talbot**: At z = p/q * z_T, produce q-fold fractional images
3. **Decoherence effect**: Reduces fringe visibility V = (I_max - I_min)/(I_max + I_min)

## Probability Flow Decomposition

Decompose j into coherent and incoherent components:

j = j_coherent + j_incoherent

Where:
- j_coherent: Interference-carrying component (phase-dependent)
- j_incoherent: Classical-like flow (phase-independent)

The ratio |j_incoherent|/|j| quantifies decoherence degree.

## Analysis Steps

### Step 1: Wave Function Reconstruction

From measured intensity pattern I(x):
1. Use phase retrieval (Gerchberg-Saxton or transport-of-intensity)
2. Reconstruct complex wave function psi(x) = sqrt(I) * exp(i*phi)

### Step 2: Current Computation

j(x) = (hbar/m) * Im(psi*(x) * nabla psi(x))

Numerical implementation:
- Use central differences for nabla psi
- Handle boundary conditions carefully (periodic for gratings)

### Step 3: Flow Visualization

- Streamlines of j(x) show quantum trajectories
- Divergence nabla.j relates to probability density change
- Vortices indicate phase singularities (decoherence markers)

### Step 4: Decoherence Quantification

Define coherence measure:
C = integral(|j_coherent|) / integral(|j|)

C = 1: Fully coherent
C = 0: Fully decohered

## Key Patterns

### Pattern 1: Environmental Decoherence
For environment-induced decoherence:
- Model as stochastic phase kicks: psi -> psi * exp(i * delta_phi(t))
- Track C(t) evolution: typically C(t) = exp(-t/tau_decoherence)

### Pattern 2: Which-Path Information
When which-path info is available:
- j splits into non-interfering components
- C relates to path distinguishability D: C^2 + D^2 = 1

### Pattern 3: Partial Coherence
For partially coherent sources:
- Use cross-spectral density formalism
- Probability flow averaged over ensemble

## Applications

- Quantum sensor design (maximizing coherence time)
- Matter-wave interferometry optimization
- Quantum-classical boundary studies
- Decoherence mitigation in quantum devices
