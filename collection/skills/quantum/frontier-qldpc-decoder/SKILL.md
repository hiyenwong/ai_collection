---
name: frontier-qldpc-decoder
description: "Frontier decoder for quantum LDPC codes — pruned dynamic-programming approach with narrow frontier syndrome decoding. Uses prefix merging with same residual syndrome and logical label, approximates logical-coset posteriors by retaining scored frontier. Achieves near-optimal thresholds for surface code and color code with linear complexity at constant list size. arXiv:2606.20513. Activates: qldpc decoding, frontier decoder, quantum error correction, sparse quantum decoding, syndrome decoding, dynamic programming QEC, narrow frontier."
metadata:
  arxiv_id: "2606.20513"
  published: "2026-06-18"
  authors: "Anthony Leverrier, Rüdiger Urbanke"
  tags: ["quantum", "qec", "qldpc", "decoding", "dynamic-programming", "syndrome"]
---

## Context

Anthony Leverrier and Rüdiger Urbanke introduce the **Frontier decoder**, a pruned dynamic-programming decoder for sparse quantum decoding problems that achieves near-optimal performance with linear complexity.

## Core Methodology

1. **Process error variables** in a chosen order via dynamic programming recursion
2. **Merge prefixes** sharing the same residual syndrome and logical label (key compression step)
3. **Approximate logical-coset posterior masses** by retaining only a narrow scored frontier
4. **Without pruning**: recursion is exact ordered inference with exponential complexity
5. **With pruning**: maintains bounded list size → linear complexity

## Key Results

- **Surface code + color code**: thresholds close to optimal in code-capacity setting
- **Circuit-level noise**: state-of-the-art performance with average retained list < 100 for gross code at p = 0.001
- **Complexity**: linear when list size is constant → enables low-latency hardware implementations

## Implementation Steps

```python
def frontier_decode(syndrome, error_variables, max_frontier_size):
    """Pruned dynamic-programming decoder for sparse quantum codes."""
    frontier = {(): (1.0, 0)}  # (prefix -> (posterior, logical_label))
    
    for var in error_variables:
        new_frontier = {}
        for prefix, (prob, logical) in frontier.items():
            for val in [0, 1]:  # binary error variable
                new_prefix = prefix + (val,)
                new_syndrome = compute_residual_syndrome(new_prefix)
                new_logical = compute_logical_label(new_prefix)
                key = (new_syndrome, new_logical)
                new_prob = prob * error_prob(var, val)
                
                if key in new_frontier:
                    new_frontier[key] = (new_frontier[key][0] + new_prob, new_logical)
                else:
                    new_frontier[key] = (new_prob, new_logical)
        
        # Prune: retain only top-k by posterior mass
        frontier = dict(sorted(new_frontier.items(), 
                               key=lambda x: x[1][0], reverse=True)[:max_frontier_size])
    
    return select_most_likely_logical(frontier)
```

## Pitfalls

- **Ordering matters**: error variable processing order affects pruning efficiency
- **Frontier size tuning**: too small → accuracy loss; too large → exponential blowup
- **Circuit-level vs code-capacity**: circuit-level noise requires larger frontiers
- **Syndrome collision**: merging assumes same residual syndrome + logical label = equivalent prefixes

## Verification

- Test on surface code with depolarizing noise → should approach optimal threshold
- Verify list size remains bounded across decoding rounds
- Compare logical error rate vs brute-force for small codes

## Activation

qldpc decoding, frontier decoder, quantum error correction, sparse quantum decoding, syndrome decoding, dynamic programming QEC, narrow frontier, Leverrier Urbanke, linear complexity decoder
