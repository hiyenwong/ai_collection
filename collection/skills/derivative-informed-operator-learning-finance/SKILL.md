---
name: derivative-informed-operator-learning-finance
description: "Derivative-informed operator learning framework for financial decision systems. Neural operators trained to match both pricing operators and Fréchet derivatives. Reduces hedging error, vega error by 40%, delta error by 15%. Use when: financial surrogate models, derivative pricing, Greeks computation, hedging, operator learning, neural operators, DeepONet, random features, no-arbitrage constraints, volatility surfaces, risk sensitivities."
metadata:
  arxiv_id: "2606.05900"
  published: "2026-06-04"
  authors: "Miquel Noguer I Alonso"
  tags: [finance, operator-learning, derivatives, hedging, neural-operators, DeepONet]
---

## Context

Financial decision systems (pricing, calibration, hedging, XVA, stress testing, portfolio optimization) need fast surrogate models. Standard neural surrogates reproduce prices but downstream tasks depend critically on derivatives: deltas, vegas, curve/credit-spread sensitivities, exposure gradients.

## Core Methodology

1. **Derivative-Informed Training**: Train neural operators to match both a high-fidelity pricing/risk operator AND directional Fréchet derivatives generated on-the-fly
2. **Combined Techniques**: Operator learning + adjoint algorithmic differentiation + tangent sensitivity equations + random Jacobian sketching + no-arbitrage constraints
3. **Error Bounds**: Derivative accuracy controls local stress errors, hedging error, and optimizer instability; discrete-time hedging error governed by second-order (gamma) accuracy

## Key Results

- Black-Scholes network (8 seeds): derivative weight cuts vega error by 40%, delta error by 15%
- Heston/Bates random-feature experiments: reduce stochastic-volatility and jump-parameter sensitivity errors by 60-76%
- Random-feature DeepONet/Galerkin operator: mapping instantaneous-volatility curves to dense price surfaces reduces out-of-sample JVP error by 44% and price RMSE by 23%
- Derivative consistency alone does NOT remove no-arbitrage violations — economic constraints must be imposed explicitly

## Implementation Steps

1. Define pricing/risk operator mapping inputs (model parameters, market states) to outputs (prices, risk quantities)
2. Generate on-the-fly Fréchet derivatives via adjoint AD or tangent sensitivity equations
3. Train operator (neural operator, random-feature operator, or finite-dimensional surrogate) with dual loss: value matching + derivative matching
4. Apply random sketching of Jacobian actions for efficiency
5. Impose no-arbitrage constraints explicitly (derivative awareness ≠ economic consistency)
6. Validate: check delta, gamma, vega accuracy separately from price accuracy

## Pitfalls

- **Derivative consistency ≠ no-arbitrage**: Even with perfect derivative matching, economic constraints must be imposed explicitly to prevent arbitrage violations
- **Second-order Greeks harder**: Unsupervised second-order Greeks (gamma) show less improvement from derivative weighting than first-order (delta, vega)
- **Random-feature efficiency**: Random-feature operators (DeepONet/Galerkin) offer best speed-accuracy tradeoff for vol surface mapping

## Verification

- Verify vega error reduction ≥ 40% vs value-only surrogate
- Verify delta error reduction ≥ 15%
- Check no-arbitrage violations are constrained (not just derivative-consistent)
- Validate out-of-sample JVP error reduction ≥ 40% for vol surface mapping

## Activation Keywords

derivative-informed, operator learning, financial surrogate, Greeks computation, hedging, vega, delta, gamma, DeepONet, random features, Fréchet derivative, no-arbitrage, volatility surface, stochastic volatility, Heston model, Bates model, financial decision systems, pricing operator
