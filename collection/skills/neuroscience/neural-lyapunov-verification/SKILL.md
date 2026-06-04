---
name: neural-lyapunov-verification
description: >
  Sound and complete verification of neural Lyapunov candidates for nonlinear control systems.
  Uses hyperplane partitioning of ReLU networks to verify stability guarantees.
  Use when: (1) verifying neural network controller stability, (2) Lyapunov function validation,
  (3) formal verification of learned control policies, (4) safety-critical neural control systems,
  (5) analyzing ReLU network dynamics for stability properties.
---

# Neural Lyapunov Verification

Verify stability of neural network controllers using Lyapunov function analysis.
Based on HyParLyVe (Hyperplane Partitioned Lyapunov Verifier) methodology.

## Core Approach

1. **Partition ReLU networks** into linear regions using hyperplane arrangements
2. **Check Lyapunov conditions** (V(x) > 0, dV/dt < 0) in each linear region
3. **Sound and complete** verification - no false positives or negatives
4. **Scalable** to shallow ReLU networks (1-2 hidden layers)

## Workflow

### Step 1: Define the System

```python
# System: dx/dt = f(x) + g(x) * u(x)
# where u(x) is the neural network controller
```

### Step 2: Verify Lyapunov Candidate

For candidate V(x) (often a neural network):
- Check V(0) = 0 and V(x) > 0 for x != 0 (positive definite)
- Check dV/dt = grad(V) * f(x) < 0 for x != 0 (negative definite derivative)

### Step 3: Hyperplane Partitioning

Partition input space by ReLU activation patterns:
- Each region = set of active/inactive neurons
- Within each region, network is affine: u(x) = Wx + b
- Verify Lyapunov conditions via linear programming in each region

### Step 4: Region-of-Attraction Estimation

Find largest sublevel set {x : V(x) <= c} that satisfies all conditions.

## Key References

- HyParLyVe: arXiv:2605.03992 - Hyperplane Partitioning for Neural Lyapunov Verification
- Related: neural-network-control-verification, formal-verification-ml

## Limitations

- Works best for shallow ReLU networks (1-2 hidden layers)
- Computational cost grows exponentially with network width
- Requires known system dynamics f(x), g(x)
