---
name: untrained-cnns-match-backprop-v1
description: "Systematic RSA comparison showing untrained CNNs match backpropagation-trained CNNs at V1 visual cortex. Trigger words: untrained CNN, backpropagation, RSA, V1, representational similarity"
---

# Untrained CNNs Match Backpropagation at V1: Systematic RSA Study

> Representational Similarity Analysis revealing that architectural constraints, not learning rules, primarily drive alignment between CNNs and early visual cortex (V1/V2).

## Metadata
- **Source**: arXiv:2604.16875v1
- **Authors**: Computational neuroscience researchers (2026)
- **Published**: 2026-04-18
- **Domain**: Computational Neuroscience, Neural Networks, Visual Cortex Modeling

## Core Methodology

### Key Finding
The study presents a systematic comparison of four learning rules—backpropagation (BP), feedback alignment (FA), predictive coding (PC), and spike-timing-dependent plasticity (STDP)—applied to identical convolutional architectures. The crucial finding: early visual alignment (V1/V2) is primarily architecture-driven rather than learning-rule dependent.

### Technical Framework

#### Learning Rules Compared
1. **Backpropagation (BP)**: Standard gradient descent with backward error propagation
2. **Feedback Alignment (FA)**: Fixed random feedback weights instead of symmetric backward pass
3. **Predictive Coding (PC)**: Bidirectional inference minimizing prediction error
4. **Spike-Timing-Dependent Plasticity (STDP)**: Hebbian-like learning based on spike timing

#### The Critical Baseline
- **Untrained Random-Weights CNN**: Weights initialized but not trained
- **Result**: Achieves rho = 0.071 with V1, matching or exceeding trained networks
- **Implication**: Architecture itself constrains representations to be V1-like

#### Representational Similarity Analysis (RSA)
- **Dataset**: THINGS-fMRI (720 stimuli, 3 subjects)
- **Brain Regions**: V1, V2, V3, V4, IT (visual hierarchy)
- **Metric**: Spearman correlation (rho) between CNN and brain RDMs

## Implementation Guide

### Prerequisites
- PyTorch for CNN implementations
- rsatoolbox for RSA computation
- Brain data (THINGS-fMRI or similar)
- scipy, numpy, matplotlib

### Step-by-Step

#### 1. CNN Architecture
```python
import torch
import torch.nn as nn

class SimpleCNN(nn.Module):
    """
    Architecture used in the study
    Multiple convolutional layers followed by fully connected
    """
    def __init__(self):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=7, stride=2, padding=3),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            
            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            
            nn.Conv2d(128, 256, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            
            nn.Conv2d(256, 512, kernel_size=3, padding=1),
            nn.ReLU(),
        )
        
        self.classifier = nn.Sequential(
            nn.AdaptiveAvgPool2d(1),
            nn.Flatten(),
            nn.Linear(512, 1000)
        )
    
    def forward(self, x, return_layer='conv4'):
        """Forward pass with intermediate feature extraction"""
        x = self.features(x)
        
        if return_layer == 'conv4':
            return x  # Return last conv layer features
        
        return self.classifier(x)
```

#### 2. Feedback Alignment Training
```python
class FeedbackAlignmentLinear(nn.Module):
    """Linear layer using fixed random feedback weights"""
    
    def __init__(self, in_features, out_features):
        super().__init__()
        self.in_features = in_features
        self.out_features = out_features
        
        # Forward weights (trainable)
        self.weight = nn.Parameter(torch.randn(out_features, in_features))
        self.bias = nn.Parameter(torch.zeros(out_features))
        
        # Feedback weights (fixed random)
        self.feedback = torch.randn(in_features, out_features)
        
    def forward(self, x):
        return torch.nn.functional.linear(x, self.weight, self.bias)
    
    def feedback_backward(self, grad_output):
        """Use fixed feedback weights for gradient computation"""
        return torch.matmul(grad_output, self.feedback.t())
```

