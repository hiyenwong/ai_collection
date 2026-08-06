---
name: interpretable-meg-decoding-perceived-speech
description: "Interpretable MEG decoding framework for perceived speech that combines spherical harmonics spatial attention, source-space mapping, and stimulus feature analysis to reveal what drives neural-to-audio retrieval. Use when implementing or analyzing MEG-based brain decoding systems, particularly for speech perception, neural source localization, or interpretable brain-computer interfaces."
metadata:
  arxiv_id: "2608.01481"
  published: "2026-08-04"
  authors: "Ilia Semenkov, Daria Kleeva, Ivan Dakhtin, Zarina Maksudova, Alex Ossadtchi"
  tags: [meg-decoding, speech-perception, interpretable-bci, source-localization, spherical-harmonics, neural-retrieval, wav2vec-embedding]
license: Complete terms in LICENSE.txt
---

# Interpretable MEG Decoding of Perceived Speech

## Overview

This methodology addresses the interpretability gap in MEG-to-audio retrieval systems by redesigning both the front-end spatial processing and decoder architecture to map directly onto electrophysiological quantities. Unlike standard deep networks trained with CLIP-style objectives against wav2vec 2.0 embeddings (which have opaque weights), this approach reveals which speech properties drive neural retrieval through source-space mapping and systematic input interventions.

## Key Innovations

### 1. Spherical Harmonics Spatial Attention
- **Problem**: Standard spatial attention operates on flattened sensor layouts, ignoring 3D MEG helmet geometry
- **Solution**: Replace with spherical harmonics defined on three-dimensional MEG helmet geometry
- **Benefit**: Enables direct mapping to cortical source space and physiologically meaningful interpretation

### 2. Source-Space Branch Architecture
- **Architecture**: Reduce subject-specific representation from 270 to 25 branches
- **Temporal Filtering**: Add temporal filter to each branch to match neuronal sources in space and time
- **Shallower Decoder**: Implement convolutional decoder with fewer parameters (20x reduction)
- **Preprocessing**: Remove ocular and cardiac components to eliminate stimulus-locked shortcuts

### 3. Systematic Stimulus Feature Analysis
- **MEG Occlusion**: Paired MEG occlusion reveals contribution of 19 stimulus features
- **Key Drivers**: Silence, sound intensity, vowels, and acoustic onsets show largest effects
- **Narrative Structure**: Coherent speech carries more recoverable information than random word lists
- **Feature Compression**: wav2vec target can be reduced to ~12 learned dimensions without accuracy loss

## Performance Results

- **Top-1 Accuracy**: 39.75% ± 0.34% among 1005 candidates across six trained solutions
- **Parameter Efficiency**: ~20 times fewer decoder parameters than baseline architecture
- **Source Recovery**: Weights map to source space, recovering generators consistent with speech-perception network
- **Hemispheric Specialization**: Left-lateralized branches carry higher-frequency rhythmic components

## Implementation Guidelines

### Core Architecture Components

#### Front-End Processing
1. **Sensor Geometry**: Represent MEG sensors using spherical harmonics on 3D helmet geometry
2. **Source Mapping**: Transform sensor-space data to source-space using spherical harmonics basis
3. **Branch Architecture**: Create 25 subject-specific branches with temporal filters
4. **Artifact Removal**: Apply preprocessing to remove ocular and cardiac components

#### Decoder Design
1. **Shallow Convolutional Decoder**: Use minimal layers to reduce parameter count
2. **wav2vec Target**: Train against wav2vec 2.0 audio embeddings with dimensionality reduction
3. **CLIP-Style Objective**: Maintain contrastive learning objective for retrieval performance

### Training Protocol
1. **Dataset**: Use MEG-MASC dataset with naturalistic speech stimuli
2. **Preprocessing**: Apply artifact removal before training to prevent shortcut learning
3. **Evaluation**: Test on 1005 candidate audio segments for Top-1 retrieval accuracy
4. **Cross-Validation**: Train multiple solutions (6+) to ensure robustness

