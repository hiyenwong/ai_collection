---
name: quantum-transportation-optimization
description: >
  Hardware-efficient quantum optimization for transportation networks using
  Approximate Quantum Compilation (AQC) to compress adiabatic evolution into
  shallow circuits combined with variational layers. Covers VRP, TSP, FLP
  quantum formulations, AQC-QAOA hybrid methods, circuit compression for
  near-term quantum hardware, and quantum algorithms as candidate generators
  in transportation decision workflows. Use when optimizing transportation
  networks (vehicle routing, facility location, logistics) with quantum
  computing, implementing hybrid quantum-classical optimization, or designing
  shallow quantum circuits for combinatorial optimization on NISQ hardware.
  Trigger: quantum transportation, AQC-QAOA, compressed adiabatic evolution,
  quantum vehicle routing, quantum logistics, hardware-efficient quantum optimization.
---

# Quantum Transportation Optimization

Methodology from arXiv:2604.26175 "Hardware-Efficient Quantum Optimization for Transportation Networks via Compressed Adiabatic Evolution" by Azfar et al.

## Core Insight

Approximate Quantum Compilation (AQC) compresses early segments of digitized adiabatic evolution into shallow circuits, which are then combined with variational layers. This enables systematic study of how initialization, circuit depth, and expressivity interact on near-term quantum hardware.

## Transportation Problems as Quantum Optimization

### Problem Formulations

| Problem | Encoding | Constraints |
|---------|----------|-------------|
| VRP (Vehicle Routing) | Binary assignment variables | Each customer visited once, capacity limits |
| TSP (Traveling Salesman) | 2-way-1-hot matrix | Each city once, each position once |
| FLP (Facility Location) | Binary open/assign vars | Assignment only to open facilities |

### QUBO Formulation Pattern

```
H = H_objective + λ₁·H_constraint1 + λ₂·H_constraint2 + ...
```

Where penalty weights λ must balance constraint satisfaction vs. objective optimization.

## AQC-QAOA Hybrid Method

### Architecture

```
[AQC Compressed Prefix] → [Variational QAOA Layers] → [Measurement]
```

1. **AQC Prefix**: Compresses early adiabatic evolution (small Γ→small Γ) into shallow circuit
2. **Variational Layers**: Standard QAOA mixer+problem unitals with trainable parameters
3. **Combined**: Circuit acts as stochastic candidate generator

### Compression Benefits

- **Reduces two-qubit gate depth** while maintaining solution quality
- **Better initialization** for variational optimization
- **Hardware-efficient** for NISQ devices with limited coherence

### Compatibility Requirement

- **Standard QAOA ansatz** effectively leverages AQC initialization
- **Linear-chain QAOA** shows limited improvement from AQC prefix
- Compression benefit depends on ansatz-prefix compatibility

## Workflow for Transportation Quantum Optimization

1. **Formulate problem** as QUBO with appropriate constraints
2. **Design adiabatic path** from mixer to problem Hamiltonian
3. **Compress prefix** using AQC to target circuit depth
4. **Append variational layers** with trainable parameters
5. **Execute on hardware** as stochastic candidate generator
6. **Post-process** candidates for feasibility
7. **Iterate** with updated variational parameters

## Hardware Considerations

- Experiments validated on IBM gate-based quantum computers
- Moderate prefix compression optimal: too much loses adiabatic benefit
- Circuit depth must respect hardware coherence limits
- Two-qubit gate count is primary bottleneck

## Integration with Classical Workflows

Quantum algorithms serve as **candidate generators** within classical transportation decision-making:

1. Quantum circuit generates diverse candidate solutions
2. Classical post-processing filters for feasibility
3. Classical optimizer refines best candidates
4. Hybrid loop: quantum exploration + classical exploitation

## Common Pitfalls

- **Penalty weight tuning**: λ too small → infeasible solutions; λ too large → flat landscape
- **Over-compression**: Losing adiabatic advantage by compressing too much of the path
- **Ansatz mismatch**: AQC prefix must be compatible with variational layers
- **Ignoring feasibility**: Quantum outputs may violate constraints; classical filtering required

## Activation Keywords

- quantum transportation
- AQC-QAOA hybrid
- compressed adiabatic evolution
- quantum vehicle routing
- quantum logistics optimization
- hardware-efficient quantum
- quantum TSP
- quantum facility location
- Approximate Quantum Compilation
