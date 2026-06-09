---
name: dealer-market-competition-nash-equilibrium
description: "Variational approach to modeling dealer market competition with internalisation and externalisation — closed-form Nash equilibrium for multi-dealer order flow competition with inventory risk management."
category: economics
tags: [dealer-market, nash-equilibrium, inventory-risk, internalisation, externalisation, variational-methods, market-microstructure, order-flow]
---

# Dealer Market Competition with Internalisation & Externalisation

## Context

In dealer markets (e.g., FX, fixed income, OTC derivatives), multiple dealers compete for client order flow by dynamically updating bid-ask quotes. Dealers must balance profit maximization with inventory risk management through two channels: attracting offsetting flow (internalisation) or offloading in the inter-dealer market (externalisation).

Source: arXiv:2606.06413 — "Competition in Dealer Markets with Internalisation and Externalisation"

## Core Methodology

1. **Multi-Dealer Game Formulation**: Model N dealers each choosing bid-ask quotes as functions of their current inventory and market state. Each dealer maximizes expected utility of terminal wealth.

2. **Internalisation**: Dealer skews quotes to attract order flow that offsets existing inventory (e.g., wider ask when long, tighter bid when long). Reduces hedging costs but may reduce competitiveness.

3. **Externalisation**: Dealer directly offloads inventory in the inter-dealer market at prevailing prices. Immediate risk reduction but incurs transaction costs and market impact.

4. **Variational Approach**: Formulate the equilibrium as a variational problem over the space of quoting strategies. Derive first-order conditions that characterize optimal quoting behavior.

5. **Closed-Form Nash Equilibrium**: Solve the system of coupled first-order conditions analytically to obtain closed-form expressions for equilibrium quotes as functions of inventory, competition intensity, and internalisation/externalisation parameters.

## Implementation Steps

1. **Define Dealer Objective**:
   - Utility: E[W_T] - (γ/2)Var[W_T] (mean-variance)
   - Terminal wealth from: client spreads + inter-dealer P&L - inventory penalty

2. **Quote Dynamics**:
   - Bid = fair_value - spread/2 + inventory_skew
   - Ask = fair_value + spread/2 - inventory_skew
   - Skew proportional to inventory and competition intensity

3. **Inventory Dynamics**:
   - dI = client_flow(bid, ask) dt + externalisation dt
   - Client flow depends on quote competitiveness vs other dealers

4. **Variational Formulation**:
   - Hamiltonian for each dealer's optimal control problem
   - Coupled through competition in client flow
   - First-order conditions yield system of PDEs

5. **Closed-Form Solution**:
   - Assume linear-quadratic structure
   - Solve coupled Riccati equations
   - Obtain explicit quote functions

## Key Results

- Closed-form equilibrium for N-dealer competition with both internalisation and externalisation
- Optimal skewing strategy balances competitiveness vs inventory risk
- Externalisation becomes more attractive when inter-dealer market is liquid
- Competition intensity determines spread compression

## Pitfalls

- **Linear-Quadratic Assumption**: Closed-form solution requires LQ structure — real markets have nonlinear effects (e.g., convex inventory costs)
- **Nash vs Stackelberg**: Assumes simultaneous move game; real markets have leader-follower dynamics
- **Client Flow Model**: Flow depends on quote ranking among dealers — model must capture discrete choice behavior
- **Inter-Dealer Market Impact**: Externalisation costs may depend on aggregate flow, not just individual volume

## Verification

1. Verify equilibrium quotes satisfy no-arbitrage conditions
2. Check that single-dealer limit recovers Avellaneda-Stoikov solution
3. Test numerical simulation of quoting game against analytical predictions
4. Compare spread levels against empirical dealer market data

## Activation Keywords

dealer market, competition, internalisation, externalisation, Nash equilibrium, inventory risk, market microstructure, variational methods, quoting strategy, order flow, bid-ask spread
