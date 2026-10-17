---
name: vaspo-value-augmented-self-distillation
description: "Value-Augmented Self-Distillation Policy Optimization: integrate privileged self-teacher signal into PPO via positional-dynamics analysis — critic value-prediction is strongest near response end while teacher guidance is strong initially, dips mid-generation, rebounds finally. Self-teacher and critic evaluate identical privileged information at student prefixes; critic gives token-level PPO advantages, teacher modulates positive advantages via bounded probability ratios. Use for LLM reasoning RL with on-policy distillation."
category: ai_collection
trigger: VASPO, self-distillation, privileged value estimation, PPO advantage, on-policy distillation, reasoning RL, GRPO, token-level advantage, teacher-student integration, positional dynamics
---

# VASPO: Value-Augmented Self-Distillation Policy Optimization

Methodology from arXiv:2610.20516 (Wu, Zhang, Zhang, Du; 2026-10-14, cs.CL/cs.AI/cs.LG).
Code: https://github.com/cii030/VASPO

## The Positional-Dynamics Diagnosis (reusable insight)

On-policy self-distillation gives dense supervision via a privileged self-teacher, but that
supervision reflects **local token preferences**, not the **expected return of an unguided
student continuation**. Recent methods bolt the teacher onto GRPO (GRPO for update direction,
teacher for signal scaling). VASPO instead integrates within PPO, guided by measured positional
dynamics along the response:

- **Privileged information helps the critic's value prediction most toward the response's end**
  (return uncertainty concentrates there).
- **Self-teacher guidance is strong initially, drops mid-generation, and rebounds at the end.**

These complementary profiles tell you *where* each signal should dominate — a rule applicable
to any dense-vs-sparse supervision combination.

## The Method

1. Self-teacher and critic **evaluate identical privileged information** at
   **student-generated prefixes** (not teacher rollouts) — both signals are computed on-policy
   at the same states.
2. The **critic computes token-level PPO advantages** from predicted continuation returns.
3. The **self-teacher modulates selected positive advantages via bounded probability ratios**
   — teacher only re-weights advantages that PPO already endorses, capped to prevent the
   teacher from overriding value-based direction.

## Results

- Six mathematical reasoning benchmarks: **+2.59pt mean over PPO (Qwen3-4B)**,
  **+1.81pt (OLMo3-7B variants)**; highest mean accuracy among evaluated methods on
  Knights and Knaves.

## Reusable Patterns

- **Signal-position analysis before fusion**: before combining two learning signals, profile
  each along the trajectory (here: response position) and assign dominance by region.
- **Privileged-information parity**: when mixing a privileged teacher with a learned critic,
  feed both the same privileged view at the same (student) states so their disagreement is
  attributable, not an artifact of different inputs.
- **Bounded modulation, not replacement**: use the secondary signal to re-weight within the
  primary algorithm's endorsement set (positive advantages only, ratio-capped) — avoids
  teacher drift destabilizing value-based learning.

## When to Use

- Training reasoning LLMs with both a privileged teacher signal and RL (PPO-style).
- Deciding how to combine dense token-level distillation with sparse outcome rewards.
- Diagnosing why naive teacher+GRPO stacking underperforms.
