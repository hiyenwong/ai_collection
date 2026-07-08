---
name: backpropagation-brain-misalignment
description: "Backpropagation algorithm misalignment with human brain visual processing hierarchy research. Uses fMRI/MEG to map backpropagated gradients onto neural data, showing DINOv3 gradients can predict brain signals but spatial/temporal organization diverges from biologically plausible backpropagation. arXiv: 2605.28693. Activation: backpropagation brain alignment, gradient neural correspondence, encoding analysis backprop, DINOv3 brain mapping, biological backpropagation, fMRI gradient mapping"
category: ai_collection
arxiv_id: "2605.28693"
tags: ["backpropagation", "brain-alignment", "fMRI", "MEG", "visual-cortex", "DINOv3", "encoding-analysis", "neuroscience-AI"]
---

# Backpropagation-Brain Misalignment: Encoding Analysis of Gradients in Visual Hierarchy

## Overview

A systematic study investigating whether backpropagated gradients from deep vision models map onto the human brain's visual processing hierarchy. While forward activations are known to align, this work extends encoding analysis to backpropagated gradients, finding that although gradients can predict brain signals, their spatial and temporal organization diverges from biologically plausible mechanisms.

**arXiv**: [2605.28693](https://arxiv.org/abs/2605.28693)
**Date**: 2026-05-27
**Categories**: q-bio.NC (Neurons and Cognition), cs.AI (Artificial Intelligence)
**Authors**: Joséphine Raugel, Maximilian Seitzer, Marc Szafraniec, Huy V. Vo, Jérémy Rapin, Patrick Labatut, Piotr Bojanowski, Valentin Wyart, Jean-Rémi King

## Problem Statement

Backpropagation is the core learning mechanism in deep learning, but whether/how it's implemented in the brain remains highly debated. Prior work established that **forward activations** of pretrained models reliably map onto the cortical hierarchy of visual processing (V1→V2→V4→IT). However, it was unknown whether **backpropagated gradients** exhibit similar correspondence.

**Key Question**: Do backpropagated gradients follow the same hierarchical organization in the brain as forward activations?

## Methodology

### Experimental Design

```
Natural Images → DINOv3 (Self-Supervised Vision Model)
                      ↓
    ┌─────────────────┴─────────────────┐
    ↓                                   ↓
Forward Activations              Backpropagated Gradients
    ↓                                   ↓
Encoding Analysis → fMRI/MEG     Encoding Analysis → fMRI/MEG
```

### Data Modalities

| Modality | What it captures | Temporal Resolution | Spatial Resolution |
|----------|-----------------|-------------------|-------------------|
| **fMRI** | Hemodynamic response to visual stimuli | ~2 seconds | ~2-3 mm (cortical) |
| **MEG** | Magnetic fields from neural currents | ~1 ms | ~5-10 mm (source-localized) |

### Encoding Analysis Extension

Standard approach: predict neural activity from model features
- **Traditional**: `neural_response = W * forward_activation + b`
- **Extended**: `neural_response = W * backprop_gradient + b`

This maps backpropagated gradients (∂L/∂x at each layer) onto the same neural data used for forward activation mapping.

### Models Tested

| Model | Type | Result |
|-------|------|--------|
| **DINOv3** | Self-supervised ViT (primary) | Gradients predict brain signals |
| + 8 additional vision models | CNNs, ViTs | Results reproduced across architectures |

## Key Findings

### Finding 1: Gradients CAN Predict Brain Signals

Backpropagated gradients from DINOv3 **reliably predict both fMRI and MEG signals**, specifically:
- **Higher-level visual cortex** (V4, IT, LOC) show stronger gradient-brain correspondence
- **Later latencies** in MEG (150-300ms post-stimulus) show stronger gradient-brain correspondence
- This suggests gradient information is present in neural responses, at least at a statistical level

### Finding 2: But the ORGANIZATION Diverges

Despite predictive power, the **spatial and temporal organization** of backpropagated gradients diverges from biologically plausible patterns:

#### Spatial Divergence
| Expected (Biological BP) | Observed (DINOv3 BP) |
|--------------------------|---------------------|
| Layer-by-layer gradient flow matching cortical hierarchy | Gradient organization doesn't align with V1→V4→IT progression |
| Lower visual areas (V1) should show early-layer gradients | Gradient-brain mapping peaks in higher areas, not lower |

#### Temporal Divergence
| Expected (Biological BP) | Observed (DINOv3 BP) |
|--------------------------|---------------------|
| Gradients computed in reverse order (deep→shallow), implying later areas should show gradient signals first | Temporal pattern of gradient-brain correspondence doesn't match reverse-order computation |
| Gradient signals should propagate backward through hierarchy | Gradient signals appear in parallel or non-hierarchical patterns |

### Finding 3: Forward vs. Gradient Asymmetry

```
Forward Activations:  Strong hierarchical alignment ✓ (V1→V2→V4→IT matches layer depth)
Backprop Gradients:   Weak/no hierarchical alignment ✗ (doesn't match expected reverse flow)
```

This asymmetry is crucial: the brain may share similar **representational content** with deep networks, but uses fundamentally different **learning mechanisms**.

## Reusable Skill Patterns

### Pattern 1: Gradient Encoding Analysis Pipeline

**Applicability**: Testing whether any model's internal gradients align with neural data

```python
# Extended encoding analysis for backpropagated gradients
def gradient_encoding_analysis(model, images, neural_data):
    """
    Map backpropagated gradients onto neural recordings.
    
    Args:
        model: Pretrained vision model
        images: Stimulus images
        neural_data: fMRI or MEG recordings (n_samples × n_channels)
    
    Returns:
        gradient_brain_mapping: Correlation between gradients and neural data
    """
    # Forward pass to get activations
    activations, gradients = {}, {}
    for layer in model.layers:
        layer.register_forward_hook(capture(activations, layer.name))
        layer.register_full_backward_hook(capture(gradients, layer.name))
    
    # Forward + backward pass
    output = model(images)
    loss = some_objective(output)  # Could be classification, self-supervised, etc.
    loss.backward()
    
    # Encoding analysis: predict neural data from gradients
    results = {}
    for layer_name, grad in gradients.items():
        # Ridge regression: neural = W * grad + b
        score = ridge_regression_predict(grad.flatten(), neural_data)
        results[layer_name] = score
    
    return results
```

### Pattern 2: Hierarchical Alignment Testing

**Applicability**: Testing whether model-to-brain mappings follow expected hierarchical patterns

```python
def test_hierarchical_alignment(model_layer_scores, brain_region_scores, expected_order):
    """
    Test whether the layer-to-brain mapping follows a hierarchical pattern.
    
    Args:
        model_layer_scores: Dict mapping layer names to brain prediction scores
        brain_region_scores: Dict mapping brain regions to prediction scores
        expected_order: Expected hierarchical order (e.g., ['V1', 'V2', 'V4', 'IT'])
    
    Returns:
        alignment_metrics: Hierarchical alignment statistics
    """
    # Spearman correlation between expected and observed ordering
    # Spatial smoothness of mapping along hierarchy
    # Cross-validation of hierarchical consistency
    pass
```

### Pattern 3: Multi-Modal Neural Validation

**Applicability**: Combining fMRI and MEG for comprehensive brain-model comparison

| Validation Type | fMRI Contribution | MEG Contribution |
|----------------|-------------------|------------------|
| **Spatial** | Precise cortical localization | Coarse source localization |
| **Temporal** | Slow hemodynamic response | Millisecond-precise timing |
| **Gradient-specific** | Where gradients predict brain activity | When gradients predict brain activity |

## Key Insights

1. **Representational Similarity ≠ Mechanistic Similarity**: Deep networks and brains may compute similar representations but arrive at them through fundamentally different mechanisms

2. **Gradient Analysis is Complementary**: Standard encoding analysis only tests forward pass; gradient analysis tests the learning mechanism itself

3. **Biological Plausibility Gap**: The divergence suggests biological learning mechanisms (local Hebbian rules, feedback alignment, predictive coding) rather than true backpropagation

4. **Self-Supervised Models**: DINOv3 (self-supervised) shows similar gradient-brain relationships as supervised models, suggesting the misalignment is architectural, not training-objective dependent

## Related Skills

- `backprop-brain-hierarchy-misalignment` - Related analysis of BP gradient vs brain hierarchy
- `untrained-cnns-match-backpropagation-v1-rsa` - RSA comparison of untrained vs trained CNNs in V1
- `target-space-recovery-profiles-brain-alignment` - Beyond accuracy metrics for brain alignment
- `brain-dnn-transformation-alignment` - Category-theoretic brain-to-DNN alignment framework
- `neural-encoding-evaluation-ground-truth` - Ground-truth approximation for neural encoding evaluation

## Pitfalls

- **Gradient objective dependence**: Results depend on which loss function gradients are computed from (classification vs. self-supervised); different objectives may yield different gradient patterns
- **Layer-to-region mapping ambiguity**: Mapping model layers to brain regions is inherently approximate; multiple mapping schemes exist
- **fMRI temporal limitation**: fMRI's slow hemodynamic response makes it unsuitable for testing the temporal order of gradient computation
- **MEG spatial limitation**: MEG's coarse spatial resolution makes precise cortical localization difficult
- **Not a disproof**: This work shows misalignment of organization, not absence of gradient-like signals entirely
