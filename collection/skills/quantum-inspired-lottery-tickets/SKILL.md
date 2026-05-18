---
name: quantum-inspired-lottery-tickets
description: >
  Quantum-inspired classical algorithm for finding winning lottery tickets in neural networks
  via optimized sparse subnetwork selection using ridgelet transform sampling.
  Use when: optimizing neural network sparsity, implementing dequantized ML algorithms,
  selecting sparse subnetworks, lottery ticket hypothesis, ridgelet-based sampling,
  or replacing quantum ML algorithms with classical equivalents.
  Trigger words: quantum-inspired, lottery tickets, dequantization, ridgelet sampling,
  sparse subnetwork selection, 量子启发, 中奖彩票
---

# Quantum-Inspired Lottery Tickets

Dequantized algorithm for finding winning lottery tickets (sparse subnetworks)
in neural networks using ridgelet transform-based optimized sampling.

## Core Methodology

### Problem
QML algorithm selects sparse subnetworks from large shallow neural networks by sampling
hidden nodes from an optimized probability distribution defined via ridgelet transform.
Naive classical approach: O(exp(D)) time. Quantum approach: O(D) time.

### Solution: Classical Dequantization
Construct fully classical algorithm running in O(poly(D)) time by:
1. Computing ridgelet transform coefficients efficiently
2. Using optimized sampling from the probability distribution
3. Avoiding exponential candidate enumeration via structured sampling

### Key Steps

1. **Compute Ridgelet Coefficients**:
   - Transform target function into ridgelet representation
   - Extract optimized sampling distribution from coefficients

2. **Efficient Classical Sampling**:
   - Sample hidden nodes from the optimized distribution
   - Use polynomial-time approximation instead of exact sampling
   - Maintain comparable empirical risk to exact sampling

3. **Subnetwork Construction**:
   - Build sparse subnetwork from sampled nodes
   - Train only selected subnetwork parameters
   - Achieve similar performance with fewer parameters

## Implementation Notes

- Achieves empirical risk comparable to exact sampling
- Substantially lower risk than uniform random sampling
- Exponentially improved runtime vs conventional classical approach
- No quantum hardware needed - runs on conventional computers
- Polynomial scaling in data dimension D

## When to Use

- Network compression / pruning via lottery ticket hypothesis
- Replacing quantum ML algorithms with classical alternatives
- Sparse subnetwork selection for large neural networks
- Ridgelet-based function approximation

## References

- arXiv: 2605.13979
- Authors: Natsuto Isogai, Hayata Yamasaki, Sho Sonoda, Mio Murao
