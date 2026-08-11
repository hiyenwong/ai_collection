---
name: cortiva-eeg-meg-image-retrieval
description: "CORTIVA framework for EEG- and MEG-to-image retrieval using candidate-score fusion of complementary visual teachers. Enables zero-shot image retrieval from neural responses by aligning three decoding routes to heterogeneous visual targets, scoring candidates independently, and combining temperature-scaled score vectors before ranking. Use for brain-computer interface applications involving neural decoding, EEG/MEG analysis, and cross-modal retrieval tasks."
metadata:
  arxiv_id: "2608.01355"
  published: "2026-08-02"
  authors: "Junhan Wang, Kani Chen"
  tags: [eeg, meg, brain-computer-interface, neural-decoding, image-retrieval, candidate-score-fusion]
license: Complete terms in LICENSE.txt
---

# CORTIVA: Candidate-Score Fusion for EEG- and MEG-to-Image Retrieval

## Overview
CORTIVA (Candidate-Score Fusion of Complementary Visual Teachers) is a framework for decoding visual experience from non-invasive brain activity (EEG/MEG) to retrieve viewed images from a candidate bank. Unlike traditional approaches that consolidate heterogeneous visual supervision into a single embedding before ranking, CORTIVA preserves complementary evidence by maintaining three independent decoding routes aligned to different visual targets.

## Key Innovations
1. **Candidate-Score Fusion**: Three decoding routes score the same indexed candidates independently and combine only their temperature-scaled score vectors before ranking
2. **Heterogeneous Visual Targets**: Each route aligns to different visual representations, preserving encoder-specific disagreements 
3. **Modality-Specific Neural Encoder**: Framework adapts to both EEG and MEG modalities with specialized encoders
4. **Simple Integration**: Gains arise from integrating complementary route scores without requiring specialized weighting rules

## Performance Results
- **THINGS-EEG2 benchmark**: 73.5% Top-1 and 95.3% Top-5 accuracy across ten participants (200-way retrieval)
- **THINGS-MEG benchmark**: 42.4% Top-1 accuracy
- **Improvement**: Exceeds strongest reported baseline by 10.3 percentage points (Top-1)

## Methodology
### Architecture Components
1. **Neural Encoder**: Modality-specific encoder for EEG or MEG data
2. **Visual Teachers**: Three heterogeneous visual representation models (e.g., DINOv2 variants)
3. **Contrastive Alignment**: Each neural encoder route aligns to its corresponding visual teacher
4. **Independent Scoring**: Each route scores all candidates in the bank independently
5. **Score Fusion**: Temperature-scaled score vectors are combined before final ranking

### Implementation Steps
1. **Data Preparation**: 
   - Preprocess EEG/MEG data according to modality specifications
   - Prepare candidate image bank with fixed indexing
   
2. **Model Setup**:
   - Initialize modality-specific neural encoder
   - Load three heterogeneous visual teacher models
   - Configure contrastive alignment losses for each route
   
3. **Training**:
   - Train neural encoder with contrastive alignment to visual teachers
   - Validate on held-out neural responses
   
4. **Inference**:
   - Encode neural response through trained encoder
   - Generate scores for all candidates via three routes
   - Apply temperature scaling to score vectors
   - Combine scores and rank candidates

## Use Cases
- **Brain-Computer Interfaces**: Real-time image identification from neural activity
- **Neuroscience Research**: Studying neural-visual correspondence and decoding mechanisms  
- **Zero-Shot Retrieval**: Identifying viewed content without task-specific training
- **Cross-Modal Analysis**: Understanding how different visual representations map to neural responses

## Pitfalls and Considerations
- **Candidate Bank Size**: Performance scales with candidate bank diversity but computational cost increases
- **Temperature Scaling**: Optimal temperature parameters may vary between modalities and datasets
- **Visual Teacher Selection**: Choice of heterogeneous visual targets significantly impacts performance
- **Neural Data Quality**: Requires high-quality, properly preprocessed EEG/MEG data
- **Computational Resources**: Three independent scoring routes require 3x computational resources vs single-route approaches

## Validation
The framework has been validated on:
- **THINGS-EEG2**: 200-way image retrieval benchmark with 10 participants
- **THINGS-MEG**: MEG-based image retrieval benchmark
- **Route Removal Analysis**: Demonstrates gain arises from complementary score integration
- **Weight Controls**: Shows uniform weighting achieves similar performance to learned weights

## References
- **Original Paper**: [arXiv:2608.01355](https://arxiv.org/abs/2608.01355)
- **Code Repository**: https://github.com/Fuyunhan/CORTIVA
- **THINGS Dataset**: Standard benchmark for neural image retrieval
- **DINOv2**: Visual foundation model used for heterogeneous targets

## Activation Keywords
- cortiva
- eeg image retrieval  
- meg image retrieval
- neural decoding
- brain-computer interface
- candidate-score fusion
- heterogeneous visual teachers
- zero-shot neural retrieval