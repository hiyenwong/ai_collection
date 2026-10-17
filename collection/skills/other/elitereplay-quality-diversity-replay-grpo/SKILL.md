---
name: elitereplay-quality-diversity-replay-grpo
description: "Preserve solution diversity in RLVR via MAP-Elites elite archive replay."
category: reinforcement-learning
---

# EliteReplay: Preserving Diverse Solutions in RL Post-Training via Quality-Diversity Search

Source: arXiv:2610.22290 (Moussa, Lee, Kumar — Ohio State, Oct 2026). Post-training recipe pairing GRPO with a quality-diversity (MAP-Elites) "elite" archive + replay loss, countering the behavior-sharpening / strategy-collapse effect of RLVR. Code: github.com/skai-research/EliteReplay

Use when: RL post-training collapses the base model's alternative correct strategies, tuning pass@k vs pass@1 tradeoffs, building replay/anchor sets for GRPO, or evaluating diversity at the strategy level (not just pass@k).

## Problem

RLVR (GRPO etc.) improves reliability (pass@1) by sharpening probability onto a few behaviors — often at the cost of reach (pass@k) and of the base model's ALTERNATIVE correct strategies. pass@k is a poor diversity proxy: a model can pass@k via one strategy. Baselines that preserve reach (MaxRL, DPH-F forward-KL, SetPO) still collapse strategy diversity.

## Method (two stages)

**Stage 1 — Offline elite archive (per-question MAP-Elites with frozen base model π₀):**
- Behavior space: approach label (induced by a separate labeler LLM from verified seed examples) + deterministic structural features (SQL: joins/subqueries; code: loops/recursion). Descriptor b(y) → archive cell.
- Loop: (1) init cells from verified seed solutions; (2) select target approach prioritizing UNREPRESENTED cells, parent elite from a different approach; (3) variation — prompt π₀ with (question, target approach, parent elite); (4) verify candidate, insert into actual-approach cell; fill empty cell or replace if shorter.
- Selection favoring untried approaches directs search toward rarely-sampled-but-correct strategies; more than doubles occupied cells vs seed sampling.

**Stage 2 — Online GRPO + replay:**
- L(θ) = (1-μ)·L_GRPO(θ) + μ·L_replay(θ), fixed μ=0.05 (small; larger μ modestly reduces pass@1)
- L_replay = -(1/|E|)Σ log πθ(y|x)/|y| — length-normalized NLL of archived solutions; batch E balanced across questions and cells
- Archive is FIXED during training; inference is direct sampling (no archive lookup)

## Results (text-to-SQL: BIRD in-dist, Spider OOD)

- pass@1 25.3% (base) → 52.5%; pass@128 74.8% BIRD (base 73.6, MaxRL 73.7, GRPO 68-69) / 93.2% Spider (baselines ≤86.9)
- U@128 (unique correct strategies): 9.1 vs MaxRL 6.2 (+50%) BIRD; 9.4 vs 5.3 (+77%) Spider
- Strategy retention: 62% BIRD / 60% Spider (baselines 34-39% / 30-37%); per-strategy coverage loss ≤9pp vs baseline's ≤28pp
- Ambiguous queries (AmbiQT Both@128): 27.0% vs 14.2% best baseline, base 37.0%
- OOD MATH-500: pass@1 35.5% vs base 28.3% while baselines DROP to 25-27% — replay acts as rehearsal mitigating OOD forgetting

## Ablation truths (important for reuse)

1. **Archive composition matters**: IID replay (same budget, uniform samples) = 7.4 U@128 vs elite 9.1 — IID overrepresents frequent approaches.
2. **Replay must CONTINUE during RL**: elite-SFT-then-GRPO (no ongoing replay) collapses back to GRPO levels (68.5% pass@128, U@128 3.0).
3. **SFT on elite archive alone**: great pass@128 (74.6/92.8) but pass@1 ≤37% — archive gives coverage, RL gives reliability; need both.
4. Metrics: U@k unbiased estimator mirrors pass@k with per-strategy counts; effective diversity = P(two random samples both correct AND structurally different); retention = |strategies kept ∩ base|/|base strategies|.

## Reuse pattern

For any RLVR pipeline where base-model diversity has downstream value (best-of-N, ambiguity coverage, ensembles, OOD robustness): (a) build per-task elite archives via MAP-Elites before training, (b) add small length-normalized replay loss on the archive throughout GRPO, (c) measure U@k + effective diversity + retention, not just pass@k. Behavior descriptors can be induced (LLM labeler + structural features) rather than hand-designed.

Related: CHORD (mixing supervised loss into on-policy RL), MAP-Elites, MaxRL/DPH-F/SetPO baselines it beats on diversity.
