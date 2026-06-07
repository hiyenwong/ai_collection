---
name: symmetry-protected-lyapunov-equivariant-rnn
description: "Symmetry-Protected Lyapunov Neutral Modes in Equivariant Recurrent Networks. Theoretical framework for when continuous attractors (zero Lyapunov exponents) are guaranteed by symmetry rather than tuning. Activation: equivariant rnn, symmetry-protected modes, Lyapunov neutral modes, continuous attractor, path integration, rotational memory."
---

# Symmetry-Protected Lyapunov Neutral Modes in Equivariant Recurrent Networks

> Theoretical framework proving that equivariant recurrent networks with Lie group symmetry have guaranteed zero Lyapunov exponents along group orbits, enabling robust continuous memory without fine-tuning.

## Metadata
- **Source**: arXiv:2605.03338
- **Authors**: Hanson Hanxuan Mo
- **Published**: 2026-05-05
- **Category**: cs.NE, math.DS

## Core Methodology

### Key Innovation
For recurrent networks storing **position, phase, or other continuous variables**, this paper proves that **symmetry guarantees neutral directions** (zero Lyapunov exponents) rather than requiring careful parameter tuning:

- **Theorem**: For a C¹ autonomous vector field equivariant under Lie group G, any compact invariant set with uniformly nondegenerate group-orbit bundle and stabilizer type H has at least **dim(G/H) zero Lyapunov exponents** tangent to the group orbit
- **Protection mechanism**: Zero group-tangent growth comes from **exact equivariance and orbit geometry**, not from parameter tuning
- **Breaking analysis**: When protection is broken, the resulting pseudo-gap predicts finite memory lifetime

### Technical Framework

**Mathematical Foundation:**
1. **Equivariance**: A vector field f is G-equivariant if f(g·x) = g·f(x) for all g ∈ G
2. **Group orbits**: The set {g·x : g ∈ G} for a point x in state space
3. **Stabilizer**: The subgroup H = {g ∈ G : g·x = x} fixing a point
4. **Quotient dimension**: dim(G/H) gives the number of protected neutral modes

**Symmetry groups and their neutral modes:**
- **S¹** (circle rotation): 1 neutral mode → head direction, angular position
- **T^q** (q-torus): q neutral modes → multi-dimensional position encoding
- **SO(n)** (rotation group): n(n-1)/2 neutral modes → full rotational invariance
- **U(m)** (unitary group): m² neutral modes → quantum state analogs

### Verification Metrics

**Five verification methods for symmetry protection:**
1. **Normalized equivariance error**: Measure ‖f(g·x) - g·f(x)‖ / ‖f(x)‖
2. **Direct group-tangent exponents**: Compute Lyapunov exponents along group directions
3. **Principal-angle alignment**: Compare tangent space with group orbit tangent
4. **Autonomous-flow-zero controls**: Verify zero growth under zero-input dynamics
5. **Orbit-dimension scaling**: Check that number of neutral modes scales with dim(G/H)

### Implementation Guide

**Training an equivariant recurrent cell:**
```python
import torch
import torch.nn as nn

class EquivariantRNNCell(nn.Module):
    """S¹-equivariant recurrent cell for path integration."""
    
    def __init__(self, hidden_dim):
        super().__init__()
        # Parameterize weights to ensure S¹ equivariance
        # Use group-equivariant convolutions or constrained weight matrices
        self.hidden_dim = hidden_dim
        
    def forward(self, x, h):
        # x: velocity input (breaks equivariance → drives motion)
        # h: hidden state (transforms under S¹ action)
        
        # Equivariant update: h' = R(θ) · h when x = 0
        # Input-dependent: h' = f(h, x) with f(g·h, g·x) = g·f(h, x)
        
        return h_new
    
    def check_equivariance(self, h, angle):
        """Verify S¹ equivariance numerically."""
        # Rotate hidden state
        h_rotated = self.rotate_state(h, angle)
        
        # Forward pass
        h_next = self.forward(x=0, h=h)
        h_next_rotated = self.forward(x=0, h=h_rotated)
        
        # Check: f(g·h) = g·f(h)
        expected = self.rotate_state(h_next, angle)
        error = torch.norm(h_next_rotated - expected)
        return error.item()

# Verification workflow
cell = EquivariantRNNCell(hidden_dim=64)

# 1. Check equivariance error (should be ~1e-8)
eq_error = cell.check_equivariance(h, angle=0.1)
assert eq_error < 1e-7, "Equivariance broken!"

# 2. Compute Lyapunov exponents along group tangent
# Use Jacobian-vector products along S¹ direction
lyap_exponents = compute_group_tangent_lyapunov(cell)
assert torch.allclose(lyap_exponents[:1], torch.zeros(1), atol=1e-6)
```

**Pseudo-gap analysis for broken symmetry:**
```python
# When equivariance is slightly broken (ε ≠ 0):
# Protected mode acquires pseudo-gap λ ≈ O(ε)
# Memory lifetime τ ≈ 1/|λ|

def estimate_memory_lifetime(equivariance_error):
    """Predict finite memory lifetime from broken symmetry."""
    pseudo_gap = equivariance_error  # First-order approximation
    if pseudo_gap > 0:
        return 1.0 / pseudo_gap
    return float('inf')  # Perfect symmetry → infinite memory
```

## Applications
- **Path integration**: S¹-equivariant cells for navigation without drift
- **Continuous working memory**: T^q-equivariant networks for multi-dimensional storage
- **Head direction cells**: Rotational symmetry in spatial cognition models
- **Phase coding**: Oscillatory representations with symmetry guarantees
- **Robust attractor networks**: Continuous attractors that don't require fine-tuning

## Pitfalls
- **Exact equivariance required**: The theorem requires exact equivariance; numerical errors break protection
- **Input breaks symmetry**: External inputs (e.g., velocity) must be handled as symmetry-breaking terms
- **Finite precision**: Floating-point errors accumulate; use high-precision arithmetic for verification
- **Group choice matters**: Wrong symmetry group → wrong number of neutral modes
- **Stability ≠ functionality**: Zero Lyapunov exponent ensures neutral drift but doesn't guarantee useful computation

## Related Skills
- working-memory-heterogeneous-delays
- rnn-task-degradation-analysis
- self-sustained-neuron-population
- neural-population-dynamics
- heteroclinic-neural-field-cognition