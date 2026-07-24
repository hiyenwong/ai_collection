---
name: adaflash-adaptive-speculative-decoding
version: 1.0.0
description: Adaptive Speculative Decoding via On-Policy Distilled Diffusion Drafters
trigger_words:
  - adaflash
  - adaptive speculative decoding
  - diffusion drafters
  - on-policy distillation
arxiv_id: 2607.19223
---

# AdaFlash: Adaptive Speculative Decoding via On-Policy Distilled Diffusion Drafters

## Overview
AdaFlash is a framework for accelerating large language model inference through adaptive speculative decoding using diffusion drafters. It addresses the high variance issues in diffusion drafters by combining on-policy distillation with adaptive length selection.

## Key Components

### 1. On-Policy Distillation (OPD) for Diffusion Drafters
- Uses reverse-KL divergence tailored specifically for diffusion drafters
- Provides stable convergence and reduces domain-level variance
- Brings consistent acceptance rates across different domains

### 2. Adaptive Length Head
- Dynamically adjusts candidate sequence length during inference
- Substantially lowers verification cost of the target model
- Handles token-level variance effectively

## Implementation Steps

1. **Setup Diffusion Drafter**: Implement or adapt a diffusion-based drafter model that can generate draft sequences in parallel
2. **Apply OPD Training**: Train the drafter using on-policy distillation with reverse-KL divergence
3. **Add Adaptive Length Head**: Implement a mechanism to predict optimal draft length based on context
4. **Integrate with Target Model**: Combine the adaptive drafter with your target LLM for speculative decoding
5. **Tune Hyperparameters**: Adjust temperature, length prediction thresholds, and verification parameters

## Benefits
- Up to 66% higher throughput compared to previous state-of-the-art methods
- Consistent performance across different domains
- Especially effective in high-concurrency scenarios
- Reduces both domain-level and token-level variance

## Use Cases
- LLM inference acceleration in production systems
- High-throughput text generation services
- Real-time conversational AI applications
- Batch processing of large text corpora

## References
- Paper: [AdaFlash: Adaptive Speculative Decoding via On-Policy Distilled Diffusion Drafters](https://arxiv.org/abs/2607.19223)
- Related work: DFlash, speculative decoding, on-policy distillation