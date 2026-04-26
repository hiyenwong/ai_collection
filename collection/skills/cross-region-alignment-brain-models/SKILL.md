---
name: cross-region-alignment-brain-models
description: "Cross-Region Alignment Patterns (CRAP) analysis for evaluating computational models of brain function. Exposes limits of normative models by comparing brain-to-brain vs. model-to-brain alignment across multiple regions. Keywords: representation alignment, cross-region patterns, computational models, neuroAI, brain alignment."
---

# Cross-Region Alignment Patterns (CRAP) for Model Evaluation

Research methodology from arXiv:2604.21780v1 for evaluating computational models through cross-region representation alignment.

## Overview

Representation alignment between deep neural networks and the brain has become popular for validating computational models. However, most studies focus on **single brain regions**, overlooking important cross-region dynamics. This skill implements **Cross-Region Alignment Patterns (CRAP)** analysis to provide a more stringent test for computational models.

## Core Insight

> Only brains align with brains across regions - normative models (task-optimized networks) show limited cross-region alignment compared to brain-to-brain alignment.

## Methodology

### Step 1: Data Collection

Collect neural responses across multiple brain regions:

```python
import numpy as np

def collect_multi_region_data(subjects, regions, stimuli):
    """
    Collect neural responses across multiple regions.
    
    Args:
        subjects: List of subject IDs
        regions: List of brain region names (e.g., ['V1', 'V2', 'V4', 'IT'])
        stimuli: Stimulus set
    
    Returns:
        brain_data: Dict mapping (subject, region) to response matrix
    """
    brain_data = {}
    
    for subject in subjects:
        for region in regions:
            # Load preprocessed fMRI or electrophysiology data
            responses = load_neural_data(subject, region, stimuli)
            brain_data[(subject, region)] = responses
    
    return brain_data
```

### Step 2: Model Response Collection

Collect responses from computational models:

```python
def collect_model_responses(models, stimuli, layers_by_region):
    """
    Collect model activations for each region's corresponding layers.
    
    Args:
        models: List of model instances (e.g., AlexNet, ResNet, task-optimized)
        stimuli: Same stimulus set used for brain data
        layers_by_region: Mapping of region names to model layer names
    
    Returns:
        model_data: Dict mapping (model, region) to activation matrix
    """
    model_data = {}
    
    for model in models:
        model_name = model.__class__.__name__
        
        for region, layer_name in layers_by_region.items():
            # Extract activations from specified layer
            activations = extract_layer_activations(model, layer_name, stimuli)
            model_data[(model_name, region)] = activations
    
    return model_data
```

### Step 3: Alignment Computation

Compute Representational Similarity Analysis (RSA) matrices:

```python
from scipy.spatial.distance import pdist, squareform
from scipy.stats import spearmanr

def compute_rdm(responses, metric='correlation'):
    """
    Compute Representational Dissimilarity Matrix.
    
    Args:
        responses: n_stimuli x n_features response matrix
        metric: Distance metric ('correlation', 'euclidean', etc.)
    
    Returns:
        rdm: n_stimuli x n_stimuli dissimilarity matrix
    """
    # Compute pairwise distances
    dist_vec = pdist(responses, metric=metric)
    rdm = squareform(dist_vec)
    return rdm


def compute_alignment_score(rdm1, rdm2, method='spearman'):
    """
    Compute alignment between two RDMs.
    
    Args:
        rdm1, rdm2: Representational dissimilarity matrices
        method: Correlation method ('spearman' or 'pearson')
    
    Returns:
        alignment: Correlation coefficient
        p_value: Significance level
    """
    # Vectorize upper triangles (excluding diagonal)
    idx = np.triu_indices_from(rdm1, k=1)
    vec1 = rdm1[idx]
    vec2 = rdm2[idx]
    
    if method == 'spearman':
        alignment, p_value = spearmanr(vec1, vec2)
    else:
        correlation = np.corrcoef(vec1, vec2)[0, 1]
        alignment = correlation
        p_value = None  # Would need permutation test
    
    return alignment, p_value
```

