---
name: mempilot-orchestrating-on-demand-multimodal-memory-curation
description: "MemPilot: Orchestrating On-Demand Multimodal Memor..."
tags: [cs.CL, cs.AI, cs.LG]
source: arxiv
arxiv_id: 2610.06830v1
utility: 0.99
published: 2026-10-05
---

# MemPilot: Orchestrating On-Demand Multimodal Memory Curation for LLM Agents

**Authors:** Haozhen Zhang, Haodong Yue, Quanyu Long, Jianzhu Bao, Qingyuan Liu...
**Published:** 2026-10-05
**arXiv:** [2610.06830v1](https://arxiv.org/abs/2610.06830v1)
**Categories:** cs.CL, cs.AI, cs.LG
**Utility Score:** 0.99

## Abstract

Memory has become integral to the LLM agent ecosystem, supporting information retention and reuse across interactions. However, most existing agent memory systems construct memory in a query-agnostic manner, which can incur unnecessary preprocessing cost and discard details that later prove essential. Recent studies have begun shifting memory processing toward runtime adaptation, but typically specialize in particular operations or fixed processing schemes, leaving flexible control over performance, cost, and latency largely underexplored. To address this challenge, we present \textbf{MemPilot}, a flexible framework that orchestrates on-demand memory curation under different performance--cost--latency preferences. Specifically, we optimize a multi-step LLM policy via reinforcement learning to iteratively choose between retrieving from query-agnostic memory and delegating query-specific curation of raw multimodal history to heterogeneous LLMs and VLMs. The policy jointly controls evidence amount, curation instructions, model selection, and visual access, enabling fine-grained allocation of runtime computation. To optimize this policy under competing objectives, we adapt objective-wise advantage decoupling by separately estimating each objective's advantage before aggregation. Moreover, we introduce prefix-based marginal utility estimation for fine-grained credit assignment across multi-step rollouts. Experiments on five multimodal agent-memory benchmarks demonstrate favorable 

## Key Contributions

- Novel research in cs.CL, cs.AI
- Published 2026-10-05

## Activation

mempilot, orchestrating, ondemand, multimodal, memory, curation, agents
