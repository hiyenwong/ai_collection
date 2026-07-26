---
name: vlm-lam-brain-alignment
description: >
  Brain alignment methodology for comparing Vision-Language Models (VLMs) and
  Large-Action Models (LAMs) against human fMRI during naturalistic interactive
  tasks. Studies how reasoning-focused vs action-focused prompts shape model
  internal representations and their alignment with brain activity across the
  cortical hierarchy. Use when: evaluating interactive AI model brain alignment,
  comparing VLM vs LAM neural representations, studying prompt-driven
  representation changes, designing fMRI encoding studies with foundation models,
  analyzing cortical processing hierarchy alignment. Triggered by: VLM brain
  alignment, LAM fMRI encoding, vision-language model neuroscience, action model
  brain comparison, prompt-symmetric representations, prompt-asymmetric
  representations, interactive gameplay fMRI, reasoning action alignment,
  cortical hierarchy encoding, Oota 2026.
---

# VLM-LAM Brain Alignment Methodology

Compare how Vision-Language Models (VLMs) and Large-Action Models (LAMs)
align with human brain activity during naturalistic interactive tasks.

## Core Insight

Action-specialized fine-tuning reorganizes multimodal representations toward
action-relevant neural computations, even when whole-brain prediction accuracy
is statistically equivalent between models.

## Key Findings (Oota et al., arXiv:2605.19352)

1. **VLMs and LAMs outperform RL baselines** in voxel-wise encoding, even at
   matched feature dimensionality
2. **Prompt gains scale with cortical hierarchy**: largest in frontal-parietal
   and motor-planning regions; early visual cortex gains ~half as much
3. **VLM is prompt-symmetric**: 12.5% unique action vs 13.6% unique reasoning
   variance — balanced representation
4. **LAM is prompt-asymmetric**: 27% unique action vs -5% unique reasoning —
   action-specialized, strongest in frontal-motor cortex
5. **Equivalent accuracy ≠ equivalent alignment**: models can match in R² while
   having fundamentally different representational organization

## Methodology

### Experimental Design
```
Stimulus: Naturalistic Atari-style video game gameplay
Recording: fMRI during gameplay
Models: VLM (reasoning/action prompts), LAM (reasoning/action prompts), RL baseline
```

### Encoding Model Pipeline
```python
# Extract model features per frame
features_vlm_reason = vlm.extract(game_frames, prompt="reason")
features_vlm_action = vlm.extract(game_frames, prompt="action")
features_lam_reason = lam.extract(game_frames, prompt="reason")
features_lam_action = lam.extract(game_frames, prompt="action")

# Train voxel-wise encoding models (e.g., ridge regression)
for voxel in voxels:
    model = Ridge().fit(features, fmr_data[:, voxel])
    r2 = model.score(test_features, test_fmr[:, voxel])
```

### Variance Partitioning
```python
# Decompose unique vs shared variance across prompts
from sklearn.linear_model import Ridge

def variance_partition(features_a, features_b, fmr_data):
    """Compute unique and shared variance for two feature sets."""
    model_a = Ridge().fit(features_a, fmr_data)
    model_b = Ridge().fit(features_b, fmr_data)
    model_ab = Ridge().fit(np.hstack([features_a, features_b]), fmr_data)

    var_a = model_a.score(features_a, fmr_data)
    var_b = model_b.score(features_b, fmr_data)
    var_ab = model_ab.score(np.hstack([features_a, features_b]), fmr_data)

    unique_a = var_ab - var_b  # variance only explained by A
    unique_b = var_ab - var_a  # variance only explained by B
    shared = var_a + var_b - var_ab

    return unique_a, unique_b, shared
```

### Cortical Hierarchy Analysis
```
Group voxels by cortical region:
  - Early visual (V1-V3)
  - Intermediate visual (V4-LOC)
  - Frontal-parietal (FPN)
  - Motor-planning (premotor, SMA)
Compare prompt gains per region
```

## Practical Applications

- **Model selection for neuro-AI**: Choose VLM for balanced reasoning+action,
  LAM for action-specialized tasks
- **Prompt engineering**: Action prompts shift LAM representations toward
  frontal-motor cortex patterns
- **Encoding study design**: Include both reasoning and action prompt variants
  for comprehensive brain alignment analysis

## Activation
VLM brain alignment, LAM fMRI encoding, vision-language model neuroscience,
action model brain comparison, prompt-symmetric representations,
prompt-asymmetric representations, interactive gameplay fMRI, reasoning action
alignment, cortical hierarchy encoding, Oota 2026, brain alignment reasoning
action.

## Paper
Oota, S.R. et al. "Brain alignment of reasoning and action representations
from vision-language and action models during naturalistic gameplay."
arXiv:2605.19352 [q-bio.NC], 2026.
