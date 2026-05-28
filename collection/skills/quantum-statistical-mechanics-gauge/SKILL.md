---
name: quantum-statistical-mechanics-gauge
description: "Gauge invariance framework for quantum statistical mechanics using operator shifting superoperators. Establishes exact sum rules interconnecting global observables and locally resolved correlation functions, both in and out of thermal equilibrium. Formulates quantum hyperdensity functional theory for formal access to hyperforces and general averaged quantum observables via universal density functionals. Use when: analyzing quantum many-body systems with gauge symmetry, deriving exact sum rules for correlation functions, developing hyperdensity functionals for quantum observables, studying operator shifting transformations, or working with nonequilibrium quantum statistical mechanics."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.26650"
  published: "2026-05-28"
  authors: "Tobias Schmidt, Johannes Ren, Matthias Schmidt"
  tags: [quantum, statistical-mechanics, gauge-invariance, hyperdensity-functional, sum-rules, many-body, nonequilibrium]
---

# Quantum Statistical Mechanics via Gauge Invariance and Operator Shifting

## Overview

This framework reformulates quantum statistical mechanics through the lens of gauge invariance under operator shifting. A shifting superoperator displaces fundamental position and momentum degrees of freedom, and averages of general observables remain invariant under this shift both in and out of thermal equilibrium.

## Core Concepts

### Shifting Superoperator

The gauge transformation is enacted by a shifting superoperator that displaces the fundamental position and momentum degrees of freedom of the quantum many-body system. This is analogous to a gauge transformation in field theory but applied at the level of quantum observables.

### Gauge Invariance of Averages

Key result: averages of general observables remain invariant under the shifting transformation both in thermal equilibrium and in nonequilibrium states. This is a powerful constraint on the structure of quantum statistical theories.

### Exact Sum Rules

The gauge invariance induces exact sum rules that interconnect:
- Global observables (e.g., total energy, particle number)
- Locally resolved correlation functions (spatially dependent correlation measures)

These sum rules provide nontrivial consistency checks for theoretical approximations and simulation methods.

### Quantum Hyperdensity Functional Theory

Extends classical density functional theory to a hierarchy of hyperfunctionals:
- Universal density functionals provide formal access to hyperforces
- General averaged quantum observables are obtained through functional derivatives
- Provides a systematic framework for nonequilibrium quantum systems

## Usage Patterns

### Pattern 1: Deriving Sum Rules for Quantum Correlations

To derive exact sum rules for a quantum many-body system:

1. Define the shifting superoperator for the system's position and momentum operators
2. Apply the gauge transformation to the observable of interest
3. Enforce gauge invariance of the thermal average
4. Extract the resulting sum rule relating global and local quantities

### Pattern 2: Hyperdensity Functional Construction

To construct a hyperdensity functional for a quantum observable:

1. Identify the universal density functional for the reference system
2. Compute functional derivatives with respect to the external potential
3. The hierarchy of derivatives yields hyperforce functionals
4. Use the sum rules as consistency constraints on approximate functionals

### Pattern 3: Nonequilibrium Extension

To extend equilibrium results to nonequilibrium:

1. Verify that the shifting superoperator commutes with the Liouvillian/time evolution
2. Apply the gauge invariance to the nonequilibrium ensemble average
3. The same sum rules hold out of equilibrium, providing strong constraints

## Key Mathematical Results

### Gauge-Invariant Observable Averages

For any observable Ô and shifting parameter λ:
⟨Ô⟩ = ⟨Ô(λ)⟩

where Ô(λ) is the shifted observable. This holds for both equilibrium and nonequilibrium ensembles.

### Hyperforce-Sum Rule Connection

The hyperforce functional F⁽ⁿ⁾(r₁,...,rₙ) satisfies:
∫dr F⁽ⁿ⁺¹⁾(r₁,...,rₙ₊₁) = constraint_from_gauge(F⁽ⁿ⁾)

This hierarchy of constraints enables systematic construction of approximate functionals.

## Error Handling

### Approximate Functionals

When constructing approximate density functionals, verify compliance with the exact sum rules derived from gauge invariance. Violations indicate the approximation breaks a fundamental symmetry.

### Large Displacement Limits

The shifting framework assumes well-defined operator displacements. For systems with bounded operators or compact configuration spaces, verify the shifting superoperator remains well-defined.

## Related Skills

- [[distributionally-robust-control]] - Distributionally robust control using uncertainty sets
- [[quantum-statistical-estimation-framework]] - Framework combining QFI, sufficient statistics, and quantum metrology
- [[thermodynamic-networks-computation]] - Thermodynamic Networks for autonomous physics-driven computation
