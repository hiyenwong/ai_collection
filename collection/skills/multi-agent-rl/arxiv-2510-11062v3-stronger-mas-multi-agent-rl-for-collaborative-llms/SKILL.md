---
name: arxiv-2510-11062v3-stronger-mas-multi-agent-rl-for-collaborative-llms
description: "AT-GRPO: Agent- and Turn-wise grouped RL for multi-agent LLM systems, boosting planning accuracy from 14-47% to 96-99.5%"
tags: [arxiv, multi-agent-rl, grpo, llm-training, multi-agent-systems, reinforcement-learning]
arxiv_id: "2510.11062v3"
utility: 0.93
date_added: "2026-10-05"
---

# Stronger-MAS: Multi-Agent Reinforcement Learning for Collaborative LLMs (AT-GRPO)

**arXiv:** 2510.11062v3 | **Utility:** 0.93 | **Date:** 2026-10-05

## Abstract

Standard GRPO grouping assumptions fail in multi-agent systems because prompts differ by role and turn. AT-GRPO introduces Agent- and Turn-wise grouped RL tailored for MAS, with a training system supporting both single-policy and multi-policy on-policy updates. Across game, planning, coding, and math tasks, it demonstrates substantial gains.

## Key Contributions

- **AT-GRPO algorithm**: Agent- and Turn-wise grouped optimization that correctly handles heterogeneous reward distributions across roles
- **MAS training system**: Supports diverse MAS workflow rollouts and on-policy RL updates for multiple policies
- **Planning breakthrough**: Boosts accuracy from 14.0-47.0% (single-agent RL baseline) to 96.0-99.5% on long-horizon planning
- **Reasoning gains**: +3.87-7.62% on coding, +9.0-17.93% on math benchmarks
- **Tested on Qwen3 models**: 1.7B and 8B parameter scales

## Methods

1. **Agent-wise grouping**: Each agent's outputs grouped separately for advantage computation
2. **Turn-wise grouping**: Within each agent, turns grouped for relative comparison
3. **Multi-policy support**: Can train role-specific or shared policies
4. **Scalable orchestration**: Handles diverse MAS workflows (voting, orchestration, etc.)

## Relevance

First principled extension of GRPO to multi-agent LLM systems. Solves the fundamental mismatch between single-agent RL assumptions and multi-agent reality. The planning results (96-99.5%) are remarkable — suggests single-agent RL fundamentally cannot handle long-horizon coordination. Practical for anyone training multi-agent LLM systems.
