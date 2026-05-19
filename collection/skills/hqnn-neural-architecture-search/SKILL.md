---
name: hqnn-neural-architecture-search
description: >
  Hybrid Quantum-Classical Neural Architecture Search (HQNN-NAS) methodology
  for designing and optimizing hybrid quantum-classical neural networks using
  hardware-aware FLOPs-constrained search. Applies NAS techniques to HQNN
  architecture design, including data encoding strategies, parameterized quantum
  circuit structures, measurement design, and classical-quantum module coupling.
  Use when designing HQNN architectures, performing quantum NAS, optimizing
  quantum-classical hybrid models for NISQ devices, or FLOPs-aware quantum model
  search. Trigger: HQNN, quantum NAS, hybrid quantum architecture search,
  FLOPs-aware quantum search, neural architecture search quantum, HQNN design.
---

# Hybrid Quantum-Classical Neural Architecture Search (HQNN-NAS)

Methodology from arXiv:2605.18345 (Marchisio et al., May 2026) for applying
Neural Architecture Search to hybrid quantum-classical neural networks (HQNNs)
with hardware-aware FLOPs constraints.

## Core Architecture

### HQNN Components

```
Input -> Classical Encoder -> Quantum Circuit -> Measurement -> Classical Decoder -> Output
```

- **Data Encoding**: Amplitude, angle, or basis encoding mapped to qubit states
- **Parameterized Quantum Circuit (PQC)**: Rotations + entangling layers
- **Measurement**: Observable expectation values as classical features
- **Classical Coupling**: Fully connected or convolutional layers before/after quantum

### Key Design Decisions

1. **Encoding strategy**: Choose based on input dimensionality and qubit count
   - Amplitude encoding: O(log n) qubits, efficient for high-dim data
   - Angle encoding: O(n) qubits, preserves feature structure
   - Basis encoding: O(n) qubits, direct binary mapping

2. **Circuit structure**: Layers of single-qubit rotations + entangling gates
   - Hardware-efficient ansatz: Native gate set matching device topology
   - Data re-uploading: Iterative encoding for expressive power

3. **Measurement design**: Select observables that capture relevant features
   - Single-qubit Z measurements: Simple, low overhead
   - Correlator measurements: Capture multi-qubit correlations

4. **Classical-quantum coupling**: Where to place classical layers
   - Classical->Quantum->Classical (sandwich): Most common
   - Multi-layer interleaving: Deeper hybrid architectures

## FLOPs-Aware Search

### Search Space Definition

```python
search_space = {
    "encoder_type": ["amplitude", "angle", "basis"],
    "circuit_depth": [2, 4, 6, 8],
    "entanglement_pattern": ["linear", "circular", "full"],
    "measurement_type": ["single", "correlator"],
    "classical_pre_layers": [0, 1, 2],
    "classical_post_layers": [1, 2, 3],
}
```

### FLOPs Calculation Proxy

Estimate computational cost as FLOPs proxy:
- Quantum FLOPs: O(depth * n_qubits^2) for entangling gates
- Classical FLOPs: O(layers * hidden_dim^2)
- Total = quantum_flops + classical_flops

### Hardware Constraints

```python
hardware_constraints = {
    "max_qubits": device.n_qubits,
    "max_circuit_depth": device.coherence_time / device.gate_time,
    "max_flops": compute_budget,
    "native_gates": device.native_gate_set,
    "topology": device.coupling_map,
}
```

## Search Strategies

### 1. Random Search with FLOPs Filtering
- Sample architectures uniformly
- Filter by hardware constraints
- Evaluate feasible candidates

### 2. Evolutionary Search
- Population of architectures
- Mutation: modify single hyperparameter
- Crossover: combine parent architectures
- Selection: accuracy + FLOPs penalty

### 3. Reinforcement Learning NAS
- Controller RNN generates architecture descriptions
- Reward = validation_accuracy - lambda * normalized_flops
- Proximal policy optimization for training controller

## Workflow

1. Define hardware constraints from target device
2. Specify search space with valid ranges
3. Choose search strategy (random/evolutionary/RL)
4. Run search with FLOPs budget constraint
5. Evaluate Pareto front of accuracy vs FLOPs
6. Select architecture on Pareto front for deployment

## NISQ Considerations

- **Noise resilience**: Prefer shallower circuits on noisy devices
- **Barren plateaus**: Limit circuit depth to avoid vanishing gradients
- **Hardware mapping**: Account for device-specific gate fidelities
- **Shot noise**: Budget for finite measurement shots
