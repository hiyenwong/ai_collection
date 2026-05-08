---
name: pulse-level-quantum-fourier
description: "Pulse-level Quantum Fourier Models (QFMs) for quantum machine learning. Use when working with variational quantum algorithms at the pulse/composite gate level, optimizing quantum Fourier models, improving QML trainability through independent pulse scalings, or analyzing expressibility and Fourier coefficient correlation (FCC) in quantum circuits. Trigger: pulse-level quantum computing, quantum Fourier model, QFM training, composite gate optimization, QML expressibility, microwave parameter optimization."
---

# Pulse-Level Quantum Fourier Models

Variational quantum algorithms using Quantum Fourier Models (QFMs) at the pulse level instead of the gate level.

## Core Insight

At the pulse level, independent pulse scalings replace a single logical angle with multiple independently tunable sub-angles. This relaxes rigid monomial couplings induced by gate-level parameterization, providing gradient descent with higher-dimensional escape routes.

## Key Metrics

- **Expressibility**: Global expressibility is not significantly altered by pulse shape control
- **Fourier Coefficient Correlation (FCC)**: Structural correlations remain similar, but local optimization landscape fundamentally changes
- **Training Performance**: Significantly boosted by decoupling local parameter constraints

## When to Use

- Optimizing QML model trainability beyond gate-level limitations
- Working with composite gates where sub-angle independence matters
- Analyzing quantum circuit expressibility with pulse-level controls
- Implementing exponential (ternary) feature maps on quantum hardware

## Workflow

1. Define QFM with pulse-level parameterization instead of gate-level
2. Map expressibility and FCC metrics to pulse parameter space
3. Apply independent pulse scalings to composite gates
4. Train with gradient descent, leveraging higher-dimensional escape routes
5. Validate against gate-level baseline on same Fourier series task

## Implementation Notes

- Control over pulse shapes does NOT significantly alter global expressibility
- The benefit comes from the local optimization landscape, not expressibility
- For composite gates, each sub-angle becomes independently tunable
- Proven effective for training QFM with exponential feature maps

## Related

- arXiv:2605.04945 - "Beyond Gates: Pulse Level Quantum Fourier Models"
- Authors: Strobl, Franz, Scheller, Kuehn, Mauerer, Streit
