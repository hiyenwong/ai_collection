---
name: constraint-locality-xy-mixer-design
description: "XY-mixer design methodology under Trotterized adiabatic evolution. Key finding: XY-mixer effectiveness depends on constraint locality — global constraints spanning all variables suffer from Trotter errors, while disjoint local constraint blocks excel even under Trotterization. Use when designing constraint-preserving quantum mixers, implementing XY-mixers on gate-based hardware, or choosing between XY-mixer and Pauli-X mixer for constrained combinatorial optimization."
category: quantum-finance
---

# Constraint Locality XY-Mixer Design

## Description

Systematic investigation of constraint-preserving XY-mixers under Trotterized Adiabatic Evolution (TAE) for combinatorial optimization on gate-based quantum hardware.

## Key Finding: Constraint Locality Criterion

**XY-mixer effectiveness depends on constraint locality, not total problem size.**

| Constraint Type | Trotter Error Impact | Mixer Choice |
|----------------|---------------------|--------------|
| Single global equality constraint (all variables) | Significant degradation | Use standard Pauli-X mixer |
| Multiple disjoint local blocks | Minimal degradation, excels | Use XY-mixer |

## Theory

### XY-Mixer Hamiltonian
```
H_XY = Σ_{(i,j)∈E} (X_i X_j + Y_i Y_j)
```
Restricts evolution to feasible subspace, preserving constraints like Hamming weight.

### Trotterization Error Scaling
The dominant Trotter error contribution depends on the **size and structure of individual constraints**, not on the total problem size. This is critical because:

```
‖[A, [A, B]]‖ dominates the second-order Trotter error
```

where A and B are the non-commuting terms in the Hamiltonian decomposition.

## Design Decision Process

1. **Identify constraint structure**: Does the problem have one global constraint or multiple local blocks?
2. **If global**: Trotter errors significantly impair XY-mixer → use Pauli-X mixer
3. **If local/disjoint**: XY-mixer outperforms X-mixer by orders of magnitude → use XY-mixer
4. **For TSP-like constraints**: Use dedicated 2-way-1-hot mixer Hamiltonian

## Validation Problems

The methodology was validated on three representative problems:

| Problem | Constraint Structure | Best Mixer |
|---------|---------------------|------------|
| Portfolio Optimization | Global cardinality | Pauli-X (under Trotterization) |
| Multi-Car Paint Shop | Local blocks | XY-mixer |
| Multi-Commodity Flow | Local blocks | XY-mixer |

## When to Use

- Designing QAOA/adiabatic mixers for constrained optimization
- Implementing XY-mixers on NISQ devices requiring Trotterization
- Portfolio optimization, routing, scheduling with hard constraints
- Choosing between constraint-preserving and penalty-based approaches

## Activation Keywords

- XY-mixer design
- Trotterized adiabatic evolution
- constraint locality
- constraint-preserving mixer
- combinatorial optimization quantum
- quantum portfolio optimization mixer
- TAE mixer selection

## References

- arXiv:2605.02465 — "Constraint Preserving XY-Mixers under Trotterized Adiabatic Evolution"