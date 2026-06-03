---
name: neuroatlas-eeg-foundation-benchmark
description: "NeuroAtlas — largest EEG benchmark (42 datasets, 260k hours) for evaluating foundation models on clinical EEG and BCI tasks. Reveals EEG-specific FMs don't consistently outperform generic time-series FMs, standard ML metrics insufficient for clinical utility. Activation: NeuroAtlas, EEG foundation model, clinical EEG benchmark, brain-computer interface evaluation, EEG-FM benchmark, epilepsy EEG, sleep EEG, brain age estimation."
---

# NeuroAtlas: Benchmarking Foundation Models for Clinical EEG and Brain-Computer Interfaces

The largest EEG benchmark to date for evaluating foundation models on clinical EEG and BCI tasks, revealing critical gaps in current EEG foundation model capabilities.

## Paper

- **arXiv**: 2605.14698
- **Title**: NeuroAtlas: Benchmarking Foundation Models for Clinical EEG and Brain-Computer Interfaces
- **Published**: 2026-05-14
- **Categories**: cs.LG, cs.AI

## Problem

Foundation models (FMs) promise unified representations that generalize across downstream tasks. While they've emerged across fields including EEG, their effectiveness remains unclear:
1. Published evaluations use different datasets, preprocessing, and metrics
2. Clinical relevance is often obscured
3. It's unknown whether EEG-specific FMs actually outperform generic alternatives

## NeuroAtlas Benchmark

The largest EEG benchmark to date:
- **42 datasets** covering diverse domains
- **260k hours** of EEG recordings
- **Clinical domains**: epilepsy, sleep medicine, brain age estimation
- **BCI tasks**: motor imagery, event-related potentials
- **Multiple datasets per task** for robust evaluation
- **Bespoke clinical evaluation metrics** beyond standard ML metrics

### Task Coverage

| Domain | Tasks | Clinical Metrics |
|--------|-------|------------------|
| Epilepsy | Seizure detection, classification | Event-level decision quality |
| Sleep Medicine | Sleep staging | Hypnogram-derived features |
| Brain Age | Age estimation | Brain-age gap |
| BCI | Motor imagery, ERP | Task-specific accuracy |

## Key Findings

### 1. EEG-Specific FMs Don't Consistently Outperform Generic Time-Series FMs
- Generic time-series FMs (no EEG focus, no EEG pretraining) match or beat specialized EEG-FMs
- Challenges assumption that domain-specific pretraining is always beneficial
- Suggests current EEG-FMs haven't fully leveraged domain knowledge

### 2. Standard ML Metrics Are Insufficient for Clinical Utility
- Accuracy/AUC/F1 don't capture clinical decision-making quality
- Need event-level evaluation (epilepsy), hypnogram features (sleep), brain-age gap
- Clinical relevance requires domain-specific validation

### 3. Model Rankings Vary Substantially Within Domains
- A model strong on epilepsy may be weak on sleep
- No single "best" model across all EEG tasks
- Pretrained models perform largely on par, with only narrow advantages for a few

## Implications

- **For Researchers**: Don't assume EEG-specific = better; evaluate rigorously
- **For Clinicians**: Current FMs don't yet deliver "out-of-the-box" unified EEG analysis
- **For the Field**: Need next-generation models that truly leverage EEG domain knowledge

## Applications

- Clinical EEG analysis (epilepsy, sleep disorders)
- Brain-computer interface development
- Brain age estimation for neurodegenerative disease screening
- EEG foundation model evaluation and comparison
- Multi-task EEG learning systems

## Technical Patterns

### Pattern 1: Clinical-Grade Evaluation Beyond Standard Metrics
```
Standard ML metrics → Clinical utility metrics
- Accuracy → Event-level decision quality
- Classification score → Hypnogram-derived features
- Regression error → Brain-age gap
```

### Pattern 2: Multi-Dataset Benchmarking for Robust Evaluation
- Multiple datasets per task prevent overfitting to specific protocols
- Cross-dataset evaluation reveals true generalization ability
- Standardized preprocessing reduces methodological confounds

### Pattern 3: Domain-Specific vs. Generic Model Comparison
- Always compare against generic baselines (time-series FMs)
- Domain-specific advantage must justify additional complexity
- Beware of "domain specialization theater" — marginal gains aren't enough

## Related Skills

- eeg-foundation-model-adapters
- tta-eeg-foundation-models
- eeg-preprocessing-reliability
- eeg-foundation-lrp-interpretability
