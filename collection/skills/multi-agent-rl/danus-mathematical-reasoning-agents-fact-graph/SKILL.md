---
name: danus-mathematical-reasoning-agents-fact-graph
description: "Orchestrating mathematical reasoning agents with fact-graph memory. Addresses scaling and orchestration challenges for LLM-based mathematical reasoning agents by coordinating parallel proof attempts using a shared fact-graph memory structure. Activation: mathematical reasoning, proof orchestration, fact-graph memory, multi-agent reasoning, parallel proof, agent coordination."
metadata:
  arxiv_id: "2607.06447"
  published: "2026-07-07"
  authors: "Jihao Liu, Guoxiong Gao, Zeming Sun, Bin Wu, Shurui Liu, Jiedong Jiang, Haocheng Ju, Leheng Chen, Ronnie Cheng, Xiping Zhang, Bin Dong"
  tags: [mathematical-reasoning, proof-orchestration, fact-graph, multi-agent, parallel-proof, agent-coordination]
---

# Danus: Orchestrating Mathematical Reasoning Agents with Fact-Graph Memory

## Overview

Recent LLM-based mathematical reasoning agents have begun to tackle research-level problems and, in several cases, have contributed to the resolution of open problems. However, scaling and orchestrating such agents effectively remains challenging, due to the difficulty of coordinating parallel proof attempts and managing accumulated mathematical knowledge. Danus introduces a fact-graph memory architecture for orchestrating mathematical reasoning agents.

## Key Innovations

### Fact-Graph Memory
- Shared memory structure representing mathematical facts and their relationships as a graph
- Enables agents to build on each other's findings across parallel proof attempts
- Prevents redundant work by tracking which facts have been established or attempted
- Graph structure captures dependencies between mathematical statements

### Multi-Agent Orchestration
- Coordinates multiple agents working on related sub-problems in parallel
- Dynamically assigns proof tasks based on the current state of the fact-graph
- Agents can contribute partial results that other agents leverage

### Scaling Mathematical Reasoning
- Addresses the combinatorial explosion of proof search space
- Leverages parallelism while maintaining coherence across agent contributions
- Bridges the gap between single-agent reasoning and multi-agent proof search

## Methodology

1. **Fact-Graph Construction**: Build a graph of mathematical facts, lemmas, and proof states
2. **Agent Specialization**: Different agents tackle different types of mathematical reasoning
3. **Orchestration Layer**: Coordinates agent task assignment based on fact-graph state
4. **Knowledge Accumulation**: Proven facts become available to all agents for future work

## Implications

- Fact-graph memory as a generalizable architecture for multi-agent reasoning beyond math
- Demonstrates that structured shared memory enables effective multi-agent proof search
- Scaling through parallelism + structured memory is a viable path for research-level reasoning
- Contributes to the emerging field of AI-assisted mathematical research

## Pitfalls

- Mathematical reasoning is a specialized domain; generalization to other domains needs validation
- Fact-graph construction and maintenance overhead may limit scalability
- Proof verification remains a bottleneck (agents may produce incorrect "facts")
- Orchestration complexity grows with the number of agents and graph size

## Activation Keywords

mathematical reasoning, proof orchestration, fact-graph memory, multi-agent reasoning, parallel proof, agent coordination, Danus, mathematical agents, research-level reasoning

## Paper Reference

arXiv:2607.06447 - "Danus: Orchestrating Mathematical Reasoning Agents with Fact-Graph Memory" (Jul 2026)
