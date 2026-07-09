---
name: from-atomic-actions-to-standard-operating-procedures-iterative-tool
description: 'Tool utilization enables Large Language Model (LLM) agents to interact with the real world and resolve complex tasks. However, existing agent frameworks predominantly rely on static toolsets composed. Based on arXiv:2607.07321.'
---

# From Atomic Actions to Standard Operating Procedures: Iterative Tool Optimization for Self-Evolving LLM Agents

**arXiv**: 2607.07321 | **Authors**: Haipeng Ding, Yuexiang Xie, Zhewei Wei, Yaliang Li, Bolin Ding | **Utility**: 0.9

## Overview

Tool utilization enables Large Language Model (LLM) agents to interact with the real world and resolve complex tasks. However, existing agent frameworks predominantly rely on static toolsets composed of granular atomic actions (e.g., basic file I/O or single-turn search), which forces agents to reinvent low-level logic for every recurring workflow, leading to increased reasoning overhead and failure rates. In this study, we propose that agents can achieve self-evolution by synthesizing these atomic actions into reusable Standard Operating Procedures (SOPs), which function as callable higher-order tools that encapsulate multi-step logic. We further introduce EvoSOP, a framework that empowers agents to extract SOPs from execution trajectories and iteratively optimize the toolset through a systematic lifecycle of construction, merging, evaluation, and pruning. Extensive experiments demonstrate that EvoSOP significantly boosts task success rates while substantially reducing the number of interaction rounds compared to baselines. Our analysis also reveals that iterative tool optimization fosters reliable and efficient tool-use patterns, providing a scalable pathway for the development of self-evolving agents.

## Key Contributions

1. Tool utilization enables Large Language Model (LLM) agents to interact with the real world and resolve complex tasks.
2. However, existing agent frameworks predominantly rely on static toolsets composed of granular atomic actions (e.g., basic file I/O or single-turn search), which forces agents to reinvent low-level logic for every recurring workflow, leading to increased reasoning overhead and failure rates.
3. In this study, we propose that agents can achieve self-evolution by synthesizing these atomic actions into reusable Standard Operating Procedures (SOPs), which function as callable higher-order tools that encapsulate multi-step logic.
4. We further introduce EvoSOP, a framework that empowers agents to extract SOPs from execution trajectories and iteratively optimize the toolset through a systematic lifecycle of construction, merging, evaluation, and pruning.

## Implementation Notes

- **Keywords**: llm, tool-use, reasoning, self-evolving
- **Categories**: cs.AI, cs.CL, cs.MA
- **Published**: 2026-07-08

## Activation Criteria

Use this skill when working on tasks involving: llm, tool-use, reasoning, self-evolving.
