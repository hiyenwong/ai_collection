---
name: taskframe-connecting-task-level-planning-with-frame-level-co
description: "TaskFrame: Connecting Task-Level Planning with Frame-Le..."
tags: [cs.CV, cs.AI]
source: arxiv
arxiv_id: 2610.40276v1
utility: 1.0
---

# TaskFrame: Connecting Task-Level Planning with Frame-Level Control for Game Agents

**arXiv ID:** [2610.40276v1](https://arxiv.org/abs/2610.40276v1)
**Published:** 2026-10-29
**Authors:** Guangzhi Wang, Junfu Pu, Yiran Wang, Xingyilang Yin, Honghao Chen...
**Utility Score:** 1.0

## Abstract

Building general game agents requires both high-level task reasoning and low-latency action control in rapidly changing visual environments. These capabilities favor models with substantially different computational profiles, making them difficult to realize within a single model. In this work, we present TaskFrame, a hierarchical planner-controller framework that connects task-level planning with frame-level keyboard-and-mouse control. A vision-language task planner decomposes a high-level goal into an ordered sequence of atomic instructions and is optimized through supervised learning and dependency-aware GRPO. The hidden states of special goal tokens that terminate each atomic instruction provide continuous goal embeddings that are cached and reused across control steps. A causal Transformer controller combines the embedding of the active goal with recent observations to predict discrete keyboard and mouse-button actions and continuous camera motion at every game step. We train the system in three stages: planner training, controller pretraining, and joint alignment. Experiments in Minecraft show that TaskFrame is competitive with general-purpose vision-language models on instruction decomposition, and that in closed-loop evaluation the agent achieves a higher combat success rate than the evaluated baselines.

## Key Contributions

- Research in multi-agent-rl domain with practical applications
- Published in top arXiv categories: cs.CV, cs.AI

## Activation

cs.CV, cs.AI, arxiv paper, utility 1.0
