---
name: dropkv-decoupling-residual-output-perturbation-for-near-optimal
description: "DropKV: Decoupling Residual-Output Perturbation fo..."
tags: [cs.AI]
source: arxiv
arxiv_id: 2610.22130v1
utility: 0.94
published: 2026-10-15
---

# DropKV: Decoupling Residual-Output Perturbation for Near-Optimal KV-Cache Eviction

**Authors:** Aozhong Zhang, Selcuk Gurses, Yanxia Deng, Naigang Wang, Chi-Chun Liu...
**Published:** 2026-10-15
**arXiv:** [2610.22130v1](https://arxiv.org/abs/2610.22130v1)
**Categories:** cs.AI
**Utility Score:** 0.94

## Abstract

Key-value (KV) cache management has become a critical bottleneck for scaling Large Language Models (LLMs) to long-context scenarios due to linear memory growth. While recent eviction methods have moved beyond simple attention-score heuristics to incorporate value representations, they typically face a fundamental trade-off: the underlying optimization for minimizing output perturbation is an NP-hard combinatorial problem, leading to mathematically suboptimal heuristics or implementations that are difficult to kernelize. In this work, we propose DropKV, a simple principled eviction framework based on Decoupled Residual-Output Perturbation. By decoupling the joint eviction decision into independent per-token scoring, DropKV circumvents combinatorial intractability and admits a provable constant-factor approximation guarantee under a cone condition that we empirically verify on three long-context LLMs. To ensure practical viability, we provide a high-performance implementation using fused Triton kernels that avoid materializing the full attention matrix, delivering a 19.8x scoring-kernel speedup that translates to up to a 9.9% matched-batch end-to-end prefill speedup. Extensive evaluations on the RULER and LongBench benchmarks demonstrate that DropKV consistently outperforms state-of-the-art baselines at equivalent cache budgets, achieving the lowest inference latency among eviction methods while also remaining faster than the dynamic cache baseline.

## Key Contributions

- Novel research in cs.AI
- Published 2026-10-15

## Activation

dropkv, decoupling, residualoutput, perturbation, nearoptimal, kvcache, eviction
