---
name: tribev2-brain-foundation-model
description: "TRIBE v2: A tri-modal (video, audio, language) foundation model for predicting human brain activity. Use when: building brain encoding models, fMRI prediction, in-silico neuroscience experiments, multimodal brain modeling, analyzing naturalistic fMRI data, or implementing the Algonauts 2025 winning architecture."
---

# TRIBE v2: Tri-Modal Brain Foundation Model

A unified foundation model for predicting human brain activity from video, audio, and language stimuli. Developed by FAIR at Meta and ENS-PSL, this model achieved first place in the Algonauts 2025 challenge.

## arXiv Reference

- **Paper**: "A foundation model of vision, audition, and language for in-silico neuroscience"
- **arXiv ID**: 2605.04326
- **Date**: May 5, 2026
- **Authors**: Stéphane d'Ascoli, Jérémy Rapin, et al. (FAIR at Meta, ENS-PSL)
- **Code**: https://github.com/facebookresearch/tribev2
- **Weights**: https://huggingface.co/facebook/tribev2
- **Demo**: https://aidemos.atmeta.com/tribev2

## Problem Statement

Cognitive neuroscience is fragmented into specialized models, each tailored to specific experimental paradigms. TRIBE v2 addresses this by providing a **unified tri-modal foundation model** that can predict brain responses across diverse naturalistic and experimental conditions.

## Core Architecture

### Transformer Encoder
- Deep transformer architecture that integrates tri-modal features
- Maps pretrained embeddings to high-resolution fMRI responses
- Handles both cortical and subcortical predictions

### Modality Dropout
- Randomly drops video, audio, or language modalities during training
- Forces the model to learn robust cross-modal representations
- Enables predictions even with incomplete stimulus information

### Subject Block
- Learnable subject-specific embeddings
- Captures individual variability in brain responses
- Enables zero-shot generalization to unseen subjects via subject embedding interpolation

## Feature Extraction Pipeline

### Text Embeddings
- Pretrained language model embeddings for textual stimuli
- Captures semantic and syntactic features relevant to neuro-linguistic processing

### Audio Embeddings
- Pretrained audio model for acoustic feature extraction
- Captures temporal dynamics of sound processing in auditory cortex

### Video Embeddings
- Pretrained vision model for visual feature extraction
- Captures spatiotemporal dynamics of visual processing

### Combining Modalities
- Concatenates tri-modal embeddings
- Applies modality dropout for robustness
- Feeds unified representation to transformer encoder

## Training Setup

### Datasets (1,000+ hours fMRI, 720 subjects)
1. **Courtois NeuroMod** - Naturalistic multimodal stimuli (Algonauts 2025)
2. **Lebel2023** - Podcast listening (audio-only)
3. **BoldMoments** - Video watching
4. **Wen2017** - Video stimuli
5. **Naturalistic NeuroImaging Database** - Various naturalistic paradigms
6. **Human Connectome Project** - Resting-state and task fMRI

### fMRI Preprocessing
- Cortical and subcortical extraction
- Rescaling and detrending
- Resampling to common space
- Hemodynamic lag correction

### Training Protocol
- Stochastic gradient descent optimization
- Log-linear scaling with data volume (no plateau observed)
- Significantly outperforms Deep FIR baseline (q(FDR) < 10^-4)

## Key Results

### Performance
- Accurate predictions across most of cortex for naturalistic stimuli
- Peak correlations in modality-specific regions (temporal for audio, visual for video)
- Subcortical predictions lower by 2-3x but still significant
- Several-fold improvement over traditional linear encoding models

### Generalization
- Zero-shot generalization to novel stimuli, tasks, and subjects
- Unseen subject prediction via subject embedding interpolation
- Fine-tuning further improves individual brain modeling

### In-Silico Experimentation
- Recovers results from decades of empirical research
- Validated on seminal visual and neuro-linguistic paradigms
- Enables hypothesis testing without new data collection

### Interpretability
- Extracts interpretable latent features
- Reveals fine-grained topography of multisensory integration
- Provides mechanistic toolkit for cognitive function decomposition

## Usage Patterns

### Pattern 1: Brain Activity Prediction
```python
# Predict brain responses to novel stimuli
from tribev2 import TRIBEv2

model = TRIBEv2.from_pretrained("facebook/tribev2")
predictions = model.predict(video=video_data, audio=audio_data, text=text_data)
```

### Pattern 2: In-Silico Experimentation
```python
# Test hypotheses about brain organization
# Without collecting new fMRI data
responses = model.simulate_stimulus(stimulus_type="visual", parameters={...})
```

### Pattern 3: Cross-Subject Generalization
```python
# Predict for unseen subjects
unseen_predictions = model.predict_unseen_subject(
    video=video_data,
    subject_embedding=interpolated_embedding
)
```

## Activation Keywords
- TRIBE v2, tribev2, brain foundation model, fMRI encoding, brain prediction, in-silico neuroscience, multimodal brain modeling, Algonauts challenge, naturalistic fMRI, brain activity prediction

## Related Skills
- `brain-dit-fmri-foundation-model` - Brain-DiT fMRI foundation model
- `brain-foundation-model-inversion` - Brain foundation model inversion
- `eeg-foundation-model-adapters` - EEG foundation models with domain adaptation
- `multimodal-brain-connectivity-gnn` - Multimodal brain connectivity analysis

## Pitfalls
1. **Data Scale**: Requires large-scale fMRI datasets (1000+ hours) for training from scratch
2. **Computational Cost**: Transformer architecture requires significant GPU resources
3. **Subject Variability**: Zero-shot subject prediction quality depends on training subject diversity
4. **Modality Balance**: Performance varies with modality availability; modality dropout helps but doesn't fully compensate

## Verification Steps
1. Compare predictions against held-out fMRI data using Pearson correlation
2. Validate against Deep FIR baseline to ensure architectural advantage
3. Test zero-shot generalization on held-out subjects
4. Run in-silico experiments against known empirical results
