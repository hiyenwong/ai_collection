---
name: eeg-foundation-sae-interpretability
description: "Mechanistic interpretability of EEG foundation models via Sparse Autoencoders (SAEs). Extract sparse feature dictionaries from EEG transformer embeddings (SleepFM, REVE, LaBraM). Ground features in clinical taxonomy (abnormality, age, sex, medication). Concept steering with target vs. off-target probe area metric. Reveals three operational regimes: selectively steerable, encoded but entangled, non-encoded. Exposes wrecking-ball interventions and clinical entanglements (age-pathology confounding). Use when interpreting EEG foundation models, analyzing neural embeddings, applying SAEs to biomedical time series, or performing concept steering on clinical models. Activation: EEG interpretability, SAE sparse autoencoder EEG, EEG foundation model mechanistic, concept steering brain model."
---

# EEG Foundation Model Interpretability via SAEs

Apply TopK Sparse Autoencoders to extract interpretable features from EEG foundation model embeddings. Ground features in clinical taxonomy.

## Workflow

### 1. Train TopK SAE on Model Embeddings

Extract embeddings from target layer of EEG transformer (SleepFM, REVE, LaBraM). Train TopK SAE:
- Dictionary size: 8x-64x embedding dimension
- TopK: 32-128 active features per input
- Loss: reconstruction + L0 sparsity constraint

### 2. Ground Features in Clinical Taxonomy

Map each SAE feature to clinical concepts:
- Abnormality markers (epileptiform, slowing, etc.)
- Demographics (age, sex)
- Medication effects
- Artifact patterns

### 3. Concept Steering with Probe Metrics

For each clinical concept:
- **Target area**: region where steering should activate
- **Off-target area**: regions where steering should NOT activate
- **Selectivity metric** = target activation / off-target activation

### 4. Identify Operational Regimes

Classify features into three regimes:
1. **Selectively steerable**: high target, low off-target — clean intervention possible
2. **Encoded but entangled**: activated but mixed with other concepts — partial control
3. **Non-encoded**: not represented in model — concept absent from representation

### 5. Critical Failure Modes

- **Wrecking-ball interventions**: steering one concept collapses global model performance
- **Clinical entanglements**: age-pathology confounding — model conflates age-related changes with disease markers
- **Cross-architecture divergence**: same concept represented differently across SleepFM/REVE/LaBraM

## Best Practices

- Always validate steering effects on held-out clinical datasets
- Report both target and off-target metrics — steering without selectivity is dangerous
- Compare across multiple architectures to identify robust vs. architecture-specific features
- Check for demographic confounding before clinical deployment

## Activation

Keywords: EEG interpretability, SAE sparse autoencoder EEG, EEG foundation model mechanistic, concept steering brain model, clinical model interpretability

Source: arXiv:2605.13930 — "Mechanistic Interpretability of EEG Foundation Models via Sparse Autoencoders"
