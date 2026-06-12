---
name: dolq-ode-discovery-llm
description: >
  DoLQ: Discovering Ordinary Differential Equations with LLM-based qualitative and quantitative
  evaluation. Multi-agent architecture for symbolic regression of governing ODEs from data.
  Sampler Agent proposes candidates, Parameter Optimizer refines equations, Scientist Agent
  uses LLM for combined qualitative (domain knowledge) and quantitative (fit metrics) evaluation
  to iteratively guide search. Accepted at ICML 2026. Use when: ODE discovery, symbolic regression,
  scientific ML, equation discovery, multi-agent scientific discovery, LLM-guided optimization.
  Activation: ODE discovery, equation discovery, LLM scientific discovery, symbolic regression
---

# DoLQ: LLM-Based ODE Discovery with Qualitative & Quantitative Evaluation

> Multi-agent symbolic regression framework that combines LLM-based qualitative evaluation with quantitative metrics to discover governing ODEs from observational data.

## Metadata
- **Source**: arXiv:2605.07323
- **Authors**: Sum Kyun Song, Bong Gyun Shin, Jae Yong Lee
- **Published**: 2026-05-08
- **Venue**: ICML 2026

## Core Methodology

### Key Innovation
Existing symbolic regression relies primarily on quantitative metrics (fit quality, complexity). Real-world ODE modeling also requires **domain knowledge** for physical plausibility. DoLQ bridges this gap with a multi-agent architecture that evaluates candidates on **both** qualitative and quantitative criteria.

### Multi-Agent Architecture

**1. Sampler Agent**
- Proposes dynamic system candidates (symbolic ODE forms)
- Explores the space of possible equation structures

**2. Parameter Optimizer**
- Refines proposed equations for numerical accuracy
- Optimizes coefficients to minimize prediction error

**3. Scientist Agent (LLM-based)**
- Conducts **qualitative evaluation**: domain knowledge, physical plausibility, known constraints
- Conducts **quantitative evaluation**: fit metrics, error measures, complexity
- **Synthesizes** both evaluations to iteratively guide the search

### Search Loop
1. Sampler proposes candidate ODEs
2. Parameter Optimizer fits coefficients
3. Scientist Agent evaluates (qualitative + quantitative)
4. Synthesized feedback guides next iteration of proposals

## Implementation Guide

### Prerequisites
- LLM with scientific reasoning capability
- Numerical ODE solver (e.g., scipy.integrate)
- Symbolic expression representation

### Key Design Patterns
- Multi-agent decomposition: separate proposal, optimization, and evaluation
- LLM as domain expert: qualitative assessment beyond numerical metrics
- Iterative refinement: feedback loop guides search direction
- Dual evaluation: both physical plausibility and numerical accuracy

### Evaluation Metrics
- Success rate on multi-dimensional ODE benchmarks
- Accuracy of recovered symbolic terms vs. ground truth
- Comparison with existing symbolic regression methods

## Applications
- Scientific discovery of governing equations from data
- Physics-informed ML with domain knowledge integration
- Automated scientific hypothesis generation
- Engineering system identification
- Computational biology model discovery

## Pitfalls
- LLM qualitative evaluation depends on prompt quality and domain specificity
- Requires ground truth for validation — may be unavailable for novel domains
- Multi-agent overhead vs. single-agent approaches
- Symbolic term recovery accuracy depends on search space definition
- Physical plausibility assessment requires well-designed evaluation criteria

## Related Skills
- dolq-ode-discovery-llm
- pem-ude-neural-governing-equations
