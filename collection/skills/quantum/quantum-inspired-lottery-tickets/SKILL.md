---
name: quantum-inspired-lottery-tickets
description: "Quantum-inspired classical algorithm for finding winning lottery tickets in neural networks. Uses ridgelet transform to define optimized sampling distribution for sparse subnetwork selection. Runs in O(poly(D)) time, removing exponential dependence from previous classical approaches. Use when: (1) pruning large neural networks efficiently, (2) finding sparse subnetworks without full training, (3) comparing quantum vs classical algorithmic advantages for subnetwork selection, (4) ridgelet-based node sampling. Activation: lottery tickets, sparse subnetwork, quantum-inspired classical algorithm, ridgelet transform, neural network pruning, dequantization, optimized sampling, polynomial time pruning"
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.13979"
  published: "2026-05-13"
  authors: "Natsuto Isogai, Hayata Yamasaki, Sho Sonoda"
  tags: [quantum, neural-networks, pruning, lottery-tickets, ridgelet, dequantization]
---

# Quantum-Inspired Lottery Tickets

Methodology for selecting sparse subnetworks from large shallow neural networks using quantum-inspired classical algorithm based on ridgelet transform.

## Core Idea

Instead of solving optimization over large-scale network, construct sparse subnetwork by sampling hidden nodes from optimized probability distribution defined via ridgelet transform.

## Key Results

- **Quantum algorithm**: O(D) sampling time
- **Previous classical**: exp[O(D)] time
- **This method**: O(poly(D)) — removes exponential dependence
- Empirical risk comparable to exact sampling, substantially lower than uniform sampling

## Methodology

### Step 1: Ridgelet Transform

Compute ridgelet coefficients f_ρ(a, b) for network weight distribution. This defines the importance landscape of hidden nodes.

### Step 2: Optimized Sampling Distribution

Construct probability distribution p(a, b) ∝ |f_ρ(a, b)|². This concentrates sampling on structurally important nodes.

### Step 3: Classical Sampling

Sample m hidden nodes from p(a, b) using the dequantized sampler. Runtime O(poly(D, m, 1/ε)) for ε-approximate sampling.

### Step 4: Subnetwork Evaluation

Train only the sampled subnetwork. Compare empirical risk against uniform baseline and full network.

## When to Use

- Large shallow networks where full training is expensive
- Need principled pruning without iterative magnitude-based methods
- Evaluating quantum advantage claims in ML (this paper provides dequantization)

## Pitfalls

- **Shallow networks only**: Method analyzed for single-hidden-layer networks
- **Ridgelet requirements**: Activation function must admit ridgelet representation
- **Sample size tradeoff**: Too few nodes → poor approximation; too many → no speedup
- **Not universal**: Does not apply to deep CNNs or transformers without modification

## References

- Isogai, Yamasaki, Sonoda, arXiv:2605.13979 (2026)
- Related: `quantum-inspired-optimization` skill
- Related: `winning-lottery-tickets-quantum-inspired` skill
