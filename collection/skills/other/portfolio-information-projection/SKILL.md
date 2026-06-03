---
name: portfolio-information-projection
description: >
  Information-theoretic framework for single-period portfolio selection under CRRA utility.
  Decomposes Certainty-Equivalent growth rate into portfolio-induced Renyi divergence,
  Renyi entropy of risk-tilted market law, and log-partition term. Connects portfolio
  optimization with information geometry and thermodynamic formalism.
  Use when: information-theoretic portfolio optimization, Renyi divergence in finance,
  CRRA utility portfolio selection, information geometry finance, Kelly criterion extensions,
  risk-tilted market laws, entropy-based portfolio optimization.
---

# Portfolio Selection via Information Projection

Information-theoretic approach to single-period portfolio optimization under CRRA utility.

## Core Decomposition

The Certainty-Equivalent (CE) growth rate under CRRA utility decomposes as:

```
CE = D_alpha(p_portfolio || q_market) + H_alpha(q_risk_tilted) + log(Z)
```

Where:
- **D_alpha**: Portfolio-induced Renyi divergence (measures deviation from market)
- **H_alpha**: Renyi entropy of risk-tilted market law (uncertainty in tilted measure)
- **log(Z)**: Log-partition function (normalization term)
- **alpha**: CRRA risk aversion parameter

## Key Insight

Portfolio optimization under CRRA utility can be reframed as an information projection problem:
- Finding the portfolio that minimizes divergence from an optimal risk-tilted measure
- The optimal portfolio is the information projection of the market law onto the feasible set

## Mathematical Framework

### CRRA Utility

```
U(W) = W^(1-gamma) / (1-gamma)  for gamma != 1
U(W) = log(W)                   for gamma = 1 (log utility)
```

### Renyi Divergence

```
D_alpha(p || q) = (1/(alpha-1)) * log(sum p_i^alpha * q_i^(1-alpha))
```

### Risk-Tilted Market Law

The market payoff distribution tilted by the investor's risk preferences:

```
q_risk_tilted(x) proportional to x^(-gamma) * p_market(x)
```

## Optimization Approach

1. **Characterize market payoff**: Assume finite support {x_1, ..., x_n} with probabilities p
2. **Compute risk-tilted measure**: q_risk_tilted proportional to x^(-gamma) * p
3. **Information projection**: Find portfolio w* that minimizes D_alpha(w || q_risk_tilted)
4. **Decompose CE**: Extract divergence, entropy, and partition contributions

## Connection to Kelly Criterion

For gamma = 1 (log utility):
- CE growth rate = expected log return - KL divergence
- Optimal portfolio = Kelly optimal
- Information projection reduces to minimizing KL divergence

## Practical Application

```python
def information_projection_portfolio(payoffs, probabilities, gamma):
    """
    Compute optimal portfolio via information projection.
    
    Args:
        payoffs: Market payoff vector (finite support)
        probabilities: Market probabilities for each payoff
        gamma: CRRA risk aversion parameter
    
    Returns:
        Optimal portfolio weights
    """
    # Compute risk-tilted measure
    tilted = payoffs**(-gamma) * probabilities
    tilted = tilted / tilted.sum()
    
    # Information projection (minimize Renyi divergence)
    # This yields the optimal portfolio weights
    alpha = 1 - gamma  # Renyi parameter from CRRA
    optimal = tilted  # Projection result
    
    return optimal
```

## When to Use

- Information-theoretic portfolio optimization
- Understanding risk preferences through information geometry
- Connecting portfolio theory with thermodynamic formalism
- Extensions of Kelly criterion to general CRRA utility
- Decomposing portfolio performance into information-theoretic components

## References

- arXiv: 2605.03184 - Single-Period Portfolio Selection via Information Projection
- Yang & Gastpar, 2026
