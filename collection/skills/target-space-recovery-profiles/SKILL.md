---
name: target-space-recovery-profiles
description: Target-Space Recovery Profiles (TSRP) methodology for evaluating model-brain alignment beyond prediction accuracy. Identifies which reproducible brain response dimensions are recovered by prediction models.
category: ai_collection
keywords: model-brain alignment, target-space recovery, fMRI encoding, visual cortex, prediction accuracy, response dimensions, NSD dataset, neural encoding evaluation
created: 2026-05-21
arxiv_id: "2605.20127"
arxiv_url: "https://arxiv.org/abs/2605.20127"
source: cron-neuroscience-research
---

# Target-Space Recovery Profiles (TSRP) for Model-Brain Alignment Evaluation

## Paper
- **Title**: Beyond Prediction Accuracy: Target-Space Recovery Profiles for Evaluating Model-Brain Alignment
- **Authors**: Ken Nakamura, Tomoya Nakai, Ryuto Yashiro, Ayumu Yamashita, Kaoru Amano
- **arXiv**: 2605.20127 (2026-05-19)
- **URL**: https://arxiv.org/abs/2605.20127

## Problem
AI vision models are evaluated against human visual cortex by measuring how accurately their internal representations predict brain responses (fMRI). However, **prediction accuracy alone is insufficient**:
- Two models can achieve similar accuracy while recovering completely different response dimensions
- Accuracy doesn't reveal which brain response patterns are actually captured
- No diagnostic framework exists to compare model-brain vs brain-brain alignment

## Core Methodology: TSRP Framework

### Step 1: Identify Reproducible Response Dimensions
- Use repeated fMRI measurements across independent trial splits
- Identify target-brain response dimensions that can be reproducibly predicted
- These represent the "true signal" in brain responses that any model should recover

### Step 2: Predict Target-Brain Responses
- Either from another subject's brain responses (brain-to-brain) or model representations (model-to-brain)
- Quantify how strongly each reproducible response dimension is recovered

### Step 3: Recovery Profile Analysis
- For each reproducible dimension, measure the prediction strength
- Create a "recovery profile" vector showing which dimensions are well-recovered
- Compare profiles across models and against human brain-to-brain baseline

## Key Findings
1. **Early-to-intermediate visual cortex responses contain a low-dimensional set of reproducible dimensions**
2. **Brain-to-brain comparisons identify consistently recoverable dimensions**, providing a diagnostic human reference
3. **Pretrained and randomly initialized models can achieve similar accuracy but show distinct recovery profiles**
4. **Prediction accuracy alone masks model-brain mismatches** — two models with equal accuracy may recover entirely different neural dimensions

## Technical Approach
```
Repeated fMRI → Split-half reproducibility analysis → Reproducible dimensions
    ↓
Model/Brain predictor → Predict target responses → Recovery strength per dimension
    ↓
Recovery Profile = [strength_dim1, strength_dim2, ...]
```

## Activation Triggers
- model-brain alignment evaluation
- neural encoding model assessment
- fMRI response prediction
- brain-to-brain comparison
- visual encoding models
- neural representational analysis

## Pitfalls
- Requires repeated fMRI measurements (expensive)
- Reproducibility threshold selection affects dimension count
- May need different analysis for different brain regions
- Recovery profile interpretation requires neuroscientific expertise

## Related Skills
- `neural-encoding-evaluation-ground-truth`: Ground-truth approximation for neural encoding
- `neural-encoding-evaluation-meeg`: Evaluation framework for MEEG encoding models
- `eeg-preprocessing-reliability`: EEG decoding reliability assessment
- `same-brain-different-prediction`: EEG decoding reliability methodology
