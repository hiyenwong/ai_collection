---
name: arxiv-2610-13982-prime-frequency-aware-unified-pruning-and-merging-for-moe-co
description: 'PRIME: Frequency-Aware Unified Pruning and Merging for MoE Compression (arXiv: 2610.13982)'
metadata:
  {
    "arxiv_id": "2610.13982",
    "utility": 0.96,
    "title": "PRIME: Frequency-Aware Unified Pruning and Merging for MoE Compression",
    "authors": "",
    "url": "https://arxiv.org/abs/2610.13982"
  }
---

# PRIME: Frequency-Aware Unified Pruning and Merging for MoE Compression

**arXiv ID:** 2610.13982
**URL:** https://arxiv.org/abs/2610.13982
**Utility Score:** 0.96

## Abstract

Mixture-of-Experts (MoE) models have emerged as an effective paradigm for scaling large language models, yet their massive parameter footprint poses severe memory challenges for deployment. Existing compression methods typically treat expert pruning and merging as disjoint operations and rely on greedy heuristics, often leading to irreversible information loss or representational pollution. In this paper, we propose PRIME, a unified optimization framework for MoE compression via adaptive PRunIng and MErging. PRIME casts the discrete prune-merge assignment step as a global Integer Linear Programming over a frequency-weighted surrogate objective, jointly selecting pruning and merging decisions while accounting for expert usage. We motivate the frequency-aware objective through an error-bound analysis under fixed representative assignments, and show that the formulation favors high-frequency experts as centroids, promoting routing stability. Extensive experiments on Qwen3-30B-A3B and Qwen3.5-122B-A10B demonstrate that PRIME achieves strong accuracy retention across knowledge, coding, math, and long-context tasks, while serving benchmarks of merged models quantify the memory and throughput benefits of expert compression in vLLM.

## Key Topics

moe, memory, compression, pruning

## Usage

This skill references the paper's concepts, methodologies, and findings for use in agent workflows.

## References

- arXiv: https://arxiv.org/abs/2610.13982
