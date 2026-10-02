---
name: arxiv-2609-38662-collabflow-recursive-self-improvement-of-agent-col
description: 'CollabFlow: Recursive Self-Improvement of Agent Collaboration (arXiv: 2609.38662)'
metadata:
  {
    "arxiv_id": "2609.38662",
    "utility": 0.87,
    "title": "CollabFlow: Recursive Self-Improvement of Agent Collaboration",
    "authors": "Xiao Huang, Mingda Zhang, Junming Zhang, Qiang Huang, Hanwen Zhang, Yue Dai, Zijia Wang, Xiaoying Tang",
    "url": "https://arxiv.org/abs/2609.38662"
  }
---

# CollabFlow: Recursive Self-Improvement of Agent Collaboration

**arXiv ID:** 2609.38662
**Authors:** Xiao Huang, Mingda Zhang, Junming Zhang, Qiang Huang, Hanwen Zhang, Yue Dai, Zijia Wang, Xiaoying Tang
**URL:** https://arxiv.org/abs/2609.38662
**Utility Score:** 0.87

## Abstract

Recursive self-improvement (RSI) lets a system improve from its own outcomes; in LLM-based multi-agent systems, Agents refine one another within a task, and outcomes improve how they collaborate across tasks. However, existing multi-agent collaboration leaves this loop open: collaboration is pre-defined at the operator level, topology-only learning keeps verbatim exchange that propagates errors, and reward maximization on a system's own outcomes concentrates on a few teams. To address these challenges, we propose CollabFlow, an RSI system of Learned Agent Collaboration: a trainable Collab-Director constructs teams of complete Agents, a frozen executor runs them, and each round's outcomes retrain the director. Within each round, the edges of a collaboration graph carry protocols of Evidence-Conditioned Communication: a receiver adopts a differing answer only when the sender's evidence is stronger by a margin, so the director learns who communicates and how. Across rounds, we further propose Collaborative Trajectory Balance (CTB), a flow-based objective that credits each team once across its construction orders and targets a reward-proportional distribution over teams, so several good teams stay in play. We also bound how far this self-generated target moves between rounds, which shrinks as records accumulate. On twelve datasets, CollabFlow outperforms all baselines and keeps improving across rounds. Code is available at https://anonymous.4open.science/r/CollabFlow-631E.

## Usage

This skill references the paper's concepts and can be used in agent workflows for:
- Understanding the paper's methodology
- Referencing key findings
- Building on the research

## References

- arXiv: https://arxiv.org/abs/2609.38662
