---
name: mmoe-diffusion-transformer-expert-design
version: 1.0.0
description: ModernMOE (MMOE) methodology for modernizing diffusion transformers with efficient expert design. Adapts routed experts, shared and lightweight experts, gate-residual routing, and attention-residual information reuse to AIGC generation.
trigger_words:
  - MMOE
  - diffusion transformer MoE
  - efficient expert design
  - AIGC foundation models
---

# MMOE: Modernizing Diffusion Transformers with Efficient Expert Design

## Overview
Modern large language models scale successfully by pairing capacity growth with efficiency, keeping per-token and deployment costs under control as capacity grows. AIGC Foundation Models (AFMs), especially diffusion-transformer backbones, have begun to adopt sparse experts, but recent efforts mostly enlarge total parameter counts and sparsity ratios without importing the efficiency mechanisms that made LLM scaling practical.

MMOE systematically adapts proven LLM efficiency designs to AFMs in a balanced way, rather than simply increasing total parameters and sparsity ratios.

## Key Components

### 1. Routed Experts
- Implement conditional computation through routing mechanisms
- Balance expert utilization across different denoising timesteps
- Ensure stable expert specialization across network depth

### 2. Shared and Lightweight Experts  
- Combine dense shared layers with sparse expert layers
- Implement lightweight expert routes for common patterns
- Reduce total parameter count while maintaining capacity

### 3. Gate-Residual Routing
- Use gating mechanisms with residual connections
- Enable smooth transitions between expert selections
- Maintain gradient flow through both gated and residual paths

### 4. Attention-Residual Information Reuse
- Reuse attention computations across expert paths
- Share key-value projections between experts when appropriate
- Reduce redundant computation in multi-head attention

## Implementation Guidelines

### Training Protocol
- Train on single eight-GPU H100 node with batch size 256 for 400k steps
- Use matched training and sampling protocols for fair comparison
- Monitor FID scores at regular checkpoints to track convergence

### Routing Analysis Metrics
- Track expert specialization stability across depth
- Measure usage of lightweight routes vs. full expert routes  
- Monitor step-to-step routing changes during denoising process

## Benefits
- Faster convergence per training step compared to dense baselines
- Better quality-cost balance among sparse variants
- Stable expert specialization with modest routing changes
- Achieves lower FID scores at every checkpoint

## Use Cases
- Diffusion transformer backbone modernization
- AIGC foundation model efficiency optimization
- Balanced scaling of generative models
- Single-machine training budget constraints

## References
- arXiv:2607.24665 [cs.CV]
- Authors: Yanhao Jia, Jiepeng Wang, Haibin Huang, Chi Zhang, Erik Cambria, Xuelong Li