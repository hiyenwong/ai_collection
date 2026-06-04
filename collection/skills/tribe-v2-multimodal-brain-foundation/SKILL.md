---
name: tribe-v2-multimodal-brain-foundation
description: "TRIBE v2 tri-modal foundation model methodology for in-silico neuroscience. Uses video, audio, and language inputs to predict brain activity across diverse experimental conditions. Trained on 1000+ hours of fMRI across 720 subjects. Enables in-silico experimentation and replaces traditional linear encoding models. Activation: TRIBE, tri-modal foundation model, in-silico neuroscience, multimodal brain prediction, video-audio-language fMRI, brain encoding model, naturalistic fMRI, multimodal neural prediction."
---

# TRIBE v2: Tri-Modal Foundation Model for In-Silico Neuroscience

> A unified vision-audio-language foundation model that predicts human brain activity across naturalistic and experimental conditions, enabling in-silico neuroscience experiments.

## Metadata
- **Source**: arXiv:2605.04326
- **Authors**: Stephane d'Ascoli, Jeremy Rapin, Yohann Benchetrit, Teon Brooks, Katelyn Begany, Josephine Raugel, Hubert Banville, Jean-Remi King
- **Published**: 2026-05-05
- **Categories**: q-bio.NC, cs.LG

## Core Methodology

### Key Innovation
TRIBE v2 is a tri-modal (video, audio, language) foundation model trained on a unified dataset of over 1,000 hours of fMRI across 720 subjects. It supersedes traditional linear encoding models, delivering several-fold improvements in prediction accuracy for brain responses to novel stimuli, tasks, and subjects.

### Technical Framework

1. **Multi-modal input processing**: Three parallel encoders process video, audio, and text streams into unified representations
2. **Brain response prediction**: The model maps multimodal features to voxel-wise fMRI responses across diverse brain regions
3. **Cross-subject generalization**: Training across 720 subjects enables zero-shot prediction on new participants
4. **In-silico experimentation**: The model can simulate brain responses to experimental paradigms without collecting new fMRI data

### Architecture Components

- **Visual encoder**: Processes video frames into spatiotemporal representations
- **Audio encoder**: Extracts auditory features from sound streams
- **Language encoder**: Processes textual/linguistic information
- **Brain mapping head**: Maps multimodal features to brain activity patterns
- **Subject adaptation**: Handles inter-subject variability through learned alignment

### Validation Results

- Accurately predicts high-resolution brain responses for novel stimuli, tasks, and subjects
- Recovers established findings from seminal visual and neuro-linguistic paradigms
- Reveals fine-grained topography of multisensory integration through interpretable latent features

## Implementation Guide

### Prerequisites
- Large-scale fMRI dataset (1000+ hours, 720+ subjects)
- Multi-modal pre-trained encoders (vision, audio, language)
- GPU cluster for training foundation model

### Step-by-Step

1. **Data curation**: Aggregate fMRI datasets across multiple studies with varied stimuli
2. **Stimulus annotation**: Encode all stimuli in three modalities (video frames, audio waveform, text transcript)
3. **Model training**: Train tri-modal encoder with brain prediction head on unified dataset
4. **Cross-validation**: Test on held-out subjects, stimuli, and experimental paradigms
5. **In-silico experiments**: Apply model to simulate brain responses to new experimental designs
6. **Feature interpretation**: Extract latent features to map multisensory integration topography

## Applications
- **In-silico neuroscience**: Simulate brain responses to novel experimental paradigms without data collection
- **Cross-modal analysis**: Study how vision, audition, and language interact in the brain
- **Individual prediction**: Predict brain responses for new subjects without individual training data
- **Encoding model replacement**: Supersede traditional linear encoding models with multimodal deep learning
- **Multisensory integration mapping**: Reveal fine-grained topography of cross-modal brain processing

## Pitfalls
- Requires massive unified fMRI dataset (1000+ hours) for effective training
- Interpretability of latent features requires careful validation against known neuroscience
- Cross-subject generalization may be limited for populations underrepresented in training data
- In-silico results must be validated against empirical findings before drawing conclusions

## Related Skills
- brain-dit-fmri-foundation-model
- neural-dynamics-universal-translator-foundation
- multimodal-brain-connectivity-gnn
- context-selective-multimodal-memory
