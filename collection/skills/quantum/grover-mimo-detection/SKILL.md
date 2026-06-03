---
name: grover-mimo-detection
description: "Quantum-native maximum likelihood detection (MLD) for overloaded MIMO systems using Grover Adaptive Search (GAS) with search space reduction. Use when designing quantum-accelerated wireless detectors, overloaded MIMO, random access channels, quantum signal processing, or when classical linear detectors degrade in overloaded scenarios."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.19389"
  published: "2026-05-19"
  tags: [quantum, mimo, wireless, grover, detection, systems-engineering]
---

# Grover-Based MIMO Maximum Likelihood Detection

## Source
- arXiv: 2605.19389 (May 19, 2026)

## Core Problem
In overloaded random access MIMO channels, classical linear detectors (ZF, MMSE) degrade severely. Exhaustive-search MLD achieves optimal BER but costs O(2^K) — intractable for large K users.

## Key Innovation
Formulate MLD as binary optimization, solve via Grover Adaptive Search (GAS) with two efficiency improvements:
1. **Search space reduction** via signal-space pruning
2. **Optimal GAS parameter settings** via probability analysis

## Methodology

### 1. Problem Formulation
MLD = minimize ||y - Hx||^2 over x in {-1,+1}^K
- Quadratic objective → QUBO form
- No penalty terms needed (unconstrained binary optimization)

### 2. Grover Adaptive Search (GAS)
- Iterative amplitude amplification with adaptive threshold
- Each iteration: oracle marks states below current threshold
- Converges to global minimum with high probability
- Quadratic speedup: O(sqrt(N)) vs O(N) classical exhaustive

### 3. Search Space Reduction
- Analyze signal constellation geometry
- Prune unlikely candidate regions
- Reduces effective search space by ~65% Grover rotations

### 4. Parameter Optimization
- Probability analysis of GAS convergence
- Optimal rotation count per iteration
- Balance between iterations and oracle complexity

## Systems Engineering Patterns
1. **Quantum-Classical Hybrid**: Use GAS only when classical methods fail (overloaded regime)
2. **Adaptive Algorithm Selection**: Switch detector based on loading ratio
3. **Resource-Aware Optimization**: Trade rotation count vs BER performance

## Activation
- Keywords: quantum mimo, grover search, overloaded MIMO, maximum likelihood detection, GAS, quantum wireless, random access channel
- Use when: designing quantum-accelerated wireless receivers, overloaded multiuser detection, quantum signal processing

## Pitfalls
- GAS requires fault-tolerant quantum computing (not NISQ-viable)
- Search space reduction depends on channel matrix conditioning
- Parameter optimization needs accurate SNR estimation
