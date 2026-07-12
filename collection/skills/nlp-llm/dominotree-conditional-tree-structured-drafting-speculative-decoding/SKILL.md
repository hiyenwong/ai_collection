---
name: dominotree-conditional-tree-structured-drafting-speculative-decoding
description: "Training-free best-first draft tree for speculative decoding using Domino's conditional non-factorized correction. Achieves up to 6.6x speedup on Qwen3-4B and highest mean accept length (10.7 tokens/round). GPU-native CUDA-graph builder for efficient tree construction. Activation: speculative decoding, tree-structured drafting, Domino conditioning, LLM inference, block-diffusion."
metadata:
  arxiv_id: "2607.08642"
  published: "2026-07-09"
  authors: "Saw S. Lin, Jyh-Shing Roger Jang"
  tags: [speculative-decoding, tree-structured-drafting, domino-conditioning, llm-inference, block-diffusion]
---

# DominoTree: Conditional Tree-Structured Drafting with Domino for Speculative Decoding

## Overview

Speculative decoding accelerates LLM inference by drafting tokens and verifying in parallel. DominoTree combines the path-dependent correction of Domino drafters with best-first tree expansion, creating a training-free method that achieves the highest mean accept length among evaluated methods on Qwen3-4B.

## Key Innovations

### Conditional Non-Factorized Tree
- Uses Domino's conditional, non-factorized correction along each root-to-node path
- Overcomes DDTree's factorized formulation that cannot represent path-dependent distributions
- Restricts per-node correction to candidate top-M for tractability

### GPU-Native CUDA-Graph Builder
- Bit-identical to reference Python implementation
- Keeps per-round tree construction cheap
- Enables practical deployment without acceptance degradation

### Performance
- Up to 6.6x speedup over autoregressive decoding on Qwen3-4B
- Highest mean accept length: up to 10.7 tokens per round at every temperature
- Throughput wins over released Domino decoder at every temperature (9-10% overall)
- Up to +22% on Alpaca at specific temperatures

## Methodology

1. **Draft Tree Construction**: Best-first tree expansion scored by Domino's conditional correction
2. **Candidate Restriction**: Limit per-node correction to top-M candidates
3. **CUDA-Graph Builder**: GPU-native tree construction for efficiency
4. **Verification**: Parallel verification by the target LLM

## Implications

- Path-dependent distributions are crucial for effective speculative decoding trees
- GPU-native implementation makes tree-structured drafting practical
- Training-free approach enables immediate deployment without additional training
- Sets new performance benchmarks for speculative decoding

## Pitfalls

- Performance advantage narrows at higher temperatures on larger models
- Tree construction complexity may increase with deeper trees
- Depends on quality of the underlying Domino drafter
- Top-M restriction may miss valid candidates in rare cases

## Activation Keywords

speculative decoding, DominoTree, tree-structured drafting, Domino conditioning, LLM inference acceleration, CUDA-graph builder, block-diffusion, Qwen3, training-free decoding

## Paper Reference

arXiv:2607.08642 - "DominoTree: Conditional Tree-Structured Drafting with Domino for Speculative Decoding" (Jul 2026)
