---
name: lightstim-qec-protocol-evaluation
description: "LightStim framework for automated Quantum Error Correction (QEC) protocol evaluation and prototyping with automated Detector Error Model (DEM) construction. Maintains Pauli tableau augmented with measurement records during circuit compilation, enabling circuit-level QEC evaluation without manual annotation. Use when: (1) Evaluating QEC protocols at circuit level, (2) Building DEMs for logical error rate estimation, (3) Prototyping new QEC codes, (4) Cross-code lattice surgery design, (5) Systematic QEC benchmarking. Activation: LightStim, QEC evaluation, detector error model, DEM construction, quantum error correction benchmarking, lattice surgery, protocol prototyping, circuit-level QEC"
metadata:
  arxiv_id: "2604.21472"
  published: "2026-04-23"
  authors: "Xiang Fang, Ming Wang, Yue Wu, Sharanya Prabhu, Dean Tullsen, Narasinga Rao Miniskar, Frank Mueller, Travis Humble, Yufei Ding"
  tags: [quantum, error-correction, qec, dem, circuit-compilation, fault-tolerance, lattice-surgery]
---

## Context

Fault-tolerant quantum computing requires circuit-level evaluation of QEC protocols and their Detector Error Models (DEMs) to estimate end-to-end logical error rates. Current DEM construction relies on manual annotation — tedious, error-prone, and limiting evaluation to simple memory experiments.

LightStim (arXiv:2604.21472, revised 2026-06-03) automates DEM construction concurrently with circuit compilation by maintaining a Pauli tableau augmented with measurement records, requiring no protocol-specific input.

## Core Methodology

1. **Pauli Tableau Tracking**: Maintain a Pauli tableau through circuit compilation, tracking how Pauli operators propagate through gates
2. **Measurement Record Augmentation**: Augment the tableau with measurement outcomes, enabling correlation tracking between stabilizer measurements
3. **Automated DEM Construction**: Extract detector error models directly from the augmented tableau — no manual annotation required
4. **Protocol-Agnostic Processing**: Works with any QEC protocol without protocol-specific configuration
5. **Cross-Code Lattice Surgery**: Supports heterogeneous designs between different code families (e.g., surface code + punctured quantum Reed-Muller codes)

## Implementation Steps

1. Define the QEC circuit (physical qubits, gates, measurements)
2. Run LightStim compilation — maintains Pauli tableau + measurement records
3. Extract DEM: detector pairs and observable counts auto-generated
4. Validate DEM: cross-check detector/observable counts against known implementations
5. Simulate: use DEM to estimate logical error rates under noise models
6. (Optional) Design cross-code lattice surgery between different QEC code families

## Key Results from Paper

- Exact detector and observable counts validated against public implementations
- Consistent logical error rates across protocols from memory experiments to end-to-end distillation circuits
- Novel heterogeneous cross-code lattice surgery between surface and punctured quantum Reed-Muller codes
- Open-sourced framework available

## Pitfalls

- **DEM construction is traditionally manual**: LightStim solves this, but understanding the underlying Pauli tableau propagation is still important for debugging
- **Circuit-level vs logical-level**: LightStim operates at circuit level — ensure noise models match the physical hardware being simulated
- **Cross-code compatibility**: When designing lattice surgery between different codes, verify boundary conditions match

## Verification

- Cross-validate detector and observable counts against public QEC implementations
- Verify logical error rates are consistent across noise models
- For cross-code designs, check that syndrome extraction remains consistent at code boundaries

## Activation

- `LightStim`, `QEC protocol evaluation`, `detector error model`, `DEM construction`, `quantum error correction benchmarking`, `lattice surgery`, `circuit-level QEC`, `fault-tolerant quantum computing`, `qec prototyping`
