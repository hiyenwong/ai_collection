---
name: arxiv-2608-20169-task-coevolve-efficient-harness-optimization-via-a
description: 'Task-CoEvolve: Efficient Harness Optimization via Adaptive Validation Task Selection (arXiv: 2608.20169)'
category: multi-agent-rl
version: "1.0"
date: 2026-08-22
---

# Task-CoEvolve: Efficient Harness Optimization via Adaptive Validation Task Selection

**Authors:** Atsuyuki Miyai, Kiyoharu Aizawa, Toshihiko Yamasaki
**arXiv:** 2608.20169
**Utility:** 1.00
**Published:** 2026-08-20T15:24:54Z
**Link:** http://arxiv.org/abs/2608.20169

## Abstract

We present a novel approach to efficient LLM agent harness optimization through adaptive validation task selection. Harness optimization iteratively rewrites the harness code based on validation performance, enabling substantial performance gains without updating the underlying model weights. Existing approaches, however, evaluate a fixed validation set in full at every iteration, incurring substantial evaluation costs even on tasks that become less discriminative as the harness evolves. We propose $\textbf{Task-CoEvolve}$, which co-evolves the validation tasks with the harness by addressing two challenges: selecting informative tasks and estimating full-set performance from partial evaluations. Task-CoEvolve builds on the observation that tasks on which candidate harnesses disagree are more informative for distinguishing among them than tasks that are consistently solved or failed. It uses variance-weighted sampling based on past outcomes to focus evaluation on tasks near the agent's capability frontier, with the sampling distribution adapting as the harness evolves. It then estimates full-set scores from the sampled tasks by accounting for their sampling probabilities, enabling consistent comparisons across iterations despite evaluating different subsets. Experiments on online text classification and Terminal-Bench 2.1 show that Task-CoEvolve consistently outperforms fixed-subset baselines and matches the final performance of full-set search while reducing the number of evaluations during optimization by 80%. Code will be released at https://github.com/Agent4Science-UTokyo/Task-CoEvolve.

## Summary

This skill encapsulates the key contributions and methods from the arXiv paper "Task-CoEvolve: Efficient Harness Optimization via Adaptive Validation Task Selection". 
The paper presents novel ideas in multi-agent-rl that can be applied to agent systems.

## How to Use

1. Review the paper's methodology and findings.
2. Identify applicable components for your agent workflow.
3. Implement the core techniques as described in the paper.
4. Validate improvements in your specific use case.

## Pitfalls

- Ensure the paper's assumptions match your agent's environment.
- Validate implementation details before deployment.
- Consider computational complexity and resource requirements.

## References

- arXiv:2608.20169