### Step 4: Cross-Region Analysis

Compute alignment patterns across regions:

```python
def compute_cross_region_alignment(data_dict, regions):
    """
    Compute cross-region alignment matrix.
    
    Args:
        data_dict: Dict mapping (source, region) to responses
        regions: List of region names
    
    Returns:
        alignment_matrix: Cross-region alignment scores
    """
    n_regions = len(regions)
    alignment_matrix = np.zeros((n_regions, n_regions))
    
    for i, region1 in enumerate(regions):
        for j, region2 in enumerate(regions):
            if i == j:
                alignment_matrix[i, j] = 1.0
                continue
            
            # Get all source responses for these regions
            rdm1_list = []
            rdm2_list = []
            
            for source in data_dict.keys():
                if isinstance(source, tuple):
                    src, reg = source
                else:
                    reg = None
                    for r in regions:
                        if (source, r) in data_dict:
                            reg = r
                            break
                
                if reg == region1:
                    rdm1_list.append(compute_rdm(data_dict[source]))
                if reg == region2:
                    rdm2_list.append(compute_rdm(data_dict[source]))
            
            # Compute average alignment
            alignments = []
            for rdm1 in rdm1_list:
                for rdm2 in rdm2_list:
                    if rdm1 is not rdm2:
                        score, _ = compute_alignment_score(rdm1, rdm2)
                        alignments.append(score)
            
            alignment_matrix[i, j] = np.mean(alignments) if alignments else 0
    
    return alignment_matrix
```

### Step 5: Pattern Comparison

Compare brain-to-brain vs. model-to-brain alignment:

```python
def compare_alignment_patterns(brain_matrix, model_matrices, region_names):
    """
    Compare cross-region alignment patterns.
    
    Args:
        brain_matrix: Brain-to-brain cross-region alignment
        model_matrices: Dict of model-to-brain alignment matrices
        region_names: List of region names
    
    Returns:
        comparison: Analysis results
    """
    results = {
        'brain_to_brain': {},
        'model_to_brain': {},
        'comparisons': {}
    }
    
    # Analyze brain-to-brain pattern
    brain_mean = np.mean(brain_matrix[np.triu_indices_from(brain_matrix, k=1)])
    brain_std = np.std(brain_matrix[np.triu_indices_from(brain_matrix, k=1)])
    results['brain_to_brain'] = {
        'mean_alignment': brain_mean,
        'std_alignment': brain_std,
        'pattern': brain_matrix
    }
    
    # Analyze each model
    for model_name, model_matrix in model_matrices.items():
        model_mean = np.mean(model_matrix[np.triu_indices_from(model_matrix, k=1)])
        model_std = np.std(model_matrix[np.triu_indices_from(model_matrix, k=1)])
        
        # Compute pattern similarity (correlation of alignment patterns)
        brain_vec = brain_matrix[np.triu_indices_from(brain_matrix, k=1)]
        model_vec = model_matrix[np.triu_indices_from(model_matrix, k=1)]
        pattern_corr = np.corrcoef(brain_vec, model_vec)[0, 1]
        
        results['model_to_brain'][model_name] = {
            'mean_alignment': model_mean,
            'std_alignment': model_std,
            'pattern_correlation': pattern_corr,
            'pattern': model_matrix
        }
        
        # Statistical comparison
        results['comparisons'][model_name] = {
            'mean_diff': brain_mean - model_mean,
            'pattern_similarity': pattern_corr,
            'captures_cross_region': pattern_corr > 0.5  # Threshold
        }
    
    return results
```

## Applications

### 1. Model Validation Pipeline

