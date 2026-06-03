---
name: misalignment-backpropagation-brain-hierarchy
description: Backpropagation gradient vs brain hierarchy alignment analysis using fMRI+MEG. Reveals fundamental misalignment between deep learning gradients and biological learning mechanisms.
category: neuroscience
tags: [backpropagation, brain-alignment, fMRI, MEG, DINOv3, vision-models, gradient-analysis, cortical-hierarchy]
activation_keywords: [backpropagation, brain hierarchy, gradient alignment, fMRI, MEG, DINOv3, vision cortex, learning mechanism, deep learning neuroscience]
arxiv_id: 2605.28693v1
authors: Joséphine Raugel, Maximilian Seitzer, Marc Szafraniec, Huy V. Vo, Jérémy Rapin, Patrick Labatut, Piotr Bojanowski, Valentin Wyart, Jean-Rémi King
published: 2026-05-27
---

# Misalignment Between Backpropagation and Brain Hierarchy

## Overview

This skill implements the methodology from arXiv:2605.28693v1 - analyzing the alignment between **backpropagated gradients** in deep neural networks and the **spatial-temporal hierarchy** of human brain responses to natural images, revealing fundamental misalignment suggesting different learning mechanisms.

## Core Discovery

**Key Finding:** Although backpropagated gradients can reliably predict fMRI and MEG signals in higher-level visual cortex and later latencies, their **spatial and temporal organization diverges** from patterns expected under a biologically plausible backpropagation mechanism.

## Methodology

### 1. Gradient-Based Encoding Analysis

**Extending Standard Encoding:**

Traditional encoding analysis maps **forward activations** to neural data. This study extends it to map **backpropagated gradients**.

```python
# Standard encoding: forward activation -> neural response
forward_alignment = RSA(model_activations, brain_responses)

# Extended encoding: backpropagated gradient -> neural response
gradient_alignment = RSA(backprop_gradients, brain_responses)
```

### 2. Brain Data Sources

**Dual-Modality Recording:**

- **fMRI**: Spatial brain responses (whole-cortex)
- **MEG**: Temporal brain responses (millisecond resolution)
- Stimulus: Natural images (varied visual content)

### 3. Vision Models Tested

**Primary Model:**
- **DINOv3**: Self-supervised vision transformer

**Reproduction on 8 vision models:**
- ResNet variants
- Vision Transformers (ViT)
- Self-supervised models
- Supervised models

## Key Results

### 1. Gradient Predicts Brain Signals

**Where gradients predict activity:**
- **Higher-level visual cortex**: Later stages of visual processing
- **Later latencies**: Delayed temporal responses (MEG)

**Performance:**
- Gradients reliably predict fMRI signals
- Gradients reliably predict MEG signals
- Specific to high-level visual areas

### 2. Spatial-Temporal Misalignment

**The Critical Discovery:**

**Expected (under biologically plausible BP):**
- Gradients computed in reverse order of cortical hierarchy
- Spatial organization follows cortical processing stages

**Observed:**
- **Order of gradient computation diverges** from cortical hierarchy
- **Spatial organization diverges** from temporal hierarchy
- **Fundamental mismatch** with brain structure

### 3. Forward vs Gradient Comparison

| Aspect | Forward Activations | Backpropagated Gradients |
|--------|-------------------|-------------------------|
| Cortical mapping | Reliable | Reliable (high-level only) |
| Temporal alignment | Matches hierarchy | Diverges from hierarchy |
| Spatial alignment | Follows visual stream | Different organization |
| Biological plausibility | Partially aligned | Misaligned |

## Implications

### 1. Different Learning Mechanisms

**Conclusion from study:**
> "Deep networks and the brain may share similar **representational content**, but they likely rely on **fundamentally different mechanisms** to learn those representations."

**Key Points:**
- **Representation similarity** ≠ **Mechanism similarity**
- Forward activations map onto cortex
- Gradients don't follow biological patterns
- Learning algorithms differ fundamentally

