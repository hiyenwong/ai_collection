---
name: rm-opd-routed-onpolicy-distillation-reward-models
description: "Two-stage framework for generalist Generative Reward Models: first train domain-specialized teacher GRMs via single-domain GRPO to their ceilings, then consolidate via routed on-policy distillation with domain contribution reweighting (prevents single-domain domination) and optional criteria-context distillation. Solves reward sparsity and cross-domain interference of Mix-RL on mixed-domain preference data. Use when training multi-domain reward models."
category: ai_collection
trigger: RM-OPD, generative reward model, on-policy distillation, GRPO, reward modeling, domain specialization, cross-domain interference, reward hacking, token-level supervision, multi-domain capability integration, teacher-surpassing effect
---

# RM-OPD: On-Policy Distillation for Generative Reward Models

Methodology from arXiv:2610.20174 (Su, Pan, Fang, Wang, Ren et al.; 2026-10-14, cs.LG/cs.CL).

## The Mix-RL Bottleneck Diagnosis

Training general-purpose Generative Reward Models (GRMs) with RL on **mixed-domain preference
data** (Mix-RL) hits two compounding bottlenecks:

1. **Reward sparsity** from outcome rewards (critique-level signal only).
2. **Cross-domain interference** from jointly optimizing heterogeneous capabilities — leading
   to imbalanced capability acquisition and pervasive **reward hacking**.

## The Two-Stage Fix (specialize first, integrate second)

**Stage 1 — Specialist acquisition:** cultivate domain-specialized teacher GRMs via
**single-domain GRPO fine-tuning**, each expert reaching its performance ceiling **in
isolation** (no interference while learning).

**Stage 2 — Capability integration:** consolidate teachers into one student via
routed on-policy distillation with two safeguards:

- **Routed on-policy distillation**: dense **signed token-level supervision** on
  student-generated critiques (on-policy states, not teacher states), routed per domain.
- **Domain contribution reweighting**: reweight token guidance toward target domain shares —
  prevents whichever domain is easiest from dominating optimization.
- **Optional criteria-context distillation**: condition teachers on domain-specific evaluation
  criteria to sharpen token-level supervision.

## Results

- Across multiple RM benchmarks and two base models: consistently outperforms vanilla Mix-RL
  and strong baselines, with an emergent **"teacher-surpassing" effect** (the integrated
  student exceeds its specialist teachers).

## Reusable Patterns

- **Separate acquisition from integration**: when multi-domain joint training interferes,
  train specialists to ceilings in isolation, then integrate through distillation rather than
  continued joint RL.
- **Dense signed token supervision on student rollouts**: converts sparse outcome reward into
  per-token direction — the standard OPD trick, applied here to reward modeling.
- **Domain-share reweighting as an anti-domination guard**: whenever merging multiple teachers,
  normalize their gradient contributions to intended proportions.
- **On-policy distillation as multi-domain glue**: OPD's dense signal is what makes integration
  stable where outcome-reward RL on the union would reward-hack.

## When to Use

- Building generalist reward models spanning heterogeneous domains (math, code, safety, chat).
- Observing capability imbalance or reward hacking in mixed-domain RLHF pipelines.
- Any multi-teacher consolidation problem (routing + reweighting + per-domain criteria).
