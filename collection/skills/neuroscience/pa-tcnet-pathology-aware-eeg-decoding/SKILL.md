---
name: pa-tcnet-pathology-aware-eeg-decoding
description: "PA-TCNet: Pathology-Aware Temporal Calibration with Physiology-Guided Target Refinement for Cross-Subject Motor Imagery EEG Decoding in Stroke Patients - arXiv:2604.16554 (April 2026). Covers cross-subject EEG decoding, pathology-aware temporal calibration for lesion-related abnormal dynamics, physiology-guided pseudo-label refinement, and stroke patient motor imagery BCI adaptation."
---

# PA-TCNet: Pathology-Aware Temporal Calibration with Physiology-Guided Target Refinement for Cross-Subject Motor Imagery EEG Decoding in Stroke Patients

**arXiv:** [2604.16554](https://arxiv.org/abs/2604.16554)
**Date:** April 2026
**Authors:** Xiangkai Wang, Yun Zhao, Dongyi He, Qingling Xia, Gen Li, Nizhuan Wang, Ningxiao Peng, Bin Jiang
**Categories:** cs.HC, q-bio.NC
**Code:** [github.com/wxk1224/PA-TCNet](https://github.com/wxk1224/PA-TCNet)

## Core Thesis

Stroke patient cross-subject EEG decoding for motor imagery (MI) brain-computer interfaces (BCI) is essential for motor rehabilitation, but is undermined by **lesion-related abnormal temporal dynamics** and **pronounced inter-patient heterogeneity**. PA-TCNet addresses this by jointly modeling pathological temporal dynamics and physiology-constrained pseudo-supervision, providing more robust cross-subject initialization for personalized post-stroke MI-BCI rehabilitation.

## Problem Statement

| Challenge | Description |
|-----------|-------------|
| **Abnormal temporal dynamics** | Brain lesions from stroke create pathological slow-wave activity that disrupts normal EEG temporal patterns |
| **Inter-patient heterogeneity** | Stroke patients exhibit highly variable EEG signatures due to different lesion locations and severities |
| **Misleading adaptation** | Existing domain adaptation methods are easily misled by pathological slow-wave activity |
| **Unstable pseudo-labels** | Target-domain pseudo-labels are unreliable when pathology distorts signal distributions |
| **Cross-subject generalization** | Standard transfer learning fails due to the unique pathological signature per patient |

## Architecture: PA-TCNet

PA-TCNet consists of two main modules working jointly:

### Module 1: Pathology-Aware Temporal Calibration (PA-TC)

Addresses the challenge of **lesion-induced temporal distortions** in EEG:

- **Temporal dynamics modeling**: Captures both normal motor-related and pathological temporal patterns in EEG
- **Pathology-aware calibration**: Explicitly accounts for stroke-lesion effects on signal timing and morphology
- **Key insight**: Lesion-related abnormal slow-wave activity must be **modeled rather than filtered**, as it carries information about the patient's neurological state
- **Temporal alignment**: Calibrates temporal features across source (healthy/control) and target (stroke patient) domains while being aware of pathological distortions

#### Design Principles

- Recognizes that stroke patients have **delayed and distorted** motor imagery temporal patterns
- Adapts temporal feature extraction to handle **heterogeneous latencies**
- Prevents pathological activity from contaminating discriminative features while preserving clinically relevant information

### Module 2: Physiology-Guided Target Refinement (PG-TR)

Addresses the challenge of **unreliable pseudo-labels** in target domain:

- **Physiology-constrained pseudo-supervision**: Uses neurophysiological priors to guide and refine pseudo-labels for target-domain (stroke patient) data
- **Target refinement**: Iteratively improves the quality of pseudo-labels by incorporating physiological constraints
- **Key insight**: Rather than trusting noisy classifier predictions, physiology-guided constraints (e.g., expected frequency band patterns for motor imagery) anchor the pseudo-label generation
- **Robust cross-subject initialization**: Produces reliable initial models that can be personalized for individual stroke patients

#### Design Principles

- Motor imagery EEG has known **physiological markers** (mu/beta band desynchronization, ERD/ERS patterns)
- These markers persist even in stroke patients, though with altered characteristics
- Using these priors constrains the pseudo-label space to physiologically plausible solutions

## Methodology Details

### Overall Pipeline

```
Source Domain EEG          Target Domain EEG (Stroke Patient)
(Healthy/Control)          (New Patient — Unlabeled)
        ↓                           ↓
  [Feature Extraction]       [Feature Extraction]
        ↓                           ↓
  [Pathology-Aware Temporal Calibration Module]
        ↓                           ↓
  [Aligned Temporal Features]  [Calibrated Features]
        ↓                           ↓
  [Physiology-Guided Target Refinement Module]
                    ↓
         [Refined Pseudo-Labels for Target]
                    ↓
          [Cross-Subject MI Classifier]
                    ↓
         Motor Imagery Prediction
```

### Cross-Subject Decoding Strategy

1. **Source domain training**: Train initial model on labeled EEG from control subjects or diverse stroke patients
2. **Temporal calibration**: Apply PA-TC module to align temporal dynamics between source and target (new stroke patient)
3. **Pseudo-label generation**: Generate initial pseudo-labels for unlabeled target patient data
4. **Physiology-guided refinement**: PG-TR module refines pseudo-labels using neurophysiological constraints
5. **Iterative adaptation**: Alternate between refinement and feature alignment for optimal transfer

### Stroke Patient Adaptation

- Handles **lesion-specific** temporal abnormalities
- Adapts to **varying severity** levels across patients
- Accounts for **different lesion locations** (cortical vs. subcortical)
- Robust to **delayed or absent** motor imagery responses common in severe stroke

## Key Contributions

1. **Pathology-aware temporal calibration** — First explicit modeling of stroke-lesion temporal dynamics for cross-subject EEG adaptation
2. **Physiology-guided target refinement** — Neurophysiological priors constrain pseudo-label generation, preventing pathological activity from degrading adaptation
3. **Joint optimization** — Temporal calibration and target refinement are optimized jointly for robust cross-subject transfer
4. **Clinical applicability** — Designed specifically for post-stroke MI-BCI rehabilitation, not just healthy-subject transfer
5. **Open-source implementation** — Code available at [github.com/wxk1224/PA-TCNet](https://github.com/wxk1224/PA-TCNet)

## Technical Details

### Signal Processing
- Input: Multi-channel EEG recordings from stroke patients during motor imagery tasks
- Temporal features capture both event-related dynamics and ongoing pathological activity
- Frequency band analysis includes delta (pathological), theta, alpha/mu, beta (motor imagery relevant)

### Domain Adaptation
- Source domain: Labeled EEG from multiple subjects (healthy or stroke)
- Target domain: Unlabeled EEG from new stroke patient
- Adaptation leverages both statistical alignment and physiological constraints

### Performance Claims
- Jointly modeling pathological temporal dynamics and physiology-constrained pseudo-supervision provides more robust cross-subject initialization
- Outperforms standard domain adaptation methods on stroke patient EEG data
- Enables personalized post-stroke MI-BCI rehabilitation with reduced calibration time

## Applications

- Post-stroke motor rehabilitation via BCI
- Personalized MI-BCI systems for stroke patients
- Plug-and-play EEG decoding (minimal calibration for new patients)
- Clinical neurorehabilitation monitoring
- Adaptive BCI systems for progressive recovery tracking

## Related Work Context

- Extends cross-subject EEG decoding (typically focused on healthy subjects) to pathological populations
- Complementary to standard domain adaptation methods (DANN, MDD, etc.) with pathology-specific innovations
- Addresses a gap where most MI-BCI research uses healthy-subject data, ignoring stroke-specific challenges

## Citations

```bibtex
@article{wang2026patcnet,
  title={PA-TCNet: Pathology-Aware Temporal Calibration with Physiology-Guided Target Refinement for Cross-Subject Motor Imagery EEG Decoding in Stroke Patients},
  author={Wang, Xiangkai and Zhao, Yun and He, Dongyi and Xia, Qingling and Li, Gen and Wang, Nizhuan and Peng, Ningxiao and Jiang, Bin},
  journal={arXiv preprint arXiv:2604.16554},
  year={2026}
}
```
