---
name: cross-modal-convergence-dispersion
description: "Generalized Procrustes Algorithm for measuring intra-modal representational convergence at single-stimulus level; intra-modal dispersion modulates cross-modal alignment."
version: "1.0"
paper_id: "2604.21836"
arxiv_url: "https://arxiv.org/abs/2604.21836"
authors: "Eghbal A. Hosseini, Brian Cheung, Evelina Fedorenko, Alex H. Williams"
published: "2026-04-23"
categories:
  - q-bio.NC
tags:
  - cross-modal-alignment
  - intra-modal-dispersion
  - procrustes-analysis
  - vision-language-models
  - representational-convergence
  - multi-modal
---

# Cross-Modal Convergence via Intra-Modal Dispersion

> Measuring representational convergence at the single-stimulus level using Generalized Procrustes Algorithm; discovering that low intra-modal dispersion predicts higher cross-modal alignment.

## Metadata
- **Source**: arXiv:2604.21836
- **Authors**: Eghbal A. Hosseini, Brian Cheung, Evelina Fedorenko, Alex H. Williams
- **Published**: 2026-04-23

## Core Methodology

### Key Innovation

Neural networks show remarkable representational convergence across architectures, training objectives, and even data modalities. However, it was unclear how individual stimuli elicit convergent representations. This work introduces:

1. **Single-stimulus convergence measurement** using Generalized Procrustes Algorithm
2. **Intra-modal dispersion** as a measure of representational agreement within a modality
3. **Discovery**: Low intra-modal dispersion (high agreement among vision models) elicits significantly higher cross-modal alignment (up to 2x)

### Technical Framework

**Step 1: Generalized Procrustes Analysis (GPA)**
- Align representational spaces across models within a modality
- Remove rotation/reflection differences
- Preserve distances for valid comparison

**Step 2: Intra-Modal Dispersion Computation**
- For each stimulus, compute representational variance across models
- Low dispersion = high agreement among models
- High dispersion = models disagree on stimulus representation

**Step 3: Stimulus Selection**
- Select stimuli based on intra-modal dispersion levels
- Create matched sets with high vs. low dispersion

**Step 4: Cross-Modal Alignment Measurement**
- Measure alignment between vision and language models
- Compare alignment for low vs. high dispersion stimuli
- Generalize across different model pairings

**Step 5: Analysis**
- Correlation between intra-modal and cross-modal measures
- Robustness to stimulus selection criteria
- Generalization across model architectures

## Implementation Guide

### Prerequisites
- Pre-trained vision models (e.g., DINOv2, CLIP, supervised ResNet)
- Language models (e.g., GPT, BERT variants)
- Stimulus dataset with paired images and text descriptions

### Step-by-Step

```python
# 1. Extract features from vision models
vision_features = {}
for model_name, model in vision_models.items():
    vision_features[model_name] = extract_features(model, stimuli_images)

# 2. Extract features from language models
language_features = {}
for model_name, model in language_models.items():
    language_features[model_name] = extract_features(model, stimuli_texts)

# 3. Apply Generalized Procrustes Analysis
from scipy.spatial import procrustes

# Align vision model spaces
aligned_vision = generalized_procrustes_analysis(vision_features)

# Align language model spaces  
aligned_language = generalized_procrustes_analysis(language_features)

# 4. Compute intra-modal dispersion
dispersion_scores = {}
for stimulus_idx in range(num_stimuli):
    # Variance across vision models for this stimulus
    vision_reps = [aligned_vision[m][stimulus_idx] for m in vision_models]
    dispersion_scores[stimulus_idx] = compute_dispersion(vision_reps)

# 5. Select stimuli by dispersion level
low_dispersion_stimuli = select_by_dispersion(dispersion_scores, percentile=25)
high_dispersion_stimuli = select_by_dispersion(dispersion_scores, percentile=75)

# 6. Measure cross-modal alignment
cross_modal_alignment = {}
for vision_model in vision_models:
    for language_model in language_models:
        # Alignment for low dispersion stimuli
        low_alignment = compute_alignment(
            aligned_vision[vision_model][low_dispersion_stimuli],
            aligned_language[language_model][low_dispersion_stimuli]
        )
        # Alignment for high dispersion stimuli
        high_alignment = compute_alignment(
            aligned_vision[vision_model][high_dispersion_stimuli],
            aligned_language[language_model][high_dispersion_stimuli]
        )
        cross_modal_alignment[(vision_model, language_model)] = {
            'low_dispersion': low_alignment,
            'high_dispersion': high_alignment
        }

# 7. Analyze modulation effect
for pair, scores in cross_modal_alignment.items():
    modulation = scores['low_dispersion'] / scores['high_dispersion']
    print(f"{pair}: {modulation:.2f}x higher alignment for low dispersion")
```

### Code Example

