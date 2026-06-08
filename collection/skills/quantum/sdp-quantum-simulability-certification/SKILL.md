---
name: sdp-quantum-simulability-certification
category: quantum-information-science
description: Semidefinite programming (SDP) hierarchy methodology for certifying quantum advantage — characterizing classically simulable quantum state families, computing critical visibility bounds, and constructing affine witnesses.
source: arxiv
source_url: https://arxiv.org/abs/2606.06204
arxiv_id: 2606.06204
authors: Mengyan Li, Yanning Jia, Fenzhuo Guo, Haifeng Dong, Sujuan Qin, Fei Gao
tags:
  - quantum-information
  - semidefinite-programming
  - quantum-advantage
  - classical-simulability
  - resource-theory
  - convex-optimization
  - POVM
  - quantum-witnesses
---

# SDP Hierarchy for Quantum Simulability Certification

## Background

Determining whether a quantum state family provides an irreducible quantum advantage (i.e., cannot be classically simulated) is fundamental in quantum resource theory and quantum information processing. A state family is **classically simulable** if it resides within the convex hull of pairwise commuting families.

## Core Methodology

### 1. Reformulating Classical Simulability as SDP Feasibility

Classical simulability is reformulated as a feasibility problem over:
- Deterministic response functions
- Auxiliary POVMs simulable by rank-one projective measurements

### 2. Complete SDP Hierarchy

**Step 1: Characterize rank-one projectively simulable POVMs**
- Build an SDP hierarchy that fully characterizes which POVMs can be simulated by rank-one projective measurements
- Each level of the hierarchy provides a tighter relaxation

**Step 2: Transfer to state families**
- Use the POVM characterization to build an SDP hierarchy for state families
- Yields **primal feasibility tests** (can this state family be classically simulated?)
- Yields **dual affine witnesses** (certificates that classical simulability fails)

### 3. Computing Critical Classical Visibility

For state families mixed with depolarizing noise:
- The SDP hierarchy gives **computable upper bounds** on the critical classical visibility
- These bounds indicate the noise level at which quantum advantage disappears
- In symmetric examples, the bounds are tight (matched by explicit classical simulations)

## Implementation Guide

### Primal Feasibility Test (Can this state family be classically simulated?)

```python
import cvxpy as cp
import numpy as np

def test_classical_simulability(states, noise_level):
    """Test if a family of noisy states can be classically simulated."""
    n = states[0].shape[0]
    k = len(states)
    noisy_states = [(1 - noise_level) * rho + noise_level * np.eye(n) / n 
                    for rho in states]
    # SDP: find commuting ensemble and mixing weights
    P = cp.Variable((k, k), symmetric=True)
    sigmas = [cp.Variable((n, n), hermitian=True) for _ in range(k)]
    constraints = []
    for i in range(k):
        constraints += [sigmas[i] >> 0, cp.trace(sigmas[i]) == 1]
        constraints += [P[:, i] >= 0, cp.sum(P[:, i]) == 1]
    for i in range(k):
        for j in range(i + 1, k):
            constraints += [sigmas[i] @ sigmas[j] == sigmas[j] @ sigmas[i]]
    for j in range(k):
        reconstructed = sum(P[i, j] * sigmas[i] for i in range(k))
        constraints += [reconstructed == noisy_states[j]]
    problem = cp.Problem(cp.Minimize(0), constraints)
    problem.solve(solver=cp.SCS, verbose=False)
    return problem.status in ['optimal', 'optimal_inaccurate'], {'status': problem.status}
```

### Dual Witness Construction

```python
def construct_non_simulability_witness(states):
    """Construct affine witness certifying non-simulability."""
    n = states[0].shape[0]
    W = cp.Variable((n, n), hermitian=True)
    target = states[0]
    objective = cp.Maximize(cp.real(cp.trace(W @ target)))
    problem = cp.Problem(objective)
    problem.solve()
    return W.value
```

### Critical Visibility Computation

```python
def compute_critical_visibility(states, tol=1e-3):
    """Binary search for critical noise level at which quantum advantage disappears."""
    lo, hi = 0.0, 1.0
    while hi - lo > tol:
        mid = (lo + hi) / 2
        feasible, _ = test_classical_simulability(states, mid)
        if feasible:
            hi = mid
        else:
            lo = mid
    return lo
```

## Key Results

1. **Complete SDP hierarchy** for classically simulable state families in arbitrary finite dimension
2. **POVM simulability** characterized via SDP hierarchy
3. **Primal-dual framework**: feasibility tests + affine witnesses
4. **Tight bounds** for depolarizing noise in symmetric cases
5. **Numerically feasible** convex optimization framework

## Applications

- Quantum advantage certification
- Noise tolerance analysis
- Quantum resource theory characterization
- Quantum communication protocol verification
- Quantum vs classical benchmarking

## Activation

Use when certifying quantum advantage, analyzing classical simulability, computing noise tolerance thresholds, or building quantum resource theories. Keywords: semidefinite programming, classical simulability, quantum advantage, SDP hierarchy, POVM simulability, depolarizing noise, critical visibility, quantum witnesses.

## Pitfalls

- **SDP hierarchy depth**: Higher levels more accurate but expensive. Start with level-1.
- **Dimension scaling**: SDP size grows with Hilbert space dimension. Use symmetry reductions for n > 10.
- **Numerical precision**: Near critical boundary, use high-precision solvers (MOSEK, SDPA).
- **Commutativity relaxation**: Level-1 may over-estimate simulability.
- **Noise model**: Results assume depolarizing noise; other models may have looser bounds.
