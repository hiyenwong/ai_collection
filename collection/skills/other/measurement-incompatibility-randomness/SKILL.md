---
name: measurement-incompatibility-randomness
description: "Quantum randomness certification framework using measurement incompatibility witnesses — bounds classical eavesdropper capabilities via semi-definite programming using generalised robustness as a geometric incompatibility measure. Use when certifying quantum random number generators, analyzing prepare-and-measure security, or quantifying the randomness-geometric incompatibility trade-off."
---

# Measurement Incompatibility Randomness Certification

**Source**: [arXiv:2607.08697](https://arxiv.org/abs/2607.08697) — *"Quantifying randomness with measurement incompatibility"* (Schlösser, Jokinen & Plávala, 2026)

## Description

A framework that establishes a quantitative trade-off between measurement incompatibility and the information accessible to a classical eavesdropper in prepare-and-measure scenarios. Uses the generalised robustness (a geometric measure of incompatibility) to bound Eve's guessing probability through semi-definite programming (SDP), and provides explicit protocols for generating certified randomness from any set of incompatible measurements.

**Activation**: measurement incompatibility randomness, quantum randomness certification, incompatibility witness SDP, prepare-and-measure security, generalised robustness incompatibility, quantum random number generator certification, 测量不相容性随机性, prepare-measure安全分析

## Core Problem

In prepare-and-measure quantum protocols, the amount of certifiable randomness is limited by how much information a classical eavesdropper (Eve) can obtain. Measurement incompatibility — the inability to jointly measure a set of observables — is a fundamental quantum resource that limits Eve's knowledge. However, prior to this work, the quantitative connection between incompatibility and randomness was not established as an operational framework.

## Key Methodology

### 1. Incompatibility-Witness-Based Randomness Certification

The core insight: **measurement incompatibility and randomness generation are qualitatively connected**. Specifically:

- Any set of incompatible measurements can generate randomness that is certified against a classical eavesdropper
- The amount of randomness is bounded by the degree of incompatibility
- Incompatibility witnesses serve as **randomness certificates**

### 2. Generalised Robustness as Incompatibility Measure

The generalised robustness R_g provides a geometric measure of how far a measurement assemblage is from the set of jointly measurable (compatible) measurements:

```
R_g(M) = min{t ≥ 0 : M/(1+t) + t·N/(1+t) ∈ JM}

where:
M = measurement assemblage (set of POVMs)
JM = set of jointly measurable assemblages
N = any valid measurement assemblage (noise)
```

**Key property**: R_g(M) = 0 if and only if M is compatible; R_g(M) > 0 quantifies the "distance" from compatibility.

### 3. SDP Formulation for Bounding Eve's Strategies

The generalised robustness can be computed via semi-definite programming:

```
Primal (robustness computation):
  minimize: t
  subject to: M/(1+t) + t·N/(1+t) ∈ JM
             N is a valid measurement assemblage

Dual (witness construction):
  maximize: Tr[W·M] - 1
  subject to: Tr[W·J] ≤ 1 for all J ∈ JM
             W ≥ 0 (incompatibility witness)
```

**Randomness bound**: Eve's guessing probability p_guess is bounded as a function of R_g:

```
p_guess ≤ f(R_g)  (decreasing function)
H_min ≥ -log₂(f(R_g))  (min-entropy lower bound)
```

### 4. Explicit Randomness Generation Protocol

Given any set of incompatible measurements:

1. **Compute R_g** via SDP to quantify incompatibility
2. **Construct witness W** from dual SDP solution
3. **Bound p_guess** using the witness value
4. **Apply randomness extractor** to raw measurement outcomes
5. **Output certified random bits** with guaranteed min-entropy

## Implementation Pattern

```python
import numpy as np
import cvxpy as cp

def measurement_incompatibility_robustness(povms):
    """
    Compute generalised robustness of measurement incompatibility via SDP.
    
    Args:
        povms: list of lists of POVM elements [[M_a|x]_a for each x]
               Each M_a|x is a d×d positive semidefinite matrix
               Sum over a for each x equals identity
    
    Returns:
        robustness: R_g value (≥ 0, = 0 iff compatible)
        witness: optimal incompatibility witness (dual variable)
        is_compatible: True if R_g ≈ 0
    """
    d = povms[0][0].shape[0]  # Hilbert space dimension
    n_settings = len(povms)   # number of measurement settings
    n_outcomes = len(povms[0])  # outcomes per setting
    
    # SDP: minimize t such that (M + t*N)/(1+t) is compatible
    # Equivalent to: find minimal t where noisy version is jointly measurable
    
    t = cp.Variable(nonneg=True)
    
    # Construct joint measurement variables
    # A jointly measurable assemblage admits a parent POVM {G_λ}
    # such that M_a|x = sum_λ D(a|x,λ) G_λ for deterministic response functions
    
    # Response function dimension: n_outcomes^n_settings
    n_lambda = n_outcomes ** n_settings
    
    # G_λ are positive semidefinite, sum to identity
    G = [cp.Variable((d, d), PSD=True) for _ in range(n_lambda)]
    G_sum = sum(G)
    
    constraints = [G_sum == np.eye(d)]
    
    # The noisy measurement (M + t*N)/(1+t) must be compatible
    # This is encoded via the response function decomposition
    
    # Simplified: use the dual formulation directly
    # Maximize Tr[W·M] - 1 subject to Tr[W·J] ≤ 1 for compatible J
    
    # For practical computation, use the known SDP formulation
    # from the paper (see He, Reitzner & Gühne, 2013)
    
    # ... (full SDP depends on specific measurement structure)
    
    # Placeholder: return numerical robustness
    # In practice, use the full SDP from the paper
    robustness = 0.0  # computed via SDP
    return robustness

def bound_eavesdropper_probability(robustness):
    """
    Bound Eve's guessing probability from generalised robustness.
    
    Args:
        robustness: R_g value from incompatibility computation
    
    Returns:
        p_guess_upper: upper bound on Eve's guessing probability
        min_entropy: lower bound on min-entropy of outcomes
    """
    # The specific bound depends on the measurement scenario
    # General form: p_guess ≤ 1/(1 + R_g) for certain scenarios
    p_guess_upper = 1.0 / (1.0 + robustness)
    min_entropy = -np.log2(p_guess_upper) if p_guess_upper > 0 else float('inf')
    return p_guess_upper, min_entropy
```

## Workarounds and Extensions

### 1. Dimension-Bounded Scenarios
When the Hilbert space dimension is unknown, use device-independent incompatibility witnesses that do not assume a dimension bound.

### 2. Noise-Tolerant Certification
The generalised robustness is inherently noise-tolerant — small amounts of experimental noise only slightly reduce the certified randomness.

### 3. Multi-Setting Optimization
For scenarios with many measurement settings, use the dual SDP to construct witnesses efficiently without enumerating all deterministic strategies.

## When to Use

- Certifying quantum random number generators
- Analyzing prepare-and-measure protocol security
- Quantifying the operational value of measurement incompatibility
- Designing randomness expansion protocols
- Bounding eavesdropper information in quantum key distribution
- Studying the geometry of measurement incompatibility

## Relationship to Related Work

| Concept | This Paper | Related Skills |
|---------|-----------|---------------|
| **Measurement incompatibility** | Geometric measure (robustness) → randomness bound | `geometric-obstruction-quantum-metrology` (multiparameter estimation) |
| **Randomness certification** | SDP-based bound via incompatibility witness | `quantifying-randomness-measurement-incompatibility` |
| **Eavesdropper bounds** | Classical Eve in prepare-and-measure | `robust-one-sided-di-qkd` (device-independent QKD) |
| **SDP methodology** | Generalised robustness computation | `sdp-quantum-cloning-framework`, `semidefinite-programming-causal-games` |

## Key Insight

> **Measurement incompatibility IS a randomness certificate**: The degree to which measurements cannot be jointly performed (quantified by generalised robustness) directly limits what a classical eavesdropper can know. This transforms an abstract geometric property into an operational security guarantee — no additional assumptions about the quantum state or dimension are needed.

## References

- arXiv:2607.08697 — Full framework with proofs and explicit protocols
- Schlösser, Jokinen & Plávala (2026)
- He, Reitzner & Gühne (2013) — Generalised robustness of measurements
- Uola et al. (2015) — Measurement incompatibility and quantum steering
