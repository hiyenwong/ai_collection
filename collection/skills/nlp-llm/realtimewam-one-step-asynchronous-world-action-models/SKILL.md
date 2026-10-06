---
name: realtimewam-one-step-asynchronous-world-action-models
description: "RealtimeWAM: One-Step Asynchronous World Action Mo..."
tags: [cs.CV, cs.LG, cs.RO]
source: arxiv
arxiv_id: 2610.06617v1
utility: 0.89
published: 2026-10-05
---

# RealtimeWAM: One-Step Asynchronous World Action Models

**Authors:** Chengtao Lv, Jinyang Du, Shuyi Feng, Yang Yong, Shiqiao Gu...
**Published:** 2026-10-05
**arXiv:** [2610.06617v1](https://arxiv.org/abs/2610.06617v1)
**Categories:** cs.CV, cs.LG, cs.RO
**Utility Score:** 0.89

## Abstract

World Action Models (WAMs) incorporate visual representations from video generation backbones to guide action prediction. Recent efficient WAMs adopt Mixture-of-Transformers (MoT) architectures and compute video representations once for reuse by the action expert. However, intra-expert iteration (\ie, multi-step action denoising) and inter-expert waiting (\ie, sequential execution of the video and action experts) still limit inference efficiency. To this end, we present RealtimeWAM, an extremely efficient WAM variant with one-step action generation and asynchronous inference, addressing these two bottlenecks. To reduce intra-expert iteration, we propose Teacher-Anchored Consistency Distillation (TACD) to address a local-global error gap: low local consistency error alone does not guarantee accurate final actions. TACD supplements local consistency with explicit supervision from the frozen teacher's multi-step rollout endpoint, enabling accurate one-step action generation. Additionally, we propose Cross-Expert Wavefront Pipelining (CEWP) to eliminate unnecessary expert-level waiting. It overlaps the two experts through block-wise sharing of the video KV cache, synchronizing only immediately before the corresponding action attention consumes it. Extensive experiments across diverse benchmarks (\eg, LIBERO, LIBERO-Plus and RoboTwin) and model variants (\eg, Fast-WAM and Faster-WAM) demonstrate the superiority of RealtimeWAM. Notably, RealtimeWAM maintains near-lossless performan

## Key Contributions

- Novel research in cs.CV, cs.LG
- Published 2026-10-05

## Activation

realtimewam, onestep, asynchronous, world, action, models
