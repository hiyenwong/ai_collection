---
name: astrocyte-breathing-cluster-robustness
description: Use when breathing clusters emerge from astrocyte feedback.
---

# Breathing Cluster Synchronization under Astrocyte Feedback: Robustness Framework

Methodology from arXiv:2610.04647 (Nguessap, Njougouo & Ferreira, USP Ribeirao Preto / IMT Lucca, 3 Oct 2026, nlin.CD): extends breathing cluster synchronization — intermittent alternation between synchronized and desynchronized states of structurally symmetric neuron subsets, driven by astrocyte-mediated feedback — to biologically realistic conditions: thermosensitive neuronal dynamics, intrinsic electric-field (ephaptic) coupling, stochastic noise, and delayed gliotransmission.

## When to use

- Modeling neuron–astrocyte networks where glial feedback modulates global synaptic gain
- Robustness sweeps of cluster/chimera-like states against temperature, ephaptic fields, noise, feedback delay
- Parameter studies of glial feedback (attenuation alpha, gain beta, basal drive gamma, delay tau) on synchronization
- Cortical UP/DOWN state-switching analogues; glial dysregulation scenarios in pathology (rigid hypersynchrony / persistent desynchrony)

## Model

Thermosensitive neuron with intrinsic electric field (per unit i):
- dx/dt = x(1−xi) − x^3/3 − y + I + A cos(w t) + C_i
- dy/dt = c(x + a − b e^{1/T} y) + r E
- dE/dt = k y + E_ext, with E_ext = D*eta(t) (Gaussian white noise)

Chemical synaptic coupling: C_i = eps(t) (x_s − x_i) Sum_j G_ij Gamma(x_j), Gamma = sigmoid (lambda=10, theta_s = −0.25 mV, x_s = 2 mV).

**Astrocyte feedback** (global, linear, delayed): d(eps)/dt = −alpha*eps + beta*R(t−tau) + gamma, where R(t) is the Kuramoto order parameter computed from spike-time-interpolated phases (linear interpolation between successive spikes). Synchronized firing -> larger extracellular glutamate transients -> stronger astrocytic Ca2+ response -> gliotransmitter release modulating eps.

**Network**: N=10 random background (p=0.7) + structurally symmetric subset Vc (e.g. {4,6,9}: G_ki = G_kj for all k outside Vc; intra-cluster connections zeroed; adjacency symmetrized, no self-loops). Symmetry is the prerequisite: the global feedback then acts uniformly on Vc, producing collective alternation.

**Metrics**: cluster synchronization error delta_x_clu(t) computed over Vc only; desynchronization fraction P = fraction of simulation time with delta_x_clu > delta_th = 0.01. Integration: 5th-order Runge–Kutta, dt=0.01, 5e5 steps (T_sim=5000); delay via discrete buffer of past R(t); initial states U[−1,1], eps(0) U[0,1].

Defaults: a=0.7, c=0.1, xi=0.175, T=5, b=0.4, I=0.5, k=0.001, w=0.005, r=0.001; alpha=3e−2, beta=8e−3, gamma=2e−3, tau=200.

## Core findings (mechanistic anchors)

1. **Slow push–pull mechanism**: cluster sync -> R up -> eps up (beta*R term) -> enhanced coupling destabilizes sync -> desync -> R down -> eps decays (alpha) -> re-sync. Self-sustained oscillation; requires symmetric connectivity so feedback acts uniformly on the subset.
2. **Role separation**: beta decides WHETHER the network breathes (too weak: no alternation; too strong: eps saturates -> rigid synchronization); alpha decides HOW FAST and HOW DEEPLY (larger alpha -> shorter breathing period, shallower amplitude swings). Astrocytes behave as nonlinear regulators, not linear amplifiers — non-monotonic parameter landscapes.
3. **Optimal corridor**: intermediate-to-high alpha (0.3–0.6) with moderate gamma (1e−3 to 3e−3) sustains rhythmic switching best; overly small alpha locks the network into rigid sync regardless of beta.
4. **Noise**: moderate noise (D=0.1) preserves breathing with irregular amplitude/period (feedback loop buffers stochastic shocks); high noise (D=1) contracts and fragments the viable parameter region into a narrow 2D island — glial regulation then operates near functional limits.
5. **Temperature sets the noise threshold**: T<=1 robust for all D (P~0); physiological T=5 breaks down at D>0.4; T=10 desynchronizes even at moderate noise — the b e^{1/T} term accelerates recovery-current kinetics, amplifying noise destabilization.
6. **Delay robustness (0 <= tau <= 1500)**: P nearly constant; tau only phase-shifts eps(t) relative to the cluster error. Breathing depends on the feedback ARCHITECTURE, not precise timing — R(t) integrates whole-network activity before modulating eps. Consistent with slow astrocytic Ca2+ timescales.
7. **Ephaptic field (r E coupling)**: modulates excitability and noise tolerance but does not alter the topological (symmetry-based) mechanism.

## Pitfalls / lessons

- P alone CANNOT distinguish rigid synchronization from a low-P breathing state — always inspect delta_x_clu(t) time series (rigid: persistently low; breathing: recurrent alternation; desync: persistently above threshold)
- N=10 with exact symmetry is proof-of-principle; larger networks with approximate/dynamically evolving symmetries remain untested
- Single global linear astrocyte omits spatial domains, Ca2+ waves, astrocyte diversity — do not over-generalize to cortical scale
- alpha values that overlap cortical attentional state-switching timescales support the "astrocytes as tunable controllers of network timescales" interpretation; pathology = leaving the buffering corridor in either direction

## Related

- Wang et al. — original breathing-cluster framework (deterministic, simplified neurons)
- [[dual-timescale-memory-astrocyte]], [[neurogliovascular-unit-noradrenaline-model]] — alternative astrocyte modeling approaches
- [[adaptive-coupling-stochastic-resonance]] — adaptive coupling as synchronization control
