---
name: trial-trajectory-relative-hindsight-distillation
description: "TRIAL for trajectory-relative hindsight distillation in RL."
---

# Trajectory-Relative Hindsight Distillation for Agentic Reinforcement Learning

## Overview
TRIAL (Trajectory-Relative Hindsight Distillation) is a framework that addresses the challenge of allocating dense hindsight supervision signals across decision turns in agentic reinforcement learning. It provides a unified turn-aligned scoring protocol that redistributes supervision while maintaining an average multiplier of one.

## Key Components
- **Outcome View Extraction**: For each decision turn, extracts the realized consequence of that decision
- **Context Evaluation**: Evaluates the same response under ordinary and hindsight-conditioned contexts
- **Signed Log-Probability Gap**: Determines direction and local strength of token-level supervision
- **Trajectory-Normalized Magnitudes**: Normalizes turn-level magnitudes jointly over the realized trajectory

## Implementation Steps
1. **Generate Rollouts**: Collect completed rollouts from the agent's interactions
2. **Extract Outcome Views**: For each decision turn in the rollout, determine the realized consequence
3. **Compute Context Evaluations**: Evaluate responses under both ordinary and hindsight-conditioned contexts
4. **Calculate Supervision Multipliers**: Use signed log-probability gaps to determine allocation multipliers
5. **Normalize Across Trajectory**: Apply joint normalization to maintain average multiplier of one
6. **Apply Token-Level Supervision**: Use the resulting multipliers for dense supervision during training

## Advantages
- **Effective Allocation**: Properly distributes dense supervision signals across turns
- **Performance Gains**: Outperforms GRPO across diverse backbone/environment combinations
- **Substantial Improvements**: Achieves significant gains beyond dense hindsight distillation alone
- **Robust Performance**: Consistently improves success rates and task scores

## Experimental Results
- **WebShop with Qwen3-1.7B**: Success rate improved from 56.4% to 75.2%, task score from 78.7% to 85.7%
- **Consistent Improvement**: Best or tied-best performance among six methods on six out of eight combinations
- **Ablation Studies**: Trajectory-relative turn allocation provides substantial gains beyond dense hindsight alone

## Use Cases
- WebShop navigation tasks
- ALFWorld environment interactions
- Agentic reinforcement learning with sparse rewards
- Multi-turn decision making with hindsight signals

## Activation Keywords
trial, trajectory-relative, hindsight distillation, agentic reinforcement learning, turn allocation, dense supervision

## References
- arXiv: [2608.07371v1](https://arxiv.org/abs/2608.07371v1)
- Original paper: "Trajectory-Relative Hindsight Distillation for Agentic Reinforcement Learning"