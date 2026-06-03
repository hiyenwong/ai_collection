---
name: branch-aware-quantum-constant-propagation
description: "Branch-Aware Quantum Constant Propagation (BQCP) — compile-time optimization for dynamic quantum circuits with mid-circuit measurements and classical feedforward. Extends Quantum Constant Propagation (QCP) by tracking classical information from mid-circuit measurements with post-measurement quantum states across execution branches, enabling path-sensitive reasoning inside conditional blocks. Use when optimizing dynamic quantum circuits, implementing compiler passes for quantum computers, performing compile-time analysis on circuits with mid-circuit measurements, or simplifying quantum circuits with classical control flow. Activation: quantum compiler optimization, dynamic quantum circuits, mid-circuit measurement, classical feedforward, quantum constant propagation, branch-aware analysis, circuit simplification, path-sensitive reasoning"
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2606.02018"
  published: "2026-06-01"
  authors: "Innocenzo Fulginiti, Yanbin Chen"
  tags: [quantum, compiler, optimization, dynamic-circuits, constant-propagation, mid-circuit-measurement]
---

## Core Concept

BQCP performs compile-time analysis on **dynamic quantum circuits** — circuits containing mid-circuit measurements and classical feedforward (branching based on measurement outcomes).

### Key Innovation over QCP
- **QCP** only handles unitary circuits — tracks quantum states but ignores classical control flow
- **BQCP** extends QCP by tracking:
  - Classical information produced by mid-circuit measurements
  - Corresponding post-measurement quantum states
  - Different execution branches (paths through conditional blocks)

### Mechanism
1. **Branch tracking** — enumerate execution paths through conditional blocks
2. **State tracking** — for each branch, track both classical measurement outcomes and quantum post-measurement states
3. **Path-sensitive reasoning** — apply different simplifications depending on branch conditions
4. **Scalability bounds** — limit quantum-state representation size and number of tracked branches

### Soundness
Both the analysis and the simplifications are formally proven sound.

### Results
- Consistently achieves larger reductions than existing passes (including QCP) on dynamic circuits
- Evaluated on both application-driven and synthetic benchmarks
- Accepted at IEEE QSW 2026

## Application Areas
- Quantum compiler optimization passes
- Dynamic circuit simplification
- Mid-circuit measurement optimization
- Classical feedforward analysis
- Noise-aware circuit compilation

## Pitfalls
- **Branch explosion**: Unbounded branch tracking grows exponentially — must cap tracked branches
- **State representation**: Full quantum state tracking is O(2^n) — use bounded representations
- **Dynamic vs unitary**: BQCP specifically targets dynamic circuits; for purely unitary circuits, QCP or other passes may suffice
- **Soundness proof**: Simplifications must preserve semantics across ALL branches simultaneously
