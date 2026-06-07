---
name: mirage-multimodal-fmri-encoding
description: "MIRAGE - Adaptive multimodal gating framework for whole-brain fMRI encoding. Integrates visual, auditory, and linguistic information via native multimodal backbone with layer-wise feature gating. Predicts brain responses to naturalistic audiovisual stimuli across subjects. Use when: (1) Building brain encoding models with multimodal stimuli, (2) Predicting fMRI responses from movies/videos, (3) Integrating visual-auditory-language features for brain prediction, (4) Interpretable modality-specific attention analysis. Activation: fMRI encoding, multimodal brain prediction, MIRAGE, brain encoding, naturalistic stimuli, adaptive gating, multimodal fusion."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.29850"
  published: "2026-05-29"
  authors: "Research Team"
  tags: [fmri, brain-encoding, multimodal, adaptive-gating, foundation-model, visual, auditory, language, neural]
---

# MIRAGE: Adaptive Multimodal Gating for Whole-Brain fMRI Encoding

State-of-the-art framework for predicting whole-brain fMRI responses to naturalistic audiovisual stimuli through native multimodal backbone and adaptive layer-wise feature gating.

## Problem Domain

### Brain Encoding Challenge

**Goal**: Predict fMRI brain responses when subjects watch/listen to naturalistic stimuli (movies, videos, narratives).

**Current limitation**: Most existing approaches rely on **unimodal representations** (only visual, only auditory, or only linguistic).

**Reality**: Naturalistic stimuli are inherently **multimodal** - movies contain visual scenes, audio soundtrack, and narrative language simultaneously.

### Why Multimodal Integration Matters

- **Visual processing**: Brain regions respond to visual scenes (V1-V5, temporal cortex)
- **Auditory processing**: Temporal cortex and auditory regions respond to sounds/music
- **Language processing**: Language regions (Broca's, Wernicke's) respond to narrative
- **Cross-modal interaction**: Brain integrates information across modalities (audio-visual fusion)

**MIRAGE addresses**: How to jointly integrate visual, auditory, and linguistic information for accurate whole-brain prediction?

## Architecture Components

### 1. Native Multimodal Backbone

**Omni-modal foundation model** - Trained jointly on visual, auditory, and linguistic modalities (not post-hoc aggregation of independent unimodal models).

**Key advantage**: Captures cross-modal interactions in feature representations, enabling:
- Visual-auditory synchronization features
- Language-visual scene grounding
- Audio-visual-linguistic coherence representations

### 2. Adaptive Layer-wise Gating

**Feature gating across backbone layers** - Dynamic selection of which features to use for brain prediction.

**Mechanism**:
- Attention weights control modality contribution at each layer
- Learnable gating parameters for visual, auditory, language streams
- Task-specific modality weighting (more visual for visual cortex, more auditory for auditory regions)

```python
class AdaptiveModalityGate(nn.Module):
    def __init__(self, num_layers, num_modalities):
        self.gate_weights = nn.Parameter(
            torch.randn(num_layers, num_modalities)
        )
    
    def forward(self, layer_features, modality_idx):
        # layer_features: features from backbone layer
        # modality_idx: which modality (visual/auditory/language)
        gate = torch.softmax(self.gate_weights[layer_idx], dim=-1)
        weighted_features = layer_features * gate[modality_idx]
        return weighted_features
```

### 3. Transformer Brain Encoder

**Maps multimodal features to brain activity patterns**.

- Takes gated multimodal features as input
- Predicts activity for each cortical parcel
- Transformer architecture enables:
  - Attention over time (stimulus temporal dynamics)
  - Attention over space (different brain regions)
  - Cross-parcel interactions

### 4. Subject-Specific Linear Head

**Individual variation handling** - Subject-specific adaptation layer.

```python
class SubjectHead(nn.Module):
    def __init__(self, feature_dim, num_parcels):
        self.subject_projections = nn.ModuleDict()
        # Each subject has unique linear projection
    
    def forward(self, features, subject_id):
        projection = self.subject_projections[subject_id]
        parcel_activity = projection(features)
        return parcel_activity
```

**Why subject-specific?**:
- Brain anatomy varies across individuals
- Functional organization differs between subjects
- Same stimulus can evoke different responses across subjects

## Technical Implementation

### Multimodal Feature Extraction

```python
# Native multimodal backbone (e.g., from omni-modal foundation model)
backbone = OmniModalFoundationModel(
    modalities=['visual', 'auditory', 'language'],
    num_layers=12
)

# Extract layer-wise features
layer_features = backbone.extract_features(
    visual_input=video_frames,
    auditory_input=audio_waveform,
    language_input=transcript_text
)
# Returns: {layer_idx: {modality: features}}
```

### Adaptive Gating Process

```python
# Initialize gating network
gating = AdaptiveLayerGating(num_layers=12, num_modalities=3)

# Apply gating to multimodal features
gated_features = []
for layer_idx in range(12):
    layer_feats = layer_features[layer_idx]
    
    # Compute modality attention
    modality_attention = gating.compute_attention(layer_feats)
    # Returns: [visual_weight, auditory_weight, language_weight]
    
    # Weight features by modality attention
    weighted_visual = layer_feats['visual'] * modality_attention[0]
    weighted_auditory = layer_feats['auditory'] * modality_attention[1]
    weighted_language = layer_feats['language'] * modality_attention[2]
    
    gated_features.append(
        torch.cat([weighted_visual, weighted_auditory, weighted_language], dim=-1)
    )
```

### Brain Activity Prediction

