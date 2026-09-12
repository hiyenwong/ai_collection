---
name: orchestration-traces-llm-mas
description: 'Research paper: Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces.'
metadata:
  openclaw:
    emoji: "🎼"
    tags: ["research", "arxiv", "multi-agent-rl", "orchestration", "llm", "credit-assignment"]
---

# Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces

**arXiv ID:** 2605.02801
**Published:** 2026-05-04
**Authors:** Chenchen Zhang
**Categories:** cs.CL
**Utility Score:** 0.97

## Abstract

As large language model (LLM) agents evolve from isolated tool users into coordinated teams, reinforcement learning (RL) must optimize not only individual actions but also how work is spawned, delegated, communicated, aggregated, and stopped.
This paper studies RL for LLM-based multi-agent systems through orchestration traces: temporal interaction graphs whose events include sub-agent spawning, delegation, communication, tool use, return, aggregation, and stopping decisions. Using this lens, we identify three technical axes.
First, reward design spans eight families, including orchestration rewards for parallelism speedup, split correctness, and aggregation quality. Second, reward and credit signals attach to eight credit- or signal-bearing units from token to team; explicit counterfactual message-level credit remains especially sparse in our curated pool.
Third, orchestration learning decomposes into five sub-decisions: when to spawn, whom to delegate to, how to communicate, how to aggregate, and when to stop. In our curated pool as of May 4, 2026, we found no explicit RL training method for the stopping decision.
We connect academic methods to public industrial evidence from Kimi Agent Swarm, OpenAI Codex, and Anthropic Claude Code. The resulting scale gap is a gap between publicly reported deployment envelopes and open academic evaluation regimes, not independent verification of industrial training traces.
We release the artifact at this https URL , including an 84-entry tagged paper pool, a 32-record exclusion log, scripted corpus statistics, and a minimal JSON schema for replayable orchestration traces.

## Key Contributions

1. **Orchestration Traces Framework**: Introduced orchestration traces as temporal interaction graphs to study RL for LLM-based multi-agent systems
2. **Eight Reward Families**: Identified reward design spans eight families including orchestration rewards for parallelism speedup, split correctness, and aggregation quality
3. **Eight Credit-Bearing Units**: Defined how reward and credit signals attach to eight credit- or signal-bearing units from token to team level
4. **Five Sub-decisions**: Decomposed orchestration learning into five sub-decisions: when to spawn, whom to delegate to, how to communicate, how to aggregate, and when to stop
5. **Industrial Connection**: Connected academic methods to public industrial evidence from Kimi Agent Swarm, OpenAI Codex, and Anthropic Claude Code

## Relevance to AI Systems

- **Orchestration Focus**: Provides a unified framework for understanding how AI teams coordinate through orchestration traces
- **Credit Assignment**: Addresses the critical challenge of credit assignment in multi-agent LLM systems
- **Practical Artifacts**: Includes an 84-entry tagged paper pool, 32-record exclusion log, scripted corpus statistics, and minimal JSON schema for replayable orchestration traces
- **Industrial Relevance**: Bridges academic methods with real-world deployments from Kimi Agent Swarm, OpenAI Codex, and Anthropic Claude Code

## Technical Keywords

orchestration traces, multi-agent reinforcement learning, credit assignment, reward design, LLM agents, multi-agent systems, Kimi Agent Swarm, OpenAI Codex, Claude Code

## URL

https://arxiv.org/abs/2605.02801

---

**Tracked:** 2026-05-30
**Source:** arXiv Paper Tracker