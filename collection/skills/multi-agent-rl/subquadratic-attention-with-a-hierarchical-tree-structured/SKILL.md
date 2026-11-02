---
name: subquadratic-attention-with-a-hierarchical-tree-structured
description: "Subquadratic Attention with a Hierarchical Tree-St..."
tags: [cs.CL, cs.AI]
source: arxiv
arxiv_id: 2610.42112v1
utility: 0.92
published: 2026-10-30
---

# Subquadratic Attention with a Hierarchical Tree-Structured Indexer

**Authors:** Leon Lufkin, Cutter Dawes, Alexander Speicher, Kamesh Krishnamurthy, Tomás Figliolia...
**Published:** 2026-10-30
**arXiv:** [2610.42112v1](https://arxiv.org/abs/2610.42112v1)
**Categories:** cs.CL, cs.AI
**Utility Score:** 0.92

## Abstract

The quadratic scaling of attention is a fundamental bottleneck limiting the long-context capabilities of large language models (LLMs). A variety of approaches have attempted to circumvent this, but they either fail to match attention's expressiveness (e.g., sliding-window or linear attention variants with fixed-size state) or only achieve constant-factor speedups (e.g., sparse attention methods whose indexers themselves scale quadratically). In this paper, we derive an asymptotically subquadratic sparse attention method based on a hierarchical, tree-structured indexer, which we call Zyphra Hierarchical Attention (ZHA). ZHA constructs a tree of recursively compressed key summaries over the KV cache, which future queries traverse from the top down to retrieve a sparse subset of keys. Crucially, by iteratively growing the tree's depth, the total cost including routing and final attention grows sublinearly in sequence length, resulting in overall subquadratic (but superlinear) scaling for attention. We demonstrate that ZHA can be cheaply applied to existing pretrained models with only a short KL distillation training stage over a few billion tokens, and maintains performance on long-context retrieval and challenging reasoning, mathematical, and agentic coding evaluation tasks. Moreover, we show that our method is highly robust to tree geometry including very deep trees of up to 6 levels. Finally, we develop a detailed performance model and show that our approach scales subquadrat

## Key Contributions

- Novel research in cs.CL, cs.AI
- Published 2026-10-30

## Activation

subquadratic, attention, hierarchical, treestructured, indexer
