---
name: pals-percentile-aware-layerwise-sparsity-for-llm-pruning
description: 'One-shot pruning methods like Wanda and SparseGPT apply the same sparsity ratio to every layer of a transformer, ignoring known variation in layer importance. We propose PALS (Percentile-Aware Layerwi. Based on arXiv:2607.07557.'
---

# PALS: Percentile-Aware Layerwise Sparsity for LLM Pruning

**arXiv**: 2607.07557 | **Authors**: Yazdan Jamshidi, Alexey Shvets | **Utility**: 0.85

## Overview

One-shot pruning methods like Wanda and SparseGPT apply the same sparsity ratio to every layer of a transformer, ignoring known variation in layer importance. We propose PALS (Percentile-Aware Layerwise Sparsity), which adjusts per-layer sparsity based on the 99th percentile of activation magnitudes, bounded to $\pm 5\%$ around the target ratio. On LLaMA-2-7B at 50\% sparsity, PALS achieves 10.96 WikiText-2 perplexity versus 12.92 for uniform Wanda (mean over 9 runs, $p < 0.001$). The benefit is architecture-dependent: LLaMA-3-8B shows marginal gains and Mistral-7B shows none. We also find that gradient-based allocation -- the seemingly more principled approach -- produces results worse than random, suggesting that gradient magnitude does not predict the impact of discrete weight removal. PALS adds negligible cost to the pruning pipeline and requires no fine-tuning.

## Key Contributions

1. One-shot pruning methods like Wanda and SparseGPT apply the same sparsity ratio to every layer of a transformer, ignoring known variation in layer importance.
2. We propose PALS (Percentile-Aware Layerwise Sparsity), which adjusts per-layer sparsity based on the 99th percentile of activation magnitudes, bounded to $\pm 5\%$ around the target ratio.
3. On LLaMA-2-7B at 50\% sparsity, PALS achieves 10.96 WikiText-2 perplexity versus 12.92 for uniform Wanda (mean over 9 runs, $p < 0.001$).
4. The benefit is architecture-dependent: LLaMA-3-8B shows marginal gains and Mistral-7B shows none.

## Implementation Notes

- **Keywords**: llm, transformer, model-pruning
- **Categories**: cs.CL, cs.LG
- **Published**: 2026-07-08

## Activation Criteria

Use this skill when working on tasks involving: llm, transformer, model-pruning.
