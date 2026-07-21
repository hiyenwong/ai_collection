---
name: quantum-modular-forms-partitions
description: "Number theory partition statistics methodology connecting restricted excludant statistics in parity-distinct partitions with quantum modular forms via q-series transformations."
tags: ["number-theory", "partitions", "quantum-modular-forms", "q-series", "combinatorics"]
related_skills: ["quantum-number-theory", "quantum-number-theory-algorithms"]
---

# Quantum Modular Forms and Partition Statistics

Methodology for studying restricted excludant statistics in partition theory through the lens of quantum modular forms. Based on arXiv:2603.13915.

## Core Concept

Studies restricted excludant statistics depending on parity in partitions where parts with same parity are distinct. Uses q-series transformations to show that generating functions of these partition statistics are related to quantum modular forms — bridging combinatorial number theory with quantum modular objects.

## Methodology

### Partition Statistics

1. **Parity-distinct partitions**: Partitions where parts of the same parity are distinct
2. **Excludant statistics**: Statistics based on excluded parts from the partition
3. **Parity dependence**: Different statistical behavior for odd vs. even exclusions
4. **Generating functions**: q-series encoding the partition statistics

### q-Series Transformations

1. **Rogers-Ramanujan type identities**: Transformations relating different partition generating functions
2. **Mock theta connections**: Relations to Ramanujan's mock theta functions
3. **Quantum modularity**: Transformation properties under modular group action

### Quantum Modular Forms

1. **Definition**: Functions with modular-like transformation properties but defined on rationals
2. **Asymptotic expansions**: Connection to partition asymptotics
3. **Analytic continuation**: Extension from discrete to continuous domain

## Mathematical Framework

```
Partition generating function:
  P(q) = Σ_{n≥0} p(n) q^n

Excludant statistics generating function:
  E_k(q) = Σ_{n≥0} e_k(n) q^n
  
Quantum modular form relation:
  E_k(q) ~ f(τ)  where q = e^{2πiτ}
  f(γτ) = (cτ+d)^k f(τ) + r(τ)  (quantum modularity)
```

## Applications

- **Partition asymptotics**: Precise asymptotic behavior of restricted partitions
- **Mock modular forms**: Connection to Ramanujan's mock theta functions
- **Quantum invariants**: Relations to quantum knot invariants and 3-manifold invariants
- **Statistical mechanics**: Partition functions of lattice models

## Implementation Considerations

- **q-series convergence**: Radius of convergence and analytic continuation
- **Modular transformation**: Behavior under SL(2,Z) action
- **Numerical evaluation**: Efficient computation of partition statistics

## Activation

**Keywords**: partition statistics, quantum modular forms, q-series, Rogers-Ramanujan, mock theta functions, number theory, combinatorics, excludant statistics, parity-distinct partitions, restricted partitions
**arXiv**: 2603.13915
**Categories**: math.NT
