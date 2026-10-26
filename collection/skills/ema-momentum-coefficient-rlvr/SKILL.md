---
name: ema-momentum-coefficient-rlvr
description: "When does momentum help in RL with verifiable rewards? Bandit theory: with exact gradients, increasing EMA coefficient β (before overshoot) strictly accelerates; with sampled gradients, fixed β loses gain to sampling fluctuations as η shrinks — instead grow β to keep η/(1-β) in the safe regime. Practical rule for LLM post-training: use larger β1 in AdamW. Use when tuning optimizer momentum for RLVR/GRPO or diagnosing why momentum seems useless."
category: ai_collection
trigger: momentum RL, EMA coefficient, RLVR, verifiable rewards, bandit formulation, bias-corrected momentum, learning rate coupling, eta over 1 minus beta, AdamW beta1, LLM post-training optimizer, sampling fluctuation
---

# When Does Momentum Help in RLVR? EMA Momentum Coefficient Theory

Methodology from arXiv:2610.20413 (Wang, Shan, Wang, Ye, Zhong; 2026-10-14,
cs.LG/cs.AI/math.OC/stat.ML).

## The Question

First-moment momentum is standard in LLM training, yet empirical work questioned its
usefulness in RL with verifiable rewards (RLVR). This paper settles it with a bandit
formulation of RLVR using **bias-corrected exponential moving average (EMA) momentum**, where
β controls how fast weights on past gradients decay.

## The Two Regimes (the core theory)

1. **Exact policy gradients**: increasing β (within the range that prevents overshoot)
   **strictly accelerates** optimization. Momentum is unambiguously good.

2. **Sampled gradients (the RLVR reality)**: a positive expected gain can be **obscured by
   sampling fluctuations**. Two failure modes:
   - As learning rate η decreases with **fixed β**, the expected gain vanishes **faster than
     the fluctuations** → momentum looks useless.
   - Fix: **increase β together with decreasing η so that η/(1−β) stays in the safe regime**.
     This preserves a nonvanishing gain that eventually dominates the fluctuations.

## The Practical Law

**Treat β and η as a coupled pair through the effective step η/(1−β).** When you lower the
learning rate (common in late LLM post-training), raise the momentum coefficient to keep the
effective accumulated-step scale constant. "Momentum doesn't help in RL" is an artifact of
decoupled tuning.

## Validation

- Bandit simulations quantitatively match the predictions.
- RLVR on **Qwen3-4B-Base** with SGD+EMA and AdamW: supports choosing larger coefficients in
  practical LLM post-training.
- **Qwen2.5-32B with AdamW: simply increasing β1 improves mean validation accuracy by ~2
  percentage points** over the conventional choice — at 32B scale.

## Reusable Patterns

- **Coupled-schedule rule**: any optimizer with exponential-accumulation parameters (momentum,
  gradient averaging) should be re-tuned *jointly* with η, via the effective step scale.
- **Signal-vs-fluctuation analysis**: when an optimization trick "doesn't work", check whether
  its expected gain decays faster than gradient-estimation noise under your annealing schedule.
- **Bandit formulation as RLVR laboratory**: strip RLVR to a bandit to get provable,
  simulatable statements about optimizer behavior before running full LLM RL.

## When to Use

- Tuning AdamW β1 / SGD momentum for GRPO/RLVR/PPO-style LLM post-training.
- Interpreting conflicting empirical results about momentum in RL.
- Designing learning-rate annealing schedules that don't silently kill momentum benefits.
