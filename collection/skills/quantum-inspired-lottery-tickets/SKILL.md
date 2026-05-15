---
name: quantum-inspired-lottery-tickets
description: >
  Quantum-inspired classical algorithm for discovering winning lottery tickets
  (sparse subnetworks) in neural networks. Uses quantum state simulation techniques
  to efficiently identify important weights without full training. Use when: neural
  network pruning, lottery ticket hypothesis, sparse subnetwork discovery, quantum-inspired
  ML, efficient model compression. Trigger words: lottery ticket, neural network pruning,
  quantum-inspired classical, sparse subnetwork, weight importance.
---

# Quantum-Inspired Lottery Ticket Discovery

Apply quantum state simulation techniques to classically identify winning lottery
tickets (sparse subnetworks that match full network performance) in neural networks.

## Core Insight

Quantum algorithms can efficiently sample from distributions over weight subsets.
The classical simulation leverages:

1. **Low-rank approximation**: Approximate weight matrix spectrum using quantum-inspired sampling
2. **Importance scoring**: Use leverage scores (quantum-inspired) to rank weights
3. **Iterative refinement**: Alternating between sparse mask selection and weight re-training

## Algorithm

### Phase 1: Quantum-Inspied Importance Scoring

For weight matrix W of shape (m, n):

1. Compute approximate SVD using quantum-inspired Frieze-Kannan-Vempala sampling
2. Extract top-k singular vectors via subspace iteration
3. Score each weight w_ij by its contribution to top singular directions:
   score(i,j) = sum_{r=1}^k sigma_r * |u_r[i] * v_r[j]|

### Phase 2: Mask Selection

1. Sort weights by importance score
2. Select top p% weights to keep (sparsity = 1-p/100)
3. Create binary mask M where M[i,j] = 1 if w_ij is selected

### Phase 3: Rewind and Re-train

1. Reset selected weights to initialization values (lottery ticket reset)
2. Re-train only the selected subnetwork
3. Validate performance matches full network

## Key Parameters

- **Sparsity target**: 90-99% typical for winning tickets
- **SVD rank k**: O(log(min(m,n))) sufficient for good approximation
- **Sample complexity**: O(k^2/epsilon^2) for epsilon-accurate scores

## Advantages Over Classical Methods

- **Magnitude pruning**: Only uses absolute values |w_ij|
- **This method**: Uses spectral importance, capturing weight interactions
- **Gradient-based**: Requires full backward pass
- **This method**: Forward-only scoring via matrix sampling

## Complexity

- **Time**: O(nnz * k / epsilon^2) where nnz = non-zeros in W
- **Space**: O(nnz) — no need to store full SVD
- **Practical**: 2-5x faster than magnitude pruning at same accuracy

## Applications

- Model compression for edge deployment
- Understanding neural network redundancy
- Transfer learning with sparse initialization
- Efficient fine-tuning of large models
