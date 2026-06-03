---
name: quantum-end-to-end-learning-qel
description: >-
  Quantum End-to-End Learning (QEL) methodology for contextual combinatorial optimization. First quantum computing-based end-to-end learning framework leveraging QAOA with context re-uploading phase-separator. Enables joint end-to-end training with stationarity guarantee, avoiding NP-hard optimization solvers. Use when: (1) solving contextual combinatorial optimization problems, (2) implementing quantum ML for decision-making under uncertainty, (3) combining QAOA with end-to-end learning, (4) designing quantum surrogate policies for optimization. Activation: QEL, contextual combinatorial optimization, quantum end-to-end learning, QAOA, context re-uploading, decision-focused quantum learning, quantum surrogate policy, quantum decision-making.

  Based on: "Quantum End-to-End Learning for Contextual Combinatorial Optimization" (Lee & Kwon, arXiv:2605.20222, May 2026).
---

# Quantum End-to-End Learning (QEL) for Contextual Combinatorial Optimization

**arXiv: 2605.20222** | Submitted: 13 May 2026 | Authors: Jaehwan Lee, Changhyun Kwon (KAIST)

## Overview

QEL is the **first quantum computing-based end-to-end learning framework** for **Contextual Combinatorial Optimization (CCO)**. It leverages Quantum Approximate Optimization Algorithms (QAOA) with a novel **context re-uploading phase-separator** to jointly capture relations among contexts, uncertain coefficients, and optimal solutions.

### Key Innovation

Whereas classical end-to-end learning for CCO either requires solving NP-hard optimization problems (PnO/Predict-and-Optimize) or lacks interpretability (DR/Decision Rule), QEL exploits an **optimization-aware structure grounded in physical principles** — specifically the QAOA ansatz — that classical methods cannot readily leverage.

## Core Methodology

### 1. Problem Formulation (Contextual Combinatorial Optimization)

Given context `s` (observed data) and uncertain coefficients `c`, the goal is to find a decision `x ∈ X` (combinatorial set) minimizing expected cost:

```
min E_{c|s}[f(x, c)]
```

### 2. Context Re-Uploading Phase-Separator

Inspired by **data re-uploading** in quantum ML (where classical data is encoded at multiple circuit depths), QEL proposes a **context re-uploading phase-separator**:

- The problem Hamiltonian (cost operator) receives the context `s` via a **contextual encoder** `g_φ(s)`
- The encoded context is mixed with the phase-separator operator at each QAOA layer
- This allows the same circuit to adapt its optimization behavior based on different contexts

```
U_P(γ, s) = exp(-i γ · g_φ(s) · H_P)
```

where `H_P` is the problem Hamiltonian and `g_φ(s)` encodes context-dependent coefficients.

### 3. Quantum Surrogate Policy

The quantum surrogate policy `π_θ(x|s)` is defined as:

1. Prepare initial state |+⟩^⊗ⁿ
2. Apply p layers of QAOA:
   - Context re-uploading phase-separator: `exp(-i γ_p · g_φ(s) · H_P)`
   - Mixer: `exp(-i β_p · H_M)`
3. Measure in computational basis → decision `x`

### 4. Joint End-to-End Training

- Train the contextual encoder `g_φ` and QAOA parameters `{γ, β}` jointly
- Loss function: task loss (actual cost of the decision)
- Backpropagation through the quantum circuit using **parameter-shift rules** or finite-difference gradients
- **Stationarity convergence guarantee**: QEL provides a theoretical guarantee that the joint training converges to a stationary point (unlike vanilla heuristic quantum optimization)

### 5. Solver-Free Inference

At inference time, given a new context `s`:
1. Encode `s` through `g_φ(s)` → modified Hamiltonian
2. Run QAOA with trained parameters
3. Sample measurement outcomes → near-optimal decision

No NP-hard optimization solver calls required at inference time.

## Key Advantages

| Aspect | Classical PnO | Classical DR | QEL (Ours) |
|--------|---------------|--------------|------------|
| Solver calls during training | NP-hard per iteration | None | None |
| Train on task loss | Yes (through solver) | Indirect | Direct |
| Parameter efficiency | High | Low | **Very High** |
| Interpretability | Via solver | Black-box | **Physical structure** |
| Stationarity guarantee | No | Usually | **Yes** |

## Implementation Notes

### Circuit Design

- **Qubit count**: Equal to number of decision variables (typically 4-12 for NISQ era)
- **Depth**: p = 2-4 layers sufficient for many problems
- **Encoder architecture**: Classical neural network `g_φ(s)` producing coefficient vectors

### Training Details

- Use **stochastic gradient descent** with Adam optimizer
- Gradient estimation for quantum parameters: **parameter-shift rule** (exact for gates of the form exp(-iθP) where P²=I)
- Batch-size: match the number of context samples per iteration
- Initialization: warm-start from random QAOA parameters

### Problems Demonstrated

The paper validates QEL on:
1. **Contextual knapsack**: Resource allocation with uncertain item values
2. **Portfolio optimization**: Asset allocation under uncertain returns (budget + risk constraints)
3. **Shortest path with stochastic costs**: Route planning with learned edge costs

## When to Use

- **You have**: A combinatorial optimization problem with contextual features and a quantum computer (or simulator)
- **You need**: An end-to-end trained policy that avoids calling classical solvers
- **You want**: Parameter-efficient quantum models with stationarity guarantees
- **Do NOT use**: When the problem has no combinatorial constraints, or when classical solvers are already extremely fast and available

## Related Work

- **Classical PnO**: Decision-focused learning, SPO+ (Elmachtoub & Grigas), DFL (Wang et al.)
- **Classical DR**: Learning to optimize, direct policy learning
- **QAOA**: Farhi et al. (2014), standard variational quantum optimization
- **Data re-uploading**: Pérez-Salinas et al. (2020), universal quantum classifiers

## References

- Lee & Kwon, "Quantum End-to-End Learning for Contextual Combinatorial Optimization", arXiv:2605.20222, 2026.
- Farhi, Goldstone, & Gutmann, "A Quantum Approximate Optimization Algorithm", arXiv:1411.4028, 2014.
- Elmachtoub & Grigas, "Smart 'Predict, then Optimize'", Management Science, 2022.

Keywords: quantum end-to-end learning, contextual combinatorial optimization, QAOA, quantum approximate optimization, context re-uploading, quantum surrogate policy, decision-focused quantum learning, quantum machine learning, quantum decision-making, stationarity guarantee, parameter-shift rule, NISQ optimization
