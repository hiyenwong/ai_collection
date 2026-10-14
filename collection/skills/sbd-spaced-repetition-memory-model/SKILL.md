---
name: sbd-spaced-repetition-memory-model
description: Interpretable 3-state spaced-repetition memory model.
category: ai_collection
tags: [spaced-repetition, memory-model, forgetting-curve, survival-analysis, restless-bandit, whittle-index, interpretable-model]
---

# SBD: Interpretable Memory Models for Spaced Repetition (arXiv:2610.10548)

## When to Use
- Build a flashcard / review scheduler that predicts recall probability P(remember | t)
- Need a mechanistically interpretable memory model instead of a black-box sequence model
- Schedule reviews under a daily budget (restless bandit) or a per-review cost (Bellman)
- Applies beyond flashcards: any "when to re-engage a decaying item" problem (retraining cadence, cache refresh, re-inspection scheduling)

## Core Framework: Three State Variables

A card carries state x = (s, b, d) with 7 fitted weights w1–w7:
- **Stability s**: scale of the memory's lifetime (Gamma scale of forgetting rate)
- **Brittleness b**: how incomplete the last review's "repair" was (virtual-age carryover)
- **Difficulty d**: tally of failures/hard passes; raises the forgetting-rate exponent

### Dynamics (per review at age t, rating q∈{1..4})

1. **Age (Jost's law + Kijima virtual age)**: `a = t^(1/w1) + sqrt(b·s)` — time compressed sub-linearly; a review is an *imperfect repair* adding virtual age √(bs)
2. **Decay exponent**: `α = w2·d^w3` — difficult cards forget faster at every age
3. **Forgetting curve (Gamma frailty survival)**: `R(a) = (1 + (a/s)^α)^(-1/α)` — Burr XII / Wickelgren power law; without repair term it reduces to classic power-law forgetting
4. **Stability update**: pass (q≥2) → Bayesian-style `s' = s + a` (keep α, absorb age); fail (q=1) → `s' = s·(1-R)^w3` — a *lapse is damage*, scaled by the surprise (1-R): expected failures erase little, surprising ones erase much
5. **Brittleness update**: `b' = w4·w5^(1-q)` — highest after failure, lowest after easy pass
6. **Difficulty update**: `d' = d + max(3-q, 0)` — monotone tally of failures/hard passes
7. **Init**: `(s0,b0,d0) = (w6·w5^(q0-1), w4·w5^(1-q0), w7 + max(3-q0,0))`

Binary variant (trained on binary ratings) keeps 7 params and has **self-contained updates** — required for planning.

## Why Parsimony Beats Accuracy (the Lucas critique argument)

Available logs come from intervals *existing schedulers chose*; a new scheduler must extrapolate outside that band, and test-set accuracy cannot certify extrapolation. Three model constraints follow:
1. **Reliable extrapolation** → every term needs a mechanistic reason beyond fit quality
2. **Simple state dynamics** → planners discretize or roll the state; exponential blowup otherwise
3. **Self-contained updates** → every model input must be model-produced (rules out features measured after last review)

This is a transferable pattern: **when data is generated under one policy but the model will be used under another, prefer the most parsimonious model whose every parameter has a mechanistic interpretation.**

## Scheduling

### Per-review cost λ (value iteration)
Maximize discounted area under recall curve:
`V(x) = max_t ∫₀ᵗ γ^τ R(τ)dτ + γᵗ[R(t)V(x_pass(t)) + (1-R(t))V(x_fail(t)) − λ]`
The optimal interval t*λ(x) falls out of value iteration on the 3-d state.

### Daily budget B (Whittle index)
Cards compete for slots → restless bandit (PSPACE-hard). Whittle relaxation: each card gets index η = the review cost at which indifferent review-now vs wait, i.e. η s.t. `t*η(x_waited) = t`. Policy: review the B cards with largest index daily; asymptotically optimal under indexability. New-card introduction handled naturally.

## Results (anki-revlogs-10k, 10k review logs)

| Model | Weights | BCE | AUC |
|-------|---------|-----|-----|
| FSRS-7 (SOTA) | 34 | 0.3237 | 0.7517 |
| SBD | 7 | 0.3279 | 0.7441 |
| SBD binary | 7 | 0.3296 | 0.7329 |

~1% behind SOTA at **80% fewer weights**; pretrained-only SBD *beats* FSRS-7 on RMSE(bins) calibration by 2%.

## Implementation Notes
- Training: recent reviews weighted more; Gaussian prior pulls each weight toward pretrained value (width from per-user fit spread, strength decays as user accumulates reviews)
- Eval protocol: per-user metrics averaged (not pooled); 5-block temporal splits
- Fine-tuning vs pretraining gap matters: report both
- Code: github.com/andersschill/memory-model-benchmark-for-spaced-repetition

## Key Formulas to Reuse
- Gamma-frailty survival: `R(a) = (1 + (a/s)^α)^(-1/α)` with shape α, scale s
- Imperfect-repair virtual age: `a = t^(1/w1) + sqrt(b·s)` (Kijima class)
- Surprise-scaled damage: `s' = s·(1-R)^w3` — expected failures cost little
- Whittle index from cost-parametric optimal interval: invert `t*η(x) = t`

## Related
- FSRS/DHP (Ye et al. 2022, Su et al. 2023) — 34-weight SOTA baseline
- Ebisu — per-card Beta posterior via moment matching (no global fit)
- ACT-R / DASH / DAS3H — feature-regression alternatives
- Lucas (1976) — policy-shift extrapolation argument
- Whittle (1988), Weber & Weiss (1990) — restless bandit indexability

## Source
Schill, A. (2026). Interpretable Memory Models for Spaced Repetition. arXiv:2610.10548 [q-bio.NC].
