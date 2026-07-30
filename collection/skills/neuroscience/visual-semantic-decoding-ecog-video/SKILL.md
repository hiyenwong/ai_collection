---
name: visual-semantic-decoding-ecog-video-stimuli
title: Visual Semantic Decoding of Electrocorticography from Video Stimuli using End-to-End Deep Learning
description: End-to-end deep learning framework for visual semantic decoding from ECoG, demonstrating promising performance without handcrafted features while maintaining interpretability.
arxiv_id: 2607.18923
date: 2026-07-21
authors:
  - Stella Ho
  - Joel Villalobos
  - Joseph West
  - Jingyang Liu
  - Weijie Qi
  - Haruhiko Kishima
  - Ryohei Fukuma
  - Takufumi Yanagisawa
  - Sam E. John
  - David B. Grayden
categories:
  - cs.LG
  - q-bio.NC
trigger_words:
  - visual semantic decoding
  - electrocorticography
  - ECoG
  - end-to-end deep learning
  - video stimuli
  - Transformer encoder
  - high-gamma
---

# Visual Semantic Decoding of Electrocorticography from Video Stimuli using End-to-End Deep Learning

## Overview
This study examines the feasibility of visual semantic decoding using an end-to-end deep learning framework with electrocorticography (ECoG) to predict visual categories from video stimuli using time-series neural inputs.

## Key Contributions

### 1. End-to-End Framework Design
- **No Handcrafted Features**: Demonstrates that end-to-end deep learning can yield promising decoding performance without manual feature engineering
- **Data Efficiency**: Achieves good performance with fewer than 50 training samples per visual category
- **Multiple Architecture Evaluation**: Evaluates various deep learning approaches and neural network architectures

### 2. Optimal Configuration
- **Mixup Augmentation**: Uses mixup data augmentation to improve generalization
- **Transformer Encoder**: Employs a Transformer-based encoder for sequence modeling
- **High-Gamma Band**: Focuses on high-gamma frequency band (80-150 Hz) inputs
- **Temporal Window**: Uses 900 ms post-stimulus temporal window

### 3. Interpretability Analysis
- **Spectral Dimension**: Analyzes discriminative information across frequency bands
- **Temporal Dimension**: Examines temporal dynamics of decoding performance
- **Cortical Dimension**: Identifies key brain regions contributing to decoding

### 4. Key Brain Regions Identified
- **Early Visual Cortex**: V2-V4 areas contribute substantially
- **Ventral Stream**: Ventral stream visual cortex involvement
- **MT+ Complex**: MT+ complex with neighboring visual areas
- **Lateral Temporal Cortex**: Significant contribution from lateral temporal cortex

## Applications

### Brain-Computer Interfaces (BCIs)
- **Visual Category Decoding**: Enables real-time decoding of perceived visual categories
- **Dynamic Stimuli Processing**: Handles complex, dynamic video stimuli rather than static images
- **Clinical Applications**: Potential applications for patients with communication disorders

### Neuroscience Research
- **Neural Representation Mapping**: Maps neural activity to semantic visual categories
- **Cross-Modal Integration**: Studies integration of visual perception and neural activity
- **Validation of Established Knowledge**: Confirms findings consistent with established neuroscience

### Machine Learning
- **Low-Data Regime Learning**: Demonstrates effective learning with limited training data
- **Interpretable Deep Learning**: Maintains model interpretability while using complex architectures
- **Multimodal Learning**: Integrates neural time-series with visual semantic categories

## Implementation Guidelines

### Data Preprocessing
- **Frequency Filtering**: Apply band-pass filtering to extract high-gamma (80-150 Hz) components
- **Temporal Segmentation**: Use 900 ms post-stimulus windows for analysis
- **Data Augmentation**: Implement mixup augmentation for small datasets

### Model Architecture
- **Transformer Encoder**: Use Transformer-based architecture for sequence modeling
- **End-to-End Training**: Train the entire pipeline jointly without intermediate feature extraction
- **Regularization**: Apply appropriate regularization for small datasets

### Evaluation Protocol
- **Cross-Validation**: Use proper cross-validation given limited data
- **Baseline Comparison**: Compare against traditional feature-engineered approaches
- **Statistical Significance**: Ensure statistical significance of results

## Verification Steps

1. **Performance Benchmarking**: Compare decoding accuracy against baseline methods
2. **Brain Region Analysis**: Verify identified brain regions match established neuroscience knowledge
3. **Frequency Band Validation**: Confirm high-gamma band importance through ablation studies
4. **Temporal Dynamics**: Analyze temporal evolution of decoding performance
5. **Generalization Testing**: Test generalization to unseen visual categories

## Related Skills
- `eeg-foundation-model-adapters`
- `visual-imagery-decoding-fmri`
- `brain-it-vqa-fmri-visual-question-answering`
- `transformer-brain-topological-alignment`

## References
- arXiv:2607.18923 [cs.LG]
- DOI: https://doi.org/10.48550/arXiv.2607.18923
- Note: This is a preprint and has not yet undergone peer review