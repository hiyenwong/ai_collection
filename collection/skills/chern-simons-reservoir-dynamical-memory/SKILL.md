---
name: chern-simons-reservoir-dynamical-memory
description: "Use when modeling memory in Chern-Simons gauge reservoirs."
version: 1.0.0
author: "Beuria & Chembrolu (arXiv 2609.13315) via neuro-cron 2026-10-24"
license: MIT
category: ai_collection
metadata:
  hermes:
    tags: [reservoir-computing, chern-simons, gauge-field, dynamical-memory, physical-reservoir]
    arxiv_id: "2609.13315"
---

# Chern-Simons Reservoir Dynamical Memory

Methodology from "Beyond density snapshots: Dynamical memory in Chern-Simons reservoirs" (Beuria & Chembrolu, arXiv:2609.13315v2, cs.ET, 18 pp). A field reservoir couples a density fluctuation rho(c,t) to an independently evolving Abelian Chern-Simons (CS) gauge connection a(c,t). The paper identifies WHICH internal variable carries input history, separates dynamical memory from its readout accessibility, and delivers a reusable controlled-comparison methodology for any physical-reservoir mechanism claim.

## When to Use

- Analyzing or designing physical/topological reservoirs whose state = density + transport or gauge field
- Deciding whether a reservoir's performance comes from the claimed mechanism (topology, gauge memory) or from ordinary density dynamics
- Building causal tests of memory carriers (constraint-preserving reset/lesion interventions)
- Sequence/pulse-order memory tasks on spiking, neuromorphic, or continuous-media substrates where a performance score alone is not enough

## The CS field reservoir

State z = (rho, a) on internal 2-torus C (coordinates need not be physical positions):
- Gauss law (density fixes curl): curl(a) = g*rho; transverse part a_c[rho] = gJ*grad(-laplacian)^-1 rho
- Spatial CS evolution: d_t a = gJ*j (J = 90-degree rotation) — the connection INTEGRATES the current history
- Overdamped constitutive drift v = -gamma*a (temporal gauge; NOT gauge-invariant — the representative choice is part of the model)
- Driven density: d_t rho + div j_p = s, with j_p = alpha*rho*v - D*grad rho, s = -tau*rho + eps*sum_l u_l rho_in,l
- CS compatibility via minimum-L2 longitudinal completion: j = j_p + grad psi with laplacian(psi) = -s (zero-mean source). The longitudinal part is the minimum-norm correction; adding any divergence-free part would silently change CS evolution.

## The exact (memory) component

On the periodic domain with zero harmonic sector: a = a_c[rho] + b, with d_t b = -alpha*gamma*g*P_parallel J(rho*a).
- b is a pure history integral of the nonlinear advective current: b = 0 identically when alpha = 0, and it is missed by every instantaneous density-snapshot reconstruction.

## Four-model controlled hierarchy (core reusable design)

Same domain, drive, numerics, initial conditions, seeds; vary ONE constitutive ingredient at a time:
1. Reciprocal: v_rec = -gamma*grad(-laplacian)^-1 g*rho — nonlocal Poisson transport, curl-free (longitudinal only)
2. Instantaneous transverse: v_0 = -gamma*J*grad(-laplacian)^-1 g*rho — Gauss-law-satisfying circulation, divergence-free, NO independent connection
3. Local feedback: v_loc = (1 + eta*rho) v_0 — instantaneous nonlinear state dependence
4. Coupled CS: v = -gamma*a with d_t a = gJ*j — adds independently evolving connection memory

Purpose: a positive memory score in model 1 cannot be credited to a CS mechanism; models 2-3 test whether the benefit requires retained history at all.

## Diagnostic battery

Reservoir protocols:
- Scalar fading memory MC(d), C = sum over 16 delays (ridge readout on the 4 lowest Fourier modes + <rho^2>)
- Matched pulse-order histories: identical duration, final input, and channelwise integrated input; ONLY the order of two pulses differs — any endpoint difference is pure path dependence
- Five-family linear decoding (density / circulation / longitudinal / geometry / all; nested leave-one-seed-out ridge, seed blocks intact to prevent leakage)
- Cyclic-drive loop area A_cyc between forward and return branches, scanned over sweep rates

