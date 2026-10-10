---
name: vfold-value-cache-compression
description: Use when compressing KV-cache across LLM layers by exploiting inter-layer value cache symmetry. No architectural changes required.
tags: [kv-cache, compression, inference-efficiency, symmetry, long-context, memory-optimization]
---

# VFold: Symmetry-Aware Value Cache

## Paper Metadata

- **arXiv ID**: 2610.12338
- **Authors**: arXiv authors
- **Categories**: cs.CL, cs.LG
- **Utility Score**: 0.87
- **Date**: 2026-10
- **Link**: https://arxiv.org/abs/2610.12338

## Key Contributions

- Exploits inter-layer value cache similarities for cross-layer compression
- Symmetry-aware approach that identifies redundant structure across layers
- Requires no architectural changes — applicable to existing deployed models
- Reduces memory footprint for long-context LLM inference

## Core Methodology

VFold observes that value caches (the V in KV-cache) across different transformer layers exhibit significant similarity — they encode overlapping information about the input sequence. Rather than storing each layer's value cache independently, VFold identifies and exploits this cross-layer redundancy.

The method discovers symmetry structure in the value caches: certain patterns repeat or are approximately shared across layers. By factorizing the caches into shared and layer-specific components, VFold achieves compression without losing the information needed for accurate attention computation.

Crucially, this is a post-hoc compression technique that requires no retraining or architectural modification. It can be applied to any existing transformer model, making it immediately deployable. The symmetry analysis reveals fundamental structure in how transformers represent information across their depth.

## Relevance to nlp-llm

Directly addresses the memory bottleneck for long-context LLM inference. Cross-layer cache compression is a practical technique that can extend the context lengths achievable on existing hardware.

## Activation

kv-cache, compression, inference-efficiency, symmetry, long-context, memory-optimization
