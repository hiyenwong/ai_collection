---
name: phase-importance-neural-representations-oppenheim-lim
description: Causal intervention methodology testing Oppenheim-Lim phase importance asymmetry in deep neural network representations. Phase/sign carries identity while magnitude dispensable; mechanistic explanation for texture-shape gap between CNNs and attention models.
category: ai_collection
created: 2026-06-17
source: arXiv:2606.17037v1
authors: Alper Yıldırım
published: 2026-06-15
---

# Phase Importance in Neural Representations: Oppenheim-Lim Test

## Overview

Classic neuroscience finding (Oppenheim & Lim, 1981): Natural images stay recognizable when reconstructed from Fourier **phase alone**, while magnitude carries little identity. This paper tests whether deep neural networks reproduce this asymmetry **internally** in their hidden representations through causal intervention experiments.

## Key Contributions

1. **Internal Oppenheim-Lim Test**: Novel methodology for probing phase/magnitude importance in neural network hidden layers via causal intervention
2. **Phase-Identity Code Discovery**: Evidence that identity rides on phase/sign while magnitude is largely dispensable for readout
3. **Architecture Comparison**: Mechanistic account of texture-shape gap between CNNs and attention models (ViT/GFNet vs ResNet)
4. **Different Exposure Bases**: Architectures share phase identity code but expose it in different bases (rectification + readout geometry)

## Core Methodology

### Causal Phase-Magnitude Transplant
- Given two images A and B
- Transplant phase of A onto magnitude of B at chosen layer
- Record which image prediction follows (phase donor or magnitude donor?)
- In PRISM2D, GFNet, ViT-B/16: prediction follows **phase/sign donor**

### Intervention Types
1. **Sign Transplant**: Binary sign transplantation (valid after ReLU)
2. **Phase Transplant**: Full phase transplantation (before ReLU)
3. **Magnitude Deletion**: Delete all image-specific magnitude
   - Barely moves accuracy → magnitude dispensable
4. **DC-Only Control**: Channel-wise spatial average consumed by readout

### Key Finding Across Architectures

| Architecture | Phase/Sign Code Location | Magnitude Importance |
|--------------|--------------------------|----------------------|
| ViT-B/16 | Late blocks | Low (dispensable) |
| GFNet | Late blocks | Low |
| PRISM2D | Late blocks | Low |
| ResNet-50 | **Before ReLU** (latent) | High spatial average |

ResNet-50 initially appears to break pattern (sign transplant after ReLU does nothing), but **fair intervention before ReLU** reveals strong latent sign code in late blocks.

## Neuroscience Connection

### Oppenheim-Lim Asymmetry (1981)
- Fourier phase → recognizable image (carries identity)
- Fourier magnitude → unrecognizable (little identity)

### Neural Network Analogy
- Hidden representations reproduce this asymmetry
- Phase/sign carries identity information
- Magnitude largely dispensable for classification decisions
- Different bases for exposure (rectification geometry)

## Mechanistic Insights

### Texture-Shape Gap Explanation
- CNNs (ResNet): Heavy reliance on texture (magnitude-dependent processing)
- Attention models (ViT/GFNet): Shape-focused (phase-dependent processing)
- Phase/sign code exposed in different bases depending on:
  1. **Rectification**: ReLU clips sign information
  2. **Readout geometry**: Spatial average vs position-specific

### Why Different Bases Matter
- ResNet: ReLU destroys sign → need intervention **before** ReLU
- ViT/GFNet: No ReLU → sign directly accessible in late blocks
- Readout location determines whether magnitude consumed

## Activation Words

**Primary**: neural representations, phase magnitude, oppenheim-lim, internal test, texture shape gap, mechanistic interpretability, visual representation, Fourier phase, deep learning interpretability

**Related**: neural encoding, visual cortex, representation learning, activation analysis, feature visualization, CNN interpretability, ViT interpretability, causality intervention, phase encoding

## Applications

### When to Use
- Probing internal representation structure in vision models
- Comparing CNN vs attention model representation bases
- Analyzing phase/magnitude information flow
- Understanding texture-shape bias in classifiers
- Causal intervention for interpretability research

### Methodology Template
```python
# Phase-Magnitude Transplant Experiment
def phase_transplant_experiment(model, image_A, image_B, layer_idx):
    """
    Causal intervention: transplant phase of A onto magnitude of B
    """
    # Extract features at layer
    feat_A = model.forward_to_layer(image_A, layer_idx)
    feat_B = model.forward_to_layer(image_B, layer_idx)
    
    # Fourier decomposition
    mag_A, phase_A = torch.fft.fft2(feat_A).abs(), torch.fft.fft2(feat_A).angle()
    mag_B, phase_B = torch.fft.fft2(feat_B).abs(), torch.fft.fft2(feat_B).angle()
    
    # Transplant: phase_A + magnitude_B
    transplanted = mag_B * torch.exp(1j * phase_A)
    reconstructed = torch.fft.ifft2(transplanted).real
    
    # Continue forward pass
    prediction = model.forward_from_layer(reconstructed, layer_idx)
    
    return prediction  # Should follow image_A (phase donor)
```

## Related Skills

- `mechanistic-interpretability-sae` - Sparse autoencoders for feature analysis
- `representation-geometry-transformer` - Geometric analysis of representations
- `activation-analysis-neural-network` - General activation probing methods
- `visual-cortex-alignment` - Brain-DNN alignment frameworks
- `texture-shape-bias-cnn` - Texture vs shape bias analysis

## Key Papers

1. Oppenheim, A. V., & Lim, J. S. (1981). "The importance of phase in signals"
2. Geirhos et al. (2018). "Generalisation in humans and deep neural networks"
3. Hermann et al. (2020). "The origins of texture bias in CNNs"

## Future Directions

1. **Phase preservation in training**: Design architectures that explicitly preserve phase
2. **Brain phase encoding**: Test whether visual cortex similarly relies on phase
3. **Cross-modal phase transfer**: Phase importance in audio/text representations
4. **Phase-aware regularization**: Loss functions penalizing phase corruption

---

## Summary

**Core thesis**: Deep neural networks reproduce Oppenheim-Lim asymmetry internally—identity rides on phase/sign, magnitude is dispensable. Different architectures expose this code in different bases (rectification geometry), providing mechanistic explanation for texture-shape gap between CNNs and attention models.

**Methodology**: Causal phase-magnitude transplantation at hidden layers + sign/phase interventions + magnitude deletion controls.

**Impact**: Bridges classic signal processing insight (phase importance) with modern mechanistic interpretability, offering causal probing framework for representation structure analysis.