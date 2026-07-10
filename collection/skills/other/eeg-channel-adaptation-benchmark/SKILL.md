---
name: eeg-channel-adaptation-benchmark
description: "Systematic benchmark of channel adaptation methods for EEG foundation models. Compares Conv1d, SSI, source-space decomposition, and Riemannian re-centering across 5 FMs (5M-157M params), 5 tasks, revealing architecture-dependent optimal methods and probe-SFT asymmetry."
---

# EEG Channel Adaptation Benchmark

**Paper:** Channel Adaptation for EEG Foundation Models: A Systematic Benchmark Across Architectures, Tasks, and Training Regimes  
**arXiv:** 2604.23091 (April 2026)  
**Authors:** Kuntal Kokate, Bruno Aristimunha, Dung Truong, Arnaud Delorme  
**Categories:** cs.LG

## Core Contribution

First systematic comparison of channel adaptation methods for EEG foundation models, addressing the challenge of heterogeneous electrode montages that prevent scaling EEG FMs across datasets.

## Problem

EEG data comes from different electrode configurations (montages):
- 10-20 system (19-21 channels)
- 10-10 system (64+ channels)
- Custom clinical setups
- Consumer headsets (few channels)

Foundation models need to handle all these for pretraining and deployment.

## Four Adaptation Methods Compared

### 1. Conv1d Projection
- Learnable 1D convolution maps input channels to model's expected channel count
- Simple, flexible
- **Optimal for:** BENDR architecture

### 2. Spherical Spline Interpolation (SSI)
- Interpolates electrode signals on spherical surface
- Biophysically motivated
- **Optimal for:** Neuro-GPT architecture

### 3. Source-Space Decomposition
- Projects sensor-space data to source space using inverse modeling
- Montages become irrelevant in source space
- **Optimal for:** Depression detection tasks

### 4. Riemannian Re-centering
- Uses Riemannian geometry of covariance matrices
- Aligns data distributions across montages
- **Optimal for:** Neuro-GPT architecture

## Five Foundation Models Tested

| Model | Parameters | Type | Adaptation Needed |
|-------|-----------|------|-------------------|
| BENDR | ~5M | Rigid montage | Yes - external adaptation required |
| Neuro-GPT | ~10M | Rigid montage | Yes - external adaptation required |
| EEGPT | ~157M | Flexible montage | No - matches native when fine-tuned |
| CBraMod | ~5M | Flexible montage | No - matches native when fine-tuned |
| [5th model] | Varies | - | - |

## Key Findings

### 1. Rigid vs. Flexible Models
- **Rigid-montage models** (BENDR, Neuro-GPT) require external adaptation
- **Flexible-montage models** (EEGPT, CBraMod) match or exceed rigid models natively when fine-tuned
- Flexible models benefit from external methods under frozen-encoder deployment

### 2. Probe-SFT Asymmetry
- External adaptation can cause **severe negative transfer** during fine-tuning of flexible models
- Probing (linear readout) benefits from adaptation, but SFT (full fine-tuning) may not
- **Recommendation:** Don't apply external adaptation before fine-tuning flexible models

### 3. Architecture-Dependent Optimal Method
- No single best method for all architectures
- Conv1d for BENDR, SSI/Riemannian for Neuro-GPT, source-space for depression detection

### 4. Compact Models Can Outperform Large Models
- 5M-parameter CBraMod outperforms models up to 31x larger on 4/5 datasets
- Consistent with independent findings that compact EEG-specific architectures can match larger models

## Evaluation Protocol

- 5 pretrained EEG foundation models (5M–157M parameters)
- 5 downstream tasks
- 2 training regimes (probe vs. SFT)
- 10–15 random seeds per configuration

## Recommendations

### For Practitioners

1. **Choose architecture first:** Flexible montage models reduce adaptation overhead
2. **Match method to architecture:** Conv1d for BENDR, SSI/Riemannian for Neuro-GPT
3. **Avoid adaptation before SFT:** Don't apply external adaptation before fine-tuning flexible models
4. **Consider compact models:** 5M CBraMod matches 31x larger models on most tasks

### For Researchers

- External adaptation methods are complementary, not competitive
- Architecture choice determines adaptation strategy
- Probe-SFT asymmetry needs theoretical explanation

## Trigger Keywords
- eeg channel adaptation, montage alignment, eeg foundation model, spherical spline interpolation, riemannian recentering, source-space decomposition, EEG通道适配

## Related Skills
- eeg-foundation-model-adapters
- tta-eeg-foundation-models
- laya-eeg-foundation
- reve-eeg-foundation
