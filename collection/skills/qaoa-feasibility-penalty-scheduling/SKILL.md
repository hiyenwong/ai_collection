---
name: qaoa-feasibility-penalty-scheduling
description: "Feasibility-driven QAOA with penalty scheduling. Introduces Λ-lr-QAOA (per-penalty linear-ramp schedules) and piecewise-ramp QAOA (two-segment piecewise schedules) for constrained optimization. Promotes penalty weights from external hyperparameters to internal variational parameters. Activation: feasibility-driven QAOA, penalty scheduling, constrained QAOA, Λ-lr-QAOA, piecewise-ramp QAOA, MWIS optimization"
metadata:
  arxiv_id: "2606.25117"
  published: "2026-06-23"
  authors: "Francesco Ferrari, Matteo Vandelli, Daniele Dragoni"
  tags: [quantum, optimization, QAOA, constraints, penalty-method, scheduling]
---

# QAOA with Feasibility Penalty Scheduling

## Description
Extends standard linear-ramp QAOA (lr-QAOA) for problems with multiple heterogeneous constraints. Introduces Λ-lr-QAOA (per-penalty linear-ramp) and piecewise-ramp QAOA (two-segment schedules) that promote penalty weights from external hyperparameters to internal variational parameters.

## Activation Keywords
- feasibility-driven QAOA
- penalty scheduling
- constrained QAOA
- Λ-lr-QAOA
- piecewise-ramp QAOA
- MWIS quantum optimization
- 可行性驱动QAOA
- 惩罚调度量子优化

## Core Concepts

### Λ-lr-QAOA (Lambda Linear-Ramp QAOA)
- Each penalty term gets its own linear-ramp schedule
- Penalty weights become internal variational parameters (not external hyperparameters)
- Joint optimization of all schedules eliminates nested penalty tuning
- Scales efficiently to multiple constraints

### Piecewise-Ramp QAOA
- Linear ramps replaced by two-segment piecewise schedules
- Enhances Ansatz expressiveness at cost of small parameter overhead (independent of circuit depth)
- Consistently outperforms lr-QAOA and Λ-lr-QAOA across depths and system sizes

### Feasibility-Driven Loss Function
- Pushes quantum state towards high-quality feasible solutions
- Filtered variant provides single hyperparameter to tune feasibility-optimality trade-off

## Methodology

### Step 1: Formulate Constrained Problem
Express as QUBO with multiple heterogeneous constraints: H = H_obj + Σ λ_i H_constraint_i

### Step 2: Construct Λ-lr-QAOA Ansatz
- For each constraint i: define linear ramp schedule γ_i(t) = α_i · t
- Promote α_i to variational parameter alongside γ, β

### Step 3: Piecewise-Ramp Enhancement (Optional)
- Replace linear ramps with two-segment piecewise: γ_i(t) = {α_i1·t for t < t*; α_i2·t + β_i for t ≥ t*}

### Step 4: Joint Optimization
- Optimize all parameters simultaneously: {γ, β, α_1, ..., α_k}
- Use feasibility-driven loss: L = -<H_obj> + λ_violation · (constraint violation penalty)

### Step 5: Filtered Loss for Feasibility-Optimality Balance
- Apply filtered variant to tune balance with single hyperparameter
- Higher filter → prioritize feasibility; Lower filter → prioritize optimality

## Usage Patterns

### Pattern 1: Constrained Portfolio Optimization
Apply to portfolio problems with budget, risk, and sector constraints.

### Pattern 2: Satellite Mission Planning
Benchmarked on Earth-observation satellite mission planning (budget-constrained MWIS).

### Pattern 3: General Constrained QUBO
Use for any QUBO with multiple heterogeneous constraints where penalty tuning is challenging.

## Pitfalls

### Parameter Scaling
Piecewise-ramp adds ~2× parameters vs. linear-ramp, but overhead is independent of circuit depth → acceptable trade-off for most applications.

### Feasibility-Optimality Trade-off
Inherent trade-off between solution feasibility and quality. No free lunch — must tune via filtered loss hyperparameter.

### High Feasibility Rate
Both Λ-lr-QAOA and piecewise-ramp exhibit high feasibility rates — crucial for industrial applications but may sacrifice some solution quality.

### Circuit Depth Requirements
Performance improvements are most pronounced at moderate-to-high circuit depths. At very low depths (p=1), benefits are limited.

## References
- arXiv: 2606.25117 - "Feasibility-driven QAOA with penalty scheduling"
- Related: `qaoa-manifold-optimization` (Riemannian manifold optimization for QAOA)
- Related: `distributed-qaoa-simulator` (distributed QAOA execution)
