---
name: adaptive-dhisparse-speculative
description: 'Adaptive DHiSparse: Speculative decoding over load-adaptive KV hierarchy for long-context serving. Use when optimizing LLM inference for long contexts with hierarchical KV caching.'
arxiv_id: '2610.13708'
utility: 0.86
authors: Naji Alazhar, Wassel Alazhar
categories: [cs.AI, cs.CL, cs.DC, cs.LG]
tags: [speculative-decoding, kv-cache, long-context, inference-optimization, serving]
---

# Adaptive DHiSparse: Speculative Decoding over Load-Adaptive KV Hierarchy

## Key Innovation

Long-context serving runs out of KV memory before hardware reaches useful throughput. Adaptive DHiSparse supports speculative decoding over hierarchical sparse KV and adapts residency to load — protecting working set, retaining additional history when GPU memory is spare, recovering through exact fused retrieval.

## Problem

- HiSparse stores history in host memory, fetches selected entries
- Uses one cache budget at every load level
- Does not handle draft-model speculative decoding (DSpark, DFlash2)

## Method

- Hierarchical sparse KV cache with host memory offloading
- Load-adaptive residency: adjusts what stays in GPU memory
- Protects required working set at all times
- Retains additional history when GPU memory available
- Exact fused retrieval for recovered entries
- Compatible with DSpark and DFlash2 speculative decoding

## Results

- Maintains speculative decoding speedups under memory pressure
- Adapts to varying load conditions
- Preserves DSpark/DFlash2 properties

## Practical Use

- Long-context LLM serving optimization
- Memory-efficient inference for large models
- Speculative decoding with hierarchical caching

## URL

https://arxiv.org/abs/2610.13708
