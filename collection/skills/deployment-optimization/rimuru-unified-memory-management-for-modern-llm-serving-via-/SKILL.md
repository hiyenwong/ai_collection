---
name: rimuru-unified-memory-management-for-modern-llm-serving-via-
description: "Rimuru: Unified Memory Management for Modern LLM Servin..."
tags: [cs.OS, cs.LG]
source: arxiv
arxiv_id: 2610.40305v1
utility: 0.87
---

# Rimuru: Unified Memory Management for Modern LLM Serving via Elastic Expert Offloading

**arXiv ID:** [2610.40305v1](https://arxiv.org/abs/2610.40305v1)
**Published:** 2026-10-29
**Authors:** Zhiyuan Fang, Dingyang Li, Jianfeng Zhong, Bin Wang, Weixi Zhu...
**Utility Score:** 0.87

## Abstract

Modern LLMs strain device memory through large model weights and attention states, particularly in resource-constrained scenarios. Existing systems separately provision memory for model weights and attention states, imposing fixed fixed boundaries that cannot adapt to the changing memory demands of workloads. Under heavy workloads, insufficient state capacity limits request concurrency and reduces throughput; under light workloads, idle memory in one region cannot be reallocated to another, wasting device memory. Meanwhile, modern LLM architectures introduce heterogeneous tensors with diverse layouts and lifetimes, further complicating memory management. These problems motivate unified memory management for heterogeneous tensors. However, a shared pool alone does not make memory directly reusable across tensors with different allocation granularities and execution layouts. This paper presents Rimuru, a modern LLM serving system that unifies memory management through elastic expert offloading. Rimuru establishes a shared page pool to enables elastic memory sharing across heterogeneous tensors. To accommodate different allocation granularities, Rimuru introduces memory views that allow each tensor type to interpret the shared memory space using its own page size and page table. Furthermore, Rimuru combines huge-page alignment with a multi-level page allocator that splits and merges pages, enabling cross-type capacity reuse. A page-table-aware fused MoE kernel directly accesses 

## Key Contributions

- Research in deployment-optimization domain with practical applications
- Published in top arXiv categories: cs.OS, cs.LG

## Activation

cs.OS, cs.LG, arxiv paper, utility 0.87
