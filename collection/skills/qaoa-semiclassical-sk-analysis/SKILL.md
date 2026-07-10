---
name: qaoa-semiclassical-sk-analysis
category: quantum-computing
trigger_words: ["QAOA semiclassical", "spin glass optimization", "Sherrington-Kirkpatrick model", "truncated Wigner approximation", "quantum advantage spin glass", "Parisi value convergence", "QAOA depth scaling", "QAOA absence of advantage"]
created: 2026-07-10
source: "arxiv:2607.08708"
---

# QAOA Semiclassical Analysis for Spin Glass Optimization

**Source**: Dries Sels & Flaviano Morone, "Absence of quantum advantage for approximate spin glass optimization" (arXiv:2607.08708, July 2026)

## Overview

This paper provides a semiclassical, large-spin S analysis of the Quantum Approximate Optimization Algorithm (QAOA) on the Sherrington-Kirkpatrick (SK) spin glass model using the truncated Wigner approximation. It reveals important limits on quantum advantage for approximate combinatorial optimization.

## Key Problem

Whether QAOA provides a genuine quantum advantage for approximate optimization of spin glass problems remains an open question. This paper analyzes the algorithm in the semiclassical regime to understand its fundamental scaling behavior.

## Core Methodology

### Truncated Wigner Approximation

- Maps quantum QAOA dynamics onto classical phase space with quantum fluctuations
- Uses large-spin S as a semiclassical parameter
- Analyzes how initial quantum fluctuations propagate through the algorithm

### Key Scaling Results

For depth-p QAOA on the SK model:
1. **Optimal spin balance**: S ~ p (spin size scales with circuit depth)
2. **Energy convergence**: Final energy converges to Parisi value as **log(p)/p**
3. **Semiclassics slightly outperforms** true spin-1/2 QAOA
4. **Both converge the same way** in the large-depth limit

### Three Regimes Identified

1. **Small S**: Dominated by quantum noise, poor performance
2. **S ~ p**: Optimal balance between noise and signal
3. **Large S**: Constrained by exponential growth of initial fluctuations

### Noise-Free Optimization

When initial noise is removed and parameters are re-optimized:
- Achieves superior **1/p convergence** (better than log(p)/p)
- Suggests the noise, not the algorithm structure, is the bottleneck

## Key Findings

1. **No quantum advantage** for approximate spin glass optimization via QAOA
2. Semiclassical methods perform as well as or better than quantum QAOA
3. Both approaches converge to the Parisi value at rate log(p)/p
4. The limitation is fundamental to the algorithm's structure, not implementation noise

## When to Use

- Evaluating whether QAOA is appropriate for combinatorial optimization problems
- Setting realistic expectations for quantum advantage in spin glass optimization
- Designing benchmark comparisons between quantum and classical optimization
- Understanding fundamental scaling limits of variational quantum algorithms

## Pitfalls

- QAOA may not provide advantage for all optimization problems — verify on a case-by-case basis
- The Parisi value is the asymptotic limit; finite-depth performance may still be practically useful
- Removing initial noise and re-optimizing parameters changes the comparison baseline

## Activation

Keywords: QAOA semiclassical, spin glass, Sherrington-Kirkpatrick, truncated Wigner, Parisi value, quantum advantage absence, depth scaling, variational quantum algorithm limits
