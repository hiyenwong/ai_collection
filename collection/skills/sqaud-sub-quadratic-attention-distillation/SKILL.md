---
name: sqaud-sub-quadratic-attention-distillation
description: "SQuad: Sub-quadratic attention distillation for video."
---

# SQuad: Sub-Quadratic Attention Distillation for Efficient Video Generation

## Overview
SQuad (Sub-Quadratic Attention Distillation) is a framework that achieves O(n√n) complexity in distilled attention for Video Diffusion Transformers (DiTs), naturally balancing the efficiency vs expressivity trade-off. Instead of training from scratch, it fits a pretrained full softmax Self-Attention DiT into a more efficient SQuad-Attention through distillation.

## Key Components

### Two-Stage Distillation Process
1. **Flow-Matching Supervised Fine-Tuning (SFT)**: Initial alignment phase
2. **Distribution Matching Distillation (DMD2)**: Enhanced sampling efficiency and quality preservation

### Performance Benefits
- Matches quadratic teacher performance on VBench (83.20 vs 83.08)
- Reduces per-step per-block attention FLOPs by ~67×
- Reduces attention latency by ~11×  
- Cuts end-to-end DiT latency by 2×
- Enables video generation in only 6 Neural Functional Evaluations (NFEs) instead of 100

## Implementation Guidelines

### When to Use
- Video generation tasks with large token counts
- When quadratic attention cost dominates runtime and memory
- Need to balance efficiency and expressivity without significant quality loss

### Integration Steps
1. Start with a pretrained full softmax Self-Attention DiT
2. Implement SQuad-Attention architecture with O(n√n) complexity
3. Apply Flow-Matching SFT for initial alignment
4. Follow with DMD2 for enhanced distribution matching and sampling efficiency

## Applications
- High-resolution video generation
- Long-duration video synthesis
- Real-time video generation applications
- Resource-constrained deployment scenarios

## References
- arXiv:2608.16585
- Wan 2.2 5B text-to-video model implementation