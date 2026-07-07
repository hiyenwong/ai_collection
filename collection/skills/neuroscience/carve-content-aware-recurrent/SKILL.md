---
name: carve-content-aware-recurrent
category: attention-mechanisms
description: CARVE (Content-Aware Recurrent with Value Efficiency) methodology — content-aware gating for recurrent models that resolves memory-blind gating, value-axis waste, and enables WY-form chunk-parallel training.
source: arxiv:2606.27229
trigger_words:
  - CARVE
  - content-aware recurrent
  - chunk-parallel linear attention
  - memory-blind gating
  - delta rule
  - GDN
  - WY-form solver
---

# CARVE: Content-Aware Recurrent with Value Efficiency

## Overview

CARVE resolves three coupled defects in leading delta-rule architectures (e.g., GDN-2) through a single principle: **erase only on the key axis**.

## The Three Problems Solved

### 1. Memory-Blind Gating
Standard recurrent models decide what to erase by looking only at the arriving token, not at the memory being modified. CARVE gates see the stored content.

### 2. Value-Axis Erase Mask Waste
Traditional architectures waste parameters at the scale of the value projection for erase masks. CARVE replaces per-value write-gate projections with a single scalar per head.

### 3. WY-Form Solver Incompatibility
The value-axis erase mask mathematically prevents the WY-form triangular chunk solver that makes recurrent training competitive with Transformers. CARVE's key-axis-only erase is provably necessary and sufficient for WY-form validity.

## Core Architecture

### Key Principle: Erase Only on Key Axis
- Reuses recurrent output tensor (already in GPU memory) as free content signal for erase gate
- Single scalar per head replaces per-value write-gate projection
- Bit-identical to GDN-2 at initialization; quality differences emerge from content gate learning

### Proven Results (1.3B params, 100B tokens)
- WikiText perplexity: 15.72 (-0.18 vs GDN-2, 4.5-sigma)
- Leads every recurrent baseline on 9 commonsense reasoning benchmarks
- State of the art on every RULER retrieval probe
- 0.4% throughput overhead, 13% lower peak memory, 19% fewer parameters

### Six Formal Theorems
1. Memory capacity bounds
2. Lyapunov stability
3. Gradient flow characterization
4. Expressivity separation
5. Pareto-optimal chunk size
6. Hybrid optimality

## Implementation Pattern
```
For each token:
  1. Compute recurrent state update
  2. Content signal = reuse output tensor (free)
  3. Erase gate = f(content_signal) on key axis only
  4. Apply scalar write-gate per head
  5. Chunk-parallel solve via WY-form
```

## Activation
Use when: building recurrent/linear attention models, optimizing chunk-parallel training, reducing memory overhead in sequence models, or improving long-context retrieval in RNNs.

## Related
- linear-attention
- recurrent-models
- chunk-parallel-training
- memory-efficient-transformers
