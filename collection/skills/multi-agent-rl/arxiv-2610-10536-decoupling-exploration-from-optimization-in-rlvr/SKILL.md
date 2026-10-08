---
name: arxiv-2610-10536-decoupling-exploration-from-optimization-in-rlvr
description: 'Decoupling Exploration from Optimization in RLVR (arXiv: 2610.10536)'
metadata:
  {
    "arxiv_id": "2610.10536",
    "utility": 1.0,
    "title": "Decoupling Exploration from Optimization in RLVR",
    "authors": "Saif Punjwani, Micah Goldblum",
    "url": "https://arxiv.org/abs/2610.10536v1",
    "categories": ["cs.LG", "cs.AI", "cs.CL"],
    "published": "2026-10-07"
  }
---

# Decoupling Exploration from Optimization in RLVR

**arXiv ID:** 2610.10536
**Authors:** Saif Punjwani, Micah Goldblum
**URL:** https://arxiv.org/abs/2610.10536v1
**Utility Score:** 1.00
**Published:** 2026-10-07
**Categories:** cs.LG, cs.AI, cs.CL

## Summary

Modern language models undergo reinforcement learning with verifiable rewards (RLVR) on top of already-trained checkpoints. A key promise of RLVR is the discovery of new reasoning strategies. In principle, a model can sample novel ideas absent from its prior training data. In practice, however, augmenting RLVR with strong novelty incentives has seen limited success and can degrade model quality. Because verifiable rewards supervise only a narrow slice of the model's knowledge and behavior, such degradations are difficult to recover from. Instead, we decouple exploration from optimization in a framework we call Exploration-Distillation (ExpDis). We train one or more explorer policies with a novelty bonus in the reward, filter their trajectories for correctness and quality, and distill them into a separate student policy. The student policy is then trained without a novelty bonus. We repeat the above procedure for several rounds, alternating between exploration and optimization. This decoupling allows us to aggressively scale exploration without degrading the student policy. Across seven mathematical reasoning benchmarks and two model families, ExpDis outperforms DAPO at the same wall-clock budget. Moreover, we observe improved pass@$k$ scaling, indicating that ExpDis produces models that generate more diverse correct solutions.

## Usage

This skill was automatically generated from the arXiv paper. It can be used to reference the paper's concepts, methodologies, or findings in agent workflows.

## References

- arXiv: https://arxiv.org/abs/2610.10536v1
