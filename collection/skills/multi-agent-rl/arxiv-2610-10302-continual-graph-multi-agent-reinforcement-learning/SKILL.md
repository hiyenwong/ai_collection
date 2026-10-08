---
name: arxiv-2610-10302-continual-graph-multi-agent-reinforcement-learning
description: 'Continual Graph Multi-Agent Reinforcement Learning (arXiv: 2610.10302)'
metadata:
  {
    "arxiv_id": "2610.10302",
    "utility": 0.86,
    "title": "Continual Graph Multi-Agent Reinforcement Learning",
    "authors": "Tommaso Marzi, Ahmed Hendawy, Jan Peters, Carlo D'Eramo, Andrea Cini...",
    "url": "https://arxiv.org/abs/2610.10302v1",
    "categories": ["cs.LG"],
    "published": "2026-10-07"
  }
---

# Continual Graph Multi-Agent Reinforcement Learning

**arXiv ID:** 2610.10302
**Authors:** Tommaso Marzi, Ahmed Hendawy, Jan Peters, Carlo D'Eramo, Andrea Cini...
**URL:** https://arxiv.org/abs/2610.10302v1
**Utility Score:** 0.86
**Published:** 2026-10-07
**Categories:** cs.LG

## Summary

In Continual Multi-Agent Reinforcement Learning (CMARL), agents learn cooperative policies across sequences of tasks, aiming to adapt effectively to new tasks while preserving the ability to solve previously encountered ones. In many applications, tasks differ in their underlying structure, which can represent, for example, distinct operational conditions or target configurations (e.g., different network topologies in power grids or arrangements in formation control). Existing CMARL methods lack dedicated mechanisms to leverage this structural information when learning new tasks, failing to promote transfer and mitigate forgetting. To fill this gap, we propose Continual Graph Multi-Agent Reinforcement Learning (CGMARL), a novel framework for CMARL problems in which task sequences are mapped into a series of attributed graphs, each modeling a task-specific structure. In CGMARL, each graph determines the environment dynamics (next states and/or rewards) and the number of agents for the corresponding task. Then, we present Graph-based Formation (GRAFO), the first CGMARL benchmark, and show how forgetting arises in this setting. Finally, to address this limitation, we propose Frozen Graph Encoder (FROG), a method that relies on a frozen graph backbone to preserve past structural information in graph-based CMARL policies. Experiments on GRAFO show that pairing FROG with existing CL methods substantially improves performance on multiple CGMARL scenarios.

## Usage

This skill was automatically generated from the arXiv paper. It can be used to reference the paper's concepts, methodologies, or findings in agent workflows.

## References

- arXiv: https://arxiv.org/abs/2610.10302v1
