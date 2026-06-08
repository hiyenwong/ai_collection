---
name: clsa-cross-layer-sparse-attention
description: Cross-layer sparse attention sharing routing index across decoder layers for 7.6x decoding speedup and 17.1x throughput improvement at 128K context
version: 1.0.0
category: ai_collection
tags: [deep-learning, transformer, attention, efficiency, long-context]
arxiv: 2606.06467v1
paper_title: "You Only Index Once: Cross-Layer Sparse Attention with Shared Routing"
authors: ["Yutao Sun", "Yanqi Zhang", "Li Dong", "Jianyong Wang", "Furu Wei"]
published: 2026-06-04
activation_keywords: [sparse attention, cross-layer, KV-sharing, routing index, long-context, decoding efficiency, YOCO]
---

# CLSA: Cross-Layer Sparse Attention

## Core Innovation

Share **routing index** across cross-decoder layers (not just KV cache), computing token-level top-k selection once and reusing across layers.

## Problem Addressed

Existing sparse attention trade-offs:
- **Block sparse**: Strong acceleration, noticeable quality loss
- **Token sparse**: More accurate, limited speedup (expensive routing)

## Methodology

### Architecture (built on YOCO)
```
Cross-decoder layers:
├── Shared KV cache (YOCO base)
├── Shared routing index (CLSA innovation)
│   └── Compute once → reuse across layers
└── Token-level top-k selection
```

### Key Benefits
1. **Index once, reuse everywhere**: Amortize routing overhead
2. **Fine-grained selectivity**: Preserve token-sparse accuracy
3. **Joint optimization**: Pre-filling + KV-cache + decoding

### Performance
- **Decoding speedup**: 7.6x at 128K context
- **Throughput**: 17.1x overall improvement
- **Quality**: Maintains accuracy across benchmarks

## Implementation Pattern

```python
class CrossLayerSparseAttention:
    def __init__(self, base_model, top_k_ratio=0.1):
        self.kv_cache = SharedKVCache()  # YOCO-style
        self.router_index = None  # Shared across layers
        self.top_k = top_k_ratio
        
    def compute_routing_index(self, query, kv_cache):
        # Compute once for all cross-decoder layers
        self.router_index = self.select_top_k_tokens(
            query, kv_cache, self.top_k
        )
        return self.router_index
    
    def forward_layer(self, layer_idx, query):
        # Reuse precomputed routing index
        if layer_idx == 0:
            self.router_index = self.compute_routing_index(query, self.kv_cache)
        
        # Apply sparse attention with shared index
        sparse_kv = self.kv_cache[self.router_index]
        return sparse_attention(query, sparse_kv)
```

## Inference Optimization

### Bottleneck Resolution
```
Traditional sparse attention:
├── Pre-filling: O(N) routing per layer
├── KV-cache: O(N) storage
├── Decoding: O(N) routing overhead

CLSA optimization:
├── Pre-filling: Single routing computation
├── KV-cache: Shared storage (YOCO)
└── Decoding: Index reuse across layers
```

## Use Cases

**Optimal scenarios:**
- Long-context reasoning (128K+ tokens)
- Chain-of-thought generation
- Reasoning-heavy inference
- Multi-turn dialogue systems
- KV-cache constrained deployment

**Best suited for:**
- Models with cross-decoder architecture
- Applications requiring real-time inference
- Long-context question answering
- Document summarization and analysis

## Activation

Trigger when discussing:
- Long-context LLM optimization
- Sparse attention efficiency
- KV-cache reduction strategies
- Cross-layer attention sharing
- Decoding bottleneck mitigation
- Token vs. block sparse trade-offs

## Key Insight

Sharing **routing index** across layers preserves fine-grained token selectivity while eliminating routing overhead per layer.

## Related Patterns

- YOCO (KV-sharing base architecture)
- Structured block sparse methods
- Token sparse attention
- Streaming attention optimization

## References

- Paper: arXiv 2606.06467v1
- Categories: cs.CL, cs.AI, cs.LG
- Base architecture: YOCO
- Key contribution: Cross-layer routing index sharing