---
name: correspondence-score-audit-alignment
description: "Three-check audit for representational similarity scores (CKA, probe transfer, alignment). Use when evaluating brain-alignment claims, cross-lingual transfer, or any model-vs-reference correspondence metric."
category: neuroscience
---

# The Score Is Not the Structure: Auditing Correspondence Measures

Source: arXiv:2610.03827v2 (NeurIPS 2026 LP4FM workshop, 2026-10-07). Two case studies: cross-lingual probe transfer (XGLM-1.7B, 17 languages) and brain-geometry alignment (Pythia 160M/410M/1.4B fine-tuned to fMRI CKA).

## Core Claim

A correspondence score C(S,R) between model structure S and reference R is a measurement, and like any measurement it can register a quantity that is not the one intended. Before reading any similarity score as evidence of shared structure, run the audit. In both case studies, **83–92% of the celebrated score survives destroying the correspondence entirely**.

## The Three-Check Audit (run in this order — each makes the next interpretable)

### 1. Content Ablation — remove the correspondence, re-score
Rebuild R so it keeps every incidental property (statistics, shape, rank, scale) but loses the match to S:
- **Shuffled target**: permute rows (sentences) — preserves statistics, aligns with nothing
- **Rank-matched noise**: same dimension, same training pressure, no brain/language content
- **Random direction** (steering case): same perturbation magnitude, points nowhere
Share of score attributable to content = increment over these controls.

### 2. Instrument Check — is C estimated equally well everywhere it's compared?
Where C is read through a fitted probe: a probe at chance in language A supports no claim about A. **Comparability, not selectivity, is what a cross-condition regression assumes** — a probe can be perfectly selective in every language and still differ in absolute reliability between them. Report per-unit instrument accuracy alongside the gradient.

### 3. Inference Check — count independent units, not observations
Pairwise designs generate many observations from few entities (272 language pairs from 17 languages; each language appears in 32 pairs). Permute **entities** (Mantel test), not pairs. Case study: steering effect p=0.0006 (pairs) → p=0.155 (languages) — a null either way, and "the explaining away would itself have been the finding."

## Case Study 1 — Cross-lingual Transfer (the instrument failure)

XGLM-1.7B, logistic probe on subject-verb agreement (MultiBLiMP, 17 languages, 272 ordered pairs):
- Transfer decays with URIEL syntactic distance: r=−0.66 (R²=0.43) — the canonical result
- **But probe accuracy itself falls with distance at r=−0.74**, and is at chance in 4/17 languages (Hindi 0.375, Urdu 0.433, Turkish 0.493, Arabic 0.497) — the 4 most typologically distant
- Instrument and predictor are **collinear by construction** → gradient not identifiable. Dropping failed probes halves variance (r=−0.47) but also truncates the distance range — truncation alone attenuates r. Of all 2,380 possible 4-language exclusions, only 4 restrict range as much; 3 of those attenuate equally → the two explanations are not separable in this design
- Steering DOES work (within-language +6.21 nats; cross-lingual beats random-direction baseline +2.85 nats on 223/272 pairs, all 17 source languages positive) — but shows **no distance-graded effect** once languages (not pairs) are the unit (p=0.155; r=−0.09 restricted)
- Verdict: the shared direction is real as a descriptor; no evidence it is a distance-graded causal lever

## Case Study 2 — Brain Alignment (the insensitivity failure)

Pythia fine-tuned with alignment loss L_align = 1 − CKA(H, B) (layer-6 hidden states vs rank-128 PCA fMRI target, Pereira 627 sentences):
- CKA rises 0.10 → 0.34 (ceiling 0.54 split-half) — "a paper reporting only this number would be reporting a large effect"
- **Shuffled and noise targets reach 0.31** — 83–92% of the score recovered with zero brain content. Brain-specific increment: only +0.03 to +0.07 (sign-flip p<0.01 — real but tiny)
- **k/n baseline law**: target-vs-target CKA between two rank-k subspaces of n sentences ≈ k/n. Measured 0.051/0.102/0.204/0.409 at ranks 32/64/128/256 vs 627 sentences — matches k/n within 1% at every rank. **Report k/n beside any CKA against a rank-k target**; at rank 256 the null baseline alone is 0.41
- Ceiling asymmetry (deliberate): use split-half reliability as scale for model scores; do NOT arithmetically subtract the k/n baseline from model scores — a model geometry is not a target matrix (unaligned model sits at 0.095, BELOW the 0.204 target-vs-target baseline)
- **No BLiMP gain**: brain-aligned never significantly above LM-only (p=0.36/0.29/0.55), never reliably above shuffled/random controls; equivalence bounds [−0.4, +1.4] points at 160M. Four null-explanations ruled out: target not too noisy (ceiling 0.54), λ not mis-tuned (λ=10 → CKA 0.38, still no gain), models not too small (3 scales alike), training not inert (fine-tuning moves BLiMP 3–6 pts — downward, shared by all conditions)

## Decision Procedure for Practitioners

Before trusting any correspondence score:
1. Score a shuffled/rank-matched control **before training anything** — the k/n baseline is computable in advance
2. Verify the instrument works at every point being compared (per-language probe accuracy; split-half reliability)
3. Permute entities, not pairs (Mantel)
4. Only then test usefulness (downstream behavioral effect vs matched controls)
5. A positive score after the audit ≠ proportionality — report the content-attributable increment, not the headline number

## Reusable Patterns

- **Correspondence ≠ proportionality**: large CKA/similarity values are dominated by form, rank, and training pressure; the content increment is the only part that means anything
- **Selectivity vs comparability** (Hewitt & Liang control tasks): selectivity licenses "probe measures something"; comparability licenses "two probes measure it equally well" — cross-condition regressions need the second, rarely reported
- **k/n rank law for CKA**: two rank-k subspaces of R^n overlap ≈ k/n regardless of content — a pre-computable null
- **Entity-level permutation (Mantel)** for any pairwise-design significance test
- **Rule out the four null-explanations** (noise, tuning, scale, inertness) to make a downstream null interpretable

## Scope

The verdicts are operationalization-specific (one fMRI dataset, one rank-128 target, one CKA objective; one probe family, one steering strength). The audit itself is general — applies to RSA, CKA, probing, steering, any model-vs-reference correspondence claim.
