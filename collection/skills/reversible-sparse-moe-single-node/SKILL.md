---
name: reversible-sparse-moe-single-node
description: Train hundred-billion-parameter sparse MoE models on single nodes using reversible recurrence stacks and state-preserving growth principles with TQP optimizer strategy.
authors:
  - Rohan Shravan
date: 2026-06-05
arxiv: 2606.07404v1
tags:
  - foundation-model
  - sparse-moe
  - single-node
  - reversible-computing
  - memory-efficient
  - scaling
---

# Reversible Sparse MoE Single-Node Training

## Overview

Train 120B sparse mixture-of-experts (MoE) models on single eight-GPU nodes through reversible recurrence stacks, state-preserving growth, and TQP optimizer strategy. Achieves flat activation memory regardless of model growth through reversibility principle.

## Key Innovation

**Three Disciplines Integration:**
1. **Reversibility**: Recurrence stack reconstructs activations in backward pass
2. **State-Preserving Growth**: Reproducible expansion principles with documented failure modes
3. **Single-Node Economics**: TQP (quantized base + trained low-rank adapters) reduces optimizer state by ~45x

**Memory Efficiency:** Activation memory remains flat as model grows (reversibility eliminates storage)

**Parameter Efficiency:** Active params rise monotonically (1.78B → 5.93B, ~5% of 118.67B stored)

## Methodology

### Principle 1: Reversible Recurrence Stack

```
# Standard: Store all activations for backward pass
# Memory: O(depth * batch_size)

# Reversible: Reconstruct activations during backward
# Memory: O(batch_size) (flat!)

Forward:
    state = initial_state
    for layer in stack:
        state = layer(state)
    # No storage of intermediate states

Backward:
    # Reconstruct from final state
    state = final_state
    for layer in reversed(stack):
        state = layer.inverse(state)  # Reversible operation
        # Compute gradients locally
```

### Principle 2: State-Preserving Growth

**Four-Stage Growth Lineage:**
1. Dense seed (small dense model)
2. 5B MoE (dense → MoE expansion)
3. 9B MoE (shallow → deep expansion)
4. 120B MoE (few → many experts)

**Each Expansion Principle:**
- Dense to MoE: Initialize experts from dense weights
- Shallow to deep: Copy layers, add depth
- Few to many: Duplicate experts, reinitialize routing

**Failure Modes (Silent):**
- Incorrect initialization → routing collapse
- Wrong growth factor → gradient instability
- Improper scaling → capacity mismatch

### Principle 3: TQP Optimizer Strategy

```
# Traditional MoE: Optimizer state for all routed experts
# Memory: O(118B * optimizer_factor) = huge

# TQP: Quantized base + trained low-rank adapters
Base expert weights: Quantized (fixed)
Low-rank adapters: Full optimizer state (2.26B params)

Optimizer state reduction:
    2.26B / 118.67B ≈ 1.9% of stored weights
    ~45x reduction vs. full expert optimizer state
```

### Architecture Details

**LightningLM 0.1V Specs:**
- 120B total parameters
- 460 routed experts
- Top-12 routing
- 5.93B active parameters per forward pass
- 8K context length
- Single 8-GPU node training

**Released Metrics:**
- Training loss: 1.78 at 120B scale
- Indic language competence (targeted)
- Code capabilities (targeted)

## Reusable Patterns

### Pattern 1: Reversible Layer Implementation
**Use when:** Memory-constrained training of deep models
**Key requirement:** Layers must have inverse operations
**Example reversible operations:**
- Addition/subtraction
- Matrix multiplication with stored matrices
- Attention with reversible patterns (e.g., reversible residual blocks)

### Pattern 2: State-Preserving Expansion
**Use when:** Growing model capacity without retraining from scratch
**Steps:**
1. Identify expansion type (dense→MoE, shallow→deep, few→many)
2. Define initialization from smaller model
3. Document expected failure modes (silent failures critical)
4. Validate state preservation with held-out loss

### Pattern 3: TQP Optimizer for Sparse Models
**Use when:** Sparse MoE with prohibitive optimizer state
**Implementation:**
- Quantize base expert weights (freeze or minimal updates)
- Train low-rank adapters per expert
- Optimizer state only on adapters
- Result: ~45x optimizer state reduction

### Pattern 4: Growth Lineage Training
**Use when:** Progressive scaling from seed to large model
**Approach:**
- Stage 1: Dense seed (fast training)
- Stage 2: MoE conversion (efficient capacity boost)
- Stage 3: Depth expansion (context/complexity)
- Stage 4: Expert multiplication (final capacity)
- Each stage: State-preserving, not retraining

## Implementation Considerations

### Reversibility Implementation
- Use reversible residual blocks (e.g., RevNet)
- Attention: Store only queries, reconstruct keys/values
- MoE routing: Stateless routing decisions

### State-Preserving Checks
- Held-out loss before and after expansion
- Targeted capability metrics (multilingual, code)
- Per-domain validation

### TQP Quantization
- Base weights: Int8 or Int4 quantization
- Adapters: Full precision, trainable
- Router: Full precision (critical for routing quality)

### Single-Node Constraints
- 8 GPUs typically 80GB each (total 640GB)
- Reversibility: Activation memory flat
- TQP: Optimizer state minimal
- Result: 120B fits on single node

## Extensions

### Beyond Language Models
- Apply to vision transformers
- Reversible ViT architectures
- Sparse vision MoE

### Multi-Node Scaling
- Reversibility + TQP for multi-node efficiency
- Distribute experts across nodes
- Router synchronization overhead

### Continuous Growth
- Automated expansion triggers
- Dynamic expert addition
- Adaptive routing expansion

## Pitfalls

1. **Reversible Layer Design**: Not all operations have efficient inverses (e.g., softmax)
2. **State-Preserving Silent Failures**: Routing collapse without obvious symptoms
3. **Quantization Degradation**: Over-quantized base weights hurt quality
4. **Adapter Rank**: Too low rank → insufficient expressiveness
5. **Expert Initialization**: Wrong initialization → slow convergence or collapse
6. **Growth Timing**: Premature expansion → unstable training

## Related Methods

- RevNet (reversible residual networks)
- Gradient checkpointing (memory trade-off)
- Sparse MoE (Switch Transformer, GShard)
- Progressive training (curriculum)
- LoRA (low-rank adaptation)

## Code & Resources

- Model family released
- Tokenizer released
- Training code released
- Paper: Experience report format

## Applications

- Large model training on limited hardware
- Startup/academic training of 100B+ models
- Efficient MoE deployment
- Memory-constrained foundation model development
- Progressive scaling strategies

## Activation Keywords

`reversible training`, `sparse MoE`, `single-node training`, `memory-efficient`, `state-preserving growth`, `TQP optimizer`, `120B model`, `low-rank adapters`, `expert quantization`, `reversible recurrence`, `growth lineage`, `flat activation memory`