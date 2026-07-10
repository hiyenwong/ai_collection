---
name: pauli-detecting-quantum-codes
description: "Quantum error detecting codes using Pauli group variance geometry — going beyond stabilizer codes via algebraic structure of Pauli operators. Covers variance-based code construction, Pauli weight distribution analysis, higher-than-stabilizer detection rates, and trade-offs between detection capability and code rate. Use when working on: quantum error detection (not correction), non-stabilizer codes, Pauli group geometry, variance codes, or codes with detection rates exceeding stabilizer bounds. Triggers: Pauli detecting code, variance geometry, non-stabilizer quantum code, error detection rate, quantum code construction, Pauli weight distribution, beyond stabilizer codes."
---

# Pauli-Detecting Quantum Codes via Variance Geometry

## Overview

Traditional quantum error-correcting codes (QECCs) are built from stabilizer groups — Abelian subgroups of the Pauli group. Pauli-detecting codes relax the stabilizer constraint, using the variance geometry of Pauli operators to construct codes that detect errors at rates exceeding stabilizer bounds. The key insight: the variance (second moment) of Pauli weight distributions encodes detection capability orthogonal to the commutativity structure exploited by stabilizers.

## Core Concepts

### Pauli Group Variance

For an n-qubit Pauli operator P = i^k · P₁ ⊗ P₂ ⊗ ... ⊗ Pₙ, define:

- **Weight** w(P) = number of non-identity factors
- **Variance** σ²(P, C) = E[w²] - E[w]² over code C's Pauli support

The variance captures how "spread out" the Pauli support is — codes with higher variance can distinguish more error patterns.

### Detection Rate

The detection rate for a code C detecting errors from set E:

```
d(C, E) = |{e ∈ E : e detected by C}| / |E|
```

Stabilizer codes are constrained by d(C,E) ≤ 1 - 2^{k-n} for [[n,k]] codes. Pauli-detecting codes break this bound by sacrificing the commutativity structure.

### Variance Geometry Framework

The variance geometry relates code properties to the geometric structure of Pauli operators in symplectic space:

1. Map Pauli operators to vectors in GF(2)^{2n} (symplectic representation)
2. Compute weight distribution: {w(P) : P ∈ N(C)} for normalizer N(C)
3. Variance σ² = Var[w(P)] measures code's distinguishing power
4. Higher variance → more error patterns distinguished → higher detection rate

## Methodology

### Step 1: Code Construction via Variance Maximization

```
Input: n (qubits), target detection set E
Output: Code C maximizing d(C, E)

1. Initialize: enumerate candidate code subspaces
2. For each candidate C:
   a. Compute Pauli weight distribution of N(C)
   b. Calculate σ²(C) = variance of weight distribution
   c. Compute detection rate d(C, E) against target errors
3. Select C* = argmax σ²(C) · d(C, E)
```

### Step 2: Variance-Optimized Code Families

| Family | Parameters | Detection Advantage |
|--------|-----------|-------------------|
| Variance-amplified | [[n, k, d_var]] | d_var > d_stab for same n,k |
| Hybrid detect-correct | [[n, k₁+k₂]] | Partial correction + enhanced detection |
| Asymmetric Pauli | [[n, k]]_asym | Biased error detection (X vs Z) |

### Step 3: Encoding Circuit Design

Unlike stabilizer codes (CNOT-based), Pauli-detecting codes may require:

1. **Non-Clifford gates**: T-gates or CCZ for non-stabilizer subspaces
2. **Adaptive circuits**: Mid-circuit measurements informing subsequent gates
3. **Teleported encoding**: Resource-state-based encoding avoiding direct circuit depth

### Step 4: Syndrome Extraction and Decoding

```
1. Measure Pauli observables in N(C) \ C
2. Variance-weighted decoding:
   - Weight syndrome outcomes by σ² contribution
   - ML decoding with variance-enhanced priors
3. Decision: detect (flag error) vs correct (if hybrid code)
```

## Detection vs Correction Trade-offs

