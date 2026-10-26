---
name: r2s-rollout-scorer-gap-repair
description: "Use when agentic on-policy distillation stalls or a per-token teacher/scorer lets the student drift. R2S diagnoses the rollout-scorer gap and repairs the teacher with takeover-informed scores before distillation, reward-free."
category: ai_collection
metadata:
  arxiv_id: "2610.28586"
---

# R2S: Rollout-to-Scorer Distillation — Repairing the Myopic Teacher

Source: arXiv:2610.28586 (Shu Zhao, Tan Yu, Oct 2026). In agentic on-policy distillation (OPD) the student trains on its own trajectories while a teacher scores every token. The standard explanation of failure is compounding error (student drifts outside the teacher's reliable region). This work shows that explanation is incomplete and proposes a scorer repair.

## The rollout-scorer gap (diagnosis)

1. From the states where the student departs most from the teacher, the **teacher's own takeovers still finish the task**, yet the student trained on the teacher's token scores keeps running out of turns.
2. Cause: **myopia of next-token scoring**. The teacher rates each token without seeing where the episode ends, so its scores let through safe, delaying moves that outcome-based RL would punish with zero reward — a penalty agentic OPD lacks.
3. Name the difference between what the teacher *does* (takeovers succeed) and what it *scores* (passes delaying moves): the **rollout-scorer gap**.

## Method (R2S)

1. **Mine high-disagreement states** from the *untrained* student (states where student and teacher diverge most).
2. **Run teacher takeovers** from those states (teacher continues the episode itself).
3. **Filter states**: keep those where enough takeovers pass a **reward-free check** — consensus across takeovers, or an LLM judge. No task reward is used anywhere.
4. **Fine-tune the teacher** to give its takeover-informed scores on every assistant token from the divergence turn onward, *without* the takeover in context (teacher must internalize where episodes end).
5. **Freeze the repaired teacher** as the sole scorer for standard OPD.

## Results

- 3 environments, 2 teachers, 4 students: R2S beats three state-of-the-art agentic-OPD methods (episode-length curricula, teacher-guided turns, prefix replay / teacher-intervention) in **all 12 teacher-student-environment cells**.
- Average **+12.8 success points** over the best baseline per cell.
- Project page: https://tree-shu-zhao.github.io/r2s/

## Reuse pattern

Whenever a **per-step scorer** (teacher, judge, reward model, process reward model) supervises a **long-horizon agent**:
- Do not assume a failed probe or bad score means the signal is absent — check whether the scorer is myopic (rates tokens/steps without outcome information).
- Repair the scorer *before* distillation/RL: mine disagreement states, run the expert's own takeovers, verify with reward-free checks (consensus, LLM judge), then fine-tune the scorer on takeover-informed targets with takeovers out of context.
- Contrast with RC-OPD (repairs the *student's* reasoning) and outcome-based RL (needs task reward): R2S repairs the *scorer*, reward-free.

Related: agentic OPD curricula and teacher-intervention methods; RC-OPD (arXiv:2610.24530-family); hindsight/privileged RLVR; process reward models with outcome calibration.
