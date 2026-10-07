---
name: confidence-ordering-reversal-contextual-priors
category: ai_collection
description: "神经解码中contextual prior融合后置信度排序反转: 深排位误差获得更大margin, 需分离读取local/prior分数."
tags: [neural-decoding, brain-computer-interface, confidence-estimation, shallow-fusion, MEG, selective-prediction]
---

# Confidence-Ordering Reversal under Contextual Priors in Neural Decoding

**Paper**: Confidence-Ordering Reversal under Contextual Priors in Neural Decoding (arXiv: 2610.08229, 6 Oct 2026)
**Authors**: Xinyu Zhang, Sichao Liu (KTH Royal Institute of Technology)
**Data**: MEG-MASC (27 participants, English) + MOUS (96 participants, Dutch)

## Core Finding

When a contextual prior (LM or accumulated evidence) is fused into neural decoding scores, confidence read from the **fused top-two margin** exhibits a **confidence-ordering reversal**: among initially-incorrect predictions, larger margins predict *repairs* (fusion fixes the error) when the correct candidate starts near the top of the local ranking, but predict *residual errors* when it starts lower.

**Key numbers (MEG-MASC)**:
- Pooled correctness AUROC 0.87 looks healthy — but repair-separation AUROC falls from **0.70 @ ranks 2–3** to **0.39 @ ranks 21–50** (below chance!)
- Errors starting beyond rank 20 (inside the reversed region) = **46.6% of all post-fusion errors**
- Replication on MOUS: 0.62 → 0.41 across the same rank groups

## The Margin-Formation Account (score-level mechanism)

Under additive shallow fusion `s̃ⱼ = sⱼ + απⱼ` (α = fusion weight):
- A **repair** must first close the correct candidate's initial deficit G⁰ₜ, so its final margin is **bounded**: `m(s̃ₜ) ≤ α·Δπₜ − G⁰ₜ` — the bigger the deficit it had to close, the smaller its remaining lead
- A **residual error** can build a large margin **between two incorrect candidates** — the prior adds `α·(π_winner − π_runner-up)` regardless of correctness. At deep ranks the correct candidate is runner-up in only 2.1% of residual errors (vs 75.2% at ranks 2–3), so the margin mostly compares two wrong candidates that can separate freely
- The prior "can widen the gap between wrong candidates as easily as it lifts the right one"

**Predictive consequence**: raising α extends positive ordering to deeper ranks. Verified by causal intervention (only α varies, score streams fixed): history-aggregation reach R₉₀ grows 3.0 → 9.3 and positive ordering extends from none → ranks 11–20, monotone in 1000/1000 participant-bootstrap resamples.

## Three Killer Implications

1. **Accuracy-weight decoupling**: under a word-level LM prior (Qwen3-4B-Base), positive ordering **keeps expanding after accuracy gain peaks** — a fusion weight chosen for accuracy does not settle confidence. Accuracy and confidence ordering are two different responses to the same prior.
2. **Recalibration cannot fix it**: any strictly increasing recalibration of the fused margin preserves ordering; entropy, score-mass-gap, and concentration summaries all reverse too. The information is **lost in fusion**, not mis-scaled.
3. **Read scores separately**: the **prior's own margin** (read before fusion) separates repairs from residual errors at AUROC 0.937 at ranks 21–50 (vs 0.392 for fused margin); stays above 0.7 in all 32 sweep cells.

## Solution: Retained-Score Confidence Estimators

Confidence estimation should retain **local + prior + fused** score streams, not just fused summaries:
- **Full estimator** (15 features: 2 local + 6 fused + 7 prior-state features, MLP): correctness AUROC **0.954** vs 0.872 for fused margin
- Selective output at matched 92% coverage: emission rises **56.7% (fused margin) → 66.6% (fused features) → 72.5% (+local) → 74.5% (full)** with mean set size 5.2
- In the deep-rank error region (ranks 21–50): validation-selected emission 32.5% → 38.2% and coverage 36.4% → 50.8% by adding prior features
- Among the 10% of deep errors scored highest by a prior-state estimator, repair rate is 8.40% vs 1.80% for decoder scores vs 1.05% base rate — prior features **find the repairable errors** the fused margin reverses on

## Priors Studied (design-space coverage)

| Prior | History source | Granularity | Update form |
|-------|---------------|-------------|-------------|
| History-aggregation | accumulated local scores (η=0.1 EMA over buckets) | sentence buckets (top-4 retained) | additive fusion (α=2.7) |
| LM sentence-level (Qwen3-4B-Base) | teacher-forced / free-running | sentence mean log-likelihood | additive fusion |
| LM word-level | teacher-forced / free-running | aligned word log-prob | additive fusion (α=0.05–16) |
| Hard bucket pruning | history-aggregation state | 4 buckets retained, rest discarded | non-additive (pruning) |

All priors share one property: candidates mapping to the same entry receive the same prior score, so the prior acts **between** entries while local scores act **within** — fusion cannot reorder within-bucket candidates.

## Evaluation Protocol (reusable)

1. Define outcomes on initially-incorrect windows: **repair** (fused = correct) vs **residual error** (fused ≠ correct); among initially-correct: **regression**
2. Group by correct candidate's **initial local rank** (2–3, 4–5, 6–10, 11–20, 21–50, 51–100)
3. **Repair-separation AUROC**: does confidence z rank a random repair above a random residual error? >0.5 positive ordering, <0.5 negative (reversed)
4. **Effective correction reach R₉₀**: 90th percentile of initial ranks among repairs — summarizes where correction operates, independent of confidence scores
5. Causal α-sweep: recompute predictions/labels at each weight with **both score streams frozen** — isolates prior contribution
6. Report **reversal boundary** (deepest positively-ordered group) alongside accuracy gain — two-axis prior evaluation

## Reuse Triggers

- Building BCI decoders with LM/context fusion (speech decoding, spellers, cursor control) — confidence gates user review, and reversed confidence sends unflagged errors to the user
- Any shallow-fusion ASR/translation system where confidence drives selective prediction, human review routing, or conformal sets
- Evaluating contextual assistance: correctness alone can't show whether remaining errors are identifiable; judge priors by **how well retained scores reveal correction outcomes**
- Source-attribution analysis: identifying what context changed precedes judging whether the change succeeded
- ASR literature parallel: shallow fusion improves recognition while degrading confidence (Kannan et al. 2018) — same additive-fusion mechanism

## Limitations (honest)

- Offline retrieval with fixed candidate pool and separate score streams; generated candidates would add pool dynamics + fused-output feedback
- Free-running history comes from local top-1, not fused predictions
- Estimators target final correctness; estimating **revision benefit** B(It) = Pr(repair|It) − Pr(regression|It) and training objectives that make successful corrections identifiable are open next steps
- Direct test pending: fixed-set assistive interfaces (BCI spellers) where revision benefit is measurable

## Related Skills

- [[brain-to-language-source-attribution]] — neural vs contextual contribution attribution
- [[eeg-based-lm-evaluation]] — LM evaluation with neural signals
- [[salience-aware-selective-decoding]] — selective decoding frameworks
- [[conformal-context-trust-decision-transformer]] — confidence-gated decision policies
