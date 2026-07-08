---
name: full-stack-fp4-pretraining
category: ai_collection
description: "Full-Stack FP4 pretraining framework — first complete NVFP4 LLM pretraining resolving stability bottlenecks in linear projections (LoRA-SVD), optimizers (AdamW second-moment transform, Muon Newton-Schulz), and attention (mixed-precision with forward-backward alignment)."
tags: [FP4, NVFP4, quantization, pretraining, low-bit-training, Muon-optimizer, attention-quantization]
---

# Full-Stack FP4: Stable LLM Pretraining with Quantized Projections, Optimizers, and Attention

## Core Problem

Existing NVFP4 pretraining targets only transformer linear layers, leaving optimizer states, optimizer arithmetic, and attention unexplored in 4-bit pipelines. Three modules have unique numerical failure patterns:
- Linear layers: hard quantization noise limits with dimension-propagated error amplification
- AdamW second moments: heavy-tailed non-negative values fragile to low-precision denominators
- Attention: error-prone computation paths demanding strict forward-backward quantization consistency

## Methodology (Module-wise Precision Strategies)

### Linear Projections
- LoRA-SVD lightweight decomposition suppresses quantization noise
- Breaks direct-quantization error ceiling
- Shrinks linear-only loss gap from 1.40% to 0.61%

### Optimizers
- AdamW second-moment transformation for robust NVFP4 storage
- Native NVFP4 Newton-Schulz iterations for Root (Muon) optimizer
- Fully supports both AdamW and Muon in 4-bit

### Attention
- Mixed-precision: quantizes Q/K/V and backward dS
- Guards vulnerable paths (PV, dOV^T branches) in BF16
- Unified tensor reuse sustains forward-backward alignment

## Results

- 3B/64B-token pretraining: near-BF16 performance with merely 1.47% loss gap
- First feasible stable end-to-end NVFP4 LLM pretraining
- All modules are plug-and-play

## When to Use

- Pretraining LLMs at scale where memory is a bottleneck
- When you need to quantize the entire training pipeline (not just weights)
- When using Muon optimizer and want to quantize Newton-Schulz iterations
- When attention quantization instability is blocking your low-bit training

## Pitfalls

- Naive low-bit matrix multiplication has fast error accumulation
- PV and dOV^T attention branches are extremely sensitive — must keep in BF16
- Forward-backward quantization consistency is critical for attention stability
- AdamW second moments need special transformation (not just naive quantization)

## Reference

arXiv:2607.04422 - "Full-Stack FP4: Stable LLM Pretraining with Quantized Projections, Optimizers, and Attention" (Ding et al., 2026)

## Activation

Full-Stack FP4, NVFP4 pretraining, 4-bit pretraining, FP4 LLM training, quantized optimizer, Muon optimizer FP4, attention quantization, low-bit LLM training, LoRA-SVD quantization
