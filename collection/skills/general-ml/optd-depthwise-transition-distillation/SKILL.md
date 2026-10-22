---
name: optd-depthwise-transition-distillation
description: "Use when on-policy distillation plateaus below the teacher. OPTD adds alignment of teacher-student layer-to-layer log-probability increments (depthwise prediction transitions) on student rollouts, recovering ~90% of the capability gap."
category: ai_collection
metadata:
  arxiv_id: "2610.28048"
---

# On-Policy Transition Distillation (OPTD)

Source: arXiv:2610.28048 (You, Li, Yu, Li — HKUST, Oct 2026). Standard OPD consolidates expert capabilities by matching teacher and student **final-layer distributions** on student-generated rollouts. OPTD investigates whether **depthwise prediction transitions** — the changes in predictions *between* layers — provide additional task-relevant supervision.

## Diagnostic finding

- Stronger teacher–student agreement in **intermediate transitions** is associated with higher answer correctness within questions.
- Correct responses exhibit **lower mean transition KL** across all measured intermediate layer pairs.
- Motivation: final-layer matching leaves the intermediate computation path unconstrained; aligning per-layer *increments* transfers how predictions evolve through depth, not just where they end.

## Method

1. Roll out the student on-policy (as in OPD).
2. Loss = final-layer distribution matching (standard OPD) **+** alignment of teacher and student **layer-to-layer log-probability increments** Δ log p between adjacent layers.
3. No change to rollout collection or architecture — purely an auxiliary supervision term on intermediate depth transitions.

## Results

- 3 backbones, 8 benchmarks spanning mathematics, coding, instruction following.
- Best or tied-best overall performance in both dual- and three-domain distillation.
- Three-domain setting: OPTD recovers **≈90% of the teacher–student capability gap vs ≈75% for plain OPD**.

## Reuse pattern

- When distilling same-tokenizer teacher→student with OPD, log the **mean transition KL per layer pair** as a health metric first: if correct answers show lower transition KL, intermediate alignment has headroom.
- Supervise **differences between adjacent layers** (increments), not raw intermediate logits — increments are the actual computation steps and transfer across residual streams.
- Combine with final-layer matching; do not replace it.
- Distinct from X-Token (cross-tokenizer alignment) and latent/hidden-state OPD variants: OPTD stays in log-prob space and needs no feature projector.

Related: on-policy distillation (OPD), GKD, X-Token cross-tokenizer distillation, LastOPD latent alignment, intermediate-layer feature distillation.
