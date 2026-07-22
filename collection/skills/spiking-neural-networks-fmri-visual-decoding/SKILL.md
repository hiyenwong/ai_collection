---
name: spiking-neural-networks-fmri-visual-decoding
short_description: Methodology for using Spiking Neural Network (SNN)-derived visual features as targets for fMRI-based visual semantic decoding, demonstrating superior brain alignment compared to traditional ANN features.
domains: [neuroscience, computational-neuroscience, brain-ai-alignment, spiking-neural-networks, fMRI]
trigger_words: [snn fmri decoding, spiking neural network brain decoding, fMRI visual semantic decoding, visual semantic decoding, brain decoding]
arxiv_id: 2607.19170
authors: Unknown
date_added: 2026-07-23
---

# Spiking Neural Networks for fMRI-Based Visual Semantic Decoding

## Overview

This skill implements the methodology from arXiv:2607.19170 "Spiking Neural Networks for fMRI-Based Visual Semantic Decoding". The approach uses SNN-derived visual features as targets for fMRI-based visual semantic decoding, showing significantly superior alignment with brain activity compared to traditional Artificial Neural Network (ANN) features.

## Key Results

### Performance Improvements
- **Feature-prediction error**: Reduced from 0.7707 (ANN) to 0.0282 (SNN) - a 27x improvement
- **Top-1 semantic decoding accuracy**: Improved from 0.1800 (ANN) to 0.4400 (SNN) on GoD dataset - a 2.4x improvement
- **Brain alignment**: SNN features show substantially better correlation with fMRI activity patterns

### Why SNNs Work Better
- **Temporal dynamics**: SNNs capture temporal aspects of neural processing that ANNs miss
- **Sparse coding**: Spike-based representations align better with biological neural coding principles
- **Energy efficiency**: SNN computation mirrors metabolic constraints of biological systems
- **Event-driven processing**: Matches the asynchronous nature of neural information processing

## Implementation Steps

### 1. SNN Feature Extraction
```python
# Load pre-trained SNN model
from snn_models import load_pretrained_snn
snn_model = load_pretrained_snn('snn_vgg16')

# Extract features from visual stimuli
def extract_snn_features(stimuli, model, time_steps=10):
    """Extract temporal SNN features from visual stimuli"""
    features = []
    for stimulus in stimuli:
        # Convert to spike trains
        spike_trains = intensity_to_latency(stimulus, time_steps)
        
        # Forward pass through SNN
        membrane_potentials = model(spike_trains)
        
        # Extract features at multiple time steps
        temporal_features = []
        for t in range(time_steps):
            feature_t = membrane_potentials[t].flatten()
            temporal_features.append(feature_t)
        
        # Aggregate temporal features
        aggregated_feature = aggregate_temporal_features(temporal_features)
        features.append(aggregated_feature)
    
    return np.array(features)
```

### 2. fMRI Encoding Model
```python
# Train fMRI encoding model using SNN features
from sklearn.linear_model import Ridge
from scipy.stats import pearsonr

def train_fMRI_encoding_model(snn_features, fMRI_data, alpha=1.0):
    """Train linear encoding model from SNN features to fMRI responses"""
    # Normalize features and fMRI data
    snn_features_norm = normalize_features(snn_features)
    fMRI_data_norm = normalize_fMRI(fMRI_data)
    
    # Train ridge regression model for each voxel
    models = []
    for voxel_idx in range(fMRI_data_norm.shape[1]):
        model = Ridge(alpha=alpha)
        model.fit(snn_features_norm, fMRI_data_norm[:, voxel_idx])
        models.append(model)
    
    return models

def evaluate_encoding_performance(models, test_features, test_fMRI):
    """Evaluate encoding model performance"""
    predictions = []
    for model in models:
        pred = model.predict(test_features)
        predictions.append(pred)
    
    predictions = np.array(predictions).T
    correlations = [pearsonr(predictions[:, i], test_fMRI[:, i])[0] 
                   for i in range(test_fMRI.shape[1])]
    
    return np.mean(correlations), correlations
```

### 3. Semantic Decoding Pipeline
```python
# Semantic category decoding from fMRI
from sklearn.metrics import top_k_accuracy_score

def semantic_decoding_pipeline(fMRI_data, semantic_labels, encoding_models):
    """Decode semantic categories from fMRI using inverse encoding"""
    # Reconstruct features from fMRI
    reconstructed_features = []
    for voxel_model in encoding_models:
        # Inverse mapping (simplified)
        inv_features = inverse_encoding(voxel_model, fMRI_data)
        reconstructed_features.append(inv_features)
    
    reconstructed_features = np.mean(reconstructed_features, axis=0)
    
    # Classify semantic categories
    classifier = train_semantic_classifier(reconstructed_features, semantic_labels)
    predictions = classifier.predict(reconstructed_features)
    
    # Evaluate top-k accuracy
    top1_acc = top_k_accuracy_score(semantic_labels, predictions, k=1)
    top5_acc = top_k_accuracy_score(semantic_labels, predictions, k=5)
    
    return top1_acc, top5_acc, predictions
```

## Expected Outcomes

### Quantitative Metrics
- **Feature prediction correlation**: >0.95 correlation between predicted and actual SNN features
- **Semantic decoding accuracy**: 40-50% top-1 accuracy on standard datasets (GoD, ImageNet)
- **Voxel-wise encoding performance**: Significant improvement over ANN baselines across visual cortex

### Brain Region Specificity
- **Early visual areas (V1, V2)**: Strong alignment with low-level SNN features
- **Higher visual areas (IT, PPA)**: Better alignment with high-level semantic SNN features  
- **Frontal regions**: Moderate improvement, suggesting SNNs capture some cognitive aspects

## Applications

### Neuroscience Research
- **Neural representation analysis**: Understanding how visual information is encoded in the brain
- **Brain-AI alignment studies**: Comparing artificial and biological neural representations
- **Computational neuroscience**: Testing hypotheses about neural coding principles
- **fMRI methodology**: Improving brain decoding and encoding model performance

### AI/Computer Vision
- **Brain-inspired computer vision**: Developing more biologically plausible vision systems
- **Neuromorphic computing**: Implementing energy-efficient visual processing
- **Representation learning**: Learning features that align with human perception
- **Explainable AI**: Using brain alignment as a measure of model interpretability

## Related Skills
- [[eccentricity-constrained-cnn-training]]: CNN training with eccentricity constraints for visual field coding
- [[spiking-jelly-framework]]: SpikingJelly framework for SNN development and deployment
- [[fMRI-encoding-models]]: General fMRI encoding model methodology
- [[brain-ai-alignment]]: Methods for aligning artificial and biological neural representations

## References
- Spiking Neural Networks for fMRI-Based Visual Semantic Decoding. arXiv:2607.19170
- SpikingJelly: A deep learning framework for Spiking Neural Networks
- Natural Scenes Dataset (NSD): High-resolution fMRI dataset for visual neuroscience
- GoD Dataset: Grounded Object Dataset for semantic decoding evaluation