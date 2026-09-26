---
name: governed-self-evolution-anytime-referee
description: Governed self-evolution: LLM proposes, frozen anytime-valid e-process referee judges. Controls FDR in agentic loops.
category: ai_collection
trigger: LLM agent governance, anytime-valid testing, e-process, e-BH, e-detector, factor mining, FDR control in agent loops
---

# Governed Self-Evolution: Anytime-Valid Referee for LLM Agents (arXiv:2609.27051)

**Source**: arXiv:2609.27051 (Bo Qu, Mingguang Chen, Licheng Wang — DeepGrounding / AlphaAvatar, 22 Sep 2026)
**Task domain shown**: quantitative factor mining on CSI 500; architecture generalizes to any agent that proposes hypotheses scored by an exogenous outcome stream.

## Core Principle

**Who judges sets false-admission count; who proposes sets yield.** In a self-improving agent loop, the agent may propose unlimited candidates, but a **frozen statistical referee** — which the agent cannot touch — must judge. The referee's guarantee holds at every stopping time for ANY proposal policy, including self-modifying ones.

The agent's surface (proposals, diagnostics, self-written probes, memory) evolves freely. The **trust kernel** (referee + scoring data + library + append-only decision log) is frozen: cannot be mounted, patched, or intercepted.

## Why Classical Testing Fails in Agent Loops

| Agent behavior | Broken assumption |
|---|---|
| Reads verdict, resubmits until pass | Optional stopping (fixed-sample tests invalid) |
| Resubmits near-duplicates of lucky candidates | Multiplicity (batch corrections assume fixed test count) |
| Learns what the evaluator rewards | Verifier-in-the-loop adaptation |
| Trained on the eval period | Knowledge-cutoff leakage (guarantee applies to LIVE runs only) |

A correction computed in advance requires a proposal process known in advance. A learning agent has no such process — hence anytime-valid (sequential) inference is the only sound judge.

## The Referee: Three Betting Procedures

All three treat **evidence as capital** (test supermartingale W with W0=1; under H0, E[W_t|G_{t-1}] ≤ W_{t-1}; Ville: P(sup W ≥ 1/α) ≤ α).

### 1. Per-candidate admission bet (e-process)
- Candidate scored ONLY on outcomes revealed after submission (daily rank-IC stream X_t ∈ [-1,1]; H0: E[X_t|G_{t-1}] ≤ 0).
- Betting capital: W_t = Π(1 + λ_s X_s), stake λ_s fixed BEFORE outcome seen (G_{t-1}-measurable), capped λ_max < 1 (no bankruptcy).
- Stake sizing: **plug-in aGRAPA** λ_t = clip(m̂/σ̂², 0, ϕ·λ_max), cap fraction ϕ=0.8. Kelly-optimal λ* = µ/σ² exceeds the safety cap at realistic noise, so the cap sets the wait.
- **Whitening for autocorrelation**: bet on X̃_t = X_t − ρ̂_t X_{t−1} (shrunk, capped ρ̂ from past data); λ_max,t = ϕ/(1+ρ̂_t). Without whitening, AR(1) ρ=0.2 admits 6% of nulls vs nominal 5%; whitened: 1.8-2.4%.