| Property | Stabilizer Code | Pauli-Detecting Code |
|----------|----------------|---------------------|
| Code rate | k/n ≤ 1 - 2H(d/n) | Can exceed stabilizer bounds |
| Detection rate | ≤ 1 - 2^{k-n} | > 1 - 2^{k-n} possible |
| Correction | Full error correction | Detection-only or partial |
| Encoding overhead | Clifford circuits | May need non-Clifford |
| Decoding complexity | NP-hard in general | Variance-weighted (often simpler) |

## Implementation Guidance

### Variance Calculation

```python
import numpy as np
from itertools import product

def pauli_weight(pauli_string):
    """Weight of a Pauli operator (non-identity count)."""
    return sum(1 for p in pauli_string if p != 'I')

def code_variance(code_paulis):
    """Variance of Pauli weight distribution for a code.
    
    Args:
        code_paulis: list of Pauli strings in the code's normalizer
    Returns:
        (mean_weight, variance) tuple
    """
    weights = [pauli_weight(p) for p in code_paulis]
    return np.mean(weights), np.var(weights)

def detection_rate(code_paulis, error_set, n_qubits):
    """Compute error detection rate for Pauli-detecting code.
    
    Args:
        code_paulis: Pauli operators in normalizer
        error_set: list of error Pauli operators to detect
        n_qubits: number of qubits
    Returns:
        fraction of errors detected
    """
    detected = 0
    code_set = set(tuple(p) for p in code_paulis)
    
    for error in error_set:
        # Error detected if it anticommutes with some normalizer element
        for cp in code_paulis:
            if anticommutes(error, cp, n_qubits):
                detected += 1
                break
    
    return detected / len(error_set)

def anticommutes(p1, p2, n):
    """Check if two Pauli operators anticommute."""
    phase = 0
    for i in range(n):
        phase += _commutation_phase(p1[i], p2[i])
    return phase % 2 == 1

def _commutation_phase(a, b):
    """Phase contribution from single-qubit Paulis."""
    pairs = {('X','Z'), ('Z','X'), ('X','Y'), ('Y','X'), ('Y','Z'), ('Z','Y')}
    return 1 if (a, b) in pairs else 0
```

### Variance-Weighted Decoder

```python
def variance_weighted_decode(syndrome, code_paulis, error_prior):
    """Decode syndrome using variance-weighted likelihood.
    
    Args:
        syndrome: measurement outcomes
        code_paulis: normalizer Pauli operators
        error_prior: prior distribution over errors
    Returns:
        most likely error or detection flag
    """
    _, var = code_variance(code_paulis)
    weights = {e: prior * np.exp(var * similarity(e, syndrome))
               for e, prior in error_prior.items()}
    
    best_error = max(weights, key=weights.get)
    
    if weights[best_error] > DETECTION_THRESHOLD:
        return best_error  # correctable
    else:
        return "DETECTED"  # flag as detected but uncorrectable
```

## Key Metrics

| Metric | Target | Notes |
|--------|--------|-------|
| Detection rate improvement | >10% over stabilizer | For same [[n,k]] |
| Variance σ² | Maximize | Higher = better detection |
| Encoding depth | <3n | Non-Clifford overhead |
| False positive rate | <0.1% | Critical for NISQ |
| Decoding time | O(n²) | Variance-weighted is fast |

## Application Domains

1. **NISQ-era error mitigation**: Detect errors without full correction overhead
2. **Quantum communication**: High-rate detection for channel monitoring
3. **Verification protocols**: State verification with improved confidence
4. **Hybrid schemes**: Detection + limited correction for resource efficiency

## Pitfalls

- Detection-only codes cannot recover from errors — must pair with retry/fallback
- Variance maximization can produce codes with poor minimum distance
- Non-stabilizer encoding circuits may introduce more errors than they detect
- Decoding is not always simpler than stabilizer decoding — depends on code structure

## References

- arXiv:2604.21800 — Pauli-detecting codes via variance geometry
- Gottesman (1997) — Stabilizer codes and quantum error correction
- Ashikhmin et al. (2000) — Quantum error detection bounds
- Rengaswamy et al. (2019) — Variance of Pauli operators in code design
