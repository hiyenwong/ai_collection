---
name: dealer-market-competition-nash-equilibrium
description: "Variational approach to modeling dealer market competition with internalisation and externalisation — analyzing Nash equilibrium in multi-dealer markets where dealers can route orders internally or to external venues."
category: quantitative-finance
---

# Dealer Market Competition with Internalisation and Externalisation

## Description
Variational approach to modeling dealer market competition where dealers can choose between internalising orders (matching against their own book) and externalising them (routing to external venues). Analyzes the Nash equilibrium of dealer strategies, showing how internalisation rates affect market quality, spreads, and dealer profitability. Provides a game-theoretic framework for understanding modern market structure with payment for order flow and internalising wholesalers.

## Activation Keywords
- dealer market competition
- order internalisation
- order externalisation
- market structure game theory
- payment for order flow
- internalising wholesaler
- Nash equilibrium market making
- 做市商竞争
- 订单内部化
- 纳什均衡市场结构

## Core Methodology

### 1. Dealer Strategy Space
- Each dealer chooses an internalisation rate ι ∈ [0, 1]: fraction of incoming flow matched internally
- Remaining flow (1 - ι) is routed to external venues (public exchanges)
- Internalisation saves on fees and adverse selection but requires sufficient flow volume
- Externalisation provides price discovery but at the cost of fees and information leakage

### 2. Variational Formulation
- Formulate each dealer's profit maximization as a variational problem
- Dealer profit function: revenue from spread - cost of inventory - adverse selection loss - routing costs
- The variational approach finds the optimal internalisation rate by solving the first-order conditions
- Key insight: the equilibrium internalisation rate depends on the dealer's flow share and the external market's liquidity

### 3. Nash Equilibrium Analysis
- A Nash equilibrium is a profile of internalisation rates where no dealer can profitably deviate
- Characterize the equilibrium: symmetric (all dealers same rate) vs asymmetric (dominant dealer internalises more)
- Study how equilibrium changes with: number of dealers, order flow distribution, external market quality

### 4. Market Quality Implications
- **Spreads**: Higher internalisation → tighter displayed spreads but wider effective spreads for non-internalised flow
- **Price Discovery**: Internalisation reduces the flow available for price discovery on public venues
- **Welfare**: Total market welfare depends on the trade-off between internalisation cost savings and reduced price discovery

## Implementation Steps

1. **Model Setup**: Specify dealer profit function with internalisation/externalisation costs
2. **First-Order Conditions**: Derive variational equations for optimal internalisation
3. **Equilibrium Computation**: Solve for Nash equilibrium using fixed-point iteration
4. **Comparative Statics**: Analyze how equilibrium changes with market parameters
5. **Welfare Analysis**: Compute total surplus under different internalisation regimes

## Pitfalls

- **Multiple Equilibria**: The dealer competition game may have multiple Nash equilibria. Use refinement criteria (stability, Pareto efficiency) to select the relevant one.
- **Flow Externalities**: One dealer's internalisation rate affects other dealers' optimal rates through flow redistribution. This externality is often the source of multiple equilibria.
- **Regulatory Constraints**: In practice, internalisation is subject to regulatory limits (e.g., SEC Rule 605/606 disclosures, MiFID II). The unconstrained equilibrium may not be implementable.
- **Empirical Calibration**: Model parameters (adverse selection cost, inventory risk) are hard to calibrate from market data. Use structural estimation or bounds analysis.

## Verification

1. Verify that the computed equilibrium satisfies the Nash condition: no profitable unilateral deviation
2. Check that internalisation rates are within [0, 1] bounds
3. Compare model predictions against empirical internalisation rates (e.g., Citadel Securities, Virtu)
4. Test sensitivity: small perturbations to parameters should not cause large equilibrium shifts (stability)

## Related Skills
- market-informedness-rl-market-making
- quantum-finance-portfolio

## Resources
- arXiv: 2606.06413
- Competition in Dealer Markets with Internalisation and Externalisation
