---
name: quantum-latent-gan-benchmark
description: "Controlled benchmark methodology for evaluating quantum generative models in medical imaging augmentation. Establishes rigorous evaluation framework comparing quantum vs classical generators under matched parameter budgets, multiple random seeds, and paired significance testing. Use when evaluating quantum generative augmentation for medical images, designing controlled benchmarks for quantum vs classical model comparison, or assessing data augmentation quality in low-data regimes. Covers: KL-regularized latent space encoding, conditional WGAN-GP training, parameter-matched comparison, low-data fraction evaluation, mode collapse detection, and diversity analysis."
---

# Quantum-Latent GAN Benchmark for Medical Imaging

## Core Methodology

From arXiv:2606.18970 — "A Controlled Benchmark of Quantum-Latent GAN Augmentation for Brain MRI" (Haider & Figini, 2026-06-17)

## Problem Statement

Quantum generative models for medical image augmentation frequently report accuracy gains, but claims are typically based on:
- Single training runs (no statistical rigor)
- Unmatched parameter budgets between quantum and classical generators
- No characterization of the data regime where benefit appears

## Controlled Benchmark Framework

### 1. Latent Space Encoding
- Encode images into a KL-regularized latent space
- Ensures consistent representation for both quantum and classical generators

### 2. Parameter-Matched Generator Comparison
- Train conditional Wasserstein GAN with gradient penalty (WGAN-GP)
- Quantum generator and classical generator have near-identical parameter counts (e.g., 1648 vs 1632)
- Eliminates capacity as a confounding variable

### 3. Data Fraction Evaluation
- Evaluate across labeled data fractions: 5%, 10%, 25%, 50%, 100%
- Use synthetic samples to augment pretrained classifier
- Identifies regime where quantum benefit (if any) emerges

### 4. Statistical Rigor
- Run 8+ random seeds per configuration
- Paired significance testing with multiple-comparison correction
- Avoid single-run cherry-picking

### 5. Quality Diagnostics
- **Intra-set diversity analysis**: Measure diversity of synthetic samples
- **Latent distribution analysis**: Compare synthetic vs real latent distributions
- **Mode collapse detection**: Identify when generator collapses to limited output modes

## Key Findings

1. **No significant advantage**: Across all data fractions, no augmentation variant significantly outperforms real-data-only training
2. **Quantum ≈ Classical**: Quantum and classical generators are statistically indistinguishable
3. **Low-data benefit = regularization**: Any apparent benefit in low-data regime behaves as regularization, not faithful data expansion
4. **Mode collapse**: Synthetic samples are off-distribution and severely mode-collapsed where data is scarce
5. **No diversity advantage**: Quantum generator is no more diverse than classical counterpart

## Application Checklist

When designing quantum generative benchmarks for medical imaging:
- [ ] Match parameter budgets between quantum and classical baselines
- [ ] Use multiple random seeds (≥8) for statistical significance
- [ ] Apply paired tests with multiple-comparison correction
- [ ] Evaluate across data fractions (not just one setting)
- [ ] Include diversity and distribution diagnostics
- [ ] Report negative/null results honestly

## Activation

- quantum generative augmentation
- quantum GAN medical imaging
- quantum vs classical benchmark
- medical image data augmentation
- controlled benchmark quantum ML
- mode collapse detection
- KL-regularized latent space
- WGAN-GP quantum generator
