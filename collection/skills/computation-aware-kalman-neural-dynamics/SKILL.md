---
name: computation-aware-kalman-neural-dynamics
description: "Computation-Aware State-Space Model (CASSM) for Bayesian latent variable modeling of neural recordings in scale-imbalanced regime. Combines computational uncertainty with model selection for tractable inference."
category: neuroscience
---

## Context

Computation-Aware Kalman Filtering with Model Selection for Neural Dynamics (arXiv:2606.01468)
Authors: JR Huml, Jonathan Wenger, John P. Cunningham
Submitted: June 2026

## Core Methodology

1. **Extends computation-aware Kalman filtering to model selection with novel training loss**
2. **CASSM designed for scale-imbalanced regime (few trials, many neurons)**
3. **Competitive with deep networks with improved uncertainty calibration**
4. **Quadratic complexity avoided through tractable inference scheme**
5. **Roadmap for choosing dynamical latent variable models based on dataset properties**

## Implementation Steps

1. **Paper Review**: Read full paper from https://arxiv.org/abs/2606.01468
2. **Method Analysis**: Extract key algorithm/framework components
3. **Code Implementation**: Implement core components in Python/PyTorch
4. **Validation**: Test on synthetic data or available benchmarks
5. **Integration**: Apply to neuroscience data analysis workflows

## Key Results

Key findings from paper:
- Extends computation-aware Kalman filtering to model selection with novel training loss
- CASSM designed for scale-imbalanced regime (few trials, many neurons)
- Competitive with deep networks with improved uncertainty calibration

## Pitfalls

- Computational complexity in large state-spaces
- Model selection hyperparameter tuning required
- Scale imbalance between trials and neurons affects performance
- Uncertainty calibration may degrade with overparameterization

## Verification

- Compare with baseline methods (linear encoding, deep networks)
- Check uncertainty calibration metrics
- Validate on held-out neural recording data

## Activation

Kalman filtering, neural dynamics, Bayesian, state-space model, latent variable
