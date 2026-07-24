---
name: eccentricity-constrained-cnn-training
short_description: Methodology for training CNNs with eccentricity-constrained egocentric video data to reveal adaptive information coding that mirrors primate visual system organization.
domains: [neuroscience, computational-neuroscience, computer-vision, brain-ai-alignment]
trigger_words: [eccentricity-constrained cnn, fovea-periphery vision coding, egocentric visual experience, adaptive information coding visual field]
arxiv_id: 2607.19316
authors: Dylan M. Diaz, Margaret M. Henderson
date_added: 2026-07-23
---

# Eccentricity-Constrained CNN Training Reveals Adaptive Information Coding Around the Visual Field

## Overview

This methodology investigates how **eccentricity-dependent visual coding** emerges from natural egocentric experience by training CNNs on gaze-contingent crops from the Visual Experience Dataset (VEDB). The research demonstrates that models trained on different eccentricities (fovea-only vs. periphery-only) develop specialized capabilities that mirror the functional organization of the primate visual system.

## Key Findings

### Visual System Organization
- **Center-preferring cortical populations**: Higher spatial resolution, overlap with face- and word-selective regions
- **Periphery-preferring populations**: Lower spatial resolution, overlap with scene-selective regions (PPA, RSC)
- **Eccentricity bias**: Reflects differential task-relevance across visual field regions

### Model Performance Differences
- **Fovea-only models**: Stronger on face recognition and fine-grained tasks
- **Periphery-only models**: Show advantage in scene-selective cortex (PPA, RSC)
- **VEDB-pretrained models**: Match neural predictivity of ImageNet-100 models across visual cortex

### Natural Experience Effects
- **Egocentric data**: Supports emergence of cortically-aligned representations
- **Adaptive constraints**: Natural visual experience shapes cortical information processing
- **Task-specific informativeness**: Different eccentricities provide varying information for different tasks

## Implementation Steps

### 1. Data Preparation
```python
# Load VEDB egocentric video and eye-tracking data
from vedb_loader import load_vedb_dataset
vedb_data = load_vedb_dataset('path/to/vedb')

# Create eccentricity-constrained crops
def create_eccentricity_crops(frames, gaze_positions, crop_type='fovea'):
    """Create gaze-contingent crops based on eccentricity"""
    crops = []
    for frame, gaze in zip(frames, gaze_positions):
        if crop_type == 'fovea':
            # Fovea-only crop around gaze position
            fovea_crop = extract_foveal_region(frame, gaze, radius=64)
            crops.append(fovea_crop)
        elif crop_type == 'periphery':
            # Periphery-only crop (mask out foveal region)
            periphery_crop = extract_peripheral_region(frame, gaze, inner_radius=64, outer_radius=256)
            crops.append(periphery_crop)
        elif crop_type == 'neurofovea':
            # Apply NeuroFovea transform to periphery
            neurofovea_crop = apply_neurofovea_transform(frame, gaze)
            crops.append(neurofovea_crop)
    
    return np.array(crops)
```

### 2. Model Training
```python
# Train ResNet-18 with contrastive learning (SimCLR)
import torch
import torch.nn as nn
from torchvision.models import resnet18

def train_eccentricity_model(crops, crop_type, epochs=100):
    """Train CNN model on eccentricity-constrained data"""
    # Initialize ResNet-18
    model = resnet18(pretrained=False)
    model.fc = nn.Identity()  # Remove final classification layer
    
    # Setup contrastive learning
    criterion = NTXentLoss(temperature=0.1)
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)
    
    # Training loop
    for epoch in range(epochs):
        for batch in dataloader:
            # Generate positive pairs through augmentations
            aug1, aug2 = augment_batch(batch)
            
            # Forward pass
            feat1 = model(aug1)
            feat2 = model(aug2)
            
            # Compute contrastive loss
            loss = criterion(feat1, feat2)
            
            # Backward pass
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
    
    return model
```

### 3. Neural Alignment Evaluation
```python
# Evaluate alignment with human fMRI data (Natural Scenes Dataset)
from sklearn.linear_model import Ridge
from scipy.stats import pearsonr

def evaluate_neural_alignment(model, nsd_stimuli, nsd_fmri, alpha=1.0):
    """Evaluate model alignment with fMRI responses"""
    # Extract features from NSD stimuli
    model.eval()
    features = []
    with torch.no_grad():
        for stimulus in nsd_stimuli:
            feature = model(stimulus.unsqueeze(0))
            features.append(feature.squeeze().cpu().numpy())
    features = np.array(features)
    
    # Train encoding models
    correlations = []
    for voxel_idx in range(nsd_fmri.shape[1]):
        ridge = Ridge(alpha=alpha)
        ridge.fit(features, nsd_fmri[:, voxel_idx])
        
        # Predict on test set
        pred = ridge.predict(features_test)
        corr = pearsonr(pred, nsd_fmri_test[:, voxel_idx])[0]
        correlations.append(corr)
    
    return np.array(correlations)
```

