---
name: eccentricity-constrained-cnn-visual-field
description: Eccentricity-Constrained CNN Training methodology for adaptive visual information coding around the visual field using egocentric data
trigger_words:
  - eccentricity constrained cnn
  - visual field coding
  - egocentric video training
  - fovea periphery models
  - gaze contingent crops
categories:
  - neuroscience
  - computational neuroscience
  - computer vision
  - deep learning
paper:
  title: "Eccentricity-Constrained CNN Training Reveals Adaptive Information Coding Around the Visual Field"
  authors: ["Dylan M. Diaz", "Margaret M. Henderson"]
  arxiv_id: "2607.19316v1"
  published: "2026-07-21"
  conference: "Proceedings of the Conference on Cognitive Computational Neuroscience 2026"
---

# Eccentricity-Constrained CNN Training for Visual Field Coding

This skill implements the methodology from the paper "Eccentricity-Constrained CNN Training Reveals Adaptive Information Coding Around the Visual Field" (arXiv:2607.19316v1) which demonstrates how visual processing adapts to different parts of the visual field using egocentric experience data.

## Key Insights

The research shows that:
- Center-preferring cortical populations have higher spatial resolution and overlap face/word-selective regions
- Periphery-preferring populations have lower spatial resolution and overlap scene-selective regions  
- This "eccentricity bias" reflects differential task-relevance across the visual field
- Egocentric experience with eye-tracking data can adaptively constrain cortical information processing

## Implementation Steps

### 1. Data Preparation
Use egocentric video and eye-tracking data from the Visual Experience Dataset (VEDB):
- Extract frames with gaze-contingent modifications
- Create three types of crops:
  - **Fovea-only crops**: Central region around gaze point
  - **Periphery-only crops**: Outer regions excluding central area  
  - **NeuroFovea-transformed periphery**: Periphery crops with neural-inspired transformation

### 2. Model Training
Train ResNet-18 models using contrastive learning (SimCLR):
```python
# Pseudo-code for eccentricity-constrained training
def create_eccentricity_crops(frame, gaze_point, crop_type='fovea'):
    if crop_type == 'fovea':
        return extract_foveal_region(frame, gaze_point, radius=64)
    elif crop_type == 'periphery':
        return extract_peripheral_region(frame, gaze_point, inner_radius=64, outer_radius=256)
    elif crop_type == 'neurofovea':
        periphery = extract_peripheral_region(frame, gaze_point, inner_radius=64, outer_radius=256)
        return apply_neurofovea_transform(periphery)
```

### 3. Evaluation Protocol
Evaluate using downstream tasks and neural alignment:
- **In-domain classification**: VEDB frame categorization across eccentricities
- **Downstream classification**: 
  - Scene categorization (Places365) 
  - Face recognition (VGGFace2)
- **Neural alignment**: Compare with human fMRI data (Natural Scenes Dataset)

### 4. Analysis Framework
Analyze model performance across visual cortex regions:
- **Scene-selective cortex (PPA, RSC)**: Expect periphery-only model advantage
- **Face/word-selective regions**: Expect fovea-only model advantage
- **General visual cortex**: Compare with ImageNet-100 trained models

## Expected Outcomes

- Fovea-only models show stronger performance on fine-grained tasks (face recognition, reading)
- Periphery-only models show advantage in scene understanding tasks
- VEDB-pretrained models achieve neural predictivity comparable to ImageNet-100 models
- Scene-selective cortex shows consistent advantage for periphery-only models

## Usage Scenarios

Use this methodology when:
- Developing vision systems that need to handle both central and peripheral visual processing
- Creating brain-aligned computer vision models
- Studying how egocentric experience shapes visual representations
- Building adaptive visual systems for AR/VR applications

## References

- Diaz, D. M., & Henderson, M. M. (2026). Eccentricity-Constrained CNN Training Reveals Adaptive Information Coding Around the Visual Field. arXiv:2607.19316v1
- Visual Experience Dataset (VEDB): https://vedb.io/
- Natural Scenes Dataset: https://natural-scenes-dataset.org/