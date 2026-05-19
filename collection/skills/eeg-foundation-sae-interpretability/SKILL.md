---
name: eeg-foundation-sae-interpretability
description: Mechanistic interpretability of EEG foundation models via Sparse Autoencoders (SAEs). Extracts monosemantic features from EEG transformers, diagnoses representational failures, and enables concept steering with clinical grounding. Use when interpreting EEG foundation models (SleepFM, REVE, LaBraM), applying SAEs to brain signal transformers, benchmarking model interpretability, or performing clinical concept steering on neuroimaging models.
---

# Mechanistic Interpretability of EEG Foundation Models via SAEs

Framework for extracting, analyzing, and steering internal representations of EEG foundation models using TopK Sparse Autoencoders. Bridges the gap between black-box clinical performance and interpretable, trustworthy neuroscience.

## Architecture

### Pipeline

```
EEG Foundation Model (SleepFM/REVE/LaBraM)
    ↓ Extract embeddings
TopK Sparse Autoencoder (SAE)
    ↓ Sparse feature dictionary
Clinical Taxonomy Grounding (abnormality, age, sex, medication)
    ↓ Monosemanticity & entanglement analysis
Concept Steering + Spectral Decoder
    ↓ Physiologically interpretable frequency signatures
```

## Key Methodology

### Sparse Autoencoder Training

- **TopK sparsity**: Enforces exactly K active features per input
- **Dictionary health audit**: Intrinsic procedure to validate feature quality
- **Cross-architecture transfer**: Single hyperparameter procedure works across SleepFM, REVE, LaBraM

### Three Operational Regimes (Concept Steering)

1. **Selectively steerable**: Clean feature manipulation without side effects
2. **Encoded but entangled**: Feature exists but coupled with others
3. **Non-encoded**: Concept not represented in model internals

### Failure Mode Detection

- **"Wrecking-ball" interventions**: Steering that collapses global performance
- **Clinical entanglements**: Age-pathology confounding — cannot suppress one without corrupting the other

### Spectral Decoder

Maps latent steering interventions back to EEG amplitude spectrum:
- Pathological slow-wave suppression
- α-band restoration
- Physiologically interpretable frequency signatures

## Clinical Applications

- Explain model predictions to clinicians
- Detect and mitigate demographic confounds (age, sex, medication effects)
- Validate model decisions against known neurophysiological markers
- Generate interpretable frequency-domain explanations

## Implementation Steps

### Step 1: Extract Embeddings

Run target EEG transformer on clinical dataset. Extract layer embeddings.

### Step 2: Train SAE

Fit TopK SAE on embeddings. Use intrinsic dictionary health audit to tune K.

### Step 3: Ground Features

Map sparse features to clinical taxonomy (abnormality, age, sex, medication).

### Step 4: Benchmark Monosemanticity

Quantify feature purity and entanglement across clinical concepts.

### Step 5: Concept Steering

Apply steering vectors. Evaluate via "target vs. off-target" probe metric.

### Step 6: Spectral Decoding

Map steering effects back to EEG frequency domain for clinical interpretation.

## When to Use

- EEG foundation model interpretability analysis
- Clinical validation of neuroimaging AI models
- Detecting model biases and confounds
- Generating neurophysiologically grounded explanations
- Comparing representational quality across EEG architectures

## Related Skills

- `eeg-foundation-lrp-interpretability`: LRP-based EEG interpretability
- `eeg-foundation-model-adapters`: Domain adaptation for EEG FMs
- `eeg-sae-interpretability`: SAE-based EEG interpretability (overlaps)

## References

Based on: Lehn-Schiøler et al. (2026). "Mechanistic Interpretability of EEG Foundation Models via Sparse Autoencoders." arXiv:2605.13930
