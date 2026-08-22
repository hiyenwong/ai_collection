---
name: arxiv-2608-20099-reward-guided-autoregressive-graph-generation-for
description: 'Reward-Guided Autoregressive Graph Generation for Efficient Multi-Agent Communication Topology Design (arXiv: 2608.20099)'
category: multi-agent-rl
version: "1.0"
date: 2026-08-22
---

# Reward-Guided Autoregressive Graph Generation for Efficient Multi-Agent Communication Topology Design

**Authors:** Poomphob Suwannapichat, Boonyarit Changaival, Caesar Wu, Pascal Bouvry
**arXiv:** 2608.20099
**Utility:** 1.00
**Published:** 2026-08-20T14:32:01Z
**Link:** http://arxiv.org/abs/2608.20099

## Abstract

LLM-based Multi-Agent Systems (MAS) achieve strong performance on complex reasoning tasks by coordinating multiple agents, but at the cost of substantial token consumption. Recent work on automatic topology design, ARG-Designer, has reframed this problem as autoregressive graph generation. However, its training objective provides no explicit incentive for the model to generate sparse and efficient topologies. We address this limitation by introducing a Reward-Guided Autoregressive Graph Generation (RGA-Designer) inspired by Reinforcement Learning from Human Feedback (RLHF). We train a reward model that jointly captures task correctness and structural compactness, and then fine-tune the pretrained graph generator using the reward model as feedback. Our method preserves task accuracy at the level of ARG-Designer while reducing token consumption by an average of 20.5%.

## Summary

This skill encapsulates the key contributions and methods from the arXiv paper "Reward-Guided Autoregressive Graph Generation for Efficient Multi-Agent Communication Topology Design". 
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

- arXiv:2608.20099
