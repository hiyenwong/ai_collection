---
name: speculative-sparse-attention-sts
category: research
created: "2026-05-19"
source: "arXiv:2605.15508v1"
description: Training-free sparse attention using draft model attention scores to construct dynamic token-and-head-wise sparsity masks for LLM inference. Achieves 2.67x speedup at ~90% sparsity with negligible accuracy loss.
tags: [attention, sparsity, speculative-decoding, inference-optimization, llm]
---

# STS: Speculative Token Sparsity for Efficient Attention

**Source**: arXiv:2605.15508v1 - "STS: Efficient Sparse Attention with Speculative Token Sparsity"

## Summary

Proposes a training-free sparse attention mechanism that uses a smaller draft model's attention scores to predict important tokens for a larger target model, achieving 2.67x speedup at ~90% sparsity with negligible accuracy loss.

## Core Methodology

### Key Insight
Tokens identified as important by a smaller draft model are highly predictive of important tokens for a larger target model. This cross-model attention correlation enables training-free sparsity.

### Algorithm
1. **Draft Model Scoring**: Run a small draft model (already needed for speculative decoding) to compute attention scores for each token
2. **Sparsity Mask Construction**: Use draft attention scores to dynamically construct token-and-head-wise sparsity masks for the target model
3. **Pruned Attention Computation**: Apply the mask to skip expensive attention computation on unimportant tokens in the target LLM
4. **Integration with Speculative Decoding**: STS piggybacks on the draft model that's already required for speculative decoding — no extra inference cost

### Mathematical Formulation
- For each layer l and head h, compute importance scores S_d^{(l,h)} from draft model
- Select top-k tokens per head: M^{(l,h)} = TopK(S_d^{(l,h)}, k)
- Target model attention only computed on selected token subsets
- Sparsity ratio α = (total attention entries - computed entries) / total entries

## When to Use
- LLM inference with long contexts (multi-million tokens for agentic applications)
- Scenarios where speculative decoding is already being used
- When you need high sparsity (>90%) without retraining the model
- Memory-constrained inference where KV cache is the bottleneck

## Implementation Considerations
- Requires a compatible draft model (same tokenizer, similar architecture family preferred)
- Works best with existing speculative decoding infrastructure
- No model retraining needed — purely inference-time optimization
- Maintains accuracy at high sparsity levels unlike static pruning methods

## Comparison to Alternatives
- **vs. static sparsity**: STS is dynamic, input-dependent
- **vs. KV cache eviction**: STS prunes computation, not just cache
- **vs. sliding window**: STS selects important tokens globally, not by position
- **vs. learned routing**: STS requires no training, uses existing draft model

## Activation
sparse attention, speculative decoding, attention sparsity, inference optimization, long context, token pruning
