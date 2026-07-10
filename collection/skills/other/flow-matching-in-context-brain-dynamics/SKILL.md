---
name: flow-matching-in-context-brain-dynamics
description: Flow Matching with In-Context Priors for Out-of-Distribution Brain Dynamics methodology — per-timestep conditioned diffusion transformer for generating realistic fMRI during unseen cognitive tasks using compositional language and spatial priors.
version: 1.0.0
category: neuroscience
tags: [brain-dynamics, fMRI, flow-matching, diffusion, transformer, zero-shot, counterfactual-neuroscience, generative-model]
arxiv: 2606.11833
authors: [Sam Gijsen, Michał Łukomski, Marc-André Schulz, Kerstin Ritter]
published: 2026-06-10
activation_keywords: [flow matching, brain dynamics, fMRI generation, zero-shot, in-context prior, diffusion transformer, counterfactual neuroscience, cognitive task]
---

# Flow Matching with In-Context Priors for Out-of-Distribution Brain Dynamics

## Overview

First generative model of whole-cortex fMRI dynamics for unseen cognitive tasks, enabling counterfactual neuroscience through compositional language and spatial priors.

**arXiv**: 2606.11833  
**Authors**: Sam Gijsen, Michał Łukomski, Marc-André Schulz, Kerstin Ritter  
**Published**: June 10, 2026  
**Categories**: cs.LG, q-bio.NC

## Core Innovation

Per-timestep conditioned diffusion transformer that:
- Generates realistic fMRI brain dynamics during **unseen cognitive tasks**
- Injects **compositional language** priors for task specification
- Optionally incorporates **spatial priors** for region-specific anchoring
- Enables **zero-shot generation** for novel experimental designs

## Key Methodology

### 1. Architecture
- Diffusion transformer backbone
- Per-timestep conditioning (not categorical)
- Dual pathway: language + optional spatial

### 2. In-Context Priors
- **Language pathway**: Task descriptions as compositional priors
- **Spatial pathway**: Optional ROI-level activation patterns
- **Joint conditioning**: Contextual integration for unseen tasks

### 3. Training Strategy
- Flow matching objective
- Context injection at each timestep
- Compositional generalization via language embedding

## Applications

### Counterfactual Neuroscience
- In-silico design of novel cognitive experiments
- Evaluate hypothetical experiments before empirical validation
- Predict brain responses to unseen task combinations

### Zero-Shot Brain Dynamics Generation
- Generate fMRI for tasks outside training distribution
- Compositional task specification via natural language
- Region-specific recruitment prediction

### Data-Driven Experimental Design
- Simulate cognitive experiments computationally
- Optimize experimental parameters before running
- Reduce empirical validation costs

## Technical Details

### Input Modalities
- **Task language**: Natural language task descriptions
- **Spatial priors**: Optional ROI activation patterns (optional)

### Output
- **Whole-cortex fMRI dynamics**: Time-series generation across all regions

### Performance
- Evaluated across **hundreds of held-out task conditions**
- Recovers region-specific recruitment from language alone
- Spatial priors complement text in degraded regions

## Implementation Patterns

### 1. Flow Matching Transformer
```python
# Per-timestep conditioned diffusion
class BrainFlowTransformer:
    def forward(self, noise, task_context, spatial_prior=None):
        # Inject language context per timestep
        timestep_emb = self.time_embed(t)
        task_emb = self.language_encoder(task_context)
        
        # Optional spatial anchoring
        if spatial_prior:
            spatial_emb = self.spatial_encoder(spatial_prior)
            conditioning = torch.cat([timestep_emb, task_emb, spatial_emb])
        else:
            conditioning = torch.cat([timestep_emb, task_emb])
        
        return self.transformer(noise, conditioning)
```

### 2. Zero-Shot Generation
```python
# Generate fMRI for unseen task
def generate_brain_dynamics(model, novel_task_description):
    # No training needed for novel tasks
    context = encode_task(novel_task_description)  # Language only
    noise = torch.randn(batch, time, regions)
    
    # Per-timestep generation
    fMRI_trajectory = model.sample(noise, context)
    return fMRI_trajectory
```

## Key Results

### Language-Only Generation
- Recovers region-specific task recruitment
- Matches held-out spatial activation patterns
- Compositional structure preserved

### Spatial + Language
- Anchors generation where language degrades
- Complementary information fusion
- Better performance in specialized regions

## Why This Matters

1. **Counterfactual neuroscience**: Simulate experiments before running
2. **Zero-shot generalization**: No training for novel tasks
3. **Compositional reasoning**: Task combinations via language
4. **Cost reduction**: In-silico validation before empirical

## Use Cases

### When to Apply
- Brain dynamics prediction for novel tasks
- Experimental design optimization
- Counterfactual cognitive neuroscience
- fMRI simulation for unseen conditions
- Compositional task brain response

### Trigger Words
- flow matching brain
- zero-shot fMRI
- counterfactual neuroscience
- in-context prior
- task-conditioned diffusion
- whole-cortex generation

## Related Skills

- `brain-dit-fmri-foundation-model` — Brain-DiT foundation model
- `flow-matching-in-context-priors-brain-dynamics` — In-context priors for brain
- `geometric-brain-dynamics-mapping` — Geometric basis functions
- `brain-cast-spatiotemporal-fmri-forecasting` — BrainCast spatiotemporal

## References

- Gijsen et al. (2026) arXiv:2606.11833
- Flow matching: Lipman et al. (2023)
- Diffusion transformers: Peebles & Xie (2023)
- MICrONS dataset: MICrONS Program

## Pitfalls

- Requires compositional task descriptions
- Spatial priors optional but improve specialized regions
- Performance varies near training manifold edge
- Language embedding quality critical