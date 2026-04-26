---
name: cross-modal-convergence
description: "Cross-modal representational convergence methodology using Generalized Procrustes Algorithm to measure intra-modal dispersion at single-stimulus level. Low intra-modal dispersion predicts up to 2× higher cross-modal alignment. Activation: representational similarity, RSA, Procrustes, cross-modal, model-brain alignment, vision-language, DINOv2."
---

# Cross-Modal Convergence via Single-Stimulus Intra-Modal Dispersion

> A methodology using the Generalized Procrustes Algorithm (GPA) to measure representational convergence at the single-stimulus level, revealing that intra-modal agreement among vision models strongly modulates cross-modal (vision-language) alignment by up to a factor of two.

## Metadata
- **Source**: arXiv:2604.21836
- **Authors**: Eghbal A. Hosseini, Brian Cheung, Evelina Fedorenko, Alex H. Williams
- **Published**: 2026-04-23
- **Categories**: q-bio.NC, cs.AI

## Core Methodology

### Key Innovation
First methodology to measure intra-modal representational convergence at the **single-stimulus level** using Generalized Procrustes Analysis. Demonstrates that stimuli with low intra-modal dispersion (high agreement among vision models) elicit significantly higher cross-modal alignment with language models — up to 2× improvement.

### Technical Framework

1. **Generalized Procrustes Algorithm (GPA)**:
   - Align representational spaces of multiple models via optimal rotation/reflection
   - Compute per-stimulus dispersion after alignment
   - Low dispersion = high agreement across models for that stimulus

2. **Intra-Modal Dispersion Metric**:
   - For each stimulus, measure variance of its representation across N vision models after Procrustes alignment
   - Sort stimuli by dispersion (low vs high)
   - Compare cross-modal alignment for low vs high dispersion groups

3. **Cross-Modal Alignment Measurement**:
   - Measure representational similarity between vision and language model activations
   - Use standard alignment metrics (CKA, linear regression, RDM correlation)
   - Evaluate on low-dispersion vs high-dispersion stimuli

### Key Findings
- Stimuli with low intra-modal dispersion show up to 2× higher cross-modal alignment
- Effect robust across different vision-language model pairings
- Effect robust to stimulus selection criteria
- Generalizes across DINOv2, CLIP, and other vision models paired with various language models
- Provides a path toward understanding sources of convergence/divergence across modalities

## Implementation Guide

### Prerequisites
- Multiple pretrained vision models (e.g., DINOv2, CLIP, ResNet, ViT variants)
- Language model with vision-compatible representations
- Python: numpy, scipy, scikit-learn

### Step-by-Step Analysis
1. **Extract representations**: Get activations from N vision models for each stimulus
2. **Procrustes alignment**: Align all model representational spaces via GPA
3. **Compute dispersion**: For each stimulus, compute variance of aligned representations across models
4. **Stratify stimuli**: Sort by dispersion, select low and high dispersion groups
5. **Measure cross-modal alignment**: Compare vision-language alignment for each group
6. **Statistical testing**: Test significance of alignment difference between groups

### Code Example
```python
import numpy as np
from scipy.spatial import procrustes
from sklearn.linear_model import LinearRegression

def generalized_procrustes(representations_list, reference=0):
    """Align multiple model representations via iterative Procrustes."""
    ref = representations_list[reference].copy()
    aligned = [ref]
    for i, rep in enumerate(representations_list):
        if i == reference:
            continue
        _, transformed, _ = procrustes(ref, rep)
        aligned.append(transformed)
    return aligned

def compute_stimulus_dispersion(aligned_reps):
    """Compute per-stimulus dispersion across aligned model representations."""
    stacked = np.stack(aligned_reps)  # (n_models, n_stimuli, n_features)
    # Compute variance across models for each stimulus
    dispersion = np.var(stacked, axis=0).mean(axis=-1)  # (n_stimuli,)
    return dispersion

def measure_crossmodal_alignment(vision_acts, language_acts):
    """Measure alignment between vision and language representations."""
    reg = LinearRegression()
    reg.fit(vision_acts, language_acts)
    score = reg.score(vision_acts, language_acts)
    return score
```

## Applications
- **Model-brain alignment prediction**: Use intra-modal dispersion to predict which stimuli will show strong brain-model alignment
- **Stimulus selection for fMRI**: Select low-dispersion stimuli for more reliable cross-modal experiments
- **Understanding representational convergence**: Identify what makes some stimuli universally "easy" vs "hard" for models
- **Multi-modal training**: Inform training data curation for vision-language models
- **Neuroscience experimental design**: Optimize stimulus sets for cross-modal studies

## Pitfalls
- GPA alignment quality depends on the number and diversity of models used
- Small stimulus sets may not reveal robust dispersion effects
- Cross-modal alignment metrics can differ in sensitivity
- The effect is correlational — low dispersion does not guarantee high cross-modal alignment for every stimulus
- Requires careful handling of representational dimensionality differences across models

## Related Skills
- neuroscience-of-transformers
- brain-graph-neural
- representation-use-usability-framework
