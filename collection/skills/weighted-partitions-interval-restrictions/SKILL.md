---
name: weighted-partitions-interval-restrictions
description: "Exact formulas and bivariate master identity methodology for weighted partitions with interval restrictions. Use when: deriving generating functions for restricted partition functions, proving partition coefficient bounds via Rogers-Fine evaluation, establishing master identities with auxiliary variables, or analyzing quantum modular forms from interval-restricted partitions. Activation: weighted partitions, interval restrictions, bivariate master identity, Rogers-Fine evaluation, false theta partition, Andrews El Bachraoui, partition coefficient bounds, quantum modular partition"
metadata:
  arxiv_id: "2606.11011"
  published: "2026-06-09"
  authors: "George E. Andrews, Mohamed El Bachraoui, Aritram Dhar, Ankush Goswami, Runqiao Li"
---

# Weighted Partitions with Interval Restrictions

**Source**: arXiv:2606.11011 — "Weighted partitions with interval restrictions: exact formulas and a bivariate master identity" by Andrews et al. (2026-06-09)

## Overview

Proves two conjectures for signed partition functions a₂''(n) and b₂''(n) introduced by Andrews and El Bachraoui for interval-restricted partitions. Central result: bivariate master identity with auxiliary variable z recording number of non-compulsory parts.

## Core Methodology

### Partition Functions with Interval Restrictions

- **a₂''(n)**: Signed partition function where parts > 1 are controlled by smallest even part
- **b₂''(n)**: Companion coefficients taking values only in {-1, 0, 1, 2}

### Bivariate Master Identity

Introduce auxiliary variable z tracking non-compulsory parts > 1:

```
(1 + q²)·B(z, q) - (1 + q)·A(z, q) = -q⁴/(1 - q³)
```

Where A(z, q) and B(z, q) are generating functions for a₂''(n) and b₂''(n).

### Key Techniques

1. **Analytic approach**: Rogers-Fine evaluation at z = -1 yields false theta formula
2. **Combinatorial approach**: Direct coefficient description of b₂''(n)
3. **Heine-Rogers-Fine proof**: Independent proof of the false theta formula
4. **Quantum modular interpretation**: Connection to quantum modular forms

### Results

- **Generating function for a₂''(n)**: Elementary rational term + false theta series with periodic signs
- **Coefficient range for b₂''(n)**: Proven to be exactly {-1, 0, 1, 2}
- **Exact coefficient description**: Explicit formula for each b₂''(n)

## Implementation Steps

### Step 1: Define the Partition Functions

```python
def a2_double_prime(n):
    """Signed partition function for interval-restricted partitions."""
    # Parts > 1 controlled by smallest even part
    pass

def b2_double_prime(n):
    """Companion coefficients."""
    # Values in {-1, 0, 1, 2}
    pass
```

### Step 2: Master Identity Verification

```python
def master_identity(z, q, N_terms=50):
    """Verify (1+q²)B(z,q) - (1+q)A(z,q) = -q⁴/(1-q³)."""
    # Compute series expansions of A(z,q) and B(z,q)
    # Check identity holds coefficient by coefficient
    pass
```

### Step 3: Rogers-Fine Evaluation

At z = -1, the identity reduces to the false theta formula for a₂''(n).

## Pitfalls

1. **Interval restriction complexity**: The constraint "parts > 1 controlled by smallest even part" creates non-trivial combinatorial structure
2. **False theta convergence**: False theta series have restricted convergence domains — analytic continuation may be needed
3. **Coefficient sign patterns**: The periodic signs in the false theta formula require careful tracking

## Activation

- weighted partitions, interval restrictions, bivariate master identity
- Rogers-Fine evaluation, false theta partition
- Andrews El Bachraoui partition
- partition coefficient bounds
- quantum modular partition
- 加权分拆, 区间限制分拆, Rogers-Fine求值
