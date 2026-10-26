---
name: mobile-oscillator-robustness-aging
description: Mobile oscillators, degree heterogeneity lowers robustness
category: ai_collection
---

# Mobile Oscillators Reshape Dynamical Robustness (arXiv 2610.16608)

**Paper**: "How Mobile Oscillators Reshape Dynamical Robustness in Complex Networks" — Chowdhury & Kundu, nlin.AO, 12 Oct 2026.

**Use when**: analyzing aging transitions / amplitude death in mobile-agent oscillator populations, swarm resilience on heterogeneous networks, or mapping temporal interaction networks onto effective mean-field coupling.

## Core Model

N mobile Stuart-Landau agents random-walk over an n-node network; agents interact diffusively only when co-located:

```
dZ_i/dt = (a_i + iω - |Z_i|²)Z_i + k Σ_j 1{x_i=x_j}(Z_j - Z_i)
```

Healthy agents (a>0) oscillate at amplitude √a; unhealthy (a<0) decay to quiescence Z=0. p = fraction unhealthy.

## Rapid-Mobility Mean-Field Reduction (the reusable trick)

When hopping is fast vs oscillator dynamics, replace the instantaneous co-location indicator by its stationary average. For an unbiased random walk, node occupation is degree-weighted: P_α = d_α/(n⟨d⟩). Two independent walkers co-locate with probability

```
P_same = Σ_α P_α² = ⟨d²⟩ / (n⟨d⟩²)
```

giving an effective GLOBAL coupling

```
k̃ = k·N·P_same = k·N·⟨d²⟩ / (n·⟨d⟩²)
```

The ratio ⟨d²⟩/⟨d⟩² is the heterogeneity amplifier: for a d-regular network it equals 1 (k̃ = kN/n); any degree variance makes k̃ strictly larger. This reduces the mobile system to a globally coupled Stuart-Landau population: dZ_i/dt = (a_i+iω-|Z_i|²)Z_i + k̃(Z̄−Z_i).

## Critical Threshold (verified numerically)

Two-group reduction (healthy mean field Z_h, unhealthy Z_u) with Z̄=(1−p)Z_h+pZ_u. Linearizing the amplitude equations about the quiescent state gives the Jacobian

```
J = [[a_h−k̃p,        k̃p     ],
     [k̃(1−p),  a_u−k̃(1−p)]]
```

Amplitude death onset (det J = 0):

```
p_c = a_h(k̃ − a_u) / (k̃(a_h − a_u))
```

with paper parameters (a_h=2, a_u=−1, N=500, n=50, k=1, d-regular ⟨d⟩=4): k̃=10, p_c=0.7333 — matches the paper exactly. **Caution**: a naive reading of the abstract-equation extraction can yield (a_h·k̃−a_u)/(k̃(a_h−a_u)) (=0.7000, wrong); always derive from the 2-group Jacobian — the correct numerator keeps a_h·(k̃−a_u).

Monotonicity: dp_c/dk̃ = a_h·a_u/(k̃²(a_h−a_u)) < 0 strictly (a_h>0, a_u<0). **More effective coupling = LOWER robustness** — counterintuitive but exact: diffusive coupling transmits the quiescent state of unhealthy agents; once healthy agents synchronize, healthy–healthy coupling terms vanish (Z_j−Z_i≈0) while healthy–unhealthy terms stay mismatched, so extra coupling disproportionately enforces a common (dying) state.

## Verified Numerical Predictions

- Topology ordering: p_c^BA < p_c^ER < p_c^Regular (BA ≈0.70 < ER ≈0.72 < Regular 0.7333 with exact BA degree moments) — scale-free collapse first.
- Numerical thresholds sit ~+0.02 above theory at T_total=200; extending to T_total=2000 shrinks the offset to ~0.005 (finite-time relaxation effect).
- Simulation protocol: RK4 dt=0.01, hop interval ΔT=0.01, R(t)=|Z̄|/√a_h, time-average over final 50 units; p_c^num = first grid p (Δp=1/N) with ⟨R⟩<10⁻⁶; 10 networks × 10 trajectories.

## Reusable Patterns

1. **Temporal-network → global-coupling map**: any system of agents with rapidly changing contacts reduces to k̃ = k⟨C⟩·N·(contact-probability moment). Degree moments ⟨d⟩,⟨d²⟩ of the mobility substrate are the ONLY topology dependence.
2. **Heterogeneity-as-coupling-amplifier**: hubs raise co-location probability (walkers visit high-degree nodes preferentially), amplifying effective coupling — use to predict robustness ordering across topologies WITHOUT simulating mobility.
3. **Jacobian-scan verification**: eigenvalue scan of the 2-group Jacobian over p validates any closed-form p_c in seconds — use before trusting pdftotext-extracted formulas.

## Applications

- Resilient swarm/robot-collective design: mobility on homogeneous substrates is strictly more robust to agent failure than on scale-free ones.
- Motile-cell populations (e.g., rhythmic microbial collectives): predict critical unhealthy fraction before collective oscillation collapse.
- Mobile sensor networks: connectivity heterogeneity trades against dynamical robustness under node degradation.

## Key References

- Aging transition literature (DANMODH et al.) for static-network baselines.
- Rapid-mobility averaging: stationary degree-weighted occupation P_α = d_α/(n⟨d⟩).
- arXiv 2610.16608 (this paper); future work: intermediate hopping rates comparable to oscillator timescales.
