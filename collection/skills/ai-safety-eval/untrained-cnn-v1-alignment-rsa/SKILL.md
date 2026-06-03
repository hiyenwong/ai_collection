---
name: untrained-cnn-v1-alignment-rsa
description: Systematic RSA comparison showing that untrained CNNs achieve V1/V2 alignment comparable to backpropagation-trained networks. Reveals architecture-driven vs objective-driven cortical alignment across visual hierarchy.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [RSA, representational-similarity, CNN, visual-cortex, V1, learning-rules, STDP, predictive-coding, feedback-alignment]
    source_paper: "Untrained CNNs Match Backpropagation at V1: A Systematic RSA Comparison of Four Learning Rules Against Human fMRI (arXiv:2604.16875)"
    authors: "Nils Leutenegger"
    published: "2026-04-18"
---

# Untrained CNNs Match Backpropagation at V1: RSA Analysis

## Overview

This paper systematically compares four learning rules (BP, FA, PC, STDP) against human fMRI data using Representational Similarity Analysis (RSA). The key finding: **early visual alignment (V1/V2) is primarily architecture-driven**, not learning-driven. An untrained CNN achieves V1 alignment statistically indistinguishable from backpropagation.

## Key Findings

| Visual Area | Dominant Factor | Best Method |
|-------------|----------------|-------------|
| V1/V2 | Architecture | Untrained = BP (rho = 0.071 vs 0.072, p = 0.43) |
| LOC | Learning objective | BP dominates |
| IT | Learning objective | BP = PC with local Hebbian (p = 0.18) |

### Critical Results

- **FA consistently impairs** representations below random baseline at V1
- **PC with local Hebbian updates** achieves IT alignment indistinguishable from BP
- **Partial RSA** confirms all effects survive pixel-similarity control
- **Region-specific effects**: Architecture determines early alignment, supervised objectives drive late alignment

## RSA Implementation

```python
import numpy as np
from scipy.spatial.distance import cdist
from scipy.stats import spearmanr

def representational_similarity_analysis(model_activations, brain_data):
    """
    Compute Representational Similarity Analysis between
    model and brain representational dissimilarity matrices.
    
    Args:
        model_activations: (n_stimuli, n_units)
        brain_data: (n_stimuli, n_voxels)
    
    Returns:
        rho: Spearman correlation between RDMs
        p_value: Statistical significance
    """
    # Compute RDMs (Representational Dissimilarity Matrices)
    model_rdm = cdist(model_activations, model_activations, metric='correlation')
    brain_rdm = cdist(brain_data, brain_data, metric='correlation')
    
    # Extract upper triangular (excluding diagonal)
    triu_idx = np.triu_indices_from(model_rdm, k=1)
    model_rdm_vec = model_rdm[triu_idx]
    brain_rdm_vec = brain_rdm[triu_idx]
    
    # Spearman correlation between RDMs
    rho, p_value = spearmanr(model_rdm_vec, brain_rdm_vec)
    
    return rho, p_value

def partial_rsa_control(model_rdm, brain_rdm, control_rdm):
    """
    Partial RSA controlling for pixel similarity.
    """
    from pingouin import partial_corr
    
    triu_idx = np.triu_indices_from(model_rdm, k=1)
    
    result = partial_corr(
        data={
            'x': model_rdm[triu_idx],
            'y': brain_rdm[triu_idx],
            'covar': control_rdm[triu_idx]
        }
    )
    return result['r'].iloc[0], result['p-val'].iloc[0]
```

## Learning Rule Comparison Framework

```python
learning_rules = {
    'BP': 'Backpropagation - supervised gradient descent',
    'FA': 'Feedback Alignment - random feedback weights',
    'PC': 'Predictive Coding - local prediction error minimization',
    'STDP': 'Spike-Timing-Dependent Plasticity - unsupervised Hebbian',
    'Untrained': 'Random weights - architecture-only baseline'
}

def systematic_comparison(architecture, training_data, brain_data):
    """
    Systematic comparison of learning rules across visual areas.
    """
    results = {}
    
    for rule_name in learning_rules:
        if rule_name == 'Untrained':
            model = create_random_weights(architecture)
        else:
            model = train_with_rule(architecture, rule_name, training_data)
        
        for area in ['V1', 'V2', 'LOC', 'IT']:
            activations = model.get_layer_activations(area)
            rho, p = representational_similarity_analysis(
                activations, brain_data[area]
            )
            results[(rule_name, area)] = {'rho': rho, 'p': p}
    
    return results
```

## Implications for Neuroscience

1. **Architecture > Learning for Early Vision**: V1/V2 alignment is determined by CNN architecture, not training
2. **Biologically Plausible Learning**: PC with local Hebbian updates can match BP at IT
3. **FA Limitations**: Feedback alignment impairs early visual representations
4. **Hierarchical Processing**: Different visual areas require different alignment mechanisms

## Applications

- Evaluating neural network models against brain data
- Understanding visual hierarchy processing
- Designing brain-inspired architectures
- Testing biological plausibility of learning rules

## References

- Untrained CNNs Match Backpropagation at V1: A Systematic RSA Comparison of Four Learning Rules Against Human fMRI
- Author: Nils Leutenegger
- arXiv: 2604.16875
- Published: 2026-04-18
- Categories: cs.LG, q-bio.NC

## Related Skills
- [[vlm-visual-cortex-alignment-robustness]]
- [[neuroscience-of-transformers]]
- [[eeg-visual-attention-decoding]]
