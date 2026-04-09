# LeanAttention: Scalable Decode-Phase Attention

## Overview

**Source:** arXiv:2405.10480v2
**Utility:** 0.91
**Topic:** Hardware-aware scalable attention for decode-phase of Transformers
**Key Contribution:** 2.6x speedup over FlashAttention-2, up to 8.33x for 512k context

## Activation Keywords

- lean attention
- decode-phase attention
- scalable transformer attention
- long context attention optimization
- flash attention alternative

## Core Innovation

### Problem
- Standard attention is **O(n²)** in context length
- FlashAttention optimizes but doesn't distinguish **decode vs prefill phases**
- Long context (512k+ tokens) remains challenging

### Solution: LeanAttention

**Key Insight:** Decode-phase has unique computation pattern:
- Only **1 new token** at a time
- KV-cache already populated
- Can parallelize differently than prefill

**Technique:**
1. Treat online softmax associativity as **reduction operation**
2. Extend "stream-K" tiling for parallel attention computation
3. Hardware-aware execution flow redesign

### Performance

| Context Length | FlashAttention-2 | LeanAttention | Speedup |
|----------------|------------------|---------------|---------|
| 128k | baseline | 2.6x avg | 2.6x |
| 256k | baseline | 4.2x | 4.2x |
| 512k | baseline | 8.33x | 8.33x |

## Architecture

```
Decode Phase (Token Generation):
┌─────────────────────────────────────────┐
│ KV-Cache (n tokens) + New Query (1 token)│
│         ↓                               │
│   Tiled Attention Computation           │
│         ↓                               │
│   Stream-K Parallel Reduction           │
│         ↓                               │
│   Output Token                          │
└─────────────────────────────────────────┘
```

## Implementation

### 1. Online Softmax as Reduction

```python
# Standard attention
attention = softmax(Q @ K.T) @ V

# Online softmax allows streaming computation
# Instead of computing full matrix, compute in tiles
# Use associativity: softmax(a, softmax(b, c)) = softmax(softmax(a,b), c)

def online_softmax_reduce(tiles):
    """
    Compute softmax incrementally using reduction property
    Each tile can be processed in parallel
    """
    result = tiles[0]
    for tile in tiles[1:]:
        result = combine_online_softmax(result, tile)
    return result
```

### 2. Stream-K Tiling

```python
def lean_attention_decode(q, k_cache, v_cache, block_size=128):
    """
    LeanAttention for decode phase
    
    Args:
        q: Query for new token (1, d)
        k_cache: Cached keys (n, d)
        v_cache: Cached values (n, d)
        block_size: Tile size for parallel computation
    """
    n = k_cache.shape[0]
    num_blocks = (n + block_size - 1) // block_size
    
    # Process blocks in parallel (stream-K pattern)
    block_outputs = []
    for i in range(num_blocks):
        start = i * block_size
        end = min(start + block_size, n)
        
        # Attention for this block
        k_block = k_cache[start:end]
        v_block = v_cache[start:end]
        
        scores = q @ k_block.T  # (1, block_size)
        block_outputs.append((scores, v_block))
    
    # Combine using online softmax reduction
    output = combine_blocks_online_softmax(block_outputs)
    return output
```

### 3. Hardware-Aware Optimization

```python
# GPU kernel considerations:
# - Maximize parallelism across context length dimension
# - Minimize memory transfers (keep KV-cache in fast memory)
# - Use shared memory for tile computation

# Pseudocode for CUDA kernel
__global__ void lean_attention_kernel(
    float* query,      // (1, d)
    float* k_cache,    // (n, d)
    float* v_cache,    // (n, d)
    float* output,     // (1, d)
    int n, int d, int block_size
) {
    // Each thread block handles one tile
    int block_idx = blockIdx.x;
    
    // Load query to shared memory
    // Load K/V block tiles
    // Compute local attention
    // Atomic reduction for online softmax combine
}
```

## Key Differences from FlashAttention

| Aspect | FlashAttention | LeanAttention |
|--------|----------------|---------------|
| Target Phase | Prefill + Decode | Decode only |
| Parallelization | Across batch/heads | Across context length |
| Best Context | 8k-32k | 128k-512k+ |
| KV-Cache | Re-computed | Pre-cached |
| Reduction Style | Block-wise | Stream-K |

## When to Use

**LeanAttention is best for:**
- Very long contexts (128k+ tokens)
- Decode-heavy workloads (generation tasks)
- Memory-constrained environments
- Need maximum throughput

**FlashAttention may be better for:**
- Shorter contexts (< 32k)
- Prefill-heavy workloads
- General-purpose attention

## Applications

| Use Case | Benefit |
|----------|---------|
| Long-context LLMs | 512k+ context feasible |
| Code generation | Long file context |
| Document QA | Full document attention |
| Multi-turn chat | Extended conversation history |

## Integration

### With PyTorch

```python
# Conceptual integration
from lean_attention import lean_attention_decode

class LeanTransformerDecoder(nn.Module):
    def forward(self, x, kv_cache):
        # Prefill phase: use FlashAttention
        if self.training or kv_cache is None:
            return flash_attention(x)
        
        # Decode phase: use LeanAttention
        else:
            q = self.q_proj(x[:, -1:])  # Last token only
            return lean_attention_decode(q, kv_cache.k, kv_cache.v)
```

### With vLLM / TensorRT-LLM

LeanAttention can be integrated into inference engines for long-context serving.

## References

- Paper: https://arxiv.org/abs/2405.10480
- DOI: https://doi.org/10.48550/arXiv.2405.10480
- Related: FlashAttention-2, Ring Attention

---

**Created:** 2026-03-28
**Source:** arXiv:2405.10480v2 - "LeanAttention: Hardware-Aware Scalable Attention"