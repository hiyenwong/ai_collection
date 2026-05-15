---
name: quantum-finance-stack-analysis
description: "Financial computation stack framework for evaluating quantum computing applicability in finance. Covers five interconnected layers: portfolio optimisation, derivative pricing, risk estimation, quantum ML, and post-quantum cryptography. Use when analyzing quantum computing applications in finance, evaluating quantum finance workflows, designing hybrid quantum-classical financial systems, or assessing quantum advantage claims in financial contexts."
---

# Quantum Finance Stack Analysis

Framework for systematically evaluating quantum computing applicability across the financial computation stack, based on arXiv:2604.08180.

## The Five-Layer Stack

1. **Portfolio Optimisation Layer** - Constrained search dominates; QAOA/quantum annealing most credible when combinatorial complexity is binding cost
2. **Derivative Pricing Layer** - Amplitude estimation methods matter when repeated expectation evaluation is the binding cost (Monte Carlo acceleration)
3. **Risk Estimation Layer** - Tail-risk and scenario estimation; quantum advantage when rare-event analysis is bottleneck
4. **Quantum ML Layer** - Task-dependent; strongest in pattern recognition on high-dimensional financial data where quantum kernels offer expressivity advantage
5. **Post-Quantum Cryptography Layer** - Already strategically necessary; financial infrastructure must migrate before fault-tolerant attacks arrive

## Evaluation Framework

For each layer, apply this logic:

1. **Identify the financial bottleneck** - What computational problem limits current approaches?
2. **Specify the quantum primitive** - Which quantum algorithm addresses this bottleneck?
3. **Compare with classical benchmark** - What is the best classical alternative?
4. **Assess implementation constraints** - Qubit count, coherence time, error rates, data loading overhead
5. **Determine hybrid vs. pure quantum** - Near-term advantage lies in hybrid workflows, not pure quantum

## Key Findings

- **Strongest near-term case**: Hybrid quantum-classical workflows rather than blanket quantum advantage claims
- **Quantum optimisation**: Most credible when constrained search dominates (portfolio selection, asset allocation)
- **Amplitude estimation**: Most impactful for repeated expectation evaluation (option pricing, VaR calculation)
- **Quantum ML**: Remains highly task-dependent; no universal advantage demonstrated
- **Post-quantum crypto**: Already strategically necessary - migrate before fault-tolerant quantum attacks

## Hybrid Workflow Design

Design hybrid quantum-classical financial systems where:

- Classical preprocessing handles data loading and feature engineering
- Quantum subroutine solves the combinatorial core
- Classical postprocessing validates and interprets results
- Feedback loop iterates between quantum and classical layers

## Implementation Checklist

- [ ] Identify computational bottleneck in financial workflow
- [ ] Map to appropriate quantum primitive (QAOA, amplitude estimation, quantum kernel, etc.)
- [ ] Establish classical baseline performance
- [ ] Estimate qubit requirements and circuit depth
- [ ] Design hybrid quantum-classical pipeline
- [ ] Validate against classical benchmark under realistic noise models
- [ ] Assess post-quantum cryptography readiness

## Resources

- Primary paper: arXiv:2604.08180 (134 pages, comprehensive review)
- Related: qbalance-workflow-optimization skill for quantum workflow selection
