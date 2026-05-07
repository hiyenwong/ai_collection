---
name: tribe-v2-foundation-model
description: >
  TRIBE v2 tri-modal foundation model methodology for in-silico neuroscience.
  Video+audio+language foundation model predicting human fMRI responses across
  diverse conditions. Trained on 1,000+ hours fMRI / 720 subjects. Enables
  zero-shot brain activity prediction, in-silico hypothesis testing, and
  multisensory integration analysis. Use when: TRIBE, brain foundation model,
  fMRI encoding model, in-silico neuroscience, multi-modal brain prediction,
  neural encoding, functional MRI prediction, Meta AI neuroscience, Algonauts,
  tri-modal brain model, naturalistic fMRI, brain response prediction.
---

# TRIBE v2: Tri-Modal Foundation Model for In-Silico Neuroscience

d'Ascoli et al., Meta FAIR, arXiv:2605.04326 (May 2026)

## Core Architecture

TRIBE v2 maps pretrained AI embeddings to high-resolution fMRI via a transformer-based encoder:

```
Stimulus (video/audio/text)
    → Pretrained embeddings (DINOv2/vision, Whisper/audio, LLM/text)
    → TRIBE v2 Transformer Encoder
    → High-resolution fMRI prediction (cortical + subcortical)
```

### Key Design Decisions
- **Tri-modal integration**: video + audio + text embeddings fused in single architecture
- **Transformer-based**: deep nonlinear integration outperforms linear FIR baselines by 2-4x
- **High-resolution fMRI**: predicts cortical vertices and subcortical regions
- **Unified dataset**: 1,000+ hours fMRI, 720 subjects, 5,094 sessions across 8 datasets

## Datasets Used

| Dataset | Mode | Modalities | Subjects | fMRI (h) |
|---------|------|------------|----------|----------|
| CNeuroMod | Train | A+V+T | 4 | 268.7 |
| BoldMoments | Train | A+V | 10 | 61.9 |
| Lebel2023 | Train | A+T | 8 | 85.8 |
| Wen2017 | Train | V | 3 | 35.2 |
| NNDb | Test | A+V+T | 86 | 160.6 |
| LPP | Test | A+T | 112 | 180.2 |
| Narratives | Test | A+T | 321 | 146.6 |
| HCP (7T) | Test | A+V+T | 176 | 178.7 |

## Performance Characteristics

1. **Encoding accuracy**: Log-linear scaling with data volume, no plateau observed
2. **Zero-shot generalization**: Predicts group-averaged responses better than individual subjects (R_group ≈ 0.4 on HCP 7T)
3. **Fine-tuning**: 1 epoch on ≤1h per-subject data yields 2-4x improvement over linear encoder from scratch
4. **Subcortical**: Predictions 2-3x lower than cortical but still significant

## In-Silico Experimentation

TRIBE v2 recovers classic neuroscience findings without retraining:

### Visual Localizers (IBC dataset)
- Fusiform Face Area (FFA) for faces
- Parahippocampal Place Area (PPA) for places
- Extrastriate Body Area (EBA) for bodies
- Visual Word-Form Area (VWFA) for characters
- Hemodynamic delay: peaks ~5s post-stimulus

### Language Localizers
- Speech vs non-speech → associative auditory cortices (A5), STS, Broca's area (45)
- Emotional vs physical pain → TPJ, MTG
- Sentences vs word lists → left hemisphere lateralization
- Complex vs simple sentences → syntactic regions (Broca)

## Interpretability

ICA on final layer reveals 5 components matching known functional networks:
1. Primary auditory cortex
2. Language network
3. Motion detection area (V5/MT)
4. Default Mode Network (DMN)
5. Visual system

## Multisensory Integration

- **Text** dominates: prefrontal cortex, language areas
- **Audio** dominates: temporal/auditory cortices
- **Video** dominates: occipital, parietal cortices
- **Largest multimodal gains**: temporal-parietal-occipital junction (up to 50% improvement)
- **Video+Audio (cyan)**: ventral/dorsal visual cortices, hippocampus
- **Text+Audio (yellow)**: superior temporal lobe, ventricles

## Usage

```python
# Load from HuggingFace
from transformers import AutoModel
model = AutoModel.from_pretrained("facebook/tribev2")

# Predict brain response to stimuli
# Input: video frames, audio waveform, text
# Output: fMRI time-series prediction (cortical vertices + subcortical)
```

- **Code**: https://github.com/facebookresearch/tribev2
- **Weights**: https://huggingface.co/facebook/tribev2
- **Demo**: https://aidemos.atmeta.com/tribev2

## Application Patterns

### 1. Brain Response Prediction
Feed any video/audio/text stimulus → predict fMRI response pattern across cortex.

### 2. In-Silico Hypothesis Testing
Run controlled experiments (flash stimuli, contrasts) without recruiting subjects.

### 3. Subject-Specific Modeling
Fine-tune on ≤1h per-subject data for individualized predictions.

### 4. Multisensory Integration Mapping
Analyze how different modalities contribute to encoding in different brain regions.

## Related Work

- TRIBE v1: Won Algonauts 2025 competition (1st/263 teams)
- Traditional linear encoding models: FIR (Dale, 1999) — outperformed 2-4x
- Unimodal brain encoding: vision (Yamins 2014), language (Huth 2016), audio (Kell 2018)

## Limitations

- fMRI only (no EEG/MEG temporal resolution)
- 3T fMRI primarily (limited 7T training data)
- Subcortical predictions lower than cortical
- Requires pretrained AI embeddings as input
