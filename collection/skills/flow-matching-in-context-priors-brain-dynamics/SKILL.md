# Flow Matching with In-Context Priors for Out-of-Distribution Brain Dynamics

## Overview
Flow Matching with In-Context Priors for Out-of-Distribution Brain Dynamics - First generative model of whole-cortex fMRI dynamics for unseen cognitive tasks, advancing counterfactual neuroscience and data-driven experimental design.

**arXiv ID**: 2606.11833v1
**Authors**: Sam Gijsen, Michał Łukomski, Marc-André Schulz, Kerstin Ritter
**Updated**: 2026-06-10

## Problem
- Generative models of neural time series restricted to categorical conditioning
- Cannot handle compositional and zero-shot generalization for novel cognitive tasks
- fMRI brain dynamics generation limited to known experimental conditions

## Solution
Per-timestep conditioned diffusion transformer that injects:
- Compositional language priors (task descriptions)
- Optional spatial priors (ROI masks) 
- In-context conditioning enabling zero-shot task generation

## Key Methods

### Architecture
- Diffusion transformer backbone for fMRI generation
- Per-timestep conditioning module
- Dual-pathway: language + spatial prior injection
- In-context learning for unseen tasks

### Conditioning Strategy
```
Language Pathway:
- Task descriptions → compositional embeddings
- Zero-shot specification for counterfactual experiments

Spatial Priors:
- ROI masks anchor generation
- Complement language when needed
- Task-specific region recruitment
```

### Generation Process
1. Parse task description → language embedding
2. Optional: inject spatial prior masks
3. Diffusion process with timestep-wise conditioning
4. Generate whole-cortex fMRI dynamics

## Key Results

### Zero-Shot Generation
- Recovers region-specific recruitment across held-out tasks
- Matches spatial activation patterns from language alone
- Spatial priors complement text pathway where language degrades

### Counterfactual Neuroscience
- In-silico experiment design before empirical validation
- Novel cognitive task specification
- Data-driven experimental planning

## Applications
- Counterfactual neuroscience experiments
- Data-driven experimental design
- fMRI simulation for novel paradigms
- Brain dynamics prediction for untested conditions

## Technical Implementation

### Input Requirements
- Task description (text)
- Optional: spatial prior masks
- Target brain regions

### Output
- Whole-cortex fMRI time series
- Task-specific activation patterns
- Regional dynamics predictions

## Advantages
- First generative model for unseen cognitive tasks
- Compositional language conditioning
- Zero-shot counterfactual generation
- Bio-inspired hierarchical reconstruction

## Limitations
- Requires extensive training data
- Spatial priors optional but improve accuracy
- Task manifold coverage affects quality

## Related Work
- fMRI foundation models
- Diffusion models for brain imaging
- In-context learning for neuroscience

## Trigger Words
- counterfactual neuroscience, zero-shot fMRI generation, brain dynamics prediction, cognitive task simulation, in-context priors, flow matching, diffusion transformer, whole-cortex fMRI

## Activation
Use when:
- Generating fMRI for novel/unseen cognitive tasks
- Simulating brain dynamics before empirical experiments
- Designing neuroscience experiments in-silico
- Predicting brain responses to untested paradigms
- Counterfactual reasoning about neural processes

## References
- arXiv:2606.11833v1
- NSD dataset (Natural Scenes Dataset)
- Diffusion transformers, flow matching