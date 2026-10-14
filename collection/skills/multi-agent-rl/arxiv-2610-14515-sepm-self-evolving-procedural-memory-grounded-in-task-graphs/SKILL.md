---
name: arxiv-2610-14515-sepm-self-evolving-procedural-memory-grounded-in-task-graphs
description: 'SEPM: Self-Evolving Procedural Memory Grounded in Task Graphs for Multi-Agent Co (arXiv: 2610.14515)'
metadata:
  {
    "arxiv_id": "2610.14515",
    "utility": 1.0,
    "title": "SEPM: Self-Evolving Procedural Memory Grounded in Task Graphs for Multi-Agent Collaboration",
    "authors": "",
    "url": "https://arxiv.org/abs/2610.14515"
  }
---

# SEPM: Self-Evolving Procedural Memory Grounded in Task Graphs for Multi-Agent Collaboration

**arXiv ID:** 2610.14515
**URL:** https://arxiv.org/abs/2610.14515
**Utility Score:** 1.00

## Abstract

Long-horizon multi-agent collaboration requires memory that preserves both successful actions and the coordination structure underlying them. Existing memory systems support information sharing or procedural reuse, but often leave the evolution of shared procedures disconnected from the task dependencies and execution states of collaborating agents. This coupling also limits the direct transfer of procedural memory designed for individual agents to team settings. We propose Self-Evolving Procedural Memory (SEPM), a framework that uses task dependency graphs as a common representation for online coordination and procedural memory evolution. During execution, a lightweight shared blackboard records structured evidence alongside task dependencies, supporting the detection of goal, plan, and world-state divergence and evidence-based realignment. After execution, verified actions and dependencies are distilled into reusable procedures, while recurring failures inform warnings and constraints. The shared procedure pool evolves through creation, refinement, specialization, and retirement, guided by success and cost utility and constrained by evidence and safety requirements. Together, these mechanisms preserve the collaborative structure and applicability conditions needed to reuse experience across tasks. Evaluations on ALFWorld, WebArena, and OfficeBench under AutoGen and DyLAN show that SEPM achieves the highest task scores among the compared methods in all six benchmark settings. Under AutoGen, it improves task scores over the no-added-memory baseline by 29.85, 25.86, and 13.00 percentage points, respectively. The codebase is available at this https URL.

## Key Topics

multi-agent, self-evolving, memory, coordination, ppo

## Usage

This skill references the paper's concepts, methodologies, and findings for use in agent workflows.

## References

- arXiv: https://arxiv.org/abs/2610.14515
