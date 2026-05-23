---
name: qaoa-interaction-threshold
description: Sharp interaction-degree threshold for simulating QAOA (Quantum Approximate Optimization Algorithm). Identifies the critical interaction degree at which classical simulation of QAOA becomes intractable. Use when: QAOA complexity analysis, quantum advantage assessment, classical simulation limits, interaction degree analysis, quantum-classical boundary studies.
---

# QAOA Interaction-Degree Threshold

## Core Concept

Identifies a sharp interaction-degree threshold for simulating QAOA circuits. Below the threshold, efficient classical simulation is possible; above it, quantum advantage emerges.

## Key Findings

1. **Sharp Threshold**: A critical interaction degree k_c exists where simulation complexity transitions
2. **Classical Regime**: For interaction degree k < k_c, tensor network methods simulate efficiently
3. **Quantum Regime**: For k > k_c, simulation complexity grows exponentially
4. **Phase Transition**: The threshold represents a computational phase transition

## Analysis Framework

### Interaction Degree Computation
1. Analyze QAOA circuit structure (mixer and cost Hamiltonian)
2. Compute interaction graph from two-qubit gate pattern
3. Calculate interaction degree k (max degree of interaction graph)
4. Compare against threshold k_c

### Simulation Complexity Estimation
- Tensor network contraction cost: O(exp(k)) for degree-k interactions
- Threshold k_c: depends on system size, QAOA depth, and hardware constraints
- Below threshold: use tensor network contraction
- Above threshold: require quantum hardware or approximate methods

## Applications

- **QAOA Circuit Design**: Optimize circuit structure relative to threshold
- **Quantum Advantage Prediction**: Determine when QAOA surpasses classical methods
- **Hybrid Algorithm Design**: Partition problems around simulation threshold
- **Benchmarking**: Use threshold as quantum-classical boundary metric

## Activation Keywords
- QAOA simulation threshold
- interaction degree QAOA
- quantum advantage boundary
- QAOA complexity analysis
- classical simulation QAOA
- computational phase transition
- QAOA 模拟阈值

## Related Skills
- quantum-optimization-qaoa
- qaoa-optimization
- quantum-algorithm-framework-designer
