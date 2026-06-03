---
name: quantum-probability-hebbian-learning
description: "Quantum probability-flow methodology for deriving local Hebbian learning rules in associative memory networks. Use when: (1) quantum-inspired learning rules for neural networks, (2) attention mechanisms from quantum probability flow, (3) quantum annealer-based learning rule validation, (4) transverse-field leakage channels for stability-driven updates. Activation: quantum probability flow, Hebbian learning, quantum annealer, associative memory, transverse field, attention-like learning rule, softmax Hebbian, quantum annealing learning"
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2606.02098"
  published: "2026-06-01"
  authors: "Masayuki Ohzeki"
  tags: [quantum, hebbian-learning, associative-memory, attention, quantum-annealing]
---

## Problem Statement

How to derive local learning rules for associative memory that exhibit attention-like behavior, using quantum mechanical principles.

## Core Methodology

### Quantum Probability-Flow Principle

1. **Transverse field** defines leakage channels from data states
2. **Minimize measured survival loss** → stability-driven weight updates
3. **Imaginary-time, dephased dynamics** → local leakage free energy = log-sum-exp of energy gaps
4. **Gradient of leakage free energy** → softmax-weighted Hebbian rule

### Two Regimes

| Regime | Dynamics | Learning Rule |
|--------|----------|---------------|
| Imaginary-time | Dephased | Softmax-weighted Hebbian (log-sum-exp) |
| Real-time | Coherent | Power-law weighted Hebbian (Lorentzian) |

### Empirical Validation

D-Wave standard-anneal and fast-anneal tests on one-hot attention forward map:
- **Standard anneal**: Better fitted by softmax than Lorentzian
- **Fast anneal**: Both regimes tested, softmax dominates

## Reusable Patterns

### Pattern 1: Stability-Driven Learning

Replace gradient descent with stability analysis:
1. Define a transverse field (quantum fluctuation) on the energy landscape
2. Measure state survival probability under perturbation
3. Update weights to maximize survival (minimize leakage)
4. Result: local learning rule emerges from global stability

### Pattern 2: Softmax Hebbian from Quantum Flow

The leakage free energy gradient produces:
```
Δw_ij ∝ softmax(ΔE_k) · x_i · x_j
```
where ΔE_k are energy gaps between data and non-data states.

This recovers the softmax attention mechanism from first quantum principles.

## Key Insights

- Attention-like weighting emerges naturally from quantum stability analysis
- Softmax is not an ad-hoc choice — it's the gradient of log-sum-exp leakage free energy
- Quantum annealer hardware provides physical validation of the learning rule
- Power-law alternative (from real-time dynamics) is less accurate empirically

## Pitfalls

- **4-page paper**: Core theory is concise; implementation details require extrapolation
- **D-Ware specific**: Validation on D-Wave hardware; results may vary on other quantum annealers
- **One-hot mapping**: Tested on one-hot attention; extension to distributed representations needed

## References

- arXiv:2606.02098v1 — Attention-Like Hebbian Learning from Quantum Probability Flow and Quantum-Annealer Tests
- Related: cond-mat.dis-nn (disordered systems and neural networks)
