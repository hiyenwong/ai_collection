---
name: affine-subcode-ensemble-decoding
description: "Affine Subcode Ensemble Decoding methodology for degeneracy-aware quantum error correction. Extends affine subcode ensemble decoding from classical to quantum LDPC codes, using overcomplete matrices and appended linearly independent rows to reduce degenerate solution search space. Use when working with quantum error correction decoding, belief propagation on QLDPC codes, degeneracy-aware decoding, toric codes, generalized bicycle codes, or Monte-Carlo simulation of quantum code performance."
---

# Affine Subcode Ensemble Decoding for Quantum Error Correction

## Overview

Quantum LDPC (low-density parity-check) codes are promising candidates for low-overhead fault-tolerant quantum computing, but **degeneracy** impairs convergence of belief-propagation (BP) decoding. This methodology extends **affine subcode ensemble decoding** from classical to quantum settings, using overcomplete matrices to reduce the degenerate solution search space.

## Core Technique

### The Degeneracy Problem

In quantum stabilizer codes, multiple distinct error patterns can produce the same syndrome (degeneracy). BP decoders converge poorly because they cannot distinguish between degenerate solutions.

### Solution: Check Matrix Augmentation

Append **linearly independent rows** to the stabilizer check matrix to constrain the search space:

1. Start with original check matrix `H` of size `m × n`
2. Find `k` linearly independent rows that are in the dual of the code but not in the row space of `H`
3. Append these rows to create an **overcomplete matrix** `H'` of size `(m+k) × n`
4. Run BP decoding on `H'` — the augmented constraints reduce degeneracy ambiguity

### Affine Subcode Ensemble Decoding

```
For each decoding path i = 1, ..., M:
  1. Sample a random subset of augmented constraints
  2. Run BP decoding with the selected constraints
  3. Record the decoded error pattern
  4. Weight results by constraint consistency

Final result = weighted majority vote across all paths
```

## Algorithm Steps

### Step 1: Matrix Augmentation

```python
def augment_check_matrix(H, num_extra_rows):
    """Augment stabilizer check matrix with linearly independent rows."""
    import numpy as np
    from scipy.sparse import vstack
    
    # Find rows in dual space not in row(H)
    null_space = find_null_space(H)  # Over GF(2)
    extra_rows = null_space[:num_extra_rows]
    
    return vstack([H, extra_rows])
```

### Step 2: Ensemble Decoding

```python
def affine_subcode_decode(syndrome, H_aug, num_paths=8, bp_iterations=50):
    """Affine subcode ensemble decoding for quantum codes."""
    results = []
    
    for _ in range(num_paths):
        # Randomly select subset of augmented constraints
        mask = random_constraint_selection(H_aug)
        H_sub = H_aug[mask]
        syndrome_sub = syndrome[mask]
        
        # Run BP on sub-problem
        error_pattern = belief_propagation(H_sub, syndrome_sub, 
                                            max_iter=bp_iterations)
        results.append(error_pattern)
    
    return majority_vote(results)
```

## Key Results

- Tested on **toric codes** and **generalized bicycle codes**
- Improved BP convergence rates
- Reduced logical error rates compared to standard BP
- Overcomplete matrices per decoding path further boost performance

## When to Use

- Decoding quantum LDPC codes where BP fails to converge
- Surface codes, toric codes, hypergraph product codes
- When degeneracy causes decoder ambiguity
- Monte-Carlo performance evaluation of quantum codes

## Activation Keywords

- affine subcode decoding
- degeneracy-aware quantum error correction
- QLDPC decoding
- quantum LDPC belief propagation
- quantum code ensemble decoding
- toric code decoding
- generalized bicycle code decoding
- quantum error correction overcomplete matrix
- affine subcode ensemble
- 仿射子码系综解码
- 量子纠错解码
- 退化解量子错误纠正

## Related Concepts

- **Belief Propagation (BP)**: Standard iterative decoder impaired by degeneracy
- **Stabilizer Codes**: Quantum error correcting codes defined by commuting Pauli operators
- **Overcomplete Matrix**: Redundant parity check matrix with extra constraints
- **Toric Code**: 2D topological quantum code on a torus
- **Generalized Bicycle Code**: QLDPC code with bicycle graph structure

## Resources

- **arXiv**: [2605.06547](https://arxiv.org/abs/2605.06547)
- **PDF**: [Download](https://arxiv.org/pdf/2605.06547v1)
