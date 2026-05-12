---
name: triple-loop-consolidation-non-gradient-memory
description: >
  Triple-Loop Consolidation methodology for persistent memory in non-gradient dissipative cognitive
  architectures. Use when: designing persistent memory for dissipative/neuromorphic systems,
  studying memory consolidation without gradient computation, implementing Deep Memory (DM) mechanism
  with recording-seeding-reentry cycle, analyzing Mixture-of-Experts (MoE) gating for memory
  specialization, modeling hippocampal consolidation parallels, or building non-gradient cognitive
  architectures. Covers: dissipative computation, non-gradient learning, triple-loop consolidation,
  expert-specific centroids, discrete MoE routing, memory reconstruction after interference.
  arXiv: 2603.27188 (Lou, 2026).
---

# Triple-Loop Consolidation for Non-Gradient Memory

## Core Problem

Dissipative cognitive architectures maintain computation through continuous energy expenditure, where
units that exhaust their energy are stochastically replaced with fresh random state. This creates a
fundamental challenge: how can persistent, context-specific memory survive when all learnable state
is periodically destroyed?

Existing memory mechanisms (elastic weight consolidation, synaptic intelligence, surprise-driven gating)
rely on gradient computation and are **inapplicable** to non-gradient dissipative systems.

## Deep Memory (DM) Mechanism

DM is a non-gradient persistent memory mechanism operating through a **triple-loop consolidation cycle**:

### Loop 1: Recording
- Record expert-specific content centroids from the active computation
- Centroids capture the essential representation of each expert's learned knowledge
- Recording is continuous, not episodic

### Loop 2: Seeding
- When units are replaced (due to energy exhaustion), seed them with stored centroid representations
- This transfers preserved knowledge into fresh units
- One-shot seeding fails; **continuous seeding** is required

### Loop 3: Stabilization (Re-entry)
- Stabilize representations through continuous re-entry into the active computation
- Seeded representations are reinforced by re-participating in ongoing processing

## Critical Prerequisites

### Discrete MoE Routing is Necessary
- **Discrete expert routing via MoE gating is a causal prerequisite** for DM
- Without discrete routing: centroids converge to identical values (MI = 0.001)
- With discrete routing: each expert develops specialized representations (MI = 1.10)
- Continuous/soft routing does not enable memory consolidation

### Minimal Critical Dyad
- Recording × Seeding is the minimal necessary combination
- Recording alone or seeding alone is insufficient
- Full triple-loop (recording + seeding + re-entry) achieves optimal performance

## Empirical Results (~970 simulation runs)

| Experiment | Result | n |
|---|---|---|
| Discrete routing necessary for specialization | MI=1.10 vs 0.001 | 91 |
| DM achieves persistent memory | R=0.984 vs 0.385 without memory | 16 |
| Continuous seeding reconstructs after interference | R_recon=0.978; one-shot fails | 30 |
| Characterized (K, p) envelope | Stable operation regime mapped | 350 |
| Recording × seeding is minimal critical dyad | Confirmed | 40 |
| DM outperforms non-gradient baselines | Beat Hopfield, ESN under matched turnover | 370 |

## Parameter Space

- **K**: Expert count / network capacity parameter
- **p**: Turnover probability (fraction of units replaced per step)
- DM operates within a characterized (K, p) envelope
- Outside this envelope: memory either collapses or computation degrades

## Baseline Comparisons

DM outperforms established non-gradient memory mechanisms under matched turnover conditions:
- **Hopfield networks**: fail under high turnover
- **Echo State Networks (ESN)**: cannot maintain persistent representations
- **Without memory**: R=0.385 vs DM's R=0.984

## Biological Parallels

DM has functional parallels to **hippocampal consolidation**:
- Recording ↔ memory encoding
- Seeding ↔ replay during sleep
- Stabilization ↔ systems consolidation
- Non-gradient nature aligns with biological constraints (synaptic consolidation doesn't use backprop)

## Implementation Notes

### Minimal Reproduction
The paper includes `dm_minimal_reproduction.py` (~200 lines, NumPy-only) as ancillary file:
- https://arxiv.org/src/2603.27188/anc/dm_minimal_reproduction.py

### Key Design Decisions
1. **Discrete vs continuous routing**: Must use hard/discrete MoE gating
2. **Continuous vs one-shot seeding**: Continuous seeding required for reconstruction
3. **Centroid specificity**: Each expert maintains distinct centroids
4. **Turnover matching**: Replacement rate must stay within (K, p) envelope

## Related Work
- Dissipative cognitive architectures (continuous energy expenditure systems)
- Non-gradient learning (local rules, Hebbian, neuromodulated plasticity)
- Mixture-of-Experts routing and specialization
- Hippocampal memory consolidation and replay

## References
- arXiv: 2603.27188
- Lou, J. (2026). Persistent Memory Through Triple-Loop Consolidation in a Non-Gradient
  Dissipative Cognitive Architecture. Submitted to Frontiers in Computational Neuroscience.
