---
name: errorless-irrationality-inverse-base-rate-effect
title: Errorless Irrationality Inverse Base-Rate Effect Across Learning Procedures
version: 1.0.0
description: Unified computational account of the inverse base-rate effect that persists across predictive, observational, and unsupervised learning procedures, proposing the OSCAR model based on self-generated feedback and pattern completion dynamics.
author: Lenard Dome, Andy J. Wills
arxiv_id: 2608.06149
date: 2026-08-07
tags:
  - inverse base-rate effect
  - computational modeling
  - irrationality
  - OSCAR model
  - auto-associator network
  - pattern completion
  - supervised learning
  - observational learning
  - unsupervised learning
---

# Errorless Irrationality: Inverse Base-Rate Effect Across Learning Procedures

## Overview

This methodology presents a unified computational account of the inverse base-rate effect (IBRE) – a robust cognitive bias where people overweigh rare events when resolving ambiguity between competing categories. The key finding is that this "irrational" bias persists across predictive (supervised), observational, and unsupervised learning procedures, demonstrating its independence from traditional prediction error signals.

The authors propose OSCAR (Optimal Self-Generated Category Assignment through Reconstruction), a new computational model that integrates core principles from established models and operates on self-generated feedback mechanisms similar to pattern completion in auto-associative networks.

## Key Contributions

### Empirical Findings
- **Procedure independence**: The inverse base-rate effect persists even when category labels are not presented (unsupervised procedure)
- **Individual differences**: First model to reproduce the pattern of individual differences seen in humans across all three learning procedures
- **Eye-tracking explanation**: Provides explanation for previously unexplained eye-tracking data that alternative accounts cannot address

### OSCAR Model Architecture
- **Auto-associator foundation**: Based on neural network architecture with self-generated feedback
- **Pattern completion dynamics**: Uses reconstruction-based feedback similar to hippocampal pattern completion
- **Self-generated category assignment**: Operates without external supervision by generating internal category representations
- **Integrated computational principles**: Combines strengths of existing validated models (GCM, ALCOVE, SUSTAIN)

### Theoretical Implications
- **Beyond prediction error**: Challenges dominant theories that explain IBRE solely through prediction error mechanisms
- **Unified framework**: Provides single computational account that works across different learning paradigms
- **Biological plausibility**: Pattern completion mechanism aligns with known hippocampal and cortical processing

## Methodology Components

### Experimental Design
1. **Predictive learning**: Traditional supervised categorization with explicit feedback
2. **Observational learning**: Passive observation of category exemplars without active prediction
3. **Unsupervised procedure**: No category labels presented, purely unsupervised structure discovery

### Model Evaluation
- **Large pre-existing dataset**: Tested on extensive supervised learning dataset
- **New experimental data**: Validated against two new experiments reported in the paper
- **Individual differences**: Reproduces human patterns of individual variation across procedures
- **Eye-tracking validation**: Explains previously unexplained eye movement patterns

### Computational Implementation
- **Feature representation**: Encodes stimulus features in distributed representation space
- **Category prototypes**: Maintains prototype representations for each category
- **Reconstruction feedback**: Generates internal feedback through pattern completion
- **Decision dynamics**: Resolves ambiguity through competitive activation dynamics

## Implementation Guidelines

### Network Architecture
```
- Input layer: Stimulus feature representation
- Hidden layer: Distributed category representation  
- Output layer: Category assignment probabilities
- Feedback connections: Auto-associative reconstruction pathways
- Competitive dynamics: Lateral inhibition between category units
```

### Learning Procedure
1. **Initialization**: Set initial category prototypes and connection weights
2. **Stimulus presentation**: Present feature vector to input layer
3. **Forward pass**: Activate category representations based on similarity
4. **Pattern completion**: Generate reconstructed stimulus through feedback
5. **Self-generated feedback**: Compare original vs reconstructed stimulus
6. **Weight update**: Modify connections based on reconstruction error
7. **Decision making**: Apply competitive dynamics for final category assignment

### Parameter Configuration
- **Similarity metric**: Configure distance function for feature comparison
- **Learning rate**: Adjust speed of prototype adaptation
- **Competition strength**: Control lateral inhibition between categories
- **Reconstruction fidelity**: Balance between accuracy and generalization

## Applications