```python
import numpy as np
from scipy.spatial.distance import cdist
from scipy.linalg import orthogonal_procrustes

def generalized_procrustes_analysis(features_dict, max_iter=100, tol=1e-5):
    """
    Apply Generalized Procrustes Analysis to align multiple representational spaces.
    
    Parameters:
    -----------
    features_dict : dict
        Mapping from model names to feature matrices (n_stimuli x n_features)
    max_iter : int
        Maximum iterations
    tol : float
        Convergence tolerance
        
    Returns:
    --------
    aligned_features : dict
        Aligned feature matrices
    """
    model_names = list(features_dict.keys())
    n_models = len(model_names)
    n_stimuli = list(features_dict.values())[0].shape[0]
    
    # Initialize with original features
    aligned = {name: features.copy() for name, features in features_dict.items()}
    
    # Iterative alignment to mean configuration
    for iteration in range(max_iter):
        # Compute current mean configuration
        mean_config = np.mean([aligned[name] for name in model_names], axis=0)
        
        # Align each model to mean
        max_change = 0
        for name in model_names:
            # Orthogonal Procrustes: find optimal rotation
            R, _ = orthogonal_procrustes(aligned[name], mean_config)
            new_aligned = aligned[name] @ R
            
            change = np.linalg.norm(new_aligned - aligned[name])
            max_change = max(max_change, change)
            
            aligned[name] = new_aligned
        
        if max_change < tol:
            break
    
    return aligned

def compute_intra_modal_dispersion(aligned_features, metric='euclidean'):
    """
    Compute intra-modal dispersion for each stimulus.
    
    Parameters:
    -----------
    aligned_features : dict
        Aligned feature matrices from GPA
    metric : str
        Distance metric for dispersion computation
        
    Returns:
    --------
    dispersion : array
        Dispersion score for each stimulus (higher = more disagreement)
    """
    model_names = list(aligned_features.keys())
    n_stimuli = aligned_features[model_names[0]].shape[0]
    
    dispersion = np.zeros(n_stimuli)
    
    for i in range(n_stimuli):
        # Collect representations from all models for this stimulus
        reps = np.array([aligned_features[name][i] for name in model_names])
        
        # Compute pairwise distances
        distances = cdist(reps, reps, metric=metric)
        
        # Dispersion = mean pairwise distance (excluding diagonal)
        mask = ~np.eye(len(model_names), dtype=bool)
        dispersion[i] = distances[mask].mean()
    
    return dispersion

def measure_cross_modal_alignment(vision_features, language_features, 
                                   stimuli_indices, method='cca'):
    """
    Measure alignment between vision and language representations.
    
    Parameters:
    -----------
    vision_features : array
        Vision model features for selected stimuli
    language_features : array
        Language model features for selected stimuli
    method : str
        Alignment method ('cca', 'rsa', 'linear_cka')
        
    Returns:
    --------
    alignment_score : float
        Alignment magnitude
    """
    v_sub = vision_features[stimuli_indices]
    l_sub = language_features[stimuli_indices]
    
    if method == 'cca':
        from sklearn.cross_decomposition import CCA
        cca = CCA(n_components=min(v_sub.shape[1], l_sub.shape[1]))
        v_c, l_c = cca.fit_transform(v_sub, l_sub)
        # Return mean canonical correlation
        return np.mean([np.corrcoef(v_c[:, i], l_c[:, i])[0, 1] 
                       for i in range(v_c.shape[1])])
    
    elif method == 'rsa':
        # Representational similarity analysis
        rdm_v = 1 - np.corrcoef(v_sub)
        rdm_l = 1 - np.corrcoef(l_sub)
        from scipy.stats import spearmanr
        return spearmanr(rdm_v[np.triu_indices_from(rdm_v, k=1)],
                        rdm_l[np.triu_indices_from(rdm_l, k=1)])[0]
    
    elif method == 'linear_cka':
        # Centered Kernel Alignment
        v_centered = v_sub - v_sub.mean(axis=0)
        l_centered = l_sub - l_sub.mean(axis=0)
        
        hsic = np.trace(v_centered @ v_centered.T @ l_centered @ l_centered.T)
        norm_v = np.linalg.norm(v_centered @ v_centered.T, 'fro')
        norm_l = np.linalg.norm(l_centered @ l_centered.T, 'fro')
        
        return hsic / (norm_v * norm_l)
```

## Applications

### Vision-Language Model Evaluation
- Identify which stimuli show strongest cross-modal alignment
- Understand when visual and linguistic representations converge
- Evaluate model robustness across stimulus types

### Multi-Modal Transfer Learning
- Select training data with low intra-modal dispersion for better transfer
- Understand which concepts transfer well across modalities
- Design better multi-modal pretraining strategies

### Neural Network Interpretability
- Study representational convergence at single-stimulus level
- Identify stimuli that elicit consistent vs. divergent representations
- Map the structure of learned representations

### Brain-Model Alignment
- Compare multi-modal alignment patterns in brains and models
- Understand how humans represent concepts across modalities
- Develop better models of cross-modal cognition

## Pitfalls

- **Procrustes limitations**: GPA removes rotation/reflection but assumes isotropic scaling; may not capture all geometric relationships
- **Stimulus selection bias**: Careful matching needed when comparing high vs. low dispersion sets
- **Model architecture effects**: Results may vary with different model families; test generalization
- **Computational cost**: GPA is iterative and can be expensive for large model sets
- **Interpretation**: Low dispersion ≠ "better" representation; reflects model agreement, not ground truth

## Related Skills

- `brain-alignment-patterns-analysis` - Brain-model alignment evaluation
- `cross-modal-convergence` - Multi-modal representational convergence
- `umwelt-representation-hypothesis` - Ecological constraints on alignment
- `rsa-representational-similarity` - Representational similarity analysis
- `generalized-procrustes-analysis` - GPA methodology reference
