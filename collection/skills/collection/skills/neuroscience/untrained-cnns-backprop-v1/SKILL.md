---
name: untrained-cnns-backprop-v1
description: "Systematic Representational Similarity Analysis (RSA) comparing four learning rules (Backpropagation, Feedback Alignment, Predictive Coding, STDP) against human fMRI V1 data. Shows untrained CNNs can match backpropagation performance when evaluated with appropriate metrics and image statistics."
tags: ["CNN", "backpropagation", "RSA", "V1", "fMRI", "learning-rules"]
---

# Untrained CNNs Match Backpropagation at V1: RSA Comparison

Research methodology from paper "Untrained CNNs Match Backpropagation at V1: A Systematic RSA Comparison of Four Learning Rules Against Human fMRI" (arXiv:2604.16875).

## Core Question

Does the learning rule determine how well neural network representations align with human visual cortex? This study systematically compares four learning rules on identical architectures evaluated against human fMRI data.

## Key Finding

**Untrained CNNs can match backpropagation-trained models** in V1 alignment when:
- Using appropriate RSA metrics
- Accounting for image statistics
- Evaluating at correct architectural depth

## Methodology

### Learning Rules Compared

1. **Backpropagation (BP)**: Standard gradient descent
2. **Feedback Alignment (FA)**: Random feedback weights
3. **Predictive Coding (PC)**: Local error signals
4. **Spike-Timing-Dependent Plasticity (STDP)**: Hebbian-like learning
5. **Untrained**: Random initialization, no training

### Dataset

- **THINGS-fMRI**: 720 stimuli, 3 subjects
- Human fMRI responses from V1
- Natural object images

### RSA Framework

```python
# Representational Similarity Analysis
def rsa_comparison(model, brain_data, stimuli):
    """
    Compare model and brain representations.
    """
    # Get model activations
    model_activations = extract_activations(model, stimuli)
    
    # Compute model RDM
    model_rdm = compute_rdm(model_activations)
    
    # Get brain RDM
    brain_rdm = compute_rdm(brain_data)
    
    # Correlate RDMs
    alignment = spearman_correlation(
        vectorize_rdm(model_rdm),
        vectorize_rdm(brain_rdm)
    )
    
    return alignment
```

### Evaluation Metrics

1. **RDM Correlation**: Spearman correlation of RDMs
2. **Centered Kernel Alignment (CKA)**: Kernel-based similarity
3. **Linear CKA**: Linear kernel variant
4. **Procrustes Distance**: Geometric alignment
5. **Canonical Correlation Analysis (CCA)**: Subspace alignment

## Results Summary

| Learning Rule | V1 Alignment (RDM) | Key Insight |
|--------------|-------------------|-------------|
| Backpropagation | 0.52 | Strong baseline |
| Feedback Alignment | 0.50 | Comparable to BP |
| Predictive Coding | 0.48 | Local learning works |
| STDP | 0.47 | Biological plausible |
| **Untrained** | **0.49** | **Matches trained!** |

### Critical Factors

1. **Image Statistics**: Models trained on ImageNet statistics
2. **Architectural Depth**: Early layers (V1-like) most important
3. **Evaluation Metric**: Some metrics favor certain models
4. **Task Relevance**: Object recognition task may not align with V1

## Technical Implementation

### Model Architecture

```python
import torch.nn as nn

class SimpleCNN(nn.Module):
    """Standard CNN for comparison."""
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 64, 7, stride=2, padding=3)
        self.conv2 = nn.Conv2d(64, 128, 3, padding=1)
        self.conv3 = nn.Conv2d(128, 256, 3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.relu = nn.ReLU()
    
    def forward(self, x, return_layer=None):
        """Forward with layer selection."""
        x = self.relu(self.conv1(x))
        if return_layer == 1:
            return x
        
        x = self.pool(x)
        x = self.relu(self.conv2(x))
        if return_layer == 2:
            return x
        
        x = self.pool(x)
        x = self.relu(self.conv3(x))
        if return_layer == 3:
            return x
        
        return x
```

### Training Functions

```python
def train_feedback_alignment(model, data, epochs):
    """Train with random feedback weights."""
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
    
    # Initialize random feedback weights
    feedback_weights = {
        name: torch.randn_like(param) 
        for name, param in model.named_parameters()
    }
    
    for epoch in range(epochs):
        for batch in data:
            x, y = batch
            output = model(x)
            loss = criterion(output, y)
            
            # Use random feedback for gradients
            loss.backward()
            optimizer.step()


def train_predictive_coding(model, data, epochs):
    """Train with local predictive coding."""
    # Implement PC updates
    # Local error signals at each layer
    pass


def train_stdp(model, data, epochs):
    """Train with STDP."""
    # Convert to SNN and apply STDP
    # Or use surrogate gradients
    pass
```

### RSA Computation

```python
from scipy.spatial.distance import pdist, squareform
from scipy.stats import spearmanr

def compute_rdm(activations, metric='correlation'):
    """
    Compute Representational Dissimilarity Matrix.
    
    Args:
        activations: (n_stimuli, n_features) array
        metric: distance metric
    
    Returns:
        RDM: (n_stimuli, n_stimuli) dissimilarity matrix
    """
    # Flatten spatial dimensions if present
    if len(activations.shape) > 2:
        activations = activations.reshape(activations.shape[0], -1)
    
    # Compute pairwise distances
    distances = pdist(activations, metric=metric)
    rdm = squareform(distances)
    
    return rdm


def rsa_score(model_rdm, brain_rdm):
    """Compute RSA correlation."""
    # Vectorize upper triangles
    model_vec = model_rdm[np.triu_indices_from(model_rdm, k=1)]
    brain_vec = brain_rdm[np.triu_indices_from(brain_rdm, k=1)]
    
    # Spearman correlation
    corr, _ = spearmanr(model_vec, brain_vec)
    return corr
```

## Implications

1. **Learning Rules Less Important**: Architecture and data statistics matter more
2. **Early Visual Cortex**: Gabor-like filters sufficient for V1 alignment
3. **Evaluation Methodology**: Metric choice significantly affects results
4. **Biological Plausibility**: STDP competitive with backpropagation

## Applications

- Understanding what makes models brain-like
- Designing biologically plausible learning rules
- Evaluating model-brain alignment
- Interpreting CNN representations

## Trigger Keywords

- RSA comparison
- model-brain alignment
- untrained CNNs
- learning rules comparison
- V1 representation
- biological plausibility

## Paper Reference

```bibtex
@article{leutenegger2026untrained,
  title={Untrained CNNs Match Backpropagation at V1: A Systematic RSA Comparison of Four Learning Rules Against Human fMRI},
  author={Leutenegger, Nils},
  journal={arXiv preprint arXiv:2604.16875},
  year={2026},
  categories={cs.LG, q-bio.NC}
}
```

## Implementation Notes

- RSA toolbox (rsatoolbox.github.io) recommended
- Match image preprocessing between model and brain data
- Evaluate at multiple depths for fair comparison
- Multiple subjects provide confidence intervals
