---
name: betamem-learning-to-remember-a-changing
description: "BetaMem: Learning to Remember a Changing World for..."
tags: [cs.AI]
source: arxiv
arxiv_id: 2610.26554v1
utility: 1.0
published: 2026-10-19
---

# BetaMem: Learning to Remember a Changing World for Embodied Agents

**Authors:** Mai Liu, He Sun, Siru Zhong, Kerun Chen, Hao Yan...
**Published:** 2026-10-19
**arXiv:** [2610.26554v1](https://arxiv.org/abs/2610.26554v1)
**Categories:** cs.AI
**Utility Score:** 1.0

## Abstract

Long-horizon embodied agents face temporal confusion and incomplete or distorted records, recurring errors from fixed memory rules, and growing storage and retrieval costs. We present BetaMem, a framework for building and evolving traceable long-term memory through six linked layers: working, spatial, entity, episodic, experiential, and procedural memory. A dual-level write contract constrains operation executability and source support for content: supervised fine-tuning learns compliant memory operations, while reinforcement learning combines repeated sampling with teacher verification of the original observations to reward complete, accurate records and penalize omissions, distortion, and unsupported content. We formulate failure-driven policy recursive self-improvement through diagnosis along the causal sequence of memory operations and local rule repairs gated by independent replay. Atomic tools frame storage, updates, retrieval, and forgetting as cost-utility allocation under storage and read budgets. Using the open-source Qwen3.5-9B model for memory generation, BetaMem achieves overall scores of 48.08% on M3-Bench-robot, 92.08% on LoCoMo, 72.6% on OpenEQA EM-EQA, and 62.4% on EgoLifeQA, the highest among the listed memory methods under their respective evaluation protocols. Training the model for memory generation raises the contract pass rate from 50.9% to 86.2% while reducing output tokens per stored action by 47.3%. A separate Qwen3-VL-8B-Instruct evaluation on EMem-

## Key Contributions

- Novel research in cs.AI
- Published 2026-10-19

## Activation

betamem, learning, remember, changing, world, embodied, agents
