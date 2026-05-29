---
name: quantum-ml-simulation-learning-comparison
description: "Methodology for empirically comparing classical simulation versus sample-based learning of quantum systems. Uses complexity-theoretic analysis of simulability vs learnability, Born-rule statistics reproduction, and empirical benchmarks. Applicable to quantum system characterization, quantum advantage verification, and hybrid quantum-classical algorithm design. Activation: quantum simulation vs learning, sample-based quantum learning, simulability learnability quantum, quantum system characterization, classical simulation benchmark, quantum ML evaluation"
metadata:
  arxiv_id: "2605.28986"
  published: "2026-05-27"
  tags: [quantum, machine-learning, statistics, simulation, learning-theory]
---

# Quantum ML: Simulation vs Sample-Based Learning Comparison

## Core Insight

Classical simulation and sample-based learning both aim to reproduce Born-rule statistics for quantum systems, but complexity-theoretic results show **simulability and learnability need not coincide**. This paper provides an empirical framework for comparing these two approaches.

## Key Concepts

### Simulability vs Learnability

- **Simulation**: Direct computation from a classical description of the quantum system
- **Learning**: Inference from measurement data (samples) alone
- **Key finding**: Systems that are hard to simulate may still be learnable from samples, and vice versa

### Methodology Framework

1. **Define system class** (e.g., random circuits, Hamiltonian evolution)
2. **Set complexity parameters** (circuit depth, qubit count, noise level)
3. **Run classical simulation**: Compute output distribution exactly or approximately
4. **Run sample-based learning**: Train model from measurement data
5. **Compare performance**: Accuracy, computational cost, sample complexity

## Usage Patterns

### Pattern 1: Quantum Advantage Verification

When evaluating whether a quantum system provides computational advantage:

```
1. Identify the quantum task
2. Attempt classical simulation (record time/memory scaling)
3. Train model from measurement samples
4. If simulation is exponentially hard but learning is efficient → quantum advantage claim needs scrutiny
5. If both are hard → genuine quantum advantage likely
```

### Pattern 2: Hybrid Algorithm Design

For designing hybrid quantum-classical algorithms:

```
1. Determine if the target distribution is classically simulable
2. If simulable → use classical simulation for training data generation
3. If not simulable → collect samples from quantum hardware
4. Compare sample efficiency of both approaches
5. Choose the more efficient path for the specific regime
```

### Pattern 3: Quantum System Characterization

For characterizing unknown quantum systems:

```
1. Collect measurement samples from the system
2. Attempt to learn the system behavior from samples
3. Compare with any available classical model
4. Use discrepancy to identify non-classical features
```

## Complexity Classes

| Class | Simulation | Learning | Example |
|-------|-----------|----------|---------|
| Easy-Easy | Efficient | Efficient | Clifford circuits |
| Hard-Easy | Intractable | Efficient | Some random circuits |
| Easy-Hard | Efficient | Intractable | Structured systems |
| Hard-Hard | Intractable | Intractable | Generic quantum systems |

## Activation

- quantum simulation vs learning
- sample-based quantum learning
- simulability learnability quantum
- quantum system characterization
- classical simulation benchmark
- quantum ML evaluation
- Born-rule statistics

## References

- Paper: https://arxiv.org/abs/2605.28986
