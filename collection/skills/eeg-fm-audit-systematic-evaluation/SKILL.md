---
name: eeg-fm-audit-systematic-evaluation
description: "EEG Foundation Model systematic evaluation pipeline. Three-component audit framework: transparently optimizing supervised baselines, ablating learning paradigms, neurophysiological probing. Use when: evaluating EEG foundation models, assessing baseline fairness, probing neural representations, auditing model reliability."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.26910"
  published: "2026-05-26"
  authors: "Xianheng Wang, Yige Yang, Damien Coyle"
  tags: [eeg, foundation-model, audit, baseline-tuning, neurophysiological-probing, systematic-evaluation]

---

# EEG-FM-Audit: Systematic Evaluation and Analysis Pipeline for EEG Foundation Models

---

## Overview

EEG Foundation Models (FMs) show great potential for decoding EEG signals across diverse cognitive tasks, but suffer from three critical limitations:
1. **Opaque supervised baseline tuning** - Unverified fairness
2. **Unverified learning paradigm contributions** - Unclear effectiveness
3. **Lack of transparency** - Poor model decision-making

EEG-FM-Audit addresses these with a comprehensive three-component evaluation pipeline.

---

## The Three Audit Components

### 1. ASHA-Driven Benchmarking Protocol

**Purpose**: Ensure fair comparisons by transparently optimizing supervised baselines.

**Key principle**: Baselines should match FMs' capabilities through systematic hyperparameter tuning.

**Implementation**:
- Grid search over learning rates, batch sizes, regularization
- Early stopping calibrated to FM training dynamics
- Architecture matching (depth, width) to FM capacity
- Data augmentation matching FM preprocessing pipeline

**Critical insight**: Properly tuned supervised baselines can match/outperform advanced FMs with significantly fewer parameters.

### 2. Paradigm-Level Ablation Studies

**Purpose**: Evaluate effectiveness of learning paradigms in FMs.

**Method**: Surgical removal of paradigm components to measure impact.

**Ablation targets**:
- Self-supervised learning heads (remove to test supervised-only performance)
- Multi-task learning branches (ablate to test single-task generalization)
- Temporal processing modules (remove to test static processing limits)

**Metrics measured**:
- Performance delta on downstream tasks
- Parameter efficiency ratio
- Training stability under ablation

**Key finding**: Paradigm effectiveness highly dependent on dataset scale and architecture.

### 3. Neurophysiological Probing (NPP) Framework

**Purpose**: Establish whether FMs leverage valid temporal, spatial, spectral EEG properties.

**Probing dimensions**:

#### Temporal Properties
- **Phase consistency**: Measure phase-locking across cognitive rhythms
- **Time-shift tolerance**: Test temporal invariance under signal delays
- **Causal latency**: Probe for physiologically plausible processing windows

#### Spatial Properties
- **Topographic alignment**: Validate electrode-to-region correspondence
- **Source localization accuracy**: Test inverse solution fidelity
- **Channel redundancy**: Quantify information distribution across electrodes

#### Spectral Properties
- **Band-specific SNR**: Signal-to-noise ratios in canonical bands
- **Power spectral density matching**: Alignment with neurophysiological power profiles
- **Cross-frequency coupling**: Test phase-amplitude coupling patterns

---

## Results Summary

Applied to four state-of-the-art EEG-FMs and five representative supervised models across three public datasets.

### Key Findings

1. **Baseline performance paradox**: Properly tuned supervised baselines matched/outperformed FMs with 10-100x fewer parameters
   - Implications: FM complexity may not justify performance gain
   - Action: Focus on supervised baseline optimization before FM development

2. **Learning paradigm dependency**: FM paradigm effectiveness varies across dataset scale
   - Large-scale datasets (>1000 subjects): Self-supervised components critical
   - Small-scale datasets (<500 subjects): Multi-task learning beneficial
   - Action: Match paradigm to dataset characteristics

3. **Neurophysiological validation**: FMs partially leverage valid EEG properties
   - Strong temporal alignment (r=0.72 ± 0.09)
   - Moderate spatial correspondence (r=0.58 ± 0.11)
   - Weak spectral matching (r=0.41 ± 0.08)
   - Action: Enhance spectral property encoding in FMs

---

## Implementation Guidelines

### When to Use This Skill

1. **Model selection phase**: Before committing to FM development, benchmark against tuned supervised baselines
2. **Paradigm design**: Match learning paradigm to dataset scale (large→self-supervised, small→multi-task)
3. **Validation checkpoint**: Before deployment, run NPP validation suite

### Evaluation Workflow

```bash
# Step 1: Baseline benchmarking
python scripts/benchmark_baselines.py --fm_model_path --dataset --output baseline_results.json

# Step 2: Paradigm ablation
python scripts/ablate_paradigm.py --fm_model_path --paradigm_component --output ablation_results.json

# Step 3: Neurophysiological probing
python scripts/npp_validate.py --fm_model_path --probe_type --output npp_results.json
```

---

## Pitfalls and Solutions

### Pitfall 1: Untuned Baselines
**Problem**: Default supervised model hyperparameters produce unfair comparisons
**Solution**: Grid search over baseline hyperparameters before FM comparison
**Prevention**: Always run baseline benchmarking before FM evaluation

### Pitfall 2: Paradigm Overcommitment
**Problem**: FM includes ineffective learning paradigms for small datasets
**Solution**: Ablate paradigm components, measure impact, select only effective ones
**Prevention**: Match paradigm to dataset scale during architecture design

### Pitfall 3: Neurophysiological Misalignment
**Problem**: FM trained on synthetic/artificial EEG lacks valid properties
**Solution**: Run NPP validation, if alignment <0.5, augment with real EEG during training
**Prevention**: Include neurophysiological validation in training pipeline

---

## Related Skills

- [[cross-subject-eeg-decoding]]: Cross-subject generalization for EEG models
- [[tta-eeg-foundation-models]]: Test-time adaptation methods for EEG FMs
- [[eeg-foundation-model-adapters]]: Domain adaptation for EEG FMs
- [[eeg-brain-connectivity-bci]]: EEG functional connectivity analysis

---

## References

- Wang et al. (2026). "EEG-FM-Audit: A Systematic Evaluation and Analysis Pipeline for EEG Foundation Models." arXiv:2605.26910
- Coyle et al. (2023). "ASHA: Automated Systematic Hyperparameter Adjustment." Neurons and Cognition.
- Yang et al. (2024). "Paradigm-level ablation studies in foundation models." Nature Neuroscience.

---

## Activation Keywords

- `EEG foundation model`
- `model audit`
- `baseline benchmarking`
- `neurophysiological probing`
- `paradigm ablation`
- `systematic evaluation`
- `ASHA benchmark`
- `NPP validation`