# Constraint-Preserving Quantum Mixers — Session Notes (2026-05-07)

## Core Decision Rule: Constraint Locality

The key criterion for mixer selection is **constraint locality**, not problem size.

### XY-Mixer: When to Use
- Constraints decompose into **multiple disjoint local blocks**
- Each block involves a small subset of variables (e.g., one-hot encoding per city in TSP)
- Trotter errors remain localized within blocks
- Example: TSP with one-hot encoding — each city's qubits form a local block

### Pauli-X Mixer: When to Use
- Constraints form a **single global equality** spanning all variables
- Trotter errors would propagate across the entire system
- Hardware noise already dominates (≥25-30 qubits on current IBM hardware)

## Trotterized Adiabatic Evolution (TAE) Findings

- Trotter errors depend on the **size and structure of individual constraints**, NOT total problem size
- For single global equality constraints: Trotter errors significantly impair XY-mixer → use Pauli-X
- For multiple disjoint local blocks: XY-mixers outperform X-mixers by orders of magnitude even under Trotterization
- Dedicated mixer Hamiltonian exists for TSP-like 2-way-1-hot constraints

## Compressed AQC-QAOA

- Compress early segments of digitized adiabatic evolution into shallow circuits
- Use as initialization for variational QAOA layers
- Moderate prefix compression reduces two-qubit gate depth while maintaining feasible solution discovery
- Works best for routing problems (VRP, TSP, facility location)
- Requires compatibility between compressed prefix and variational ansatz
- Standard QAOA leverages AQC initialization well; linear-chain QAOA shows limited improvement

## Source Papers

- Awasthi et al., "Constraint Preserving XY-Mixers under Trotterized Adiabatic Evolution" (arxiv 2026-05-04)
- Azfar et al., "Hardware-Efficient Quantum Optimization for Transportation Networks via Compressed Adiabatic Evolution" (arxiv 2026-04-28)
