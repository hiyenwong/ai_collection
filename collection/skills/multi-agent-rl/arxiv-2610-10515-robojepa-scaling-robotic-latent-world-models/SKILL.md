---
name: arxiv-2610-10515-robojepa-scaling-robotic-latent-world-models
description: 'RoboJEPA: Scaling Robotic Latent World Models (arXiv: 2610.10515)'
metadata:
  {
    "arxiv_id": "2610.10515",
    "utility": 0.95,
    "title": "RoboJEPA: Scaling Robotic Latent World Models",
    "authors": "Artem Zholus, Nicolas Beltran-Velez, Jianhao Yuan, Sarath Chandar, Tushar Nagarajan...",
    "url": "https://arxiv.org/abs/2610.10515v1",
    "categories": ["cs.AI", "cs.RO"],
    "published": "2026-10-07"
  }
---

# RoboJEPA: Scaling Robotic Latent World Models

**arXiv ID:** 2610.10515
**Authors:** Artem Zholus, Nicolas Beltran-Velez, Jianhao Yuan, Sarath Chandar, Tushar Nagarajan...
**URL:** https://arxiv.org/abs/2610.10515v1
**Utility Score:** 0.95
**Published:** 2026-10-07
**Categories:** cs.AI, cs.RO

## Summary

Latent world models have shown a remarkable ability to predict future states and to plan in the real world. In practice, however, we lack a principled way to estimate how their capabilities scale with model size, data, and compute, an open problem that slows progress in the field. In this work we present RoboJEPA, a world model based on the Joint Embedding Predictive Architecture (JEPA) and trained on a large-scale dataset spanning 12 robotic embodiments. We show that RoboJEPA's imagination error, the error of its latent rollouts, follows a second-order power law in compute, allowing us to predict model quality well beyond the scale at which the law is fit. We further show that downstream robotic planning performance improves predictably with compute, and that imagination error is strongly correlated with it, making it a reliable proxy for real-robot evaluation. Finally, we demonstrate that latent world models can be deployed zero-shot as robotic agents, planning toward a single goal image to solve tasks requiring long-horizon planning on real hardware. We release all model checkpoints together with our training and robot deployment code. To our knowledge, this is the first work to establish scaling laws for multi-embodiment robotic world models trained on real robot data, and RoboJEPA, at 8B parameters, is the largest JEPA predictor model trained to date.

## Usage

This skill was automatically generated from the arXiv paper. It can be used to reference the paper's concepts, methodologies, or findings in agent workflows.

## References

- arXiv: https://arxiv.org/abs/2610.10515v1
