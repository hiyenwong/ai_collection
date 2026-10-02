---
name: arxiv-2609-38482-panda-a-decentralized-architecture-with-flexible-o
description: 'PANDA: A Decentralized Architecture with Flexible Orchestration for Scalable, Fault-Tolerant Multi-Agent Systems (arXiv: 2609.38482)'
metadata:
  {
    "arxiv_id": "2609.38482",
    "utility": 0.92,
    "title": "PANDA: A Decentralized Architecture with Flexible Orchestration for Scalable, Fault-Tolerant Multi-Agent Systems",
    "authors": "Matthew D. Laws, Cristina Nita-Rotaru",
    "url": "https://arxiv.org/abs/2609.38482"
  }
---

# PANDA: A Decentralized Architecture with Flexible Orchestration for Scalable, Fault-Tolerant Multi-Agent Systems

**arXiv ID:** 2609.38482
**Authors:** Matthew D. Laws, Cristina Nita-Rotaru
**URL:** https://arxiv.org/abs/2609.38482
**Utility Score:** 0.92

## Abstract

Existing architectures for LLM-based multi-agent systems (MAS) cannot reliably and efficiently solve multi-step tasks at scale: they struggle to support large numbers of agents and concurrent tasks, tolerate failures, govern agent interactions, and accommodate the diverse planning and execution patterns different tasks require. We present PANDA, a decentralized architecture that connects a large collective of heterogeneous, independently administered agents, letting them discover each other's capabilities and self-organize into small specialized teams per task. PANDA scales by decoupling collective communication from team communication, allowing agents to participate in multiple teams simultaneously, load-balancing tasks across the collective, and scheduling concurrent work within each agent. PANDA further separates the underlying architecture from the orchestration strategy, supporting three planning and execution patterns (star, chain, and mesh) that can be selected according to the structure and requirements of each task. PANDA detects infrastructure and orchestration failures and recovers affected tasks by dynamically replanning around failed components. Finally, to provide governance without a centralized service that would limit scalability, PANDA uses a web-of-trust model to constrain agent interactions to established trust relationships. We evaluate PANDA on the HotPotQA benchmark, demonstrating that it scales to thousands of agents, assembles teams in milliseconds, matches state-of-the-art accuracy at up to 8x the efficiency, and sustains 100% task completion under faults where existing systems fail.

## Usage

This skill references the paper's concepts and can be used in agent workflows for:
- Understanding the paper's methodology
- Referencing key findings
- Building on the research

## References

- arXiv: https://arxiv.org/abs/2609.38482
