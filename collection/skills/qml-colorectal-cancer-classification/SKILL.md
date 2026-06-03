---
name: qml-colorectal-cancer-classification
description: "Quantum machine learning for clinical risk prediction with imbalanced data — F_beta-optimized QNN configurations for minority class identification in low-prevalence medical outcomes. Covers ZZFeatureMap encodings, RealAmplitudes/EfficientSU2 ansatze, noisy simulation, and quantum advantage for clinical sensitivity. Activation: quantum machine learning cancer, QNN clinical prediction, anastomotic leak prediction, quantum minority class, F-beta optimized quantum, quantum medical classification, quantum colorectal, quantum surgical outcome, ZZFeatureMap medical, quantum sensitivity optimization, quantum clinical risk"
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2604.13951"
  published: "2026-04-15"
  authors: "Vojtech Novak, Ivan Zelinka, Lenka Pribylova, Lubomir Martinek, Vladimir Bencurik, Martin Beseda"
  tags: [quantum, machine-learning, medical, classification, imbalanced-data]
---

## Problem Statement

Classify rare clinical events (e.g., anastomotic leak at 14% prevalence) where classical models sacrifice sensitivity for overall accuracy. Quantum feature spaces better prioritize minority class identification.

## Core Methodology

### Quantum Feature Encoding + Ansatz Selection

1. **ZZFeatureMap** — entangling quantum feature encoding that maps clinical features into Hilbert space
2. **Ansatz choices**:
   - `RealAmplitudes` — parameterized rotation layers with real-valued amplitudes
   - `EfficientSU2` — hardware-efficient SU(2) rotation ansatz
3. **F_beta optimization** — optimize for F_beta score (emphasizes recall) instead of accuracy

### Key Results

| Metric | Classical Baseline | QNN (F_beta-optimized) |
|--------|-------------------|----------------------|
| Sensitivity | 66.7% | 83.3% |
| Prevalence | 14% (anastomotic leak) | 14% |

### Workflow

1. **Data preparation**: Clinical dataset with known low-prevalence target (10-20%)
2. **Feature encoding**: ZZFeatureMap with depth matching feature count
3. **Ansatz selection**: Compare RealAmplitudes vs EfficientSU2 under simulated noise
4. **Optimization**: Use F_beta (not accuracy) as primary metric — beta > 1 weights recall higher
5. **Noise simulation**: Test under realistic hardware noise models before deployment
6. **Optimizer selection**: Evaluate multiple optimizers (COBYLA, SPSA, Adam) for convergence under noise

## Why Quantum Works Here

- **ZZFeatureMap** creates entangled feature representations that capture nonlinear interactions between clinical variables
- **Quantum feature spaces** provide richer decision boundaries for minority class separation
- **F_beta optimization** aligns quantum circuit training with clinical priorities (sensitivity > accuracy)

## Pitfalls

- **Accuracy is misleading for imbalanced data** — a model predicting "no leak" for all cases achieves 86% accuracy but 0% sensitivity. Always use F_beta, recall, or AUC-PR
- **Noise sensitivity** — QNN performance degrades under simulated noise; test ansatz robustness before hardware deployment
- **Small datasets** — quantum models may overfit on small clinical datasets; use regularization or cross-validation
- **Optimizer choice matters** — different optimizers converge to different local minima under noise; compare multiple optimizers

## Activation Keywords

quantum machine learning cancer, QNN clinical prediction, anastomotic leak prediction, quantum minority class, F-beta optimized quantum, quantum medical classification, quantum colorectal, quantum surgical outcome, ZZFeatureMap medical, quantum sensitivity optimization, quantum clinical risk
