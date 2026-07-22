---
name: eccentricity-constrained-cnn-training
short_description: Eccentricity-Constrained CNN Training methodology for adaptive information coding around the visual field using egocentric video data with eye-tracking.
domains: [neuroscience, computational-neuroscience, computer-vision, brain-ai-alignment]
trigger_words: [eccentricity constrained cnn, fovea periphery vision, egocentric visual experience, gaze-contingent processing, VEDB, Natural Scenes Dataset]
arxiv_id: 2607.19316
authors: Dylan M. Diaz, Margaret M. Henderson
date_added: 2026-07-23
---

# Eccentricity-Constrained CNN Training for Adaptive Visual Field Coding

## Overview

This skill implements the methodology from arXiv:2607.19316 "Eccentricity-Constrained CNN Training Reveals Adaptive Information Coding Around the Visual Field" by Dylan M. Diaz and Margaret M. Henderson. The approach trains CNNs on gaze-contingent egocentric video data to model how the primate visual system develops eccentricity-dependent coding strategies.

## Key Concepts

### Biological Foundation
- **Center-preferring cortical populations**: Higher spatial resolution, overlap face/word-selective regions
- **Periphery-preferring populations**: Lower spatial resolution, overlap scene-selective regions  
- **Eccentricity bias**: Reflects differential task-relevance across the visual field based on natural viewing behavior

### Methodology Components
- **Visual Experience Dataset (VEDB)**: Egocentric video with eye-tracking for natural viewing patterns
- **Eccentricity isolation**: 
  - Fovea-only crops (central vision)
  - Periphery-only crops (surrounding vision)  
  - Periphery-only crops with NeuroFovea transform
- **Model architecture**: ResNet-18 trained with contrastive learning (SimCLR)
- **Evaluation framework**: 
  - In-domain VEDB frame classification
  - Downstream transfer to VGGFace2 (faces) and Places365 (scenes)
  - Neural alignment using Natural Scenes Dataset (NSD) fMRI

## Implementation Steps

### 1. Data Preparation
```python
# Load VEDB dataset with eye-tracking coordinates
from vedb_loader import load_vedb_dataset
dataset = load_vedb_dataset(eye_tracking=True)

# Create eccentricity-isolated crops
def create_fovea_crops(frames, gaze_points, radius=64):
    """Extract central foveal regions around gaze points"""
    fovea_crops = []
    for frame, gaze in zip(frames, gaze_points):
        x, y = int(gaze[0]), int(gaze[1])
        crop = frame[y-radius:y+radius, x-radius:x+radius]
        fovea_crops.append(crop)
    return fovea_crops

def create_periphery_crops(frames, gaze_points, inner_radius=64, outer_radius=256):
    """Extract peripheral regions excluding foveal area"""
    periphery_crops = []
    for frame, gaze in zip(frames, gaze_points):
        # Create mask for peripheral region
        mask = create_annular_mask(frame.shape, gaze, inner_radius, outer_radius)
        periphery = frame * mask
        periphery_crops.append(periphery)
    return periphery_crops
```

### 2. Model Training
```python
# Train separate models for fovea and periphery
import torch
import torchvision.models as models
from simclr import SimCLR

# Fovea-only model
fovea_model = SimCLR(base_model=models.resnet18(), out_dim=128)
fovea_dataset = create_fovea_crops(vedb_frames, gaze_points)
train_simclr(fovea_model, fovea_dataset)

# Periphery-only model  
periphery_model = SimCLR(base_model=models.resnet18(), out_dim=128)
periphery_dataset = create_periphery_crops(vedb_frames, gaze_points)
train_simclr(periphery_model, periphery_dataset)
```

### 3. Evaluation Pipeline
```python
# Downstream transfer evaluation
def evaluate_downstream(model, task='faces'):
    if task == 'faces':
        # Transfer to VGGFace2
        return evaluate_on_vggface2(model)
    elif task == 'scenes':
        # Transfer to Places365  
        return evaluate_on_places365(model)

# Neural alignment evaluation
def evaluate_neural_alignment(model, nsd_data):
    """Evaluate model alignment with NSD fMRI data"""
    encoding_scores = compute_encoding_model_scores(model, nsd_data)
    return encoding_scores
```

## Expected Results

### Performance Patterns
- **Fovea-only models** show stronger performance on both face recognition (VGGFace2) and scene categorization (Places365)
- **VEDB-pretrained models** generalize better to scene categorization than face recognition overall
- **Periphery-only models** demonstrate small but consistent advantage in scene-selective cortex (PPA, RSC)

### Neural Alignment Findings
- VEDB-pretrained models match neural predictivity of ImageNet-100 models across visual cortex
- Scene-selective cortex shows specific alignment with peripheral statistics
- Egocentric data supports emergence of cortically-aligned representations

## Applications

### Neuroscience Research
- Computational modeling of visual development from natural experience
- Testing hypotheses about ecological constraints shaping neural representations
- Understanding how natural viewing behavior provides implicit supervision

### AI/Computer Vision
- Brain-inspired foveated vision systems leveraging natural viewing patterns
- Egocentric AI systems that learn from first-person perspective data
- Representation learning using gaze-contingent constraints
- Neural decoding studies of visual field organization

## Related Skills
- [[spiking-neural-networks-fmri-visual-decoding]]: Brain-AI alignment using SNN features for fMRI decoding
- [[natural-scenes-dataset-encoding]]: Neural encoding models using NSD fMRI data
- [[egocentric-vision-systems]]: First-person perspective computer vision systems

## References
- Diaz, D. M., & Henderson, M. M. (2026). Eccentricity-Constrained CNN Training Reveals Adaptive Information Coding Around the Visual Field. arXiv:2607.19316
- Visual Experience Dataset (VEDB): https://vedb.io
- Natural Scenes Dataset (NSD): https://naturalscenesdataset.org