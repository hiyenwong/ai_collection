---
name: flow-matching-in-context-brain-dynamics
description: Flow Matching with In-Context Priors for Out-of-Distribution Brain Dynamics methodology. First generative model of whole-cortex fMRI dynamics for unseen cognitive tasks. Per-timestep conditioned diffusion transformer with compositional language priors and spatial priors for counterfactual neuroscience.
---

# Flow Matching with In-Context Priors for Brain Dynamics

**arXiv ID**: 2606.11833
**Authors**: Sam Gijsen, Michał Łukomski, Marc-André Schulz, Kerstin Ritter
**Published**: 2026-06-10
**URL**: https://arxiv.org/abs/2606.11833

## Problem Statement

Generative models of neural time series (fMRI) have remained restricted to categorical conditioning, precluding:
- Compositional generalization
- Zero-shot generation
- Counterfactual neuroscience experiments

Existing approaches cannot generate realistic brain dynamics for unseen cognitive tasks.

## Key Innovation

**First generative model of whole-cortex fMRI dynamics for unseen cognitive tasks** using:
- Per-timestep conditioned diffusion transformer
- Compositional language priors (in-context)
- Optional spatial priors (in-context)

## Architecture

### Dual Conditioning Pathway

1. **Language Priors**: Compositional task descriptions injected in-context
2. **Spatial Priors**: Optional region-specific activation patterns
3. **Synergy**: Spatial priors anchor generation where language alone degrades

### Diffusion Transformer

- Per-timestep conditioning
- Zero-shot generation capability
- Held-out task evaluation across hundreds of conditions

## Results

### Language Pathway
- Recovers region-specific recruitment across tasks
- Predicts held-out spatial activation patterns
- Compositional structure preserved

### Spatial + Language
- Anchors generation in degraded regions
- Maintains compositional counterfactual specification
- Superior performance vs language alone

## Applications

### Counterfactual Neuroscience
- In-silico design of novel cognitive experiments
- Pre-empirical validation of hypotheses
- Data-driven experimental design

### Zero-Shot Generation
- Unseen cognitive tasks from language descriptions
- Compositional task combinations
- Novel experiment prototyping

## Methodology

### 1. Training
- Train on known cognitive tasks
- Condition per-timestep with language descriptions
- Optional spatial prior injection

### 2. Generation
- Language-only: zero-shot from descriptions
- Language + Spatial: anchored generation
- Evaluate across held-out task manifold

### 3. Validation
- Region-specific recruitment recovery
- Spatial activation pattern accuracy
- Training manifold characterization

## Use Cases

- Design cognitive experiments before empirical testing
- Generate brain activity for novel task combinations
- Predict fMRI patterns for unseen tasks
- Counterfactual neuroscience simulations

## Cross-Domain Connections

- **Brain Dynamics**: fMRI generative modeling
- **Flow Matching**: Diffusion transformers
- **Zero-Shot Learning**: Language-conditioned generation
- **Counterfactual Reasoning**: In-silico experiments

## Activation Keywords

`counterfactual neuroscience`, `zero-shot fMRI`, `flow matching brain`, `in-context priors`, `diffusion transformer brain`, `generative brain dynamics`, `language-conditioned fMRI`

## Code Availability

Available at: (link in arXiv comments)
