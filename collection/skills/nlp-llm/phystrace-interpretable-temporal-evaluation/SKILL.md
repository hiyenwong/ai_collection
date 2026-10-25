---
title: "PhysTrace: Interpretable Temporal Evaluation of Physical Consistency in Video Generative Models"
authors: "Taekoan Yoo, Wonkyung Jung, Kyunghun Kim, Kyeongbo Kong"
published: "2026-10-22"
arxiv_id: "2610.31429v1"
url: "https://arxiv.org/abs/2610.31429v1"
categories: ["cs.AI", "cs.RO"]
utility_score: 0.87
tags: [arxiv, paper, nlp-llm]
---

# PhysTrace: Interpretable Temporal Evaluation of Physical Consistency in Video Generative Models

**Authors:** Taekoan Yoo, Wonkyung Jung, Kyunghun Kim, Kyeongbo Kong
**Published:** 2026-10-22
**arXiv:** [2610.31429v1](https://arxiv.org/abs/2610.31429v1)
**Categories:** cs.AI, cs.RO
**Utility Score:** 0.87

## Abstract

World action models increasingly rely on pretrained video models assumed to capture physical dynamics for prediction, planning, and action generation. Existing evaluations assess plausibility, probe representations, or measure predictive surprise, but rarely identify which history-conditioned physical expectations conflict with observations. We introduce PhysTrace, a training-free framework aligning MLLM-generated, history-conditioned expectations with observed video windows to temporally localize physical violations and provide interpretable descriptions without task-specific probes or classifiers. We also introduce IntPhys2-Timing, adding violation intervals to IntPhys2. PhysTrace achieves a Hit Rate of up to 70.7% across physical principles on IntPhys2-Timing and outperforms the compared methods in overall possible-impossible discrimination accuracy on IntPhys2. Applied to reconstructed videos along the trajectories of pretrained diffusion/flow-based video models, PhysTrace reveals attribute- and noise-dependent patterns in physical violation localization, enabling interpretable physical consistency analysis across timesteps.

## Key Contributions

- Research paper from arXiv, auto-processed by Hermes cron job
- Utility score >= 0.85 indicates high relevance for AI/ML research
- Category: nlp-llm

## Related Skills

Check the `nlp-llm` directory for related papers and tools.
