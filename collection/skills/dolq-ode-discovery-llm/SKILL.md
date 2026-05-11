---
name: dolq-ode-discovery-llm
description: "DoLQ framework for discovering ODEs using LLM-based qualitative and quantitative evaluation. Multi-agent architecture with Sampler Agent, Parameter Optimizer, and Scientist Agent for symbolic equation discovery from observational data. Accepted at ICML 2026. Activation: ODE discovery, equation discovery, symbolic regression, differential equation, dolq, LLM-based evaluation, scientific machine learning."
---

# DoLQ: ODE Discovery with LLM-Based Evaluation

> Multi-agent framework for discovering governing ordinary differential equations from observational data using LLM-based qualitative and quantitative evaluation. Accepted at ICML 2026.

## Metadata
- **Source**: arXiv:2605.07323
- **Authors**: Sum Kyun Song, Bong Gyun Shin, Jae Yong Lee
- **Published**: 2026-05-08
- **Venue**: ICML 2026

## Core Methodology

### Key Innovation
Existing symbolic regression approaches rely primarily on quantitative metrics. DoLQ addresses the gap by incorporating **domain knowledge** via LLM-based qualitative evaluation to ensure physical plausibility of discovered equations.

### Multi-Agent Architecture

1. **Sampler Agent**: Proposes dynamic system candidates (equation structures)
2. **Parameter Optimizer**: Refines equations for numerical accuracy
3. **Scientist Agent**: Leverages LLM to conduct both:
   - **Qualitative evaluation**: Physical plausibility, domain knowledge consistency
   - **Quantitative evaluation**: Numerical accuracy against observed data
   - Synthesizes results to iteratively guide the search

### Workflow

```
Data → Sampler Agent → Candidate Equations
                           ↓
                    Parameter Optimizer → Refined Equations
                           ↓
                    Scientist Agent (LLM)
                    ├── Qualitative Eval (domain knowledge)
                    └── Quantitative Eval (numerical fit)
                           ↓
                    Synthesize → Guide next iteration
                           ↓
                    Best ODE discovered
```

## Applications
- Scientific machine learning for dynamical systems
- Discovering governing equations from neural population data
- Physics-informed equation discovery
- Multi-dimensional ODE benchmark problems

## Implementation Guide

### Prerequisites
- LLM API access (for Scientist Agent)
- Numerical optimization library (for Parameter Optimizer)
- ODE solver for simulation-based evaluation

### Key Design Principles
1. **Multi-agent separation**: Each agent has distinct role and expertise
2. **Iterative refinement**: Feedback loop from evaluation guides search
3. **Dual evaluation**: Both qualitative (LLM domain knowledge) and quantitative (numerical metrics)
4. **Symbolic term recovery**: Focus on recovering correct symbolic terms, not just numerical fit

## Pitfalls
- LLM qualitative evaluation quality depends on prompt design and model capability
- Parameter optimization can be computationally expensive for complex systems
- Search space explosion in high-dimensional ODE discovery
- Only validated on synthetic benchmarks; real-world biological data application needs verification

## Related Skills
- pem-ude-neural-governing-equations
- neural-emulator-theory
- spiking-neural-network-differential-equation
- ode-complexity-dynamics
