---
name: hierarchical-world-models-with-implicit-dynamics
description: "Hierarchical World Models with Implicit Dynamics..."
tags: [cs.RO, cs.AI]
source: arxiv
arxiv_id: 2610.42146v1
utility: 0.91
published: 2026-10-30
---

# Hierarchical World Models with Implicit Dynamics

**Authors:** Gaoyue Zhou, Yvonne Wu, Zichen Jeff Cui, Nicolas Ballas, Mido Assran...
**Published:** 2026-10-30
**arXiv:** [2610.42146v1](https://arxiv.org/abs/2610.42146v1)
**Categories:** cs.RO, cs.AI
**Utility Score:** 0.91

## Abstract

Planning with world models enables test-time adaptation for embodied agents, offering superior generalization over direct policy learning. However, long-horizon tasks remain hindered by cumulative errors and search complexity. Existing hierarchical methods often use rigid macro-actions or latent skills, leading to brittle representations and limited fine-grained control. We introduce ID-WM (Implicit Dynamics World Models), a hierarchical world model that decouples state-space reachability from local control. Our framework utilizes a high-level model to sample feasible transitions across the state manifold and a low-level world model as an inverse dynamics solver to ground these transitions into precise actions. This allows the planner to identify reachable subgoals without being constrained by low-level execution details. By prioritizing local physical feasibility over global behavioral patterns, ID-WM synthesizes novel long-horizon plans from short segments, transcending the specific behavioral modes seen during training. We demonstrate its effectiveness across three navigation and manipulation suites, achieving a 38.5% improvement over state-of-the-art policy and diffusion-based planners. Crucially, by leveraging this hierarchical structure to mitigate compounding errors, our approach yields a 135% performance gain over single-level world model MPC, particularly in complex, unseen configurations for long-horizon tasks. Videos can be viewed at https://id-wm.github.io

## Key Contributions

- Novel research in cs.RO, cs.AI
- Published 2026-10-30

## Activation

hierarchical, world, models, implicit, dynamics
