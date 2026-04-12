---
name: data-driven-mhe-sample-complexity
description: Data-Driven Moving Horizon Estimators (DDMHE) for Linear Systems with Sample Complexity Analysis. Novel estimator combining offline and online data without known model parameters. Proves ultimate boundedness of estimation error, establishes relationship between noise covariances and error, quantifies sample complexity vs. estimation performance. Use for: (1) Model-free state estimation, (2) data-driven control design, (3) sample complexity analysis, (4) linear system estimation with unknown parameters.
---

# Data-Driven Moving Horizon Estimation with Sample Complexity

## Overview

Traditional Moving Horizon Estimation (MHE) requires known system matrices (A, B, C, D). This work proposes a **Data-Driven MHE (DDMHE)** that uses offline historical data and online observations to estimate states without knowing model parameters.

**Key Innovation**: Combines Willems' fundamental lemma with moving horizon optimization, providing theoretical guarantees on estimation error and sample complexity.

## Key Concepts

### Data-Driven Formulation

**Willems' Fundamental Lemma**:
- Offline data: `{u_off, y_off}` (input-output trajectories)
- Online data: `{u_on, y_on}` (current measurements)
- Hankel matrices: `U_p, U_f, Y_p, Y_f`

**Representation**:
```
System behavior ≈ Hankel matrix span
[u; y] ∈ span(Hankel matrices)
```

### DDMHE Optimization

**Formulation**:
```
minimize ||x_est - x_true||²
subject to:
  Output consistency: y_online matches estimated outputs
  Input history: u_online matches input trajectory
  Hankel constraint: trajectory in data span
```

**Constrained Least Squares**:
- Split into output-consistency constraint
- Input-history-matching objective
- Data-driven representation

### Estimation Error Analysis

**Ultimate Boundedness**:
```
E[||e_est||²] ≤ bound (ultimately bounded)
```

**Noise-Error Relationship**:
```
Estimation error ∝ noise covariances (Q, R)
Explicit formula linking noise to error bounds
```

### Sample Complexity

**Offline Data Length Effect**:
```
N_off → estimation error
More data → better estimation (proved relationship)
```

**Performance Gap**:
```
Gap between DDMHE (data-driven) and MHE (model-based)
Quantified analytically
Decreases with more offline data
```

## Mathematical Framework

### Data Matrices

**Hankel Structure**:
```
U_p = [u(0)...u(N-p)]  (past inputs)
U_f = [u(p)...u(N)]    (future inputs)
Y_p = [y(0)...y(N-p)]  (past outputs)
Y_f = [y(p)...y(N)]    (future outputs)
```

**Persistence of Excitation**:
```
rank(U_p, U_f) ≥ n (system order)
```

### DDMHE Algorithm

**Step 1: Construct Hankel matrices from offline data**

**Step 2: At each time step**:
- Collect online measurements `{u_on, y_on}`
- Solve constrained optimization
- Estimate state `x_est`

**Step 3: Update horizon**:
- Shift window forward
- Repeat estimation

### Theoretical Results

**Theorem 1 (Ultimate Boundedness)**:
```
||e_est|| ≤ ε_ultimate (as t → ∞)
where ε_ultimate depends on noise covariances
```

**Theorem 2 (Noise-Error Relationship)**:
```
E[||e_est||²] = f(Q, R, N_off)
Explicit function relating noise to error
```

**Theorem 3 (Sample Complexity)**:
```
||e_est|| ≤ g(N_off)
Error decreases with offline data length
```

## Applications

### 1. Model-Free Estimation

When system matrices unknown:
- Use historical trajectories
- Apply DDMHE algorithm
- Estimate states online

### 2. Data-Rich Systems

With abundant offline data:
- Train on historical data
- Deploy DDMHE online
- Achieve near-model-based performance

### 3. Sample Complexity Analysis

For data collection planning:
- Determine required data length
- Predict estimation accuracy
- Optimize data collection strategy

## Implementation Guidelines

### Data Collection

1. Collect offline input-output trajectories
2. Ensure persistence of excitation
3. Store Hankel matrices

### Horizon Selection

- Choose horizon length `N_h`
- Balance accuracy vs. computation
- Typical: `N_h ≥ 2n` (twice system order)

### Optimization Setup

1. Formulate constraints (output consistency)
2. Define objective (input matching)
3. Solve constrained least squares

### Performance Verification

1. Compare with model-based MHE
2. Measure estimation error
3. Validate theoretical bounds

## Advantages

1. **Model-Free**: No need for system matrices
2. **Provable**: Theoretical guarantees on error
3. **Practical**: Sample complexity guides data needs
4. **Flexible**: Adapts to different noise levels

## Theoretical Contributions

- Proves ultimate boundedness of DDMHE
- Establishes noise-error relationship
- Quantifies sample complexity
- Bridges data-driven and model-based estimation

## References

- Paper: "Data-Driven Moving Horizon Estimators for Linear Systems with Sample Complexity Analysis" (arxiv:2604.08328)
- Authors: Peihu Duan, Jiabao He, Yuezu Lv, Guanghui Wen
- PDF: ~/.openclaw/workspace/papers/data-driven-mhe-sample-complexity.pdf

## Related Skills

- `cognitive-flexibility-bayesian-estimation`: Bayesian state estimation
- `safe-rl-forward-invariant`: Forward invariance in learning
- `resilience-dynamics-cpsos`: Dynamic risk assessment