---
name: sparsedecoding-llm-pruning
description: Use when pruning LLMs for efficient inference with Hessian-guided methods focused on the decoding (generation) stage rather than prefill.
tags: [pruning, inference-efficiency, hessian, decoding, memory-bound, sparse-inference]
---

# SparseDecoding: LLM Pruning

## Paper Metadata

- **arXiv ID**: 2610.12327
- **Authors**: arXiv authors
- **Categories**: cs.CL, cs.LG
- **Utility Score**: 0.86
- **Date**: 2026-10
- **Link**: https://arxiv.org/abs/2610.12327

## Key Contributions

- Decoding-aware pruning: optimizes for the generation stage specifically, not just prefill/encoding
- Hessian-guided pruning focused on decoding-stage sensitivity
- Addresses memory-bound latency in autoregressive generation
- Shows that prefill-optimal pruning is not decoding-optimal

## Core Methodology

SparseDecoding recognizes that LLM inference has two distinct phases — prefill (processing the prompt) and decoding (autoregressive token generation) — with different computational characteristics. Standard pruning methods optimize for overall model quality or prefill efficiency, but decoding is memory-bound (dominated by memory access, not compute) and has different sensitivity patterns.

The method uses Hessian information specifically computed for the decoding stage to guide pruning decisions. The Hessian captures which parameters most affect the model's output distribution during generation, allowing the method to preserve parameters that matter most for token-by-token prediction while removing those that can be safely dropped.

This decoding-focused approach addresses the key bottleneck in long-form generation: memory-bound latency from loading large model weights at each step. By pruning more aggressively in dimensions that don't affect decoding quality, SparseDecoding achieves faster generation without proportional quality loss.

## Relevance to nlp-llm

Practical inference optimization: shows that task-aware pruning (decoding-specific) outperforms generic pruning for the generation use case that dominates LLM deployments.

## Activation

pruning, inference-efficiency, hessian, decoding, memory-bound, sparse-inference
