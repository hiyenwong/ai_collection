---
name: joint-surrogate-learning-neuromorphic
description: DMOSOPT — scalable optimization framework using jointly learned surrogate models for constrained multi-objective optimization of neural dynamical systems. Learns smooth approximations of objective landscapes and feasibility boundaries to guide search with unified gradients.
version: 1.0.0
metadata:
  hermes:
    tags: [multi-objective-optimization, surrogate-models, DMOSOPT, neural-dynamics, supercomputing, constrained-optimization]
    source_paper: "Joint Surrogate Learning of Objectives, Constraints, and Sensitivities for Efficient Multi-objective Optimization of Neural Dynamical Systems (arXiv:2603.20984)"
    citations: 0
---

# DMOSOPT: Joint Surrogate Learning for Neural System Optimization

## Overview

Paper: arXiv:2603.20984 (2026-03-22)
Authors: Gressmann, Frithjof; Raikov, Ivan Georgiev; Kim, Seung Hyun; Gazzola, Mattia; Rauchwerger, Lawrence

Biophysical neural system simulations are among the most computationally demanding scientific applications. Their optimization requires navigating high-dimensional parameter spaces under numerous constraints with binary feasible/infeasible partitions and no gradient signal. DMOSOPT introduces a **unified, jointly learned surrogate model** that captures the interplay between objectives, constraints, and parameter sensitivities.

## Key Contributions

1. **Unified Joint Surrogate** — Single model learns objectives, constraints, and sensitivities simultaneously
2. **Smooth Approximation** — Learns smooth approximations of objective landscapes and feasibility boundaries
3. **Unified Gradient Steering** — Provides gradients that simultaneously steer toward better objectives and constraint satisfaction
4. **Sensitivity Estimation** — Partial derivatives yield per-parameter sensitivity estimates for targeted exploration
5. **Supercomputing Scale** — Validated from single-cell dynamics to population-level networks at scale

## Problem Setting

### Challenge

- **High-Dimensional Parameter Spaces**: Neural models have many tunable parameters
- **Binary Constraints**: Feasible/infeasible regions with no gradient signal
- **Computational Cost**: Each simulation evaluation is expensive
- **Multi-Objective**: Multiple competing objectives to optimize simultaneously

### DMOSOPT Solution

```
Training Data → Joint Surrogate Model → Unified Gradient + Sensitivities → Guided Optimization → Fewer Evaluations
```

## Joint Surrogate Model

### Components

1. **Objective Surrogate**: Smooth approximation of the objective function landscape
2. **Constraint Surrogate**: Smooth approximation of the feasibility boundary
3. **Sensitivity Estimator**: Partial derivatives provide per-parameter importance

### Unified Gradient

The joint surrogate provides a single gradient signal that:
- **Steers toward improvement**: Direction of objective optimization
- **Respects constraints**: Avoids infeasible regions
- **Guides exploration**: Sensitivity estimates focus search on impactful parameters

## Optimization Pipeline

1. **Initial Sampling**: Generate initial parameter configurations (e.g., Latin hypercube)
2. **Evaluation**: Run expensive simulations for each configuration
3. **Surrogate Training**: Fit joint surrogate model to collected data
4. **Gradient-Guided Search**: Use surrogate gradients to propose new configurations
5. **Iterative Refinement**: Alternate between evaluation and surrogate updates
6. **Convergence**: Stop when improvement plateaus or budget exhausted

## Validation Scope

- **Single-Cell Dynamics**: Ion channel parameter optimization
- **Population-Level Networks**: Network connectivity and dynamics tuning
- **Incremental Stages**: Full neural circuit modeling workflow
- **Supercomputing Scale**: Validated on HPC systems

## Applications

- **Computational Neuroscience**: Parameter fitting for biophysical models
- **Neuromorphic Computing**: Hardware parameter optimization
- **Scientific Computing**: Constrained multi-objective optimization in any domain
- **Hyperparameter Optimization**: ML model tuning with expensive evaluations

## When to Use This Skill

- Optimizing expensive simulation-based models with constraints
- Multi-objective optimization where gradient information is unavailable
- Parameter fitting for biophysical neural models
- Any scenario with expensive evaluations and complex feasibility constraints

## Advantages Over Traditional Methods

| Method | Gradient Information | Constraint Handling | Evaluation Efficiency |
|--------|---------------------|-------------------|----------------------|
| Grid Search | No | Hard constraints only | Very poor |
| Bayesian Optimization | No (acquisition) | Soft constraints | Moderate |
| Genetic Algorithms | No | Penalty functions | Poor |
| DMOSOPT | **Yes (learned)** | **Unified with objectives** | **High** |

## References

- **Paper**: Gressmann, F., Raikov, I.G., Kim, S.H., Gazzola, M., Rauchwerger, L. "Joint Surrogate Learning of Objectives, Constraints, and Sensitivities for Efficient Multi-objective Optimization of Neural Dynamical Systems," arXiv:2603.20984, Mar. 2026
- **Related**: Surrogate modeling, multi-objective optimization, Bayesian optimization, parameter fitting