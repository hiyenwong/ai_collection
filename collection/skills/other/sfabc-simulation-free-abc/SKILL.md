---
name: sfabc-simulation-free-abc
description: ABC via CME convex relaxation, no Gillespie simulation.
trigger: simulation-free ABC, SFABC, stochastic reaction network inference, chemical master equation, CME relaxation, telegraph model, gene expression bursting, single-cell RNA kinetics, likelihood-free inference, Gillespie cost, convex feasibility test, Dirichlet resampling, rejection sampling posterior, snapshot data inference, promoter architecture TATA, burst size burst frequency, moment closure alternative, LP relaxation steady state, Bayesian parameter inference q-bio
author: engineering-lion5
category: ai_collection
version: 1.0
license: MIT
related_skills: simulation-free-abc, simulatable-process-learning-theory, bic-model-selection-bb-plot, sample-optimal-gaussian-state-learning
---

# SFABC — Simulation-Free Approximate Bayesian Computation for Stochastic Reaction Networks

**Source**: arXiv 2610.26361 (Zekai Li, Mauricio Barahona, Philipp Thomas — Imperial College London, 19-20 Oct 2026). Replaces Gillespie simulation in ABC with a **convex CME-relaxation feasibility test**: a parameter set is accepted if the Dirichlet-resampled data distribution lies within an ϵ-neighborhood of SOME solution of a finite subset of Chemical Master Equation constraints. The relaxation provably **contains** the true (intractable) CME solution, tightens monotonically with the number of equations M, and converges to the exact posterior as ϵ→0, M→full state space, time-grid→0. On the telegraph benchmark it matches ABC posterior accuracy while cutting wall time 50% (N=250) to 78% (N=500) — the LP feasibility test is ~independent of sample size while Gillespie simulation scales with N.

## When to Use

- Bayesian inference of reaction rates k of a **stochastic reaction network (SRN)** from count data (single-cell RNA counts, copy numbers) where the CME likelihood is intractable and ABC/simulation-based inference is the fallback you want to avoid.
- **Snapshot data** (steady state: CME reduces to algebraic constraints Σ_r k_r Q_r p = 0), **time-resolved** data (integrate CME against test functions → constraints on a finite time grid at observation times), **cell-cycle-resolved** data.
- Any "accept/reject against a physics constraint set" pattern: the data-resampling + feasibility-test construction generalizes beyond CME to any system with tractable relaxations of an intractable consistency condition.

## Algorithm (SFABC-Rej)

1. **S1** Sample k from prior π(k).
2. **S2** Resample candidate distributions p′_t ~ Dir(α(X_t)) with α = (n_1+1, …, n_B+1, 1) over the B_t unique observed states **plus one aggregate bucket for unobserved mass** — captures finite-sample variability; the +1s prevent zero probabilities.
3. **S3 Feasibility test (the core)**: solve the LP — does there exist p ≥ 0 over a finite state subset with Σp = 1, satisfying the CME equations restricted to a subset M of states, and 1-norm distance Σ_{u∈U}|p(u) − p′(u)| ≤ ϵ over observed states U? Accept k iff feasible. No simulation, no likelihood evaluation.
4. **S4** Weight accepted k by **1/V_ϵ^M(k)** (inverse acceptance volume, estimated by uniform-Dirichlet resampling) — corrects for parameters whose acceptance regions are larger.
5. **SFABC-SMC**: sequential Monte Carlo over a tolerance schedule ϵ₁>ϵ₂>… improves efficiency; enables model selection between competing SRN topologies.

## The Relaxation (why it works)

- **Steady state**: CME ∂p/∂t = Σ_r k_r Q_r p = 0 becomes linear equality constraints in p — an underdetermined finite system when restricted to M equations. Solutions form a convex set containing the true p_k.
- **Transient data**: integrate the CME against time-dependent test functions φ (generator identity d/dt E[φ] = E[Aφ]) → constraints at observation times only.
- **Tightening**: more equations (larger M) shrinks the feasible set → posterior approximation tightens systematically. As M → full state space, ϵ → 0: exact posterior.
- Resulting posterior is **wider** than truth at finite relaxation (one-sided approximation) — never overconfident.

## Empirical Findings to Reuse (paper)

- Telegraph model (k_off=2, k_on=8, k_syn=5, k_deg=1): KS distance to MCMC-exact posterior matches standard ABC at ϵ=2; posterior-predictive KS also matches. Runtime per iteration flat in N (LP) vs growing (simulation): 50% total-time cut at N=250, 78% at N=500.
- Robustness: 100 parameter sets from 10^Uniform(−1,1) priors — unbiased posterior medians, posterior-predictive KS improves as ϵ shrinks. Posterior CV much smaller for k_syn than k_on/k_off (k_syn sets expression level; switching rates are weakly identified from marginals).
- Mouse fibroblast scRNA-seq (224 vs 8,916 cells): TATA-box promoters show **higher burst size BS = k_syn/k_off** (P~1e-4, 1e-10), **lower gene activity GA = k_on/(k_on+k_off)** in the large dataset; burst frequency BF = k_on/k_deg unchanged — TATA shapes bursting via promoter switching, not frequency.
- Time-resolved data recover kinetic rates on **absolute** time scale; cell-cycle-resolved data discriminate competing regulation models.

## Verification (this session, mini-telegraph LP, scipy `highs`)

- Exact steady state via truncated generator solve: mean mRNA = 4.0000 (theory k_syn·k_on/(k_deg(k_on+k_off)) = 4) ✓; variance 4.36 > Poisson 4 ✓ (over-dispersion).
- **(a) True params accepted** (12–100% depending on M, ϵ); **(b) 10×-wrong params (k_on=0.8, k_syn=50, k_deg=3) accepted 0/60, 0/60, 0/60** — perfect discrimination.
- **(c) Tightening**: acceptance at true params falls 1.00 → 0.13 as M_eq goes 2 → 25 (relaxation provably tightens); wrong stay at 0.
- **(d) Posterior concentration**: rejection over a k_on grid, E[k_on] = 8.00 (true) with all mass in [4,16]; at N=800 only the true grid point survives.
- **Pitfalls found**: ϵ must scale with Dirichlet-resampling noise (~L1 ≈ 0.42/0.28/0.10 at N=50/200/800 — decays slower than 1/√N because the observed-state count grows with N); LP needs slack variables s_j ≥ ±(marg_p(u)−p′(u)) per observed state; at the truncation boundary the synthesis outflow must still appear in the equation (mass conservation).

## Implementation Recipe

```python
# variables: p(0..NMAX) per promoter state, slacks s_j per observed state
# A_eq: CME steady-state rows for n <= M_eq  (inflow - outflow per state),
#       plus normalization row (sum p = 1)
# A_ub:  p(u)+s_j >= p'_j, -p(u)-s_j >= -p'_j  per observed u ;  sum s <= eps
# linprog(c=0, ...) status==0  <=>  accept k
```
Bench: 122 unknowns + ~30 slacks solves in <0.1 s — independent of N.

## Limitations / Boundaries

- Posterior wider than truth at finite M (by construction); SFABC-SMC with ϵ-schedule mitigates.
- Identifiability limits inherited from marginals: k_on/k_off only weakly constrained by snapshot marginals (small posterior CV differences observed).
- Transient case needs test-function integration — more bookkeeping than the steady-state algebraic form.
