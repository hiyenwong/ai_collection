---
name: quantum-gan-benchmark-controlled-evaluation
description: Controlled benchmark methodology for quantum vs classical generators in medical imaging with matched parameters (arXiv:2606.18970)
category: quantum-benchmarking
---

# Controlled Benchmark of Quantum Generative Augmentation

Methodology from arXiv:2606.18970 (June 2026). Rigorous framework for evaluating quantum generative models in medical imaging.

## Core Pattern

Isolate quantum generator contribution through **controlled evaluation**:
- Match parameter budgets between quantum and classical generators (1648 vs 1632 params)
- Multiple random seeds with paired significance testing
- Multiple comparison correction
- Intraset diversity and latent-distribution analyses
- Evaluate across labeled data fractions (5% to 100%)

## Key Findings

- **No augmentation variant** significantly outperforms real-data-only training
- Quantum and classical generators are **statistically indistinguishable**
- Low-data benefit acts as **regularization**, not faithful data expansion
- Synthetic samples are off-distribution and severely mode-collapsed where data is scarce
- Framework released as testbed for rigorous quantum generative evaluation

## Implementation Steps

1. Encode images into KL-regularized latent space
2. Train conditional Wasserstein GAN with gradient penalty
3. Compare quantum vs classical generator with matched parameters
4. Evaluate across data fractions (5%-100%) with 8+ random seeds
5. Apply paired significance testing with multiple-comparison correction
6. Analyze intraset diversity and latent distributions
7. Characterize whether benefits are regularization or faithful expansion

## When to Use

- Evaluating quantum generative models for medical imaging
- Any claim of quantum advantage in generative modeling
- Need for rigorous, controlled benchmarking protocols
- Avoiding false positives from parameter budget mismatches

## References

- arXiv: 2606.18970v2
- Authors: Syed Mujtaba Haider, Silvia Figini
