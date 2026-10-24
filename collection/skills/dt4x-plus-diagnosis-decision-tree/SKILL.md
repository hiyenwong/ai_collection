---
name: dt4x-plus-diagnosis-decision-tree
description: Use when building hybrid model-based + data-driven fault diagnosis systems. Enhanced symbolic-regression decision tree whose node expressions separate target classes while preserving ARR coherence of non-target classes.
trigger: DT4X, analytical redundancy relations, symbolic regression decision tree, fault diagnosis indicator, hybrid diagnosis, interpretability diagnosis tree, ARR properties, fault indicator discovery
category: ai_collection
---

# DT4X+: Fully Efficient Fault Indicators via ARR-Coherent Symbolic Regression Trees

**Source**: arXiv:2609.28087v1 (2026-09-23) — Bezmaternykh, Travé-Massuyès, Chanthery.

## Problem

Model-based diagnosis uses **Analytical Redundancy Relations (ARRs)** — input-output relations serving as diagnosis indicators — prized for interpretability. Data-driven methods add adaptability. **DT4X** combined them: symbolic regression generates multivariate relations used as **split functions in a decision tree**. But its symbolic regression optimizes only the separation between **two selected classes** at each node — **fragmenting the remaining classes**, degrading interpretability and performance.

## DT4X+ Enhancement

Modify (a) training-set construction and (b) the symbolic-regression loss so expressions **separate the target classes while preserving the coherence of non-target classes**:

- Resulting relations become **fully consistent with ARR properties** → more informative splits, improved robustness, better performance on dynamic-system datasets.

## Core Pattern (reusable)

When learning structured symbolic expressions as decision functions over multiple classes:

1. **Do not optimize pairwise separation alone** — a split function that isolates classes (A vs B) may scatter (C, D, E) into arbitrary fragments, destroying downstream tree structure.
2. **Penalize fragmentation of non-target classes** — the loss should keep non-target classes coherent (each remaining class should land consistently on one side or in a structured arrangement), not just achieve target separation.
3. **Constrain expressions to the domain's structural properties** (here: ARR input-output relation properties) so learned indicators inherit the interpretability guarantees of the model-based paradigm.

## Verified Results

Experiments across several dynamic-system benchmarks: enhanced formulation brings **more informative splits, improved robustness, better diagnosis performance** vs DT4X.

## Implementation Checklist

1. Build per-node training sets that maintain non-target class integrity (oversample/structure so each split's non-target classes stay identifiable).
2. Symbolic regression search with a composite loss: `L = separation(target) + λ·coherence(non-target)` (e.g., penalize variance of non-target class assignment across the expression's output).
3. Filter expressions for ARR property compliance (input-output relation form).
4. Grow the decision tree using these expressions as split functions; prune by diagnosis performance, not just purity.
5. Evaluate on dynamic-system datasets with known fault modes; check robustness under noise.

## Related Skills

- `automated-iot-automotive-testing` — deployment-aware diagnosis/testing
- `neo-agentic-program-analysis` — program-level analysis
- `stochastic-physical-neural-networks` — physics-constrained learning (same "constrain to structure" principle)