### Cognitive Science Research
- **Bias investigation**: Study systematic deviations from rational decision-making
- **Learning mechanism analysis**: Understand how different learning procedures shape cognition
- **Individual differences**: Model variation in cognitive strategies across populations
- **Neural correlates**: Generate testable predictions for neuroimaging studies

### Artificial Intelligence
- **Robust categorization**: Develop AI systems that handle ambiguous classification
- **Unsupervised learning**: Create models that discover structure without explicit labels
- **Human-like reasoning**: Build systems that exhibit realistic cognitive biases
- **Adaptive decision-making**: Implement flexible categorization under uncertainty

### Clinical Applications
- **Cognitive assessment**: Use IBRE as diagnostic marker for cognitive disorders
- **Therapeutic intervention**: Design training protocols to address maladaptive biases
- **Decision support**: Develop tools that compensate for systematic reasoning errors

## Validation Framework

### Baseline Comparisons
- **GCM (Generalized Context Model)**: Exemplar-based categorization model
- **ALCOVE**: Attention-learning model with error-driven attention shifts  
- **SUSTAIN**: Clustering-based model with adaptive category formation
- **Random baseline**: Chance-level performance on categorization tasks

### Performance Metrics
- **Categorization accuracy**: Overall performance across conditions
- **IBRE magnitude**: Strength of inverse base-rate bias in ambiguous trials
- **Individual fit**: Correlation between model and human individual differences
- **Cross-procedure generalization**: Performance consistency across learning paradigms

### Robustness Tests
- **Parameter sensitivity**: Test stability across parameter variations
- **Architecture variations**: Evaluate different network configurations
- **Dataset generalization**: Apply to novel categorization problems
- **Noise tolerance**: Assess performance under noisy input conditions

## Integration Examples

### For Cognitive Modeling
```python
# Example implementation framework
class OSCARModel:
    def __init__(self, n_features, n_categories):
        self.prototypes = initialize_prototypes(n_features, n_categories)
        self.weights = initialize_weights(n_features, n_categories)
        self.competition_strength = 0.5
        
    def forward_pass(self, stimulus):
        # Compute similarity to prototypes
        similarities = compute_similarities(stimulus, self.prototypes)
        # Apply competitive dynamics
        activations = apply_competition(similarities, self.competition_strength)
        return activations
        
    def pattern_completion(self, stimulus, activations):
        # Reconstruct stimulus from category activations
        reconstructed = np.dot(activations, self.weights.T)
        return reconstructed
        
    def update_weights(self, stimulus, reconstructed, activations):
        # Update based on reconstruction error
        error = stimulus - reconstructed
        self.weights += learning_rate * np.outer(activations, error)
        # Update prototypes
        self.prototypes += learning_rate * error.reshape(-1, 1) * activations
```

### For Experimental Design
```python
# Testing across learning procedures
def test_ibre_across_procedures():
    model = OSCARModel(n_features=10, n_categories=2)
    
    # Predictive learning (supervised)
    predictive_accuracy, predictive_ibre = run_predictive_experiment(model)
    
    # Observational learning  
    observational_accuracy, observational_ibre = run_observational_experiment(model)
    
    # Unsupervised learning
    unsupervised_accuracy, unsupervised_ibre = run_unsupervised_experiment(model)
    
    # Verify IBRE persists across all procedures
    assert all(ibre > 0 for ibre in [predictive_ibre, observational_ibre, unsupervised_ibre])
    return predictive_ibre, observational_ibre, unsupervised_ibre
```

## References

- Dome, L., & Wills, A. J. (2026). Errorless Irrationality: A unified computational account of the inverse base-rate effect across predictive, observational, and unsupervised procedures. arXiv:2608.06149 [q-bio.NC].
- Medin, D. L., & Edelson, S. M. (1988). Problem structure and the use of base-rate information from experience. Journal of Experimental Psychology: General, 117(1), 68–85.
- Nosofsky, R. M. (1986). Attention, similarity, and the identification–categorization relationship. Journal of Experimental Psychology: General, 115(1), 39–57.
- Love, B. C., Medin, D. L., & Gureckis, T. M. (2004). SUSTAIN: a network model of category learning. Psychological review, 111(2), 309.

## Activation Keywords

Use this methodology when: studying inverse base-rate effects, modeling cognitive biases in categorization, developing computational models of irrational decision-making, investigating pattern completion in neural networks, analyzing individual differences in learning strategies, or creating unified frameworks for supervised/unsupervised learning integration.