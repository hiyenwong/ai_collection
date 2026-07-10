---
name: description-length-genetic-programming
description: "Description Length (DL) and Fractional Bayes Factor (FBF) model selection methodology for genetic programming and symbolic regression. Evaluates DL/FBF as principled alternatives to AIC/BIC for selecting compact, generalizable expressions. Use when working with symbolic regression, genetic programming model selection, Fisher-information-based complexity penalties, or preventing structural bloat in evolved expressions."
arxiv_id: "2605.22374"
published: "2026-05-21"
authors: "Gabriel Kronberger, Fabricio Olivetti de Franca, Deaglan J. Bartlett, Harry Desmond, Pedro G. Ferreira"
tags: [symbolic-regression, genetic-programming, model-selection, description-length, bayesian]
---

# Description Length Genetic Programming

## Core Methodology

This paper evaluates **Description Length (DL)** and **Fractional Bayes Factor (FBF)** as principled, data-efficient alternatives to AIC/BIC for model selection in Genetic Programming Symbolic Regression (GPSR).

### Problem

GPSR suffers from overfitting and structural bloat, especially with noisy data. Heuristic selection of compact expressions often fails.

### Key Innovation

DL using **Fisher-information-based parameter encoding** provides a more accurate complexity penalty than AIC/BIC, leading to better test performance on both synthetic and real-world regression problems.

### Three Search/Selection Strategies

| Strategy | Approach | Result |
|----------|----------|--------|
| **(i) Post-selection** | Multi-objective search (accuracy + program length), then DL/FBF selection | **Best** — improves test performance over AIC/BIC |
| **(ii) DL as objective** | Multi-objective search with DL directly as objective | Comparable to post-selection |
| **(iii) DL as fitness** | Single-objective optimization with DL/FBF as fitness | **Avoid** — premature convergence to overly simple models |

### Key Findings

1. **DL/FBF post-selection** outperforms AIC/BIC on test datasets
2. **BIC + same complexity penalty** from DL/FBF produces similar results
3. **Single-objective DL/FBF fitness** frequently causes premature convergence — use multi-objective instead
4. **Fisher-information-based encoding** captures parameter uncertainty better than naive length counting

## Agent Instructions

### When to Apply

- User asks about symbolic regression model selection
- Need to prevent bloat in genetic programming
- Choosing between AIC, BIC, and more principled criteria
- Working with noisy regression data where overfitting is a concern

### Implementation Pattern

```python
import numpy as np

def description_length(model, data, params):
    """Calculate description length using Fisher information.
    
    DL = L(data|params) + 0.5 * log(det(Fisher)) + complexity_terms
    """
    n = len(data)
    residuals = data - model(params)
    # Log-likelihood term
    ll = -0.5 * n * np.log(2 * np.pi) - 0.5 * np.sum(residuals**2)
    # Fisher information (numerical approximation)
    eps = 1e-6
    fisher = np.zeros((len(params), len(params)))
    for i in range(len(params)):
        for j in range(len(params)):
            pp = params.copy()
            pm = params.copy()
            pp[i] += eps; pp[j] += eps
            pm[i] -= eps; pm[j] -= eps
            fisher[i,j] = (ll_at(pp) - 2*ll + ll_at(pm)) / (4*eps**2)
    # DL = -2*LL + log(det(F)) + param_encoding
    det_f = np.abs(np.linalg.det(fisher))
    dl = -2 * ll + np.log(det_f + 1e-10) + len(params) * np.log(n)
    return dl

def fractional_bayes_factor(model1, model2, data, b=0.1):
    """Fractional Bayes Factor for model comparison.
    Uses fraction b of data as training, rest for Bayes factor.
    """
    # Partial likelihood for training fraction
    n_train = max(1, int(b * len(data)))
    # ... compute marginal likelihoods ...
    pass
```

### Practical Guidance

1. **Use multi-objective GPSR** with accuracy + length as objectives
2. **Apply DL/FBF as post-selection criterion** on the Pareto front
3. **Avoid using DL/FBF as direct fitness** in single-objective optimization
4. **Fisher-information encoding** is more accurate than simple parameter counting
5. **BIC + DL complexity penalty** is a good approximation when full DL computation is expensive

## Error Handling

### Premature Convergence
If GP converges to overly simple models:
- Check if DL/FBF is being used as direct fitness → switch to post-selection
- Reduce the complexity penalty weight
- Increase population size and generations

### Fisher Information Computation
If Fisher matrix is singular or ill-conditioned:
- Add small regularization: `fisher += eps * np.eye(n_params)`
- Use numerical differentiation with appropriate step size (1e-6 to 1e-4)
- Consider analytical Fisher if available

## Activation Keywords

- description length genetic programming
- DL model selection symbolic regression
- fractional bayes factor GPSR
- fisher information complexity penalty
- genetic programming overfitting prevention
- symbolic regression model selection
- 描述长度遗传编程
- 符号回归模型选择
