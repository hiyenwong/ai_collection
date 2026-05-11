---
name: "dolq-ode-discovery-llm"
description: "DoLQ framework for discovering ODEs using LLM-based qualitative and quantitative evaluation. Multi-agent architecture for interpretable scientific equation discovery. Activation: ODE discovery, symbolic regression LLM, DoLQ, scientific equation discovery, multi-agent discovery, dynamical system discovery, SINDy alternative."
---

# DoLQ: Discovering ODEs with LLM-Based Qualitative and Quantitative Evaluation

**Paper:** Sum Kyun Song, Bong Gyun Shin, Jae Yong Lee — "Discovering Ordinary Differential Equations with LLM-Based Qualitative and Quantitative Evaluation" (arXiv: 2605.07323, accepted at ICML 2026)
**Code:** https://github.com/Bon99yun/DoLQ

## Overview

DoLQ is a multi-agent framework that discovers governing ordinary differential equations from observational data by combining quantitative metrics (MSE, parameter fitting) with qualitative evaluation (LLM-based semantic assessment of physical plausibility). Key insight: similar MSE values can correspond to completely different equations — quantitative metrics alone are insufficient for correct scientific discovery.

## Core Problem

Traditional symbolic regression and SINDy rely primarily on quantitative fitting metrics. Different equations can produce nearly identical MSE but represent fundamentally different physics. Real scientific discovery requires domain knowledge and physical plausibility checks. SINDy requires pre-specified basis function libraries.

## Multi-Agent Architecture

### Three-Agent Framework

1. **Sampler Agent** — Proposes dynamic system candidate terms with physical justifications based on system description and Scientist Agent feedback
2. **Parameter Optimizer** — Refines equations for accuracy by fitting coefficients to data
3. **Scientist Agent** — LLM-based evaluator conducting qualitative semantic assessment and quantitative iterative comparison, synthesizing both to guide search

### Iterative Loop

```
System Description -> Sampler Agent -> Candidate Terms -> Parameter Optimizer -> Fitted Equations -> Scientist Agent -> Feedback Loop
```

## Key Innovation: Qualitative Evaluation

- LLM assesses whether proposed equations are physically plausible given system context
- Evaluates mathematical form consistency with known physics/biology principles
- Prevents overfitting to noise by requiring semantic coherence
- Bridges the gap between statistical fit and scientific validity

## Comparison with Existing Methods

| Method | Quantitative | Qualitative | Multi-Agent | Library-Free |
|--------|-------------|-------------|-------------|-------------|
| SINDy | Yes | No | No | No (requires library) |
| Traditional SR | Yes | No | No | Yes |
| **DoLQ** | **Yes** | **Yes** | **Yes** | **Yes** |

## When to Use

- Discovering governing equations from time-series data
- Need interpretable mathematical models of dynamical systems
- Working in physics, chemistry, biology, or engineering domains
- Quantitative fitting alone is insufficient (need physical plausibility)
- Comparing or improving upon SINDy-based approaches
- Building scientific discovery AI systems

## References

- Song et al. (2026). DoLQ: ODE Discovery with LLM Evaluation. arXiv: 2605.07323. ICML 2026.
- Brunton et al. (2016). SINDy: Discovering governing equations from data. PNAS.
