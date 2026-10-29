---
name: groundcontrol-satellite-conditioned-multi-view-diffusion
description: "Research paper: GroundControl: Satellite-Conditioned Multi-View Diffusion for Reconstruction-Fre"
tags: [arxiv, paper, cs.CV, cs.AI, cs.LG]
arxiv_id: "2610.37545"
utility: 0.85
---

# GroundControl: Satellite-Conditioned Multi-View Diffusion for Reconstruction-Free Novel View Synthesis

**arXiv:** [2610.37545](https://arxiv.org/abs/2610.37545)
**Authors:** Akshay Krishnan, Matias Turkulainen, Jamie Wynn, Zawar Qureshi, Mohamed Sayed...
**Published:** 2026-10-27
**Categories:** cs.CV, cs.AI, cs.LG
**Utility Score:** 0.85

## Abstract

Multi-view or video diffusion models have recently emerged as state-of-the-art approaches for novel-view synthesis from sparse image collections. While they can produce high quality images, they tend to hallucinate unrealistic spatial layouts when synthesizing views outside the input views (scene extrapolation). We propose to address this challenge for outdoor scenes by using satellite images as an additional information source to condition the multi-view generative model. We introduce a new satellite-conditioned multi-view diffusion model that combines conditioning from a satellite image and street-level input images when generating novel-views. Our cross-attention based conditioning allows us to retain pretrained multi-view diffusion priors to generate seamless, realistic, novel views from a handful of source views, while also adhering to the scene layout as seen from satellite images. Our model does not use 3D scene reconstruction, and only relies on posed street and satellite views. Our experiments on outdoor datasets show that our model is better than both satellite-conditioned or street-view conditioned baselines on novel-view synthesis, especially on challenging cases where target views have very little overlap with source views. Project page: https://nianticspatial.github.io/groundcontrol

## Key Contributions

- Paper identified as high-utility (≥0.85) from arXiv scan
- Relevant to: cs.CV, cs.AI, cs.LG

## Potential Applications

- Research reference for vision generative domain
- Building block for future work in this area
