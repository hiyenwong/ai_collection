---
name: asymmetric-nonlinear-return-extrapolation
description: "Asymmetric nonlinear return extrapolation framework for optimal portfolio choice under stochastic volatility. Extends return extrapolation with saturation in belief updating and gain/loss asymmetry. Use when: behavioral portfolio optimization, return extrapolation, asymmetric belief updating, CRRA investor, stochastic volatility portfolio, Heston model portfolio."
metadata:
  arxiv_id: "2606.10805"
  published: "2026-06-10"
  authors: "Unknown"
  tags: [finance, portfolio, behavioral-finance, extrapolation, stochastic-volatility, heston]
---

# Asymmetric Nonlinear Return Extrapolation for Portfolio Choice

## Description
Framework extending return extrapolation with two behaviorally realistic features: **saturation in belief updating** and **asymmetry between gains and losses**. Derives optimal portfolio for CRRA investor under Heston stochastic volatility as sum of sentiment-distorted myopic demand, variance hedging demand, and sentiment hedging demand.

## Activation Keywords
- asymmetric return extrapolation
- nonlinear belief updating
- behavioral portfolio optimization
- saturation extrapolation
- sentiment-distorted portfolio
- gain loss asymmetry portfolio
- 非线性收益外推
- 行为投资组合

## Core Methodology

### Key Innovations
1. **Smooth nonlinear asymmetric extrapolation function** — captures saturation and gain/loss asymmetry
2. **Three-component optimal portfolio decomposition:**
   - Sentiment-distorted myopic demand
   - Variance hedging demand
   - Sentiment hedging demand
3. **Semilinear HJB equation** solved by two independent numerical methods:
   - Finite-difference ADI scheme with time-step policy iteration
   - Deep learning-driven iterative scheme

### Four Behavioral Anomalies Generated
1. **Asymmetric responses to gains and losses**
2. **Attenuated reactions at extremes** (saturation effect)
3. **Excess trading volume**
4. **Welfare loss rising with extrapolation strength**

### Central Finding
**Saturation acts as endogenous correction mechanism** — at same local slope at origin, asymmetric nonlinear extrapolator carries smaller welfare loss than linear one.

## Usage Patterns

### Pattern 1: Portfolio Decomposition Analysis
1. Specify CRRA utility, Heston volatility parameters
2. Define asymmetric nonlinear extrapolation function
3. Solve semilinear HJB via ADI or deep learning scheme
4. Decompose optimal portfolio into three components
5. Analyze behavioral anomalies and welfare implications

### Pattern 2: Saturation Effect Quantification
1. Compare linear vs nonlinear extrapolator at same local slope
2. Measure welfare loss differential
3. Demonstrate saturation as self-correcting mechanism

## Pitfalls
- **Two numerical methods needed** for cross-validation (ADI + deep learning)
- **Saturation is key** — nonlinear extrapolator outperforms linear at same slope due to endogenous correction
- **State-dependent** — effects vary with volatility regime and sentiment level
- **Welfare analysis essential** — welfare loss is the primary metric for comparing extrapolation models
