---
name: direct-on-policy-distillation
category: machine-learning
description: Direct On-Policy Distillation (Direct-OPD) for weak-to-strong generalization — transferring RL-induced policy shifts as implicit reward signals
trigger_words: direct-OPD, on-policy distillation, weak-to-strong generalization, policy distillation, RLVR, implicit reward, policy shift
arxiv_id: "2607.05394"
date: "2026-07-07"
---

# Direct On-Policy Distillation (Direct-OPD)

## Paper
**Title:** Weak-to-Strong Generalization via Direct On-Policy Distillation
**arXiv:** 2607.05394
**Date:** 2026-07-06
**Category:** cs.LG

## Core Methodology

Direct-OPD transfers the teacher's RL-induced policy shift to a stronger student model, instead of directly distilling the post-RL teacher policy.

### Key Innovation
- **Policy shift transfer:** Compares post-RL teacher with its pre-RL reference; treats their log-ratio as a dense implicit reward for the student
- **On-policy states:** Applies the policy shift signal on the stronger student's own on-policy states
- **No explicit reward model:** Avoids training a separate reward model or running sparse-reward RL on the target

### Mechanism
```
1. Run RL on smaller (weak) model → get post-RL policy π_weak^RL
2. Compute policy shift: Δ = log(π_weak^RL / π_weak^pre)
3. Apply Δ as implicit reward on strong student's on-policy states
4. Optimize strong student: maximize E[Δ · log(π_strong)]
```

## Results
- Qwen3-1.7B boosted from 48.3% to 62.4% on AIME 2024
- 4 hours on 8 A100 GPUs
- Outperforms step-matched direct RL
- Enables sequential composition of multiple policy shifts

## Reusable Patterns
- **RL outcome reuse:** RL results can be reused across model scales as implicit reward signals
- **Dense implicit rewards:** Policy differences create dense reward signals from sparse RL
- **Weak-to-strong transfer:** Smaller models can teach larger models more efficiently than direct imitation
- **Sequential composition:** Multiple policy shifts can be composed sequentially

## When to Use
- When you have a small model with good RL results but want to improve a larger model
- When RL on the target model is too expensive
- When you want to reuse RL supervision across model scales
- When building teacher-student pipelines for reasoning models
