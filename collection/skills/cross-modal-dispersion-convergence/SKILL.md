---
name: cross-modal-dispersion-convergence
description: "Cross-modal convergence analysis methodology using Generalized Procrustes Algorithm to measure intra-modal representational convergence at single-stimulus level. Reveals how low intra-modal dispersion (high agreement among vision models) elicits significantly higher cross-modal alignment between vision and language models. Activation: cross-modal convergence, representational alignment, Procrustes analysis, vision-language alignment, neural representation, single-stimulus analysis"
---

# Cross-Modal Dispersion and Convergence Analysis

## Overview

This methodology introduces a framework for understanding how individual stimuli elicit convergent representations across different neural networks and modalities. Using the **Generalized Procrustes Algorithm (GPA)**, it measures intra-modal representational convergence at the single-stimulus level to reveal how stimulus-specific agreement modulates cross-modal alignment.

## Key Insight

**Low intra-modal dispersion → High cross-modal alignment**

Stimuli with high agreement among vision models (low intra-modal dispersion) elicit significantly higher cross-modal alignment between vision and language models than those with high dispersion (up to 2x improvement with DINOv2-language model pairings).

## Core Methodology

### 1. Generalized Procrustes Algorithm (GPA)

The GPA aligns multiple configurations by iterative transformations (translation, rotation, scaling, reflection) to minimize sum of squared distances between corresponding points.

```python
def generalized_procrustes_analysis(representations_list, iterations=1000):
    """
    Align multiple representation spaces to a common reference
    
    Parameters:
    - representations_list: List of representation matrices from different models
    - iterations: Maximum iterations for convergence
    
    Returns:
    - aligned_representations: List of aligned representation matrices
    - mean_configuration: Consensus configuration
    """
    import numpy as np
    from scipy.spatial.distance import cdist
    from scipy.linalg import orthogonal_procrustes
    
    n_models = len(representations_list)
    n_stimuli, n_features = representations_list[0].shape
    
    # Initialize mean configuration
    mean_config = np.mean(representations_list, axis=0)
    
    # Iteratively align to mean configuration
    for _ in range(iterations):
        aligned = []
        for rep in representations_list:
            # Center representations
            rep_centered = rep - np.mean(rep, axis=0)
            mean_centered = mean_config - np.mean(mean_config, axis=0)
            
            # Orthogonal Procrustes
            R, _ = orthogonal_procrustes(rep_centered, mean_centered)
            aligned_rep = rep_centered @ R + np.mean(mean_config, axis=0)
            aligned.append(aligned_rep)
        
        # Update mean configuration
        new_mean = np.mean(aligned, axis=0)
        
        # Check convergence
        if np.allclose(mean_config, new_mean, rtol=1e-6):
            break
        mean_config = new_mean
    
    return aligned, mean_config
```

### 2. Intra-Modal Dispersion Calculation

```python
def compute_intra_modal_dispersion(representations_list, stimulus_idx=None):
    """
    Compute intra-modal dispersion for stimuli
    
    For each stimulus, measures how much different models disagree
    about its representation (after Procrustes alignment)
    
    Parameters:
    - representations_list: List of aligned representation matrices from
                            models within the same modality (e.g., vision)
    - stimulus_idx: Specific stimulus index (None for all stimuli)
    
    Returns:
    - dispersion: Per-stimulus dispersion scores
    """
    import numpy as np
    from scipy.spatial.distance import cdist
    
    n_models = len(representations_list)
    n_stimuli = representations_list[0].shape[0]
    
    if stimulus_idx is not None:
        # Single stimulus dispersion
        stimulus_reps = np.array([rep[stimulus_idx] for rep in representations_list])
        # Variance across models
        dispersion = np.var(stimulus_reps, axis=0).mean()
    else:
        # All stimuli dispersion
        dispersion = []
        for i in range(n_stimuli):
            stimulus_reps = np.array([rep[i] for rep in representations_list])
            disp = np.var(stimulus_reps, axis=0).mean()
            dispersion.append(disp)
        dispersion = np.array(dispersion)
    
    return dispersion
```

### 3. Cross-Modal Alignment Measurement

```python
def measure_cross_modal_alignment(vision_reps, language_reps):
    """
    Measure alignment between vision and language representations
    
    Parameters:
    - vision_reps: Vision model representations (n_stimuli x n_features)
    - language_reps: Language model representations (n_stimuli x n_features)
    
    Returns:
    - alignment_score: Cross-modal alignment score
    """
    from scipy.stats import pearsonr
    from scipy.spatial.distance import pdist, squareform
    
    # Compute representational similarity matrices (RDMs)
    vision_rdm = pdist(vision_reps, metric='correlation')
    language_rdm = pdist(language_reps, metric='correlation')
    
    # Correlation between RDMs (alignment score)
    alignment, _ = pearsonr(vision_rdm, language_rdm)
    
    return alignment
```

### 4. Complete Analysis Pipeline