### 2. Backpropagation Question

**Open Question Revisited:**
- Is backpropagation implemented in the brain?
- This study: **Probably not in a straightforward way**
- Evidence: Gradient organization ≠ cortical hierarchy

### 3. Alternative Learning Mechanisms

**Potential Biological Alternatives:**
- Predictive coding
- Hebbian learning
- Spike-timing dependent plasticity (STDP)
- Feedback alignment
- Target propagation

## Implementation Guide

### Step 1: Extract Backpropagated Gradients

```python
# Example: extracting gradients for encoding analysis
import torch

def extract_gradients(model, input_image, target_output):
    """
    Extract backpropagated gradients for encoding analysis.
    
    Args:
        model: Vision model (e.g., DINOv3)
        input_image: Input stimulus
        target_output: Target for gradient computation
    
    Returns:
        layer_gradients: Dict of gradient tensors per layer
    """
    # Forward pass
    output = model(input_image)
    
    # Compute loss (e.g., reconstruction, classification)
    loss = compute_loss(output, target_output)
    
    # Backward pass
    loss.backward()
    
    # Extract gradients per layer
    layer_gradients = {}
    for name, param in model.named_parameters():
        if param.grad is not None:
            layer_gradients[name] = param.grad.detach()
    
    return layer_gradients
```

### Step 2: Gradient Encoding Analysis

```python
# Representational Similarity Analysis (RSA) for gradients

def gradient_rsa(gradients_dict, brain_data):
    """
    Compare gradient representations with brain responses.
    
    Args:
        gradients_dict: {layer_name: gradient_tensor}
        brain_data: fMRI/MEG responses to same stimuli
    
    Returns:
        correlation: Alignment score per layer
    """
    correlations = {}
    
    for layer, grad in gradients_dict.items():
        # Flatten gradients to representational vector
        grad_repr = grad.flatten()
        
        # Compute RDM (Representational Dissimilarity Matrix)
        grad_rdm = compute_rdm(grad_repr)
        brain_rdm = compute_rdm(brain_data)
        
        # Correlation between RDMs
        correlations[layer] = correlate_rdms(grad_rdm, brain_rdm)
    
    return correlations
```

### Step 3: Hierarchy Analysis

```python
# Analyze gradient hierarchy vs cortical hierarchy

def analyze_hierarchy_alignment(gradient_correlations, cortical_hierarchy):
    """
    Compare gradient computation order with cortical processing order.
    
    Args:
        gradient_correlations: {layer: brain_region_alignment}
        cortical_hierarchy: {region: processing_stage}
    
    Returns:
        alignment_score: Measure of hierarchical alignment
    """
    # Expected: reverse order of cortical hierarchy
    # Observed: different order
    
    gradient_order = sort_by_correlation(gradient_correlations)
    cortical_order = sort_by_hierarchy(cortical_hierarchy)
    
    # Compute alignment
    alignment = compute_order_correlation(gradient_order, cortical_order)
    
    return alignment
```

### Step 4: Temporal Analysis (MEG)

```python
# Temporal dynamics analysis

def temporal_gradient_alignment(gradients, meg_data, time_windows):
    """
    Analyze gradient-brain alignment across time.
    
    Args:
        gradients: Layer gradients
        meg_data: Time-resolved brain responses
        time_windows: Latency ranges to analyze
    
    Returns:
        temporal_profile: Alignment per time window
    """
    temporal_profile = {}
    
    for t_start, t_end in time_windows:
        # Extract MEG responses in time window
        meg_window = extract_time_window(meg_data, t_start, t_end)
        
        # Compute alignment
        temporal_profile[(t_start, t_end)] = gradient_rsa(gradients, meg_window)
    
    return temporal_profile
```

## Key Visualizations

### 1. Spatial Gradient Mapping

**What to visualize:**
- Gradient correlation per brain region
- Comparison with forward activation mapping
- Cortical hierarchy overlay

**Expected patterns:**
- High correlation in high-level visual cortex
- Different spatial distribution vs forward activations

