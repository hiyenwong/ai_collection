---
name: iris-visual-cortex-framework-vit
description: "IRIS: A Visual Cortex-Inspired Framework for Analyzing Orientation Selectivity in Vision Transformers. Introduces neuroscience-inspired metrics (RSS, ORS, orientation tuning bandwidth) to quantify how orientation selectivity emerges in ViTs during training. Use when analyzing low-level feature encoding in transformers, studying biological plausibility of AI vision models, or investigating how training paradigms affect representational geometry in deep learning."
metadata:
  arxiv_id: "2608.05122"
  published: "2026-08-05"
  authors: "Vaishnavi B Mohan, Vijayakrishna Naganoor, Yashas Annadani, Shashank Hegde"
  tags: [neuroscience, computer-vision, vision-transformers, orientation-selectivity, representational-similarity]
license: Complete terms in LICENSE.txt
---

# IRIS: Visual Cortex-Inspired Framework for Vision Transformers

## Overview

IRIS (Inspired by Retinotopic Information Structure) is a neuroscience-inspired framework for analyzing how orientation selectivity—a fundamental property of the primary visual cortex (V1)—emerges in Vision Transformers (ViTs). Unlike convolutional neural networks that build local features through inductive biases, ViTs process information globally, raising questions about how they encode low-level visual features.

This framework introduces three key metrics to systematically study orientation selectivity in ViTs:
1. **Representational Similarity Score (RSS)** - Measures similarity between ViT representations and biological V1 responses
2. **Orientation Recruitment Score (ORS)** - Quantifies how many units become orientation-selective during training
3. **Orientation Tuning Bandwidth** - Measures the specificity of orientation tuning in individual units

## Key Findings

The paper demonstrates that:
1. **Training paradigm is the strongest determinant** of orientation selectivity, with models sharing an objective peaking at comparable relative depths regardless of scale
2. **Early-to-middle layers recruit orientation-selective units** over time, while deeper layers lose selectivity and broaden tuning toward semantic encoding
3. **The metrics provide mechanistic heuristics** for determining optimal layer unfreezing strategies for downstream generalization

## Methodology

### Step 1: Implement IRIS Metrics

```python
# Pseudocode for RSS calculation
def calculate_rss(vit_activations, v1_responses):
    """Calculate Representational Similarity Score between ViT and V1"""
    # Compute representational dissimilarity matrices
    vit_rdm = compute_rdm(vit_activations)
    v1_rdm = compute_rdm(v1_responses)
    
    # Calculate similarity (e.g., Spearman correlation)
    rss = spearman_correlation(vit_rdm, v1_rdm)
    return rss

# Pseudocode for ORS calculation  
def calculate_ors(layer_activations, orientation_stimuli):
    """Calculate Orientation Recruitment Score for a layer"""
    orientation_selective_units = []
    for unit_idx in range(layer_activations.shape[-1]):
        unit_responses = layer_activations[:, :, unit_idx]
        tuning_curve = compute_tuning_curve(unit_responses, orientation_stimuli)
        if is_orientation_selective(tuning_curve):
            orientation_selective_units.append(unit_idx)
    
    ors = len(orientation_selective_units) / layer_activations.shape[-1]
    return ors
```

### Step 2: Analyze Training Dynamics

Track RSS, ORS, and tuning bandwidth across:
- Different model depths (relative depth: layer_idx / total_layers)
- Training epochs/timepoints
- Different training objectives (supervised vs self-supervised)

### Step 3: Apply to Downstream Tasks

Use IRIS metrics to guide transfer learning:
- Identify optimal layers to unfreeze based on orientation selectivity profiles
- Compare different pretraining paradigms using biological plausibility metrics
- Evaluate architectural modifications for improved low-level feature learning

## Applications

- **Model Interpretability**: Understand how ViTs encode basic visual features without local inductive biases
- **Architecture Design**: Guide development of more biologically plausible vision models
- **Transfer Learning**: Optimize fine-tuning strategies based on representational geometry
- **Neuroscience-AI Bridge**: Systematically compare artificial and biological vision systems

## Pitfalls and Considerations

- **Stimulus Set**: Ensure orientation stimuli cover full range (0-180°) with sufficient resolution
- **Biological Baseline**: Use appropriate V1 data for comparison (species, recording method, etc.)
- **Model Variants**: Account for differences between ViT variants (DeiT, Swin, etc.)
- **Computational Cost**: Full analysis requires activations from all layers across training trajectory

## Activation Keywords

- IRIS framework
- orientation selectivity
- vision transformers neuroscience
- representational similarity score
- biological plausibility ViT
- V1-inspired metrics
- low-level feature encoding transformers

## References

- Original Paper: [arXiv:2608.05122](https://arxiv.org/abs/2608.05122)
- Related Skills: `neuroscience-of-transformers`, `transformer-brain-topological-alignment`