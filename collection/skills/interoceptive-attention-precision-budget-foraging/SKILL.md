---
name: interoceptive-attention-precision-budget-foraging
description: "Interoceptive precision routing in active-inference agents"
tags: [active-inference, interoception, precision, attention, foraging, homeostasis, active-inference-agents, kappa-attention]
---

# Interoceptive Attention as Dynamic Homeostatic Prioritization (κ-Budget Routing in a Foraging Agent)

**Source**: arXiv:2608.04232v1 (2026-08-04, cs.AI/q-bio.NC) — Grimbly, Kuske, Boonstra, Bassett, van Hoof, Hodson. Shows that routing a **fixed interoceptive precision budget** toward the currently most-needed bodily channel (driven by the agent's own beliefs) more than doubles foraging survival — and the gain flows through PLANNING as much as perception.

**Activation**: active inference agent design, interoceptive precision allocation, attention-as-precision, multi-need homeostatic agents, homeostatic RL alternative, active-inference foraging gridworlds, need prioritization mechanism, precision budget constraints.

## When to Use
- Designing active-inference agents with MULTIPLE competing bodily needs and limited perceptual bandwidth
- Modeling attention as precision allocation (κ) rather than adding reward terms
- Deciding WHERE a precision/attention signal should act (belief update vs policy evaluation)
- Needing falsifiable ablation battery for attention-like mechanisms

## Mechanism (κ-Attention)
1. **Fixed budget**: Σ_m κ_m ≤ K (=2.60 across 4 channels), per-channel floor κ_floor=0.05, cap 1. Attended channel κ_att=0.90, others κ_un=(K−κ_att)/3≈0.567. Uniform control: κ=K/4=0.65 everywhere — ALL agents compared at IDENTICAL budget.
2. **κ is the likelihood diagonal**: A^(m)_{o,s} = κ_m if o=s else (1−κ_m)/5 — the SAME shaped likelihood matrix feeds BOTH the per-step belief update AND the expected-free-energy (EFE) planner.
3. **Belief-driven selector (never ground truth)**: m* = argmax_m E_{q(s_m)}[need_m], need_m=(s_max−s)/s_max. Selector reads only posterior beliefs; body model itself is learned online (Dirichlet pseudo-counts on A, prior concentration α0 controls rigidity).
4. EFE = risk (KL to preferred replete observations) + ambiguity (expected likelihood entropy); policies P(π) ∝ exp(−γG(π)), γ=16, horizon H=3.

## AffectWorld Testbed
- 6×6 gridworld, hunger/thirst (lethal, decay 1/step) + suffocation (non-lethal, depletes on water tiles — a need to prioritize WITHOUT second mortality route) + 1 inert control channel (anchors agent-vs-uniform comparison: a no-signal channel cannot create the survival gap)
- 12 layouts (easy/medium/far), 11 used for headline; n=32 seeds × 100 trials; survival = reach 60-step horizon
- Stats: paired cluster-bootstrap, Holm-corrected

## Key Results
1. **Selective ≈ doubles survival**: 0.414 vs 0.199 (2.08×, p≤10⁻⁴). Oracle ceiling (true dynamics) only 0.66 — task genuinely hard.
2. **Direction is the mechanism, not unevenness**: anti-aligned control (same split, least-needed channel) = 0.144, significantly BELOW uniform. Need-aligned rule climbs monotonically with κ_att asymmetry; anti-aligned stays flat (~0.36); +44–46pp gap at κ_att 0.90–0.99.
3. **Propagation ablation locates the pathway**: inference-only (planner sees uniform A) loses 20pp at α0=0.1; at α0=10 loses 88pp, collapsing to anti-aligned level. Planning-only ablation alone reaches 0.865 easy-tier (≈ full model). → The planner's use of shaped likelihood carries ~half the benefit at default priors and nearly ALL under rigid priors. Inference-stage shaping becomes necessary only when prior overrides state inference.
4. **Robustness**: attentive holds ~0.85 plateau survival across α0∈{10⁻³..10²} while uniform collapses at α0≥10; advantage at every K∈{1.5..4.0} (32–56pp), both peak at K=2.60 (at high K uniform suffers planner-overcommitment; selective keeps policy posterior softer); survives tile-mutation non-stationarity 0.02–0.10.
5. **Dynamic beats fixed**: ties always-attend-hunger on easy layouts (0.83) but wins under rigid priors (~0.90 vs 0.65) and forced need-switching (+23.5pp).
6. **Per-observation learning acceleration**: attended channel's likelihood model converges ~2.4× faster; +0.31 accuracy above uniform AT MATCHED observation count (not a data-quantity artifact); anti-aligned also accelerates (+0.22) → any non-uniform allocation buys some speedup, direction adds +0.09. Mechanism: κ sharpens Dirichlet updates at the update step itself.

## Implementation Notes
- Factorized POMDP: fixed body-transition prior B + learned observation likelihood A (Dirichlet). κ-shaping touches A only.
- Code: github.com/sgrimbly/attention-aif-sab2026-snapshot
- Budget K=2.60 chosen so attended channel informative (0.90) while others not blind (~0.57) — at K=4 the cap binds, muddying the direction claim; keep sweeps where no channel saturates.

## Pitfalls / Scope
- κ-routing is HAND-SPECIFIED; whether a learned router converges to need-aligned policy is open
- Selector assumes body-state posterior well-calibrated to true need — under strong miscalibration the mechanism can misroute (untested)
- Claim is 'one sufficient implementation', not uniquely identified vs alternative actuation sites; a matched preference-reweighting comparator (change planner target only, no likelihood sharpening) is the missing decisive test — note sibling paper's dissociation below
- Minimal gridworld → biological readings (interoceptive gain-modulation by urgency) are hypothesis-generating only

## Verified Information-Theoretic Structure (17/17 numeric checks passed)

- **MI(κ) is convex in κ** (channel entropy is concave in a distribution that is linear in κ), so at fixed Σκ the TOTAL channel information is maximized at EXTREMES, not at uniform: selective (0.90 + 3×0.567) carries 3.659 bits vs uniform 4×0.65 = 3.353 bits (+0.306 bits, 6-level channels).
- **Anti-aligned allocation has IDENTICAL total MI** to selective (same magnitudes, different target) — so the survival/learning gap between them (attentive beats anti-aligned by ~0.09 at matched observation count) is NOT channel information; it is need-targeted action. Convexity explains the paper's finding that any non-uniform allocation buys acceleration (anti-aligned +0.22 above uniform); direction adds the rest.
- Monotone climb of total MI with κ_att at K=2.60 (3.353 → 4.020 bits as κ_att 0.65→0.99) mirrors the paper's monotone behavioral climb with asymmetry (+44pp @0.90, +46pp @0.99).
- Verification anchors: κ_un=(2.60−0.90)/3=0.5667; A columns valid ∀κ (κ+5(1−κ)/5=1); MI(0.90)=1.884 > MI(0.65)=0.838 > MI(0.567)=0.592 bits; min 2nd difference of MI over κ∈[0.05,0.98] = 5.2e-3 > 0; 0.414/0.199=2.080×; cap binds only at K≥3.90 (at K=4: (4−0.9)/3=1.033→clipped, allocated 3.9).

## Related Skills
- [[interoceptive-prioritisation-precision-preference]] — arXiv:2610.18617, the two-routes dissociation (κ-likelihood routing vs preference reweighting) in active inference; this skill supplies the foraging-agent mechanism study
- [[belief-mop-active-inference-bellman]] — POMDP belief-MOP active inference machinery
