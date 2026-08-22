---
name: arxiv-2608-19993-optimal-skill-selection-for-llm-agents-with-provab
description: 'Optimal Skill Selection for LLM Agents with Provable Bicriteria Guarantees (arXiv: 2608.19993)'
category: multi-agent-rl
version: "1.0"
date: 2026-08-22
---

# Optimal Skill Selection for LLM Agents with Provable Bicriteria Guarantees

**Authors:** Yu Chen, Ruishuo Chen, Xun Wang, Zhuoran Li, Longbo Huang
**arXiv:** 2608.19993
**Utility:** 1.00
**Published:** 2026-08-20T13:08:17Z
**Link:** http://arxiv.org/abs/2608.19993

## Abstract

Loading reusable skill documents into a bounded context window is now the primary way large language model (LLM) agents acquire task-specific capabilities, which makes skill selection a first-order determinant of task performance and token cost. Yet current agents score skills independently by semantic relevance and assemble the set by top-$k$ or greedy packing, with no quality guarantee or cost awareness on the selected set. As a result, redundant or poorly chosen skills waste scarce context tokens and can even degrade performance. We give the first model of how the selected skill set shapes execution outcomes and cast skill selection as an optimization problem: choose a skill set under a hard token budget to maximize a monotone submodular benefit minus context penalty. For this problem, we develop Best Prefix Selection (BPS), a polynomial-time algorithm, and prove, to our knowledge, the first performance guarantee for skill selection: a bicriteria $(1-1/e,1)$ approximation whose benefit coefficient is optimal in polynomial time. On a contamination-controlled BigCodeBench variant, BPS outperforms all the baselines, reaching $0.73$ measured task success versus $0.20$--$0.52$ for released skill routers, text retrievers, and the executor's own selection, on $28\%$ fewer tokens than the strongest released router.

## Summary

This skill encapsulates the key contributions and methods from the arXiv paper "Optimal Skill Selection for LLM Agents with Provable Bicriteria Guarantees". 
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

- arXiv:2608.19993
