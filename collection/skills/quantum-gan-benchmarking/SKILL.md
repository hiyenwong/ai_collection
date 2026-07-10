---
name: quantum-gan-benchmarking
description: Controlled benchmarking methodology for evaluating quantum generative models in medical image augmentation.
trigger_keywords: ["quantum GAN benchmark", "quantum generative model evaluation", "controlled quantum benchmark", "quantum augmentation", "medical image quantum"]
---

# Quantum GAN Benchmarking

## Description

Methodology from arXiv:2606.18970 that provides a controlled benchmark for evaluating quantum generative models in medical image augmentation. Addresses the problem that many quantum ML papers report accuracy gains based on single training runs, unmatched parameter budgets, and no characterization of the data regime where quantum advantage appears.

## Core Methodology

1. **Parameter Budget Matching**: Ensure quantum and classical generators have equivalent parameter counts
2. **Multi-Run Statistics**: Evaluate over many training runs to characterize variance, not just mean performance
3. **Data Regime Sweep**: Test across different training data sizes to identify where quantum models help
4. **Contribution Isolation**: Measure only the quantum generator's contribution to final classification accuracy

## Key Patterns

- **Matched-Parameter Comparison**: Control for model capacity when comparing quantum vs classical
- **Statistical Rigor**: Multiple random seeds, confidence intervals, statistical significance testing
- **Regime Characterization**: Identify the specific conditions (data size, noise level, problem complexity) where quantum provides advantage
- **Ablation-Style Isolation**: Hold everything constant except the generator to isolate quantum contribution

## Applications

- Rigorous evaluation of quantum generative models for medical imaging
- Fair comparison between quantum and classical augmentation strategies
- Identifying practical regimes for quantum advantage in generative modeling
- Setting standards for quantum ML benchmarking

## Activation

Use when: evaluating quantum generative models, benchmarking quantum vs classical augmentation, designing fair quantum ML experiments, medical image generation.

**Keywords**: quantum GAN, controlled benchmark, parameter matching, statistical evaluation, data regime analysis, medical image augmentation, generative models
