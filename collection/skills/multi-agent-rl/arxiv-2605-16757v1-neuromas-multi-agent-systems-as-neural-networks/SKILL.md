---
name: arxiv-2605-16757v1-neuromas-multi-agent-systems-as-neural-networks
description: "NeuroMAS: Treats multi-agent language systems as trainable neural-network-like architectures with LLM agents as nodes and textual signals as edges"
tags: [arxiv, multi-agent-rl, neural-architecture, llm-agents, trainable-mas, progressive-growth]
arxiv_id: "2605.16757v1"
utility: 0.90
date_added: "2026-10-05"
---

# NeuroMAS: Multi-Agent Systems as Neural Networks with Joint Reinforcement Learning

**arXiv:** 2605.16757v1 | **Utility:** 0.90 | **Date:** 2026-10-05

## Abstract

NeuroMAS treats a multi-agent language system as a trainable and scalable neural-network-like architecture. LLM agents serve as nodes connected by text-carrying edges. Nodes are role-free but structure-aware: topology determines information flow, while RL training determines how nodes communicate, specialize, and coordinate.

## Key Contributions

- **Architecture-as-MAS paradigm**: Shifts design from workflow engineering to architecture design (depth, width, connectivity, growth)
- **Role-free nodes**: No hand-designed roles (planner, critic, verifier); specialization emerges from training
- **Progressive growth**: Larger systems grown from smaller trained systems, preserving learned behavior
- **Theoretical efficiency**: Modular textual computation is more parameter-efficient when tasks admit hierarchical decompositions
- **Consistent gains**: Outperforms prompt-only collaboration, single-model training, and recent trained MAS baselines

## Methods

1. **Node architecture**: Each LLM agent receives task input + upstream messages, generates textual outputs for downstream
2. **Structure-aware**: Node knows position and message format, but NOT functional role
3. **Joint RL training**: All nodes optimized together using final task reward
4. **Progressive scaling**: Start small, train, then expand while preserving learned communication patterns

## Relevance

Fundamentally reframes how we think about multi-agent systems — not as hand-crafted workflows but as trainable architectures. The progressive growth finding (larger systems only trainable when grown from smaller ones) mirrors biological development and suggests practical training strategies. Directly applicable to building better multi-agent LLM systems.
