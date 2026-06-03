---
name: pulse-level-qfm
description: Pulse-level Quantum Fourier Models (QFMs) for quantum machine learning. Optimizes variational quantum algorithms by using pulse parameters instead of gate-level angles, providing higher-dimensional escape routes in the optimization landscape. Use when: designing pulse-level quantum circuits, optimizing QFM training, improving variational quantum algorithm convergence, working with quantum machine learning expressibility and Fourier coefficient correlation, or replacing gate-level parameterization with pulse-level control. Trigger: pulse-level QFM, quantum Fourier model, pulse variational quantum, QFM training optimization, quantum pulse parameterization, arXiv 2605.04945.
---

# Pulse-Level Quantum Fourier Models

Optimize variational quantum algorithms (VQAs) by operating at the pulse level rather than the gate level, unlocking higher-dimensional optimization landscapes for quantum machine learning.

## Core Insight

Gate-level parameterization creates **rigid monomial couplings** — a single logical angle controls the entire gate. Pulse-level parameterization replaces each gate angle with **multiple independently tunable sub-angles**, decoupling local parameter constraints and providing gradient descent with higher-dimensional escape routes.

## Key Findings (arXiv:2605.04945v1)

1. **Expressibility is unchanged**: Control over pulse shapes does NOT significantly alter global expressibility or structural correlations (FCC) of the Ansatz.
2. **Optimization landscape is fundamentally altered**: The local landscape changes dramatically, even if the global properties don't.
3. **Composite gates benefit most**: Independent pulse scalings replace single logical angles → multiple independently tunable sub-angles.
4. **Training performance boosted**: Gradient descent gains higher-dimensional escape routes, significantly improving convergence.

## When to Use

- VQA training is stuck in local minima
- Gate-level QFM performance is plateauing
- Need to improve quantum model trainability without changing Ansatz expressibility
- Working with hardware-native pulse control (microwave parameters)

## Implementation Pattern

### Step 1: Replace gate-level angles with pulse scalings

For a composite gate with angle θ, instead of:
```
U(θ) = exp(-i θ H / 2)
```

Use independent pulse scalings:
```
U_pulse = exp(-i θ₁ s₁ H / 2) · exp(-i θ₂ s₂ H / 2) · ...
```
where sᵢ are independently tunable scale factors.

### Step 2: Optimize at pulse level

Train the expanded parameter set {θᵢ, sᵢ} instead of {θ}. This provides:
- More degrees of freedom per gate
- Decoupled parameter constraints
- Higher-dimensional escape routes from local minima

### Step 3: Validate expressibility

Check that global expressibility and Fourier coefficient correlation (FCC) remain consistent with the original gate-level model — they should be nearly unchanged.

## Metrics to Track

| Metric | Gate-Level | Pulse-Level | Expected Change |
|--------|-----------|-------------|-----------------|
| Expressibility | Measured | Measured | ~Unchanged |
| Fourier Coefficient Correlation | Measured | Measured | ~Unchanged |
| Local optimization landscape | Constrained | Relaxed | Significantly improved |
| Training convergence | Baseline | Enhanced | Significantly boosted |

## Activation Keywords

- pulse-level QFM
- quantum Fourier model pulse
- pulse variational quantum
- QFM training optimization
- quantum pulse parameterization
- beyond gates quantum

## References

- arXiv:2605.04945v1 — "Beyond Gates: Pulse Level Quantum Fourier Models" by Strobl et al., 2026
- Categories: quant-ph