```python
def validate_model_comprehensive(model, brain_data, stimuli, regions):
    """
    Comprehensive model validation using CRAP analysis.
    
    Args:
        model: Computational model to validate
        brain_data: Multi-subject, multi-region brain data
        stimuli: Stimulus set
        regions: List of regions
    
    Returns:
        validation_report: Detailed validation results
    """
    # Collect model responses
    layers = identify_best_layers(model, regions, brain_data, stimuli)
    model_data = collect_model_responses([model], stimuli, layers)
    
    # Compute within-region alignment
    within_region_scores = {}
    for region in regions:
        brain_rdms = [compute_rdm(brain_data[(s, region)]) 
                      for s in subjects]
        model_rdm = compute_rdm(model_data[(model.__class__.__name__, region)])
        
        scores = [compute_alignment_score(b_rdm, model_rdm)[0] 
                  for b_rdm in brain_rdms]
        within_region_scores[region] = np.mean(scores)
    
    # Compute cross-region alignment
    brain_matrix = compute_cross_region_alignment(brain_data, regions)
    model_matrix = compute_cross_region_alignment(model_data, regions)
    
    comparison = compare_alignment_patterns(
        brain_matrix, 
        {model.__class__.__name__: model_matrix},
        regions
    )
    
    # Generate report
    report = {
        'within_region_alignment': within_region_scores,
        'cross_region_alignment': comparison,
        'overall_score': np.mean(list(within_region_scores.values())),
        'captures_global_dynamics': comparison['comparisons'][model.__class__.__name__]['captures_cross_region']
    }
    
    return report
```

### 2. Normative Model Comparison

Compare task-optimized vs. self-supervised vs. brain-predictive models:

```python
def compare_model_paradigms(models, brain_data, stimuli, regions):
    """
    Compare different model training paradigms.
    
    Model types:
    - Supervised (task-optimized)
    - Self-supervised (contrastive, predictive)
    - Brain-predictive (trained to predict brain activity)
    """
    results = {}
    
    for paradigm, model_list in models.items():
        paradigm_scores = []
        for model in model_list:
            report = validate_model_comprehensive(model, brain_data, stimuli, regions)
            paradigm_scores.append(report)
        
        results[paradigm] = {
            'mean_within_region': np.mean([r['overall_score'] for r in paradigm_scores]),
            'mean_cross_region': np.mean([
                r['cross_region_alignment']['comparisons'][model.__class__.__name__]['pattern_correlation']
                for r in paradigm_scores
            ]),
            'captures_global': np.mean([
                r['cross_region_alignment']['comparisons'][model.__class__.__name__]['captures_cross_region']
                for r in paradigm_scores
            ])
        }
    
    return results
```

## Key Findings

1. **Local vs. Global**: Models capture local representations well but fail at global coordination
2. **Task Optimization Limitation**: Task-optimized networks show strong single-region alignment but weak cross-region patterns
3. **Brain-Only Patterns**: Some cross-region patterns are unique to biological brains
4. **Implications for NeuroAI**: Need models that capture both local and global brain dynamics

## Best Practices

1. **Region Selection**: Include regions at different hierarchy levels
2. **Stimulus Diversity**: Use diverse stimuli that engage multiple regions
3. **Multiple Models**: Compare across training paradigms
4. **Statistical Testing**: Use permutation tests for significance

## References

- Höfling, L., et al. (2026). Only Brains Align with Brains: Cross-Region Alignment Patterns Expose Limits of Normative Models. arXiv:2604.21780v1
- Kriegeskorte, N., & Kievit, R.A. (2013). Representational geometry: Integrating cognition, computation, and the brain
- Yamins, D.L., et al. (2014). Performance-optimized hierarchical models predict neural responses in higher visual cortex

## Related Skills

- `brain-alignment-patterns-analysis`: General alignment pattern analysis
- `only-brains-align-brains`: Brain-to-brain alignment comparison
- `representation-steering`: LLM representation steering methods

## Activation Keywords

- cross-region alignment
- representation alignment
- brain model validation
- computational neuroscience
- neuroAI evaluation
- normative models