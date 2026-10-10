---
name: cortiva-candidate-score-fusion
version: 1.0.0
description: CORTIVA methodology for candidate-score fusion of complementary visual teachers for EEG- and MEG-to-image retrieval
tags:
  - brain-computer-interface
  - neural-decoding
  - image-retrieval
  - eeg
  - meg
  - multimodal-learning
trigger_words:
  - cortiva
  - candidate-score fusion
  - neural image retrieval
  - eeg-to-image
  - meg-to-image
  - visual teachers
---

# CORTIVA: Candidate-Score Fusion for Neural Image Retrieval

## Overview
CORTIVA (Candidate-Score Fusion of Complementary Visual Teachers) is a framework for decoding visual experience from non-invasive brain activity (EEG and MEG) through candidate-score fusion. Instead of collapsing heterogeneous visual supervision into a single embedding before ranking, CORTIVA preserves complementary evidence by aligning three decoding routes to heterogeneous visual targets, scoring the same indexed candidates independently, and combining only their temperature-scaled score vectors before ranking.

## Key Innovations

### 1. Candidate-Score Fusion Framework
- **Independent Route Scoring**: Three decoding routes aligned to heterogeneous visual targets score the same candidate bank independently
- **Score Vector Combination**: Only temperature-scaled score vectors are combined before final ranking
- **Preservation of Complementary Evidence**: Maintains encoder-specific disagreements and diverse similarity geometries

### 2. Heterogeneous Visual Supervision
- **Multiple Visual Targets**: Different visual encoders provide complementary supervision signals
- **Diverse Similarity Geometries**: Each route maintains its own similarity space for candidate evaluation
- **Independent Alignment**: Each neural decoder route aligns independently to its visual target

### 3. Temperature-Scaled Score Integration
- **Calibrated Score Vectors**: Temperature scaling ensures proper score calibration across routes
- **Simple Weighted Combination**: Uniform weighting demonstrates effectiveness without complex fusion rules
- **Robust Performance**: Gains persist even with uniform weighting, indicating inherent complementarity

## Performance Results

### EEG Results (THINGS-EEG2 Benchmark)
- **73.5% Top-1 accuracy** across ten participants (200-way retrieval)
- **95.3% Top-5 accuracy** 
- **+10.3 percentage points** improvement over strongest baseline for Top-1
- **+5.4 percentage points** improvement over strongest baseline for Top-5

### MEG Results (THINGS-MEG)
- **42.4% Top-1 accuracy** with modality-specific neural encoder
- Establishes new state-of-the-art for MEG-based image retrieval

## Methodology Components

### Decoding Architecture
1. **Neural Encoder**: Modality-specific (EEG or MEG) neural activity encoder
2. **Visual Teachers**: Multiple heterogeneous visual representation models
3. **Route Alignment**: Independent contrastive alignment between neural and visual spaces
4. **Candidate Scoring**: Independent scoring of fixed candidate bank by each route
5. **Score Fusion**: Temperature-scaled combination of score vectors
6. **Final Ranking**: Rank candidates based on fused scores

### Validation Controls
- **Route-Removal Retraining**: Matched retraining after route removal confirms complementarity
- **Weight Controls**: Four different weighting schemes demonstrate robustness
- **DINOv2 Analysis**: Independent analyses reproduce local error neighborhoods and neural-visual correspondence

## Applications

### Brain-Computer Interfaces
- **Visual Experience Decoding**: Real-time identification of viewed images from neural activity
- **Zero-Shot Retrieval**: No need for subject-specific training on target images
- **Millisecond Resolution**: Leverages temporal precision of EEG/MEG

### Neuroscience Research
- **Neural-Visual Correspondence**: Provides insights into how visual information is represented in brain activity
- **Cross-Modal Alignment**: Studies alignment between neural and artificial visual representations
- **Temporal Dynamics**: Enables study of visual processing dynamics at millisecond resolution

## Implementation Guidelines

### For EEG/MEG Processing
- Use appropriate preprocessing pipelines for neural data
- Consider temporal windowing strategies for optimal decoding
- Implement modality-specific neural encoders

### For Visual Teacher Selection
- Choose diverse visual models (different architectures, training objectives)
- Ensure visual models are pretrained on relevant datasets
- Consider computational efficiency for real-time applications

### For Score Fusion
- Implement temperature scaling for proper score calibration
- Start with uniform weighting as baseline
- Experiment with learned weighting if additional performance is needed

## Use Cases
Use when:
- Building EEG/MEG-based brain-computer interfaces for image retrieval
- Researching neural decoding of visual experience
- Developing multimodal learning systems with complementary supervision
- Exploring alternative approaches to embedding-level consolidation
- Working with zero-shot neural image retrieval tasks

## References
- Wang, J., Chen, K. (2026). CORTIVA: Candidate-Score Fusion of Complementary Visual Teachers for EEG- and MEG-to-Image Retrieval. arXiv:2608.01355v1
- GitHub Repository: https://github.com/Fuyunhan/CORTIVA
- THINGS-EEG2 Dataset: Standard benchmark for neural image retrieval
- THINGS-MEG Dataset: MEG counterpart for neural image retrieval

## Pitfalls and Considerations

### Data Requirements
- **Large Candidate Banks**: Performance scales with candidate bank size but increases computational cost
- **Preprocessing Sensitivity**: Neural decoding performance sensitive to preprocessing choices
- **Subject Variability**: Inter-subject variability may require personalized approaches

### Computational Considerations
- **Memory Requirements**: Large candidate banks require significant memory for score storage
- **Real-time Constraints**: Multiple visual teachers increase computational load
- **Temperature Calibration**: Proper temperature scaling crucial for effective fusion

### Evaluation Metrics
- **Top-K Accuracy**: Primary metric for retrieval performance
- **Mean Reciprocal Rank (MRR)**: Alternative ranking metric
- **Computational Efficiency**: Inference time and memory usage for practical applications