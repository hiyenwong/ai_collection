---
name: quantum-portfolio-optimization
description: >
  Methodology for quantum-enhanced portfolio optimization using QAOA,
  quantum-inspired algorithms (LogQ), and hybrid quantum-classical approaches.
  Covers noise characterization, QUBO formulation, and convergence analysis.
  Use when working with quantum finance, portfolio optimization, QAOA applications,
  quantum-inspired optimization, or hybrid quantum-classical financial modeling.
  Trigger: quantum portfolio, QAOA portfolio, quantum finance, quantum optimization,
  LogQ algorithm, hybrid quantum genetic, QUBO finance, portfolio optimization quantum
---

# Quantum Portfolio Optimization

## Description

Comprehensive methodology for applying quantum and quantum-inspired algorithms
to portfolio optimization problems. Covers QAOA with noise characterization,
LogQ quantum-inspired classical algorithms, and hybrid quantum-classical genetic
algorithms for financial optimization tasks.

## Activation Keywords

- quantum portfolio optimization
- QAOA portfolio
- quantum finance
- quantum-inspired optimization
- LogQ algorithm
- hybrid quantum genetic algorithm
- QUBO finance
- quantum optimization finance
- 量子投资组合
- quantum portfolio

## Core Methods

### 1. QAOA for Portfolio Optimization (arXiv:2604.19426)

Use Quantum Approximate Optimization Algorithm (QAOA) with noise characterization:

- **Landscape Span Compression (LSC)**: Device-agnostic metric quantifying noise
  distortion in variational energy landscapes
- Key finding: Hardware noise compresses landscape by 24-30% without displacing
  the global minimum, supporting classical-to-hardware parameter transfer
- Feasibility fractions at optimal parameters remain 1.5-1.7x above random
- Consistent noise cost: ~0.03 approximation-ratio units across instances
- Zero-Noise Extrapolation: Mixed results (+7%/+9%/-4%), requires 3-5x more shots

### 2. LogQ Algorithm - Quantum-Inspired Classical (arXiv:2604.12925)

Reformulates quantum QUBO solving as classical non-linear continuous relaxation:

- Encodes QUBO problems with fewer resources than quantum circuits
- Eliminates Pauli decomposition and measurement overhead
- Uses gradient-inspired parameter optimization
- Applicable to portfolio optimization, fleet optimization, charging stations

### 3. Hybrid Quantum Genetic Algorithm (arXiv:2604.11667)

Combines quantum computing with evolutionary algorithms:

- HQGA converges faster than classical GA for portfolio optimization
- Maintains higher population diversity throughout optimization
- Requires fewer evaluations-to-solution than brute-force
- Use when quantum hardware access is available for hybrid computation

## QUBO Formulation for Portfolio Optimization

```python
import numpy as np
from scipy.optimize import minimize

def portfolio_to_qubo(returns, cov_matrix, budget, risk_aversion=0.5):
    """Convert portfolio optimization to QUBO form.

    Minimize: -w^T * returns + risk_aversion * w^T * cov * w
    Subject to: sum(w) = budget, w_i in {0,1}
    """
    n = len(returns)
    Q = risk_aversion * cov_matrix
    for i in range(n):
        Q[i, i] -= returns[i]  # Linear term into diagonal

    # Add budget constraint as penalty
    penalty = 10.0
    Q += penalty * np.ones((n, n))
    return Q
```

## Noise Characterization Workflow

1. Run classical simulation to find optimal parameters
2. Execute on quantum hardware with LSC metric tracking
3. Compare calibration model fidelity (target r > 0.95)
4. Apply error mitigation (ZNE, readout correction)
5. Measure approximation ratio degradation

## Convergence Analysis

Compare hybrid vs classical approaches:
- Track evaluations-to-solution metric
- Monitor population diversity over generations
- Record convergence speed (iterations to optimum)
- Document solution quality vs compute cost tradeoff

## Key Findings from Recent Research

| Metric | QAOA (Hardware) | LogQ (Classical) | HQGA (Hybrid) |
|--------|----------------|------------------|---------------|
| Noise resilience | ~0.03 AR cost | N/A (classical) | Partial |
| Convergence speed | Baseline | Fast | Faster than GA |
| Population diversity | N/A | N/A | Higher than GA |
| Parameter transfer | Works (min unchanged) | N/A | Works |
| Error mitigation | Mixed (ZNE) | N/A | Partial |

## Resources

- See references/qaoa-noise-analysis.md for LSC metric details
- See references/logq-algorithm.md for LogQ implementation
- See references/hqga-comparison.md for hybrid algorithm benchmarks

## Related Skills

- quantum-portfolio-optimizer: QAOA with constraints
- quantum-ml-patterns: General QML patterns
- quantum-finance-portfolio: Financial applications
