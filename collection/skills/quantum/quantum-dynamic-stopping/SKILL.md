---
name: quantum-dynamic-stopping
category: quantum
description: Dynamic stopping criteria for quantum linear systems algorithms (QLSA) using residue monitoring and Chebyshev amplification. Addresses the open problem of when to stop QLSA without knowing ||A^{-1}b||, using only oracle access to the residue vector ||b - Ax||. Enables provable precision guarantees with near-optimal query complexity.
---

# Quantum Dynamic Stopping for QLSA

## Overview

Quantum Linear Systems Algorithms (QLSA) like HHL solve $A\vec{x}=\vec{b}$ exponentially faster than classical methods under certain conditions. However, a fundamental open problem is: **when to stop the algorithm** when you only have oracle access, not the explicit solution vector?

This skill provides dynamic stopping criteria using residue monitoring $\|\vec{b} - A\vec{x}\|$, with provable precision guarantees and near-optimal query complexity.

## When to Use

- Running QLSA/HHL and need stopping criteria without knowing $\|A^{-1}\vec{b}\|$
- Only oracle access to $\vec{b}$ and $A$, not explicit vector representations
- Need provable precision guarantees (relative error $\epsilon$)
- Working with condition number $\kappa = \|A\|\|A^{-1}\|$ bounded systems
- Resource estimation for quantum linear solver implementations

## Key Concepts

### The Stopping Problem

Classically: easy — compute residual $\|\vec{b} - A\vec{x}_t\|$ directly.
Quantumly: hard — $\vec{x}$ is encoded in quantum state $|x\rangle$, no direct access.

**Solution**: Construct quantum state $|r\rangle \propto \vec{b} - A\vec{x}$ (residue state) and measure its norm.

### Core Algorithm

```
Input: Oracles for A and b, target relative error ε
Output: State |x⟩ such that ||x - A^{-1}b|| / ||A^{-1}b|| ≤ ε

1. Initialize: |x⟩ ← |b⟩ (or random state)
2. Loop:
   a. Construct residue state: |r⟩ ∝ b - Ax  (Chebyshev amplification)
   b. Estimate residue norm: r = ||b - Ax||  (Amplitude Estimation)
   c. If r ≤ ε·||b||/κ: STOP (converged)
   d. Otherwise: update |x⟩ using QLSA step
3. Return |x⟩
```

### Query Complexity

- **With known $\|A^{-1}\vec{b}\|$**: $\mathcal{O}(\kappa \log(1/\epsilon))$ queries
- **Without knowing $\|A^{-1}\vec{b}\|$** (this method): $\mathcal{O}(\kappa \log(\kappa/\epsilon))$ queries
- **Overhead**: only $\mathcal{O}(\log \kappa)$ factor — near-optimal

### Chebyshev Amplification

The residue $\vec{b} - A\vec{x}_t$ is amplified using Chebyshev polynomials:

$$T_k(A) = \cos(k \arccos A)$$

This amplifies small eigenvalue components, making the residue measurable even when $\kappa$ is large.

### Amplitude Estimation for Residue Norm

Use quantum amplitude estimation to measure $\|\vec{b} - A\vec{x}\|$:

1. Prepare state: $|0\rangle|0\rangle \to \alpha|1\rangle|r\rangle + \beta|0\rangle|\perp\rangle$
2. $\alpha^2 = \|\vec{b} - A\vec{x}\|^2 / (\text{normalization})$
3. Estimate $\alpha$ with $\mathcal{O}(1/\delta)$ queries for $\delta$ precision

## Implementation Steps

### Step 1: Residue State Preparation

Given access to oracles $O_A$ (block encoding of $A$) and $O_b$ (state preparation for $b$):

1. Apply QLSA to get $|x_t\rangle$
2. Apply $O_A$ to get $A|x_t\rangle$
3. Use linear combination of unitaries (LCU) to prepare $|r\rangle \propto |b\rangle - A|x_t\rangle$

### Step 2: Norm Estimation

```python
# Pseudocode for residue norm estimation
def estimate_residue_norm(oracle_A, oracle_b, state_x, precision=0.01):
    """
    Estimate ||b - Ax|| using amplitude estimation.
    Returns (norm_estimate, confidence_interval)
    """
    # 1. Prepare residue state
    residue_state = prepare_residue(oracle_A, oracle_b, state_x)
    
    # 2. Amplitude estimation
    norm_sq = amplitude_estimate(residue_state, precision)
    
    return sqrt(norm_sq), precision
```

### Step 3: Stopping Criterion

```python
def should_stop(residue_norm, b_norm, kappa, epsilon):
    """
    Check if relative error criterion is satisfied.
    ||x - A^{-1}b|| / ||A^{-1}b|| ≤ ε
    """
    # Sufficient condition: ||b - Ax|| ≤ ε·||b||/κ
    threshold = epsilon * b_norm / kappa
    return residue_norm <= threshold
```

### Step 4: Adaptive Iteration

```python
def qlsa_with_dynamic_stopping(oracle_A, oracle_b, epsilon, kappa_max):
    """QLSA with provable stopping criterion."""
    kappa = kappa_max  # conservative initial estimate
    x_state = prepare_initial_state(oracle_b)
    
    for iteration in range(max_iterations):
        # Chebyshev-amplified QLSA step
        x_state = chebyshev_qlsa_step(oracle_A, x_state, degree=kappa)
        
        # Estimate residue
        r_norm, _ = estimate_residue_norm(oracle_A, oracle_b, x_state)
        
        if r_norm <= epsilon * oracle_b.norm() / kappa:
            return x_state  # converged
        
        # Optionally refine kappa estimate
        kappa = refine_condition_estimate(oracle_A, x_state, r_norm)
    
    raise ConvergenceError("QLSA did not converge within max iterations")
```

## Pitfalls

- **Condition number dependence**: Query complexity scales as $\mathcal{O}(\kappa)$, so ill-conditioned systems require many more queries
- **Block encoding overhead**: Requires efficient block encoding of $A$ — not all matrices admit sparse/efficient encodings
- **Amplitude estimation cost**: Each norm estimation costs $\mathcal{O}(1/\delta)$ queries; balance precision vs. overhead
- **Lower bound**: $\Omega(\kappa/\epsilon)$ queries is information-theoretic lower bound — cannot do better
- **Phase estimation alternative**: Using quantum phase estimation instead of Chebyshev gives $\mathcal{O}(\kappa^2/\epsilon)$ — worse scaling

## Verification

- Residue norm should monotonically decrease (in exact arithmetic)
- Final relative error bound: $\|\vec{x} - A^{-1}\vec{b}\| / \|A^{-1}\vec{b}\| \leq \epsilon$
- Query count should be $\mathcal{O}(\kappa \log(\kappa/\epsilon))$

## References

- Paper ID 621 in kg.db (QLSA dynamic stopping with Chebyshev amplification)
- HHL algorithm (Harrow, Hassidim, Lloyd 2009)
- Quantum amplitude estimation (Brassard et al. 2002)
- Chebyshev iteration for quantum linear solvers
