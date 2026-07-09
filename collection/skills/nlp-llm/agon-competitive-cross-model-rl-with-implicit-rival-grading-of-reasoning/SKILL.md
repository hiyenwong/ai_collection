---
name: agon-competitive-cross-model-rl-with-implicit-rival-grading-of-reasoning
description: 'Reinforcement learning from verifiable rewards (e.g. GRPO) is the engine behind todays reasoning models, yet it grades only the final answer. On hard problems this trains models to write more rather. Based on arXiv:2607.07690.'
---

# Agon: Competitive Cross-Model RL with Implicit Rival Grading of Reasoning

**arXiv**: 2607.07690 | **Authors**: Vladislav Beliaev | **Utility**: 0.86

## Overview

Reinforcement learning from verifiable rewards (e.g. GRPO) is the engine behind today's reasoning models, yet it grades only the final answer. On hard problems this trains models to write more rather than to think better, since the trace itself is never graded and no label for good thinking exists. We introduce Agon, which makes two competing models each other's graders. Both attempt the same problem; in alternating roles, one drafts a solution and the other reads it while solving, and each is rewarded for out-solving the other. To win, a model must out-reason a rival that has seen its work, so reasoning is judged implicitly during training, with no process labels and no reward model. Because both models are optimized, each faces a progressively stronger rival, which single-model RL cannot provide. The two need only be comparably strong and behaviorally different. At inference the pair deploys as it trains, a two-stage cascade in which one model drafts and the other answers after reading the draft. On the hard split of DeepMath with Qwen3, this doubles GRPO's pass@1, roughly eight times the gain of an untrained Mixture-of-Agents pass over the same base. The ordering replicates on competitive-programming code and across model families (Qwen3.5, Gemma 4). For now the models talk in text; the next step is to let them reason together in latent space.

## Key Contributions

1. Reinforcement learning from verifiable rewards (e.g.
2. GRPO) is the engine behind today's reasoning models, yet it grades only the final answer.
3. On hard problems this trains models to write more rather than to think better, since the trace itself is never graded and no label for good thinking exists.
4. We introduce Agon, which makes two competing models each other's graders.

## Implementation Notes

- **Keywords**: reinforcement-learning, grpo, reasoning
- **Categories**: cs.LG, cs.AI, cs.CL
- **Published**: 2026-07-08

## Activation Criteria

Use this skill when working on tasks involving: reinforcement-learning, grpo, reasoning.
