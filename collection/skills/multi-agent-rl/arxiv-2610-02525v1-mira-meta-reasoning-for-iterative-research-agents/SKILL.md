---
name: arxiv-2610-02525v1-mira-meta-reasoning-for-iterative-research-agents
description: "MIRA: Hierarchical architecture for long-horizon research agents with meta-reasoning over investigation allocation and generative actor-critic for credit assignment"
tags: [arxiv, multi-agent-rl, meta-reasoning, long-horizon, autoresearch, actor-critic]
arxiv_id: "2610.02525v1"
utility: 0.92
date_added: "2026-10-05"
---

# MIRA: Meta-reasoning for Iterative Research Agents

**arXiv:** 2610.02525v1 | **Utility:** 0.92 | **Date:** 2026-10-05

## Abstract

Long-horizon research agents must decide both how to investigate and what to investigate next as evidence accumulates. MIRA introduces a hierarchical architecture separating research allocation from execution: an outer-loop meta-reasoner curates context and writes work orders, while a fresh inner-loop executor carries out each investigation.

## Key Contributions

- **Hierarchical meta-reasoning**: Outer loop decides what/whether to investigate; inner loop executes work orders
- **Generative critic for credit assignment**: Forecasts expected remaining return from partial states at meta-reasoning boundaries
- **Cross-environment pretraining**: Improves forecasting and adaptation, yielding transferable prior for valuing partial progress
- **MIRA-AC**: Generative actor-critic jointly trained to forecast remaining return AND choose next investigation, without separate critic model
- **No policy training needed for improvements**: MIRA improves long-horizon inference even without RL training

## Methods

1. **Persistent research record**: Accumulates evidence across investigations
2. **Meta-reasoner**: Reads record, writes work order or ends episode
3. **Fresh executor**: Carries out each work order (execution = transition between meta-reasoning actions)
4. **Generative actor-critic (MIRA-AC)**: Trained on proxy hill-climbing signals, transfers across autoresearch environments

## Relevance

Directly addresses the credit assignment problem in long-horizon agentic systems. The separation of "what to do" from "how to do it" mirrors how human research teams operate. Cross-environment value pretraining is a practical technique for building better research agents. Applicable to theorem proving, neural architecture search, and open-ended discovery.
