---
name: leggett-garg-neural-dynamics
description: >
  Leggett-Garg inequality testing methodology for probing non-diffusive stochastic structure
  in neural dynamics. Use when analyzing whether neural dynamics exhibits quantum-like temporal
  correlations, persistent stochastic processes, memory effects, or non-Markovian structure.
  Applicable to single-neuron electrophysiology analysis, cable-equation model validation,
  Kac-type finite-velocity process modeling, and Telegrapher's equation derivation for neural systems.
  Triggers: Leggett-Garg, neural dynamics, non-diffusive, persistent stochastic, Kac process,
  Telegrapher equation, temporal correlation, macrorealism, non-invasive measurability,
  quantum-like neural, neural memory effects.
---

# Leggett-Garg Neural Dynamics Testing

Methodology from arXiv:2605.12126 — using Leggett-Garg inequalities (LGI) as a temporal probe
to distinguish diffusive (Wiener/cable-equation) models from non-diffusive persistent stochastic
models in single-neuron dynamics.

## Core Concept

The LGI is a temporal analogue of Bell-type constraints. In neural dynamics context:
- **LGI satisfaction** → purely diffusive, Markovian, trajectory-based dynamics
- **LGI violation** → persistent stochastic dynamics with memory, finite propagation speed,
  contextual temporal structure (mathematically analogous to quantum systems)

**Important**: LGI violation here does NOT imply microscopic quantum coherence in the brain.
It indicates breakdown of purely diffusive description and presence of non-Markovian structure.

## Key Steps

### 1. Define Dichotomic Observable

Select a measurable quantity Q(t) ∈ {+1, −1} from neural recordings:
- Spike/no-spike binary state
- Above/below threshold membrane potential
- Excited/inhibited firing rate regime

### 2. Compute Two-Time Correlation Functions

For measurements at times t₁, t₂, t₃:

```
C(ti, tj) = E[Q(ti) · Q(tj)]
```

### 3. Compute LGI Combination

```
K = C(t1,t2) + C(t2,t3) − C(t1,t3)
```

Classical bound: |K| ≤ 1 under macrorealism + non-invasive measurability.

### 4. Experimental Protocol

- Record single-neuron activity across multiple trials
- Measure Q(t) at three equally-spaced time points
- Estimate correlation functions from ensemble averages
- Test whether |K| > 1 (LGI violation)

### 5. Interpretation

|K| > 1 indicates:
- Persistent (non-diffusive) stochastic transport
- Finite-velocity processes (Kac-type)
- Telegrapher's equation dynamics
- Dirac-like envelope equations via analytic continuation
- Intrinsic memory in neural dynamics

## Mathematical Background

### Kac Process → Telegrapher's Equation

Finite-velocity random walk with velocity ±v and reversal rate α:

```
∂²P/∂t² + 2α ∂P/∂t = v² ∂²P/∂x²
```

In the limit α → ∞, v → ∞ with v²/2α = D fixed → diffusion equation.

### Analytic Continuation to Dirac-like Equations

The Telegrapher's equation connects to Dirac-like envelope equations through
analytic continuation, providing the mathematical bridge to quantum-like
temporal correlations without requiring actual quantum coherence.

## Activation

Keywords: leggett-garg, neural dynamics, non-diffusive, persistent stochastic,
Kac process, Telegrapher equation, temporal correlation, macrorealism,
non-invasive measurability, quantum-like neural, neural memory effects
