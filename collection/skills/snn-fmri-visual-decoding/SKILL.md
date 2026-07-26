---
name: snn-fmri-visual-decoding
version: 1.0.0
description: Spiking Neural Networks for fMRI-Based Visual Semantic Decoding - methodology for using SNN-derived visual features as alternative targets for fMRI-based visual decoding, demonstrating stronger alignment with fMRI responses and improved visual semantic decoding performance compared to ANN-derived features.
author: Jiahong Zhang, Jinning Zhao, Sijun Shen, Siyuan Xu, Bo Xu, Guoqi Li
license: arXiv.org perpetual non-exclusive license
arxiv_id: 2607.19170
date_added: 2026-07-23
categories:
  - neuroscience
  - computational-neuroscience
  - brain-computer-interface
  - spiking-neural-networks
  - fmri-decoding
---

# Spiking Neural Networks for fMRI-Based Visual Semantic Decoding

## Overview

This skill implements the methodology from the paper "Spiking Neural Networks for fMRI-Based Visual Semantic Decoding" (arXiv:2607.19170) which demonstrates that **SNN-derived visual features provide superior targets for fMRI-based visual decoding** compared to conventional ANN-derived features. The key insight is treating the target visual representation as a scientific variable rather than just an engineering choice.

## Key Findings

- **Stronger fMRI alignment**: SNN representations better correspond to measured brain responses than ANN representations
- **Improved feature prediction**: On GoD dataset, SNN-derived features reduce feature-prediction error from 0.7707 to 0.0282
- **Enhanced semantic decoding**: Top-1 semantic decoding accuracy improves from 0.1800 to 0.4400 on GoD dataset
- **Multiple SNN variants tested**: LIF, PSN, MPSN, and BuSNN all show advantages over ANN baseline
- **Temporal dynamics matter**: Both spiking neural dynamics and temporal simulation steps contribute to observed advantages

## Methodology

### Problem Formulation

The framework treats fMRI-based visual semantic decoding as mapping brain activity into visual features:

1. **Stimulus processing**: Same images processed by either ANN or SNN feature extractors
   - ANN features: dense and static (ResNet-18 backbone)
   - SNN features: spike-based and temporally dynamic (SEW-ResNet-18 variants)

2. **Controlled comparison**: Same L2-regularized linear fMRI-to-feature decoder used for all models
   - Only feature vectors used as regression targets are varied
   - Decoder form, input preprocessing, and training protocol kept fixed

3. **Evaluation protocol**: Multi-level assessment including:
   - Voxel-level alignment (PCC analysis)
   - Semantic-level alignment 
   - Semantic classification
   - Image retrieval (fMRI-to-image)
   - Semantic-guided reconstruction

### SNN Variants

Four spiking neuron variants were evaluated under the same SEW-ResNet-18 backbone:

- **LIF (Leaky Integrate-and-Fire)**: Classical membrane integration
- **PSN (Parallel Spiking Neuron)**: Parallel temporal computation  
- **MPSN (Memory-based Parallel Spiking Neuron)**: Explicit memory propagation
- **BuSNN (Bursting Spiking Neuron)**: Burst-like spike coding

### Feature Extraction

For SNNs, features are obtained through temporal averaging of spike responses:

```
SNN_feature = (1/T) * Σ(t=1 to T) SNN_response(t)
```

Where T is the number of discrete time steps for temporal simulation.

## Implementation Steps

### 1. Setup Environment
```python
# Install required dependencies
pip install torch torchvision numpy scipy scikit-learn
# For SNN training frameworks
pip install spikingjelly  # or other SNN libraries
```

### 2. Prepare Visual Encoders
- Use ResNet-18 as ANN baseline (pretrained on ImageNet)
- Use SEW-ResNet-18 variants for SNN models (same architecture family)
- Keep encoders fixed during fMRI decoder training

### 3. Extract Target Features
```python
# For ANN
ann_features = resnet18_backbone(image)

# For SNN  
snn_responses = []
for t in range(T):  # T time steps
    spike_response = sew_resnet18(image, timestep=t)
    snn_responses.append(spike_response)
snn_features = torch.mean(torch.stack(snn_responses), dim=0)
```

