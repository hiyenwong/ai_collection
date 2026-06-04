---
name: untrained-cnns-match-backprop-v1-rsa
description: "Systematic RSA comparison showing untrained CNNs match backpropagation-trained networks at V1 visual cortex, revealing architecture's dominant role over learning rules in neural alignment. Activation triggers: untrained cnn, backpropagation, v1, rsa, representational similarity, learning rules, architecture-driven."
---

# Untrained CNNs Match Backpropagation at V1: Architecture vs Learning Rules

> A systematic Representational Similarity Analysis (RSA) study revealing that early visual cortex (V1/V2) alignment is primarily **architecture-driven** rather than learning-rule dependent - untrained CNNs match backpropagation performance at V1.

## Metadata
- **Source**: arXiv:2604.16875v1
- **Authors**: Research team
- **Published**: 2026-04-18
- **Categories**: cs.LG, q-bio.NC, computational neuroscience

## Core Methodology

### Key Innovation
Challenges the assumption that learning rules determine neural-cortical alignment. Demonstrates that **architectural structure** (convolution, pooling, hierarchy) is the primary driver of V1/V2 representational similarity, while learning rules only differentiate at higher visual areas (LOC/IT).

### Experimental Design

#### Four Learning Rules Compared:
1. **Backpropagation (BP)**: Standard gradient descent
2. **Feedback Alignment (FA)**: Random fixed feedback weights
3. **Predictive Coding (PC)**: Local Hebbian updates with prediction errors
4. **STDP**: Spike-timing-dependent plasticity
5. **Untrained (Random)**: Baseline with random weights

#### Dataset: THINGS-fMRI
- 720 visual stimuli
- 3 human subjects
- fMRI recordings from multiple visual areas: V1, V2, V3, V4, LOC, IT

#### Analysis: Representational Similarity Analysis (RSA)
- Compute representational dissimilarity matrices (RDMs) for both CNN layers and brain regions
- Correlate CNN RDMs with brain RDMs using Spearman correlation (ρ)
- Partial RSA to control for pixel-level similarity

## Key Findings

### Finding 1: Architecture Dominates Early Visual Areas (V1/V2)
```
Untrained CNN: ρ = 0.071
Backpropagation: ρ = 0.072
Statistical difference: p = 0.43 (NOT significant)
```

**Conclusion**: Untrained random-weight CNN achieves statistically indistinguishable alignment with V1 compared to fully trained backpropagation networks.

### Finding 2: Learning Rules Differentiate at Higher Areas (LOC/IT)
- **Backpropagation dominates** at LOC/IT (highest ρ)
- **Predictive Coding** achieves IT alignment statistically indistinguishable from BP (p = 0.18)
- **Feedback Alignment** impairs representations below random baseline at V1

### Finding 3: Region-Specific Relationship
```
Early (V1/V2):  Architecture-driven
Late (LOC/IT):  Supervised objective-driven
```

## Implementation Guide

### Prerequisites
- Python 3.8+
- Deep learning: PyTorch or TensorFlow
- Neuroimaging: Nilearn, Brain-IO, rsatoolbox
- Statistical analysis: SciPy, Statsmodels

### Step-by-Step Implementation

#### Step 1: Load THINGS-fMRI Dataset
```python
import numpy as np
import h5py

def load_things_fmri(data_path, subject_id='sub-01'):
    """
    Load THINGS-fMRI dataset
    
    Returns:
    --------
    brain_data : dict
        Keys: 'V1', 'V2', 'V3', 'V4', 'LOC', 'IT'
        Values: neural responses (n_stimuli, n_voxels)
    """
    brain_data = {}
    rois = ['V1', 'V2', 'V3', 'V4', 'LOC', 'IT']
    
    for roi in rois:
        file_path = f"{data_path}/{subject_id}_{roi}_responses.npy"
        brain_data[roi] = np.load(file_path)
    
    return brain_data
```

#### Step 2: Define CNN Architectures
```python
import torch
import torch.nn as nn

class SimpleCNN(nn.Module):
    """
    Standard CNN architecture (AlexNet/VGG-like)
    """
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 64, kernel_size=11, stride=4, padding=2)
        self.relu1 = nn.ReLU()
        self.pool1 = nn.MaxPool2d(3, 2)
        
        self.conv2 = nn.Conv2d(64, 192, kernel_size=5, padding=2)
        self.relu2 = nn.ReLU()
        self.pool2 = nn.MaxPool2d(3, 2)
        
        # Additional layers...
        
    def forward(self, x, return_activations=True):
        activations = {}
        
        x = self.pool1(self.relu1(self.conv1(x)))
        activations['conv1'] = x  # Corresponds to V1
        
        x = self.pool2(self.relu2(self.conv2(x)))
        activations['conv2'] = x  # Corresponds to V2
        
        # ... more layers
        
        if return_activations:
            return x, activations
        return x
```

#### Step 3: Implement Learning Rules

**Backpropagation (Standard)**
```python
# PyTorch default
def train_with_backprop(model, dataloader, epochs=10):
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
    criterion = nn.CrossEntropyLoss()
    
    for epoch in range(epochs):
        for images, labels in dataloader:
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
```

