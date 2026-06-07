---
name: geosae-brain-mri-sae
description: >
  GeoSAE methodology for interpretable brain MRI foundation model annotation using
  geometry-guided sparse autoencoders with age-deconfounded partial correlations.
  Prevents SAE feature collapse in deep transformer layers, extracts biomarkers
  from frozen brain MRI foundation models. Achieves MCI-to-AD conversion prediction
  (AUC 0.746) with 2% embedding dimensions, cross-cohort replication (r=0.97).
  Use when: GeoSAE, brain MRI foundation model interpretability, sparse autoencoder
  for medical imaging, Alzheimer's biomarker discovery, age-deconfounded analysis,
  SAE feature collapse prevention, geometric prior SAE, brain MRI annotation,
  ADNI AIBL MRI analysis, Braak staging localization, MCI conversion prediction.
---

# GeoSAE: Geometry-Guided SAE for Brain MRI Foundation Model Annotation

Nerrise et al., Stanford University, arXiv:2605.01829 (May 2026)
CVPR Workshop on Computer Vision for Clinical Applications (CV4Clinical) 2026

## Problem

Brain MRI foundation models learn rich anatomical representations, but interpreting
what clinical information they encode remains difficult. Standard SAEs suffer from
**severe feature collapse** in deep transformer layers. In Alzheimer's research,
**aging confounds** nearly every clinical variable, making naive annotation unreliable.

## Core Method

GeoSAE uses the foundation model's **learned manifold geometry** to prevent feature
collapse and annotates surviving features via **age-deconfounded partial correlations**.

### Architecture

```
Brain MRI (T1-weighted)
    → Frozen Foundation Model (e.g., SynthSeg, FreeSurfer-style)
    → Layer-wise activations
    → GeoSAE (geometry-guided sparse autoencoder)
    → Interpretable features
    → Age-deconfounded partial correlation annotation
    → Clinical biomarker mapping
```

### Key Innovations

1. **Geometric prior guidance**: Uses the manifold structure learned by the foundation
   model to guide SAE training, preventing feature collapse in deep layers
2. **Age-deconfounded annotation**: Partial correlations control for age, isolating
   disease-specific signals from normal aging effects
3. **Cross-cohort replication**: Features replicate across ADNI → AIBL without
   retraining (r=0.97)

## Results

| Metric | Value |
|--------|-------|
| MCI-to-AD AUC | 0.746 |
| Embedding dimensions used | 2% |
| Cross-cohort replication | r=0.97 |
| Comorbidity-annotated features | Chance-level |
| Datasets | ~14k T1 scans (ADNI + AIBL) |

### Key Findings

- **Compact interpretable feature set** predicts MCI-to-AD conversion using only 2%
  of embedding dimensions
- **Comorbidity-annotated features** achieve only chance-level performance, suggesting
  GeoSAE captures disease-specific rather than comorbid signals
- **Neuroanatomical localization** consistent with Braak staging of AD pathology
- **Cross-cohort generalization** without any retraining needed

## Datasets

- **ADNI**: Alzheimer's Disease Neuroimaging Initiative
- **AIBL**: Australian Imaging Biomarkers and Lifestyle Study
- **Total**: ~14,000 T1-weighted MRI scans

## Usage Patterns

### 1. Biomarker Discovery from Frozen Models
Apply GeoSAE to any frozen brain MRI foundation model to extract interpretable
clinical biomarkers without retraining the base model.

### 2. Age-Deconfounded Clinical Analysis
Use partial correlation annotation to separate disease effects from normal aging,
critical for neurodegenerative disease research.

### 3. Cross-Cohort Validation
Leverage geometry-guided features that replicate across different datasets without
retraining, enabling multi-site biomarker validation.

### 4. SAE Feature Collapse Prevention
Use geometric priors from the foundation model's manifold structure to guide SAE
training in deep transformer layers.

## Limitations

- Requires a pretrained brain MRI foundation model
- T1-weighted MRI only (no multi-modal extension shown)
- Age deconfounding assumes linear age effects
- Focused on AD/MCI — extension to other diseases needs validation

## Code

- https://github.com/favour-nerrise/GeoSAE

## Related Work

- Sparse Autoencoders (SAEs) for LLM interpretability
- Brain MRI foundation models (SynthSeg, SynSegHD, etc.)
- Alzheimer's disease neuroimaging biomarkers
- Braak staging of AD pathology
- Age-deconfounded neuroimaging analysis
