---
name: flyhack-connectome-claim-stress-test
description: "Stress-testing mechanistic claims in connectome-constrained models (flyvis). Use for scoping circuit conclusions."
category: ai_collection
tags: [connectome-constrained-models, flyvis, mechanistic-claims, attribution-matching, circuit-discovery, reverse-phi, adversarial-robustness, ensemble-degeneracy]
---

# FlyHack: Stress-Testing Mechanistic Claims in Connectome-Constrained Models

**Source**: arXiv:2610.13018 (Dhawan, University of Florida, q-bio.NC, Oct 2026)

## What It Is

A stress-testing framework for mechanistic claims derived from connectome-constrained neural networks, demonstrated on **flyvis** (Drosophila motion-vision model, 64 cell types, 721 hexagonal columns, ~45k neurons, 1.5M neuron-level connections, 734 free parameters, 50-model released ensemble). The core result: mechanistic conclusions from connectome-constrained models are **conditional** on four axes — comparison model, intervention semantics, circuit representation, and trained ensemble member. Claims must be scoped to all four, not stated as properties of "the connectome".

## Core Contributions

### 1. Model-family behaviour is not wiring-specific
- Task-matched causal CNN controls (8.2k / 50k / 988k params, same task/Sintel rendering/target/loss/lattice) show **three-level reverse-phi reversal in both families** — period- and velocity-dependent (e.g. flyvis 46/50 models at 30°/98.6°/s but 25/50 at 65.7°/s; CNNs reverse at 90°/65.7°/s but never at 90°/197.2°/s). Neither family reproduces the fly's stationary-sawtooth response (preregistered prediction FAILED: 3/50 models, median 2.3-2.6% of moving-grating response).
- Adversarial direction-reversal (ℓ∞ PGD): flyvis needs ϵ*/contrast = 0.21–0.27 vs parameter-matched CNN 0.13–0.25, but the margin gap **largely closes for larger CNNs** (within factor 1.4). Attack advantage over naive counter-grating ≈ 2 in both families — the optimized perturbation concentrates opposite-direction motion energy, not a wiring-specific weakness.
- Perturbation transfer shows NO consistent family ordering (0.15 flyvis→flyvis vs 0.29 CNN-seed→CNN-seed at own ϵ*; reversed at fixed bound: 0.61 vs 0.50).

### 2. Attribution must match the intervention (the central methodological finding)
Ground truth = **exhaustive single-connection interventions** over all 604 type-to-type connection classes, with four replacement semantics: zero, same-stimulus mean (LEAKS stimulus info — diagnostic only), held-out mean (primary), counterfactual.
- **Zero-aligned EAP evaluated against held-out ground truth: Spearman 0.126. Matched EAP: 0.872.** Same method, same model, 7x agreement gap. Under counterfactual: 0.279 → 0.813.
- Zero-aligned IG is likewise crippled by mismatch (0.007 P@20 vs 0.485 matched; Spearman 0.122 vs 0.565).
- Important-edge IDENTIFICATION is robust to mismatch (AUROC > 0.91 in every row), but effect-size ordering and circuit-set composition are not: matched EAP places ~13/20 true top-20 in its own top-20 (P@20 0.44–0.66).
- **Rule: an attribution score answers only the causal question encoded in its baseline/path. Never compare a zero-ablation score against a mean-replacement ground truth.**

### 3. Circuit conclusions vary with representation and ensemble member
- Greedy cell-type sets meet a model-relative T4/T5 tuning criterion (Ftun ≥ 6) in only **25/50 models**; T4/T5 output silencing reduces the 8-clip optic-flow score to F ≤ 2 in 40/50.
- Expanding successful type sets into source-active connections then greedily pruning removes **74–91%** (57–149 of 71–164 added connections), leaving 13–31 connections — compactness is partly an artifact of intervention granularity.
- Post-hoc two-sided response-amplitude check: only **2 of 6** first-success cell-type sets still pass (Ftun 5,6,5,7,4,1 vs threshold 6).
- Agreement with the canonical T4/T5 preferred-direction layout is only **190/400 subtypes** (47.5%), identical under moving-edge measure; no rotation/reflection of the canonical layout does better.
- Ensemble splits (success/failure of greedy search, T4/T5 sensitivity) show NO association with the release's legacy task-error ranking (Mann-Whitney p = .780/.313) — task performance does not identify biologically-matching circuit solutions.

### 4. Evaluation artefacts catalogue (Appendix B)
- Two-level periodic reverse-phi is phase-equivalent to translation — contrast-inverting gratings are not an independent stimulus class.
- A one-sided retained-output metric is satisfied by degenerate sub-networks.
- Same-input mean-current ablation leaks stimulus information; same-stimulus mean replacement "finds" 4.5-connection "circuits" in 16/20 cases of which **only 3/16 contain any photoreceptor→decoder path** — the compactness is stimulus leakage, not a compact circuit.

## How to Use / Protocol

1. **Scope claims**: When reading any connectome-constrained-model result, record (model family, intervention semantic, circuit representation, ensemble member). A claim missing any axis is unscoped.
2. **Match attribution to intervention**: Choose the replacement semantics (zero / held-out mean / counterfactual) BEFORE computing IG or EAP; construct the attribution path for that same semantics (global path w(α)=αw with replacement-current field removed: x(α) = x + (1−α)R).
3. **Exhaustive ground truth when feasible**: With 604 connection classes, full single-component sweeps are affordable; score top-k sets by interventional reproduction (direction within 45°, magnitude ratio [0.5,2], bounded activity) on 8 clips, not by attribution ranking.
4. **Ensemble-first**: Never report a circuit claim from one trained solution; run the intervention across all available ensemble members and report the success fraction with Wilson CIs (e.g. T4/T5 silencing: 80.0%, 95% CI 67.0–88.8%).
5. **Detect leakage**: If an ablation replacement uses data derived from the test stimulus (same-stimulus mean), treat all downstream compactness results as suspect; verify found "circuits" contain a complete input→output path.
6. **Preregister + report failures**: Directional predictions stated before analysis; failed predictions (stationary sawtooth) reported alongside successes.

## Key Numbers

| Quantity | Value |
|---|---|
| Models where greedy cell-type search passes Ftun ≥ 6 | 25/50 |
| T4/T5 silencing reduces score to F ≤ 2 | 40/50 (80%, CI 67-89%) |
| Canonical T4/T5 preferred-direction agreement | 190/400 (47.5%) |
| EAP Spearman: zero-aligned → held-out GT | 0.126 |
| EAP Spearman: held-out-matched → held-out GT | 0.872 (AUROC 0.970) |
| Connection pruning of type-derived sets | 74–91% removable, 13–31 remain |
| flyvis adversarial margin ϵ*/contrast | 0.21–0.27 (vs CNN-small 0.13–0.14) |

## Related Skills / Concepts

- [[connectome-wiring-statistics-control]] — separating wiring specificity from statistical control
- [[correspondence-score-structure-audit]] / [[correspondence-score-audit-alignment]] — related caution for RSA/CKA-style representational scores
- [[boundary-preserving-null-connectome]] — rewired nulls for connectome claims
- Beiran & Litwin-Kumar (2025) connectivity underdetermination; Karaneen et al. (2026) retraining non-identifiability; Marder & Goaillard (2006) degeneracy.

## Citation

Dhawan, A. (2026). FlyHack: Stress-Testing Mechanistic Claims in a Connectome-Constrained Visual Model. arXiv:2610.13018.