### 4. Downstream Task Evaluation
```python
# Evaluate on downstream classification tasks
def evaluate_downstream_tasks(model, task_datasets):
    """Evaluate on face recognition and scene categorization"""
    results = {}
    
    # Face recognition (VGGFace2)
    face_acc = evaluate_on_dataset(model, task_datasets['vggface2'])
    results['face_recognition'] = face_acc
    
    # Scene categorization (Places365)
    scene_acc = evaluate_on_dataset(model, task_datasets['places365'])
    results['scene_categorization'] = scene_acc
    
    return results
```

## Expected Outcomes

### Quantitative Metrics
- **Neural predictivity**: VEDB-pretrained models should match or exceed ImageNet-100 performance
- **Scene-selective cortex advantage**: Periphery-only models show 5-10% higher explained variance in PPA/RSC
- **Task specialization**: Clear performance differences between fovea-only and periphery-only models

### Brain Region Specificity
- **Early visual areas**: Both models perform similarly
- **Face-selective regions (FFA)**: Fovea-only models show advantage
- **Scene-selective regions (PPA, RSC)**: Periphery-only models show consistent advantage
- **Higher-order regions**: Mixed patterns reflecting task demands

## Applications

### Neuroscience Research
- **Visual system organization**: Understanding how natural experience shapes cortical organization
- **Eccentricity coding**: Testing hypotheses about fovea-periphery functional specialization
- **Developmental neuroscience**: Modeling how visual experience guides neural development
- **Computational modeling**: Building more realistic models of visual processing

### AI/Computer Vision
- **Egocentric vision systems**: Developing AI that leverages natural visual experience
- **Task-adaptive architectures**: Creating models that specialize for different visual tasks
- **Brain-inspired AI**: Building systems that mirror biological visual processing principles
- **Representation learning**: Learning features that align with human visual perception

## Best Practices

### Data Selection
- **Use diverse egocentric datasets**: VEDB provides rich natural viewing experience
- **Include eye-tracking data**: Essential for accurate gaze-contingent cropping
- **Balance eccentricity ranges**: Ensure adequate coverage of foveal and peripheral regions

### Model Architecture
- **Start with standard architectures**: ResNet-18 provides good baseline performance
- **Consider receptive field sizes**: Match architecture to eccentricity constraints
- **Use appropriate pretraining**: Contrastive learning works well for unsupervised representation learning

### Evaluation Strategy
- **Multiple downstream tasks**: Test on diverse visual tasks to assess specialization
- **Comprehensive neural alignment**: Evaluate across multiple brain regions and datasets
- **Control comparisons**: Include non-egocentric baselines (e.g., ImageNet) for reference

## Limitations and Future Directions

### Current Limitations
- **Dataset size**: VEDB is smaller than large-scale datasets like ImageNet
- **Computational cost**: Training multiple specialized models requires significant resources
- **Individual differences**: Natural viewing patterns vary across individuals

### Future Research
- **Larger egocentric datasets**: Collect more diverse natural viewing experience
- **Dynamic eccentricity modeling**: Model continuous rather than discrete eccentricity
- **Cross-modal integration**: Combine visual with other sensory modalities
- **Real-time applications**: Develop systems that adapt to user's current gaze behavior

## Related Skills
- [[spiking-neural-networks-fmri-visual-decoding]]: SNN-derived features for fMRI decoding
- [[natural-scenes-dataset-analysis]]: Working with NSD fMRI data
- [[egocentric-vision-modeling]]: General methodology for egocentric computer vision
- [[brain-ai-alignment]]: Methods for aligning artificial and biological neural representations

## References
- Eccentricity-Constrained CNN Training Reveals Adaptive Information Coding Around the Visual Field. arXiv:2607.19316
- Visual Experience Dataset (VEDB): Egocentric video with eye-tracking
- Natural Scenes Dataset (NSD): High-resolution fMRI dataset for visual neuroscience
- SimCLR: Simple Framework for Contrastive Learning of Visual Representations