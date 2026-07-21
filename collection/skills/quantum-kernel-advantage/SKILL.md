---
name: quantum-kernel-advantage
description: >
  Quantum kernel advantage methodology for medical foundation model embeddings.
  Uses Quantum Support Vector Machines (QSVM) with frozen medical foundation model embeddings
  for binary medical classification tasks. Provides evidence of quantum kernel advantage
  over classical kernels on medical imaging data. Use when: medical image classification with
  quantum kernels, QSVM for healthcare, quantum advantage demonstration, medical foundation
  model evaluation, MIMIC-CXR classification, quantum-classical fair comparison,
  quantum embedding methods, two-tier comparison framework, chest radiograph analysis.
---

# Quantum Kernel Advantage in Medical Classification

## Core Pattern

Apply quantum kernels to frozen medical foundation model embeddings to achieve classification advantages over classical kernels on medical imaging tasks.

## Key Paper

**Quantum Kernel Advantage** (arXiv:2604.24597v1): Evidence of quantum kernel advantage on MIMIC-CXR using QSVM with MedSigLIP-448, RAD-DINO, ViT-patch32 embeddings

## Two-Tier Comparison Framework

**Tier 1**: Untuned QSVM vs. untuned linear SVM (C=1) — identical PCA-reduced features
**Tier 2**: Tuned QSVM vs. tuned classical SVM — full hyperparameter optimization

## Implementation

1. Extract embeddings from medical foundation model
2. Apply PCA to reduce to q qubits (q=4-8)
3. Encode using ZZFeatureMap or ZFeatureMap
4. Train QSVM with quantum kernel evaluation
5. Run classical SVM with identical features for fair comparison

## Quantum Feature Map Choices

- **ZZFeatureMap**: Entangling, captures feature interactions
- **ZFeatureMap**: Non-entangling, faster but less expressive
- **PauliFeatureMap**: Generalized, configurable depth

## Pitfalls

- Quantum advantage may disappear on noisy hardware
- Aggressive PCA loses medical features
- Must ensure identical features and search spaces for fair comparison
- Medical data requires careful stratification by patient

## Classical Collapse Analysis

See `references/classical-collapse-comparison.md` for detailed analysis of the classical kernel collapse phenomenon observed with frozen medical foundation model embeddings — including eigenspectrum analysis, tiered comparison framework, and code for effective rank computation.
