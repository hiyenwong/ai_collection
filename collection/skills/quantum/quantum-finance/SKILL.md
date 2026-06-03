---
name: quantum-finance
version: v1.0.0
last_updated: 2026-04-06
description: "Quantum computing applications in finance: portfolio optimization, option pricing, risk management, and financial simulations using quantum algorithms (QAOA, quantum annealing, quantum Monte Carlo, amplitude estimation). Use for quantum finance research, NISQ-era financial applications, and quantum advantage analysis in derivatives/derivatives pricing."
---

# Quantum Finance

Quantum computing applications in financial engineering and quantitative finance.

## Activation Keywords
- quantum finance
- quantum portfolio optimization
- quantum option pricing
- quantum risk management
- quantum Monte Carlo finance
- QAOA portfolio
- quantum annealing finance
- quantum derivatives
- quantum algorithms finance
- 量子金融
- 量子投资组合

## Tools Used
- `exec`: Run Python quantum finance scripts
- `read`: Load quantum finance research papers
- `web_search`: Search arxiv for quantum finance papers
- `feishu_bitable_app`: Create/analyze quantum finance data tables

## Core Applications

### 1. Portfolio Optimization
**Algorithms**: QAOA, Quantum Annealing (D-Wave), VQE
**Advantage**: Higher-order moments (skewness, kurtosis) beyond mean-variance

Key papers:
- Higher-Order Portfolio Optimization with QAOA (arxiv:2509.01496)
- End-to-End Portfolio Optimization with Quantum Annealing (arxiv:2504.08843)
- PO-QA Framework (arxiv:2407.19857)

### 2. Option Pricing & Derivatives
**Algorithms**: Quantum Amplitude Estimation (QAE), Quantum Monte Carlo
**Advantage**: Quadratic speedup over classical Monte Carlo

Key papers:
- Option Pricing using Quantum Computers (arxiv:1905.02666)
- A Threshold for Quantum Advantage in Derivative Pricing (arxiv:2012.03819)
- Quantum Monte Carlo Integration (arxiv:2105.09100)

### 3. Risk Management
**Applications**: VaR estimation, credit risk, scenario generation
**Algorithms**: Quantum Monte Carlo for risk analytics

Key papers:
- Quantum Monte Carlo simulations for financial risk analytics (arxiv:2303.09682)

### 4. Quantum Game Theory for Economics
**Applications**: Non-Nashian equilibria, quantum decision theory
**Key insight**: Nash equilibria incompatible with Bell inequality violations

Key papers:
- Nashian game theory is incompatible with quantum physics (arxiv:2112.03881)
- Quantum games and synchronicity (arxiv:2408.15444)

## Instructions for Agents

### Step 1: Identify Financial Problem Type
Categorize the financial problem:
- Portfolio optimization → QAOA/Annealing
- Derivative pricing → QAE/QMC
- Risk analytics → QMC
- Economic modeling → Quantum game theory

### Step 2: Assess Quantum Advantage Potential
Evaluate if quantum advantage is achievable:
- Check problem size and complexity
- Consider NISQ-era constraints
- Estimate resource requirements

### Step 3: Select Appropriate Algorithm
| Problem | Algorithm | Current Feasibility |
|---------|-----------|---------------------|
| Portfolio (small) | QAOA | NISQ-ready |
| Portfolio (large) | Quantum Annealing | Available (D-Wave) |
| Option pricing | QAE | Requires fault-tolerant |
| Monte Carlo | QMC | Partial NISQ |
| Game theory | Quantum games | Theoretical |

### Step 4: Implement or Recommend Solution
Provide implementation guidance based on current quantum hardware capabilities.

## NISQ-Era Considerations

Current quantum computers have limitations:
- **QAOA**: Works for small portfolios (10-50 assets)
- **Quantum Annealing**: Available on D-Wave, handles larger problems
- **QAE**: Requires error correction for full advantage
- **QMC**: Reduced circuit depth versions exist

## References

For detailed algorithm specifications, see:
- [QAOA.md](references/QAOA.md) - QAOA implementation details
- [QMC.md](references/QMC.md) - Quantum Monte Carlo methods
- [GAMES.md](references/GAMES.md) - Quantum game theory foundations

## Examples

### Example 1: Portfolio Optimization Analysis
```
User: "Analyze quantum portfolio optimization methods for a 30-asset portfolio"

Agent: 
1. Identifies QAOA as suitable algorithm
2. Calculates expected qubit requirements (~30-60 qubits)
3. References Higher-Order Portfolio Optimization paper
4. Provides implementation outline using Qiskit/Cirq
```

### Example 2: Quantum Advantage Threshold
```
User: "When does quantum computing become advantageous for option pricing?"

Agent:
1. References Threshold for Quantum Advantage paper (arxiv:2012.03819)
2. Explains resource estimates: error rates, qubits, circuit depth
3. Estimates threshold conditions for practical advantage
```

## Related Skills
- `stock-analysis` - Classical stock technical analysis
- `akshare` - Financial data fetching
- `thsdk-stock` - Chinese stock market analysis

## Knowledge Graph Integration

Papers in kg.db with quantum finance keywords:
- Search: `quantum portfolio optimization`, `QAOA`, `quantum Monte Carlo`, `quantum option pricing`, `quantum annealing`

## Notes
- Quantum finance is an emerging field
- NISQ-era algorithms have practical limitations
- Hybrid quantum-classical approaches are recommended
- Monitor arxiv for latest developments