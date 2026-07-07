---
name: unipool-shared-expert-moe
description: "Expert guidance for globally shared expert pool Mixture-of-Experts architecture. Based on UniPool paper (arXiv:2605.06665). Use when designing MoE architectures, expert pooling, pool-level balancing, NormRouter, sublinear expert parameter scaling, or memory-efficient LLM training."
---

# UniPool: Globally Shared Expert Pool for Mixture-of-Experts

Based on: *UniPool: A Globally Shared Expert Pool for Mixture-of-Experts* (arXiv:2605.06665)
Authors: Minbin Huang, Han Shi, Chuanyang Zheng, Yimeng Wu, Guoxuan Chen, Hong Cheng

## Problem

Modern MoE architectures use rigid per-layer expert ownership, coupling depth scaling with linear expert-parameter growth. Replacing a deeper layer's learned top-k router with uniform random routing drops accuracy by only 1.0-1.6 points, revealing redundancy in per-layer expert allocation.

## Key Innovation

UniPool replaces per-layer expert ownership with a **single global shared pool** accessed by independent per-layer routers:

1. **Pool-level auxiliary loss**: Balances expert utilization across entire pool, not per-layer
2. **NormRouter**: Provides sparse and scale-stable routing into shared pool
3. **Sublinear scaling**: Expert parameters need not grow linearly with depth

## Architecture

```
Layer 1 ──┐
Layer 2 ──┼→ Shared Expert Pool → Independent per-layer routers
Layer N ──┘
```

### Key Components

1. **Global Expert Budget**: Treat expert capacity as global architectural budget
2. **Pool-Level Balancing**: Auxiliary loss balances across entire pool
3. **NormRouter**: Sparse, scale-stable routing mechanism

## Results

- Tested on 5 LLaMA scales: 182M, 469M, 650M, 830M, 978M parameters
- Trained on 30B tokens from The Pile
- Up to 0.0386 validation loss reduction vs vanilla MoE
- Reduced-pool variants (41.6%-66.7% expert budget) match or outperform layer-wise MoE

## Implementation Patterns

### Pattern 1: Pool-Level Auxiliary Loss
- Balance expert utilization at pool level, not per-layer
- Prevents expert collapse in shared architecture
- Critical for stable training with shared routing

### Pattern 2: Reduced Pool Variants
- Use 41.6%-66.7% of vanilla expert budget
- Match or exceed vanilla MoE performance
- Expert parameters scale sublinearly with depth

### Pattern 3: Composable with Finer Expert Decomposition
- UniPool benefits compose with finer-grained expert decomposition
- Can combine with other MoE improvements

## Activation Keywords

- unipool
- shared expert pool
- pool-level MoE
- global expert budget
- NormRouter
- sublinear MoE scaling
- expert parameter reduction

## Implementation Steps

1. **Architecture Design**
   - Replace per-layer expert sets with single shared pool
   - Maintain independent per-layer routers
   - Add pool-level auxiliary loss

2. **Training Configuration**
   - Use NormRouter for stable routing
   - Monitor expert utilization across pool
   - Compare against matched vanilla MoE baseline

3. **Scaling Analysis**
   - Test pool size as explicit depth-scaling hyperparameter
   - Evaluate reduced-pool variants at multiple scales
   - Measure sublinear scaling efficiency

## Pitfalls

1. **Per-layer balancing in shared pool** → use pool-level loss instead
2. **No baseline comparison** → always match vanilla MoE at same scale
3. **Ignoring router stability** → NormRouter critical for stable training
4. **Fixed pool size** → treat pool size as depth-scaling hyperparameter

## Related Skills

- emo-emergent-moe-modularity
- moe-optimal-transport-routing
- routing-distraction-multimodal-moe

## References

- arXiv:2605.06665
