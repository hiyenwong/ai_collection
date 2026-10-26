---
name: frustrated-cycle-contextuality
description: Use when designing cyclic contextuality or binding tests.
category: ai_collection
---

# Binding-Motivated Contextuality: Frustrated-Cycle H¹ Obstruction

**Source**: arXiv:2609.23977 (Shavit, Sep 2026, q-bio.NC)

## When to Use
- Designing experiments on perceptual binding (intransitive dominance cycles) or judgment contextuality (order effects, conjunction fallacy)
- Computing contextuality from cyclic judgment data (Suppes–Zanotti / n-cycle inequalities, Contextuality-by-Default)
- Choosing between obstruction measures: contextual fraction CF vs Čech class vs signed margin V⋆
- Cross-domain individual-difference designs correlating contextuality across perception and decision-making

## Core Idea
Perceptual binding failures and judgment contextuality share ONE mathematical obstruction: a nonzero class in H¹ of a presheaf with no global section. Local data (pairwise judgments/percepts) are consistent, yet no single global assignment (joint distribution / coherent percept) exists. Sheaf cohomology is exactly the mathematics of "consistent local parts fail to glue globally."

Key: the coefficient group does NOT move with data — H¹(C_n; Z₂) ≅ Z₂ for every cycle, odd or even. What separates frustrated from unfrustrated is the CLASS, not the group. Parity is NOT the criterion: the even 4-cycle (CHSH scenario) is contextual for suitable non-uniform correlations; the real discriminator is frustration past the threshold c*, not oddness.

## The Three Obstruction Measures (critical distinctions)
1. **Contextual fraction CF** (Abramsky–Barbosa–Mansfield 2017): LP-based, COMPLETE — CF=0 iff global section exists. CF = 1−NCF where NCF = max Σ g_C b_g s.t. g|C = Σ b_g e_C(s), b≥0. For cyclic systems: CF = 2·CNT2 (CbD statistic), and CF = max(0,V)/2 on the contextual side.
2. **Čech cohomology class** (Abramsky et al. 2015): only SUFFICIENT — nonzero certifies contextuality, but ZERO does NOT certify absence (Hardy model is the standard witness; Carù 2017). Never use as a null test.
3. **Signed obstruction margin V⋆** = Σᵢ ε⋆ᵢγᵢ − (n−2) − Δ: carries ALL of CF's information PLUS sub-threshold variation CF discards (CF = [V⋆]₊/2 when ε⋆ is the active facet). Use for confirmatory statistics, NOT clamped CF.

## The n-Cycle Test [proved]
- n dichotomous judgments M₀..M_{n−1} (outcomes ±1), each evaluable only against its two neighbours; contexts = adjacent pairs.
- Global (noncontextual) joint distribution exists IFF cyclic (Suppes–Zanotti/n-cycle) inequalities hold.
- Uniform adjacent anticorrelation c, unbiased marginals, odd n: **CF(c) = max(0, −((n−2)+nc)/2)** — threshold c* = −(n−2)/n, slope −n/2. For n=3: zero for c ≥ −1/3, rises to 1 at c=−1. Even 4-cycle under UNIFORM c never obstructs (it 2-colours) — this is the matched control.
- Signalling ∆ (marginal shifts with context) must be measured and subtracted: system is contextual iff V = 3|c|−1−∆ > 0. Use CbD consistification when marginals shift.

## Why the Perceptual Design Needs TWO Binary Judgments per Pairing
A single forced choice per pairing ("is A nearer than B?") does NOT instantiate the H¹ object:
- Read as one variable/context: 3 responses always admit a joint assignment — obstruction is to total order (linear-ordering polytope), not a global section
- Read as complementary outcomes (winner +1/loser −1): degenerate — within-context correlation pinned at −1, frustration F≡2, margin collapses to V⋆=2−∆; random responding (p=0.5) would be maximally contextual while strong deterministic cyclic dominance would be noncontextual — the psychological reading inverts! (7 of 8 published forced-choice systems hit this degeneracy)
- Fix: two SEPARATELY calibrated binary judgments per pairing, each anchored to a FIXED EXTERNAL criterion ("nearer than a reference depth"), not to the co-presented stimulus → within-context correlation c becomes a free, estimable design parameter

## Cross-Domain Test Design (the novel contribution)
Shared mechanism predicts: within-subject correlation between perceptual CF and judgment CF. But both are inconsistency scores → general response consistency g confounds any bare correlation.

