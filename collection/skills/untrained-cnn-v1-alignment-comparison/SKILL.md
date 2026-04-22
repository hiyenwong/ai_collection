---
name: untrained-cnn-v1-alignment-comparison
description: "Systematic RSA comparison of learning rules against human fMRI. Shows that architecture (not learning rule) drives early visual alignment at V1. BP, FA, PC, STDP compared on identical CNNs. Activation: RSA fMRI comparison, visual cortex alignment, learning rules neuroscience, untrained CNN V1, predictive coding visual, feedback alignment, STDP fMRI"
---

# Systematic RSA Comparison of Learning Rules Against Human fMRI at V1

## Overview

This skill provides methodology for systematically comparing neural network learning rules against human brain activity (fMRI) using Representational Similarity Analysis (RSA). The key finding: **early visual alignment (V1/V2) is primarily architecture-driven, not learning-rule-driven**.

## Source Paper

- **Title**: Untrained CNNs Match Backpropagation at V1: A Systematic RSA Comparison of Four Learning Rules Against Human fMRI
- **arXiv**: https://arxiv.org/abs/2604.16875
- **Published**: 2026-04-18
- **Categories**: cs.LG, q-bio.NC

## Core Concepts

### 1. Architecture vs Learning Rule Distinction

| Visual Area | Primary Driver | Untrained CNN | Best Learning Rule |
|-------------|---------------|---------------|-------------------|
| V1/V2 | **Architecture** | ρ = 0.071 (BP: ρ = 0.072, p = 0.43) | No significant difference |
| LOC/IT | **Learning Rule** | Low alignment | BP dominates |
| IT | **Learning Rule** | Low alignment | PC ≈ BP (p = 0.18) |

### 2. Learning Rules Compared

| Learning Rule | Type | V1 Alignment | IT Alignment | Notes |
|--------------|------|-------------|-------------|-------|
| Backpropagation (BP) | Supervised | Baseline | Best | Gold standard |
| Feedback Alignment (FA) | Approximate BP | **Below random** | Poor | Impairs representations |
| Predictive Coding (PC) | Local Hebbian | Moderate | ≈ BP | Local updates work |
| STDP | Unsupervised | Moderate | Low | No labels needed |
| Random weights | Untrained | ≈ BP at V1 | Low | **Architecture matters** |

### 3. RSA Methodology

Representational Similarity Analysis pipeline:
1. Extract RDMs (Representational Dissimilarity Matrices) from model layers
2. Extract RDMs from fMRI data (THINGS-fMRI: 720 stimuli, 3 subjects)
3. Compute correlation between model and brain RDMs
4. Partial RSA controls for pixel similarity
5. Statistical testing with permutation

## Implementation

