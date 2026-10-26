---
name: correspondence-score-structure-audit
description: "Audit protocol for correspondence scores (brain alignment CKA, cross-lingual probes) — ablate the correspondence, check instrument reliability, count independent units. Use before claiming a similarity score means shared structure."
category: ai_collection
source_paper: "The Score Is Not the Structure: Brain Alignment and Cross-Lingual Transfer (arXiv:2610.03827)"
trigger_words: correspondence score audit, brain alignment CKA, shuffled target baseline, reliability ceiling, probe transfer, typological distance, unit counting, Mantel permutation, content ablation, instrument reliability
---

# Correspondence Score Structure Audit

**Paper**: Saman Rahbar, "The Score Is Not the Structure: Brain Alignment and Cross-Lingual Transfer" (arXiv:2610.03827v2, NeurIPS 2026 LP4FM workshop poster)
**Code**: https://github.com/saman-rahbar/score-is-not-the-structure

## TL;DR

Two methodologically unrelated settings (model↔brain alignment via CKA; cross-lingual probe transfer) fail the same three-part audit: a large share of each correspondence score is **not the correspondence**. A permuted/noise fMRI target recovers **83–92%** of a brain-alignment CKA score; a typological transfer gradient is partly probe reliability in disguise; pair-counting turns a null into p=0.0006. A contaminant that **co-varies with the signal inflates the effect instead of masking it** — tight CIs don't help because they're tight around the wrong quantity.

## The Three-Part Audit Template

Run these three checks **in order**, before interpreting any similarity/correspondence score C(S, R) between model structure S and reference R:

### 1. Content ablation — rebuild R without the correspondence
- **Shuffle**: permute target rows (preserves stats/shape, lines up with nothing)
- **Noise**: rank-matched Gaussian of same dimension (keeps training pressure)
- **Random direction**: same magnitude as real steering direction (for steering studies)
- Re-score C against these ablations. **Only the increment over ablation is attributable to content.**
- KEY REGULARITY (measured, verified at 4 ranks within 1%): two rank-k targets of n items score CKA ≈ **k/n** against each other regardless of correspondence. Report k/n beside any CKA against a rank-k target; score a shuffled target of the same rank BEFORE training anything. Rank 256 of 627 sentences ⇒ baseline 0.41.

### 2. Instrument check — is C equally reliable everywhere it's compared?
- Where C reads through a fitted probe: a probe at chance within a language makes its transfer accuracy **uninterpretable**, no matter why it fails.
- Reliability must NOT co-vary with the predictor. Measured: within-language probe accuracy falls with typological distance at r = −0.74; 4/17 languages at chance (Hindi .375, Urdu .433, Turkish .493, Arabic .497), and those 4 rank 1st/3rd/4th/5th most distant → contaminant collinear with predictor by construction → **gradient magnitude not identifiable** without a control separating them. Dropping them halves variance (r −0.66 → −0.47) but truncates the predictor range, so the two explanations cannot be separated in-sample. The claim must be weakened to "not identifiable without a reliability control."
- For fMRI targets: **split-half noise ceiling** (split-half CKA between independent participant halves, identical rank-k construction). Ceiling ≈ 0.54 here vs raw-voxel reliability 0.11. Nothing measured against a target can exceed its reproducible part.

### 3. Inference check — count independent units
- Pairwise designs generate many observations from few entities. Permute the **entities** (languages), not the pairs — standard Mantel construction.
- Measured: steering effect p = 0.0006 counting 272 pairs as independent → p = 0.155 when 17 languages are the unit. **One permutation choice away from a false finding.**
- Ceiling asymmetry (deliberate): use the reliability ceiling to scale model scores; do NOT arithmetically subtract the k/n baseline from model scores (model geometry is not a target matrix; unaligned model sits at 0.095 < baseline 0.204). Ceiling is a reliability bound; baseline applies only to target-to-target comparisons.

