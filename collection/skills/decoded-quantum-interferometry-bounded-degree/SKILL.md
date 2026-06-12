---
name: decoded-quantum-interferometry-bounded-degree
description: "Complexity-theoretic benchmark for decoded quantum interferometry (DQI), QAOA, and classical heuristics on bounded-degree max-Ek-LINSAT. Extends NP-hardness to arbitrary finite fields F_q with bounded degree D, proving hardness to exceed r/q + O(1/sqrt(D)). Identifies 1/sqrt(D log D) classical decoder barrier vs. 1/sqrt(D) quantum decoder scaling. arXiv: 2606.13570"
category: quantum/optimization
metadata:
  arxiv_id: "2606.13570"
  authors: "Maximilian J. Kramer, Carsten Schubert, Jens Eisert"
  subjects: "quant-ph,cs.CC,cs.DS"
  published_date: "2026-06-11"
---

## Context

For general max-k-XORSAT with k>=3, no polynomial-time algorithm can substantially beat random guessing on worst-case instances unless P=NP. However, bounded-degree instances (each variable appears in at most D constraints) are algorithmically easier — polynomial-time algorithms can beat the random baseline by O(1/sqrt(D)). This work extends the hardness analysis to bounded-degree max-Ek-LINSAT over arbitrary finite fields F_q and establishes the complexity-theoretic benchmark for DQI, QAOA, and classical heuristics.

## Core Methodology

### Hardness Extension to Finite Fields

For max-Ek-LINSAT(q,r) with bounded degree D over F_q:
- It is NP-hard to exceed r/q + O_{q,r}(1/sqrt(D))
- This extends the Boolean case (Trevisan/Barak) to arbitrary finite fields
- Provides the complexity-theoretic ceiling for any algorithm (classical or quantum)

### DQI Decoder Scaling Analysis

1. **Classical Decoder Barrier**: DQI with classical decoders faces an information-theoretic `1/sqrt(D log D)` barrier
   - This prevents matching the complexity-theoretic `1/sqrt(D)` scaling
   - Represents a fundamental limitation of classical post-processing

2. **Quantum Decoder Compatibility**: DQI with quantum decoders is compatible with the `1/sqrt(D)` scaling
   - Identifies quantum decoding as the key ingredient for matching complexity-theoretic bounds
   - Provides a clear target for quantum advantage demonstrations

### Implications for QAOA

- QAOA on bounded-degree instances is similarly constrained by the `1/sqrt(D)` ceiling
- Any quantum advantage is confined to improving the constant prefactor
- The hardness result establishes when QAOA can/cannot outperform classical methods

### Algorithmic Benchmarking Framework

```
For bounded-degree optimization:
1. Compute the random assignment baseline: r/q
2. The hardness ceiling: r/q + O(1/sqrt(D))
3. Classical algorithm target: r/q + O(1/sqrt(D)) — achievable
4. DQI classical decoder: r/q + O(1/sqrt(D log D)) — suboptimal
5. DQI quantum decoder: r/q + O(1/sqrt(D)) — optimal
6. QAOA: depends on depth and angle optimization
```

## Implementation Steps

### Step 1: Problem Formulation
```
Input: Linear system over F_q with k variables per equation, max degree D
Output: Assignment maximizing satisfied equations

Parameters:
- q: Field size (q=2 for Boolean)
- k: Number of variables per equation
- D: Maximum degree (variable occurrences)
- r: Target satisfaction ratio
```

### Step 2: Classical Baseline Computation
- Random assignment achieves r/q expected satisfaction
- For k>=3, NP-hard to beat this by more than O(1/sqrt(D)) on worst-case instances
- Polynomial-time algorithms can achieve O(1/sqrt(D)) improvement on bounded-degree instances

### Step 3: DQI Protocol
```
DQI Protocol:
1. Encode the optimization problem into a quantum circuit
2. Apply the quantum interference pattern
3. Decode measurement outcomes:
   a. Classical decoder: achieves O(1/sqrt(D log D)) — below optimal
   b. Quantum decoder: achieves O(1/sqrt(D)) — matches hardness ceiling
4. Return best assignment
```

### Step 4: QAOA Comparison
```
QAOA Protocol:
1. Construct cost Hamiltonian from max-Ek-LINSAT instance
2. Optimize variational angles (p layers)
3. Sample and decode
4. Performance bounded by O(1/sqrt(D)) ceiling
```

### Step 5: Benchmarking
```
Benchmark Protocol:
1. Generate (k,D)-regular instances over F_q
2. Run: random baseline, classical algorithm, DQI (classical/quantum decoder), QAOA
3. Compare achieved approximation ratios against hardness ceiling
4. Identify regimes where quantum methods show advantage
```

## Pitfalls

- **Bounded-Degree Assumption**: Results only apply to bounded-degree instances. For unbounded-degree instances, the hardness is much stronger (NP-hard to beat 1/2 by any constant for k>=3). **Fix**: Verify degree bounds before applying these results.
- **Constant Prefactor Focus**: On bounded-degree instances, quantum advantage is only in the constant prefactor, not asymptotic scaling. **Implication**: Advantage may be small and hard to demonstrate experimentally.
- **Classical Decoder Barrier**: The `1/sqrt(D log D)` barrier for classical decoders is information-theoretic, not computational. **Implication**: No classical decoding strategy (regardless of computational power) can overcome this barrier within the DQI framework.
- **Field Generalization**: The extension to arbitrary F_q introduces q,r-dependent constants. **Implication**: The exact scaling constants depend on field parameters.
- **Worst-Case vs. Average-Case**: Hardness results are worst-case. **Implication**: Average-case instances may be easier. Distinguish between worst-case hardness and practical performance.

## Verification

1. **Hardness Bound**: Verify the NP-hardness proof for max-Ek-LINSAT(q,r) with bounded degree D.
2. **DQI Classical Barrier**: Confirm the `1/sqrt(D log D)` information-theoretic barrier for classical decoders.
3. **DQI Quantum Compatibility**: Verify that quantum decoders can achieve `1/sqrt(D)` scaling.
4. **QAOA Ceiling**: Confirm QAOA is similarly bounded by `1/sqrt(D)`.
5. **Empirical Validation**: Test on concrete bounded-degree instances and compare achieved ratios against bounds.

## Activation

decoded quantum interferometry, bounded degree optimization, max-LINSAT hardness, quantum decoder advantage, DQI classical barrier, QAOA bounded degree, finite field satisfiability, approximation hardness quantum, complexity-theoretic quantum benchmark, information-theoretic decoder barrier