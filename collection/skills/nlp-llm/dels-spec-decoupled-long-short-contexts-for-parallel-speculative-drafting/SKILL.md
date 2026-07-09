---
name: dels-spec-decoupled-long-short-contexts-for-parallel-speculative-drafting
description: 'Speculative decoding accelerates LLM inference by drafting multiple tokens and verifying them in parallel. Block-parallel drafters such as DFlash further improve drafting efficiency by predicting an e. Based on arXiv:2607.07409.'
---

# DeLS-Spec: Decoupled Long-Short Contexts for Parallel Speculative Drafting

**arXiv**: 2607.07409 | **Authors**: Hong-Kai Zheng, Piji Li | **Utility**: 0.85

## Overview

Speculative decoding accelerates LLM inference by drafting multiple tokens and verifying them in parallel. Block-parallel drafters such as DFlash further improve drafting efficiency by predicting an entire block in one pass, but their position-wise predictions lack explicit intra-block causal conditioning. Recent methods such as Domino and DSpark attempt to introduce such causality into block-parallel drafting, but they require training the draft model from scratch, which limits their flexibility and increases training cost. We propose DeLS-Spec, a decoupled long-short context speculative decoding method. DeLS-Spec treats the fixed DFlash model as a long-context expert and introduces a lightweight local head as a short-context expert. The local head can be trained independently with a standard next-token prediction objective, without joint training with the target model or the DFlash backbone, leading to extremely low training cost. At inference time, DeLS-Spec combines long-context and short-context logits, and the local head is not tied to a specific DFlash checkpoint, making the method more modular and flexible. Experiments on Qwen3 models show that DeLS-Spec consistently improves speedup and average acceptance length over DFlash across math, code, and dialogue benchmarks.

## Key Contributions

1. Speculative decoding accelerates LLM inference by drafting multiple tokens and verifying them in parallel.
2. Block-parallel drafters such as DFlash further improve drafting efficiency by predicting an entire block in one pass, but their position-wise predictions lack explicit intra-block causal conditioning.
3. Recent methods such as Domino and DSpark attempt to introduce such causality into block-parallel drafting, but they require training the draft model from scratch, which limits their flexibility and increases training cost.
4. We propose DeLS-Spec, a decoupled long-short context speculative decoding method.

## Implementation Notes

- **Keywords**: llm, ecg, speculative-decoding
- **Categories**: cs.CL
- **Published**: 2026-07-08

## Activation Criteria

Use this skill when working on tasks involving: llm, ecg, speculative-decoding.
