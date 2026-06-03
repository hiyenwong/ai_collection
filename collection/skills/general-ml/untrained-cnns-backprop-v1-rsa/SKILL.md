---
name: untrained-cnns-backprop-v1-rsa
description: "Systematic RSA comparison showing untrained CNNs match backpropagation-trained CNNs in V1 visual cortex alignment. Large-scale fMRI analysis reveals that random feature detectors can capture V1 representational structure. Keywords: untrained CNN, V1 cortex, backpropagation, RSA, representational similarity, visual cortex, fMRI."
---

# Untrained CNNs Match Backpropagation at V1: A Systematic RSA Comparison

> Systematic comparison of four learning rules (backpropagation, random, Hebbian, STDP) reveals that untrained CNNs achieve comparable V1 representation alignment to backprop-trained models, challenging the necessity of extensive training for visual cortex modeling.

## Metadata
- **Source**: arXiv:2604.16875v1
- **Authors**: Nils Leutenegger
- **Published**: 2026-04-18
- **Category**: Computer Vision and Pattern Recognition (cs.CV)

## Core Methodology

### Key Innovation
The study challenges the assumption that backpropagation training is essential for CNNs to capture neural representations in V1. Using Representational Similarity Analysis (RSA) with 40,000 ImageNet samples and human fMRI data, it demonstrates that randomly initialized CNNs exhibit strikingly similar representational geometries to backpropagation-trained models specifically in early visual cortex (V1).

### Technical Framework

**1. Model Comparison Design**
- Four CNN architectures with different training paradigms:
  - **Backpropagation**: Standard supervised training on ImageNet
  - **Random**: Untrained, random weights (no learning)
  - **Hebbian**: Unsupervised Hebbian learning
  - **STDP**: Spike-timing dependent plasticity training

**2. Representational Similarity Analysis (RSA)**
- **Stimuli**: 40,000 ImageNet samples
- **Neural Data**: Human fMRI recordings from V1 visual cortex
- **Representational Dissimilarity Matrix (RDM)**: Pairwise comparison of neural/model responses
- **Similarity Metric**: Pearson correlation between model and neural RDMs

**3. Analysis Scope**
- Layer-wise comparison across CNN depth
- Comparison with established ventral stream models
- Correlation with behavioral metrics (human RT, accuracy)

## Key Findings

### 1. V1 Representation Parity
- Untrained CNNs show **statistically equivalent V1 alignment** to backpropagation-trained models
- No significant difference in representational geometry between random and trained weights in early layers

### 2. Architecture Over Training
- CNN architectural structure (convolution, pooling, hierarchical processing) appears more critical than learned weights for V1 modeling
- Random feature detectors capture sufficient V1 statistical structure

### 3. Generalization Across Rules
- Hebbian and STDP-trained CNNs also achieve competitive V1 alignment
- Suggests biological plausibility of alternative learning rules for visual cortex models

## Implementation Guide

### Prerequisites
- Python 3.8+
- PyTorch or TensorFlow for CNN implementation
- Nilearn or similar for fMRI analysis
- Scipy for RSA computations

### Step-by-Step RSA Comparison

**Step 1: Prepare CNN Models**
```python
import torch
import torchvision.models as models

# Load pretrained (backpropagation) model
pretrained_cnn = models.alexnet(pretrained=True)

# Create untrained (random) version
untrained_cnn = models.alexnet(pretrained=False)

# Alternative learning rules implementation
class HebbianCNN(torch.nn.Module):
    """CNN with Hebbian learning rule"""
    def hebbian_update(self, pre, post, lr=0.001):
        """Δw = η * pre * post"""
        delta_w = lr * torch.outer(pre.flatten(), post.flatten())
        return delta_w

class STDPCNN(torch.nn.Module):
    """CNN with STDP learning"""
    def stdp_update(self, pre_time, post_time, A_plus=0.01, A_minus=0.01, tau=20):
        """STDP: Δw = A₊ * exp(-Δt/τ) if Δt>0 else -A₋ * exp(Δt/τ)"""
        dt = post_time - pre_time
        if dt > 0:
            return A_plus * torch.exp(-dt / tau)
        else:
            return -A_minus * torch.exp(dt / tau)
```

**Step 2: Extract Representations**
```python
from collections import defaultdict
import numpy as np

def extract_layer_representations(model, dataloader, layer_names):
    """Extract activations from specified layers"""
    representations = defaultdict(list)
    
    def hook_fn(name):
        def hook(module, input, output):
            representations[name].append(output.detach().cpu().numpy())
        return hook
    
    # Register hooks
    hooks = []
    for name, module in model.named_modules():
        if name in layer_names:
            hooks.append(module.register_forward_hook(hook_fn(name)))
    
    # Forward pass
    model.eval()
    with torch.no_grad():
        for batch in dataloader:
            _ = model(batch)
    
    # Remove hooks
    for h in hooks:
        h.remove()
    
    return {k: np.vstack(v) for k, v in representations.items()}
```

