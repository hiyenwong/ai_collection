---
name: untrained-cnns-match-backpropagation-v1-rsa
description: Systematic RSA comparison showing untrained CNNs match backpropagation-trained CNNs at V1 visual cortex. Use for understanding representational similarity, visual cortex modeling, and the role of training in neural network-brain alignment. Keywords: CNN, V1, RSA, untrained networks, backpropagation, representational similarity analysis, visual cortex.
---

# Untrained CNNs Match Backpropagation at V1: Systematic RSA Study

> Large-scale fMRI study reveals untrained CNNs achieve comparable representational similarity to V1 visual cortex as backpropagation-trained CNNs, challenging assumptions about the necessity of training for brain alignment.

## Metadata
- **Source**: arXiv:2604.16875v1
- **Authors**: Multiple neuroscience and ML researchers
- **Published**: 2026-04-18
- **Category**: Computational Neuroscience, Machine Learning

## Core Methodology

### Research Question
Do convolutional neural networks (CNNs) require task-specific training to align with biological visual processing in V1, or do architectural biases alone suffice?

### Methodology Framework
1. **Representational Similarity Analysis (RSA)**
   - Compare layer-wise representations of CNNs to human V1 fMRI responses
   - Use representational dissimilarity matrices (RDMs) to quantify alignment

2. **Network Variants Tested**
   - Untrained/randomly initialized CNNs
   - Backpropagation-trained CNNs on ImageNet
   - Various architectures (VGG, ResNet, etc.)

3. **Brain Data**
   - Large-scale fMRI recordings from human subjects viewing natural images
   - Focus on primary visual cortex (V1) responses

### Key Findings
- **Surprising Result**: Untrained CNNs achieve comparable RSA alignment to V1 as trained CNNs
- **Layer-wise Pattern**: Alignment peaks at intermediate layers for both trained and untrained networks
- **Architecture Matters**: Specific architectural choices (convolution, pooling) are more important than training for V1 alignment

## Implementation Guide

### Prerequisites
- Python with PyTorch or TensorFlow
- RSA libraries (e.g., rsatoolbox)
- Pretrained CNN models
- fMRI dataset (or synthetic V1 response data)

### Step-by-Step Analysis

1. **Extract Network Representations**
```python
import torch
import torchvision.models as models

# Load untrained and trained models
untrained_cnn = models.vgg16(pretrained=False)
trained_cnn = models.vgg16(pretrained=True)

# Extract activations from each layer
activations_untrained = extract_layer_activations(untrained_cnn, images)
activations_trained = extract_layer_activations(trained_cnn, images)
```

2. **Compute Representational Dissimilarity Matrices**
```python
from rsatoolbox.rdm import calc_rdm
from rsatoolbox.data import Dataset

# Create RDMs for each layer
rdm_untrained = calc_rdm(Dataset(activations_untrained))
rdm_trained = calc_rdm(Dataset(activations_trained))
rdm_v1 = calc_rdm(Dataset(v1_fmri_responses))
```

3. **Compare Representations**
```python
from scipy.stats import pearsonr

# Compute similarity between network and V1 RDMs
similarity_untrained = pearsonr(rdm_untrained, rdm_v1)[0]
similarity_trained = pearsonr(rdm_trained, rdm_v1)[0]

print(f"Untrained-V1 similarity: {similarity_untrained:.3f}")
print(f"Trained-V1 similarity: {similarity_trained:.3f}")
```

## Applications
- **Model Selection**: Evaluate CNN architectures for neuroscience research without expensive training
- **Biological Plausibility**: Study how architectural constraints shape visual representations
- **Efficient Brain Modeling**: Use untrained networks as baseline models for visual cortex
- **Understanding Learning**: Isolate the contribution of training from architecture in brain alignment

## Pitfalls
- **Beyond V1**: Results may not generalize to higher visual areas (V2, V4, IT)
- **Task Specificity**: Untrained networks may lack task-relevant features for specific visual tasks
- **Dataset Dependency**: Alignment metrics depend on stimulus set used for RSA
- **Correlation vs Causation**: RSA similarity doesn't imply identical computation

## Related Skills
- brain-inspired-snn-pattern-analysis
- neuroscience-of-transformers
- visual-imagery-decoding-fmri
- vlm-visual-cortex-alignment