### 4. Train fMRI-to-Feature Decoder
```python
from sklearn.linear_model import Ridge

# Same decoder for all models
decoder = Ridge(alpha=1.0)  # L2 regularization
decoder.fit(fmri_responses_train, target_features_train)
```

### 5. Evaluate Performance
- **Feature prediction error**: MSE between predicted and actual features
- **Semantic decoding accuracy**: Top-k classification accuracy
- **Retrieval performance**: Acc@K for fMRI-to-image retrieval
- **Reconstruction quality**: Best-of-five semantic reconstruction score

## Datasets and Benchmarks

### Primary Datasets
- **GoD (Generic Object Decoding)**: Main evaluation dataset
- **NSD (Natural Scenes Dataset)**: Cross-dataset validation
- **Mini-Algonauts 2021**: Voxel-level alignment analysis

### Evaluation Metrics
- **Feature prediction error**: Lower is better (MSE)
- **Top-1 semantic accuracy**: Higher is better
- **Acc@K retrieval**: Higher is better
- **Reconstruction score**: Higher is better (combines feature similarity, ranking consistency, category consistency)

## Results Summary

| Model | Feature Prediction Error (GoD) | Top-1 Accuracy (GoD) | Acc@1 Retrieval (GoD) |
|-------|-------------------------------|---------------------|----------------------|
| ANN   | 0.7707                        | 0.1800              | 0.44                 |
| LIF   | 0.0282                        | 0.4400              | 0.40                 |
| PSN   | -                             | -                   | **0.58**             |
| MPSN  | -                             | -                   | 0.52                 |
| BuSNN | -                             | -                   | 0.56                 |

## Applications

### Brain-Computer Interfaces
- Improved visual decoding for communication restoration
- Better alignment between neural measurements and computational models
- Enhanced semantic information recovery from fMRI signals

### Neuroscience Research
- Testing hypotheses about neural representation formats
- Understanding what makes visual features "brain-decodable"
- Bridging computational neuroscience and neuroimaging

### AI Model Development
- Designing brain-inspired visual representations
- Evaluating neural network architectures from a neuroscience perspective
- Developing more interpretable AI systems

## Limitations and Considerations

### Technical Limitations
- Uses same decoder across all features (more expressive decoders could improve absolute performance)
- Focuses on matched ANN/SNN backbones (broader architectural comparisons needed)
- Reconstruction based on semantic guidance rather than direct pixel-level reconstruction

### Interpretation Caveats
- Results don't imply fMRI directly measures biological spikes
- SNN advantage suggests sparse, temporally structured representations better match BOLD measurement characteristics
- BOLD signals reflect synaptic and local population processing more than spiking output alone

## Future Directions

1. **Extended model comparisons**: Test against vision transformers, multimodal models
2. **Advanced decoders**: Develop subject-specific, more expressive decoding models
3. **Direct reconstruction**: Combine with stronger generative models for pixel-level reconstruction
4. **Human evaluation**: Include perceptual quality assessment of reconstructed images
5. **Cross-modal applications**: Extend to other neuroimaging modalities (EEG, MEG)

## Activation Keywords

Use this skill when working with:
- fMRI visual decoding
- brain-computer interfaces
- spiking neural networks
- neural representation alignment
- visual semantic decoding
- brain-inspired AI
- computational neuroscience
- neuroimaging analysis

## References

- Zhang, J., Zhao, J., Shen, S., Xu, S., Xu, B., & Li, G. (2026). Spiking Neural Networks for fMRI-Based Visual Semantic Decoding. arXiv:2607.19170 [cs.NE].
- Related work on fMRI decoding: [13, 18, 1]
- SNN training frameworks: [11, 12, 51, 50]
- Neuroimaging fundamentals: [25, 24, 33]

## Code Availability

The original authors state: "The code will be released upon publication." Check the arXiv page for updates on code availability.