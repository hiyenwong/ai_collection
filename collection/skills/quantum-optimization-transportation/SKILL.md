---
name: quantum-optimization-transportation
description: "Apply quantum optimization algorithms to transportation network problems including vehicle routing, urban logistics, and infrastructure planning. Covers compressed adiabatic evolution, constraint-preserving XY-mixers, QAOA variants, and hardware-efficient formulations. Use when formulating transportation combinatorial optimization as quantum problems, implementing constraint-preserving quantum mixers, or optimizing hardware resource usage for quantum annealing."
---

# Quantum Optimization for Transportation Networks

Map large-scale transportation combinatorial optimization problems to quantum-compatible formulations with hardware-efficient implementations.

## Activation Keywords
- quantum transportation optimization
- quantum vehicle routing
- compressed adiabatic evolution
- constraint-preserving quantum mixers
- quantum logistics
- hardware-efficient quantum optimization
- quantum network optimization

## Problem Classes

### Transportation Problems
- **Vehicle Routing Problem (VRP)**: Minimize fleet travel cost with capacity/time constraints
- **Traffic Flow Optimization**: Signal timing, route assignment
- **Infrastructure Planning**: Network design, facility location
- **Subgroup Discovery for Network Security**: Interpretable rule generation

### Quantum Formulations
- **QUBO**: Quadratic Unconstrained Binary Optimization
- **Ising Model**: Spin glass formulation
- **Adiabatic Evolution**: Slow evolution from easy to hard Hamiltonian

## Formulation Workflow

### Step 1: Problem Encoding
Map decision variables to qubits:
- Binary variables → single qubit
- Integer variables → binary encoding (log n qubits)
- Permutation variables → one-hot encoding (n² qubits)

### Step 2: Constraint Handling
Two approaches:
1. **Penalty-based**: Add λ·constraint² to objective
   - Increases problem size, distorts energy landscape
   - Risk of infeasible solutions
2. **Constraint-preserving mixers**: XY-mixers under Trotterized evolution
   - Maintain feasibility throughout evolution
   - No penalty parameter tuning needed

### Step 3: Hardware-Efficient Mapping
Compressed adiabatic evolution:
- Reduce circuit depth via compression
- Map to available qubit connectivity
- Minimize SWAP gate overhead

### Step 4: Algorithm Selection
- **QAOA**: Near-term NISQ devices, shallow circuits
- **Adiabatic**: Quantum annealers (D-Wave), full connectivity
- **Compressed adiabatic**: Balance between depth and expressivity

## Key Techniques

### XY-Mixer for Constraints
For constraint Ax = b:
- Design mixer Hamiltonian that preserves constraint subspace
- Trotterized evolution maintains feasibility
- Avoids penalty-based approach drawbacks

### Compression Strategy
1. Identify redundant terms in Hamiltonian
2. Apply Trotter-Suzuki decomposition
3. Merge commuting terms
4. Result: shorter circuit, same approximation quality

## Performance Metrics
- **Approximation ratio**: Solution quality vs. optimal
- **Circuit depth**: Hardware resource requirement
- **Constraint satisfaction**: Feasibility of solutions
- **Qubit count**: Scalability indicator

## Common Pitfalls
- One-hot encoding explodes qubit count for large problems
- Penalty methods require careful λ tuning
- Connectivity mismatch causes SWAP overhead
- Decoherence limits adiabatic evolution time

## References
- Hardware-Efficient Quantum Optimization for Transportation Networks (arxiv 2604.26175)
- Constraint Preserving XY-Mixers under Trotterized Adiabatic Evolution (arxiv 2605.02465)
- Formulating Subgroup Discovery as Quantum Optimization (arxiv 2604.27153)
- Quantum Hypergraph Partitioning (arxiv 2605.02635)
