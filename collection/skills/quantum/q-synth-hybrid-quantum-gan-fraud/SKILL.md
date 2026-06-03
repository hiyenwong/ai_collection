---
name: q-synth-hybrid-quantum-gan-fraud
description: "Hybrid quantum-classical GAN for imbalanced fraud detection. PQC as generator, classical NN as discriminator. Evaluates statistical fidelity and downstream performance."
version: 1.0.0
author: Hermes Agent (Cron Job)
license: MIT
source: arXiv:2605.21164
metadata:
  hermes:
    tags: [Quantum, GAN, Fraud-Detection, Class-Imbalance, Hybrid]
---

# Q-SYNTH: Hybrid Quantum-Classical Adversarial Augmentation

## Overview
Q-SYNTH addresses extreme class imbalance in fraud detection using a hybrid classical-quantum GAN framework. A parameterized quantum circuit (PQC) serves as the generator while a classical neural network serves as the discriminator.

**Paper**: arXiv:2605.21164 (May 2026)

## Core Methodology

### Architecture
- **Generator**: Parameterized quantum circuit encoding minority class distributions
- **Discriminator**: Classical neural network for real vs synthetic classification
- **Training**: Alternating optimization with gradient-based updates

### Evaluation Dimensions
1. **Statistical Fidelity**: Kolmogorov-Smirnov statistics, Wasserstein distances
2. **Detectability**: AUC-ROC for real vs synthetic discrimination
3. **Downstream Performance**: Classification across quantum and classical classifiers

### Key Findings
- Q-SYNTH reduces marginal distribution mismatch vs classical GAN
- SMOTE achieves strongest feature-wise similarity
- Classical GAN attains highest downstream performance in several settings
- Q-SYNTH offers favorable compromise between fidelity and performance

**Activation**: quantum GAN, fraud detection, class imbalance, Q-SYNTH, parameterized quantum circuit, tabular data generation, hybrid quantum-classical
