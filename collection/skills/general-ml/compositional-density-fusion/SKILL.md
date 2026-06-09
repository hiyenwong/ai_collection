---
name: compositional-density-fusion
description: "Compositional boundaries for density fusion methodology from arXiv:2606.05871 — algebraic compositionality analysis for hierarchical probabilistic model fusion. Characterizes normalized weighted linear pooling as the unique order-invariant fusion rule and shows why pairwise solvability alone is insufficient for schedule-independent distributed uncertainty management. Activation: density fusion, uncertainty management, order-invariant fusion, distributed probabilistic models, compositional fusion, probabilistic aggregation."
---

## Context

Distributed uncertainty-management systems often combine local probabilistic models along aggregation trees. The final density should depend on weighted sources, not on the order in which intermediate nodes combine them. This paper (arXiv:2606.05871, June 2026) establishes compositional boundaries for local segment-valued fusion rules, showing when hierarchical execution remains order-invariant.

## Core Methodology

### 1. Algebraic Compositionality Problem

The central question: when can a local fusion rule be executed hierarchically while remaining order-invariant?

**Key Result**: Within the class of continuous binary rules with additive output weights and weight-only coefficients, order-invariant hierarchical execution **characterizes normalized weighted linear pooling**.

### 2. Norm-Induced Segment Balancing

Norm-induced segment balancing realizes the corresponding coefficient for normalized weighted linear pooling, ensuring that the fusion is independent of aggregation tree structure.

### 3. f-Divergence Balancing Obstruction

Smooth endpoint-to-candidate f-divergence balancing has a different local geometry: its quadratic expansion induces **square-root effective weights**, showing why pairwise solvability alone is insufficient for schedule-independent fusion.

### 4. Gaussian Mixture Case Study

- **Exact fusion** is compositional for Gaussian mixtures
- **Stepwise compression** is compositional only under a congruence condition on unnormalized component measures
- This obstruction is local to endpoint-to-candidate binary balancing
- Global divergence barycenters retain additive-weight local limits

## Implementation Steps

### Step 1: Normalized Weighted Linear Pooling

```python
import numpy as np

def weighted_linear_pool(distributions, weights):
    """Order-invariant fusion of weighted distributions via linear pooling."""
    # Normalize weights
    w = np.array(weights) / np.sum(weights)
    # Linear pool: weighted average of densities
    pooled = sum(wi * di for wi, di in zip(w, distributions))
    return pooled
```

### Step 2: Verify Compositionality

```python
def verify_compositionality(fusion_fn, dists, weights, tree_structures):
    """Test if fusion is order-invariant across tree structures."""
    results = []
    for tree in tree_structures:
        result = fusion_fn(dists, weights, tree)
        results.append(result)
    # Check all results are equivalent (within tolerance)
    return np.allclose(results[0], results[1:], atol=1e-10)
```

### Step 3: f-Divergence Barycenter

```python
from scipy.optimize import minimize

def f_divergence_barycenter(distributions, weights, f_div):
    """Compute f-divergence barycenter for distributed fusion."""
    def loss(barycenter):
        return sum(wi * f_div(barycenter, di) 
                   for wi, di in zip(weights, distributions))
    return minimize(loss, x0=np.mean(distributions, axis=0))
```

## Pitfalls

- **Pairwise Solvability ≠ Schedule Independence (2026-06-08 verified)**: Even if every pair of distributions can be fused, the global fusion may depend on aggregation order. The f-divergence quadratic expansion induces square-root effective weights, breaking compositionality. **Fix**: Use normalized weighted linear pooling for guaranteed order-invariance.
- **Gaussian Mixture Compression**: Stepwise compression of Gaussian mixtures is compositional only under congruence conditions on unnormalized component measures. Violating this causes order-dependent results. **Fix**: Check congruence condition before applying stepwise compression; fall back to global barycenter if not met.
- **Endpoint-to-Candidate vs Global**: The compositionality obstruction is local to endpoint-to-candidate binary balancing. Global divergence barycenters retain additive-weight local limits and are safer for distributed systems.

## Verification

1. **Order-Invariance Test**: Apply fusion in different tree orders; verify identical results
2. **Weight Additivity**: Output weights should sum to 1 after fusion
3. **Congruence Check**: For Gaussian mixtures, verify component measure congruence before stepwise compression

## Activation

density fusion, uncertainty management, order-invariant fusion, distributed probabilistic models, compositional fusion, probabilistic aggregation, f-divergence barycenter, weighted linear pooling, schedule-independent fusion