**The confound-residualized protocol:**
1. g-capturing control: transitive/signalling-matched triple where random responses read as inconsistent (NOT a degenerate zero-variance control); variance- and reliability-MATCHED to the frustrated arm
2. Regress each arena's frustrated CF on its control score → correlate residuals. Positive under shared mechanism; ≈0 under independent sheaves or pure-g confound
3. Falsifier needs a NUMBER: preregister smallest effect of interest r_min>0; reject only when calibrated one-sided upper bound U₁₋α < r_min. "ρ̂≈0" alone cannot falsify "ρ>0"

## Why V⋆ Replaces CF for Confirmation (structural bias findings)
- CF is clamped at zero; residualizing one clamped variable on another leaves irreducible dependence: false-positive rate asymptotes at ~0.058 no matter how precisely the control is measured (0.089 even residualizing on the TRUE latent)
- The bias GROWS with N (√N−3 scaling): CF-scored error rate 0.067→0.117 as N: 200→400; null statistic mean drifts 0.37→0.60
- V⋆ on both arms AND control: null statistic centred (−0.003..−0.021), rate 0.058–0.076 flat; calibrated cutoff = 95th pct of V⋆'s own simulated null (1.74–1.79, vs textbook 1.645; NOT 2.11–2.39 needed for CF)
- Scoring arms on V⋆ but control on CF is WORSE than changing nothing (0.141 vs 0.096)
- Power: N≈200, ≥80 trials/context frustrated arms → detects 30%-of-variance shared component at 0.968

## Trial Count Requirements
- Control arm needs 4–8× the frustrated arm's trials (its variance comes only from g): 320–640 trials/context for reliability 0.86–0.90 (160 gives only 0.68)
- Frustrated arm: 80 trials/context → split-half reliability 0.90–0.92 at population c≈−0.55 (straddling c*), per-subject CF SD≈0.23
- Range restriction: don't push frustration past c* until everyone saturates — CF must VARY across subjects to correlate
- Total burden: 2,400–4,320 presentations (4,800–8,640 responses), split across two sessions (one arena each, order counterbalanced)

## Identifiability Limits (honest constraints, proved)
- A trait loading 0.6 on both controls forges ρ_obs = 0.209 with NO shared obstruction — observationally equivalent to a genuine 9/43 shared-obstruction correlation; NO statistic on the six scores has power above its own size. Report contamination share 1−L²_g/S_cross instead (26.5% in that case)
- Naive disattenuation r_true = r_obs/√(ρ_p ρ_j) is NOT confound-immune: reliable g forges disattenuated correlation ≈1
- Method-of-moments SEM estimator: (S_cross − L²_g)/(S_within − L²_g) — confound-safe under its assumptions, but control-specific trait violates them; SEM reference distribution for L_θ=0 boundary should use parametric bootstrap, NOT asserted ½χ²₀+½χ²₁ until derived
- V⋆ = F − Δ is a difference of two measured things: shared SIGNALLING (∆_P, ∆_J covariance) can forge positive cross-domain association without shared frustration — report all four components F_P, ∆_P, F_J, ∆_J and require survival of adjustment for the measured disturbances

## Retrospective Validation
The scoping rule ("contextual iff sufficiently frustrated and cyclic, V>0, whatever parity") postdicts all 6 published CbD verdicts: contextual cases all frustrated-cyclic (Snow Queen — an EVEN 4-cycle! — Bruza faces, impossible figures); nulls all non-cyclic or sub-threshold. Recomputation of 8 real systems from raw contingency tables matches published values to ≤0.002. Prior nulls (double-detection, polls, conjoint choices) were never frustrated cyclic — H¹=0 predicted there, so "no contextuality found" is consistent with theory, not threatening.

## Implementation Notes
- Verify control arm correlations stay uniform and below c*: preregistered anisotropy tolerance ‖c−c̄·1‖_∞ ≤ (1−|c̄|)/2 (else even control turns contextual: (0.6,0.6,0.6,−0.6) has mean 0.3 yet CF=0.2)
- Penrose tribar = H¹ with R₊ (depth) coefficients; the Z₂ version used here = cyclic-ordering bistability; coefficient group is a MODELING CHOICE (Penrose used both in one paper)
- Rigor tags throughout: [R] proved/verified, [C] conjecture, [A] analogy. All three experiments designed but UNRUN — the paper is a registered-report-style design + simulation calibration

## Cross-References
- Abramsky & Brandenburger 2011 (sheaf contextuality), ABM 2017 (contextual fraction)
- Contextuality-by-Default: Kujala & Dzhafarov; Cervantes consistification + Snow Queen
- Seely 2025 (predictive-coding operational sheaf)
- Related skills: [[sheaf-consistency-mbse]], [[formalizing-binding-problem]], [[information-coincidence-identity]]
