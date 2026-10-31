---
name: continuous-action-world-models-learning-cross-embodiment-spatiotemporal
description: "Continuous-Action World Models: Learning Cross-Emb..."
tags: [cs.RO, cs.CV, cs.LG]
source: arxiv
arxiv_id: 2610.40401v1
utility: 0.93
published: 2026-10-29
---

# Continuous-Action World Models: Learning Cross-Embodiment Spatiotemporal Dynamics Priors

**Authors:** Liangyu Li, Qingwen Liu
**Published:** 2026-10-29
**arXiv:** [2610.40401v1](https://arxiv.org/abs/2610.40401v1)
**Categories:** cs.RO, cs.CV, cs.LG
**Utility Score:** 0.93

## Abstract

We introduce Continuous-Action World Models (CoAWM), a framework for learning cross-embodiment spatiotemporal dynamics priors that support robot action generation across embodiments and execution frequencies. At its core is a shared latent function space that captures the spatial and temporal structure of robot actions. We learn this space through two stages. First, function pretraining brings trajectories from different embodiments and sampling frequencies into a common representation, learning shared dynamics priors through action reconstruction and consistency across temporal sampling views. By accommodating heterogeneous robot trajectories, this stage broadens the range of data sources available for pretraining and facilitates scaling to larger and more diverse datasets. Second, we connect the pretrained function space to a world-model backbone, enabling observations, language instructions, and the current robot state to condition the prediction of a latent action function. A single decoder takes any query time and returns the corresponding end-effector action. By separating shared dynamics priors from task-conditioned action selection and temporal sampling, our approach provides a unified foundation for transferring robot experience across embodiments and control frequencies.

## Key Contributions

- Novel research in cs.RO, cs.CV
- Published 2026-10-29

## Activation

continuousaction, world, models, learning, crossembodiment, spatiotemporal, dynamics, priors