### 2. Temporal Gradient Profile

**What to visualize:**
- Gradient-brain alignment across time (MEG)
- Latency distribution of gradient predictability
- Comparison with forward activation timing

**Expected patterns:**
- Strong alignment at later latencies
- Delayed gradient effects vs forward effects

### 3. Hierarchy Misalignment Plot

**What to visualize:**
- Gradient layer order vs cortical processing order
- Deviation from expected reverse hierarchy
- Layer-to-region mapping

**Expected patterns:**
- Non-linear relationship between layers and regions
- Different ordering than cortical hierarchy

## Applications

### 1. Brain-Model Comparison

**Research Use:**
- Evaluate biological plausibility of learning algorithms
- Test alternative training methods
- Guide neuroscience-inspired AI development

### 2. Alternative Learning Design

**Design Implications:**
- Feedback alignment networks
- Predictive coding architectures
- Hebbian-like learning in deep nets

### 3. Neuroscience Interpretation

**Interpretation Guidance:**
- Don't assume gradient = biological feedback
- Forward activations more reliable for brain mapping
- Gradients reveal computation, not learning mechanism

## Pitfalls & Limitations

### Methodological Challenges

1. **Gradient Extraction Complexity:**
   - Gradients depend on loss function choice
   - Target selection affects gradient structure
   - Multiple gradient sources possible

2. **Brain Data Limitations:**
   - fMRI: Low temporal resolution (~1-2s)
   - MEG: Limited spatial resolution
   - Individual variability in responses

3. **Model Architecture Variability:**
   - Different architectures → different gradients
   - Depth affects gradient magnitude
   - Residual connections change gradient flow

### Interpretation Pitfalls

1. **Gradient ≠ Feedback:**
   - Gradients computed, not "sent backward"
   - Different from biological feedback signals
   - Mathematical construct, not neural signal

2. **Correlation ≠ Mechanism:**
   - Gradient predicts brain ≠ gradient used by brain
   - Similar representations ≠ similar algorithms
   - Don't over-interpret alignment

3. **High-Level Bias:**
   - Gradients align only in high-level cortex
   - Low-level visual areas show less correlation
   - Task-dependent effects unclear

## Advanced Extensions

### 1. Multi-Model Comparison

**Compare across architectures:**
- CNNs vs Transformers
- Supervised vs Self-supervised
- Different depths and widths

### 2. Alternative Gradient Definitions

**Explore different gradient computations:**
- Attention gradients (for transformers)
- Layer-wise relevance propagation
- Integrated gradients
- SmoothGrad

### 3. Task-Specific Gradients

**Compare gradients from different tasks:**
- Classification gradients
- Reconstruction gradients
- Contrastive learning gradients
- Supervised vs unservised

## Research Extensions

### Open Questions

1. **What causes the misalignment?**
   - Architecture factors?
   - Training objective?
   - Biological constraints not captured?

2. **Can we design better-aligned gradients?**
   - Feedback alignment?
   - Predictive coding networks?
   - Brain-constrained architectures?

3. **Does misalignment affect performance?**
   - Are biologically-aligned gradients better?
   - Trade-off between alignment and accuracy?

### Future Directions

1. **Design biologically plausible training algorithms**
2. **Test alternative gradient formulations**
3. **Develop brain-constrained architectures**
4. **Create gradient-brain alignment metrics**

## References

- **arXiv Paper**: 2605.28693v1 (May 27, 2026)
- **Authors**: Raugel et al.
- **Primary Model**: DINOv3
- **Brain Data**: fMRI + MEG natural image responses
- **Comment**: 13 pages, 9 figures

## Related Skills

- [[neuroscience-of-transformers]] - Transformer architectures for brain data
- [[brain-dnn-transformation-alignment]] - Brain-DNN alignment methodology
- [[vlm-visual-cortex-alignment-robustness]] - VLM visual cortex alignment
- [[predictive-coding-light]] - Predictive coding framework