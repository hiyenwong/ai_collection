---
name: matched-context-grpo
description: 'Matched-Context Group Policy Optimization for LLM agent training with sparse terminal feedback. Use when training long-horizon agents needing credit assignment from outcome-only rewards.'
arxiv_id: '2610.13755'
utility: 0.88
authors: Chenxu Zhang, Yaorui Shi, Wenlong Zhang, Jianchao Tan, Zihan Wang
categories: [cs.LG, cs.AI]
tags: [reinforcement-learning, grpo, credit-assignment, llm-agents, long-horizon]
---

# Matched-Context Group Policy Optimization (MCGPO)

## Key Innovation

Training long-horizon language model agents requires assigning credit to intermediate decisions from sparse terminal feedback. MCGPO defines comparison contexts with pre-action state windows and constructs weighted action preferences from already-collected trajectories.

## Method

- Constructs comparison contexts using pre-action state windows
- Builds weighted action preferences from sibling rollouts
- Matches context evidence for both action alternatives
- Controls how evidence enters the learning signal

## Results

- Improved credit assignment in long-horizon agent training
- Better sample efficiency than standard GRPO
- More stable training dynamics with sparse rewards

## Practical Use

- Training LLM agents on tasks with only outcome-level feedback
- Improving credit assignment in multi-step reasoning
- Enhancing sample efficiency in agent RL training

## URL

https://arxiv.org/abs/2610.13755
