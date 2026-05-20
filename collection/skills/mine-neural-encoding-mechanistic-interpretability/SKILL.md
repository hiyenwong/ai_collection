---
name: mine-neural-encoding-mechanistic-interpretability
description: "Mechanistically Interpretable Neural Encoding (MINE) methodology. Applies mechanistic-interpretability tools from AI to neural encoding models for brain vision studies. Opens the black box of encoding models to localize image features driving voxel-level activity. Use when: neural encoding, mechanistic interpretability for brain models, voxel-level feature attribution, brain encoding with interpretable AI, visual cortex analysis, fMRI encoding models. Keywords: mechanistic interpretable neural encoding, MINE, voxel-level feature attribution, brain encoding interpretability, mechanistic interpretability fMRI."
---

# MINE: Mechanistically Interpretable Neural Encoding

> Framework applying mechanistic-interpretability tools from AI to neural encoding models, enabling semantically interpretable descriptions of image features driving millimeter-scale (voxel-level) brain activity.

## Metadata
- **Source**: arXiv:2605.16468
- **Authors**: Idan Daniel Grosbard, Mor Geva, Galit Yovel
- **Published**: 2026-05-15

## Core Methodology

### Key Innovation
Traditional neural encoding models predict cortical responses to natural images but treat the encoder as a black box — they are correlational and don't reveal *which* image features drive *each* voxel's response. MINE opens this black box by applying mechanistic-interpretability tools (from AI interpretability research) to neural encoding.

### Technical Framework

1. **Language-aligned image representations**: Use vision-language model representations (e.g., CLIP) to predict each voxel's response to natural images
2. **Per-image feature attribution**: Apply mechanistic interpretability to localize which features within natural images drive each voxel's activation, producing semantically interpretable descriptions
3. **Per-voxel functional profiles**: Generalize per-image features into per-voxel functional selectivity profiles
4. **Causal validation** (3-tier):
   - **Generation**: Show per-image descriptions are sufficient to generate images that elicit voxel responses matching original responses (vs. random/low-attribution controls)
   - **Counterfactual insertion/removal**: Insert or remove predicted features from images → activation shifts in expected direction
   - **Counterfactual editing via profiles**: Edit images guided by per-voxel activation profiles → stronger activation shifts, confirming profiles faithfully capture selectivity

### Validation Protocol

| Validation Type | Method | Outcome |
|----------------|--------|---------|
| Sufficiency | Generate images from per-image descriptions | Match original voxel responses better than controls |
| Causal (feature) | Insert/remove predicted features | Activation shifts in expected direction |
| Causal (profile) | Edit images via per-voxel profiles | Stronger activation shifts than feature-level edits |
| Recovery | Apply to known category-selective regions | Recovers known categorical preferences + fine-grained voxel structure |

## Implementation Guide

### Prerequisites
- fMRI data with natural image stimuli
- Pretrained vision-language model (CLIP or similar)
- Ridge regression or similar linear encoding model

### Step-by-Step

1. **Encode**: Train voxel-wise encoding models using VLM image features → predict fMRI responses
2. **Attribute**: For each voxel and each image, compute feature attribution scores identifying which VLM dimensions drive the prediction
3. **Describe**: Map high-attribution VLM dimensions to semantic descriptions via the language-aligned representation
4. **Profile**: Aggregate per-image descriptions into per-voxel functional profiles
5. **Validate**:
   - Generate images from descriptions, measure response match
   - Counterfactually edit images, measure activation shift

### Code Example

```python
# Simplified MINE pipeline
import numpy as np
from sklearn.linear_model import Ridge

# Step 1: Train encoding model
# X: image features (VLM representations), Y: voxel responses
encoding_model = Ridge()
encoding_model.fit(X_train, Y_train[voxel_idx])

# Step 2: Feature attribution per image
# For each image, compute which features drive the prediction
attributions = encoding_model.coef_ * X_test  # simple linear attribution

# Step 3: Semantic description via VLM language space
# Map high-attribution features to nearest language tokens/descriptions
top_features = np.argsort(np.abs(attributions))[-k:]
descriptions = vlm.decode_features(top_features)

# Step 4: Causal validation — counterfactual editing
edited_image = counterfactual_edit(original_image, target_features, direction)
predicted_shift = encoding_model.predict(edited_image) - encoding_model.predict(original_image)
```

## Applications
- Discover fine-grained functional selectivity in visual cortex beyond category-level analysis
- Causal validation of encoding model hypotheses
- Bridge between AI mechanistic interpretability and neuroscience
- Characterize unique voxel structure within known brain regions (FFA, PPA, etc.)

## Pitfalls
- Requires large natural image datasets with sufficient feature diversity
- VLM representation quality directly affects interpretability
- Counterfactual edits must be realistic enough to still be processable by the visual system
- Linear attribution (used here) may miss nonlinear feature interactions

## Related Skills
- feature-visualization-brain-encoder
- neural-encoding-evaluation-ground-truth
- decoding-encoding-alignment-critique
