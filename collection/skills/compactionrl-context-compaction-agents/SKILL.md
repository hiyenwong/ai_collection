---
name: compactionrl-context-compaction-agents
category: ai_collection
description: "CompactionRL methodology for training long-horizon agentic LLMs with context compaction. Jointly optimizes task execution and summary generation with token-level loss normalization and cross-trajectory GAE."
tags: [context-compaction, long-horizon-agents, agentic-rl, context-window, trajectory-compaction, SWE-bench, terminal-bench]
---

# CompactionRL: RL with Context Compaction for Long-Horizon Agents

## Core Problem

Long-horizon agentic LLMs are limited by finite context windows — extended interaction trajectories exceed maximum context length before task completion. Context compaction (summarizing previous states) offers a natural solution but incorporating it into RL remains underexplored.

## Methodology

**CompactionRL** jointly optimizes:
1. Task execution policy (standard RL objective)
2. Summary generation (what to compress and how)
3. Token-level loss normalization (handles variable-length trajectories)
4. Cross-trajectory generalized advantage estimation (GAE across compacted trajectories)

This enables LLM agents to learn from compacted long-horizon trajectories.

## Results

- GLM-4.5-Air (106B-A30B): 66.8% Pass@1 on SWE-bench Verified (+7.0), 24.5% on Terminal-Bench 2.0 (+3.1)
- GLM-4.7-Flash (30B-A3B): 56.0% SWE-bench (+5.5), 20.2% Terminal-Bench (+6.8)
- Deployed in RL pipeline for GLM-5.2 (750B-A40B)

## When to Use

- Training coding agents that need to handle long multi-file trajectories
- When context windows are a bottleneck for agentic RL training
- When you need to compress and learn from long interaction histories
- SWE-bench, Terminal-Bench, and similar long-horizon coding benchmarks

## Pitfalls

- Token-level loss normalization is critical — naive averaging over variable-length trajectories fails
- Cross-trajectory GAE must account for compaction-induced information loss
- Summary quality directly impacts downstream task performance

## Reference

arXiv:2607.05378 - "CompactionRL: Reinforcement Learning with Context Compaction for Long-Horizon Agents" (Li et al., 2026)

## Activation

CompactionRL, context compaction, long-horizon agents, agentic RL, context window, trajectory compaction, SWE-bench, terminal bench, agent context management
