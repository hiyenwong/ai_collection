---
name: moe-optimal-transport-routing
description: "Mixture-of-Experts (MoE) routing using optimal transport for balanced expert utilization. Region-graph Sinkhorn routing for WSI classification and spatial data. Use when: MoE load balancing, expert routing optimization, spatial token assignment, entropic optimal transport, Sinkhorn iterations, MIL aggregation, computational pathology, region-to-expert assignment, capacity-constrained routing."
---

# MoE Optimal Transport Routing

## Overview

ROAM (Region-graph OptimAl-transport Mixture-of-experts): A spatially-aware MoE routing method using entropic optimal transport for balanced expert utilization without auxiliary losses.

## Core Concepts

### 1. Problem: Unbalanced MoE Routing

**Softmax Routing Issues:**
- Few experts absorb most routing mass
- Collapse to near-single-pathway solution
- Load balancing requires auxiliary losses
- Inefficient expert utilization

### 2. Solution: Optimal Transport Routing

| Method | Constraint | Benefit |
|--------|------------|---------|
| Softmax | None | Simple but unbalanced |
| Top-k | Sparsity | Fixed expert count |
| Sinkhorn | Capacity | Balanced by construction |

### 3. ROAM Architecture

```
Spatial Region Tokens
    ↓ Compress
Region Graph Construction
    ↓ Optimal Transport
Region-to-Expert Assignment (Sinkhorn)
    ↓ Graph Regularization
Coherent Routing Across Neighbors
    ↓ Pool
Expert Aggregation
```

## Implementation

### Entropic Optimal Transport (Sinkhorn)

```python
# Key Sinkhorn formulation for MoE routing

def sinkhorn_routing(cost_matrix, capacity, entropy_reg):
    """
    Optimal transport routing with capacity constraints.
    
    Args:
        cost_matrix: Region-to-expert assignment costs
        capacity: Per-expert capacity marginals
        entropy_reg: Entropic regularization parameter
    
    Returns:
        Routing matrix P (balanced by construction)
    """
    # Sinkhorn iterations
    # P = exp(-C/ε) @ diag(u) @ diag(v)
    # Converges to optimal transport plan
```

### Graph-Regularized Routing

```
Standard Sinkhorn → Region assignments independent
    ↓ Add
Graph Regularization → Neighboring regions route coherently
    ↓ Effect
Spatial continuity + Balanced utilization
```

## Key Metrics

| Metric | Purpose | Target |
|--------|---------|--------|
| Expert Utilization | Load balance | Uniform distribution |
| Routing Coherence | Spatial continuity | Neighbor agreement |
| Classification AUC | Performance | >0.85 on benchmarks |
| Expert Collapse | Failure mode | Avoid single-expert dominance |

## Design Patterns

### 1. Region Token Compression

```python
# Compress dense patch bags into spatial bins

dense_patches → spatial_binning → region_tokens

# Benefits:
# - Align routing with tissue neighborhoods
# - Reduce routing complexity
# - Enable graph construction
```

### 2. Capacity-Constrained Marginals

```python
# Per-slide capacity marginals

capacity_per_expert = total_regions / num_experts

# Enforced by Sinkhorn
# No auxiliary load-balancing loss needed
```

### 3. Graph Regularization

```python
# Diffuse routing assignments over region graph

routing_logits → graph_laplacian → coherent_routing

# Encourages:
# - Neighbors route to same experts
# - Spatial continuity
# - Reduced routing variance
```

## Use Cases

| Domain | Application |
|--------|-------------|
| Computational Pathology | WSI classification |
| Medical Imaging | Spatial MoE routing |
| Satellite Imagery | Region-based analysis |
| Document Classification | Spatial token routing |
| Video Understanding | Temporal MoE routing |

## Advantages Over Softmax

| Aspect | Softmax | ROAM |
|--------|---------|------|
| Load Balance | Requires auxiliary loss | Built-in |
| Expert Collapse | Common | Prevented |
| Spatial Coherence | Not considered | Graph-regularized |
| Capacity Control | Implicit | Explicit marginals |

## Key Takeaways

- Optimal transport enables balanced routing by construction
- Graph regularization adds spatial coherence
- No auxiliary load-balancing losses needed
- Capacity marginals prevent expert collapse

## Reference

**Paper:** "Region-Graph Optimal Transport Routing for Mixture-of-Experts Whole-Slide Image Classification"
**arXiv:** 2604.07298v1
**Authors:** Xin Tian, Jiuliu Lu, et al.
**Date:** 2026-04-08