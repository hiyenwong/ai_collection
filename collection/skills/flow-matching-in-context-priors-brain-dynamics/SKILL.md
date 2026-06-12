---
name: flow-matching-in-context-priors-brain-dynamics
description: Flow Matching with In-Context Priors for generating out-of-distribution brain dynamics (fMRI) for unseen cognitive tasks - counterfactual neuroscience framework
version: 1.0.0
category: neuroscience
activation_keywords:
  - flow matching
  - brain dynamics
  - fMRI generation
  - counterfactual neuroscience
  - in-context prior
  - diffusion transformer
  - zero-shot brain dynamics
  - cognitive task prediction
trigger_pattern: "Flow matching|brain dynamics|fMRI generation|counterfactual neuroscience|in-context prior|zero-shot cognitive task"
authors:
  - Sam Gijsen
  - Michał Łukomski
  - Marc-André Schulz
  - Kerstin Ritter
arxiv_id: 2606.11833
published_date: 2026-06-10
---

# Flow Matching with In-Context Priors for Out-of-Distribution Brain Dynamics

**arXiv: 2606.11833** | Published: 2026-06-10 | Categories: cs.LG, q-bio.NC

## Problem Statement

Generative models of neural time series have largely remained restricted to categorical conditioning, precluding:
- **Compositional generalization**: Cannot combine multiple task conditions
- **Zero-shot generalization**: Cannot generate for unseen cognitive tasks
- **Counterfactual neuroscience**: Cannot support in-silico experimental design before empirical validation

Traditional approaches require categorical labels, preventing flexible task specification and novel experiment simulation.

## Core Innovation

**Per-timestep conditioned diffusion transformer** that generates realistic fMRI brain dynamics during **unseen cognitive tasks** by injecting:
1. **Compositional language priors**: Natural language task descriptions in-context
2. **Optional spatial priors**: Region-specific activation patterns when available

This enables **zero-shot generation** of whole-cortex fMRI for novel cognitive experiments.

## Methodology Framework

### Architecture: Per-timestep Conditioned Diffusion Transformer

```
[Task Description (Language)] → [Language Encoder] → [Per-timestep Conditioning]
                                        ↓
[Optional Spatial Prior] → [Spatial Anchor] → [Cross-modal Fusion]
                                        ↓
                        [Diffusion Transformer Backbone]
                                        ↓
                    [Generated fMRI Dynamics (4D Time Series)]
```

### Key Technical Components

#### 1. Compositional Language Conditioning
- **Input**: Natural language task descriptions (e.g., "working memory task with emotional distraction")
- **Encoding**: Language encoder maps task semantics to conditioning vectors
- **Compositional**: Can combine multiple task aspects (cognitive load + emotional valence)
- **Per-timestep**: Condition varies across diffusion steps for temporal dynamics

#### 2. Spatial Prior Injection
- **Optional**: When region-specific hypotheses exist, spatial priors anchor generation
- **Complementary**: Anchors generation in regions where language alone degrades
- **Retention**: Preserves compositional structure for counterfactual specification

#### 3. Training Manifold Characterization
- Evaluate across hundreds of held-out task conditions
- Characterize predictive performance relative to training distribution
- Recover region-specific recruitment patterns from language alone

## Key Results

### From Language Alone
1. **Region-Specific Recruitment Recovery**: Accurate prediction of task-dependent regional activation
2. **Held-Out Spatial Patterns**: Recover activation patterns for unseen spatial configurations
3. **Compositional Generalization**: Combine task conditions not seen during training

### Spatial Prior Benefits
1. **Anchor in Degraded Regions**: Where language-only predictions fail
2. **Retain Compositional Structure**: Enable counterfactual task specification
3. **Complementary Pathways**: Language + spatial = better than either alone

### Zero-Shot Task Generation
- **First**: Whole-cortex fMRI dynamics for unseen cognitive tasks
- **Counterfactual Capability**: In-silico experiment design and evaluation
- **Data-Driven Experimental Design**: Optimize task parameters before validation

## Implementation Guide

### Step 1: Model Architecture Setup

