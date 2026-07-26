---
name: visual-semantic-decoding-ecog
title: Visual Semantic Decoding of Electrocorticography from Video Stimuli
description: End-to-end deep learning framework for decoding visual semantic categories from ECoG signals during video stimulus presentation.
trigger_words:
  - "visual semantic decoding"
  - "ECoG decoding"
  - "electrocorticography video"
  - "brain-to-vision decoding"
  - "neural visual categorization"
paper_id: "2607.18923"
date: "2026-07-21"
authors:
  - "Stella Ho"
  - "Joel Villalobos"
  - "Joseph West"
  - "Jingyang Liu"
  - "Weijie Qi"
  - "Haruhiko Kishima"
  - "Ryohei Fukuma"
  - "Takufumi Yanagisawa"
  - "Sam E. John"
  - "David B. Grayden"
---

# Visual Semantic Decoding of Electrocorticography from Video Stimuli using End-to-End Deep Learning

## Overview
This methodology enables inference of semantic interpretation of visual perception from complex, noisy brain activity using electrocorticography (ECoG). The approach uses an end-to-end deep learning framework to predict visual categories from video stimuli using time-series neural inputs without handcrafted features.

## Key Components

### Dataset
- **Participants**: n=17 patients with drug-resistant epilepsy
- **Modality**: Electrocorticography (ECoG)
- **Stimuli**: Video presentations with visual categories
- **Training samples**: Fewer than 50 samples per visual category

### Best-Performing Architecture
- **Data augmentation**: Mixup augmentation
- **Encoder**: Transformer-based encoder
- **Frequency band**: High-gamma (80-150 Hz) inputs
- **Temporal window**: 900 ms post-stimulus window

### Brain Regions Contributing to Performance
- Early visual cortex (V2-V4)
- Ventral stream visual cortex
- MT+ complex with neighboring visual areas
- Lateral temporal cortex

## Implementation Guidelines

### Preprocessing
1. Extract high-gamma band (80-150 Hz) from raw ECoG signals
2. Apply 900 ms post-stimulus temporal windowing
3. Normalize across channels and trials

### Model Architecture
1. Use Transformer-based encoder architecture
2. Implement mixup data augmentation for limited training samples
3. Apply spectral, temporal, and spatial attention mechanisms

### Evaluation
1. Assess decoding performance across visual categories
2. Analyze model interpretability through spectral, temporal, and cortical dimensions
3. Validate consistency with established neuroscience knowledge

## Applications
- Brain-computer interfaces for visual perception restoration
- Neural decoding of complex visual scenes
- Understanding neural representations of semantic visual categories
- Clinical applications for patients with visual processing disorders

## Validation
The framework demonstrates that end-to-end deep learning can yield promising decoding performance from dynamic visual stimuli while maintaining model interpretability. Results are broadly consistent with established neuroscience knowledge about visual processing pathways.

## References
- arXiv:2607.18923 [cs.LG]
- DOI: https://doi.org/10.48550/arXiv.2607.18923