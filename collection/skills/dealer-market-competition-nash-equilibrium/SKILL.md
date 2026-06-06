---
name: dealer-market-competition-nash-equilibrium
description: "Variational approach to modeling dealer market competition with internalisation and externalisation — Nash equilibrium analysis using optimal transport."
category: economics
---

# Dealer Market Competition Nash Equilibrium

## Context

Dealers in financial markets compete through internalisation (executing orders internally) and externalisation (routing to external venues). This paper develops a variational approach to model this competition and find Nash equilibria.

## Core Methodology

1. **Formulate dealer competition as a variational inequality problem**
   - Model internalisation/externalisation as decision variables
   - Capture market impact and adverse selection costs

2. **Derive Nash equilibrium conditions**
   - Each dealer optimizes given others' strategies
   - Equilibrium characterized by first-order conditions

3. **Analyze equilibrium properties**
   - Study how internalisation rates affect market quality
   - Compare welfare under different market structures

4. **Apply optimal transport methods**
   - Use optimal transport framework for distributional analysis
   - Characterize equilibrium order flow distribution

## Implementation Steps

1. Define dealer objective functions incorporating:
   - Spread revenue
   - Internalisation benefits
   - Externalisation costs
   - Adverse selection risk

2. Set up variational inequality formulation
3. Solve for Nash equilibrium numerically
4. Analyze comparative statics

## Pitfalls

- Internalisation creates endogeneity in order flow — must model feedback effects
- Multiple equilibria possible; need selection criteria
- Real markets have more than two venues; extension to N-venue case needed

## Verification

- Check equilibrium conditions: no dealer profitable deviation
- Validate against empirical market structure data
- Compare with existing theoretical predictions

## Activation

dealer market, internalisation, externalisation, market maker, Nash equilibrium, optimal transport, variational inequality, competition, order flow
