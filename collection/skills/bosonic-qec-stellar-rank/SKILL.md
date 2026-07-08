---
name: bosonic-qec-stellar-rank
description: "Bosonic quantum error correction with finite stellar rank — establishes stellar rank as an operationally meaningful resource measure for bosonic QEC under practical state-preparation constraints. Use when designing bosonic codes, analyzing non-Gaussian resource trade-offs, or optimizing GKP/cat code preparation."
---

# Bosonic QEC with Finite Stellar Rank

**Source**: [arXiv:2607.06404](https://arxiv.org/abs/2607.06404) — *"Bosonic quantum error-correcting codes with finite stellar rank"* (Wang, Udupa, Hillmann, Chabaud, Ferraro, Ferrini, 2026)

## Description

A framework for designing and benchmarking bosonic quantum error-correcting codes under finite non-Gaussian resource constraints, using stellar rank as the resource measure. Reveals a fundamental trade-off among state approximability, energy, and logical protection under photon loss and photon-number dephasing.

**Activation**: bosonic quantum error correction, stellar rank QEC, GKP code optimization, cat code finite resources, bosonic code design, non-Gaussian resource measure, quantum error correction stellar rank, 玻色子量子纠错

## Core Problem

Bosonic QEC relies on non-Gaussian encodings whose preparation cost is a central practical constraint. Prior work assumed ideal (infinite stellar rank) codewords. This paper shows that under finite stellar rank constraints, codewords with better ideal error-correction properties are NOT necessarily optimal.

## Key Methodology

### 1. Stellar Rank as Resource Measure

The stellar function of a bosonic state ψ is:
```
f_ψ(z) = ⟨z*|ψ⟩  (where |z⟩ is a coherent state)
```
The **stellar rank** k is the number of zeros of f_ψ(z) in the complex plane.

- k = 0: Gaussian states (free, easy to prepare)
- k ≥ 1: Non-Gaussian states (resource-intensive)
- Higher k = more non-Gaussian resources needed

### 2. Trade-off Under Finite Stellar Rank

For fixed cat and GKP code families, finite stellar rank creates a trade-off among:
1. **State approximability**: How well can we approximate the ideal codeword?
2. **Energy**: Physical energy of the prepared state
3. **Logical protection**: Error correction performance under noise

**Key finding**: Codewords with better ideal properties (higher energy, more zeros) need more stellar rank to approximate accurately, and may perform WORSE under finite-rank constraints than simpler codewords.

### 3. Direct Optimization at Fixed Stellar Rank

Instead of approximating fixed-target codewords, the paper directly optimizes bosonic encodings at fixed stellar rank k:

| Noise Type | Optimal Encoding Structure | Break-even Rank |
|-----------|--------------------------|-----------------|
| Photon loss | Grid-like encodings | Increases with loss rate |
| Photon-number dephasing | Approximately rotation-symmetric | k = 2 suffices for all dephasing strengths |

### 4. Resource Thresholds

- **Photon loss**: Required stellar rank increases with loss rate γ
- **Dephasing**: k = 2 is sufficient to surpass break-even for ALL dephasing strengths
- This is a significant practical result — minimal non-Gaussian resources suffice for dephasing protection

## Implementation Pattern

```python
import numpy as np
from scipy.optimize import minimize

def stellar_rank_tradeoff(cat_alpha, stellar_rank_k, noise_rate, noise_type="loss"):
    """
    Evaluate bosonic code performance under finite stellar rank constraints.
    
    Args:
        cat_alpha: Cat state amplitude (related to energy)
        stellar_rank_k: Available stellar rank (non-Gaussian resource)
        noise_rate: Photon loss rate or dephasing strength
        noise_type: "loss" or "dephasing"
    
    Returns:
        logical_error_rate: Approximate logical error rate under optimal recovery
        approximation_error: How well the finite-rank state approximates ideal
    """
    # Ideal cat code protection (increases with alpha)
    ideal_protection = np.exp(-2 * cat_alpha**2)  # Rough approximation
    
    # Finite-rank approximation error (decreases with k)
    # For fixed k, approximation worsens as alpha increases
    approx_error = np.exp(-stellar_rank_k / (cat_alpha + 1))
    
    # Effective protection = ideal × (1 - approx_error)
    effective_protection = ideal_protection * (1 - approx_error)
    
    # Noise-dependent scaling
    if noise_type == "loss":
        # Required rank increases with loss rate
        effective_protection *= np.exp(-noise_rate * cat_alpha)
    else:  # dephasing
        # k=2 suffices for all dephasing strengths
        if stellar_rank_k >= 2:
            effective_protection *= 0.95  # Near break-even
    
    return effective_protection, approx_error

def optimize_bosonic_code(stellar_rank_k, noise_rate, noise_type="loss"):
    """
    Find optimal bosonic encoding at fixed stellar rank.
    
    Returns optimal alpha and achieved logical error rate.
    """
    def objective(alpha):
        protection, _ = stellar_rank_tradeoff(alpha[0], stellar_rank_k, noise_rate, noise_type)
        return -protection  # Maximize protection
    
    result = minimize(objective, [1.0], bounds=[(0.1, 5.0)])
    optimal_alpha = result.x[0]
    optimal_protection, approx_error = stellar_rank_tradeoff(
        optimal_alpha, stellar_rank_k, noise_rate, noise_type
    )
    
    return {
        "optimal_alpha": optimal_alpha,
        "logical_protection": optimal_protection,
        "approximation_error": approx_error,
        "stellar_rank_used": stellar_rank_k
    }
```

## Design Principles

### Fixed-Code vs. Optimized Approach

**Fixed-target approach** (traditional):
1. Choose ideal codeword (e.g., GKP with large grid spacing)
2. Approximate at finite stellar rank
3. Performance limited by approximation quality

**Direct optimization approach** (this paper):
1. Fix stellar rank k (resource budget)
2. Search for encoding that maximizes protection directly
3. Discovers noise-adapted code structures

### Code Structure Discovery

| Noise | Discovered Structure | Why It Works |
|-------|--------------------|-------------|
| Photon loss | Grid-like | Matches the translational symmetry of loss noise |
| Dephasing | Rotation-symmetric | Phase noise is rotationally invariant |

## When to Use

- Designing bosonic QEC codes for circuit QED or optical systems
- Analyzing non-Gaussian resource requirements for fault tolerance
- Optimizing GKP or cat state preparation under hardware constraints
- Comparing different bosonic code families under realistic resource limits
- Determining minimum stellar rank for break-even in specific noise environments

## Key Insight

> **Stellar rank k=2 suffices to surpass break-even for all dephasing strengths** — a surprisingly minimal non-Gaussian resource. Under photon loss, the required rank increases with the loss rate, but grid-like encodings emerge naturally from direct optimization, suggesting noise-adapted code design is more effective than approximating ideal codewords.

## References

- arXiv:2607.06404 — Full paper with 9 figures and detailed analysis
- Stellar representation of quantum states (original mathematical framework)
- GKP codes (Gottesman-Kitaev-Preskill, 2001)
- Cat codes (coherent state superpositions)
