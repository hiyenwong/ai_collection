---
name: arxiv-2608-20256-learning-when-to-think-adaptive-reasoning-for-test
description: 'Learning When to Think: Adaptive Reasoning for Test-Time Compute Allocation (arXiv: 2608.20256)'
category: multi-agent-rl
version: "1.0"
date: 2026-08-22
---

# Learning When to Think: Adaptive Reasoning for Test-Time Compute Allocation

**Authors:** Gijs Kassenaar, Zhao Yang, Vincent François-Lavet
**arXiv:** 2608.20256
**Utility:** 1.00
**Published:** 2026-08-20T16:54:08Z
**Link:** http://arxiv.org/abs/2608.20256

## Abstract

Reasoning language models trained with reinforcement learning typically operate under a fixed token budget rather than an explicitly adaptive one, which can lead to over-computation on easy problems and insufficient computation on difficult ones. We study whether a model can learn to allocate its own reasoning effort by choosing, as the first token of its response, one of three modes: \textsc{NoThink} (answer as quickly as possible), \textsc{Short} (brief reasoning), or \textsc{Long} (extended reasoning). The choice is learned inside Group Relative Policy Optimization (GRPO) with no separate router, through a shaped reward that makes each mode worthwhile at a different response length, together with hard per-mode token caps that keep the modes distinct. On a 1.5B distilled model trained on MATH, the three modes emerge without collapsing to a single choice, and the brief modes end up more accurate than \textsc{Long}, which shows that the router sorts problems by difficulty rather than at random. Averaged over three seeds, the resulting policy stays close to the base model's accuracy on the held-out MATH500 ($0.782$ vs.\ $0.796$) while cutting the mean response length from $4{,}796$ to $2{,}811$ tokens (a $41\%$ reduction). Interestingly, it also transfers to other benchmarks without retraining, with the largest savings where problems are easier, with for instance 76\% token reduction on GSM8K and at higher accuracy than the baselines at similar response length. In short, we build a reasoning model that adaptively chooses how much to reason for each problem.

## Summary

This skill encapsulates the key contributions and methods from the arXiv paper "Learning When to Think: Adaptive Reasoning for Test-Time Compute Allocation". 
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

- arXiv:2608.20256
