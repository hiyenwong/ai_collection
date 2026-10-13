---
name: sguid-skill-bank-distillation
description: Select a compact skill bank for on-policy distillation - keep only skills that yield consistent learning signals; enables stable model-skill co-evolution loops.
category: ai_collection
trigger: skill distillation, skill bank selection, model-skill co-evolution, on-policy distillation with skills, inference-time skill retrieval, skill utility filtering, curriculum from rollouts
---

# SGUID: Selecting a Compact Skill Bank for Model-Skill Co-Evolution

Methodology from arXiv:2610.12367 (Liu et al., 2026-10-08, cs.CL): when distilling skill-conditioned
teachers into a model, **fewer than 25% of retrieved skills provide useful distillation signals**.
Blind full-bank distillation wastes compute and can destabilize training; selection is the key
mechanism for stable co-evolution.

## The Finding

- Skills = reusable procedural guidance (few-shot recipes, workflow hints) injected at inference
  or used to condition a teacher in on-policy distillation.
- Prior work retrieves skills by **semantic relevance** and distills them all.
  Individual utility is neglected: relevant ≠ useful for learning.
- In OPD setups, most retrieved skills produce no consistent advantage signal → dilute gradients,
  and naive unfiltered skill updates can **degrade** the student (observed drops on HMMT25 with
  Qwen3-4B).

## SGUID Selection Procedure

1. **Roll out with skill-conditioned teachers**: for each candidate skill s in the bank,
   collect student-side on-policy trajectories supervised by the teacher conditioned on s.
2. **Measure consistent learning signal**: retain skill s only if it yields effective signals
   *throughout* training — e.g., per-skill advantage/reward curves that stay positive or
   loss deltas that repeatedly favor s-conditioned supervision. Skills with noisy,
   negative, or flat signals are dropped.
3. **Distill the selected subset** into the model (standard OPD on the kept skills).
4. **Co-evolution round**: after distillation, curate a *new* candidate bank from the updated
   model's own rollouts (fresh failure modes), run SGUID again, distill the newly selected
   few skills. Repeat.

## Empirical Anchors

- Four models (Olmo and Qwen families): distilling **6 selected skills matches or beats
  full-bank distillation** (banks up to 11× larger) on mean avg@12 for 3/4 models —
  and for all 4 after a second round of 3 newly selected skills.
- Stability: unfiltered skill updates drop Qwen3-4B HMMT25 by 0.3 pts; SGUID raises it
  +0.5 (round 1) then +1.1 (round 2). Qwen3-8B: 64.3% → 66.3% over two rounds.
- Skill selection, not skill quantity, drives stable model-skill co-evolution.

## Reusable Patterns

1. **Utility-first retrieval**: rank/retain auxiliary guidance (skills, prompts, tools,
   demonstrations) by *measured downstream learning signal*, not embedding similarity.
2. **Consistency across training** as the retention test: a one-shot win can be luck;
   a skill must keep paying across steps/epochs to earn a slot in the context or curriculum.
3. **Co-evolution loop**: model update → new rollout bank → re-select → distill.
   This is curriculum generation from the model's own current failures — each round's bank
   is drawn from the updated model, so the loop tracks its moving frontier.
4. Compact curated banks (≤10 skills) can replace large retrieval banks for distillation,
   cutting teacher-call cost by an order of magnitude at equal or better downstream accuracy.
