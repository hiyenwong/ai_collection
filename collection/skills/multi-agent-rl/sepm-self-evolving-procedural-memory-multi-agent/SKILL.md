---
name: sepm-self-evolving-procedural-memory-multi-agent
description: "Self-evolving procedural memory for multi-agent systems using task graphs. Extracts, merges, prunes, and promotes coordination patterns from execution traces."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [Research, arXiv, Paper, multi-agent-rl]
    source: arXiv
    arxiv_id: "2610.14515"
    paper_title: "SEPM: Self-Evolving Procedural Memory Grounded in Task Graphs for Multi-Agent Collaboration"
---

# SEPM: Self-Evolving Procedural Memory Grounded in Task Graphs for Multi-Agent Collaboration

**arXiv ID:** 2610.14515  
**URL:** https://arxiv.org/abs/2610.14515  
**PDF:** https://arxiv.org/pdf/2610.14515

## Abstract

Long-horizon multi-agent collaboration requires memory that preserves both successful actions and the coordination structure underlying them. Existing memory systems support information sharing or procedural reuse, but often leave the evolution of shared procedures disconnected from the task dependent structure that makes them transferable. We introduce SEPM, a framework in which procedural memory is grounded in task graphs that encode the dependency relations among subtasks. After each collaboration episode, the system extracts a procedural graph from the execution trace and stores it in a shared procedural memory. A self-evolving mechanism then refines stored procedures by merging overlapping sub-graphs, pruning low-reward branches, and promoting reusable coordination patterns. At retrieval time, agents match the current task structure against stored procedural graphs to guide planning. Experiments show that SEPM improves multi-agent collaboration performance and procedure transfer across tasks compared with baselines that lack graph-grounded procedural memory.

## Key Contributions

- See paper for detailed methodology and results
- Category: multi-agent-rl

## Links

- [Abstract](https://arxiv.org/abs/2610.14515)
- [PDF](https://arxiv.org/pdf/2610.14515)
- [HTML](https://arxiv.org/html/2610.14515)
