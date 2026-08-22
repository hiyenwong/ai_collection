---
name: headcast-attention-heads-video-generation
version: 1.0.0
description: HeadCast methodology for efficient autoregressive video generation through training-free attention head classification and KV cache optimization.
author: Jinliang Shen, Lianghao Su, Zheming Li, Kang He, ZiLiang Lai et al.
license: MIT
arxiv_id: 2607.20125v1
tags:
  - video-generation
  - attention
  - efficiency
  - kv-cache
  - autoregressive
---

# HeadCast: Casting Attention Heads for Efficient Autoregressive Video Generation

## Overview
HeadCast is a training-free, plug-and-play acceleration framework for autoregressive (AR) video diffusion models that addresses the continuously growing Key-Value (KV) cache problem during inference.

## Key Components

### Attention Head Classification
After a short warm-up period, HeadCast performs one-time classification at the maximum-noise step to sort every attention head into one of four archetypes:
- **Sink Heads**: Handle attention sink phenomena
- **Dummy Heads**: Can be safely pruned or approximated
- **Spatial Heads**: Focus on spatial relationships within frames
- **Global Heads**: Preserve long-range temporal consistency

### Head-Specific Pathways
- Restructures the monolithic KV cache into head-specific pathways
- Retains Global heads to maintain temporal consistency that aggressive eviction would destroy
- Spatial pathway operates on a fixed-size grid, providing resolution-dependent savings

## Implementation Guidelines

### Integration Workflow
1. Load pre-trained AR video diffusion model
2. Perform short warm-up inference to observe head behaviors
3. Execute one-time classification at maximum-noise step
4. Restructure KV cache into head-specific pathways
5. Continue inference with optimized attention computation

### Performance Characteristics
- Acceleration improves with higher resolution (1.62x at 720P, 1.95x at 1080P)
- Maintains VBench quality comparable to full attention
- Largely eliminates inter-frame flickering
- No re-training required

## Use Cases
- High-resolution autoregressive video generation
- Streaming video synthesis
- Real-time video diffusion applications
- Memory-constrained inference scenarios

## Activation Keywords
HeadCast, video generation, attention heads, KV cache optimization, autoregressive diffusion, inference acceleration

## References
- arXiv: [2607.20125v1](https://arxiv.org/abs/2607.20125v1)
- Authors: Jinliang Shen, Lianghao Su, Zheming Li, Kang He, ZiLiang Lai et al.
- Published: July 22, 2026
- Code: https://github.com/sjlgaga/HeadCast