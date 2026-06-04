---
name: tribe-v2-foundation-model
category: ai_collection
description: TRIBE v2 tri-modal foundation model methodology for in-silico neuroscience. Uses video/audio/language embeddings to predict whole-brain fMRI across 720 subjects.
created: 2026-05-09
updated: 2026-05-09
source: arXiv 2605.04326
---

# TRIBE v2: Tri-Modal Foundation Model for In-Silico Neuroscience

## Overview
TRIBE v2 is a foundation model that predicts high-resolution fMRI brain activity from video, audio, and text stimuli. Built on a unified dataset of 1000+ hours of fMRI across 720 subjects, it enables zero-shot generalization to novel stimuli, tasks, and subjects.

**arXiv**: 2605.04326 (May 2026)
**Authors**: d'Ascoli, Rapin, Benchetrit, Brooks, Begany, Raugel, Banville, King (FAIR at Meta)
**Code**: https://github.com/facebookresearch/tribev2
**Weights**: https://huggingface.co/facebook/tribev2

## Core Methodology

### Architecture
- **Transformer encoder** with modality dropout and subject-specific blocks
- **Tri-modal input**: video (ImageBind/Vision), audio (Wav2Vec), language (LLaMA) embeddings
- **Unseen subject prediction**: learns population-level priors for zero-shot subject generalization

### Training Pipeline
1. **Feature Extraction**: Pre-trained AI models extract embeddings per modality
2. **Modality Dropout**: Randomly drop modalities during training for robustness
3. **Subject Blocks**: Per-subject linear adapters capture individual variability
4. **High-Resolution fMRI**: Predicts at vertex-level resolution (not just ROI averages)

### Four Essential Criteria
1. **Integration**: Whole-brain responses across diverse experimental conditions
2. **Performance**: Exceeds traditional linear encoding models
3. **Generalization**: Zero-shot to novel stimuli, tasks, and subjects
4. **Interpretability**: Decomposes cognitive function organization

## Key Findings

### Encoding Performance
- Accurately predicts cortical AND subcortical responses across naturalistic and experimental conditions
- Several-fold improvements over classic linear baselines
- Scaling laws: performance increases with more training hours per subject

### Zero-Shot Generalization
- Generalizes to new subjects without fine-tuning
- Generalizes to new tasks/paradigms not seen during training
- Fine-tuning on half a subject's data significantly improves individualized predictions

### In-Silico Experiments
- **Visual**: Recovers face/body selectivity (FFA, EBA), object-selective cortex findings
- **Language**: Recovers sentence > word, social > non-social, emotional > neutral contrasts
- Agreement between predicted and actual z-scores across 360 HCP parcels

### Interpretability (ICA)
- Independent Component Analysis reveals neuroscientifically relevant patterns
- Components correlate with known functional networks (visual, language, default mode, etc.)

### Multimodal Integration
- Text-only, audio-only, video-only ablations reveal modality-specific regions
- Bimodal/multimodal integration areas identified via RGB cortical mapping
- Reveals fine-grained topography of multisensory integration

## Dataset Scale
| Dataset | Mode | Subjects | fMRI (h) | Purpose |
|---------|------|----------|----------|---------|
| CNeuroMod | A+V+T | 4 | 268.7 | Train (deep) |
| BoldMoments | A+V | 10 | 61.9 | Train |
| Lebel2023 | A+T | 8 | 85.8 | Train |
| Wen2017 | V | 3 | 35.2 | Train |
| NNDb | A+V+T | 86 | 160.6 | Test (wide) |
| LPP | A+T | 112 | 180.2 | Test |
| Narratives | A+T | 321 | 146.6 | Test |
| HCP | A+V+T | 176 | 178.7 | Test (7T) |

**Total**: 720 subjects, 5094 sessions, 1117.7 hours fMRI

## Application Triggers
Use this skill when:
- Building brain encoding/decoding models
- Designing in-silico neuroscience experiments
- Working with fMRI prediction tasks
- Studying multimodal brain integration
- Analyzing zero-shot brain response generalization
- Comparing foundation models to linear baselines

## Key Concepts
- Foundation model for neuroscience
- Tri-modal (video/audio/text) brain encoding
- In-silico hypothesis testing
- Zero-shot subject generalization
- Fine-grained cortical parcellation (HCP-MMP1)
- Independent Component Analysis (ICA) for interpretability
- Modality dropout for robustness
- Scaling laws in brain encoding

## Limitations
- fMRI temporal resolution limits (slow hemodynamic response)
- Primarily trained on healthy adult subjects
- In-silico experiments approximate but don't replace empirical validation
- 3T vs 7T resolution differences across datasets

## Related Skills
- `brain-dit-fmri-foundation-model-v6`
- `meta-learning-in-context-brain-decoding-v5`
- `multimodal-brain-connectivity-gnn`
- `geometric-brain-dynamics-mapping-v7`
