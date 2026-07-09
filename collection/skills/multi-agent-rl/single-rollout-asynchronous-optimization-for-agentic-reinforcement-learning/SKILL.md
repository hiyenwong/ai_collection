---
name: single-rollout-asynchronous-optimization-for-agentic-reinforcement-learning
description: 'Reinforcement learning (RL) is becoming increasingly important for post-training large language models (LLMs). Previous RL pipelines for LLMs were mostly synchronous and batch-interleaved, which is in. Based on arXiv:2607.07508.'
---

# Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning

**arXiv**: 2607.07508 | **Authors**: Zhenyu Hou, Yujiang Li, Jie Tang, Yuxiao Dong | **Utility**: 0.9

## Overview

Reinforcement learning (RL) is becoming increasingly important for post-training large language models (LLMs). Previous RL pipelines for LLMs were mostly synchronous and batch-interleaved, which is inefficient for long-horizon agentic tasks. Recently, asynchronous RL has emerged as a more efficient alternative by updating the model as rollouts arrive. However, existing asynchronous RL systems often emphasize throughput, while leaving training stability and task effectiveness largely underexplored. For example, a key challenge is that group-wise sampling in the widely-used GRPO framework does not naturally fit asynchronous agentic training. In this paper, we present Single-rollout Asynchronous Optimization (SAO) to address the stability and off-policy challenges in asynchronous RL. To reduce off-policy effects and improve generalization, we replace group-wise sampling with single-rollout sampling, that is, using one rollout per prompt. We further improve this single-rollout strategy with practical value-model training designs. To improve optimization stability, we introduce a strict double-side token-level clipping strategy. SAO is able to train stably for one thousand steps and consistently outperform GRPO and its variants on agentic coding and reasoning benchmarks, such as SWE-Bench Verified, BeyondAIME, and IMOAnswerBench. We also demonstrate that single-rollout RL is particularly effective in a simulated online learning setting, where the model must adapt to changing evolving environments. To this end, SAO is successfully deployed in the agentic RL pipeline for training the open GLM-5.2 model (750B-A40B).

## Key Contributions

1. Reinforcement learning (RL) is becoming increasingly important for post-training large language models (LLMs).
2. Previous RL pipelines for LLMs were mostly synchronous and batch-interleaved, which is inefficient for long-horizon agentic tasks.
3. Recently, asynchronous RL has emerged as a more efficient alternative by updating the model as rollouts arrive.
4. However, existing asynchronous RL systems often emphasize throughput, while leaving training stability and task effectiveness largely underexplored.

## Implementation Notes

- **Keywords**: agentic, reinforcement-learning, llm, ecg
- **Categories**: cs.LG, cs.AI
- **Published**: 2026-07-08

## Activation Criteria

Use this skill when working on tasks involving: agentic, reinforcement-learning, llm, ecg.
