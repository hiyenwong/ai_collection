---
name: memory-attention-lookup-values
description: Use when designing efficient attention variants or reducing GPU memory for LLM inference. Replaces the value projection with token-indexed memory tables plus contextual keys; value construction reduces to lookup+add.
trigger: memory attention, token-indexed memory, value projection replacement, attention lookup, CPU offloading inference, KV-free value construction, layer-specific token memory, memory-table attention
category: ai_collection
---

# Memory Attention (MA): Token-Indexed Memory as Attention Values

**Source**: arXiv:2609.28399v1 (2026-09-23) — Jiale Kang.

## Problem

Language models build attention values from contextual hidden states even when content may be reusable across contexts — a dedicated value projection W_V recomputes representations that repeat.

## Core Mechanism

Replace the value projection with **token-indexed memory** complemented by contextual keys:

```
values = M_l[token_ids]        # layer-specific token memory table
attn_out = softmax(QK^T/√d) · values
```

- **Memory supplies token-specific representations** (stable per token, reusable across contexts).
- **Keys preserve context dependence** (attention routing still dynamic).
- At inference, **fold normalization into the memory tables** → value construction = **lookup + addition** only. No W_V matmul.
- Token-indexed retrieval enables **CPU offloading with prefetching** → GPU parameter storage drops (memory tables can live in host RAM, prefetched by token id ahead of use).

## Verified Results

Under matched training token budgets (with extra memory parameters):
- Improved language modeling perplexity across attention configurations.
- Improved average downstream performance.
- GPU memory reduction via CPU offload + prefetch (no attention math on GPU for values).

## Implementation Checklist

1. Per attention layer l, allocate token memory M_l ∈ R^{V×d_v}.
2. Replace `V = H·W_V` with `V = M_l[x]` (embedding-lookup on token ids); keep Q/K projections unchanged.
3. Fold LayerNorm/RMSNorm into M_l entries after training so inference is pure lookup.
4. For offloading: store M_l in pinned host memory; prefetch rows for upcoming tokens via speculative next-token ids or simple n-gram lookup.
5. Budget: memory adds V×d_v×L parameters — amortize via shared vocab tables across layers if too large.

## Trade-offs

- Extra parameters (memory tables) vs removed W_V compute.
- Token-level value is context-invariant by design — keys carry all context dependence; tasks needing context-dependent value semantics may degrade.
- Cold-start tokens (rare ids) have under-trained memory rows — tie to embedding init.

## Related Skills

- `attention-residuals` — other attention surgery
- `spark-efficient-attention-3d` — attention efficiency patterns
- `pbkv-agent-workflow` — KV-cache management (complementary: MA removes values from cache pressure entirely)
