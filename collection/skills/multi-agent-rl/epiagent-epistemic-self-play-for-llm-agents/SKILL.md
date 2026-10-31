---
name: epiagent-epistemic-self-play-for-llm-agents
description: "EpiAgent: Epistemic Self-Play for LLM Agents..."
tags: [cs.AI, cs.CL, cs.MA]
source: arxiv
arxiv_id: 2610.40227v1
utility: 0.99
published: 2026-10-29
---

# EpiAgent: Epistemic Self-Play for LLM Agents

**Authors:** Xuanfa Jin, Xinyu Cui, Zhijian Ma, Xue Yan, Jian Zhao...
**Published:** 2026-10-29
**arXiv:** [2610.40227v1](https://arxiv.org/abs/2610.40227v1)
**Categories:** cs.AI, cs.CL, cs.MA
**Utility Score:** 0.99

## Abstract

Epistemic game theory explains an agent's strategic behavior via the beliefs it holds about others and how these beliefs are updated as the interactions unfold. Modern LLM-based agents, however, often lack an explicit mechanism for learning and updating such beliefs to guide decisions under incomplete information. To bridge this gap, we propose EpiAgent, a framework that equips LLM-based agents with an explicit, learnable epistemic layer, which maintains beliefs over others' private information and combines these beliefs with the agent's available information into an epistemic state for action selection. Concretely, the agent's policy is decomposed into two coupled stages: Epistemic Update, which updates these beliefs from interaction histories, and Action Planning, which selects actions conditioned on the updated epistemic state. By formulating their dependency as a bi-level optimization problem, we introduce Epistemic Self-Play, an algorithm that alternately optimizes the two stages through self-play, utilizing an intrinsic prediction reward to evaluate how well inferred beliefs predict subsequent observations. Empirical results across both mixed and competitive scenarios show that EpiAgent consistently outperforms prompting-based and RL-based baselines. Further analyses reveal the benefits of dedicated epistemic training, improvements in belief inference accuracy, and the contribution of learned beliefs to action planning. These results demonstrate the value of an explicit

## Key Contributions

- Novel research in cs.AI, cs.CL
- Published 2026-10-29

## Activation

epiagent, epistemic, selfplay, agents
