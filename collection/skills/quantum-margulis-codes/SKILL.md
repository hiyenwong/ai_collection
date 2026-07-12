---
name: quantum-margulis-codes
description: >
  Quantum Margulis Codes methodology for fault-tolerant quantum computation.
  A new class of QLDPC codes derived from Margulis classical LDPC construction via
  two-block group algebra (2BGA) framework. Unlike bivariate bicycle codes, these can
  be efficiently decoded with standard min-sum decoder (linear complexity) under code
  capacity noise model. Use when: QLDPC code design, quantum error correction codes,
  fault-tolerant quantum computing, LDPC code construction, girth-controlled codes,
  or min-sum quantum decoding.
---

# Quantum Margulis Codes

## Core Innovation

Quantum Margulis codes are QLDPC codes constructed from Margulis' classical LDPC
construction through the 2BGA (two-block group algebra) framework. Their key advantage:
**Tanner graph lacks group symmetry**, which mitigates error degeneracy in QLDPC decoding,
allowing efficient min-sum decoding instead of expensive ordered statistics decoding.

## Key Concepts

### 1. 2BGA Framework (Two-Block Group Algebra)

- Constructs quantum CSS codes from classical LDPC codes
- Uses group algebra structure to define X and Z check matrices
- Margulis construction provides good girth and distance properties

### 2. Why Min-Sum Works (vs. OSD for BB Codes)

- **Bivariate Bicycle (BB) codes**: Tanner graph has group symmetry → error degeneracy
  → BP/min-sum gets stuck → requires OSD
- **Margulis codes**: Tanner graph breaks group symmetry → less degeneracy →
  min-sum decoder with linear complexity works efficiently

### 3. Girth-Controlled Construction

- Algorithm to construct 2BGA codes with controlled girth (minimum 6 or 8)
- Higher girth → fewer short cycles → better BP/min-sum performance
- Validated codes at lengths 240 and 642

### 4. Error Floor Performance

- Quantum Margulis codes significantly outperform BB codes in error floor region
- Under min-sum decoding: 2-8 orders of magnitude better error floor
- Critical for fault-tolerant thresholds

## Code Construction Steps

```
def construct_quantum_margulis(girth_target=8):
    """
    Construct quantum Margulis code with target girth.
    
    Returns H_X, H_Z check matrices for CSS code.
    """
    # Start with Margulis base construction
    # Margulis graph: (Z_2 x Z_2 x Z_2, specific edge rules)
    base_graph = margulis_construction()
    
    # Lift to 2BGA framework
    # H_X = [A | B] structure from group algebra
    # H_Z = [B^T | A^T] (CSS dual structure)
    H_X, H_Z = lift_to_2bga(base_graph)
    
    # Enforce girth constraint
    # Remove edges that create short cycles
    H_X, H_Z = enforce_girth(H_X, H_Z, min_girth=girth_target)
    
    # Verify CSS commutation: H_X @ H_Z^T = 0
    assert (H_X @ H_Z.T) % 2 == 0
    
    return H_X, H_Z
```

## Decoder: Min-Sum for Margulis Codes

```
def min_sum_decode(syndrome, H, max_iterations=100):
    """
    Standard min-sum decoder works well for Margulis codes
    (unlike BB codes which need OSD).
    """
    # Initialize messages
    msg_v2c = zeros(n, m)  # variable to check
    msg_c2v = zeros(m, n)  # check to variable
    
    for iteration in range(max_iterations):
        # Check node update (min-sum rule)
        for j in range(m):  # check nodes
            for i in H[j].nonzero():  # connected variables
                # Min of absolute values, sign product
                msgs = [abs(msg_v2c[k, j]) for k in H[j].nonzero() if k != i]
                signs = [sign(msg_v2c[k, j]) for k in H[j].nonzero() if k != i]
                msg_c2v[j, i] = prod(signs) * min(msgs)
        
        # Variable node update
        for i in range(n):
            for j in H[i].nonzero():  # connected checks
                msg_v2c[i, j] = llr[i] + sum(msg_c2v[k, i] for k in H[i].nonzero() if k != j)
        
        # Estimate
        estimate = [1 if llr[i] + sum(msg_c2v[j, i] for j in H[i].nonzero()) < 0 else 0
                    for i in range(n)]
        
        if syndrome_check(estimate, H, syndrome):
            return estimate
    
    return estimate  # Best effort
```

## When to Use

- **High-rate QLDPC codes**: Need good encoding rate with low decoding complexity
- **Error floor regime**: Operating at low physical error rates where BB codes struggle
- **Resource-constrained decoding**: Cannot afford OSD complexity
- **Hardware implementation**: Min-sum is highly parallelizable and hardware-friendly

## Key Parameters

| Parameter | Description | Typical Value |
|-----------|-------------|---------------|
| Code length | Number of physical qubits | 240, 642, ... |
| Girth | Minimum cycle length in Tanner graph | 6 or 8 |
| Rate | Encoding rate (logical/physical) | ~0.1-0.5 |
| Decoder | Min-sum iterations | 50-200 |

## Pitfalls

- **Girth enforcement may reduce rate**: Higher girth = fewer edges = lower rate
- **Not universal**: Margulis construction works for specific code families
- **Code capacity only**: Results validated under code capacity model; circuit-level noise may differ
- **Length constraints**: Not all code lengths are achievable with Margulis construction

## Comparison with Other QLDPC Codes

| Property | Margulis | BB Codes | Hypergraph Product |
|----------|----------|----------|-------------------|
| Decoder | Min-sum | OSD required | OSD required |
| Complexity | Linear | High | High |
| Error floor | Excellent | Poor | Moderate |
| Girth control | Yes | Limited | Limited |

## References

- arXiv:2503.03936 "Construction and Decoding of Quantum Margulis Codes"
  (Pacenti, Chytas, Vasic; revised May 2026, accepted in Quantum)
