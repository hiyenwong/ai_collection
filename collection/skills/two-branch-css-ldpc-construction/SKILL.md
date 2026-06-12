---
name: two-branch-css-ldpc-construction
description: >
  Methodology for constructing regular CSS QLDPC (Quantum Low-Density Parity-Check)
  base matrices using a two-branch multiplicative-coset approach over finite fields.
  Use when: (1) designing quantum error-correcting codes, (2) constructing CSS codes
  from LDPC base matrices, (3) optimizing quantum code parameters for fault-tolerant
  computation, (4) implementing belief propagation decoding for quantum codes,
  (5) analyzing finite-length quantum code performance.
  Keywords: CSS LDPC, quantum error correction, QLDPC, finite field construction,
  multiplicative coset, base matrix, cyclic lift, belief propagation, Tanner graph,
  girth constraint, logical operator, depolarizing channel.
version: 1.0.0
author: Hermes Agent
license: MIT
---

# Two-Branch CSS LDPC Construction

Methodology from arXiv:2605.23894 (Okada, Kasai, May 2026).

## Core Contribution

A two-branch multiplicative-coset construction for **regular CSS QLDPC base matrices**
that reduces regularity, CSS orthogonality, and same-type 4-cycle exclusion to explicit
quotient-coset conditions over a finite field.

## Key Design Principles

### Two-Stage Construction

The finite-length design is separated into two stages:

1. **Base Matrix Stage**: Fixes the degree distribution and the first girth constraints
   - Uses finite field algebra to construct the base matrix
   - Ensures CSS orthogonality (H_X · H_Z^T = 0 mod 2)
   - Excludes same-type 4-cycles in the Tanner graph

2. **Cyclic Lift Stage**: Randomizes edge connections subject to exact algebraic checks
   - Applies a cyclic lift (e.g., 64-fold) to the base matrix
   - Ensures the lifted code maintains girth constraints
   - Excludes specific logical operator supports

### Explicit Quotient-Coset Conditions

For target column weight J and even row weight L:
- Regularity condition → quotient-coset structure over finite field
- CSS orthogonality → multiplicative coset relationships
- Same-type 4-cycle exclusion → explicit algebraic constraints

## Construction Steps

### Step 1: Select Parameters
- Choose target (J, L) regular degree pair
- Select finite field size and structure
- Define quotient groups and coset representatives

### Step 2: Build Base Matrix
- Apply normalized exhaustive search for coset conditions
- Construct base matrix satisfying all constraints
- Verify: CSS orthogonality, no same-type 4-cycles

### Step 3: Cyclic Lift
- Choose lift factor N (e.g., 64)
- Apply cyclic permutation to each non-zero entry
- Verify lifted girth constraints (e.g., girth ≥ 8)
- Check for excluded logical support orbits

### Step 4: Decoding Setup
- Joint log-domain belief propagation
- Low-complexity deterministic post-processing for small residual syndromes
- Repair rules for residual patterns with 2 unsatisfied checks

## Example: (3,10)-Regular Code

- **Parameters**: J=3, L=10, 64-fold cyclic lift
- **Code**: [[10240, 4108, 10 ≤ d ≤ 32]] CSS code
- **Girth**: Same-type Tanner graphs have girth ≥ 8
- **Performance**: FER = 1.0×10⁻⁷ at depolarizing probability p=0.058
- **Decoding**: Joint BP + post-processing

## When to Use

- **Quantum error correction code design**: When constructing new QLDPC codes
- **CSS code families**: When regular degree distributions are needed
- **Finite-length code analysis**: When evaluating specific code instances
- **Decoder development**: When implementing BP decoders for quantum codes
- **Hardware-aware code design**: When code parameters must match hardware constraints

## Advantages Over Prior Methods

1. **Not tied to single degree distribution**: Works for various (J, L) pairs
2. **Explicit algebraic conditions**: Reduces search to finite field arithmetic
3. **Two-stage separation**: Base matrix and lift can be optimized independently
4. **Logical operator control**: Can explicitly exclude specific weight orbits

## Decoding Strategy

1. **Primary**: Joint log-domain belief propagation
2. **Post-processing**: Deterministic rules for small residual syndromes
3. **Repair**: Special handling for 2-unsatisfied-check residual patterns
4. **Iterative**: Re-run BP after post-processing if needed

## Related Patterns

- Distributed quantum error correction
- Syndrome decoding via factor graphs
- Quantum LDPC code families (surface codes, color codes, hypergraph product codes)
- Belief propagation and min-sum decoders for quantum codes

## Activation

CSS LDPC construction, quantum LDPC, QLDPC base matrix, multiplicative coset,
finite field code construction, cyclic lift, Tanner graph girth, belief propagation
decoding, quantum error correction code design, depolarizing channel performance
