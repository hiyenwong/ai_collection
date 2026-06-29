---
name: bregman-admm-second-order-guarantees
description: "Bregman ADMM methodology for nonconvex linearly constrained optimization under two-sided relative smoothness, providing almost-sure second-order stationarity guarantees"
---

# Bregman ADMM Second-Order Guarantees

## Description
Bregman ADMM analysis for nonconvex linearly constrained optimization under two-sided relative smoothness. This framework replaces standard Lipschitz gradient assumptions with Hessian comparison relative to a Bregman kernel, covering polynomial objectives in matrix and tensor models where global Lipschitz constants do not exist. Shows that one iteration defines a smooth primal-dual fixed-point map whose strict-saddle KKT points are unstable, yielding almost-sure convergence to second-order stationary points from random initialization.

## Activation Keywords
- Bregman ADMM nonconvex
- second-order KKT guarantees
- relative smoothness optimization
- non-Lipschitz optimization
- 布列格曼ADMM非凸优化
- strict-saddle avoidance
- distributed matrix factorization
- 二阶KKT保证
- Bregman proximal splitting
- tensor factorization optimization

## Tools Used
- coding: Implement Bregman ADMM algorithms in Python/Julia
- terminal: Run optimization experiments on matrix/tensor factorization

## Usage Patterns

### Pattern 1: Nonconvex Matrix Factorization
For matrix factorization with non-Lipschitz objectives:
1. Choose Bregman kernel matching the geometry of the constraint set
2. Apply Bregman ADMM with two-sided relative smoothness
3. Converge to second-order stationary points (not just first-order)
4. Avoid strict saddle points with probability 1

### Pattern 2: Distributed Star Consensus Optimization
For distributed optimization over star graph topology:
1. Formulate as multi-block star consensus problem
2. Apply multi-block Bregman ADMM
3. Exploit null space cancellation from star graph structure
4. Achieve second-order stationarity guarantees

### Pattern 3: Symmetric Tensor Factorization
For tensor decomposition with non-separable structure:
1. Use Bregman proximal splitting beyond separable consensus
2. Apply symmetrization and scaling steps
3. Handle polynomial objectives without Lipschitz constants

## Instructions for Agents

### Step 1: Problem Formulation
Verify the problem fits the Bregman ADMM framework:
- Nonconvex objective function
- Linear equality constraints: Ax + Bz = c
- Two-sided relative smoothness condition holds
  - ∇²f(x) ⪯ L · ∇²h(x) (upper bound)
  - ∇²f(x) ⪰ μ · ∇²h(x) (lower bound)
  - where h is the Bregman kernel

### Step 2: Bregman Kernel Selection
Choose appropriate Bregman kernel h(x):
- **Matrix factorization**: h(X) = ||X||_F² / 2 (standard quadratic)
- **Positive semidefinite constraints**: h(X) = -log det(X) (log-det barrier)
- **Simplex constraints**: h(x) = Σ x_i log x_i (negative entropy)
- **Polynomial objectives**: Custom kernel matching polynomial growth

### Step 3: Algorithm Implementation
Implement Bregman ADMM iteration:
```
x^{k+1} = argmin_x { f(x) + (ρ/2) ||Ax + Bz^k - c + u^k||² + D_h(x, x^k) }
z^{k+1} = argmin_z { g(z) + (ρ/2) ||Ax^{k+1} + Bz - c + u^k||² }
u^{k+1} = u^k + Ax^{k+1} + Bz^{k+1} - c
```
where D_h is the Bregman divergence associated with kernel h.

### Step 4: Convergence Verification
Check convergence properties:
1. **Fixed-point map**: Verify iteration defines smooth primal-dual map
2. **Strict-saddle avoidance**: Random initialization → probability 0 of converging to strict saddle
3. **Second-order stationarity**: Limiting KKT points satisfy ∇²L ⪰ 0
4. **First-order convergence**: Standard ADMM convergence rate applies

### Step 5: Multi-Block Extension
For distributed optimization:
1. Decompose problem into star graph consensus form
2. Apply block-wise Bregman ADMM updates
3. Use determinant reduction with Bregman-specific symmetrization
4. Exploit null space cancellation from star topology

## Mathematical Framework

### Two-Sided Relative Smoothness
Standard assumption: ||∇f(x) - ∇f(y)|| ≤ L ||x - y|| (Lipschitz)

Bregman assumption: L · ∇²h(x) - ∇²f(x) ⪰ 0 AND ∇²f(x) - μ · ∇²h(x) ⪰ 0

This covers polynomial objectives f(x) = x^p where no global L exists but relative smoothness holds for appropriate h.

### Bregman Divergence
D_h(x, y) = h(x) - h(y) - ⟨∇h(y), x - y⟩

Key property: D_h(x, y) ≥ 0 with equality iff x = y (when h strictly convex).

### Strict Saddle Property
A KKT point (x*, z*, u*) is a strict saddle if the Hessian of the Lagrangian has at least one negative eigenvalue in the tangent space of active constraints.

**Theorem**: Under two-sided relative smoothness, the Bregman ADMM fixed-point map has strict saddles as unstable fixed points. From random initialization, iterates converge to strict saddles with probability zero.

## Error Handling

### Relative Smoothness Violation
If two-sided relative smoothness condition is not satisfied:
- Choose different Bregman kernel
- Restrict domain to open set where condition holds
- Add regularization to satisfy lower bound

### Ill-Conditioned Bregman Kernel
If ∇²h(x) is ill-conditioned:
- Use preconditioning
- Switch to simpler kernel (quadratic)
- Apply damping: h_damped = h + ε||·||²

### Non-Convergence
If algorithm does not converge:
- Increase penalty parameter ρ
- Verify constraint qualification holds
- Check if problem has feasible solution
- Try different initialization

## Examples

### Example 1: Distributed Matrix Factorization
Given data matrix Y, factorize as Y ≈ XZ^T with distributed blocks:
```python
# Each worker holds block Y_i
# Consensus: X_i = X_global
# Bregman ADMM with log-det kernel for positive semidefiniteness
# Converges to second-order stationary point
```

### Example 2: Symmetric Tensor Factorization
Factorize symmetric tensor T ≈ Σ λ_i a_i ⊗ a_i ⊗ a_i:
```python
# Non-separable objective (cannot split into independent blocks)
# Bregman proximal splitting beyond consensus form
# Symmetrization step preserves tensor structure
```

## Resources
- arXiv: 2606.28307 - Second-Order KKT Guarantees for Bregman ADMM
- Bregman proximal algorithms literature
- ADMM convergence analysis references
