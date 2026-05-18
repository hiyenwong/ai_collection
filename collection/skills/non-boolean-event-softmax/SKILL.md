---
name: non-boolean-event-softmax
description: Methodology for analyzing softmax and normalized response functions in non-Boolean event structures with overlapping contexts. Covers single-valuedness constraints on shared atoms, consistent connectedness, no-disturbance conditions, and coordinate parametrizations of admissible-weight polytopes. Use when studying choice theory with overlapping contexts, generalized softmax rules, cognitive science with incompatible measurements, quantum contextuality and exotic weights exceeding classical bounds, event structure normalization, or probabilistic modeling with shared atoms across contexts. Trigger words: non-boolean event structures, generalized softmax, consistent connectedness, no-disturbance, admissible weights, contextuality, exotic weights, overlapping contexts.
license: Complete terms in LICENSE.txt
---

# Non-Boolean Event Softmax

Methodology from "Local Softmax and Global Weights in Non-Boolean Event Structures" (arXiv: 2605.16248).

## Core Insight

In non-Boolean event structures with overlapping contexts, local normalization (softmax) does not automatically yield a global probability weight. Single-valuedness on shared atoms (no-disturbance/consistent connectedness) collapses generalized softmax rules to coordinate parametrizations of the strictly positive part of the admissible-weight polytope.

## Key Results

1. **Collapsing theorem**: Single-valuedness on shared atoms → generalized softmax collapses to coordinate parametrization of admissible-weight polytope
2. **Completeness**: Any strictly positive admissible weight can be represented this way; boundary weights arise as limits
3. **Exotic weights**: Weights exceeding classical or quantum bounds are reachable when no-disturbance is relaxed
4. **Dynamical perspective**: Continuous-time softmax dynamics with local learning rates converges to admissible weights

## When to Use

- Analyzing choice behavior across overlapping decision contexts
- Modeling cognitive systems with incompatible measurements
- Studying contextuality in quantum foundations
- Generalizing softmax beyond Boolean event algebras
- Understanding when local normalization fails globally

## Pitfalls

- Do not assume local normalization implies global consistency
- Boundary weights require limits, not direct parametrization
- Exotic weights (beyond quantum bounds) require dropping no-disturbance
- Single-valuedness is the critical constraint — without it, softmax remains unconstrained
