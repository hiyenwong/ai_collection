---
name: multi-objective-quantum-workflow
description: >
  Multi-objective optimization methodology for quantum computing workflows,
  combining compilation strategy selection, noise suppression, and error-mitigation.
  Based on QBalance framework (arXiv: 2605.02966) and action-space engineering for
  RL-based circuit routing. Use when: designing quantum compilation pipelines,
  optimizing NISQ device execution, selecting error-mitigation strategies,
  or formulating multi-objective quantum workflow problems.
---

# Multi-Objective Quantum Workflow Optimization

## Core Concept

Near-term quantum workloads involve coupled decisions across compilation, noise suppression,
and error mitigation. Frame these as **finite multi-objective strategy-selection problems**
over circuits, backends, and transformation policies.

## Problem Formulation

```
minimize  f(c, b, t) = w1·error + w2·latency + w3·cost
subject to t ∈ T, b ∈ B, c ∈ C
```

## Strategy Selection Framework

### Step 1: Define Candidate Strategies
Each strategy: `(layout_policy, routing_policy, basis_gates, noise_suppression, error_mitigation)`

### Step 2: Score with Survival-Product Error Proxy
```
survival_product = ∏_g (1 - ε_g)
```
Lightweight ranking before expensive circuit execution.

### Step 3: Bayesian Candidate Ordering
```
score(c) = E[w · φ(c)] + β · σ(c)
```
Feature vector + uncertainty estimate for exploration-exploitation tradeoff.

### Step 4: Non-Dominated Selection
Apply Pareto dominance filtering. Select from the Pareto front.

## Action-Space Engineering for RL-Based Routing

For RL circuit routing in DQC architectures:
1. State-dependent actions: depend on current qubit placement
2. Action masking: prune invalid actions, reduces space by 10-100x
3. Modular decomposition: separate placement, routing, execution

## Distributionally Robust Control

Use Sinkhorn discrepancy for uncertainty sets around noise distributions:
- Combines observed data with prior knowledge
- Convex and tractable for LQ control
- Robust to distributional shifts in quantum gate noise

## Practical Workflow

1. **Characterization**: Profile backend, circuit, estimate baseline error
2. **Strategy Search**: Generate candidates → score → Bayesian ordering → execute top-K
3. **Selection**: Build Pareto front → select → execute → update model
