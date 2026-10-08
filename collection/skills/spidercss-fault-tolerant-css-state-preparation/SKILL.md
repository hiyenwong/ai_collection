---
name: spidercss-fault-tolerant-css-state-preparation
description: "Use when compiling fault-tolerant CSS state-prep circuits via ZX-calculus. Fault-equivalence by construction."
category: ai_collection
---

# SpiderCSS: Scalable Fault-Tolerant CSS State Preparation

Source: arXiv:2610.03714 (Poór, Khesin, Li, Rodatz, van de Wetering, Yeung — Oxford/Amsterdam/QuSoft, 2 Oct 2026)

## Core Methodology

Pipeline for compiling fault-tolerant (FT) state-preparation circuits for **arbitrary CSS codes**, scalable to distance 15 (vs SAT/ILP which die early), beating Flag-at-Origin (FaO) on all metrics: −53.8% CNOT (best), ~10× depth reduction, +33.7% avg logical-error-rate improvement, +9.5% acceptance rate. Every component runs in **polynomial time**.

### Key idea: Fault Tolerance by Construction (not verification)

Instead of synthesizing a circuit then verifying FT (expensive), start from an *idealized, fault-free ZX-diagram* of the target state and transform it using ONLY **fault-equivalent rewrites**. Fault equivalence of the end circuit to the idealization then holds *by construction* — no verification round needed.

**Fault equivalence (Def II.15)**: diagrams D1 (noise N1) and D2 (noise N2) are w-fault-equivalent iff every undetectable fault F1 on D1 with N1(F1)<w has a corresponding F2 on D2 with N2(F2)≤N1(F1), and vice versa. Properties: transitive; preserved under sequential/parallel composition (Prop II.16) — so rewrites compose inside larger diagrams. The ZX-calculus restricted to fault-equivalent rewrites is **complete** [van de Wetering et al.] — you don't lose rewriting power.

**Prop II.17**: D w-FT prepares |ψ⟩ ⟺ D is w-fault-equivalent to the idealization where the only allowed faults are output-qubit flips weighted by count. This *recovers* the standard FT definition as a special case.

**Trap (Lemma II.18)**: ordinary spider unfusion is NOT fault-equivalent (π-copy rule blows up fault weight: an internal X-edge flip propagates to all output edges). Only the special rewrite family of "Fault Tolerance by Construction" [Rodatz et al.] preserves it — unidealize edges with those rules only.

### Pipeline steps

1. **Normal form**: target CSS state (code stabilizers + logical state stabilizers) → ZX-diagram in normal form → rewrite to bipartite graph of Z- and X-spiders (idealized spec).
2. **Unidealize** internal edges with fault-equivalent rewrites (introduces ancilla/measurement structure without losing FT).
3. **Spider decomposition**: each high-weight Z/X-spider (= CAT state in Z/X basis) → network of 3-ary spiders via modified **SpiderCat** procedure, with *provably optimal spider counts* → optimal CNOT counts for CAT-state prep (rooted spanning-tree argument; optimality when CAT state is "well-ordered").
4. **Layout**: assign each spider to a qubit + timestep; **minimum diameter spanning forest (MDSF)** of the connectivity graph minimizes max component diameter (controls depth); simulated annealing over external-edge orderings; RREF-basis selection to minimize total logical CNOT cost.
5. **Scheduling heuristics** (pick by objective): *Earliest Start* (immediate depth), *Critical Path* (overall depth), *Active Spider* (min simultaneous spiders → width), *Seq. Distance* (annealed avg distance between consecutive uses of same spider → qubit lifetime/reuse).
6. **Extract circuit**: arrange by topological generations of the DAG; primary qubit lines run root→boundary; remaining spiders Y-placed on their paths.

### Why acceptance rate improves

Minimize **number of flags** in CAT states (fewer check qubits that can trip) + routing that minimizes qubit lifetime + maximizes reuse. Fewer flags and shorter lifetimes → higher probability a shot passes all checks.

## Reusable Patterns

- **Correctness-by-construction over post-hoc verification**: define an equivalence relation on (artifact, noise-model) pairs that is preserved by your transformation algebra; restrict all rewrites to the preserving subset; completeness of the restricted algebra means no power is lost. Applicable beyond QC (compiler passes, distributed protocol refinement).
- **CAT-state LEGO + global routing**: solve local components to provable optimality (spanning trees), then treat inter-component wiring as a separate graph-optimization (MDSF/annealing) layer. Local-optimal + global-near-optimal beats monolithic search at scale.
- **Objective-selectable scheduling**: same DAG, four heuristics mapped to different cost functions (depth / width / lifetime). Expose the choice as a knob rather than hardcoding.

## Benchmark anchors

CSS codes [[7,1,3]] → [[95,1,7]], [[47,1,11]], [[49,1,5/7]]: CNOT −53.8% max, depth ~10× best-case, LER −90% max, acceptance +9.5% avg vs FaO. Polynomial in d throughout.

## Pitfalls

- Do NOT use generic ZX simplification (unfusion, local complementation) — most standard rewrites break fault equivalence even when they preserve semantics. Use only the FT-by-Construction rewrite set.
- Edge-flip vs CSS-edge-flip noise models give different equivalence classes — declare the noise model first.
- SpiderCat decomposition optimality requires well-ordered CAT states; fall back to optimal- among-available when the well-ordering fails.

## Activation

fault-tolerant state preparation, CSS codes, ZX-calculus, fault-equivalent rewrites, CAT states, SpiderCat, Flag at Origin, minimum diameter spanning forest, logical error rate acceptance
