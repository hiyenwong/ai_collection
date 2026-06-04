---
name: brain-of-omnifunctional-foundation-model
version: v1.0.0
last_updated: 2026-05-05
description: "Brain-OF: First omnifunctional brain foundation model jointly pretrained on fMRI, EEG and MEG. Uses Any-Resolution Neural Signal Sampler, DINT attention with Sparse MoE, and Masked Temporal-Frequency Modeling for dual-domain pretraining. Pretrained on ~40 datasets. Source: arXiv:2602.23410 (Guo et al., Feb 2026)."
---

# Brain-OF: Omnifunctional Brain Foundation Model

## Description

Brain-OF is the first omnifunctional brain foundation model jointly pretrained on fMRI, EEG and MEG, capable of handling both unimodal and multimodal inputs within a unified framework. It reconciles heterogeneous spatiotemporal resolutions using an Any-Resolution Neural Signal Sampler, manages semantic shifts with DINT attention and Sparse Mixture of Experts, and employs Masked Temporal-Frequency Modeling for dual-domain pretraining.

**Source Paper:** [arXiv:2602.23410](https://arxiv.org/abs/2602.23410) - "Brain-OF: An Omnifunctional Foundation Model for fMRI, EEG and MEG" (Hanning Guo, Farah Abdellatif, Hanwen Bi, Andrei Galbenus, Jon N. Shah, Abigail Morrison, Jurgen Dammers, Feb 26, 2026)

## Activation Keywords

- brain-OF
- omnifunctional brain foundation model
- multimodal brain foundation
- Any-Resolution Neural Signal Sampler
- DINT attention
- Masked Temporal-Frequency Modeling
- fMRI EEG MEG foundation model
- 脑基础模型
- 多模态脑信号
- 脑信号基础模型

## Core Architecture

### 1. Any-Resolution Neural Signal Sampler

Projects diverse brain signals (fMRI, EEG, MEG) with heterogeneous spatiotemporal resolutions into a shared semantic space. This is critical because:
- **fMRI**: High spatial resolution (~mm), low temporal resolution (~seconds)
- **EEG**: Low spatial resolution, high temporal resolution (~ms)
- **MEG**: Medium spatial resolution, high temporal resolution (~ms)

### 2. DINT Attention + Sparse Mixture of Experts (MoE)

- **DINT Attention**: Manages semantic shifts between modalities
- **Shared Experts**: Capture modality-invariant representations
- **Routed Experts**: Specialize in modality-specific semantics

### 3. Masked Temporal-Frequency Modeling (MTFM)

Dual-domain pretraining objective that jointly reconstructs brain signals in:
- **Time domain**: Temporal dynamics reconstruction
- **Frequency domain**: Spectral content reconstruction

## Implementation Workflow

### Step 1: Multi-Modal Data Preparation

```python
# Load brain signals from different modalities
fmri_data = load_fmri(subject_id)  # (n_regions, n_timepoints_fMRI)
eeg_data = load_eeg(subject_id)    # (n_channels, n_timepoints_EEG)
meg_data = load_meg(subject_id)    # (n_channels, n_timepoints_MEG)
```

### Step 2: Any-Resolution Sampling

```python
# Project all modalities to shared semantic space
shared_repr = any_resolution_sampler(
    fmri=fmri_data,
    eeg=eeg_data,
    meg=meg_data,
    target_resolution=common_resolution
)
```

### Step 3: Forward Pass through Brain-OF Backbone

```python
# DINT attention + Sparse MoE
output = brain_of_backbone(
    input=shared_repr,
    shared_experts=shared_weights,
    routed_experts=modality_specific_weights,
    routing_strategy=expert_selection(input)
)
```

### Step 4: Masked Temporal-Frequency Pretraining

```python
# Dual-domain reconstruction loss
time_loss = reconstruct_time_domain(masked_input, output)
freq_loss = reconstruct_frequency_domain(masked_input, output)
total_loss = time_loss + freq_loss
```

### Step 5: Downstream Task Fine-Tuning

```python
# Fine-tune on specific neuroscience tasks
model = BrainOF.from_pretrained("brain-of-base")
model.fine_tune(task="fmri_decoding", dataset=task_data)
# or
model.fine_tune(task="eeg_classification", dataset=task_data)
# or
model.fine_tune(task="multimodal_fusion", dataset=multi_data)
```

## Pretraining Corpus

- ~40 datasets across fMRI, EEG, and MEG modalities
- Large-scale multimodal brain signal collection
- Covers diverse neuroscience tasks and populations

## Advantages

1. **First Multimodal**: First foundation model to jointly handle fMRI, EEG, and MEG
2. **Resolution-Agnostic**: Handles heterogeneous spatiotemporal resolutions
3. **Dual-Domain**: Pretrains on both time and frequency domains
4. **Unified Framework**: Single model for unimodal and multimodal inputs
5. **Superior Performance**: Outperforms single-modality models across diverse tasks

## Applicable Tasks

- Brain signal decoding and classification
- Cross-modal prediction (e.g., EEG-to-fMRI synthesis)
- Multimodal brain-computer interfaces
- Neurological disorder detection
- Brain state prediction

## Resources

- Paper: https://arxiv.org/abs/2602.23410
- Related: Brain-DiT foundation models (existing skills)
- Related: EEG foundation model adapters

## Pitfalls

- Requires large multimodal datasets for effective pretraining
- Computational cost of joint pretraining is significant
- Modality imbalance may require careful sampling strategies
- Sparse MoE routing needs sufficient data to learn expert specialization