Gauge-dynamics protocols:
- Residuals R_G (Gauss law) and R_S (spatial CS) — reconstructions can satisfy Gauss law while violating the evolution equation
- Reconstruction errors E_a, E_v; closure fitting (best scalar local multiplier)
- Checkpoint reset: clone the state, replace a -> a_c[rho] (removes b at FIXED density and curl), continue with identical inputs, measure delta-rho
- Two-site cross-response Delta-R_chi vs advective strength alpha (forward-reverse cancellation failure)

## Key results (honest ledger)

- E_a = 0.155 evolved-connection mismatch at t~4; the best local closure fit reduces it by only 0.033% — scalar local multipliers cannot absorb b
- Reset at fixed density changes future density by 1.77 +/- 0.17% (vanishes at alpha = 0; robust to 24^2 grid, halved time step, tau variation) — b causally affects dynamics within the chosen gauge + drift law
- R_S: coupled 1.4e-2 vs reconstructions 5.5e-2 — Gauss-law satisfaction is NOT spatial-CS evolution; halving dt halves the coupled residual (temporal discretization dominated)
- Scalar memory C: 0.19 / 0.28 / 0.25 / 0.27 — NO resolved scalar advantage for coupled CS
- Pulse-order decoding (all features): 0.81 / 0.80 / 0.87 / 0.86; coupled CS beats instantaneous-transverse by 6.5 +/- 1.9 pp (7.3 +/- 1.8 at 24^2) but NOT local feedback (-1.2 +/- 1.9 pp)
- Cyclic lag: first cycle CS 0.292 < controls 0.418 / 2.008, but the ordering REVERSES on cycles 2-3 (0.271 / 0.266 vs 0.209 / 0.214) — first-cycle advantage is preparation-dependent, not persistent
- No topological protection established: fixed domain topology, zero harmonic sector, no isolated computational benefit from topology

## Transferable patterns

1. Mechanism-vs-score discipline: never infer mechanism from performance; build the control ladder that adds one physical ingredient at a time
2. Matched-history path test: equalize everything except event ORDER; endpoint separation is then pure path dependence
3. Constraint-preserving reset: lesion one field component while holding the constraint data (density + Gauss curl) fixed — the reservoir analogue of lesion/rescue experiments; small effects (1.8%) that survive refinement can be causal
4. Channel-resolved readout: decompose decoding features by physical channel (density vs circulation vs divergence) — aggregate scores hide which variable carries the code
5. Memory is not readout accessibility: information can live in the state yet be linearly undecodable from chosen features; keep "encoded" and "accessible" claims separate
6. Preparation dependence: single-cycle comparisons can invert across cycles; report cycles 2+ before claiming lag advantages

## Pitfalls

- v = -gamma*a is a constitutive law for a chosen gauge representative; reset experiments are interventions within that representative, not gauge-invariant measurements
- Reset is not reachability: it does not show that two natural input histories produce identical density with different futures
- Excluding the TESTED closures (instantaneous transverse, scalar local) does not exclude all instantaneous density functionals
- Pseudospectral products need the two-thirds-rule dealiasing; monitor both residuals, not just Gauss law

## Cross-domain interface

- Engram analogy: b is a slowly accumulating, perturbation-sensitive memory trace riding on fast density activity — parallel to memory held in synaptic/structural variables vs instantaneous firing; "dynamical memory vs readout accessibility" mirrors decoding-vs-mechanism debates in neuroscience
- Pulse-order decoding is a minimal temporal-sequence sensitivity benchmark for spiking and physical substrates

## References

- Beuria & Chembrolu, arXiv:2609.13315v2 (2026)
- Deser, Jackiw & Templeton, Ann. Phys. 140 (1982) — topologically massive gauge theory
- Beuria & Chembrolu, Phys. Rev. E 113, 065401 (2026) — precursor: topological flux on a context manifold
- Singh et al., Chaos Solitons Fractals 202, 117460 (2026) — Hodge-projected echo-state networks
