---
name: tf-engram-a-train-free-engram-with-ssd-backed-memory-for-large-language-models
description: 'Large Language Models (LLMs) store factual knowledge and domain-specific patterns implicitly in dense Transformer parameters, making knowledge expansion costly through pretraining, fine-tuning, retrie. Based on arXiv:2607.07388.'
---

# TF-Engram: A Train-Free Engram with SSD-Backed Memory for Large Language Models

**arXiv**: 2607.07388 | **Authors**: Yutang Ma, Kecheng Huang, Xikun Jiang, Zili Shao | **Utility**: 0.86

## Overview

Large Language Models (LLMs) store factual knowledge and domain-specific patterns implicitly in dense Transformer parameters, making knowledge expansion costly through pretraining, fine-tuning, retrieval augmentation, or longer contexts. Engram-style memory offers a compact hidden-state injection pathway, but existing GPU-resident designs often rely on hash-based compression, causing unrelated phrases to collide in shared slots and weakening phrase-level semantic fidelity. We present TF-Engram, a train-free Engram system that constructs phrase-specific semantic memory offline from external corpora, stores large memory tables across a GPU--DRAM--SSD hierarchy, and uses Early-Exit Guided Predictive Prefetching to hide external-memory latency during autoregressive decoding. On Qwen3-0.6B, TF-Engram improves the average downstream score from 57.6 to 59.4, outperforming both the frozen backbone and a parameter-matched LoRA baseline. System evaluation shows that large TF-Engram tables can be built with moderate offline cost, SSD-backed storage substantially reduces GPU memory demand, and predictive prefetching recovers much of the throughput loss caused by external memory access. These results demonstrate that static phrase memory can be integrated into LLM inference as a scalable, train-free, and low-overhead system component.

## Key Contributions

1. Large Language Models (LLMs) store factual knowledge and domain-specific patterns implicitly in dense Transformer parameters, making knowledge expansion costly through pretraining, fine-tuning, retrieval augmentation, or longer contexts.
2. Engram-style memory offers a compact hidden-state injection pathway, but existing GPU-resident designs often rely on hash-based compression, causing unrelated phrases to collide in shared slots and weakening phrase-level semantic fidelity.
3. We present TF-Engram, a train-free Engram system that constructs phrase-specific semantic memory offline from external corpora, stores large memory tables across a GPU--DRAM--SSD hierarchy, and uses Early-Exit Guided Predictive Prefetching to hide external-memory latency during autoregressive decoding.
4. On Qwen3-0.6B, TF-Engram improves the average downstream score from 57.6 to 59.4, outperforming both the frozen backbone and a parameter-matched LoRA baseline.

## Implementation Notes

- **Keywords**: llm, transformer, agent-memory
- **Categories**: cs.CL, cs.LG
- **Published**: 2026-07-08

## Activation Criteria

Use this skill when working on tasks involving: llm, transformer, agent-memory.