#### 3. Representational Similarity Analysis
```python
import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.stats import spearmanr

def compute_rdm(features, metric='correlation'):
    """
    Compute Representational Dissimilarity Matrix
    
    Args:
        features: (n_stimuli, n_features) array
        metric: distance metric for RDM
    
    Returns:
        RDM: (n_stimuli, n_stimuli) dissimilarity matrix
    """
    # Compute pairwise distances
    distances = pdist(features, metric=metric)
    rdm = squareform(distances)
    return rdm

def compare_rdms(rdm1, rdm2):
    """
    Compare two RDMs using Spearman correlation
    
    Returns:
        rho: Spearman correlation coefficient
        pvalue: statistical significance
    """
    # Vectorize upper triangles (excluding diagonal)
    triu_idx = np.triu_indices_from(rdm1, k=1)
    v1 = rdm1[triu_idx]
    v2 = rdm2[triu_idx]
    
    rho, pvalue = spearmanr(v1, v2)
    return rho, pvalue
```

#### 4. Full Analysis Pipeline
```python
def evaluate_cnn_brain_alignment(model, brain_rdms, stimuli_loader, 
                                 layer_names=['conv1', 'conv2', 'conv3', 'conv4']):
    """
    Evaluate CNN alignment with multiple brain regions
    
    Args:
        model: CNN model
        brain_rdms: Dict of brain region RDMs {'V1': rdm, 'V2': rdm, ...}
        stimuli_loader: DataLoader for THINGS stimuli
        layer_names: CNN layers to evaluate
    
    Returns:
        alignment_scores: Dict of rho values
    """
    model.eval()
    
    # Extract CNN features for all stimuli
    all_features = {layer: [] for layer in layer_names}
    
    with torch.no_grad():
        for batch in stimuli_loader:
            images = batch['image']
            
            # Forward through model
            for layer in layer_names:
                features = model.extract_layer(images, layer)
                features = features.view(features.size(0), -1)
                all_features[layer].append(features.cpu().numpy())
    
    # Concatenate batches
    for layer in layer_names:
        all_features[layer] = np.concatenate(all_features[layer], axis=0)
    
    # Compare with brain RDMs
    alignment_scores = {}
    
    for layer in layer_names:
        cnn_rdm = compute_rdm(all_features[layer])
        
        for region, brain_rdm in brain_rdms.items():
            rho, pval = compare_rdms(cnn_rdm, brain_rdm)
            alignment_scores[f"{layer}_{region}"] = {
                'rho': rho,
                'pvalue': pval
            }
    
    return alignment_scores
```

## Key Results

### V1 Alignment (Early Visual)
| Model | Rho | Significance |
|-------|-----|--------------|
| Untrained Random | 0.071 | p < 0.001 |
| Backpropagation | 0.073 | p < 0.001 |
| Feedback Alignment | 0.070 | p < 0.001 |
| Predictive Coding | 0.069 | p < 0.001 |
| STDP | 0.068 | p < 0.001 |

**Interpretation**: No significant difference—architecture dominates at V1

### Higher Visual Areas (V4, IT)
- Training improves alignment substantially
- Backpropagation shows best performance
- Learning rule becomes important for complex representations

## Implications

### For Neuroscience
- **Architecture Matters Most**: CNN structure inherently matches early visual processing
- **Learning Refines**: Training improves higher-level representations
- **Model Selection**: Untrained CNNs sufficient for V1 modeling

### For Deep Learning
- **Inductive Bias**: Convolutions provide strong geometric priors
- **Weight Initialization**: Good initialization captures much of architecture's power
- **Training Efficiency**: Focus training on higher layers for transfer learning

## Pitfalls
- **Dataset Specificity**: Results from THINGS-fMRI may not generalize
- **Architecture Sensitivity**: Different CNN architectures may show different patterns
- **Subject Variability**: Individual brain differences affect alignment scores
- **Layer Definition**: Precise mapping of CNN layers to brain regions is challenging

## Related Skills
- primary-visual-cortex-v1-functions
- eeg-visual-attention-decoding
- vlm-visual-cortex-alignment-robustness
- neural-encoding-evaluation-ground-truth

## References
```
@article{untrained2026cnn,
  title={Untrained CNNs Match Backpropagation at V1: A Systematic RSA Comparison of Learning Rules},
  journal={arXiv preprint arXiv:2604.16875},
  year={2026}
}
```
