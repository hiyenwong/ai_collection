---
name: entropy-production-limits-flock-hierarchy
description: Use when inferring hierarchy from animal group trajectories.
version: 1.0
author: neuro-cron 2026-10-25
license: MIT
category: ai_collection
trigger: leader-follower hierarchy inference, collective decision-making, flock size scaling, non-reciprocal interactions, stochastic thermodynamics of communication, pigeon homing GPS analysis
metadata:
  arxiv_id: "2610.31126"
  paper: "Entropy-production cost limits hierarchical decision-making in homing pigeon flocks"
  paper_authors: "Bibaswan Ghosh, Vipul Rai, Harsh Soni, Nitin Kumar (IIT Bombay / IIT Mandi)"
  published: "2026-10-22"
  pages: 17
  hermes:
    tags: [collective-behavior, stochastic-thermodynamics, active-matter, decision-making, animal-tracking]
    related_skills: [field-intelligence-jazz-improvisation, thermodynamic-brain-connectivity, self-organizing-rl-swarm-approaches-explore-exploit-optimum]
---

# Entropy-Production Cost Limits Hierarchical Decision-Making in Flocks

A trajectory-only, multi-scale framework connecting **coarse-grained homing performance, microscopic directional delays, and stochastic thermodynamics** for leader-follower hierarchies in animal collectives. Central result: small flocks fly by pronounced hierarchy; larger flocks become more egalitarian, and this transition is the consequence of holding the **per-individual entropy production rate constant** — non-reciprocal communication costs entropy, and the budget per bird is fixed.

## When to Use
- You have GPS/trajectory data of a navigating group (birds, fish, robots) and need a **quantitative hierarchy index** inferred from coordinates alone (no interaction sensors).
- You observe group-size-dependent decision structure and want a physical explanation.
- You model non-reciprocal agent communication and want its **thermodynamic (EPR) cost** — Schnakenberg entropy production applies to any pairwise asymmetric event process.
- Testing wisdom-of-crowds claims: the Many-Wrongs hypothesis (equal-weight route averaging) FAILS quantitatively on real pigeon data; influence hierarchy is required.

## Level 1 — Analytical homing model (extract behavioral traits from trajectories)
Model each individual/flock as an overdamped active Brownian particle: speed v, orientation theta with rotational diffusion D_r; angular deviation phi from the home direction bounded to +/- phi_m (phi_m = tolerance to navigational error). The dimensionless velocity autocorrelation has a closed form with two behavioral parameters:
- **lambda = L_H D_r / v** (path stochasticity; L_H = homing distance, persistence length L_p = v/D_r)
- **phi_m** (error-tolerance cone half-angle)

Long-time plateau of the autocorrelation = **sin^2(phi_m) / phi_m^2** — the signature of bounded angular deviation; the short-time decay carries lambda. Fit C*(t*) from GPS coordinates to extract both independently (validated on 3 animal species).

Pigeon finding (Sasaki et al. dataset, N = 1, 2, 4, 8): **lambda is N-independent, phi_m decreases systematically with N** — collective homing improves solely because birds tolerate less navigational error, not because individual paths get less noisy.

## Level 2 — Agent-based simulation with rank-dependent influence (infer the hierarchy index)
Solo-flight calibration: agent self-corrects (SC): when |phi| > phi_m-tilde (=74 deg), reset heading to 0 (stochastic-resetting mechanism; reproduces the empirical near-Gaussian phi distribution with phi_m = 54 deg, lambda = 10, D_r = 0.02 rad^2/s, v = 55 km/h).

Social coupling: an SC event in agent i broadcasts a signal; agent j reorients toward home (INDUCED correction, IC) with probability **P_i = e^{-eta (i-1)}** where i is i's hierarchical rank. P_1 = 1; eta = 0 recovers egalitarian; eta to infinity = single-leader limit.
- Egalitarian communication reproduces the phi_m(N) decrease only qualitatively — the predicted tolerance cone is far too narrow. **Hierarchy is needed for every N.**
- Calibrate eta(N) by matching simulated phi_m to experiment: **eta decreases monotonically with N** — hierarchical (small N) toward egalitarian (large N).

## Level 3 — Stochastic thermodynamics of non-reciprocity (why eta falls with N)
Rates of IC events between i and j: F_{i to j} = R_i P_i, F_{j to i} = R_j P_j (R_i = SC rate, weakly rank-dependent, approx R_0). Treat the two directions as independent Poisson processes; time-reversal symmetry is broken when F_{i to j} differs from F_{j to i}. Schnakenberg EPR per pair:

    S_dot_ij = (F_{i->j} - F_{j->i}) * ln(F_{i->j} / F_{j->i})

(= KL divergence rate between time-forward and time-reversed event histories.) Thermodynamic affinity Omega_ij = ln(F_{i->j}/F_{j->i}); per-agent mean affinity Omega_i = (1/(N-1)) sum_j Omega_ij — its sign gives the direction of net information flow (positive = net leader).

Summing over pairs with the exponential rank law gives the EPR per individual in closed form:

    s_dot = R_0 * eta / [2 (1-e^{-eta})^2] * [(N-1) - (N+1)e^{-eta} + (N+1)e^{-N eta} - (N-1)e^{-(N+1) eta}]

Near equilibrium (N eta << 1): **s_dot ~ R_0 eta^2 N^3** — quadratic in eta (Onsager reciprocity), vanishing as eta -> 0 (reciprocal communication = equilibrium).

**Constant-EPR hypothesis**: holding s_dot = K constant across flock sizes (with the measured weak decay R_0 = 0.026 N^{-0.25} /s) reproduces the empirical eta(N) curve well (K = 0.004 k_B) — hierarchy weakening emerges from preventing per-bird EPR divergence.

## Microscopic validation — directional delay times
Pairwise velocity cross-correlation kappa_ij(tau) = <v_i(t) . v_j(t+tau)>; the delay tau*_ij = argmax_tau kappa_ij(tau) gives who-leads-whom; per-bird average tau*_i orders the hierarchy. Phenomenological link to the influence probability:

    tau*_i = A - B / P_i = A - B e^{eta (i-1)}

with A, B physiological timescales (sensory response + aerodynamic inertia), N-independent. Empirical checks: delays bounded within +/-0.25 s (matching pigeon reaction times from independent studies); A, B constant across N; independent Nagy et al. dataset (N = 9) fits with eta = 0.05 < eta(N = 8) — extending the decreasing trend.

## Key insights
1. **Hierarchy is not noise — it is a budget allocation.** The phi_m(N) trend cannot be reproduced by egalitarian communication at any N; but the strength of hierarchy is capped by a per-individual entropy-production budget.
2. **Information flow = thermodynamic force.** Leader-follower asymmetry is an affinity (log-ratio of directional event rates); its KL-rate cost is the EPR — a direct bridge from trajectory statistics to stochastic thermodynamics.
3. **Topological interaction numbers have a thermodynamic rationale**: starlings interacting with only 6-7 neighbors may reflect the EPR cost of maintaining many non-reciprocal links.
4. **Method needs only trajectory coordinates** — transferable to fish schools, mammal herds, drone swarms, programmable active-matter robots as testbeds for the constant-EPR hypothesis.

## Caveats
- Assumes every pair communicates bidirectionally with finite reverse probability (breaks for large flocks / one-way signaling).
- Coarse-grained: all corrections instantaneous in simulation; real birds have finite sensory/cognitive delays (absorbed into the delay-time validation rather than the simulator).
- Constant-K was fitted to the eta(N) trend (one parameter); the near-equilibrium scaling and delay-time validation are independent supports, not proof.