### 4. (Only then) Usefulness test
- Verify the intervention works before testing its variation: steering works within-language (+6.21 nats, 16/17 positive) and cross-lingually (+2.85 nats, 223/272 pairs) — this is what makes the distance-null informative rather than empty.
- Brain-aligned fine-tuning: CKA 0.10→0.34 (62–78% of ceiling) but **zero BLiMP gain** over LM-only/shuffled/random at any scale (160M/410M/1.4B, 20/8/8 seeds). Equivalence bounds: true 160M effect within [−0.4, +1.4] BLiMP points.
- Nulls stay interpretable only because the audit ran first: target not too noisy (ceiling), λ not mistuned (λ=10 → CKA 0.38, still no gain), models not too small (3 scales agree), training not inert (fine-tuning moves BLiMP 3–6 pts, cancels across conditions).

## Empirical Headlines (Both Studies)

| Study | Decisive check | Numbers |
|---|---|---|
| Brain alignment (Pythia 160M/410M/1.4B, Pereira 2018 fMRI 627 sentences, layer-6 mean-pooled, rank-128 PCA target, L=1−CKA, λ=1) | Content ablation | Shuffled/noise targets reach 0.31 vs brain 0.34; brain-specific increment +0.028/+0.068/+0.064 (5–13% of ceiling), sign-flip p<0.01 paired over seeds — real but tiny; alignment pressure does the rest |
| Cross-lingual (XGLM-1.7B, 17 languages, MultiBLiMP minimal pairs, mid-layer verb-position logistic probe) | Instrument check | Transfer r = −0.66 (R²=0.43); probe reliability gradient r = −0.74; restricted 13-language r = −0.47 with bootstrap spanning zero [−0.77, +0.18] |
| Both | Unit counting | Language-level permutation: transfer p=10⁻⁴ survives; steering p 0.0006→0.155 does not |

Setup details worth copying: 4 training conditions identical except target — LM-only (λ=0) / brain / shuffled / random; 16-sentence batches, H = layer-6 hidden states mean-pooled per sentence, B = matched fMRI rows, L_align = 1 − CKA(H,B) added to next-token loss; 6 epochs AdamW lr 5e-5 wd 0.01. Probe: L2 logistic (C=1) on standardized features, 300 minimal-pair cap (180 train) per language — training-size differences ruled out by design (accuracy vs train size r = −0.04; Basque 163 examples → 0.755 beats all four failures).

## Why These Failures Are Easy to Miss

The contaminant **co-varies with the signal** (second-order structure travels with real fMRI targets; probe reliability travels with typological proximity) — it inflates rather than obscures. A confidence interval on the score is tight around the wrong quantity. Also: selective probes (Hewitt–Liang control tasks) measure within-language memorization; **comparability** — whether two probes measure equally well across languages — is the orthogonal property cross-lingual regressions actually assume.

## Reusable Protocol (Any Correspondence Score)

1. Compute C(S, R) as usual.
2. Build shuffled / noise / random-direction ablations of R; re-score. Report C_model, C_ablated, Δ = C − C_ablated.
3. For rank-k targets: compute k/n analytic baseline in advance; sweep a few ranks to verify.
4. Measure instrument reliability (probe accuracy per stratum, or split-half ceiling) and check its correlation with the study axis. If collinear → report "not identifiable" instead of the gradient magnitude.
5. Permute entities, not pairs (Mantel). Report both unit-level and pair-level p only to expose the gap.
6. Prove the intervention works (positive control) before reading any null about its variation.
7. Only then test usefulness on downstream behavior B with matched controls.

## Limitations the Paper Itself Flags

- Single fMRI dataset (627 sentences), mean-pooled rank-128 target, one similarity objective — bounds the operationalization, not brain content in general (only 5–13% of ceiling was brain-specific here).
- One model family each; one layer/token position chosen a priori (mid-layer, agreeing verb); nonlinear interventions untested; language-level permutation treats languages as exchangeable (Hindi–Urdu, Romance families violate); random direction matched in size but not in span.

## Related

- [[brain-alignment-causal-dissociation-attention-heads]] — audit protocol: alignment vs causal scores cross-correlation (complementary: this skill adds ablation + unit-counting)
- [[snr-sample-size-representational-alignment]] — alignment vs data quality/quantity
- [[stimulus-symmetries-rsm-confound]] — stimulus-driven RSM confounds
- [[lpact-brain-lm-alignment-evaluation]] — locked-predictive alignment testing
- [[llm-eeg-graph-refinement]] — clinical-graph variant of alignment claims
