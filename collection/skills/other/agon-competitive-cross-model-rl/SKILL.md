---
name: agon-competitive-cross-model-rl
category: reinforcement-learning
tags: [rl, grpo, reasoning, multi-agent, competitive, cross-model, implicit-grading]
source: arXiv:2607.07690v1
authors: Vladislav Beliaev
date: 2026-07-08
---

# Agon: Competitive Cross-Model RL with Implicit Rival Grading of Reasoning

Makes two competing models each other's graders for reasoning, without process labels or reward models.

## Problem

GRPO grades only the final answer. On hard problems this trains models to "write more" rather than "think better," since the reasoning trace is never graded and no process label exists.

## Solution

Two competing models act as each other's graders through competitive interaction:
1. Both attempt the same problem
2. In alternating roles, one drafts a solution and the other reads it while solving
3. Each is rewarded for **out-solving** the other
4. To win, a model must out-reason a rival that has seen its work — reasoning is judged implicitly

## Implementation Steps

1. Initialize two models of comparable strength but behavioral difference
2. **Draft phase**: Model A generates a solution trace
3. **Response phase**: Model B reads A's trace and generates its own solution
4. **Reward**: Model B wins if it solves the problem while A failed, or if both solve but B's solution is superior
5. **Alternating roles**: Swap which model drafts first across problems
6. Both models are optimized simultaneously — each faces a progressively stronger rival
7. **Inference**: Deploy as a two-stage cascade (draft → answer after reading draft)

## Key Results

- Doubles GRPO's pass@1 on hard DeepMath split with Qwen3
- ~8x the gain of an untrained Mixture-of-Agents pass over the same base
- Works across model families (Qwen3.5, Gemma 4)
- Replicates on competitive-programming code
- No process labels, no reward model needed

## Key Insights

- **Self-grading through competition**: Reasoning quality is implicitly judged by whether the rival can beat it
- **Progressive difficulty**: Each model faces a stronger rival as training progresses
- **Deployment benefit**: The trained pair can be deployed as a cascade, not just during training

## Pitfalls

- Models must be comparably strong but behaviorally different (too similar = no signal)
- Inference requires two models (cascade), increasing compute cost
- Single-model RL cannot provide the progressive rival escalation

## Verification

- Monitor per-model win rate trajectory during training
- Verify both models improve, not just one dominating
- Check cascade performance at inference vs individual model performance
