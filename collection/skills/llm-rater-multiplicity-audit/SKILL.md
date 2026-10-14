---
name: llm-rater-multiplicity-audit
description: Audit LLM-as-rater pipelines for rater-driven variance, threshold drift, and decision flips.
category: ai_collection
---

# LLM Rater Multiplicity Audit (Neuroscience/Psychiatry)

**Source**: Baihan Lin (Mount Sinai/Harvard), arXiv:2610.08501, Oct 2026. Verified 2026-10-12.
**Companion**: COMPASS 2.0 psychometric RSA (arXiv:2610.06615, same author — wording covariance can masquerade as symptom structure).

## When to Use
- Any pipeline where an LLM scores/scores/classifies human subjects: depression screening (PHQ-8), symptom rating, psychiatric triage, qualitative coding, human evaluation of text
- Before deploying LLM-based assessment: AUC/ICC alone CANNOT certify it — rater choice dominates
- Benchmark papers reporting "LLM X achieves AUC Y on clinical interviews" — check the rater facets

## Core Finding (880-rater pre-registered multiverse, 189 interviews, PHQ-8)
- **Model choice explained 30.0% of score variance; stable participant differences only 10.5% (2.8×)**
- Two AUC≥0.70 raters disagreed on screening decisions for **40% of participants**; no participant got a unanimous verdict out of 880 raters
- Between-rater AUC variance was 10.6× its sampling variance
- Same-AUC models made opposite deployments: Qwen2.5-7B (AUC 0.81) flagged 24/100, missing 14 of 30 depressed; Mistral-7B (AUC 0.80) flagged 80/100, missing 1

## The Rater Facet Grid (what defines "a rater")
| Facet | Levels tested | Impact found |
|-------|---------------|--------------|
| Model | 11 open models (1B–21B) | 30.0% variance |
| Wording | instrument/clinician/evidence-only/role-play/self-report | evidence-only: −27 pp flagged |
| Text view | participant speech vs whole conversation | |
| Answer reading | expected value vs most-likely option | |
| Score format | digit sum / letter sum / direct total (A–D vs D–A order) | letter reversal: median 21 pp, up to 85 pp |
| Deployment | quantization, inference library, transcription | 4-bit+library: 21% decisions changed |

## Method: The Audit Protocol
1. **Define the defensible multiverse**: cross model × wording × view × reading rule × format → N raters, all applied to the SAME fixed interview set (never vary the data, only the rater)
2. **Variance decomposition** (generalizability theory): partition summed-score variance into person main effect vs rater facets + interactions. Report dependability Φ = person-variance share
3. **Decision-flip rate**: probability two random raters (both AUC≥0.70) give opposite screening decisions per participant. Track vs number of raters (grows: 40% at 2 raters → 94% at 10)
4. **Offset-vs-accuracy separation**: AUC measures ranking; the share flagged follows the rater's mean over-rating via normal-ogive curve (R²=0.91, stable across confirmation set). "A rater is a bathroom scale with a misplaced zero"
5. **Trivial-choice probes**: answer-letter order reversal, digits-vs-letters, evidence-only wording — if these move decisions by >5 pp, the pipeline is rater-driven
6. **Locked confirmation**: fix analysis pre-registration, apply once to a new interview set
7. **Recalibration ceiling test**: fit per-rater calibration on ~40 labels → accuracy 60%→75%, disagreement halved, but ~1-in-5 individual decisions STILL flip. Report the residual flip rate as the honest limit

## Key Metrics to Report (beyond AUC)
- Person-variance share and model/rater-variance share (the 2.8× ratio)
- Decision-disagreement rate among high-AUC raters (per participant, and distribution over severity)
- Rater offset (mean over-rating) vs flagged-share curve + its confirmation R²
- Cronbach α is a RED HERRING: median α=0.91 (very consistent) but correlated 0.02 with validity — internal consistency ≠ validity
- Calibration gain AND residual flip rate after recalibration

## Pitfalls
- **Internal consistency is not validity** — consistent raters can be consistently wrong
- **AUC cannot see location**: ranking quality says nothing about who crosses the threshold
- **Group-level claims are fragile**: 16% of raters reversed the sign of a small gender difference; 14% found "significant" differences absent from self-report
- **Specificity checks**: below-threshold PTSD symptoms and talkativeness predicted flags (partial Spearman 0.36/0.25) — scores may track distress, not the target construct
- Averaging raters is not enough: 11 models × 5 wordings × 3 formats lifted dependability only to 0.53
- Psychometric RSA (COMPASS 2.0): wording similarity alone induces covariance resembling symptom structure — verify language-derived geometry against wording geometry, not just self-report

## Reusable Pattern
```
for each rater config in multiverse:
    score all subjects -> per-rater vector
V = decompose(scores_matrix)  # person vs facets
flips = P(decision_i differs | pair of AUC>=0.70 raters)
offset_curve = fit(flagged_share ~ rater_offset)  # normal ogive
report: variance shares, flip rate, offset curve R2, alpha-vs-validity corr, calibration ceiling
```

## Cross-References
- Companion skill: `psychiatric-triage-ai-chatbots` (benchmark of frontier chatbots)
- Related: `llm-claims-data-actuarial-analysis` (LLM extraction audit), `experto-invisible-manipulation` (advisory manipulation audit)
- kg.db concepts: llm-as-rater, predictive-multiplicity, generalizability-theory, calibration, multiverse-analysis
