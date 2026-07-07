---
name: topological-subsystem-code-construction
description: Framework for constructing topological subsystem codes using anticommuting quantum spin liquids — extends toric code with spatial modifications creating extensive ground state degeneracy as subsystem degrees of freedom, with local gauge qubits undisturbed by check operators.
trigger: topological subsystem code, anticommuting quantum spin liquid, subsystem qec, toric code subsystem, gauge qubits, lattice geometry qec
category: quantum
---

# Topological Subsystem Code Construction Framework

## Description
Framework for constructing topological subsystem codes based on anticommuting quantum spin liquids. Canonical models are spatial modifications of the toric code that void stabilizer code property, instead containing extensive sets of anticommuting local conserved operators. This degeneracy forms subsystem degrees of freedom. Code inherits many-body topological order from quantum spin liquid. Unique property: extensive number of local gauge qubits undisturbed by check operators apart from logical qubits.

## Activation Keywords
- topological subsystem code
- anticommuting quantum spin liquid
- subsystem qec
- toric code subsystem
- gauge qubits
- lattice geometry qec

## Core Methodology

### Step 1: Base Model Selection
1. Start with anticommuting quantum spin liquid model
2. Canonical model is spatial modification of toric code
3. Model voids stabilizer code property
4. Contains extensive set of anticommuting local conserved operators

### Step 2: Subsystem Code Derivation
1. Extensive ground state degeneracy forms subsystem DOF
2. Code inherits topological order from spin liquid
3. Check operators leave local gauge qubits undisturbed
4. Logical qubits remain encoded in topological sector

### Step 3: Lattice-Specific Construction
1. **Square lattice**: weight-4 local check operator measurements
2. **Kagome lattice**: weight-3 local check operator measurements
3. Adapt measurement schedule to lattice geometry

### Step 4: Implementation
1. Map to hardware-native gate set
2. Optimize measurement circuit depth
3. Leverage extensive gauge qubits for error detection flexibility
4. Suitable for various quantum hardware platforms

## Key Innovations
- **Extensive Gauge Qubits**: Unlike other subsystem codes, local gauge qubits remain undisturbed
- **Low-Weight Checks**: Weight-3 and weight-4 measurements achievable on near-term hardware
- **Template-Based**: Framework provides template for different lattice geometries
- **Topological Protection**: Inherits many-body topological order from parent spin liquid

## When to Use
- Designing fault-tolerant quantum error correction codes
- Implementing topological codes on specific lattice geometries
- Reducing measurement weight in QEC implementations
- Leveraging gauge degrees of freedom for error detection

## Related Papers
- arXiv:2606.26226 — Toric code made subsystem: a framework for topological subsystem codes

## Resources
- arXiv: https://arxiv.org/abs/2606.26226