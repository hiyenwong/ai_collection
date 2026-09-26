---
name: opd-pre-rl-distillation
description: Use when training LLMs with RL on reasoning. Shows on-policy distillation as a preparation stage before RL beats SFT+RL, with divergence/trajectory-source selection rules.
trigger: OPD before RL, policy distillation RL preparation, pre-RL distillation, reverse KL vs forward KL distillation, Pass@k limitation, teacher trajectory distillation, RL initialization, reasoning RL warm-up
category: ai_collection
---

# OPD Starts before RL: On-Policy Distillation as RL Preparation

**Source**: arXiv:2609.28145v1 (2026-09-23) — Dong, Zhu, Xu, Xie et al. (29 authors).

## Problem

RL improves reasoning, but its performance depends on the **initial policy**. Question: does on-policy distillation (OPD) as a *preparation stage* provide benefits beyond initial accuracy?

## Core Findings

1. **OPD-initialized students reach higher final performance** after shared RL than direct RL or SFT-then-RL, and this advantage **emerges even when OPD produces little immediate accuracy gain**.
2. **Pre-RL Pass@k does not explain the benefit**: similar or higher Pass@k does not necessarily lead to better post-RL performance. Pass@k is an insufficient selector for RL initialization.
3. **Mechanism — distributional alignment**: what matters is alignment with the **teacher's full distribution beyond top-1 agreement**. This may preserve higher-quality reasoning paths while retaining alternatives that RL can refine with outcome feedback — leaving RL a richer hypothesis distribution to search over.
4. **Divergence objective selection rule** (trajectory source matters):
   - **Reverse-KL OPD** performs better *before* RL.
   - **Forward-KL OPD** overtakes it *after* RL — when distilling on *student-generated* trajectories.
   - With **teacher-generated** distillation trajectories, **reverse KL remains ahead at both stages**.
   - → Preferred distillation objective depends on (a) trajectory source and (b) what training follows.

## Practical Recipe

1. Choose teacher > student capability (e.g., large reasoning model → small).
2. Trajectory source: prefer **student-sampled** trajectories with **forward-KL** if post-RL is planned; prefer **teacher trajectories + reverse-KL** when distillation quality itself matters most (or teacher sampling is cheaper).
3. Run OPD to distributional alignment (not to accuracy plateau — watch KL to teacher, not eval acc).
4. Then run RL (outcome-reward) on the distilled checkpoint.
5. **Evaluate OPD choices by post-RL performance**, not by pre-RL benchmarks.

## Why It Matters

- Reframes OPD from "compression" to **RL initialization shaping**: distillation's real product is a better-behaved search distribution, not just a smarter model.
- Explains why SFT (teacher-forced, top-1) underperforms OPD as RL init: SFT collapses to mode, destroying alternatives RL needs.
- Connects to the entropy/exploration view of RL: OPD preserves the "good modes" RL can later exploit.

## Related Skills

- `on-policy-distillation-dlm-transformation`, `near-policy-distillation` — OPD mechanics
- `efficient-opd-distillation` — OPD efficiency variants
- `latent-on-policy-self-distillation` — self-distillation contrast