**Step 3: Compute RDMs**
```python
from scipy.spatial.distance import pdist, squareform

def compute_rdm(representations, metric='correlation'):
    """
    Compute Representational Dissimilarity Matrix
    
    Args:
        representations: (n_samples, n_features) array
        metric: distance metric ('correlation', 'euclidean', 'cosine')
    
    Returns:
        rdm: (n_samples, n_samples) dissimilarity matrix
    """
    # Flatten representations if needed
    if representations.ndim > 2:
        representations = representations.reshape(representations.shape[0], -1)
    
    # Compute pairwise distances
    distances = pdist(representations, metric=metric)
    rdm = squareform(distances)
    
    return rdm
```

**Step 4: RSA Comparison**
```python
from scipy.stats import pearsonr

def rsa_comparison(model_rdm, neural_rdm, mask=None):
    """
    Compare model and neural RDMs
    
    Args:
        model_rdm: Model representational dissimilarity matrix
        neural_rdm: Neural (fMRI) RDM
        mask: Optional mask for upper triangle
    
    Returns:
        correlation: Pearson correlation between RDMs
        p_value: Statistical significance
    """
    if mask is None:
        # Use upper triangle (excluding diagonal)
        mask = np.triu(np.ones_like(model_rdm, dtype=bool), k=1)
    
    model_vec = model_rdm[mask]
    neural_vec = neural_rdm[mask]
    
    correlation, p_value = pearsonr(model_vec, neural_vec)
    
    return correlation, p_value

# Compare across models
results = {}
for model_name, model_rdms in all_model_rdms.items():
    for layer_name, rdm in model_rdms.items():
        corr, pval = rsa_comparison(rdm, fmri_rdm_v1)
        results[f"{model_name}_{layer_name}"] = {
            'correlation': corr,
            'p_value': pval
        }
```

**Step 5: Statistical Testing**
```python
from scipy import stats

def compare_learning_rules(results_dict):
    """
    Statistical comparison of different learning rules
    
    Args:
        results_dict: Dict with structure {model: {layer: {metric: value}}}
    
    Returns:
        comparison_table: DataFrame with statistical tests
    """
    import pandas as pd
    
    # Extract correlations for each learning rule
    backprop_corrs = [v['correlation'] for k, v in results_dict.items() 
                      if 'backprop' in k]
    random_corrs = [v['correlation'] for k, v in results_dict.items() 
                    if 'random' in k]
    
    # Paired t-test
    t_stat, p_val = stats.ttest_rel(backprop_corrs, random_corrs)
    
    # Effect size (Cohen's d)
    pooled_std = np.sqrt((np.std(backprop_corrs)**2 + np.std(random_corrs)**2) / 2)
    cohens_d = (np.mean(backprop_corrs) - np.mean(random_corrs)) / pooled_std
    
    return {
        't_statistic': t_stat,
        'p_value': p_val,
        'cohens_d': cohens_d,
        'backprop_mean': np.mean(backprop_corrs),
        'random_mean': np.mean(random_corrs)
    }
```

## Applications

### 1. Visual Cortex Modeling
- **Use case**: Develop biologically plausible vision models without extensive training
- **Benefit**: Reduced computational cost for neuroscience-inspired AI

### 2. Neural Network Interpretability
- **Use case**: Understand what CNNs learn vs. what is inherent in architecture
- **Benefit**: Disentangle architectural bias from learned representations

### 3. Brain-Computer Interfaces
- **Use case**: Build V1 decoders with minimal training data
- **Benefit**: Faster calibration for BCI systems

### 4. Efficient Model Design
- **Use case**: Design vision models for resource-constrained environments
- **Benefit**: Random weights may suffice for certain visual tasks

## Pitfalls

### 1. Limited to Early Visual Areas
- **Issue**: Results specific to V1; higher visual areas (IT, V4) show stronger training dependence
- **Mitigation**: Do not generalize to entire ventral stream

### 2. Task-Dependent Representations
- **Issue**: Untrained CNNs perform poorly on downstream tasks despite V1 alignment
- **Mitigation**: Distinguish representational similarity from functional performance

### 3. Dataset Bias
- **Issue**: ImageNet statistics may match natural image statistics that V1 is tuned for
- **Mitigation**: Test with diverse visual stimuli beyond ImageNet

### 4. Layer Depth Matters
- **Issue**: Later CNN layers show significant training effects
- **Mitigation**: Focus analysis on early-to-mid layer comparisons for V1 modeling

## Related Skills
- sparsity-neuromorphic-impulse-radio
- multiplication-free-spike-time-fpga
- conv-delay-learning-snn
- brain-inspired-capture-evidence-driven

## References
```bibtex
@article{leutenegger2026untrained,
  title={Untrained CNNs Match Backpropagation at V1: A Systematic RSA Comparison of Four Learning Rules Against Human fMRI},
  author={Leutenegger, Nils},
  journal={arXiv preprint arXiv:2604.16875},
  year={2026}
}
```
