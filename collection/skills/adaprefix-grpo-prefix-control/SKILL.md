---
name: adaprefix-grpo-prefix-control
category: reinforcement-learning
tags: [rl, grpo, reasoning, curriculum, prefix-control, adaptive-difficulty]
source: arXiv:2607.07674v1
authors: Vladislav Beliaev
date: 2026-07-08
---

# AdaPrefix-GRPO: Adaptive Trace Prefix Control for Hard Reasoning Problems

Addresses GRPO stalling on hardest problems via adaptive difficulty control.

## Problem

GRPO stalls on a model's hardest problems: when no rollout in a group succeeds, group-relative advantages vanish and the problem contributes no gradient. Hard frontier examples are wasted.

## Solution

Prepend a correct prefix of a reference solution to raise the success rate, making prefix length a continuous knob on difficulty. The key insight: **adjust prefix length to hold success rate near 50%**, where GRPO's gradient signal is largest.

## Implementation Steps

1. For each hard problem, obtain a reference solution (or partial solution)
2. During training, prepend a correct prefix of the reference to the model's input
3. **Feedback controller**: dynamically adjust prefix length to maintain ~50% success rate
4. Mask the prefix tokens in the loss so the model is only graded on its own generations
5. Gradually withdraw assistance (reduce prefix) as the model improves
6. Deploy the model without any prefix

## Key Results

- More than doubles GRPO accuracy on held-out hard math problems (2.1x for 0.6B model)
- 1.6x gain on Qwen3-1.7B, 1.7x on AIME
- Roughly halves trace length
- Smaller models see larger gains
- Implemented as data prep + loss mask; trainer is otherwise stock GRPO

## Pitfalls

- Requires reference solutions for hard problems (may not always be available)
- Controller tuning: 50% target may need adjustment per task difficulty
- Must ensure the model actually learns the skill, not just memorizes prefixes

## Verification

- Monitor per-problem success rate trajectory during training
- Verify held-out accuracy gains at matched training FLOPs
- Check that deployed model (no prefix) achieves gains
