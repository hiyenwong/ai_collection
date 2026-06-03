---
name: quantum-option-pricing-heat-equation
description: "Exponentially fast quantum state preparation for the heat equation applied to financial option pricing. Maps Black-Scholes PDE to quantum linear system via heat equation discretization, achieving exponential speedup over classical methods. Use when: quantum finance, option pricing on quantum computers, Black-Scholes quantum solver, PDE-to-quantum mapping, quantum derivatives pricing, heat equation quantum simulation."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.28950"
  published: "2026-05-29"
  tags: [quantum, finance, option-pricing, PDE, heat-equation, black-scholes]
---

# Quantum Option Pricing via Heat Equation State Preparation

## Core Methodology

Presents methods for pricing financial derivatives on quantum devices with provable advantage over classical methods. Maps the Black-Scholes partial differential equation to a quantum linear system via heat equation discretization, enabling exponentially fast solution state preparation.

## Key Insights

1. **PDE-to-Quantum Mapping**: Black-Scholes PDE can be transformed to a heat equation, which maps naturally to a quantum linear system Ax = b
2. **Exponential Speedup**: Quantum state preparation for the heat equation achieves exponential speedup in spatial dimension compared to classical discretization
3. **Derivative Pricing Pipeline**: Complete pipeline from financial contract specification to quantum circuit implementation
4. **NISQ-Compatible**: Includes error analysis and resource estimates for near-term quantum devices

## Algorithm Steps

1. **Black-Scholes to Heat Equation**: Transform BS PDE via change of variables to standard heat equation
2. **Discretization**: Discretize heat equation on grid, yielding linear system
3. **Quantum Encoding**: Encode discretized system as quantum linear system using amplitude encoding
4. **HHL or QLSA**: Solve using Quantum Linear System Algorithm (HHL variant)
5. **Payoff Extraction**: Extract option price from quantum state via amplitude estimation
6. **Error Bounds**: Provide rigorous error bounds for discretization + quantum algorithm

## When to Use

- Pricing European/American options on quantum hardware
- Portfolio risk analysis with quantum speedup
- Monte Carlo alternatives for derivative pricing
- Any PDE-based financial modeling task

## Practical Considerations

- Requires fault-tolerant quantum computer for full advantage
- NISQ-friendly variants use variational approaches
- Condition number of discretized system affects HHL runtime
- Amplitude estimation provides quadratic speedup for expectation estimation

## Related Approaches

- Quantum Monte Carlo for option pricing
- Quantum amplitude estimation for risk measures
- Classical finite difference methods
- Quantum PDE solvers (QLSA-based)
