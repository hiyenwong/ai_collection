---
name: "distributed-quantum-fourier-transform"
description: "Distributed Quantum Fourier Transform (QFT) circuit optimization — circuit partitioning for distributed quantum systems using teleportation to minimize e-bit consumption."
---

# Distributed Quantum Fourier Transform

## Description
Optimizes distributed QFT circuit design by partitioning quantum circuits across multiple quantum processing units (QPUs) using teleportation-based communication. The core optimization objective is minimizing e-bit (entangled bit) consumption during distributed computation. Applicable to any distributed quantum computing architecture where qubits span multiple nodes and inter-node communication is expensive.

## Activation Keywords
- distributed quantum Fourier transform
- distributed QFT circuit
- quantum circuit partitioning
- distributed quantum computing
- e-bit optimization quantum
- teleportation-based distributed quantum
- 分布式量子傅里叶变换
- distributed quantum circuit optimization
- multi-node quantum computing

## Core Concepts

### Problem Statement
- QFT is a fundamental subroutine in many quantum algorithms (Shor's, phase estimation, etc.)
- In distributed settings, qubits are spread across multiple QPUs
- Inter-node quantum communication (teleportation) is expensive
- Goal: minimize e-bit consumption while preserving QFT functionality

### Key Approach
- **Circuit partitioning**: Divide the QFT circuit across distributed nodes
- **Teleportation optimization**: Minimize number of teleportations needed
- **E-bit counting**: Track entangled bit pairs consumed by each inter-node operation
- **Distributed architecture**: Multiple QPUs connected via quantum links

### Complexity Trade-offs
- Sequential QFT: O(n²) gates, single QPU
- Distributed QFT: O(n²) gates total, but spread across k QPUs
- Communication cost: O(k·n) e-bits for k-node partitioning
- Trade-off: more nodes → less per-node qubit requirement, more communication

## Usage Patterns

### Pattern 1: Large-Scale QFT on Small QPUs
When a QFT requires more qubits than any single QPU can hold:
1. Partition qubits across available QPUs
2. Optimize partitioning to minimize inter-node teleportations
3. Execute local QFT sub-circuits on each QPU
4. Coordinate via teleportation for cross-node interactions

### Pattern 2: E-Bit Budget Optimization
When entanglement resources are limited:
1. Analyze QFT circuit structure for cross-node dependencies
2. Reorder operations to batch teleportations
3. Use qubit routing to minimize total e-bit consumption
4. Validate correctness with distributed simulation

### Pattern 3: Heterogeneous QPU Networks
When QPUs have different qubit counts and connectivity:
1. Assign qubits to QPUs based on capacity and connectivity
2. Optimize partitioning for heterogeneous topology
3. Account for varying link fidelities between nodes
4. Schedule operations to overlap computation and communication

## Instructions for Agents

### Step 1: Circuit Analysis
- Analyze the QFT circuit for cross-node gate dependencies
- Identify which qubit pairs interact across node boundaries
- Build the dependency graph of the circuit

### Step 2: Partition Design
- Given k QPUs with capacities c₁, c₂, ..., cₖ:
  - Assign qubits to minimize cross-node interactions
  - Use graph partitioning algorithms (e.g., spectral partitioning)
  - Consider both qubit capacity and connectivity constraints

### Step 3: E-Bit Optimization
- Count e-bits required for each cross-node gate
- Look for opportunities to reorder operations
- Use teleportation merging when multiple gates share the same node pair
- Apply qubit routing to reduce total teleportation count

### Step 4: Validation
- Verify distributed QFT produces correct output distribution
- Compare gate count and e-bit consumption vs. baseline
- Check that all node capacity constraints are satisfied

## Error Handling

### Excessive E-Bit Consumption
- **Problem**: Partitioning requires too many e-bits for available entanglement
- **Solution**: Reduce number of partitions; use SWAP networks within nodes

### Fidelity Degradation
- **Problem**: Teleportation errors accumulate across many hops
- **Solution**: Use error-corrected teleportation; limit maximum hop distance

### Capacity Overflow
- **Problem**: A single QPU cannot hold its assigned qubits
- **Solution**: Re-partition with tighter constraints; use qubit compression

## Related Skills
- `distributed-quantum-computing` — distributed quantum computing patterns
- `quantum-compiler-routing` — qubit routing and compilation
- `qubit-mapping-routing-memoization` — scalable qubit mapping
- `athena-distributed-quantum-compiler` — ATHENA compiler for distributed scheduling
- `dsabre-distributed-quantum-router` — dSABRE routing for multi-core quantum

## Resources
- arXiv: 2606.18494 — "Towards an Optimally Distributed Quantum Fourier Transform Circuit"
