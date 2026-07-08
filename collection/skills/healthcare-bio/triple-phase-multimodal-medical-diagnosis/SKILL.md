---
name: triple-phase-multimodal-medical-diagnosis
description: "Triple-phase multimodal framework for medical image classification — combines cross-modality contrastive learning, modality-specific fine-tuning, and feature-level multimodal ensemble learning for patient-level prediction. Validated on microbial keratitis subtype diagnosis with 85.84% accuracy across 1645 patients."
---

# Triple-Phase Multimodal Medical Diagnosis

## Description

A three-phase framework for multimodal medical image classification that addresses cross-site generalization challenges. Phase 1 uses cross-modality contrastive learning to learn shared representations across imaging modalities. Phase 2 performs modality-specific fine-tuning to capture modality-unique features. Phase 3 combines representations via feature-level multimodal ensemble learning for patient-level prediction. The approach is validated on microbial keratitis classification (bacterial vs. fungal) using slit-lamp photography with multiple illumination modes.

## Activation Keywords
- triple-phase multimodal diagnosis
- cross-modality contrastive medical
- multimodal medical ensemble
- microbial keratitis classification
- slit-lamp multimodal diagnosis
- cross-site medical generalization
- multi-illumination medical imaging
- modality-specific fine-tuning medical
- feature-level multimodal ensemble
- patient-level medical prediction
- multimodal clinical classification
- contrastive learning medical imaging

## Tools Used
- web_search: Search arXiv for related papers
- web_extract: Fetch paper details
- exec: Run Python for ML pipelines
- write: Create analysis scripts or reports

## Core Methodology

### Phase 1: Cross-Modality Contrastive Learning

- Learn shared representation space across multiple imaging modalities
- For microbial keratitis: blue-light, sclerotic-scatter, and white-light illumination
- Contrastive loss pulls same-patient-different-modality representations together
- Pushes different-patient representations apart
- Establishes modality-invariant feature foundation

### Phase 2: Modality-Specific Fine-Tuning

- Fine-tune each modality branch independently
- Capture modality-unique discriminative features
- Blue-light: captures fluorescein staining patterns
- Sclerotic-scatter: reveals stromal infiltration depth
- White-light: shows overall lesion morphology
- Each modality contributes complementary diagnostic information

### Phase 3: Feature-Level Multimodal Ensemble

- Concatenate/combine features from all fine-tuned modality branches
- Patient-level prediction via ensemble of modality-specific predictions
- Handles missing modalities gracefully (single-modality inference)
- Robust to modality-specific artifacts

### Cross-Site Generalization

- **Key finding**: Pooled evaluation is overly optimistic
- **Resampling-based and balance-based re-evaluation** provide realistic cross-site assessment
- Model maintains top performance under all evaluation settings

## Usage Patterns

### Pattern 1: Multi-Illumination Ophthalmology

1. Collect images under multiple illumination modes (blue-light, sclerotic-scatter, white-light)
2. Phase 1: Contrastive pretraining across illumination modes
3. Phase 2: Fine-tune each illumination-specific branch
4. Phase 3: Ensemble prediction at patient level
5. Evaluate with resampling-based cross-site validation

### Pattern 2: General Multimodal Medical Imaging

1. Identify available imaging modalities (e.g., MRI T1/T2/FLAIR, CT/PET)
2. Cross-modality contrastive learning for shared representation
3. Modality-specific fine-tuning for unique features
4. Feature-level ensemble for combined prediction
5. Site-specific evaluation for realistic performance estimate

### Pattern 3: Single-Modality Inference

1. Train full multimodal model (Phases 1-3)
2. At inference, use available modality branches
3. Model gracefully degrades with fewer modalities
4. Clinical deployment flexibility

## Implementation Guide

### Step 1: Contrastive Pretraining

```python
# Cross-modality contrastive learning
# Same patient, different modalities → positive pairs
# Different patients → negative pairs
for patient_batch in dataloader:
    # Extract features from each modality
    features_blue = encoder_blue(patient_batch.blue_images)
    features_sclerotic = encoder_sclerotic(patient_batch.sclerotic_images)
    features_white = encoder_white(patient_batch.white_images)

    # Contrastive loss: pull same-patient features together
    loss = contrastive_loss(
        features_blue, features_sclerotic, features_white,
        labels=patient_ids
    )
    loss.backward()
```

### Step 2: Modality-Specific Fine-Tuning

```python
# Freeze shared encoder, fine-tune modality-specific heads
for modality in ['blue', 'sclerotic', 'white']:
    encoder = get_encoder(modality)
    encoder.train()
    for batch in modality_dataloader(modality):
        features = encoder(batch.images)
        logits = classifier_head[modality](features)
        loss = cross_entropy(logits, batch.labels)
        loss.backward()
```

### Step 3: Feature-Level Ensemble

```python
# Combine modality features for patient-level prediction
def predict_patient(blue_img, sclerotic_img, white_img, metadata):
    f_blue = encoder_blue(blue_img)
    f_sclerotic = encoder_sclerotic(sclerotic_img)
    f_white = encoder_white(white_img)

    # Feature-level fusion
    combined = fuse_features([f_blue, f_sclerotic, f_white], metadata)
    prediction = ensemble_classifier(combined)
    return prediction
```

### Step 4: Cross-Site Evaluation

```python
# Resampling-based evaluation for realistic performance
from sklearn.model_selection import StratifiedShuffleSplit

# Ensure each site is proportionally represented
sss = StratifiedShuffleSplit(n_splits=10, test_size=0.2)
for train_idx, test_idx in ssss.split(X, y, groups=sites):
    # Train and evaluate
    # Report per-site metrics, not just pooled
```

## Error Handling

### Overly Optimistic Pooled Evaluation
- **Problem**: Aggregating all sites hides site-specific degradation
- **Solution**: Always report resampling-based and balance-based metrics

### Missing Modalities at Inference
- **Problem**: Not all imaging modes available for every patient
- **Solution**: Train modality-specific branches; use available subset at inference

### Cross-Site Distribution Shift
- **Problem**: Different sites have different imaging protocols
- **Solution**: Contrastive pretraining provides modality-invariant features; resampling evaluation detects shift

### Class Imbalance
- **Problem**: Rare disease subtypes underrepresented
- **Solution**: Balance-based re-evaluation; weighted contrastive loss

## Results (Microbial Keratitis)

- Dataset: 1,645 patients, 17,158 images from India and United States
- Accuracy: 85.84%
- Average F1: 84.46%
- AUC: 0.885
- Top performance under all evaluation settings (pooled, resampling, balance-based)

## Resources

- Paper: arXiv:2607.03740 — "Triple-Phase Multimodal Knowledge Aggregation Framework for Microbial Keratitis Subtype Diagnosis on Slit-Lamp Photography"
- Authors: Yiqing Wang, Maria A. Woodward, Ziyun Yang, et al.
- Multicenter dataset: India + United States
- Modalities: Blue-light, sclerotic-scatter, white-light slit-lamp photography

## Related Skills

- `hybrid-quantum-classical-feature-fusion-medical` — Feature fusion for medical AI
- `medical-ai-diagnosis` — AI-based medical diagnosis patterns
- `adaptive-hybrid-feature-fusion-medical` — Adaptive feature fusion methodology
- `eeg-visual-attention-decoding` — Multimodal neuroimaging decoding