### 2. Multiplicity: online e-BH over a frozen universe
- Universe frozen at N_v slots per epoch; candidate c gets weight γ_c = w_v/N_v.
- Admitted set R_t = {c: E_c(t) ≥ 1/(k*_t·α·γ_c)} with k*_t = max{k: #{c: E_c ≥ 1/(kαγ_c)} ≥ k}.
- Capital frozen at admission-day value; admissions never revoked. FDR ≤ α at every stopping time, under ARBITRARY dependence between candidates (e-values merge: Vovk-Wang).
- Resubmission counter-intuitively harmless: a resubmitted near-copy opens a NEW slot and only spends proposer's slots. Repetition cannot raise FDR above α.
- Bar height: first admission needs capital N_v/(α) (with N_v=2000, α=0.05 → 40,000×). Wait scales as ln(N_v/(kα))·2σ²/µ².

### 3. Retirement: e-detector (changepoint)
- Null: factor still viable E[X̃_t|G_{t-1}] ≥ δ_t = δ(1−ρ̂_t); bet AGAINST on Y_t = δ_t − X̃_t.
- **Restart every day**: new e-process W^(j) starts each day j; statistic M_t = Σ_{j≤t} W_t^(j); retire when M_t ≥ A (A*=1260 = 5 trading years, registered in advance). Restarts keep responsiveness — a single process would dilute new evidence with the healthy period.
- Stake = Kelly bet against the design alternative "full decay to zero": λ_t = clip(δ_t/2 / (σ̂² + δ_t²), 0, λ_max²) — NOT fitted to data (a data-fitted stake alarms on healthy factors).
- Guarantee: E[τ_A] ≥ A nonasymptotically, no i.i.d. assumption (Shin et al. 2024 e-detectors). Library-level error-over-patience ≤ K/A*.
- **⚠️ Calibration pitfall (verified in test run 2026-09-26)**: the run-length bound E[τ_A] ≥ A is a LOWER bound on false-alarm delay, not an upper bound on false-alarm RATE over a fixed campaign. With A=200 and δ=0.015, a simulated healthy factor (edge 0.03) falsely alarmed at day ~369. The paper registers A*=1260 (5 trading years) precisely because the guarantee is vacuous over shorter campaigns; false-retirement rate must be checked by simulation (paper: 0.5–1.5% at ρ≤0.2, 8.5% at ρ=0.4). Budget A generously and validate by Monte-Carlo before deployment.

## Validity Conditions (Proposition 1) — what an agent cannot break
The controller may be ANY policy (scripted, bandit, LLM, self-modifying) if:
1. Betting fractions and cluster weights stay G_{t-1}-measurable (agent can't size bets with future knowledge)
2. Each candidate bet only on post-submission data
3. Library frozen within an epoch
4. Candidate chosen with no info about its post-submission outcomes (holds in live runs; may FAIL in historical replay if model trained on the period — the "foretelling" counterexample: merged capital E[M]=1.25 despite each bet being fair; alignment invariant + unit test removes it)

## Economic Parameters (the registered-threshold discipline)
- **Viability threshold δ** = break-even edge = 2c·TO/κ (per-side cost c=15bp, one-way turnover TO, IC-to-return conversion κ̄=0.018 market constant — NOT estimated per-sleeve; a per-sleeve estimate inverts decisions). δ=0.015 registered before runs. δ is a signal-quality floor, not per-family economics — break-even differs by family by 10× (reversal 0.074 vs value 0.010).
- **Execution layer** separate from referee: holds certified ranking h days chosen from 5 desk frequencies, net(h) = κ·mean IC(1..h) − 2c·τ(h); shelve factor if max_h net(h) ≤ 0. Execution neutrality (Proposition 2): book recomputable from append-only log without re-running the agent (auditability + free counterfactual re-booking).

## Measured Results (what to cite)
- **Synthetic (planted truth)**: frozen referee 0 false admissions every seed; leaky (peeking t-test / adaptive threshold / no-gate) 0.26–0.85 per submission REGARDLESS of controller. Hidden-retry attack extracts +0.027 false/submit from peeking referee, zero from frozen.
- **Real CSI 500 (10y walk-forward)**: frozen 11.7 false admissions/campaign vs leaky 86–196 (round-robin), 37–78 (LLM). Post-admission-only re-judging: 5–11× advantage.
- **LLM controller value**: beats round-robin yield in 6/6 family×library settings; ≈ bandit on allocation (bandit is a strong baseline because slots don't dilute); UNIQUE capability = authoring diagnostic probes (lowers intervention regret 0.23–0.39 in 3/6 families, never hurts). Memory ablation: 0/10 significant. Under leaky referees, LLM partially substitutes for the missing judge (reduces false admissions vs round-robin 4/4) — apparent skill from the leak.
- **Cost of certification**: median wait ~500 trading days/admission (information bound: wait ~ ln(N_v/kα)·2σ²/µ²; at σ≈0.12, µ=0.015, no bettor certifies <5 years). Certified book net Sharpe +0.33–0.50 vs ungated +0.59–0.77. Two causes: (a) **horizon mismatch** — daily certificate can't see slow factors (momentum IC 0.001/day but 0.009 at 63-day hold; ungated book earned from 892 momentum sleeves, frozen held 6); (b) the **wait** is paid in regimes. A 500-day fixed-horizon t-test+BH comparator with same patience builds a BETTER book (+0.12–0.24 Sharpe) — because the anytime-valid bar favors the strongest-per-day statistic (short-horizon reversal, worst net economics). **Design lesson: certify the horizon that is traded, not the daily one.**

## Reusable Pattern (apply to any agent-with-evaluator system)
1. Split the loop: swappable **agent surface** vs frozen **trust kernel** (referee, scoring data, hypothesis library, append-only decision log, cost meter).
2. Score candidates only on outcomes revealed after submission (alignment invariant: everything used at t is G_{t-1}-measurable).
3. Judge with betting e-processes: per-candidate e-BH admission + e-detector retirement; guarantee survives any proposer.
4. Register thresholds (α, δ, A, slots N_v) BEFORE runs; never tune post hoc.
5. Keep a counterfactual comparator: same patience, fixed-horizon test — measures what anytime-validity buys beyond valid-but-fixed.
6. For LLM roles: keep direction/diagnosis/probe-authoring on the agent; never let it judge its own proposals.
7. Probes and instruments written by the agent never enter statistical inference (zero multiplicity cost).
8. Replay caution: a model trained on the eval period breaks condition (iv) — report live vs replay separately.

## Cross-References
- Anytime-valid foundations: Waudby-Smith & Ramdas 2024 (aGRAPA betting); Wang & Ramdas 2022 (e-BH); Fischer et al. 2024 (online e-BH); Shin et al. 2024 (e-detectors); Vovk & Wang 2021 (e-value merging); Ville 1939.
- Related in collection: [[conformal-e-process-changepoint-detection]] (weight-norm regime switch for e-process/e-detector), [[river-rl-without-ground-truth]] (verifiable agent ranking), [[llm-self-correction-confidence-signals]].
- **KG**: arXiv:2609.27051, cs.AI/q-fin.PM/q-fin.ST
