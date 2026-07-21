---
name: stst-jepa-eeg-foundation
description: "STST-JEPA: Shallow-Target Spatio-Temporal Joint Embedding Prediction Architecture for EEG self-supervised learning. Combines latent-prediction objective with auxiliary signal-reconstruction term under spatiotemporal block masks. Pretrained on 47,703 EEG sessions (ages 5-81), achieves MAE=3.06 years for brain-age regression. Native 30-second windows achieve rank-1 on NeuralBench x EEGD leaderboard for sex classification (BA=0.911) and age prediction (r=0.749). Age-prediction residual negatively correlated with cognitive efficiency."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [eeg, self-supervised-learning, brain-age, JEPA, foundation-model, neural-benchmark, spatiotemporal-masking, EMA-target, cognitive-efficiency]
    category: ai_collection/collection/skills/neuroscience
    arxiv_id: "2607.06629"
    arxiv_url: "https://arxiv.org/abs/2607.06629"
    published: "2026-07-07"
    authors: ["Roy Segal", "Yoni Svechinsky", "Tomer Fekete"]
    categories: ["cs.LG", "q-bio.NC"]
    trigger_words: ["STST-JEPA", "shallow-target JEPA", "EEG self-supervised", "EEG brain-age", "EEG foundation model", "NeuralBench", "EEGD", "latent prediction EEG", "spatiotemporal block mask", "cognitive efficiency EEG", "EMA tokenizer EEG"]
created: "2026-07-13"
updated: "2026-07-13"
---

# STST-JEPA: Shallow-Target Spatio-Temporal Joint Embedding Prediction Architecture For EEG Self-Supervised Learning

**arXiv**: 2607.06629 | **Published**: 2026-07-07 (v2: 2026-07-09) | **Authors**: Roy Segal, Yoni Svechinsky, Tomer Fekete

## Core Innovation

Introduces **STST-JEPA**, a self-supervised transformer for resting-state and task EEG that combines two objectives:
1. **Latent-prediction objective**: Predicting masked-token representations against an EMA-of-tokenizer target
2. **Auxiliary signal-reconstruction term**: Applied to 30-second multi-channel windows under spatiotemporal block masks

## Key Results

### Pretraining Scale
- **47,703 EEG sessions** spanning ages 5-81
- Data from TUH (Temple University Hospital) and Healthy Brain Network (HBN) corpora
- **First EEG foundation model** to cover the full pediatric-to-older-adult range

### Brain-Age Regression
- **MAE = 3.06 years** (r = 0.924) on 3,367 held-out sessions
- **Baseline: ~10 years MAE** (predict-the-mean)
- Lightweight attentive probe on frozen pretrained embeddings

### NeuralBench x EEGD Leaderboard (Rank-1)
Using native 30-second windows with light task-specific finetuning of final layers:
| Task | Metric | Score |
|------|--------|-------|
| Sex classification | Balanced accuracy | **0.911** |
| Age prediction | Pearson r | **0.749** |
| Psychopathology composite | Pearson r | **0.215** |

### Cognitive Efficiency Correlation
- Age-prediction residual (predicted - chronological age) is **negatively correlated with cognitive efficiency** across several examined tasks
- This validates brain-age deviation as a meaningful biomarker

## Architecture Details

### STST-JEPA Design

**Shallow-Target** refers to predicting against an EMA (Exponential Moving Average) of the tokenizer's representations, rather than predicting raw signal or deep features. This approach:
- Provides stable, smooth targets for learning
- Avoids the collapse issues common in self-supervised learning
- Captures meaningful spatio-temporal structure in EEG

**Spatiotemporal Block Masking**:
- Masks are applied in both spatial (channel) and temporal (time) dimensions simultaneously
- Forces the model to learn cross-channel and cross-temporal dependencies
- More biologically plausible than random masking (models natural data loss patterns)

**Dual Objective**:
1. **Primary**: JEPA-style latent prediction (predicting representations, not pixels/signal)
2. **Auxiliary**: Signal reconstruction (ensures the learned representations retain signal fidelity)

### Why This Works for EEG

1. **Cross-site heterogeneity**: Self-supervised pretraining on massive diverse data learns representations robust to montage differences
2. **Small labeled cohorts**: Frozen embeddings + lightweight probe avoids overfitting
3. **Subject-level non-stationarity**: The EMA target provides stable learning signals despite individual variability
4. **Full age range**: 47K sessions across 5-81 years enables learning developmental trajectories

## Comparison to Prior EEG Foundation Models

Previous EEG foundation models struggled with:
- Limited pretraining data (typically <10K sessions)
- Narrow age ranges (often adults only)
- Poor cross-site generalization
- Weak performance on downstream tasks

STST-JEPA addresses all four limitations simultaneously.

## Practical Applications

### 1. Brain-Age as Biomarker
- Use the pretrained model for rapid brain-age estimation from 30-second EEG windows
- Deviation from chronological age tracks neurological and psychiatric burden
- Applicable across full lifespan (pediatric to older adult)

### 2. EEG Classification/Regression
- Fine-tune the last layers for any downstream EEG task
- Native 30-second window handling (no need for arbitrary epoching)
- Achieves SOTA on sex, age, and psychopathology prediction

### 3. Cognitive Assessment
- Age-prediction residual correlates with cognitive efficiency
- Can serve as a screening tool for cognitive decline or enhancement

### 4. Cross-Site EEG Analysis
- Model handles montage heterogeneity natively
- Useful for multi-site studies and clinical deployment

## Methodology for Reproduction

1. **Data**: TUH + HBN corpora (47,703 sessions, ages 5-81)
2. **Preprocessing**: Standardize to common montage, handle missing channels
3. **Pretraining**: 
   - Spatiotemporal block masking on 30-second windows
   - Dual objective: JEPA latent prediction + signal reconstruction
   - EMA target for stable training
4. **Downstream**:
   - Frozen embeddings + lightweight probe (for brain-age)
   - Light finetuning of final layers (for classification/regression)

## Key Insight

The combination of **shallow-target prediction** (predicting EMA-of-tokenizer representations) with **signal reconstruction** creates representations that are both semantically meaningful and signal-faithful — addressing the core tension in self-supervised EEG learning between abstraction and fidelity.

## Trigger Words

STST-JEPA, shallow-target JEPA, EEG self-supervised learning, EEG brain-age, EEG foundation model, NeuralBench EEGD, spatiotemporal block masking, EMA tokenizer, cognitive efficiency EEG, latent prediction EEG, EEG representation learning, brain-age biomarker
