---
name: geostate-learning-view-decoupled-geometry-states
description: "GeoState: Learning View-Decoupled Geometry States for 3D World Modeling"
tags: [arxiv, paper, multi-agent-rl]
arxiv_id: "2610.22343"
utility: 0.86
date: "2026-10-17"
---

# GeoState: Learning View-Decoupled Geometry States for 3D World Modeling

**arXiv:** [2610.22343](https://arxiv.org/abs/2610.22343)
**Authors:** Hongchang Liu, Jian Liu, Yujuan Ding, Liang Peng, Xun Jiang...
**Published:** 2026-10-15
**Categories:** cs.CV, cs.AI, cs.LG, cs.RO
**Utility Score:** 0.86

## Abstract

Recent 3D world models increasingly use features from geometry foundation models (GFMs) as predictive world states, benefiting from their rich geometric priors. However, the view dependence of these features entangles scene dynamics with camera-induced variation, making the resulting state evolution harder to predict. We propose GeoState, a view-decoupled geometry representation for predictive 3D world modeling that separates scene-state evolution from camera-dependent observation. Specifically, a scene tokenizer aggregates multi-view GFM features into a view-decoupled scene state, which a geometry decoder queries using camera rays. An autoregressive world model then predicts future scene states, while camera motion is modeled separately. The predicted states can therefore be decoded under either predicted or externally specified cameras, while retaining a single context-derived scale throughout the rollout without per-frame scale alignment. Experiments show that GeoState outperforms prior 3D world models on Waymo, supports geometrically consistent cross-view querying, and generalizes zero-shot to KITTI and nuScenes. Project page: https://hongchang-liu.github.io/GeoState-project-page/

## Key Contributions

- Novel research in cs.CV, cs.AI
- High utility score (0.86) indicating significant research value

## Activation

geostate, learning, viewdecoupled, geometry, states, world, modeling

## Notes

Added by arXiv cron job on 2026-10-17.
