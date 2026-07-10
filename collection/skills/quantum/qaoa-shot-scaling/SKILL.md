---
name: qaoa-shot-scaling
version: 1.0.0
description: Statistical analysis methodology for QAOA measurement shot budget allocation. Derives sufficient conditions on shot requirements for cost estimation and SGD convergence. Reveals counterintuitive scaling where total shot budget decreases with instance size for specific graph classes.
category: quantum
tags:
  - quantum
  - qaoa
  - statistics
  - optimization
  - shot-budget
  - maxcut
trigger_words:
  - qaoa shot budget
  - qaoa measurement statistics
  - quantum measurement scaling
  - qaoa shot allocation
  - quantum optimization measurement
  - shot number scaling
  - qaoa parameter optimization
  - quantum approximate optimization algorithm measurements
source_paper: "arXiv:2607.03340 - Measurements Number Scaling in QAOA for MaxCut: A Statistical Analysis (2026)"
---

# QAOA Shot Budget Scaling Analysis

## Overview

Statistical methodology for analyzing and allocating measurement shots in QAOA (Quantum Approximate Optimization Algorithm) optimization workflows. Derives rigorous bounds on shot requirements and reveals counterintuitive scaling where larger instances may require fewer total shots for specific graph classes.

## Core Methodology

### 1. Shot Budget Derivation for Cost Estimation

For QAOA cost estimation to within relative error `δ` with confidence `1-ε`:

```
n_shots ≥ Var(C) / (δ² · E[C]² · ε)
```

Where `Var(C)` is the variance of the cost Hamiltonian and `E[C]` is its expectation value.

### 2. SGD Convergence Shot Requirements

For SGD-based QAOA parameter optimization to reach target relative suboptimality `η`:

```
n_shots_per_iter ≥ O(Var(C) / (η² · ||∇E[C]||²))
```

With explicit iteration bound:

```
T ≤ O(1 / (α · η²))
```

Where `α` is the strong convexity parameter of the QAOA landscape.

### 3. Counterintuitive Scaling Law

For specific graph classes (formally characterized in the paper):

```
Total_Shot_Budget(n) ~ O(f(n)) where f(n) decreases with n
```

This means: **larger MaxCut instances on certain graph topologies require fewer total shots** to achieve the same relative performance metric.

### 4. Graph Class Characterization

The scaling phenomenon occurs when:
- The cost function concentration is strong (low variance relative to expectation)
- The QAOA landscape has favorable curvature properties
- Graph structural complexity scales favorably with size

## Practical Rules of Thumb

### Shot Allocation Strategy

1. **Small instances (n < 50)**: Start with 1000-5000 shots, monitor convergence
2. **Medium instances (50 < n < 500)**: Use 500-2000 shots, leverage concentration
3. **Large instances (n > 500)**: May reduce to 100-500 shots on favorable graphs

### Adaptive Shot Budgeting

```python
def adaptive_qaoa_shots(graph, depth_p, current_iter):
    """Dynamically allocate shots based on graph properties and optimization stage."""
    # Early iterations: fewer shots suffice for coarse gradient
    if current_iter < 10:
        return max(100, base_shots // 10)
    # Later iterations: more shots for precision
    return base_shots

# For concentration-favorable graphs (regular, dense)
# Total budget may decrease with size
```

## Key Insights

1. **Cost Concentration**: QAOA cost functions concentrate around their mean for large instances, reducing variance and thus shot requirements
2. **Parameter Redundancy**: QAOA landscapes exhibit parameter optimization redundancy, allowing fewer shots in early optimization stages
3. **Graph Structure Matters**: Not all graph classes show decreasing shot budgets; the phenomenon depends on structural properties
4. **Early vs Late Stages**: Use adaptive shot allocation — fewer shots early, more shots late

## Verification Steps

1. Compute cost variance for target graph class
2. Verify concentration bounds hold
3. Validate SGD convergence at allocated shot budget
4. Compare total budget against naive fixed-shot baseline

## Activation

This skill activates when analyzing QAOA workflows, designing quantum optimization experiments, allocating measurement budgets, or studying quantum algorithm scalability.
