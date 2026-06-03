# Quantum Monte Carlo for Finance

Quantum Monte Carlo methods for financial simulations and risk analytics.

## Overview

Quantum Monte Carlo (QMC) provides quadratic speedup for numerical integration and simulation:
- Classical Monte Carlo: O(M) samples for error ε
- Quantum Monte Carlo: O(1/ε) queries for same error
- Potential 100x-1000x speedup for financial applications

## Key Algorithms

### Quantum Amplitude Estimation (QAE)
Core algorithm for Monte Carlo speedup:
```
Classical: M samples → error = σ/√M
Quantum: M queries → error = σ/M
```
Quadratic improvement in convergence rate.

### Variational Quantum Monte Carlo
NISQ-compatible approach using variational circuits.

## Financial Applications

### 1. Value-at-Risk (VaR) Estimation
```python
# Classical approach
def classical_var(portfolio_returns, confidence=0.95):
    return np.percentile(portfolio_returns, (1-confidence)*100)

# Quantum approach (conceptual)
def quantum_var(portfolio_returns, confidence=0.95):
    # Use QAE to estimate tail probability
    # Quadratic speedup for large portfolios
```

### 2. Option Pricing
```
Payoff function: max(S_T - K, 0) for call option
QAE estimates E[payoff] with fewer samples
```

### 3. Credit Risk Modeling
Scenario generation for credit risk factors:
- Equity risk
- Interest rate risk  
- Credit spread risk

## Implementation Considerations

### Circuit Depth Requirements
| Application | Required Depth | NISQ Feasibility |
|-------------|----------------|------------------|
| Simple VaR | ~100 | Partial |
| Option pricing | ~1000+ | Requires error correction |
| Credit risk | ~5000+ | Long-term |

### Error Rates
Threshold for practical advantage: ~10⁻³ error rate per gate

## Minimal Circuit Depth QMC

From arxiv:2105.09100:
- Retains full quadratic advantage
- No arithmetic or phase estimation needed
- Uses amplitude amplification directly

## Key Papers

1. arxiv:2303.09682 - QMC for financial risk analytics
2. arxiv:1905.02666 - Option pricing with quantum computers
3. arxiv:2105.09100 - Minimal circuit depth QMC
4. arxiv:2012.03819 - Threshold for quantum advantage in derivatives

## Practical Guidelines

1. **Current limitation**: Full QAE requires fault-tolerant quantum computers
2. **NISQ alternative**: Variational QMC with reduced depth
3. **Hybrid approach**: Use quantum for sampling, classical for aggregation
4. **When to use**: Large-scale Monte Carlo where classical computation is bottleneck