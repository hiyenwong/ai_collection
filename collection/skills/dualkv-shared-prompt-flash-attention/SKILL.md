---
name: dualkv-shared-prompt-flash-attention
category: research
created: "2026-05-19"
source: "arXiv:2605.15422v1"
description: FlashAttention kernel variant that eliminates shared-prompt replication during RL training. Fused CUDA kernels process prompt once across N rollouts, achieving 1.63-3.82x speedup for GRPO/DAPO training.
tags: [attention, flash-attention, rl-training, kernel-optimization, grpo]
---

# DualKV: Shared-Prompt Flash Attention for Efficient RL Training

**Source**: arXiv:2605.15422v1 - "DualKV: Shared-Prompt Flash Attention for Efficient RL Training with Large Rollouts and Long Contexts"

## Summary

Proposes a FlashAttention kernel variant that eliminates redundant prompt computation during RL post-training (GRPO, DAPO). By processing shared prompts once across all N rollout sequences, achieves 1.63-3.82x speedup and increases MFU from 36% to 76%.

## Core Methodology

### Key Insight
In decoder-only models, causal masking makes prompt representations invariant across all N response sequences at every layer. Standard FlashAttention replicates all P prompt tokens N times, duplicating compute on identical hidden states.

### Two Components
1. **Fused CUDA Kernels**: Forward and backward kernels that iterate over two disjoint KV regions:
   - Shared context (processed once)
   - Per-sequence response (processed N times)
   - Single kernel launch for both regions

2. **Data Pipeline Redesign**: Repacks N(P+R) tokens into P+NR tokens per micro-batch
   - Token reduction factor: ρ = N(P+R) / (P+NR)
   - Extends benefit from attention to entire model

### Results
- Qwen3-8B GRPO (N=32, 8K-context, 8xH100): 1.63-2.09x speedup, MFU 36%→76%
- DAPO: 2.47x speedup, 77% MFU
- 30B MoE (16xH100): 3.82x policy-update speedup, 3.38x end-to-end speedup
- Mathematically equivalent to standard attention — no approximation

## When to Use
- RL post-training with large rollouts (N ≥ 16) and long contexts (P ≥ 8K)
- GRPO, DAPO, or similar multi-response RL algorithms
- When prompt computation dominates policy update cost
- Memory-constrained training requiring sequence parallelism

## Implementation Considerations
- Requires custom CUDA kernel implementation
- Must modify data pipeline to repack tokens
- Works with any decoder-only model
- Eliminates need for Ulysses sequence parallelism at scale

## Activation
dualkv, shared prompt flash attention, grpo training speedup, rl kernel optimization, prompt dedup, daPO
