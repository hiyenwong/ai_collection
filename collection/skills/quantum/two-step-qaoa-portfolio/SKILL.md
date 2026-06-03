---
name: two-step-qaoa-portfolio
description: Two-Step QAOA methodology for large-scale portfolio optimization. First step uses classical screening to identify promising asset subsets, second step applies quantum optimization for weight allocation. Reduces circuit depth requirements while maintaining solution quality on NISQ devices.
category: quantum-finance
---

# Two-Step QAOA Portfolio Optimization

## Description
Two-Step Quantum Approximate Optimization Algorithm for portfolio optimization that combines classical pre-screening with quantum optimization. The first step identifies promising asset subsets using classical methods (e.g., mean-variance analysis, heuristic screening), then the second step applies QAOA for optimal weight allocation within the reduced search space. This hybrid approach significantly reduces circuit depth requirements while maintaining solution quality, making it practical for NISQ-era quantum devices.

## Activation Keywords
- two-step QAOA
- hybrid portfolio screening
- classical quantum portfolio
- NISQ portfolio optimization
- asset subset screening QAOA
- reduced search space QAOA

## Tools Used
- exec: Run quantum optimization and classical screening scripts
- terminal: Execute portfolio optimization pipelines
- skill_manage: Reference related quantum finance skills

## Usage Patterns

### Large-Scale Portfolio Selection
When the number of assets exceeds available qubits:
1. Apply classical screening to reduce candidate pool
2. Run QAOA on the reduced subset
3. Combine results for full portfolio

### NISQ Device Optimization
For limited-qubit quantum hardware:
1. Use classical heuristics for coarse selection
2. Quantum optimization for fine-tuning weights
3. Validate end-to-end performance

## Instructions for Agents

### Step 1: Classical Screening
Reduce the asset universe using classical methods:
- **Mean-variance screening**: Select top-K assets by Sharpe ratio
- **Clustering-based**: Group correlated assets, pick representatives
- **Momentum screening**: Filter by recent performance trends
- **Risk filtering**: Remove assets with unacceptable risk profiles

Target: Reduce N assets to K assets where K ≤ available qubits

### Step 2: Quantum Weight Optimization
Apply QAOA on the K selected assets:
- Formulate weight allocation as QUBO
- Choose appropriate mixer (XY-mixer for cardinality constraints)
- Consider CD-QAOA for improved performance
- Optimize parameters using classical optimizer

### Step 3: Integration
Combine classical screening results with quantum optimization:
- Map quantum solution back to full asset universe
- Apply portfolio rebalancing constraints
- Validate risk-return profile

### Step 4: Validation
- Backtest against classical-only approaches
- Compare Sharpe ratios, maximum drawdown
- Test robustness across market regimes
- Verify transaction costs are reasonable

## Error Handling

### Screening Misses Good Assets
If classical screening eliminates optimal assets:
1. Use ensemble of screening methods
2. Increase screening pool size (K)
3. Apply diversity constraints to screening

### QAOA Fails to Converge
If quantum optimization doesn't converge:
1. Reduce problem size further
2. Use warm-start from classical solution
3. Try CD-QAOA with counterdiabatic terms

### Hardware Noise
For noisy quantum devices:
1. Apply error mitigation
2. Increase measurement shots
3. Use robust parameter initialization

## Key Findings from Research (2026-05-16)

### Two-Step QAOA (arXiv:2605.06858, entity 1120)
- **Classical screening + quantum optimization** reduces circuit depth
- **Maintains solution quality** compared to full quantum approach
- **Practical for NISQ devices** with limited qubits
- **Workflow**: Screen → Select → Optimize → Validate

### Complementary Findings
- **D-Wave Hybrid Audit**: Quantum contribution mainly in exploration phase
- **QAOA Mixers**: XY mixers preferred for constrained portfolios
- **CCD-QAOA**: Best performance when circuit depth permits

## Best Practices

1. **Always validate classical screening** doesn't eliminate optimal solutions
2. **Use multiple screening methods** for robustness
3. **Start simple**: X-mixer → XY-mixer → CD-QAOA progression
4. **Monitor circuit depth** vs. solution quality tradeoff
5. **Benchmark against classical baselines** (mean-variance, Black-Litterman)

## Resources
- arXiv:2605.06858 (kg.db entity 1120)
- kg.db entities 1118-1120 for related portfolio papers

## Related Skills
- `cd-qaoa-portfolio-optimization`: Counterdiabatic QAOA methodology
- `quantum-finance-portfolio`: Standard quantum portfolio optimization
- `qbalance-quantum-workflow-optimization`: Quantum workflow optimization