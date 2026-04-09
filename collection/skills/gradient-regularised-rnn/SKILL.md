# Gradient-Regularised RNN for Brain Hierarchy

**Source:** arXiv:2511.02722
**Utility:** 0.95
**Created:** 2026-03-25

## Activation Keywords

- gradient regularised RNN
- AS hierarchy
- sensory association gradient
- Ornstein-Uhlenbeck neural timescale
- functional gradient RNN
- schizophrenia gradient

## Description

A framework linking large-scale cortical architecture with neural computation stability using functional gradients to regularise recurrent neural networks (RNNs), with applications to understanding schizophrenia.

## Core Methodology

### 1. Association-Sensory (AS) Gradient Extraction

**Method:**
- Extract individual AS gradients via spectral analysis of brain connectivity
- Quantify hierarchical specialisation by gradient spread
- Relate spread with connectivity geometry

**Finding:** Schizophrenia compresses the AS hierarchy → reduced functional differentiation

### 2. Neural Timescale Modelling

**Method:** Ornstein-Uhlenbeck (OU) process

**Finding:**
- Most specialised regions at gradient extremes have longer time constants
- This effect is attenuated in schizophrenia

### 3. Gradient-Regularised RNN

**Purpose:** Study how cortical architecture affects computation

**Approach:**
1. Extract AS gradients from individual fMRI
2. Use gradients to regularise subject-specific RNNs
3. Train RNNs on working memory tasks
4. Analyse fixed point stability

**Key Results:**
- Networks with greater gradient spread learn more efficiently
- Lower task loss plateau
- Stronger alignment to prescribed AS geometry
- More stable neural states during memory delay
- Lower energy and smaller maximal Jacobian eigenvalues

### 4. Fixed Point Linearisation

**Analysis:**
- Examine fixed point stability during memory delay
- Compute energy landscape
- Calculate maximal Jacobian eigenvalues

## Implementation Framework

```python
# Conceptual pipeline
def gradient_regularised_rnn_pipeline(fmri_data, wm_task):
    # Step 1: Extract AS gradients
    connectivity = compute_functional_connectivity(fmri_data)
    as_gradient = spectral_gradient_analysis(connectivity)
    gradient_spread = quantify_spread(as_gradient)
    
    # Step 2: Build gradient-regularised RNN
    rnn = GradientRegularisedRNN(
        gradient_prior=as_gradient,
        regularisation_strength=gradient_spread
    )
    
    # Step 3: Train on working memory task
    rnn.train(wm_task)
    
    # Step 4: Analyse fixed points
    fixed_points = find_fixed_points(rnn)
    stability = compute_jacobian_eigenvalues(fixed_points)
    
    return {
        'gradient_spread': gradient_spread,
        'task_loss': rnn.loss,
        'fixed_point_stability': stability
    }
```

## Applications

1. **Neuropsychiatric Research**
   - Understanding schizophrenia through gradient compression
   - Linking cortical architecture to computation

2. **Working Memory Modelling**
   - Subject-specific RNN models
   - Stability analysis of memory states

3. **Brain-Computational Bridge**
   - Connecting macroscale gradients to microscale dynamics
   - Mechanistic accounts of disease

## When to Use

- Studying cortical hierarchy and specialisation
- Building subject-specific neural network models
- Investigating computational consequences of brain disorders
- Working memory task modelling
- Analysing fixed point stability in RNNs

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: Neuropsychiatric Research

### Step 2: Working Memory Modelling

### Step 3: Brain-Computational Bridge

### Step 4: Understand the Request

### Step 5: Search for Information

### When to Apply
- Studying cortical hierarchy and specialisation
- Building subject-specific neural network models
- Investigating computational consequences of brain disorders

## Examples

### Example 1: Basic Application

**User:** I need to apply Gradient-Regularised RNN for Brain Hierarchy to my analysis.

**Agent:** I'll help you apply gradient-regularised-rnn. First, let me understand your specific use case...

**Context:** Association-Sensory (AS) Gradient Extraction

### Example 2: Advanced Scenario

**User:** Studying cortical hierarchy and specialisation

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for gradient-regularised-rnn?

**Agent:** Let me search for the latest research and best practices...

## Related Skills

- `kuramoto-brain-network` - Oscillator-based brain modelling
- `time-varying-brain-connectivity` - Dynamic connectivity analysis
- `functional-connectome-fingerprint` - Individual connectivity patterns

## References

- Abulikemu, S., et al. "Association-sensory spatiotemporal hierarchy and functional gradient-regularised recurrent neural network with implications for schizophrenia." arXiv:2511.02722 (2025)
- Ornstein-Uhlenbeck process for neural timescale modelling