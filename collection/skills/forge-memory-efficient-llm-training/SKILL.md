---
name: forge-memory-efficient-llm-training
description: Fused On-Register Gradient Elimination for memory-efficient LLM training. Folds optimizer step into backward pass, applies tile-by-tile in registers, eliminating materialized gradients.
trigger_words:
  - memory-efficient training
  - gradient elimination
  - fused optimizer
  - register optimization
  - LLM training memory
version: 1.0
arxiv: 2606.22932v1
authors: Dikshant Kukreja, Kritarth Prasad, Avinash Anand, et al.
date: 2026-06-22
categories: cs.LG
---

# FORGE: Fused On-Register Gradient Elimination for Memory-Efficient LLM Training

**Core Insight:** Materialized gradients are artifacts of differentiation staging, not learning requirements. Eliminate them by folding optimizer into backward pass and applying tile-by-tile in registers.

## Problem Addressed
- **Memory ceiling bottleneck** - all layer gradients live simultaneously at backward-to-optimizer seam
- **Gradient materialization** - unnecessary tensor storage before optimizer read
- **bf16 precision loss** - conversion to bf16 for storage → read-back degrades fidelity

## Key Methodology

### Three Principles

1. **Fusion**: Fold optimizer step into backward pass
2. **Tile-by-Tile**: Apply updates one tile at a time, entirely in registers
3. **Instant Consumption**: Each gradient tile born and consumed in same registers, never becomes tensor

### Mathematical Guarantee
- **Full precision**: Fused step is **provably exact** - identical optimizer update
- **bf16/8-bit regimes**: Faithful (bounded deviation), **unbiased via stochastic rounding**
- **No precision conversion loss**: Gradients never converted to bf16 for storage

## Implementation Pattern

```python
def forge_backward(layer, grad_tile, optimizer_state):
    # Compute gradient tile in registers
    grad_tile = compute_gradient_tile(layer)
    
    # Immediately apply optimizer update in registers (no materialization)
    updated_weight = optimizer_step_in_registers(
        layer.weight, 
        grad_tile, 
        optimizer_state
    )
    
    # Stochastic rounding for bf16 (unbiased)
    if using_bf16:
        updated_weight = stochastic_round(updated_weight, target_dtype='bf16')
    
    # Update weight directly (gradient never stored)
    layer.weight = updated_weight
    
    # Gradient tile evaporated - never materialized
    return # No gradient tensor written to memory
```

## Performance Gains
- **>50% memory reduction** for optimizer step
- **~1.5x faster** at small batch sizes (fine-tuning typical)
- **4x micro-batch capacity** in tensor-parallel Megatron-LM (8B training)

## When to Use
- LLM fine-tuning with small batch sizes
- Memory-constrained GPU environments
- Continued pretraining
- Tensor-parallel training
- Any element-wise optimizer rule (Adam, AdamW, etc.)

## Key Insight
**Gradient materialization is unnecessary** - the backward-to-optimizer seam is an artifact, not a learning requirement. Fusion changes *when* update happens, not *what* it computes.

---

## References
- arXiv: [2606.22932v1](https://arxiv.org/abs/2606.22932v1)
- Authors: Dikshant Kukreja, Kritarth Prasad, et al. (9 authors)
- Categories: cs.LG