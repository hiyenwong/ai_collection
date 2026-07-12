---
name: constraint-preserving-quantum-mixers
description: >
  Constraint-preserving quantum mixer patterns for combinatorial optimization on NISQ hardware.
  Covers XY-mixer vs Pauli-X mixer selection criteria, Trotterized Adiabatic Evolution (TAE),
  compressed AQC-QAOA initialization, and QUBO formulation strategies. Use when designing
  quantum optimization circuits for constrained problems (VRP, TSP, portfolio optimization,
  network security), choosing mixer Hamiltonians, or encoding combinatorial problems for
  quantum solvers (QAOA, adiabatic evolution, variational quantum optimization).
---

# Constraint-Preserving Quantum Mixers

## Core Insight

Constraint handling in quantum optimization has two competing approaches:
- **Penalty methods**: Add constraint terms to cost Hamiltonian — simple but distort energy landscapes
- **Constraint-preserving mixers** (XY-mixers): Restrict evolution to feasible subspace — theoretically superior but require Trotterization

The key decision criterion is **constraint locality**, not problem size.

## Mixer Selection Rule

### Use XY-Mixer when:
- Constraints decompose into **multiple disjoint local blocks**
- Each block involves a small subset of variables (e.g., one-hot per city in TSP)
- Trotter errors remain localized within blocks

### Use Pauli-X Mixer when:
- Constraints form a **single global equality** spanning all variables
- Trotter errors would propagate across the entire system
- Hardware noise already dominates (NISQ scaling boundary ~25-30 qubits at p=1)

## Compressed AQC-QAOA Initialization

Instead of standard QAOA from uniform superposition:
1. Compress early segments of digitized adiabatic evolution into shallow circuits (AQC)
2. Use compressed prefix as initialization for variational layers
3. Trade-off: reduced two-qubit gate depth vs. expressivity loss

**Key finding**: Moderate prefix compression improves feasible solution discovery for routing problems, but effectiveness depends on compatibility between compressed prefix and variational ansatz.

## QUBO Formulation Patterns

### Problems admitting direct QUBO:
- Two-way partitioning with all-or-nothing cut
- Portfolio optimization with budget constraint
- Subgroup discovery (feature selection as binary optimization)

### Problems requiring higher-order objectives:
- k-way hypergraph partitioning (k > 2)
- General hyperedge cut functions
- Multi-commodity flow with capacity constraints

### Encoding strategy:
1. Identify binary decision variables
2. Express objective as quadratic form x^T Q x
3. Encode constraints as penalty terms or use constraint-preserving mixers
4. Validate: check that ground state corresponds to optimal feasible solution

## NISQ Scaling Boundary

Empirical results on IBM hardware (ibm_pittsburgh, 127 qubits):
- QAOA at depth p=1 maintains >97% WRAcc ratio up to 15 qubits
- Degrades to ~85% at 20 qubits
- Drops below 65% at 25 qubits (circuit noise dominates)
- Near-zero signal at 30 qubits

This establishes a practical boundary for near-term quantum optimization.

## TSP-like 2-way-1-hot Constraints

For problems with one-hot encoding (exactly one option per group):
- Use dedicated XY-mixer Hamiltonian preserving the one-hot subspace
- Each group's qubits form a local block — XY-mixer excels
- Trotterization error scales with block size, not total problem size

## References

- Awasthi et al., "Constraint Preserving XY-Mixers under Trotterized Adiabatic Evolution" (2026)
- Azfar et al., "Hardware-Efficient Quantum Optimization for Transportation Networks via Compressed Adiabatic Evolution" (2026)
- Spell & Shyu, "Formulating Subgroup Discovery as a Quantum Optimization Problem for Network Security" (2026)
- Li et al., "Quantum Hypergraph Partitioning" (2026)