```python
def cross_modal_dispersion_analysis(
    vision_models_reps,      # Dict: {model_name: representations}
    language_models_reps,    # Dict: {model_name: representations}
    stimulus_labels=None
):
    """
    Full cross-modal dispersion and convergence analysis
    
    Parameters:
    - vision_models_reps: Dictionary of vision model representations
    - language_models_reps: Dictionary of language model representations
    - stimulus_labels: Optional stimulus category labels
    
    Returns:
    - results: Analysis results including dispersion and alignment
    """
    # Step 1: Align vision models within modality
    vision_list = list(vision_models_reps.values())
    aligned_vision, vision_mean = generalized_procrustes_analysis(vision_list)
    
    # Step 2: Align language models within modality  
    language_list = list(language_models_reps.values())
    aligned_language, language_mean = generalized_procrustes_analysis(language_list)
    
    # Step 3: Compute intra-modal dispersion for each stimulus
    vision_dispersion = compute_intra_modal_dispersion(aligned_vision)
    language_dispersion = compute_intra_modal_dispersion(aligned_language)
    
    # Step 4: Analyze cross-modal alignment vs dispersion
    results = []
    for vision_model_name, vision_aligned in zip(vision_models_reps.keys(), aligned_vision):
        for lang_model_name, lang_aligned in zip(language_models_reps.keys(), aligned_language):
            alignment = measure_cross_modal_alignment(vision_aligned, lang_aligned)
            
            results.append({
                'vision_model': vision_model_name,
                'language_model': lang_model_name,
                'alignment': alignment,
                'vision_dispersion': vision_dispersion.mean(),
                'language_dispersion': language_dispersion.mean(),
                'per_stimulus_correlation': compute_dispersion_alignment_correlation(
                    vision_dispersion, language_dispersion, alignment
                )
            })
    
    return results


def compute_dispersion_alignment_correlation(dispersion, alignment_scores):
    """
    Correlation between dispersion and alignment at single-stimulus level
    """
    from scipy.stats import pearsonr
    
    # Lower dispersion should correlate with higher alignment
    correlation, p_value = pearsonr(-dispersion, alignment_scores)
    
    return {
        'correlation': correlation,
        'p_value': p_value,
        'interpretation': 'Negative correlation expected: low dispersion → high alignment'
    }
```

## Key Findings

### 1. Intra-Modal Dispersion Modulates Cross-Modal Alignment

| Dispersion Level | Cross-Modal Alignment (Example) |
|-----------------|--------------------------------|
| Low (high agreement) | ~2x higher alignment (DINOv2 + language models) |
| High (low agreement) | Lower alignment |

### 2. Generalization Across Model Pairings
- Effect is **robust across different vision-language model pairings**
- Independent of specific stimulus selection criteria
- Consistent across architectural families

### 3. Single-Stimulus Resolution
- Enables understanding of **which specific stimuli** drive alignment
- Reveals stimulus-level factors contributing to convergence
- Provides path toward understanding sources of convergence/divergence

## Applications

### 1. Model-Brain Alignment Research
- **Identify stimuli that maximize model-brain alignment**
- Understand what makes representations "brain-like"
- Guide model development toward more biological plausibility

### 2. Multimodal Model Evaluation
- Evaluate vision-language model alignment quality
- Identify poorly aligned stimulus categories
- Guide data curation for multimodal training

### 3. Cognitive Science
- Understand how humans represent stimuli across modalities
- Study cross-modal transfer in human perception
- Link computational models to cognitive theories

### 4. Explainable AI
- Explain why certain stimuli are easy/hard for multimodal models
- Identify ambiguous or multi-interpretable stimuli
- Characterize model decision boundaries

## Implementation Considerations

### Data Requirements
- **Representations from multiple models** within each modality
- **Paired stimuli**: Same set of stimuli represented by all models
- **Sufficient samples**: Enough stimuli to compute reliable statistics

### Model Selection
- Include diverse architectures (CNNs, Transformers, etc.)
- Cover different training objectives (supervised, self-supervised, CLIP-style)
- Ensure representation dimensionality is compatible or use dimensionality reduction

### Statistical Validation
- Bootstrap confidence intervals for dispersion and alignment
- Control for stimulus set size
- Test robustness to model selection

### Visualization

```python
def plot_dispersion_alignment_analysis(dispersion, alignment, stimulus_labels=None):
    """
    Visualize the relationship between dispersion and alignment
    """
    import matplotlib.pyplot as plt
    
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Scatter plot
    ax1 = axes[0]
    scatter = ax1.scatter(dispersion, alignment, c=stimulus_labels, cmap='viridis', alpha=0.6)
    ax1.set_xlabel('Intra-Modal Dispersion (log scale)')
    ax1.set_ylabel('Cross-Modal Alignment')
    ax1.set_title('Dispersion vs. Alignment')
    if stimulus_labels is not None:
        plt.colorbar(scatter, ax=ax1, label='Stimulus Category')
    
    # Binned analysis
    ax2 = axes[1]
    n_bins = 5
    bins = np.percentile(dispersion, np.linspace(0, 100, n_bins + 1))
    bin_centers = (bins[:-1] + bins[1:]) / 2
    bin_alignments = []
    bin_stds = []
    
    for i in range(n_bins):
        mask = (dispersion >= bins[i]) & (dispersion < bins[i+1])
        bin_alignments.append(alignment[mask].mean())
        bin_stds.append(alignment[mask].std())
    
    ax2.errorbar(bin_centers, bin_alignments, yerr=bin_stds, marker='o')
    ax2.set_xlabel('Intra-Modal Dispersion')
    ax2.set_ylabel('Mean Cross-Modal Alignment')
    ax2.set_title('Binned Analysis')
    
    plt.tight_layout()
    return fig
```

## References

- **Paper**: arXiv:2604.21836
- **Title**: Modulating Cross-Modal Convergence with Single-Stimulus, Intra-Modal Dispersion
- **Authors**: Eghbal A. Hosseini, Brian Cheung, Evelina Fedorenko, Alex H. Williams
- **Published**: April 23, 2026
- **Categories**: q-bio.NC, cs.AI
- **Workshop**: ICLR 2026 Workshop on Representational Alignment (Re-Align)

## Related Concepts

- Generalized Procrustes Analysis (GPA)
- Representational Similarity Analysis (RSA)
- Model-brain alignment
- Cross-modal learning
- Vision-language models
- Multimodal representations
- Neural network interpretability
- Brain-inspired AI