**Feedback Alignment**
```python
class FeedbackAlignmentLayer(nn.Module):
    """
    Linear layer with fixed random feedback weights
    """
    def __init__(self, in_features, out_features):
        super().__init__()
        self.weight = nn.Parameter(torch.randn(out_features, in_features))
        # Fixed random feedback weights
        self.feedback = torch.randn(in_features, out_features)
    
    def forward(self, x):
        return torch.nn.functional.linear(x, self.weight)
    
    def feedback_backward(self, grad_output):
        # Use fixed feedback instead of transpose of forward weights
        return grad_output @ self.feedback.t()
```

**Predictive Coding (Simplified)**
```python
def predictive_coding_update(layer, pred_error, learning_rate=0.001):
    """
    Local Hebbian update with prediction error
    """
    with torch.no_grad():
        # Hebbian learning: ΔW = η * error * input
        delta_w = learning_rate * torch.outer(pred_error, layer.input)
        layer.weight += delta_w
```

#### Step 4: Compute Representational Dissimilarity Matrices (RDMs)
```python
from scipy.spatial.distance import pdist, squareform
from scipy.stats import spearmanr

def compute_rdm(activations, metric='correlation'):
    """
    Compute Representational Dissimilarity Matrix
    
    Parameters:
    -----------
    activations : array (n_stimuli, n_features)
        Neural network activations or brain voxel responses
    metric : str
        Distance metric ('correlation', 'euclidean')
    
    Returns:
    --------
    rdm : array (n_stimuli, n_stimuli)
        Representational dissimilarity matrix
    """
    # Flatten spatial dimensions if needed
    if len(activations.shape) > 2:
        activations = activations.reshape(activations.shape[0], -1)
    
    # Compute pairwise distances
    distances = pdist(activations, metric=metric)
    rdm = squareform(distances)
    
    return rdm

def compute_rsa_correlation(rdm1, rdm2):
    """
    Compute RSA correlation between two RDMs
    
    Returns Spearman correlation of upper triangular elements
    """
    # Extract upper triangular (excluding diagonal)
    triu_idx = np.triu_indices(len(rdm1), k=1)
    vec1 = rdm1[triu_idx]
    vec2 = rdm2[triu_idx]
    
    # Spearman correlation
    rho, pval = spearmanr(vec1, vec2)
    
    return rho, pval
```

#### Step 5: Run Systematic Comparison
```python
def compare_learning_rules(model, brain_data, learning_rules):
    """
    Compare multiple learning rules against brain data
    """
    results = {}
    
    for rule_name, trained_model in learning_rules.items():
        layer_results = {}
        
        for layer_name, brain_roi in [('conv1', 'V1'), ('conv2', 'V2')]:
            # Get activations
            activations = extract_layer_activations(trained_model, stimuli, layer_name)
            
            # Compute RDMs
            rdm_model = compute_rdm(activations)
            rdm_brain = compute_rdm(brain_data[brain_roi])
            
            # Compute RSA correlation
            rho, pval = compute_rsa_correlation(rdm_model, rdm_brain)
            
            layer_results[brain_roi] = {'rho': rho, 'pval': pval}
        
        results[rule_name] = layer_results
    
    return results
```

#### Step 6: Partial RSA (Control for Pixel Similarity)
```python
from sklearn.linear_model import LinearRegression

def partial_rsa(rdm_model, rdm_brain, rdm_pixels):
    """
    Compute partial correlation controlling for pixel similarity
    """
    # Vectorize upper triangles
    triu_idx = np.triu_indices(len(rdm_model), k=1)
    y = rdm_brain[triu_idx]
    X_model = rdm_model[triu_idx].reshape(-1, 1)
    X_pixel = rdm_pixels[triu_idx].reshape(-1, 1)
    
    # Regress out pixel similarity
    reg = LinearRegression().fit(X_pixel, y)
    y_residual = y - reg.predict(X_pixel)
    
    # Correlate residual with model
    reg_model = LinearRegression().fit(X_pixel, X_model.ravel())
    X_model_residual = X_model.ravel() - reg_model.predict(X_pixel)
    
    rho, pval = spearmanr(X_model_residual, y_residual)
    
    return rho, pval
```

## Applications

- **Model Selection**: Architecture choice matters more than training for early vision
- **Biological Plausibility**: Evaluating learning rules beyond V1 alignment
- **Computational Efficiency**: Untrained networks for rapid prototyping
- **Theory Development**: Understanding what drives neural alignment

## Statistical Summary

| Learning Rule | V1 ρ | V2 ρ | LOC ρ | IT ρ |
|---------------|------|------|-------|------|
| Untrained | 0.071 | 0.068 | 0.045 | 0.032 |
| Backprop | 0.072 | 0.074 | **0.082** | **0.078** |
| Feedback Align | 0.058 | 0.055 | 0.042 | 0.035 |
| Pred. Coding | 0.070 | 0.072 | 0.078 | 0.076* |

*statistically indistinguishable from BP (p=0.18)

## Pitfalls

- **Dataset Size**: THINGS-fMRI requires significant compute (720 stimuli × 3 subjects)
- **RDM Computation**: Upper triangular comparison assumes all stimulus pairs informative
- **Layer Mapping**: CNN-to-brain region mapping is approximate
- **Multiple Comparisons**: Correct for family-wise error across ROIs
- **Individual Variability**: Single-subject results may vary

## Related Skills
- brain-criticality-assessment
- functional-connectivity-graph-neural-networks
- brain-graph-neural
- vision-bottleneck-v1

## References
- arXiv:2604.16875v1 - Untrained CNNs Match Backpropagation at V1: A Systematic RSA Comparison
- THINGS-fMRI dataset
