---
name: plaquette-ftqc-design
category: quantum-computing
trigger_words: ["plaquette", "hardware-aware FTQC", "fault-tolerant quantum computer design", "logical performance from device physics", "XPauli sampler", "near-Clifford sampler", "leakage error simulation", "quantum error budget"]
created: 2026-07-10
source: "arxiv:2607.08767"
---

# Plaquette: Hardware-Aware FTQC Design Platform

**Source**: Conchello Vendrell et al., "Plaquette: A hardware-aware design platform for fault-tolerant quantum computers" (arXiv:2607.08767, July 2026)

## Overview

Plaquette is a theoretical framework and software suite that computes the logical performance of fault-tolerant quantum computer (FTQC) architectures directly from the physics of device imperfections. It bridges the gap between hardware-level error models and logical-level performance metrics, enabling accurate error budgeting and overhead estimation.

## Key Problem

Hardware teams building FTQCs must decide which imperfections to suppress. Scalable stabilizer simulators use stochastic Pauli models, but real hardware noise often departs from these:
- **Superconducting transmons**: leak out of computational subspace
- **Neutral atoms**: scatter through intermediate states
- **Trapped ions**: heat as motional modes absorb phonons
- **All platforms**: miscalibrated controls over-rotate coherently

## Core Methodology

### Four Sampler Classes

1. **Stabilizer Sampling**: For pure Pauli noise (standard approach)
2. **XPauli Sampler**: NEW — handles leakage and environment sectors
3. **Near-Clifford Samplers**: For coherent errors (over-rotations, calibration errors)
4. **Full-State Simulation**: Exact reference calculations (small-scale only)

### Workflow

```
Physical Error Model (Kraus/Hamiltonian-Lindblad/Channel)
    ↓
Automatic Compilation → Required Representation per Sampler
    ↓
Logical Performance Metrics (threshold, error rates, overhead)
```

### Error Model Specification

Errors are specified once as:
- Kraus operators
- Hamiltonian-Lindblad dynamics
- Experimentally reconstructed quantum channels

Then automatically compiled into the representation required by each sampler class.

## Key Findings

1. **XPauli and near-Clifford samplers match full-state simulation** within statistical uncertainty
2. **Pauli twirling can fall short** depending on the error model
3. **Discrepancy size varies** with platform and noise process
4. **Reliable thresholds, error budgets, and overhead estimates** require the most accurate simulation available

## When to Use

- Designing FTQC architectures with non-Pauli error sources
- Building error budgets that account for leakage, coherent errors, or environmental coupling
- Validating whether Pauli-twirled approximations are sufficient for a given platform
- Comparing logical performance across hardware platforms (superconducting, neutral atom, trapped ion)

## Activation

Keywords: plaquette, hardware-aware, FTQC design, XPauli, near-Clifford, leakage simulation, coherent error, error budgeting, Kraus compilation, fault-tolerant threshold
