---
name: npa-moment-selection-synergy
description: "Use when tightening NPA/SDP bounds under a fixed computational budget, selecting moments or SDP constraints, or diagnosing subset-optimization landscapes."
category: ai_collection
---

# NPA Moment Selection by Synergy (arXiv:2607.14755)

**Paper**: "Moment Optimization in the Navascués-Pironio-Acín Hierarchy" — Flora, Losel Matos, Heightman, Kriváchy, Garriga, Acín (ICFO/ETH, v2 2026-10-08). Open-source: github.com/Ciscone7/OptimalMomentsNPA

Replaces rigid NPA level truncation (NPA1→NPA2→NPA3) with **budget-aware moment-subset selection**: given initial set I (e.g. NPA1), candidate pool F (e.g. NPA2), and budget k, choose the k moments from A = F\I that give the tightest SDP bound. Applicable to ANY noncommutative polynomial optimization (Bell violations, ground-state certification, device-independent protocols).

## Why greedy fails: synergistic landscape

Brute-force ground truth on I3322 (N=21 candidates, 2^21 subsets) reveals:
- Improvement concentrated in a **sharp transition window** (5 < k ≤ 19); subsets of identical size span nearly the whole NPA1→NPA2 gap.
- **Optimal k-subset ⊅ optimal (k−1)-subset + best element** — strong higher-order synergy; greedy stays flat at the NPA1 plateau until most of A is included.
- Landscape is spin-glass-like: rugged, frustrated local minima → need global search.

## Marginal synergy diagnostic Δ(S_k) — cost-free convergence monitor

```
Δ(S_k) = (1/k) Σ_i [ f_γ(S_k \ {m_i}) − f_γ(S_k) ]  ≥ 0
```
Average bound degradation when any single moment is removed from best k-subset. Computed from data already gathered at step k−1 → **zero extra SDP cost**.
- Δ large & rising: collective/synergy regime — keep optimizing, marginal-cost plateau is a TRAP.
- Δ peaks then decays: true saturation/modular regime (on I3322, Δ(S_8*) ≈ 0.084 exactly at the NPA2-saturation step k=8).
- Random-subset estimate Δ(k) (n≈50–200 samples): peak position = cheap upper bound on saturation budget k.

## Three optimizers (pick by use case)

| Method | Mechanism | Best when |
|---|---|---|
| **RBM + REINFORCE** | Parametric policy π_θ over Hamming-weight-k binary vectors; visible logits y_i=(W^T h)_i+b_i, sigmoid p_i, **Gumbel top-k sampling** (log p_i + g_i, keep top k) enforces ‖x‖₁=k; policy gradient ∇J = E[(L(x)−b)∇log π_θ(x)], EMA baseline b | Tight certification needed; hard transition regime — reaches log-gap −9.6 vs PT's −4.2 at 1/10 the SDP cost (5 orders closer to optimum) |
| **Parallel Tempering (PT)** | R replicas at geometric temperature ladder, Metropolis at fixed T_r, periodic swap A_swap = min(1, exp[(f(x_j)−f(x_i))(1/T_i−1/T_j)]); Hamming-weight-preserving bit flips; swap on CURRENT configs (preserves detailed balance) | A physically motivated warm-start ansatz exists (seed one cold replica with it) — used for Heisenberg local-basis warm-starts |
| **Bayesian Optimization** | Random-forest surrogate, 250 SDP evals amortized | Fast survey of many instances; ~20× fewer SDP evals than PT, lower accuracy in transition |

All three: ~2 orders of magnitude below brute force (brute-force peaks at C(21,10)=352,716 normalized evals).

## Key results

1. **I3322**: transition window 5 < k ≤ 19; RBM tracks optimal path closest; all methods beat greedy.
2. **All 171 non-trivial Bell inequalities in (4,4,2,2)** (N=40, C(40,20)≈1.4×10^11 infeasible): transition starts k≈9–33 (mostly 10–24); all reach 5% of NPA2 before k=40; only 127/171 reach 1% before full NPA2. **"NPA2 bound" conflates qualitatively different convergence regimes** — prefer moment-selective over level-based.
3. **1D Heisenberg chain ground state** (Bethe-ansatz exact benchmark):
   - Physical local basis B_local is **internally compressible for energy**: fixed fraction p=0.3 of monomials already beats full NPA2 (N-independent plateau, even/odd parity split from frustration); p=0.7 reaches 10^−4–10^−5.
   - **Compressibility breaks for nonlocal observables**: half-chain correlator C_N/2 error does NOT plateau (local basis lacks long-range operator products).
   - **B_local is NOT globally optimal**: enlarged pool NPA4 + PT **warm-started from local-basis solution** improves certified C_N/2 gap from 7.13×10^−5 to ≈10^−6 (~2 orders of magnitude, k≈1300); independent NPA4 search without warm-start barely reaches local-basis level. Energy LB also crosses full-local bound at k≈800 (E_LB≈−3.805 vs E_0=−3.797300).

## Reusable procedure

1. Cast problem as moment optimization: I = minimal moments defining cost; F = next-level pool; budget k.
2. Estimate saturation budget: sample ~50–200 random k-subsets, locate Δ(k) peak.
3. Pick optimizer: certification-critical → RBM; warm-start ansatz available → PT; many instances, eval-dominated → BO.
4. Monitor Δ(S_k) alongside cost curve; do NOT stop at the first marginal-cost plateau.
5. For nonlocal observables: enlarge pool beyond physically local monomials; warm-start from the local solution.
6. Open direction: use Δ actively — grow the hierarchy selectively in high-synergy directions instead of uniform level jumps.
