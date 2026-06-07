---
name: speculative-decoding-optimization
description: >
  Optimize LLM inference using speculative decoding with KV cache compression.
  Covers adaptive gamma selection, compression-aware token verification,
  and KV cache management for reduced latency. Use when: (1) Optimizing
  LLM serving throughput, (2) Implementing speculative decoding with draft models,
  (3) Managing KV cache for long-context generation, (4) Reducing inference latency
  for large language models. Triggers on: speculative decoding, KV cache, draft model,
  token verification, gamma selection, LLM optimization, inference speedup.
---

# Speculative Decoding Optimization

## Overview

Speculative decoding accelerates LLM inference by using a smaller draft model
to generate candidate tokens, which the target model verifies in parallel.
Key insight: the draft model is cheap; verification is parallel and cheap.

## Core Algorithm

```
for each generation step:
    1. Draft model generates γ candidate tokens (auto-regressive)
    2. Target model computes probabilities for all γ tokens in ONE forward pass
    3. Verify each token: if P_target >= P_draft, accept; else reject
    4. On rejection: sample from corrected distribution, reset draft
```

**Speedup ≈ (γ + 1) / (1 + rejection_rate × γ)**

## KV Cache Management

### Compression-Aware Gamma Selection

The optimal number of draft tokens (γ) depends on:
- Draft-target model agreement rate
- KV cache memory pressure
- Sequence length and context window utilization

**Adaptive γ formula:**
```
γ = min(γ_max, floor(1 / (1 - agreement_rate)))
```

Where agreement_rate is the historical acceptance rate of draft tokens.

### Cache Compression Techniques

1. **Layer skipping**: Skip KV cache for lower attention layers during draft
2. **Quantization**: Int4/Int8 KV cache reduces memory by 4-8x
3. **Sliding window**: Keep only recent KV entries, evict oldest
4. **Prefix sharing**: Reuse KV cache for shared prompt prefixes across requests

## Implementation Patterns

### Pattern 1: Single-Request Speculative Decoding

Use when optimizing single-stream generation latency.

```python
def speculative_decode(draft_model, target_model, prompt, gamma=5):
    tokens = tokenize(prompt)
    accepted = 0
    total_draft = 0
    
    while not eos(tokens):
        # Draft phase
        candidates = draft_model.generate(tokens, steps=gamma)
        total_draft += len(candidates)
        
        # Verification phase (parallel)
        logits = target_model.forward(tokens + candidates)
        
        # Accept/reject
        new_tokens = verify(logits, candidates, tokens)
        tokens.extend(new_tokens)
        accepted += len(new_tokens)
    
    return tokens, accepted / total_draft
```

### Pattern 2: Multi-Request Batch Speculation

Use when serving multiple concurrent requests.

- Batch draft tokens from multiple requests
- Single target model forward pass verifies all
- Dynamic γ per request based on individual agreement rates

### Pattern 3: Self-Speculative Decoding

Use when no separate draft model is available.

- Early layers of target model serve as draft
- Shallow decoder generates candidates
- Full model verifies

Typically achieves 1.5-2x speedup with no extra model.

## Verification Strategies

### Rejection Sampling (Standard)

```python
def verify(target_logits, draft_tokens, temperature=1.0):
    accepted = []
    for i, token in enumerate(draft_tokens):
        p_target = softmax(target_logits[i])
        p_draft = draft_probs[i]
        
        if p_target[token] >= p_draft[token]:
            accepted.append(token)
        else:
            # Sample from corrected distribution
            corrected = p_target / (1 - p_draft)
            new_token = sample(corrected, temperature)
            accepted.append(new_token)
            break  # Stop at first rejection
    return accepted
```

### Tree-Based Speculation

For higher parallelism, use tree-structured draft tokens:
- Draft model generates a tree of candidates
- Target model verifies multiple paths simultaneously
- Higher acceptance rate due to path diversity

## Performance Tuning

| Parameter | Effect | Typical Range |
|-----------|--------|---------------|
| γ (gamma) | More candidates = more speedup but higher rejection | 3-8 |
| Draft size | Smaller = faster draft but lower quality | 100M-1B params |
| Batch size | Larger = better GPU utilization | 8-64 |
| Temperature | Lower = higher agreement rate | 0.3-0.8 |

## When NOT to Use

- Very short outputs (< 50 tokens): overhead dominates
- Already memory-bound: KV cache compression won't help
- Low draft-target agreement (< 40%): speedup < 1.1x

## References

- **SpecKV** (arXiv:2605.02888): Adaptive gamma selection with compression awareness
- **LLM.spec_decode**: Speculative decoding in vLLM
- **Medusa**: Multi-head speculative decoding architecture
