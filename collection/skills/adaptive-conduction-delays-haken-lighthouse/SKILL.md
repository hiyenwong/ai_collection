---
name: adaptive-conduction-delays-haken-lighthouse
description: "Theory of phase-locked activity in delayed spiking networks using the Haken Lighthouse model — an analytically tractable event-based framework bridging integrate-and-fire networks and coupled phase oscillators. Derives self-consistency conditions for phase-locked states with multiple fixed delays, linear stability theory formulated in spike-time perturbations, and activity-dependent white matter plasticity (myelination-modulated conduction speed) creating slow-fast state-dependent delay systems that self-organize toward commensurate delay-period relationships. Activation: Haken Lighthouse model, phase locking, conduction delays, white matter plasticity, spike-time perturbations, circulant ring networks, slow-fast adaptive delays, myelination, commensurate timing, temporal coordination."
metadata:
  arxiv_id: "2606.21508"
  published: "2026-06-19"
  authors: "Stephen Coombes, Rüdiger Thul, Stefan Ruschel, Rachel Nicks"
---

# Adaptive Conduction Delays and Phase Locking in Spiking Haken Lighthouse Networks

**arXiv**: [2606.21508](https://arxiv.org/abs/2606.21508) | **Published**: 2026-06-19

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

## Network Architectures Analyzed

1. **Single-Node Autapse**: fold bifurcations of regular-spiking branches, dynamic instabilities of inter-spike intervals
2. **Reciprocal Two-Node**: synchronous, anti-synchronous, and asymmetric phase-locked states; two-delay → one-delay reduction
3. **Ring Networks with Distance-Dependent Delays**: circulant symmetry allows stability diagonalization via Fourier modes; traveling waves analyzed systematically

## White Matter Plasticity (Slow-Fast System)

### Plasticity Rule

Activity-dependent myelination modulates conduction speed and hence delay:

```
dτ_ij/dt_slow = ε · F(activity_ij)               (plasticity)
dθ_i/dt_fast = S(ψ_i(t))                          (spiking)
```

- τ_ij evolves on timescale 1/ε >> 1 relative to spiking
- Creates a **state-dependent delay problem** (delays depend on network state)
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

## Common Pitfalls

- **Delays as parameters vs. dynamical variables**: Traditional models treat τ as fixed; this work shows τ should be treated as a slow dynamical variable when myelination is considered
- **α-function vs. other kernels**: Results use α-function for analytical tractability; other kernels (exponential, double-exponential) require numerical treatment
- **Circulant assumption**: Ring network stability diagonalization requires distance-dependent coupling symmetry; arbitrary topologies need full eigenvalue computation
- **Timescale separation validity**: Slow-fast analysis requires ε << 1; if plasticity is too fast, the frozen-branch approximation breaks down
- **Spike-time vs. phase perturbations**: Stability must be analyzed in spike-time domain (not phase domain) for event-driven models — phase perturbations alone miss timing-dependent effects