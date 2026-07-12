# Anyonic Quantum Kernels via Fractional Exchange Statistics (arXiv:2606.16090)

Methodology from Zhang et al. (Jun 2026) that **unifies bosonic, fermionic, and anyonic exchange statistics** within a single quantum kernel learning paradigm.

## Core Insight

Exchange statistics is a tunable computational resource, not a fixed property:
- **Bosonic**: fully symmetric wavefunctions (exchange phase θ = 0)
- **Fermionic**: fully antisymmetric (exchange phase θ = π)
- **Anyonic**: fractional phase θ ∈ (0, π) → accesses feature-space directions unavailable to either limit

## Three-Level Analysis

### 1. Representation Level
Haar-averaged effective dimension: D_eff(θ) > max(D_eff^bosonic, D_eff^fermionic) for optimal θ. Fractional exchange phases access feature-space directions inaccessible to purely symmetric or antisymmetric limits.

### 2. Kernel Geometry Level
Anyonic Gram matrices show:
- Greater separation from distinguishable-particle baseline
- Reduced label-dependent model complexity
- Better-conditioned kernel matrices

### 3. Learning Performance Level
Anyonic kernels consistently outperform bosonic/fermionic counterparts:
- Stronger target alignment
- More favorable class geometry
- Better generalization on classification benchmarks

## Implementation Pattern

Design quantum feature maps with tunable exchange statistics parameter θ ∈ [0, π]. On hardware without native anyonic support, simulate using controlled phase gates:

```python
def anyonic_exchange(wire_a, wire_b, theta):
    qml.IsingZZ(theta, wires=[wire_a, wire_b])
```

Optimize θ jointly with model parameters or via grid search.

## Hardware Note

No native anyonic support on current hardware — simulate via controlled phase gates or unitary braiding circuits.

## When to Use

- Mixed/asymmetric data structure where bosonic/fermionic kernels alone are insufficient
- Complex decision boundaries in classification
- Suboptimal Gram matrix conditioning in standard quantum kernels