```python
import torch
import torch.nn as nn

class InContextFlowMatching(nn.Module):
    """
    Per-timestep conditioned diffusion transformer for fMRI generation.
    
    Args:
        - language_encoder: Transformer encoder for task descriptions
        - spatial_prior_encoder: Optional encoder for spatial activation patterns
        - diffusion_transformer: DiT backbone for 4D fMRI generation
        - num_voxels: Number of voxels in brain volume
        - num_timepoints: Number of timepoints in fMRI sequence
    """
    def __init__(
        self,
        language_encoder,
        spatial_prior_encoder=None,
        diffusion_transformer,
        num_voxels=50000,
        num_timepoints=100
    ):
        super().__init__()
        self.language_encoder = language_encoder
        self.spatial_prior_encoder = spatial_prior_encoder
        self.diffusion_transformer = diffusion_transformer
        
        # Conditioning projection
        self.language_proj = nn.Linear(768, diffusion_transformer.hidden_dim)
        self.spatial_proj = nn.Linear(num_voxels, diffusion_transformer.hidden_dim)
        
        # Cross-modal fusion
        self.condition_fusion = nn.MultiheadAttention(
            embed_dim=diffusion_transformer.hidden_dim,
            num_heads=8
        )
    
    def forward(
        self,
        task_description,
        spatial_prior=None,
        timestep,
        noisy_fMRI
    ):
        """
        Generate conditioned fMRI dynamics.
        
        Args:
            - task_description: str or list of str (compositional)
            - spatial_prior: optional tensor [batch, num_voxels]
            - timestep: diffusion timestep [batch]
            - noisy_fMRI: current noisy state [batch, num_voxels, num_timepoints]
        
        Returns:
            - velocity_field: predicted velocity for flow matching
        """
        # Encode language condition
        lang_embedding = self.language_encoder(task_description)
        lang_condition = self.language_proj(lang_embedding)
        
        # Encode spatial prior if available
        if spatial_prior is not None:
            spatial_embedding = self.spatial_prior_encoder(spatial_prior)
            spatial_condition = self.spatial_proj(spatial_embedding)
            
            # Cross-modal fusion
            fused_condition = self.condition_fusion(
                lang_condition, spatial_condition, spatial_condition
            )[0]
        else:
            fused_condition = lang_condition
        
        # Per-timestep conditioning
        timestep_embed = self.diffusion_transformer.time_embed(timestep)
        condition = fused_condition + timestep_embed
        
        # Generate velocity field
        velocity = self.diffusion_transformer(noisy_fMRI, condition)
        
        return velocity
```

### Step 2: Training Pipeline

```python
def train_incontext_flow(
    model,
    train_dataset,
    task_vocab,
    num_epochs=100,
    batch_size=32
):
    """
    Train flow matching model with in-context priors.
    
    Key training considerations:
    - Diverse task descriptions in training set
    - Compositional task combinations
    - Optional spatial priors from known activation patterns
    """
    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-4)
    
    for epoch in range(num_epochs):
        for batch in train_dataset:
            # Extract batch components
            fMRI = batch['fMRI']  # [batch, voxels, timepoints]
            task_desc = batch['task_description']  # str or compositional
            spatial_prior = batch.get('spatial_prior', None)  # optional
            
            # Sample timestep
            t = torch.rand(batch_size, device=fMRI.device)
            
            # Flow matching: interpolate between noise and data
            noise = torch.randn_like(fMRI)
            x_t = (1 - t.view(-1, 1, 1)) * noise + t.view(-1, 1, 1) * fMRI
            
            # Target velocity: data - noise
            target_velocity = fMRI - noise
            
            # Predict velocity
            pred_velocity = model(
                task_description=task_desc,
                spatial_prior=spatial_prior,
                timestep=t,
                noisy_fMRI=x_t
            )
            
            # Flow matching loss
            loss = F.mse_loss(pred_velocity, target_velocity)
            
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
```

### Step 3: Zero-Shot Generation for Novel Tasks

```python
def generate_counterfactual_fMRI(
    model,
    novel_task_description,
    spatial_prior=None,
    num_steps=50,
    num_samples=10
):
    """
    Generate fMRI dynamics for unseen cognitive task.
    
    Args:
        - novel_task_description: str describing new task (e.g., "dual n-back with auditory distraction")
        - spatial_prior: optional hypothesis about region activation
    
    Returns:
        - generated_fMRI: synthetic brain dynamics for novel task
    """
    # Initialize from noise
    x = torch.randn(num_samples, num_voxels, num_timepoints)
    
    # Reverse flow (generate from noise to data)
    for step in range(num_steps):
        t = torch.ones(num_samples) * (step / num_steps)
        
        # Predict velocity
        velocity = model(
            task_description=novel_task_description,
            spatial_prior=spatial_prior,
            timestep=t,
            noisy_fMRI=x
        )
        
        # Euler step (or use more sophisticated ODE solver)
        x = x + velocity * (1.0 / num_steps)
    
    return x  # Generated fMRI for novel task
```