```python
# Transformer brain encoder
brain_encoder = TransformerBrainEncoder(
    input_dim=gated_feature_dim,
    num_parcels=200,  # Number of cortical parcels
    num_heads=8
)

# Predict parcel activity
parcel_predictions = brain_encoder(
    gated_features,
    temporal_context=stimulus_timepoints
)
# Returns: (timepoints, num_parcels) activity predictions
```

## Key Results

### State-of-the-Art Performance

**MIRAGE achieves SOTA** in whole-brain fMRI prediction for naturalistic audiovisual stimuli.

### Native Multimodal Superiority

**Critical finding**: Natively multimodal features **consistently outperform** post-hoc aggregation of independent unimodal features.

| Approach | Visual Cortex | Auditory Cortex | Language Regions | Whole Brain |
|----------|---------------|-----------------|------------------|-------------|
| Unimodal (visual only) | Good | Poor | Poor | Moderate |
| Unimodal (auditory only) | Poor | Good | Poor | Moderate |
| Post-hoc aggregation | Moderate | Moderate | Moderate | Moderate |
| **MIRAGE (native multimodal)** | **Excellent** | **Excellent** | **Excellent** | **SOTA** |

**Why native beats post-hoc?**:
- Cross-modal interaction features (e.g., visual-audio synchronization)
- Temporal alignment across modalities
- Modality grounding (language-visual scene correspondence)
- Shared representation space across modalities

### Interpretable Modality Attention

**Learned attention weights are directly inspectable** - Understand which modalities contribute to predictions for each brain region.

**Findings**:
- **Visual cortex**: High visual attention, moderate auditory, low language
- **Auditory cortex**: High auditory attention, moderate visual, low language
- **Language regions**: High language attention, moderate visual/auditory
- **Cross-modal regions**: Balanced attention across modalities

### Anatomical Modality Patterns

**Each modality traces a distinct anatomical pattern across cortex**:

```
Visual attention pattern:
  High: V1, V2, V3, V4, V5 (occipital cortex)
  Moderate: Temporal visual areas
  Low: Frontal, language regions

Auditory attention pattern:
  High: Primary auditory cortex (A1), superior temporal gyrus
  Moderate: Temporal-parietal junction
  Low: Occipital, frontal motor

Language attention pattern:
  High: Broca's area, Wernicke's area, temporal language regions
  Moderate: Prefrontal cortex
  Low: Occipital, motor regions
```

## Cross-Backbone Validation

**MIRAGE tested across different foundation model backbones**:

- Video foundation models (e.g., VideoMAE)
- Audio foundation models (e.g., AudioMAE)
- Language foundation models (e.g., LLaMA, GPT)
- Omni-modal foundation models (e.g., ImageBind)

**Result**: Native multimodal backbone consistently outperforms post-hoc unimodal aggregation **across all backbone choices**.

## Practical Applications

### Movie/Video Brain Prediction

- Predict brain responses while watching movies
- Naturalistic audiovisual stimuli with narrative
- Cross-subject generalization

### Cross-Modal Interaction Studies

- Investigate how brain integrates visual-auditory-language information
- Understand modality-specific cortical processing
- Analyze cross-modal attention patterns

### Subject-Specific Encoding Models

- Adapt models to individual brain anatomy
- Handle inter-subject variation in fMRI responses
- Personalized brain encoding for neuroscience research

### Brain-Computer Interface

- Predict brain activity from stimuli
- Inverse problem: infer stimuli from brain activity
- Real-time brain response prediction

## Experimental Methodology

### Data Requirements

1. **Naturalistic stimuli**: Movies/videos with audio and narrative
2. **fMRI recordings**: Whole-brain activity while subjects view stimuli
3. **Subject identifiers**: Multiple subjects for cross-subject evaluation
4. **Temporal alignment**: Stimulus timepoints aligned to fMRI volumes

### Evaluation Metrics

- **Prediction accuracy**: Correlation between predicted and actual fMRI activity
- **Parcel-level prediction**: Accuracy for each cortical parcel
- **Subject-level generalization**: Cross-subject performance
- **Modality contribution**: Attention weight analysis

### Cross-Subject Evaluation

- Train on subset of subjects
- Test on held-out subjects
- Measure subject-specific adaptation effectiveness

## Design Implications

### For Brain Encoding Models

1. **Use native multimodal features**: Don't aggregate independent unimodal models
2. **Adaptive gating**: Allow task-specific modality weighting
3. **Subject-specific heads**: Handle inter-subject variation
4. **Layer-wise integration**: Use features from multiple backbone layers

### For Foundation Models

1. **Train jointly on multiple modalities**: Capture cross-modal interactions
2. **Preserve temporal alignment**: Align features across modalities over time
3. **Enable layer-wise extraction**: Extract features from multiple depth levels

### For Interpretability

1. **Inspect attention weights**: Understand modality contributions
2. **Analyze anatomical patterns**: Map modality attention to brain regions
3. **Compare cross-modal features**: Study visual-auditory-language integration

## Future Directions

1. **Temporal gating**: Time-varying modality attention (scene-dependent weighting)
2. **Parcel-specific gating**: Different gating parameters for each brain region
3. **Inverse encoding**: Infer stimuli from brain activity using multimodal features
4. **Clinical applications**: Brain encoding for neurological disorder analysis

## Activation Triggers

- Building brain encoding model for movies/videos
- Predicting fMRI responses from naturalistic audiovisual stimuli
- Integrating visual-auditory-language features for brain prediction
- Analyzing modality-specific cortical processing
- Subject-specific brain encoding model design
- Cross-modal attention interpretability analysis

## Related Skills

- Brain encoding model design
- Foundation model feature extraction
- Transformer architecture for brain prediction
- Multimodal neural network integration
- fMRI analysis and interpretation
- Naturalistic stimuli brain imaging