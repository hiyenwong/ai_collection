---
name: imagined-speech-cross-subject-null
description: EEG imagined-speech content does not transfer across people.
created: 2026-10-17
source_paper: "arXiv:2610.20954 - Cross-subject decoding of imagined speech from scalp EEG: a leakage-controlled evaluation on three public corpora"
---

# Imagined-Speech Cross-Subject Null (arXiv:2610.20954)

**Use when**: evaluating cross-subject/cross-person BCI transfer claims, designing leakage-controlled EEG decoding protocols, diagnosing why a "state vs rest" decoder is not decoding the intended mental content, or deciding whether to collect more trials vs build a fancier model.

## Core Finding (negative result, bounded)

Across 3 public corpora (ds003626, KaraOne, 2020 BCI Competition Track 3) and **482 ordered participant pairs**: imagined-speech **content did not transfer between any pair of people** — mean pair-transfer accuracy within 0.006 of chance on every corpus; no pair survived FDR correction. Subject-level alignment (Euclidean/Riemannian), source-participant selection, and representational similarity all confirmed **no shared class geometry**. The obstacle is in the **signal and data quantity, not the decoder choice**.

Companion paper: eeg-speech-decoding-detection-floor-audit (arXiv:2610.20942) — the null results here are detection-floor-bounded (band-power reference detects 0.54 µV injected mu/beta ERD; phase features detect 5-10% mixing).

## The Leakage-Controlled Protocol (reusable checklist)

1. **Split integrity by assertion**: one module generates every split; run HALTS if a trial appears in >1 set, if a LOSO test participant appears in training, or if a test class is absent from training. No selection signal ever taken from test data.
2. **Four statistics per cell**: exact binomial per-participant threshold (α=0.05) + count above it; one-sided Wilcoxon signed-rank vs chance; BCa bootstrap 95% CI; BH-FDR within test families (q = adjusted p).
3. **Shuffle-label control for every positive result**: permute labels within participant, re-run identical pipeline 200× (50× for networks); result stands ONLY if null mean ≤ chance AND observed > null 95th pct.
4. **Pitfall**: within-subject shuffle nulls fall BELOW chance (permuted-label training is anti-correlated with held-out fold → anti-conservative p-values). Use binomial threshold + group test for within-subject decisions; use shuffle control only for "does the pipeline manufacture signal".
5. **Report macro-F1 alongside accuracy**: F1 < accuracy (e.g. 0.1796 vs 0.2063 LOSO) indicates uneven predictions from training-participant asymmetries — a tell of no learned class structure.

## State-vs-Content Diagnostic (the key methodological transfer)

Imagery-vs-rest on KaraOne generalized (~0.61 LOSO after artifact/elapsed-time controls) — but the decoder labelled the **pre-imagery interval** (prompt perception + articulator preparation, NO imagery) as imagery as often as imagery itself. The contrast reads a **post-stimulus state**, not imagery.

**Rule**: before attributing a state-vs-rest result to a mental content, decode a matched **post-stimulus interval containing no imagery** from the same trials; if it carries the same distinction, the effect is a state change following the stimulus.

Implementation: cut rest (−2.0–0.0 s), pre-imagery (0.0–+2.0 s), imagery (from +2.03 s) windows from identical preprocessing; train rest-vs-imagery decoder on other participants, apply to all three windows of held-out participant; a content decoder must label pre-imagery as rest. Split grouped by trial so rest and imagery never split across folds (elapsed-time confound control).

## Why Reported Accuracies Diverge (audit triggers)

- **Segment-wise splitting** lets classifiers recognize the recording, not the class — inflates deep-model accuracy substantially.
- **Feature/model selection outside CV** and selection on test data bias the same direction.
- **Block designs**: slow drift becomes a condition proxy (ds003626 condition collinear with time).
- **Prompt-type confound (KaraOne)**: word-vs-phoneme prompt type alone decodes at 0.8371 with 14/14 above threshold; restricting to 7 phonemes removed an imagined-speech effect entirely (+0.0288 p=0.0011 → −0.0015 n.s.). Any contrast with unequal word proportions rides on prompt type.
- **Small test sets**: theoretical chance is misleading; single CV estimates carry wide error bars — always report exact binomial thresholds.

## Five Explanations for the Within-Subject Ceiling (strong-inference exclusion)

Each hypothesis got an experiment that could overturn it:

| # | Hypothesis | Test | Verdict |
|---|---|---|---|
| 1 | Upstream failure (rest vs task fails) | ds003626 three-way condition contrast | EXCLUDED (decodes 0.6079) |
| 2 | Too many features | single band, PCA 16/32/64, anatomical region, 5× cropped training | EXCLUDED (dimensionality reduction LOWERED accuracy) |
| 3 | Missing cross-channel structure | 23 Riemannian configurations | EXCLUDED (covariance ≈ band power) |
| 4 | Wrong analysis window | 500 ms windows in 50 ms steps, cluster permutation | EXCLUDED (no better window) |
| 5 | Too little data per class | trial-count is the ONLY variable ordering corpora (12→80/class) | **SURVIVES** |

Conclusion: collect **more trials of the target condition per participant**, or methods extracting more from few trials — not further decoder development. Adding trials from other conditions of the same words did NOT substitute.

## Key Numbers

- Within-subject (only corpus above threshold for every participant): competition corpus 0.3147 held-out (chance 0.200, 15/15 above binomial threshold) — but its frequency profile **failed an artifact audit**.
- ds003626 inner speech LOSO: 0.2590, 0/10 above threshold. KaraOne words LOSO: 0.2643, 1/14.
- KaraOne strongest binary result (/iy/ contrast, 0.5883 with prompts held out) was explained by **prompt type**.
- Session leakage inflates ceiling by +0.0162 avg (largest 0.0402 on KaraOne) — pooled-session 5-fold numbers are optimistic.
- EEGNet on pronounced speech: 0.4231 within-subject but 0.2511 LOSO — within-subject success says nothing about transferability.

## What Would Falsify This

Shared structure in a representation not computed here. Explicitly not covered: class-dependent phase locking (amplitude/covariance decoders blind at any injected size), phase tied to an internal event with variable timing. Foundation models pretrained on large EEG collections not evaluated. A positive cross-subject result must beat the detection floor AND pass the state-vs-content diagnostic.

## References

- arXiv:2610.20954 (companion: arXiv:2610.20942 → skill eeg-speech-decoding-detection-floor-audit)
- Corpora: OpenNeuro ds003626, KaraOne (U Toronto), BCI Competition 2020 Track 3
- Code: github.com/blessadeik/scalp-eeg-speech-decoding (per-run records, split hashes)
- Related skills: eeg-speech-decoding-detection-floor-audit, same-brain-different-prediction, identity-trap-eeg-foundation-models
