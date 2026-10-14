---
name: arxiv-2610-14883-marl-battlegrounds-a-novel-jax-native-benchmark-for-heteroge
description: 'MARL-BattleGrounds: A Novel JAX-native Benchmark for Heterogeneous and Competiti (arXiv: 2610.14883)'
metadata:
  {
    "arxiv_id": "2610.14883",
    "utility": 0.96,
    "title": "MARL-BattleGrounds: A Novel JAX-native Benchmark for Heterogeneous and Competitive Multi-agent RL",
    "authors": "",
    "url": "https://arxiv.org/abs/2610.14883"
  }
---

# MARL-BattleGrounds: A Novel JAX-native Benchmark for Heterogeneous and Competitive Multi-agent RL

**arXiv ID:** 2610.14883
**URL:** https://arxiv.org/abs/2610.14883
**Utility Score:** 0.96

## Abstract

We present MARL-BattleGrounds (MARL-BGs), an easy-to-use JAX-native benchmark for heterogeneous and competitive multi-agent reinforcement learning (MARL), designed to be sample-efficient, computationally efficient, and researcher-centric. MARL benchmarks are typically simple and efficient, like SMAX, where winning reduces to unit micromanagement, or rich and costly, like Dota 2. MARL-BGs fills this missing middle. Its first mode, Team Deathmatch, is a simultaneous turn-based game between two teams of five heterogeneous agents. The five classes have distinct basic, passive, and ultimate abilities designed to synergize with allies and counter enemies. Our 52 hand-designed maps with diverse obstacles include a 12-map curriculum and ten held-out validation and test maps. MARL-BGs provides two canonical evaluation modes. First, eight endgame scenarios form a hard generalization challenge: each asks a team to win an unseen, nearly lost position against a strong reactive controller within 5-10 ticks. Second, a monthly round-robin tournament retrains each submission on equal compute, plays it against every member of the current &#34;Big Nine&#34; field, and publishes the Elo results on the official leaderboard. All entrants are publicly released as downloadable opponents. MARL-BGs records 11,192 metrics per game in 28 topics. We also include three strong scripted opponents, an analytical replay viewer, and off-the-shelf tools for self-play, cross-play, curriculum learning, and zero-shot coordination evaluation. We even provide an API for LLM-based agents and use it to evaluate Qwen3.5-9B against our strongest policy. In our BattleClient, humans can play alongside or against any mix of policies, enabling human-AI evaluation. We benchmark MARL-BGs with six additional deep MARL baselines, which we release. On one RTX 5090 with 1,024 parallel games, the simulator runs 50,000 5v5 game steps per second.

## Key Topics

multi-agent, reinforcement learning, benchmark, efficient

## Usage

This skill references the paper's concepts, methodologies, and findings for use in agent workflows.

## References

- arXiv: https://arxiv.org/abs/2610.14883