## Methodology

### Step 1: Problem Analysis
Identify whether your task requires:
- Interpretable brain decoding (not just black-box performance)
- Source-space neural activity mapping
- Understanding which stimulus features drive neural responses
- Efficient parameter usage in decoder architecture

### Step 2: Architecture Implementation
1. **Spatial Processing**: Implement spherical harmonics basis for 3D MEG geometry
2. **Branch Creation**: Design 25 branches with temporal filtering per branch
3. **Decoder Design**: Build shallow convolutional decoder with minimal parameters
4. **Preprocessing Pipeline**: Integrate ocular/cardiac artifact removal

### Step 3: Training and Validation
1. **Contrastive Training**: Train with CLIP-style objective against wav2vec embeddings
2. **Source Validation**: Verify that weights map meaningfully to cortical sources
3. **Feature Analysis**: Perform systematic occlusion studies to identify key drivers
4. **Ablation Studies**: Test narrative vs. random speech structure effects

### Step 4: Interpretation and Analysis
1. **Source Localization**: Analyze recovered generators against known speech-perception network
2. **Hemispheric Analysis**: Examine left vs. right hemisphere specialization patterns
3. **Feature Contribution**: Quantify contribution of individual stimulus features
4. **Dimensionality Analysis**: Determine optimal wav2vec embedding dimensionality

## Applications

### Primary Use Cases
- **Speech Perception Research**: Study neural mechanisms of natural speech processing
- **Interpretable BCI**: Develop brain-computer interfaces with transparent decision-making
- **Neural Source Localization**: Map MEG activity to cortical generators during speech perception
- **Stimulus Feature Analysis**: Identify which acoustic features drive neural responses

### Secondary Applications
- **Clinical Diagnostics**: Assess speech processing deficits in neurological disorders
- **Audio Retrieval Systems**: Build neural-guided audio search and retrieval systems
- **Cognitive Neuroscience**: Investigate narrative structure processing in the brain
- **Neurotechnology Development**: Design next-generation neural decoding architectures

## Pitfalls and Solutions

### Common Issues
1. **Geometry Mismatch**: Incorrect spherical harmonics implementation for MEG helmet
   - **Solution**: Validate geometry representation against known MEG sensor positions

2. **Overfitting**: Small number of branches may lead to overfitting
   - **Solution**: Use cross-validation and multiple training solutions

3. **Artifact Contamination**: Residual ocular/cardiac artifacts create false correlations
   - **Solution**: Apply rigorous preprocessing and validate with clean/noisy comparisons

4. **Source Ambiguity**: Multiple source configurations may explain same sensor data
   - **Solution**: Use regularization and anatomical constraints in source mapping

### Validation Checks
- Verify source-space mapping recovers known speech-perception network regions
- Confirm hemispheric specialization matches literature (left dominance for speech)
- Validate that occlusion results are consistent across multiple subjects
- Ensure narrative structure effects are robust to different speech materials

## References

- **Original Paper**: Semenkov, I., Kleeva, D., Dakhtin, I., Maksudova, Z., & Ossadtchi, A. (2026). Interpretable MEG Decoding of Perceived Speech: Cortical Sources and the Stimulus Features That Drive Retrieval. arXiv:2608.01481 [cs.LG].
- **Related Work**:
  - Huth, A. G., et al. (2016). Natural speech reveals the semantic maps that tile human cerebral cortex. Nature.
  - Schrimpf, M., et al. (2021). Brain-Score: Which artificial neural network for object recognition is most brain-like? PLOS Computational Biology.
  - Kell, A. J. E., et al. (2018). A task-optimized neural network replicates human auditory behavior, predicts brain responses, and reveals a cortical processing hierarchy. Neuron.

## Activation Keywords
- interpretable meg decoding
- perceived speech
- spherical harmonics meg
- source-space mapping
- speech perception network
- neural retrieval
- stimulus feature analysis
- wav2vec embedding
- brain-computer interface
- narrative structure processing