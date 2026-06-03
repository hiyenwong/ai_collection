---
name: constraint-preserving-quantum-optimization
description: >
  Constraint-preserving quantum optimization methodology using XY-mixers and
  Trotterized Adiabatic Evolution (TAE). Covers constraint handling in quantum
  combinatorial optimization, mixer selection criteria, Trotter error analysis,
  and structure-aware quantum circuit design. Use when working with quantum
  optimization algorithms (QAOA, adiabatic evolution, VQE), constraint handling
  in quantum computing, Trotterization error analysis, XY-mixer implementation,
  or designing quantum circuits for constrained optimization problems.
  Trigger: quantum optimization constraints, XY-mixer, Trotterized adiabatic,
  constraint-preserving quantum, QAOA constraints, quantum mixer design.
---

# Constraint-Preserving Quantum Optimization

Methodology from arXiv:2605.02465 "Constraint Preserving XY-Mixers under Trotterized Adiabatic Evolution" by Awasthi et al.

## Core Insight

Constraint-preserving mixers (e.g., XY-mixers) restrict quantum evolution to feasible subspaces, avoiding penalty-based approaches that increase problem size and distort energy landscapes. However, Trotterization on gate-based hardware introduces approximation errors whose impact depends on **constraint locality**, not total problem size.

## Key Decision Rule: Mixer Selection

| Constraint Structure | Recommended Mixer | Reason |
|---------------------|-------------------|--------|
| Single global equality (all variables) | Pauli-X mixer | Trotter errors in XY-mixer significantly impair performance |
| Multiple disjoint local blocks | XY-mixer | Outperforms X-mixer by orders of magnitude even under Trotterization |
| TSP-like 2-way-1-hot | Dedicated mixer Hamiltonian | See dedicated TSP mixer below |

**Key criterion**: Constraint locality determines XY-mixer effectiveness.

## Trotter Error Analysis

### Error Scaling

- Dominant Trotter error contribution depends on **individual constraint size and structure**
- NOT dependent on total problem size
- For global constraints spanning all n variables: error scales with O(n)
- For k disjoint local constraints of size m: error scales with O(m), independent of n

### Error Mitigation Strategies

1. **Decompose global constraints** into local blocks where possible
2. **Reduce Trotter step count** by using larger time steps with fewer repetitions
3. **Use structure-aware mixer design** matching constraint topology
4. **Combine TAE with variational layers** for hybrid optimization

## Implementation Patterns

### XY-Mixer for Partition Constraints

For constraints where variables partition into groups with fixed sum:

```
H_XY = Σ_{(i,j)∈feasible} (X_i X_j + Y_i Y_j)
```

This preserves Hamming weight within each constraint block.

### TSP 2-Way-1-Hot Mixer

For traveling salesman problem constraints (each city visited exactly once, each time step has exactly one city):

```
H_TSP_mixer = Σ_{city} H_XY(row_city) + Σ_{time} H_XY(col_time)
```

Each row and column forms an independent XY-mixer block.

### Circuit Implementation

1. Decompose XY-mixer into two-qubit gates via Trotterization
2. Apply each constraint block's XY-mixer sequentially
3. Interleave with problem Hamiltonian evolution
4. Use adiabatic schedule: H(t) = (1-t/T)·H_mixer + (t/T)·H_problem

## Workflow for Constrained Quantum Optimization

1. **Identify constraint structure**: Global vs. local, equality vs. inequality
2. **Decompose constraints**: Break global constraints into local blocks if possible
3. **Select mixer**: Use decision rule above
4. **Design Trotter schedule**: Balance step size vs. accuracy
5. **Validate**: Compare with penalty-based baseline on small instances
6. **Scale**: Test on hardware with increasing qubit counts

## Common Pitfalls

- **Penalty method trap**: Adding penalty terms increases circuit depth and distains energy landscapes
- **Global XY-mixer on global constraints**: Trotter errors compound and destroy constraint preservation
- **Ignoring constraint topology**: Mixer must match constraint structure for effectiveness
- **Over-Trotterization**: Too many small steps increase gate count without proportional accuracy gain

## Activation Keywords

- quantum optimization constraints
- XY-mixer
- Trotterized adiabatic evolution
- constraint-preserving quantum
- QAOA constraints
- quantum mixer design
- quantum combinatorial optimization
- Trotter error analysis
- quantum constraint handling
