---
name: non-hermitian-gnw-consciousness
description: "Non-Hermitian potential well formalism for the subliminal-preconscious-conscious processing hierarchy in the Global Neuronal Workspace. Uses nonlinear Schrödinger-type equation in imaginary time with non-Hermitian, non-normal Hamiltonian to model conscious access as bound state emergence. Activation: GNW, consciousness, non-Hermitian, neural field theory, bound states, sensory processing hierarchy, cloud functions, global neuronal workspace."
tags: [neuroscience, consciousness, GNW, neural-field-theory, non-Hermitian, quantum-analogue]
version: 1.0.0
author: agent
date: 2026-07-12
---

# Non-Hermitian Potential Well Formalism for Conscious–Preconscious–Subliminal Processing

**arXiv: [2607.08302](https://arxiv.org/abs/2607.08302v1)** | q-bio.NC, nlin.AO | Lubashevskiy & Lubashevsky

## Overview

A phenomenological model of the **Global Neuronal Workspace (GNW)** that reproduces the tripartite taxonomy of sensory processing (subliminal, preconscious, conscious) using a **non-Hermitian, non-normal Hamiltonian** framework. Conscious access emerges as a **bound state** when both landscape depth and top-down attention exceed thresholds.

## Core Framework

### Cloud Functions and GNW Hilbert Space
- GNW modeled as Hilbert space **H = L²(Rᴺ)** over N-dimensional perceptual state space
- High-level representations encoded as **cloud functions** Ψ(x,t)
- |Ψ(x,t)|² interpreted as normalized density over perceptual configurations
- Nonlocality represents perceptual uncertainty from neural processing mechanisms
- Normalization: ∫|Ψ(x,t)|² dx = 1

### Governing Equation
The cloud function evolves according to a **nonlinear Schrödinger-type equation in imaginary time**:

```
τ ∂Ψ/∂t = -Ĥ Ψ + ⟨Ψ|Ĥ|Ψ⟩ Ψ
```

where τ ~ 200ms (characteristic time of high-level visual processing), and Ĥ is a **non-Hermitian, non-normal Hamiltonian**.

### Priority Hamiltonian Decomposition
Ĥ = Ĥ' + iĤ'' decomposes into complementary processes:

**Hermitian component (Recognition)**:
```
Ĥ' = A(x,t) [-ℓ²∇² + Ω(x)]
```
- Drives Ψ toward minima of the GNW landscape Ω(x)
- Proportional to attention degree A (0 ≤ A ≤ 1)
- Acts as dissipative localization → stimulus recognition

**Anti-Hermitian component (Broadcasting)**:
```
Ĥ'' = [-c_η·ℓ²∇² - c_ω·Ω(x)]
```
- Promotes delocalization of Ψ → information broadcasting
- Operates without selective attention
- Minima of Ω act as potential barriers in this component

### GNW Landscape
- Effective potential Ω(x) shaped by **early sensory processing**
- Bridges early (feedforward) and late (recurrent) processing stages
- Minima correspond to established stimulus representations

## Tripartite Processing Taxonomy

The model naturally reproduces three regimes based on landscape depth U and attention A:

### I. Subliminal Processing
- **U < U_c²(c)**: Stimulus too weak → no bound state
- Neural activity cannot trigger global ignition regardless of attention

### II. Preconscious (Supraliminal Unattended)
- **U > U_c²(c)** but **A < A_c**: Stimulus strong enough, but insufficient attention
- Representation exists but is unstable (preconscious buffer)
- Bound state exists but Re E₀ < 0 → unstable

### III. Conscious (Supraliminal Attended)
- **U > U_c²(c)** and **A > A_c**: Both conditions met
- **Stable bound state emerges** → conscious access
- Information broadcast throughout GNW

### Phase Transition
- Emergence of bound state at A = A_c is a **first-order phase transition**
- Bound state appears with finite spatial extent (not diverging)
- Contrast with Hermitian wells (second-order, diverging localization length)

## Pöschl–Teller Potential Well Model

For a single potential well in 1D:
```
Ω(η) = -U / cosh²(η)
```

Ground state eigenfunction: Ψ₀(η) = Z₀ / cosh^μ(η)

where μ(μ+1) = ((A - ic)/(A + ic))·U

**Stability criteria**:
1. **Existence**: Re μ > 0 ⟺ U > U_c¹(g) = ¼(g² - 1)/g², where g = c/A
2. **Stability**: Re E₀ > 0 ⟺ U > U_c²(g) (computed numerically)

## Key Insights

1. **Dual role of GNW landscape**:
   - Minima → attractors (recognition via Hermitian part)
   - Minima → barriers (broadcasting via anti-Hermitian part)

2. **Conscious access as bound state emergence**:
   - Requires BOTH sufficient stimulus strength (U > threshold) AND attention (A > A_c)
   - Mathematically formalizes GNW's two-condition theory

3. **Maxima don't support recognition**:
   - Bound states at landscape maxima are all unstable
   - Only minima contribute to stimulus recognition

4. **First-order vs second-order transition**:
   - Non-Hermitian: bound state appears with finite extent (first-order)
   - Hermitian: bound state energy approaches continuum edge (second-order)

## Mathematical Properties

- **Non-normal operator**: eigenfunctions non-orthogonal → winner-takes-all competition
- **Nonlinear norm-preserving term**: ⟨Ψ|Ĥ|Ψ⟩Ψ enables transitions between eigenstates
- **Complex-valued landscape**: combines recognition (real) and broadcasting (imaginary)
- **Spatially nonlocal interactions**: via convolution structure of Ĥ

## Applications
- Modeling conscious access dynamics
- Explaining attention-dependent perception
- Bridge between first-person phenomenology and neural implementation
- Previously applied to: power law of working memory, change-of-mind in decision-making

## Pitfalls
- **Phenomenological model**: Not derived from first-principles neural dynamics
- **Short-range approximation**: Only two leading terms of convolution kept
- **Constant attention assumption**: A(x,t) = constant; spatially varying attention needs separate analysis
- **1D simplification**: Full N-dimensional case may have richer dynamics

## Related Skills
- `consciousness-usk-framework` - USK consciousness theory
- `canonical-functionalism-consciousness` - Canonical functionalism
- `neural-dynamics-analysis-methodology` - Neural dynamics analysis
- `quantum-cognition` - Quantum probability for cognitive modeling
