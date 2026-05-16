---
name: information-theoretic-portfolio-selection
description: Portfolio selection methodology using information projection and Renyi divergence decomposition under CRRA utility. Decomposes certainty-equivalent growth rate into portfolio-induced Renyi divergence, Renyi entropy of risk-tilted market law, and log-partition term. Use when designing portfolio selection strategies, applying information theory to finance, optimizing under risk aversion, or analyzing market payoff distributions through divergence measures.
---

# Information-Theoretic Portfolio Selection

Portfolio selection under CRRA utility through information-theoretic lens.

## Core Theory

For a market with finite-support payoff vector, the CRRA certainty-equivalent growth rate decomposes as:

```
CE_growth = D_α(p_portfolio || p_market) + H_α(p_risk_tilted) + log(Z)
```

where:
- `D_α`: Portfolio-induced Renyi divergence from market law
- `H_α`: Renyi entropy of risk-tilted market distribution
- `log(Z)`: Log-partition function term
- `α`: Renyi order, operationally linked to risk aversion coefficient

## Key Insight

The Renyi order α has clear operational meaning: it equals the investor's risk aversion parameter. This bridges information geometry with portfolio theory.

## Methodology Steps

1. **Estimate Market Distribution**: From historical returns, construct empirical payoff distribution
2. **Compute Risk-Tilted Law**: p_α(x) ∝ p(x)^α (exponential tilting)
3. **Calculate Renyi Divergence**: D_α between portfolio-induced and market distributions
4. **Optimize**: Maximize CE_growth = divergence + entropy + log-partition
5. **Select Portfolio**: Choose weights that maximize information-theoretic objective

## Practical Applications

- Single-period portfolio selection
- Risk-aversion calibration via Renyi order
- Market efficiency assessment via divergence measures
- Information geometry approach to asset allocation

## Activation

portfolio selection, CRRA utility, Renyi divergence, information projection, information theory finance, risk aversion optimization, market payoff distribution
