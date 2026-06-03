---
name: streamindex-csa-topk
description: Memory-bounded compressed sparse attention via streaming chunked top-k. Eliminates OOM in DeepSeek-V4 CSA indexer by avoiding full score tensor materialization.
category: deep-learning
tags: [attention, sparse-attention, Triton, memory-optimization, DeepSeek, compression]
trigger: streamindex, compressed sparse attention, streaming top-k, CSA indexer, Triton, OOM prevention, TileLang
---

# StreamIndex: Memory-Bounded Compressed Sparse Attention via Streaming Top-k

## Overview
StreamIndex solves the OOM problem in DeepSeek-V4's Compressed Sparse Attention (CSA) indexer by using a chunked partition-merge top-k driver that never materializes the full [B, S, H_I, T] score tensor.

## Core Technique
1. **Chunked Partition-Merge Top-k**: Process the score tensor in chunks, maintaining a running top-k selection without materializing the full intermediate
2. **Triton Implementation**: Custom Triton kernels for efficient chunked scoring and top-k reduction on GPU
3. **Bit-Exact Recall**: Set-overlap recall against materialize ground truth is bit-exact at small S; mean recall ≥ 0.9980 across all configurations
4. **Kernel Composition**: Chunked driver composes with TileLang's pipelined attention kernel for end-to-end memory-bounded execution

## Key Results
- **32x regime extension**: Materialize path OOMs at S=65,536; StreamIndex runs to S=1,048,576 with 6.21 GB peak HBM
- **Composition**: At S=262,144, materialize+TileLang OOMs; StreamIndex+TileLang runs in 1.97s at 18.56 GB peak
- **Target**: Indexer step only — not a faster attention kernel or end-to-end checkpoint validation

## Implementation Steps
1. Partition the [B, S, H_I, T] score computation into manageable chunks
2. For each chunk: compute scores via learned projection, run local top-k
3. Merge local top-k results using partition-merge strategy
4. Output final top-k indices for sparse attention kernel
5. Compose with existing attention kernel (e.g., TileLang) for full pipeline

## Pitfalls
- Chunk size selection affects both memory and performance — requires tuning for target GPU
- Only addresses the indexer step, not the sparse attention kernel itself
- Bit-exactness degrades slightly at very large S (min recall 0.9980) — verify tolerance for your use case

## Activation Keywords
streamindex, compressed sparse attention, streaming top-k, CSA indexer, Triton, OOM prevention, TileLang, DeepSeek V4, memory optimization