```python
import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.stats import pearsonr, spearmanr

def compute_rdm(activations):
    """
    Compute Representational Dissimilarity Matrix.
    
    Args:
        activations: [n_stimuli, n_features] activation matrix
    
    Returns:
        RDM: [n_stimuli, n_stimuli] dissimilarity matrix
    """
    # Cosine dissimilarity
    distances = pdist(activations, metric='cosine')
    rdm = squareform(distances)
    return rdm


def rsa_correlation(model_activations, brain_activations):
    """
    Compute RSA correlation between model and brain representations.
    
    Returns:
        correlation: Spearman rank correlation
        p_value: Statistical significance
    """
    model_rdm = compute_rdm(model_activations)
    brain_rdm = compute_rdm(brain_activations)
    
    # Extract upper triangle (symmetric matrix)
    model_upper = model_rdm[np.triu_indices_from(model_rdm, k=1)]
    brain_upper = brain_rdm[np.triu_indices_from(brain_rdm, k=1)]
    
    correlation, p_value = spearmanr(model_upper, brain_upper)
    return correlation, p_value


def partial_rsa(model_activations, brain_activations, control_features):
    """
    Partial RSA controlling for pixel similarity.
    
    Args:
        control_features: [n_stimuli, n_pixels] pixel features to control for
    """
    from scipy.stats import partial_correlation
    
    control_rdm = compute_rdm(control_features)
    control_upper = control_rdm[np.triu_indices_from(control_rdm, k=1)]
    
    model_rdm = compute_rdm(model_activations)
    brain_rdm = compute_rdm(brain_activations)
    model_upper = model_rdm[np.triu_indices_from(model_rdm, k=1)]
    brain_upper = brain_rdm[np.triu_indices_from(brain_rdm, k=1)]
    
    # Partial correlation controlling for pixel similarity
    X = np.column_stack([model_upper, brain_upper, control_upper])
    # Compute partial correlation between model and brain, controlling for pixels
    # (simplified implementation)
    residual_model = np.linalg.lstsq(control_upper.reshape(-1, 1), 
                                      model_upper, rcond=None)[1]
    residual_brain = np.linalg.lstsq(control_upper.reshape(-1, 1),
                                      brain_upper, rcond=None)[1]
    return spearmanr(residual_model, residual_brain)


class RSABenchmark:
    """
    Systematic RSA benchmark for comparing learning rules.
    """
    
    def __init__(self, brain_data, stimuli_names):
        """
        Args:
            brain_data: dict mapping brain_region -> [n_stimuli, n_voxels]
            stimuli_names: list of stimulus identifiers
        """
        self.brain_data = brain_data
        self.stimuli_names = stimuli_names
        self.results = {}
    
    def evaluate_model(self, model_name, layer_activations, brain_region='V1'):
        """Evaluate a model's alignment with brain data."""
        if brain_region not in self.brain_data:
            raise ValueError(f"Unknown brain region: {brain_region}")
        
        corr, p_value = rsa_correlation(
            layer_activations,
            self.brain_data[brain_region]
        )
        
        self.results[(model_name, brain_region)] = {
            'correlation': corr,
            'p_value': p_value,
            'n_stimuli': len(self.stimuli_names)
        }
        return corr, p_value
    
    def compare_learning_rules(self, model_activations_by_rule, brain_region='V1'):
        """
        Compare multiple learning rules against brain data.
        
        Args:
            model_activations_by_rule: dict {rule_name: [n_stimuli, n_features]}
        """
        results = {}
        for rule, activations in model_activations_by_rule.items():
            corr, p_value = self.evaluate_model(
                rule, activations, brain_region
            )
            results[rule] = {'correlation': corr, 'p_value': p_value}
        
        # Rank by correlation
        ranked = sorted(results.items(), 
                       key=lambda x: x[1]['correlation'], 
                       reverse=True)
        
        return ranked
    
    def test_architecture_vs_learning(self, 
                                       untrained_activations,
                                       trained_activations_by_rule,
                                       brain_region='V1'):
        """
        Test whether architecture or learning rule drives alignment.
        
        Returns:
            architecture_effect: Effect size of architecture
            learning_effect: Effect size of learning rule
            conclusion: Interpretation
        """
        # Architecture effect: untrained vs random baseline
        architecture_corr, _ = self.evaluate_model(
            'untrained', untrained_activations, brain_region
        )
        
        # Learning effects: each rule vs untrained
        learning_effects = {}
        for rule, activations in trained_activations_by_rule.items():
            rule_corr, _ = self.evaluate_model(
                rule, activations, brain_region
            )
            learning_effects[rule] = rule_corr - architecture_corr
        
        # Statistical conclusion
        max_learning_delta = max(abs(v) for v in learning_effects.values())
        
        if max_learning_delta < 0.01:
            conclusion = f"Architecture-driven (V1/V2 pattern): "                         f"untrained ({architecture_corr:.3f}) ≈ best trained"
        else:
            best_rule = max(learning_effects, key=learning_effects.get)
            conclusion = f"Learning-rule-driven: {best_rule} best "                         f"(+{learning_effects[best_rule]:.3f})"
        
        return {
            'architecture_correlation': architecture_corr,
            'learning_effects': learning_effects,
            'conclusion': conclusion
        }
```

## Practical Applications

### 1. Model-to-Brain Alignment Research
- Benchmark new architectures against human brain data
- Determine which visual areas are architecture vs learning sensitive
- Guide architecture selection for brain-inspired AI

### 2. Learning Rule Evaluation
- Assess biological plausibility of learning rules
- Compare FA, PC, STDP against BP for cortical alignment
- Identify region-specific learning rule effects

### 3. Brain-Inspired AI Design
- Use architecture priors for early visual processing
- Use supervised learning for higher-level representations
- Hybrid approaches: architectural constraints + local learning

## Key Insights

1. **Architecture Dominates Early Vision**: V1/V2 alignment is primarily driven by convolutional architecture, not the learning rule — even random weights achieve similar alignment
2. **Learning Rules Matter for Higher Areas**: LOC/IT alignment requires proper learning signals (BP or PC)
3. **Feedback Alignment is Harmful**: FA consistently performs below random baseline at V1
4. **Predictive Coding is Competitive**: PC with local Hebbian updates achieves IT alignment statistically indistinguishable from BP
5. **Pixel Similarity Control**: All effects survive partial RSA controlling for low-level pixel features

## Experimental Setup

Based on THINGS-fMRI dataset:
- **720 stimuli** across diverse object categories
- **3 subjects** for cross-subject validation
- **Multiple brain regions**: V1, V2, V3, V4, LOC, IT
- **Partial RSA**: Controls for pixel-level similarity

## Related Skills
- [[neuroscience-of-transformers]]
- [[neural-encoding-evaluation-ground-truth]]
- [[computational-neuroscience-in-llm-era]]
- [[vlm-visual-cortex-alignment-robustness]]

## Activation Keywords
- RSA fMRI comparison
- visual cortex alignment
- learning rules neuroscience
- untrained CNN V1
- predictive coding visual
- feedback alignment
- STDP fMRI
- representational similarity analysis
- brain-model alignment
