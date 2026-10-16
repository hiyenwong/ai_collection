---
name: ultra-high-rate-quantum-codes
description: Use when designing ultra-high-rate QEC codes.
version: "1.0.0"
source: https://arxiv.org/abs/2609.30069
source_title: "Design Principles for Ultra-High-Rate Quantum Codes"
authors: "Jong Yeon Lee, Koki Okada, Nishad Maskara, Kenta Kasai, Hengyun Zhou"
published: 2026-09-24
categories: quant-ph
trigger_words:
  - ultra-high-rate quantum codes
  - quantum code design
  - encoding rate
  - pair-partition construction
  - column weight design
  - halving transformation
  - non-CSS codes
  - LDPC quantum codes
---

# Design Principles for Ultra-High-Rate Quantum Codes

## Overview

**arXiv 2609.30069** (Lee, Okada, Maskara, Kasai, Zhou — 2026-09-24). Systematic design principles for ultra-high-rate quantum error-correcting codes that minimize qubit overhead: some constructions need as few as **2 physical data qubits per logical qubit**. The paper provides the first systematic navigation of the tradeoff space among **encoding rate, code distance, check weight, and blocklength**.

## Core Methodology

### 1. The Design Space
Four coupled parameters, no free lunch:
- **Encoding rate k/n** — logical qubits per physical qubit (ultra-high = 2:1 to 4:1 data qubits)
- **Distance d** — error suppression exponent
- **Check weight** — stabilizer row weight (syndrome extraction circuit complexity)
- **Blocklength n** — total qubits per code block

Key tension: larger distance at compact blocklength requires **heavier checks** (higher column weight).

### 2. Code Templates
- **Pair-partition construction**: partition qubits into pairs, build stabilizer checks over pairs — compact blocklength by construction.
- **Halving transformation**: post-processing that **reduces blocklength by half** while preserving code properties — multiply k/n.
- **Symmetry-informed low-weight logical basis**: exploit code symmetries to find logical operators of minimum weight (large effective distance without search).

### 3. Column Weight as the Key Design Knob
Ensemble analysis of degree distributions shows **column weight** (qubits per check, column of the parity-check matrix) governs the rate–distance–check-weight Pareto frontier:
- Increasing column weight → larger achievable distances at fixed compact blocklength.
- Cost: heavier checks (worse syndrome extraction, more hook errors).
- **At physical error rate p = 0.1%, increased distance usually wins** — the penalty from heavier checks is dominated by the suppression gain.

### 4. Concrete Compact Codes Found
Non-CSS codes with check weight 10:
- `[[90, 21, 11]]` — rate 0.23, distance 11, n=90
- `[[140, 31, 15]]` — rate 0.22, distance 15
- `[[200, 43, 20]]` — rate 0.215, distance 20

These sit on a favorable point of the Pareto frontier relative to prior ultra-high-rate constructions.

## Reusable Patterns

1. **Pareto navigation pattern**: when a design space has rate/distance/weight/blocklength tradeoffs, pick ONE parameter as the knob (column weight), derive the rest via ensemble analysis, then sweep.
2. **Pair-partition + halving**: build the smallest primitive first (pairs), then apply a structure-preserving reduction (halving) rather than searching the full space.
3. **Error-rate-dependent regime choice**: at p=0.1% distance dominates; thresholds shift at higher p — always state the physical error rate alongside code parameter claims.
4. **Symmetry before search**: use code automorphisms to restrict the logical-operator search space to symmetric sectors.

## Activation
- Designing QEC codes with qubit overhead < 5:1 physical:logical
- Comparing rate vs distance at fixed blocklength
- Deciding whether heavier checks are acceptable at a given physical error rate
- Reducing blocklength of an existing high-rate code

## Pitfalls
- **Distance claims without physical error rate are incomplete** — the distance-vs-check-weight winner flips by regime.
- Non-CSS codes trade CSS-structure tools (separate X/Z checks) for compactness — syndrome extraction circuits need re-derivation.
- The halving transformation reduces blocklength but can concentrate logical weight; re-verify logical-operator weight after halving.
- Column weight 10 checks imply deep syndrome-extraction schedules — check hardware cycle-time budgets before adopting.

## Source
- arXiv: [2609.30069](https://arxiv.org/abs/2609.30069)
- Imported to kg.db entities 9701, linked to 8 QEC-related papers via kg_relations
