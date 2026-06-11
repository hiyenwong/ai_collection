---
name: flow-matching-in-context-priors-brain-dynamics
description: Flow matching with in-context priors for generating out-of-distribution fMRI brain dynamics, enabling zero-shot generation of unseen cognitive tasks
version: 1.0.0
author: Sam Gijsen, Michał Łukomski, Marc-André Schulz, Kerstin Ritter
arxiv_id: 2606.11833v1
published: 2026-06-10
categories: [cs.LG, q-bio.NC]
activation_keywords: [flow matching, brain dynamics, fMRI generation, counterfactual neuroscience, in-context priors, diffusion transformer, zero-shot]
github: https://github.com/SamGijsen/pinc-flows
---

# Flow Matching with In-Context Priors for Out-of-Distribution Brain Dynamics

## Overview

This methodology proposes a **per-timestep conditioned diffusion transformer** for generating realistic fMRI brain dynamics during **unseen cognitive tasks** by injecting both compositional language and optional spatial priors in-context. It enables **counterfactual neuroscience** by supporting in-silico design and evaluation of novel cognitive experiments before empirical validation.

**Key Innovation**: First generative model of whole-cortex fMRI dynamics for unseen cognitive tasks with zero-shot generalization.

## Core Concepts

### 1. Per-Timestep Conditioned Diffusion Transformer
Architecture combines:
- **Diffusion transformer backbone**: Processes 4D fMRI signals
- **Timestep conditioning**: Injects task-specific context at each diffusion step
- **Multi-modal priors**: Language + optional spatial activation patterns

### 2. In-Context Prior Injection
Two complementary pathways:

#### Language Pathway
```python
def inject_language_prior(task_description, timestep):
    """
    Encode compositional task description
    Inject into diffusion process at timestep t
    """
    # Encode task as compositional language
    task_embedding = language_encoder(task_description)
    
    # Condition diffusion step
    conditioned_latent = diffusion_step(
        latent_z_t,
        condition=task_embedding,
        timestep=timestep
    )
    return conditioned_latent
```

#### Spatial Prior Pathway (Optional)
```python
def inject_spatial_prior(activation_pattern, timestep):
    """
    Anchor generation in specific brain regions
    Complements language pathway where language degrades
    """
    # Encode spatial activation pattern
    spatial_embedding = spatial_encoder(activation_pattern)
    
    # Combine with language pathway
    combined_prior = combine(
        language_prior,
        spatial_prior,
        weights=[0.6, 0.4]  # Adaptive weighting
    )
    return combined_prior
```

### 3. Zero-Shot Generation Pipeline

**Training Phase**:
- Train diffusion transformer on known cognitive tasks
- Learn joint manifold of task language + fMRI dynamics
- Encode compositional task structure

**Zero-Shot Generation Phase**:
1. Specify novel task in compositional language
2. Optionally provide spatial prior (if available)
3. Generate fMRI dynamics for unseen task
4. Validate against held-out task conditions

## Implementation Architecture

### Model Components

```
PINC-Flows Architecture:
├── Language Encoder (Transformer)
│   └── Compositional task description → Task embedding
├── Spatial Encoder (optional)
│   └── ROI activation patterns → Spatial prior
├── Diffusion Transformer Backbone
│   ├── Multi-head attention for temporal dependencies
│   ├── Spatial attention for cortical connectivity
│   └── Timestep conditioning module
├── Renderer
│   └── Latent space → 4D fMRI volumes
```

### Training Procedure

1. **Data Collection**: fMRI time series from multiple cognitive tasks
2. **Task Encoding**: Compositional language descriptions
3. **Diffusion Training**: Learn denoising process conditioned on task embeddings
4. **Multi-task Learning**: Joint training across task manifold

### Inference Procedure

```python
def generate_counterfactual_fMRI(
    novel_task_description,
    spatial_prior=None,
    num_steps=1000
):
    """
    Zero-shot generation for unseen cognitive task
    """
    # Initialize latent
    z_T = sample_noise(shape=[time, space])
    
    # Iterative denoising with task conditioning
    for t in reversed(range(num_steps)):
        # Inject in-context priors
        task_condition = encode_task(novel_task_description)
        if spatial_prior:
            task_condition = combine(task_condition, spatial_prior)
        
        # Diffusion step
        z_t = denoise_step(
            z_{t+1},
            condition=task_condition,
            timestep=t
        )
    
    # Render to fMRI space
    fMRI_dynamics = render(z_0)
    return fMRI_dynamics
```

## Key Findings

### 1. Language-Only Generation
From language descriptions alone, model recovers:
- **Region-specific recruitment** across tasks
- **Held-out spatial activation patterns**
- **Compositional task structure**

### 2. Spatial Prior Benefits
Spatial priors complement language pathway:
- Anchor generation where language alone degrades
- Retain compositional structure for counterfactuals
- Improve generation fidelity in specific ROIs

### 3. Training Manifold Relationship
Characterized predictive performance:
- Near-manifold tasks: High fidelity generation
- Far-from-manifold tasks: Graceful degradation
- Counterfactual extrapolation: Maintains biological plausibility

## Applications

### 1. Counterfactual Neuroscience
- Design novel cognitive experiments in-silico
- Predict brain responses to unseen task combinations
- Reduce cost of exploratory neuroscience studies

### 2. Data-Driven Experimental Design
- Generate synthetic fMRI for hypothesis testing
- Optimize task parameters before real experiments
- Estimate expected activation patterns

### 3. Brain Dynamics Modeling
- Test causal hypotheses about task-brain relationships
- Model individual variability in task responses
- Predict effects of task manipulations

### 4. Foundation Model Enhancement
- Use generated data for fMRI foundation model training
- Augment scarce neuroimaging datasets
- Enable multi-task pre-training

## Experimental Validation

### Dataset
- Hundreds of held-out task conditions
- Whole-cortex fMRI dynamics
- Compositional task descriptions

### Metrics
- Spatial activation pattern recovery
- Region-specific recruitment accuracy
- Biological plausibility measures

### Results
- Language pathway alone recovers spatial patterns
- Spatial priors enhance regions where language degrades
- Compositional structure preserved for counterfactuals

## Limitations & Considerations

1. **Language Prior Quality**: Depends on task description precision
2. **Spatial Prior Availability**: Optional but beneficial for specific ROIs
3. **Training Manifold Coverage**: Limited by training task diversity
4. **Biological Validation**: Generated dynamics need empirical verification

## Future Directions

1. Extend to **resting-state** fMRI generation
2. Add **temporal prior** pathway (sequence predictions)
3. Combine with **clinical** datasets (patient populations)
4. Develop **task optimizer** using generated feedback

## Related Work

This advances beyond:
- **Categorical conditioning**: Traditional diffusion models
- **Task-specific models**: No zero-shot capability
- **Static generation**: Missing temporal dynamics

## Implementation Details

### Hyperparameters
- Diffusion steps: 1000
- Backbone: Diffusion Transformer
- Conditioning: Per-timestep injection
- Training: Multi-task joint learning

### Code Availability
- GitHub: https://github.com/SamGijsen/pinc-flows
- Pretrained models included
- Zero-shot generation scripts

## References

- arXiv: 2606.11833v1
- Authors: Sam Gijsen, Michał Łukomski, Marc-André Schulz, Kerstin Ritter
- Published: 2026-06-10
- Code: https://github.com/SamGijsen/pinc-flows

## Related Skills

- [[brain-dit-fmri-foundation-model]]
- [[flow-matching-neural-dynamics]]
- [[generative-brain-dynamics-models]]
- [[counterfactual-brain-dynamics]]