### Step 4: Counterfactual Experiment Design

```python
def design_counterfactual_experiment(
    model,
    base_task,
    intervention_variations,
    evaluation_metrics
):
    """
    Design and evaluate novel cognitive experiments in-silico.
    
    Args:
        - base_task: known task (e.g., "working memory")
        - intervention_variations: list of interventions to test
          (e.g., ["with emotional distraction", "with time pressure", "dual-task"])
        - evaluation_metrics: what to measure (activation in specific regions)
    
    Returns:
        - experiment_predictions: predicted outcomes for each intervention
        - optimal_design: recommended experimental parameters
    """
    predictions = []
    
    for intervention in intervention_variations:
        # Compositional task description
        novel_task = f"{base_task} {intervention}"
        
        # Generate counterfactual fMRI
        generated_fMRI = generate_counterfactual_fMRI(
            model,
            novel_task_description=novel_task
        )
        
        # Evaluate metrics
        metrics = {}
        for region, roi in evaluation_metrics['regions'].items():
            metrics[region] = generated_fMRI[:, roi, :].mean()
        
        predictions.append({
            'intervention': intervention,
            'fMRI': generated_fMRI,
            'metrics': metrics
        })
    
    # Rank interventions by predicted effect magnitude
    optimal_design = select_optimal_intervention(predictions)
    
    return predictions, optimal_design
```

## Applications

### 1. Counterfactual Neuroscience
- **Hypothesis Testing**: Generate predictions for novel task combinations before empirical validation
- **Causal Inference**: Simulate interventions (e.g., "what if we added emotional distraction?")
- **Theory Validation**: Compare generated dynamics with theoretical predictions

### 2. Data-Driven Experimental Design
- **Parameter Optimization**: Find task parameters that maximize target region activation
- **Efficiency**: Reduce wasted experiments by pre-screening in-silico
- **Novel Paradigm Discovery**: Explore task combinations not previously considered

### 3. Clinical Translation
- **Patient-Specific**: Generate dynamics for patient populations with specific conditions
- **Treatment Simulation**: Predict brain dynamics under therapeutic interventions
- **Personalized Protocols**: Design optimal cognitive training protocols

## Technical Pitfalls

### ⚠️ Language Conditioning Limitations
- **Issue**: Language alone may not capture fine-grained spatial patterns
- **Solution**: Combine with spatial priors when hypothesis-driven
- **Mitigation**: Characterize degradation regions to know when to use spatial anchors

### ⚠️ Out-of-Distribution Challenges
- **Issue**: Performance degrades for tasks far from training manifold
- **Mitigation**: Quantify distance from training distribution
- **Validation**: Compare with held-out task conditions during training

### ⚠️ Temporal Dynamics Accuracy
- **Issue**: Generated temporal patterns may lack precise temporal structure
- **Solution**: Use per-timestep conditioning for temporal variation
- **Validation**: Compare generated vs. real temporal autocorrelation

### ⚠️ Compositional Generalization Limits
- **Issue**: Composing unfamiliar task aspects may fail
- **Mitigation**: Train on diverse compositional combinations
- **Validation**: Test systematically on compositional splits

## Related Work

- **Brain Dynamics Models**: Brain-DiT, Brain-OF, NeuroSTORM
- **Flow Matching**: Continuous-time generative modeling
- **Diffusion Transformers**: DiT, stable diffusion architectures
- **Counterfactual Neuroscience**: In-silico brain simulation

## References

1. Gijsen et al. (2026). "Flow Matching with In-Context Priors for Out-of-Distribution Brain Dynamics"
2. Brain-DiT: Universal multi-state fMRI foundation model
3. Flow matching theory: Lipman et al. (2023)
4. Diffusion transformers: Peebles & Xie (2023)

## Code Availability

- GitHub: https://github.com/SamGijsen/pinc-flows
- Pretrained models available

## Citation

```bibtex
@article{gijsen2026flowmatching,
  title={Flow Matching with In-Context Priors for Out-of-Distribution Brain Dynamics},
  author={Gijsen, Sam and Łukomski, Michał and Schulz, Marc-André and Ritter, Kerstin},
  journal={arXiv preprint arXiv:2606.11833},
  year={2026}
}
```