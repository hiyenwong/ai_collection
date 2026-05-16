---
name: quantum-ldpc-decoding-optimization
description: "Quantum LDPC code design and decoding optimization methodology. Covers Univariate Bicycle codes, Multiple-Bases Belief Propagation List Decoding, and structured decoding diversity for QLDPC codes (arXiv:2605.14173, 2605.14170)."
---

# Quantum LDPC Code Design and Decoding Optimization

## Description
A methodology for designing and decoding quantum Low-Density Parity-Check (QLDPC) codes, combining:
1. **Univariate Bicycle (UB) codes**: Structured QLDPC subclass using Frobenius relation for single-polynomial code design
2. **Multiple-Bases Belief-Propagation List Decoder (MBBP-LD)**: Structured decoding diversity via cycle-free subtree decompositions

Based on: Rabeti & Mahdavifar (2026) — arXiv:2605.14173, 2605.14170

## Activation Keywords
- quantum LDPC codes
- QLDPC decoding
- bicycle codes quantum
- belief propagation list decoding
- MBBP-LD decoder
- univariate bicycle codes
- quantum error correction LDPC
- structured decoding diversity

## Tools Used
- exec: Run QEC simulations, BP decoding
- write: Save decoder implementations
- read: Load code specifications, syndrome data

## Part 1: Univariate Bicycle (UB) Codes

### Construction
UB codes are a structured subclass of Generalized Bicycle (GB) quantum LDPC codes:

```
GB codes: Two polynomials (a(x), b(x)) → H = [A|B]
UB codes: Single polynomial via Frobenius relation → H = [A|A^q]
```

**Key advantage**: Reduces code design space from 2-polynomial search to 1-polynomial search while preserving sparsity.

### Algebraic Structure
1. **Frobenius Relation**: H = [A | A^q] where A^q is Frobenius image
2. **Logical Coset Space**: Explicit basis construction for logical quotient space
3. **Distance Bounds**: Upper bounds via cycle-density properties of circulant matrices

### Design Steps
```
Step 1: Choose block length n (hundreds to ~10^3)
Step 2: Select single polynomial g(x) over GF(q)
Step 3: Construct parity check: H = [circ(g) | circ(g)^q]
Step 4: Verify CSS commutation: H_X · H_Z^T = 0
Step 5: Optimize: minimize weight, maximize distance
Step 6: Bound distance: analyze cycle-density of circulants
```

## Part 2: Multiple-Bases Belief-Propagation List Decoding (MBBP-LD)

### Core Idea
Generate **structured decoding diversity** by:
1. Constructing multiple redundant parity-check representations
2. Using cycle-free subtree decompositions of Tanner graph
3. Running BP decoding in parallel across representations

### Algorithm
```
Step 1: Given QLDPC code H and syndrome s
Step 2: Decompose Tanner graph into cycle-free subtrees
Step 3: For each subtree decomposition:
   a. Construct redundant parity-check matrix H_i
   b. Run standard BP decoding with (H_i, s)
   c. Collect candidate codewords
Step 4: List combination:
   a. Merge candidate lists from all bases
   b. Select best candidate (minimum weight error)
Step 5: Output: corrected error pattern
```

### Complexity
- **Linear-time**: Same as standard BP per base
- **Parallelizable**: All bases decoded simultaneously
- **No super-linear post-processing**: Unlike traditional list decoders

### Advantages over Standard BP
1. **Trapping set avoidance**: Multiple bases break harmful structures
2. **Improved error floor**: Better performance at low error rates
3. **No overhead increase**: Linear complexity preserved

## Implementation Notes

### Tanner Graph Decomposition
```python
def decompose_tanner_graph(H):
    """Decompose Tanner graph into cycle-free subtrees."""
    # Find spanning forest
    # Each tree gives a redundant parity-check representation
    subtrees = []
    for cycle_free_subgraph in find_cycle_free_decompositions(H):
        H_redundant = construct_redundant_parity_check(cycle_free_subgraph)
        subtrees.append(H_redundant)
    return subtrees
```

### BP Decoding
```python
def bp_decode(H, syndrome, max_iter=100):
    """Standard belief propagation for QLDPC."""
    # Initialize messages
    # Iterate: check nodes → variable nodes → check nodes
    # Return: most likely error pattern
    return error_estimate
```

## Applications
1. **Surface code alternatives**: UB codes can match [[1201,1,25]] surface code performance at smaller block lengths
2. **Fault-tolerant quantum computing**: Efficient QEC for NISQ and beyond
3. **Quantum memory**: Long-lived quantum storage with active correction

## Performance Benchmarks
- UB codes [[256,2]] and [[512,2]] achieve logical error rates comparable to [[1201,1,25]] surface code
- MBBP-LD improves error floor by 1-2 orders of magnitude over standard BP

## Error Handling
- If no good polynomial found: expand search space or increase block length
- If BP fails to converge: increase max iterations or try different bases
- For degenerate codes: handle multiple minimum-weight errors

## References
- Rabeti & Mahdavifar (2026): arXiv:2605.14173 (UB codes)
- Rabeti & Mahdavifar (2026): arXiv:2605.14170 (MBBP-LD)
- Panteleev & Kalachev (2022): Asymptotically good QLDPC codes
- Kovalev & Pryadko (2012): GB codes

## Related Skills
- quantum-error-correction-methods
- syndrome-adaptive-gain-qldpc
- distributed-quantum-error-correction