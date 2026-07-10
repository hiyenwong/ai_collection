---
name: leggett-garg-neural-dynamics
description: "Leggett-Garg inequality testing methodology for neural dynamics. Proposes experimental tests to distinguish diffusive vs non-diffusive stochastic structure in single neurons using temporal correlations. Connects Kac processes to Telegrapher equation and Dirac-like envelope equations. Activation: Leggett-Garg inequality, neural dynamics, Telegrapher equation, persistent stochastic process, non-diffusive neuron, quantum-inspired neuroscience, temporal correlations."
---

# Leggett-Garg Tests in Neural Dynamics

Methodology for probing non-diffusive stochastic structure in single-neuron dynamics using Leggett-Garg-type temporal correlation tests, based on Ghose (2026), arXiv:2605.12126.

## Core Concept

The Leggett-Garg inequality (LGI) is a temporal analogue of Bell inequalities. This methodology proposes using LGI tests on single-neuron dynamics to distinguish between:

1. **Diffusive models** (Wiener process / cable equation): Standard neural dynamics models where membrane potential evolves as Brownian motion. These ALWAYS satisfy LGIs.
2. **Non-diffusive persistent models** (Kac-type finite-velocity processes): Models with memory and persistence that lead to the Telegrapher\'s equation. These CAN violate LGIs.

## Key Theoretical Framework

### Telegrapher\'s Equation vs Cable Equation

The cable equation (standard neural model):
$$\frac{\partial V}{\partial t} = D \frac{\partial^2 V}{\partial x^2}$$

The Telegrapher\'s equation (persistent stochastic model):
$$\frac{1}{v^2} \frac{\partial^2 V}{\partial t^2} + \frac{1}{D} \frac{\partial V}{\partial t} = \frac{\partial^2 V}{\partial x^2}$$

Key difference: Telegrapher\'s equation includes a second-order time derivative, capturing finite-velocity transport with memory effects.

### Leggett-Garg Inequality

For measurements at three times $t_1 < t_2 < t_3$, with dichotomic observable $Q(t) = \pm 1$:

$$K = C_{12} + C_{23} - C_{13} \leq 1$$

where $C_{ij} = \langle Q(t_i)Q(t_j) \rangle$ is the two-time correlation function.

**Violation condition**: $K > 1$ indicates non-diffusive, persistent temporal structure.

### Analytic Continuation: Kac → Dirac

- Kac processes (persistent random walks with finite velocity) are analytically continued to Dirac-like envelope equations
- This provides a mathematical bridge between classical persistent stochastic transport and quantum-like temporal correlations
- Violation is interpreted conservatively: NOT evidence of quantum coherence, but evidence against simple diffusive description

## Experimental Protocol

### Step 1: Measurement Setup
- Record single-neuron membrane potential at high temporal resolution
- Define dichotomic observable: $Q(t) = +1$ if $V(t) > V_{threshold}$, $Q(t) = -1$ otherwise
- Choose appropriate threshold (e.g., resting potential or mean firing threshold)

### Step 2: Correlation Measurement
- Measure two-time correlation functions $C(t_1, t_2)$ for multiple time pairs
- Use non-invasive or weakly-invasive measurement to minimize disturbance
- Ensure measurement independence (no-signaling in time)

### Step 3: LGI Computation
- Compute $K = C(t_1,t_2) + C(t_2,t_3) - C(t_1,t_3)$ for triplets of measurement times
- Test for violation: $K > 1$
- Optimize time intervals to maximize potential violation

### Step 4: Interpretation
- If $K \leq 1$: Consistent with diffusive (cable equation) dynamics
- If $K > 1$: Evidence of persistent, non-Markovian temporal structure
- Oscillatory temporal correlations are the key signature of violation

## Key Findings

- Purely diffusive dynamics **always** satisfies LGIs
- Persistent stochastic dynamics can produce **oscillatory temporal correlations** capable of violating LGIs
- Violation indicates: persistence, memory, and contextual temporal structure
- These features are mathematically analogous to quantum systems, but the interpretation is conservative (no quantum coherence claim)

## Applications

- Probing non-Markovian structure in neural dynamics
- Distinguishing competing models of single-neuron behavior
- Understanding memory effects in neural processing
- Bridge between neuroscience and quantum foundations (conceptual, not ontological)
- Experimental probe of contextual temporal structure without requiring quantum brain claims

## Pitfalls

1. **Conservative interpretation**: LGI violation does NOT imply quantum coherence in neurons. It indicates non-diffusive stochastic structure only.
2. **Measurement invasiveness**: Strong measurements can artificially destroy temporal correlations. Use weak or non-invasive techniques.
3. **Time resolution**: Telegrapher\'s equation effects operate at very short timescales. Sub-millisecond recording resolution needed.
4. **No-signaling assumption**: LGI tests require measurement independence. Ensure measurements at $t_i$ do not influence future dynamics beyond the natural evolution.
5. **Alternative classical explanations**: Persistent stochastic processes are classical — distinguish from quantum carefully.

## Mathematical Tools

- **Kac process**: Random walk with finite velocity, alternating direction at Poisson-distributed times
- **Telegrapher\'s equation**: Derived from Kac process in the diffusion limit with finite velocity
- **Dirac envelope equation**: Obtained via analytic continuation from Telegrapher\'s equation
- **Temporal correlation functions**: $C(t_1, t_2) = \langle Q(t_1)Q(t_2) \rangle$

## Related Skills

- neural-dynamics-universal-translator: Cross-model neural dynamics alignment
- neural-critical-dynamics-theory: Critical dynamics in neural systems
- stochastic-physical-neural-networks: Physical neural networks with stochastic dynamics
- quantum-neuroscience-patterns: Umbrella skill for quantum-neuroscience research patterns
- orchid-kuramoto-quantum-consensus: Bio-inspired Kuramoto quantum consensus protocol
