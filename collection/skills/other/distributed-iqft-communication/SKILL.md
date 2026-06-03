---
name: distributed-iqft-communication
description: Communication-efficient distributed inverse QFT reducing inter-node quantum communication from O(P²) to O(P) via threshold-driven pruning of controlled-phase rotations. Use when designing distributed quantum algorithms, scaling quantum circuits across multiple QPUs, or optimizing quantum network communication.
---

# Distributed Inverse QFT with Communication Efficiency

## Core Concept

Execute inverse Quantum Fourier Transform (iQFT) across P distributed quantum nodes by pruning remote controlled-phase gates whose impact falls below a threshold ("communication horizon"), reducing quantum communication complexity from O(P²) to O(P).

## Technical Approach

1. **Distributed iQFT**: Split n-qubit register across P nodes (Q qubits each)
2. **Communication Horizon**: Prune controlled-phase gates beyond threshold distance
3. **Exponential Decay**: Controlled-phase rotation significance decreases exponentially with qubit distance
4. **Linear Scaling**: Entanglement consumption per node saturates to constant

## Key Results

- Communication complexity: O(P²) → O(P) with negligible accuracy loss
- Functional correctness preserved for practical threshold values
- Entanglement resource consumption per node becomes constant
- Directly applicable to distributed Shor's algorithm, phase estimation

## Usage Patterns

### Pattern 1: Distributed QFT Design
1. Partition n-qubit register across available QPUs
2. Implement local iQFT gates within each node
3. Apply communication horizon: skip inter-node gates below threshold
4. Verify accuracy vs. full iQFT meets requirements

### Pattern 2: Quantum Network Protocol
1. Establish entanglement links between nodes
2. Execute distributed iQFT with pruned communication
3. Coordinate measurement results classically
4. Aggregate output for downstream algorithm

## Activation Keywords
- distributed inverse QFT
- quantum Fourier transform distributed
- communication-efficient quantum algorithm
- quantum network iQFT
- multi-QPU quantum computing
- quantum communication pruning
