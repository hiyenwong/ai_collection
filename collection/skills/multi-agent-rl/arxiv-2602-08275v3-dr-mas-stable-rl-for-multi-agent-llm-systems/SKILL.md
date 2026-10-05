---
name: arxiv-2602-08275v3-dr-mas-stable-rl-for-multi-agent-llm-systems
description: "Dr. MAS: Identifies gradient-norm inflation as root cause of instability in MAS RL, proposes agent-wise advantage normalization for stable training"
tags: [arxiv, multi-agent-rl, grpo, training-stability, gradient-dynamics, llm-training]
arxiv_id: "2602.08275v3"
utility: 0.91
date_added: "2026-10-05"
---

# Dr. MAS: Stable Reinforcement Learning for Multi-Agent LLM Systems

**arXiv:** 2602.08275v3 | **Utility:** 0.91 | **Date:** 2026-10-05

## Abstract

Directly extending GRPO with a single global advantage baseline to multi-agent LLM systems is brittle under heterogeneous agent reward statistics, leading to gradient spikes and unstable training. Dr. MAS identifies gradient-norm inflation as the root cause and proposes agent-wise advantage normalization for stable training.

## Key Contributions

- **Root cause identified**: Global advantage baseline over heterogeneous agent steps inflates per-agent gradient second moment, triggering gradient-norm spikes
- **Agent-wise normalization**: Each agent's advantages normalized using its own reward mean and variance, calibrating gradient scales
- **End-to-end framework**: Scalable orchestration, flexible per-agent LLM serving, shared GPU resource scheduling
- **Heterogeneous model support**: Natively supports multiple different LLMs over unified GPU pool
- **Empirical gains**: +5.6% avg@16 and +4.6% pass@16 on math; +15.2% avg@16 and +13.1% pass@16 on search, while eliminating gradient spikes

## Methods

1. **Theoretical analysis**: Shows vanilla GRPO's global baseline mismatches heterogeneous agents' reward distributions
2. **Agent-wise baselines**: Replace global normalization with per-agent statistics
3. **Lifecycle-aware management**: Dynamic dispatch releases inactive models' GPU memory
4. **Tested on Qwen2.5 and Qwen3**: Under both LLM-sharing and non-sharing settings

## Relevance

Companion paper to AT-GRPO — while AT-GRPO designs the algorithm, Dr. MAS explains WHY vanilla approaches fail and how to fix it. The gradient-norm inflation diagnosis is a general insight applicable beyond MAS. The heterogeneous model support is practically important for real deployments where different roles may need different model sizes.
