# Distributed Quantum Fourier Transform (QFT) Circuit Optimization

## arXiv: 2606.18494
"Towards an Optimally Distributed Quantum Fourier Transform Circuit"

## Core Problem
- QFT is fundamental subroutine (Shor's, phase estimation, etc.)
- In distributed settings, qubits span multiple QPUs
- Inter-node teleportation is expensive
- Goal: minimize e-bit consumption while preserving QFT functionality

## Key Approach
- **Circuit partitioning**: Divide QFT across k QPUs
- **Teleportation optimization**: Minimize teleportations between nodes
- **E-bit counting**: Track entangled bit pairs for each cross-node operation
- **Trade-off**: more nodes → less per-node qubits, more communication (O(k·n) e-bits)

## Usage Patterns

### Pattern 1: Large-Scale QFT on Small QPUs
1. Partition qubits across available QPUs
2. Optimize partitioning to minimize inter-node teleportations
3. Execute local QFT sub-circuits on each QPU
4. Coordinate via teleportation for cross-node interactions

### Pattern 2: E-Bit Budget Optimization
1. Analyze QFT circuit for cross-node gate dependencies
2. Reorder operations to batch teleportations
3. Use qubit routing to minimize total e-bit consumption

### Pattern 3: Heterogeneous QPU Networks
1. Assign qubits to QPUs based on capacity and connectivity
2. Account for varying link fidelities between nodes
3. Schedule operations to overlap computation and communication

## Error Handling
- **Excessive e-bits**: Reduce partitions; use SWAP networks within nodes
- **Fidelity degradation**: Use error-corrected teleportation; limit max hop distance
- **Capacity overflow**: Re-partition with tighter constraints

## Related Skills
- `distributed-quantum-computing` — distributed quantum patterns
- `quantum-compiler-routing` — qubit routing
- `athena-distributed-quantum-compiler` — ATHENA compiler
- `dsabre-distributed-quantum-router` — dSABRE routing
