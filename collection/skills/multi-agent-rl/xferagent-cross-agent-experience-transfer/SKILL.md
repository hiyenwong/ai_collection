---
name: xferagent-cross-agent-experience-transfer
description: "Cross-agent experience transfer framework for LLM agents. Uses compatibility-aware retrieval and structured adaptation to selectively reuse experiences across agents with different histories."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [Research, arXiv, Paper, multi-agent-rl]
    source: arXiv
    arxiv_id: "2610.19581"
    paper_title: "XferAgent: Cross-Agent Experience Transfer for Self-Improving LLM Agents"
---

# XferAgent: Cross-Agent Experience Transfer for Self-Improving LLM Agents

**arXiv ID:** 2610.19581  
**URL:** https://arxiv.org/abs/2610.19581  
**PDF:** https://arxiv.org/pdf/2610.19581

## Abstract

Large language model (LLM) agents can reuse experience from prior task executions to improve performance on subsequent tasks. Although existing methods enable cross-agent experience sharing, differences in agents' execution histories and task requirements make shared experiences difficult to reuse effectively. We propose XferAgent, a framework for cross-agent experience transfer that enables LLM agents to selectively reuse and adapt experiences from other agents. XferAgent introduces a compatibility-aware retrieval mechanism that identifies transferable experiences based on task similarity and agent capability alignment, followed by a structured adaptation process that adjusts retrieved experiences to the target agent's context. Experiments across diverse agent benchmarks show that XferAgent consistently improves task success rates compared to agents that operate without cross-agent transfer or with naive experience sharing.

## Key Contributions

- See paper for detailed methodology and results
- Category: multi-agent-rl

## Links

- [Abstract](https://arxiv.org/abs/2610.19581)
- [PDF](https://arxiv.org/pdf/2610.19581)
- [HTML](https://arxiv.org/html/2610.19581)
