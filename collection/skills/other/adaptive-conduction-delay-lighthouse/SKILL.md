---
name: adaptive-conduction-delay-lighthouse
description: "Haken Lighthouse model with adaptive conduction delays and phase locking theory. Provides analytically tractable framework for phase-locked states in delayed spiking networks, spike-time perturbation stability analysis, and activity-dependent white matter plasticity (myelination-modulated delays). Applicable to: SNN temporal coordination, communication-through-coherence, white matter plasticity modeling, delayed spiking network analysis, circulant ring networks, autapse dynamics, and slow-fast adaptive delay systems."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2606.21508"
  published: "2026-06-19"
  authors: "Stephen Coombes, Rüdiger Thul, Stefan Ruschel, Rachel Nicks"
  tags: [spiking-neural-networks, phase-locking, conduction-delays, white-matter-plasticity, haken-lighthouse, event-driven, slow-fast-systems, myelination, temporal-coordination, circulant-networks]
---

# Adaptive Conduction Delays and Phase Locking in Spiking Haken Lighthouse Networks

**arXiv**: [2606.21508](https://arxiv.org/abs/2606.21508) | **Published**: 2026-06-19 | **Category**: q-bio.NC

## Core Contribution

Develops a mathematically tractable framework for **phase-locked activity in delayed spiking networks** using the **Haken Lighthouse model** — an event-driven spiking description bridging integrate-and-fire networks and coupled phase oscillators. Introduces **activity-dependent white matter plasticity** where myelination modulates axonal conduction speed, creating a slow-fast system with state-dependent delays that self-organizes toward commensurate delay-period relationships.

## Haken Lighthouse Model

The model describes N pulse-coupled nodes on a directed weighted graph:

```
dθ_i/dt = S(ψ_i(t))                              (1)
ψ_i(t) = Σ_j w_ij (η_ij * s_j)(t)                (2)
s_j(t) = Σ_m δ(t - T_j^m)                        (3)
```

- θ_i ∈ S: phase variable of node i
- S(x): sigmoidal firing-rate function (monotonically increasing, positive)
- ψ_i: synaptic input from delayed spike trains
- η_ij(t) = η(t - τ_ij): causal kernel with propagation delay τ_ij
- α-function kernel: η(t) = α²·t·e^{-αt}·H(t), Q = (1 + d/dt/α)²
- Firing times T_j^m defined by threshold: θ_j(T_j^m) = 2π (phase wraps)

**Key insight**: This is an event-driven spiking system where continuous phase evolution couples to discrete spike times, making it amenable to analytical treatment while preserving spike-level temporal precision.

## Phase-Locked State Theory

### Self-Consistency Equation

For phase-locked states T_i^m = mT + φ_i·T with φ_i ∈ [0,1):

```
2π = ∫₀ᵀ dt S( Σ_j w_ij P(t + (φ_i - φ_j)T - τ_ij) )           (7)
```

where P(t) is the T-periodic synaptic drive function, equivalently:
- Fourier series: P(t) = Σ_n P_n e^{iω_n t} with ω_n = 2πn/T
- P_n = η̂(ω_n)/T where η̂ is Fourier transform of η
- Closed form for α-function: P(t) = α²e^{-αt}/(1-e^{-αT}) · [t + T·e^{-αT}/(1-e^{-αT})]

### Stability Analysis (Spike-Time Perturbations)

Linear stability is formulated directly in terms of **spike-time perturbations**:
- Perturb firing times T_i^m → T_i^m + ε_i^m
- Derive characteristic equation for ε evolution
- For ring networks with circulant symmetry: stability decomposes into Fourier modes (twisted states)
- Eigenvalue problem: det[I - M(λ)] = 0 where M encodes delayed spike interactions

## Key Network Architectures Analyzed

### 1. Single-Node Autapse (Self-Connection)
- Explicit fold bifurcations of regular-spiking branches
- Dynamic instabilities of inter-spike intervals
- Shows how a single delay can create multistability

### 2. Reciprocal Two-Node Network
- Synchronous (φ_1 = φ_2), anti-synchronous (φ_1 = φ_2 + 0.5), and asymmetric phase-locked states
- Two-delay problem reduces to equivalent one-delay description
- Explicit conditions for existence and stability of each state

### 3. Ring Networks with Distance-Dependent Delays
- Circulant symmetry allows stability diagonalization via Fourier modes
- Twisted states (traveling waves) analyzed systematically
- Spatial structure of delays shapes which patterns are stable

## White Matter Plasticity (Slow-Fast System)

### Plasticity Rule

Activity-dependent myelination modulates conduction speed and hence delay:

```
dτ_ij/dt_slow = ε · F(activity_ij)               (plasticity)
dθ_i/dt_fast = S(ψ_i(t))                          (spiking)
```

- τ_ij evolves on timescale 1/ε >> 1 relative to spiking
- This creates a **state-dependent delay problem** (delays depend on network state)
- Frozen phase-locked branches organize the adaptive dynamics

### Key Results from Adaptive Dynamics

1. **Synchrony emergence**: Plasticity drives networks toward synchronized states even from asynchronous initial conditions
2. **Slow switching**: Networks exhibit long-timescale transitions between competing phase-locked patterns
3. **Commensurate delay classes**: Heterogeneous delays self-organize into discrete delay-period classes (τ ≈ nT/k for integers n,k)
4. **Attractor reshaping**: Adaptive conduction reshapes the attractor landscape of the delayed spiking network

### Slow-Fast Interpretation

- **Fast subsystem**: Spiking dynamics with frozen delays (phase-locked branches)
- **Slow subsystem**: Delay evolution guided by activity statistics
- **Critical manifold**: Set of phase-locked states parameterized by delay values
- Plasticity selects points on the critical manifold that satisfy commensurate timing

## Implications for SNN Design and Neuromorphic Computing

### Why Delays Matter
- Delays are **not small corrections** — they are fundamental dynamical ingredients
- Event-based computation is intrinsically temporal: spike timing carries information
- Delays enhance memory, temporal processing, and reservoir-like computation
- Adaptive delays provide additional degrees of freedom beyond synaptic weights

### Design Principles
1. **Commensurate timing**: Networks self-organize toward τ ≈ nT/k relationships
2. **Communication-through-coherence**: Efficacy depends on phase alignment of inputs
3. **Slow-fast separation**: Plasticity timescale >> spiking timescale enables self-organization
4. **Circulant exploitation**: Spatial symmetry in delay structure enables efficient analysis

### Connection to NeuroAI
- Provides tractable mathematics for studying how adaptive delays regulate temporal coordination
- Bridges spiking descriptions, phase oscillators, and rate-based neural fields
- Relevant for event-based neuromorphic hardware where timing is a design parameter

## Methodology Summary

1. **Model specification**: Define Haken Lighthouse network with delays τ_ij on graph
2. **Phase-locking analysis**: Solve self-consistency equations (7) for φ_i and T
3. **Stability computation**: Linearize spike-time perturbations, solve characteristic equation
4. **Symmetry exploitation**: For circulant networks, diagonalize via Fourier modes
5. **Slow-fast decomposition**: Separate fast spiking from slow delay evolution
6. **Critical manifold analysis**: Track how frozen branches organize adaptive dynamics
7. **Event-driven simulation**: Validate analytical predictions with direct spike-time simulation

## Activation Keywords

adaptive conduction delays, phase locking, Haken Lighthouse model, white matter plasticity, activity-dependent myelination, delayed spiking networks, spike-time perturbations, slow-fast systems, commensurate timing, communication through coherence, event-driven SNN, circulant ring networks, twisted states, temporal coordination, synchrony emergence, delay-period relationships

## Related Skills

- `adaptive-conduction-delays-haken-lighthouse` (separate existing skill)
- `network-attractors-delay-plasticity` — delay plasticity in attractor networks
- `spiking-reservoir-robustness` — SNN temporal processing
- `kuramoto-brain-network` — phase dynamics in brain networks
- `spiking-oscillation-mapping` — oscillatory states in spiking networks

## Common Pitfalls

- **Delays as parameters vs. dynamical variables**: Traditional models treat τ as fixed; this work shows τ should be treated as a slow dynamical variable when myelination is considered
- **α-function vs. other kernels**: Results use α-function for analytical tractability; other kernels (exponential, double-exponential) require numerical treatment
- **Circulant assumption**: Ring network stability diagonalization requires distance-dependent coupling symmetry; arbitrary topologies need full eigenvalue computation
- **Timescale separation validity**: Slow-fast analysis requires ε << 1; if plasticity is too fast, the frozen-branch approximation breaks down
- **Spike-time vs. phase perturbations**: Stability must be analyzed in spike-time domain (not phase domain) for event-driven models — phase perturbations alone miss timing-dependent effects

## References

- Coombes, S. et al. (2026). "Adaptive conduction delays and phase locking in spiking Haken Lighthouse networks." arXiv:2606.21508
- Haken, H. — original Synergetics programme introducing the Lighthouse model
- Coombes et al. (2024) — previous revisiting of Lighthouse model for synchrony, waves, bumps
