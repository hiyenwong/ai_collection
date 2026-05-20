---
name: vlm-lam-brain-alignment
description: "Brain alignment methodology for Vision-Language Models (VLMs) and Large-Action Models (LAMs) during naturalistic gameplay. Studies how action-focused and reasoning-focused prompts shape model internal representations and align with fMRI brain activity. Reveals prompt-symmetric vs prompt-asymmetric representational organization."
---

# VLM/LAM Brain Alignment During Naturalistic Gameplay

## Overview

This methodology studies brain alignment of foundation models (VLMs and LAMs) during interactive gameplay using fMRI recordings. Published as arXiv:2605.19352 (Oota et al., 2026).

**Core Insight**: Action-specialized fine-tuning reorganizes multimodal representations toward action-relevant neural computations even when whole-brain prediction accuracy is statistically equivalent between VLM and LAM.

## Key Contributions

### 1. Interactive Brain Alignment Beyond Passive Tasks
- Most brain-encoding studies focus on language comprehension or passive visual processing
- This work extends alignment studies to interactive, naturalistic gameplay scenarios
- Uses Atari-style video games as dynamic, goal-directed environments

### 2. Prompt-Driven Representation Analysis
- Examines how action-focused vs reasoning-focused prompts shape model representations
- Compares alignment patterns across different prompting strategies
- Reveals qualitative differences in representational organization

### 3. Variance Partitioning for Model Comparison
- Uses variance partitioning to decompose unique contributions of different model components
- Identifies prompt-symmetric (VLM) vs prompt-asymmetric (LAM) organizations
- Maps alignment patterns to cortical processing hierarchy

## Key Findings

### Prediction Performance
- Both VLMs and LAMs exhibit significantly better voxel-wise encoding performance than RL baselines
- Advantage holds even under matched feature dimensionality
- Prompt-driven gains scale with cortical processing hierarchy

### Cortical Hierarchy Effects
- **Largest improvements**: Frontal-parietal and motor-planning regions
- **Moderate improvements**: Early visual cortex (roughly half the gain)
- Suggests higher-order cognitive regions benefit more from foundation model representations

### Representational Organization
- **VLM**: Prompt-symmetric (12.5% unique action vs 13.6% unique reasoning)
- **LAM**: Prompt-asymmetric (27% unique action vs -5% unique reasoning)
- Asymmetry strongest in frontal-motor cortex
- Action-specialized fine-tuning reorganizes representations toward action-relevant computations

## Methodology

### Step 1: Data Collection
```python
# Record fMRI while participants play Atari-style games
# Extract model features from VLMs and LAMs with different prompts
# Match feature dimensionality for fair comparison

gameplay_data = collect_fmi_during_gameplay(participants)
vlm_features = extract_features(vlm_model, game_frames, prompt='action')
lam_features = extract_features(lam_model, game_frames, prompt='action')
```

### Step 2: Encoding Model Training
```python
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score

# Train voxel-wise encoding models
encoding_models = {}
for voxel in voxels:
    model = Ridge(alpha=1.0)
    model.fit(train_features, voxel_responses)
    encoding_models[voxel] = model

# Evaluate with cross-validation
scores = cross_val_score(encoding_model, features, responses, cv=5)
```

### Step 3: Variance Partitioning Analysis
```python
def variance_partitioning(model_a, model_b, brain_responses):
    """Decompose unique and shared variance contributions."""
    pred_a = model_a.predict(test_features)
    pred_b = model_b.predict(test_features)
    
    # Unique variance for each model
    unique_a = r2_score(brain_responses, pred_a) - r2_score(brain_responses, pred_b)
    unique_b = r2_score(brain_responses, pred_b) - r2_score(brain_responses, pred_a)
    shared = min(r2_score(brain_responses, pred_a), r2_score(brain_responses, pred_b))
    
    return unique_a, unique_b, shared
```

### Step 4: Cortical Mapping
```python
# Map alignment patterns to brain regions
# Identify regions with strongest prompt-driven effects
# Compare across cortical hierarchy

regions = ['early_visual', 'frontal_parietal', 'motor_planning']
for region in regions:
    alignment_scores = compute_alignment(region_features, region_responses)
    print(f"{region}: {alignment_scores}")
```

## Applications

- **Interactive AI Evaluation**: Assess model alignment during dynamic tasks
- **Neuroscience of Agency**: Study how action representations map to brain activity
- **Model Architecture Design**: Inform development of action-specialized models
- **Brain-Computer Interfaces**: Leverage foundation model representations for decoding
- **Cognitive Neuroscience**: Understand hierarchical processing of action vs reasoning

## Related Concepts

- Brain-encoding models
- Representational Similarity Analysis
- Foundation model alignment
- Interactive neuroscience paradigms
- Variance partitioning in neuroimaging
- Cortical hierarchy mapping
- Action representation in brain
- Vision-language models
- Large-action models

## Implementation Considerations

- Requires fMRI data collection during interactive tasks
- Foundation model feature extraction with multiple prompts
- Careful control for feature dimensionality differences
- Variance partitioning requires sufficient sample size
- Cortical ROI definition affects interpretation of hierarchical effects

## References

- arXiv:2605.19352 - "Brain alignment of reasoning and action representations from vision-language and action models during naturalistic gameplay"
- Natural Scenes Dataset (NSD) for fMRI benchmarks
- Brain-encoding model frameworks (Naselaris et al., 2011)
- Vision-language model literature (CLIP, BLIP, etc.)
- Large-action model research
