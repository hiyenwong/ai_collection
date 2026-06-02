---
name: renyi-divergence-fermionic-states
description: "Explicit formulas for regularized Rényi divergences in fermionic quasi-free states — quantum information theory methodology for binary state discrimination error exponents, connecting Petz-type and sandwiched Rényi divergences to information-theoretic bounds. Activation: renyi divergence fermionic, quantum state discrimination, quasi-free fermions, information theory quantum, error exponents quantum"
---

## Summary

**Paper**: arXiv:2605.31379 — "Rényi divergences and binary state discrimination error exponents for fermionic quasi-free states"
**Authors**: Milán Mosonyi, Gábor Maróti-Zareczky
**Date**: 29 May 2026
**Categories**: quant-ph, cs.IT, math-ph

## Core Methodology

### Problem Domain

Binary i.i.d. quantum state discrimination — determining which of two quantum states a system is in, with error probabilities characterized by Rényi divergences.

### Key Contributions

1. **Explicit formulas** for regularized Rényi divergences between translation-invariant, gauge-invariant quasi-free states on doubly infinite fermionic chains
2. **Coverage of divergence types**: Petz-type, sandwiched, log-Euclidean, maximal, measured, and integral Rényi divergences
3. **Asymptotic classicality theorem**: Single-mode-per-site case becomes asymptotically classical — all regularized Rényi divergences converge to equal values
4. **Persistent non-commutativity**: Multiple-modes-per-site case retains non-commutativity under regularization, yielding different values for different Rényi parameters

### Mathematical Framework

- **State class**: Translation-invariant + gauge-invariant quasi-free fermionic states
- **Chain structure**: Doubly infinite fermionic lattice
- **Divergence analysis**: Regularized (thermodynamic limit) versions of multiple Rényi divergence families
- **Super-exponential decay construction**: Generalized from Bunth et al. (2023) to multiple modes per site

### Two Regimes Identified

| Regime | Modes per site | Behavior |
|---|---|---|
| Single-mode | 1 | Asymptotically classical, all divergences equal |
| Multi-mode | >1 | Non-commutativity persists, divergences differ by parameter |

## Reusable Patterns

### Quantum State Discrimination Pipeline

For analyzing quantum hypothesis testing problems:

1. **Characterize states**: Identify if states belong to a tractable class (e.g., quasi-free fermionic)
2. **Compute Rényi divergences**: Use closed-form expressions when available
3. **Derive error exponents**: Map divergences to discrimination error bounds
4. **Check asymptotic regime**: Single-mode → classical, multi-mode → quantum

### Information-Theoretic Bounds Framework

The paper provides a template for deriving information-theoretic limits:
- **Upper bounds**: Via sandwiched Rényi divergences
- **Lower bounds**: Via Petz-type Rényi divergences
- **Gap analysis**: When bounds differ, quantify the non-commutativity contribution

## Activation

Keywords: renyi divergence fermionic, quantum state discrimination, quasi-free fermions, information theory quantum, error exponents quantum, petz renyi, sandwiched renyi, fermionic chain
