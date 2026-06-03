---
name: memory-efficient-looped-transformer
category: mlops
description: Memory-Efficient Looped Transformer (MELT) architecture for decoupling reasoning depth from KV cache memory consumption. Use when implementing looped/recurrent LLMs, designing memory-efficient reasoning architectures, or training Ouro-style models.
---

# Memory-Efficient Looped Transformer (MELT)

## Problem

Recurrent LLM architectures (like Ouro) perform multi-step reasoning by iteratively updating internal representations without generating intermediate tokens. However, they retain a standard Key-Value (KV) cache across iterations, causing memory to grow **linearly with reasoning depth**. This limits practical scalability of deep reasoning loops.

## MELT Architecture

### Core Idea (arXiv:2605.07721)
**Decouple reasoning depth from memory consumption** by maintaining a single KV cache per layer that is **shared across reasoning loops**, updated via a learnable gating mechanism.

### Key Components

1. **Shared KV Cache per Layer**: Instead of KV cache per layer per loop, use one KV cache per layer shared across all loops
2. **Learnable Gating Mechanism**: Updates the shared cache over time across loops
3. **Constant Memory Footprint**: Memory usage independent of reasoning depth

### Two-Phase Training Procedure

**Phase 1: Interpolated Transition**
- Smoothly transition from standard LoopLM to MELT architecture
- Interpolate between original KV cache behavior and shared KV cache behavior
- Provides stable initialization for the shared KV cache

**Phase 2: Attention-Aligned Distillation**
- Distill from the original LoopLM starting model to MELT
- Align attention patterns between the two architectures
- Ensures MELT captures the same reasoning capabilities

### Training from Pretrained Ouro

MELT models can be fine-tuned from pretrained Ouro parameters using the two-phase procedure, achieving:
- Performance comparable to or better than standard LLMs of similar size
- Memory footprint comparable to standard LLMs (dramatically smaller than Ouro's)
- Constant-memory iterative reasoning without sacrificing LoopLM performance

## Implementation Pattern

```
for loop_idx in range(num_loops):
    # Shared KV cache - same for all loops
    kv_cache = update_kv_cache(
        kv_cache,  # same cache, updated in place
        current_hidden_states,
        gating_weights  # learnable gate
    )
    
    # Attention with shared cache
    output = attention(query=current_hidden_states, kv=kv_cache)
    hidden_states = output + hidden_states  # residual
```

## Pitfalls

- **Gating mechanism is critical**: Poor gating design leads to cache contamination across loops
- **Two-phase training is necessary**: Direct training from scratch is unstable
- **Distillation target quality matters**: The LoopLM starting model must be well-trained
- **Loop depth selection**: Too few loops limits reasoning; too many may not add value
- **Cache update strategy**: Naive replacement loses information; naive accumulation overflows

## Activation Keywords

- looped transformer, Ouro, MELT, recurrent LLM
- KV cache memory, reasoning depth, iterative reasoning
- constant memory transformer, looped language model
- multi-step reasoning without token generation
