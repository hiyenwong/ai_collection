---
name: distributionally-robust-control
description: "Design and analyze distributionally robust control systems under uncertainty with incomplete distribution information. Covers Sinkhorn ambiguity sets, convexity analysis, weak compactness, tractability guarantees, and MPC approaches. Use when designing controllers for systems with uncertain probability distributions, implementing robust MPC, or analyzing worst-case performance under distributional ambiguity."
---

# Distributionally Robust Control

Design controllers that remain effective when uncertainty distributions are incompletely known, using ambiguity sets to bound worst-case scenarios.

## Activation Keywords
- distributionally robust control
- ambiguity set
- Sinkhorn distance
- robust MPC
- distributional uncertainty
- worst-case optimization
- Wasserstein ambiguity

## Core Concepts

### Ambiguity Sets
- **Sinkhorn ambiguity sets**: Defined via entropic optimal transport distance
  - Convexity: Set of distributions within Sinkhorn distance of nominal
  - Weak compactness: Guarantees existence of worst-case distribution
  - Tractability: Dual formulation yields computable optimization

### Key Properties
1. **Convexity**: Ambiguity set is convex → tractable worst-case optimization
2. **Weak compactness**: Existence of worst-case distribution in set
3. **Tractability**: Dual problem reformulation enables efficient computation

## Design Workflow

### Step 1: Characterize Uncertainty
Define the nominal distribution and uncertainty structure:
- Historical data for nominal estimate
- Sources of distributional shift
- Available side constraints (support, moments)

### Step 2: Construct Ambiguity Set
Choose ambiguity set based on available information:
- **Wasserstein ball**: When only support information available
- **Sinkhorn ball**: When computational efficiency needed (entropic regularization)
- **Moment-based**: When moment bounds are known

### Step 3: Formulate Robust Problem
```
min_u max_{P ∈ A} E_P[cost(u, ξ)]
```
Where A is the ambiguity set, u is control, ξ is uncertainty.

### Step 4: Derive Tractable Reformulation
- Use duality theory to convert inner maximization
- For Sinkhorn: dual involves entropic regularization term
- Verify convexity of resulting problem

### Step 5: Implement Controller
- Solve tractable reformulation at each time step (MPC)
- Verify constraint satisfaction under worst-case distribution
- Analyze suboptimality gap vs. true optimal

## Common Patterns

### Pattern: MPC with Distributional Robustness
1. At each time step, construct ambiguity set from data
2. Solve distributionally robust MPC problem
3. Apply first control input
4. Update ambiguity set with new observations

### Pattern: Aging-Aware Energy Management
For EV charging with PV:
- Model battery degradation as state-dependent cost
- Use distributionally robust optimization for demand uncertainty
- Balance economic performance with battery longevity

## Analysis Checklist
- [ ] Ambiguity set is convex (for tractability)
- [ ] Worst-case distribution exists (for validity)
- [ ] Dual reformulation is computable (for implementation)
- [ ] Constraint satisfaction verified (for safety)
- [ ] Suboptimality bounded (for performance)

## References
- Sinkhorn Ambiguity Sets for Distributionally Robust Control (arxiv 2605.03845)
- Online Energy Management for Bidirectional EV Charging with MPC (arxiv 2605.03844)
- HyParLyVe: Neural Lyapunov Verification (arxiv 2605.03992)
