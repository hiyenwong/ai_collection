---
name: autoregressive-flow-matching-neural-dynamics
description: >
  Autoregressive Flow Matching (AFM) methodology for probabilistic prediction of
  neural dynamics from multimodal sensory input. Models neural activity as a
  temporally evolving process where future states depend on recent neural history.
  Evaluated on Algonauts 2025 challenge fMRI dataset using subject-specific models.
  Use when: (1) Probabilistic neural dynamics prediction, (2) fMRI time-series
  forecasting, (3) Closed-loop neurotechnology applications, (4) Flow-based
  generative modeling for neuroscience, (5) Autoregressive neural response prediction.
  Activation: autoregressive flow matching, neural dynamics prediction, fMRI forecasting,
  flow matching neuroscience, probabilistic neural prediction, Algonauts challenge,
  BOLD prediction, transport-based generative modeling neural.
---

# Autoregressive Flow Matching for Neural Dynamics Prediction

## Paper

**Title:** Probabilistic Prediction of Neural Dynamics via Autoregressive Flow Matching
**Authors:** Nicole Rogalla, Yuzhen Qin, Mario Senden, Ahmed El-Gazzar, Marcel van Gerven
**arXiv:** [2604.11178](https://arxiv.org/abs/2604.11178)
**Published:** 2026-04-13
**Categories:** q-bio.NC, cs.LG
**Size:** 25 pages, 4 figures

## Core Methodology

### Problem
Forecasting neural activity in response to naturalistic stimuli — predicting future
BOLD activity given past neural dynamics and concurrent sensory input.

### Key Innovation: Autoregressive Flow Matching (AFM)
- Adapts **flow matching** (transport-based generative modeling) to neural dynamics
- Learns conditional distribution of future neural activity given:
  - Past neural dynamics (recent BOLD history)
  - Concurrent multimodal sensory input
- Models neural activity as **temporally evolving process** with autoregressive dependencies

### Architecture
```
Sensory Input (audio/visual) → Feature Extractors
                                    ↓
Past BOLD Dynamics → Autoregressive Factorization
                                    ↓
Flow Matching Model → Probabilistic Prediction of Future BOLD
```

### Evaluation
- **Dataset:** Algonauts Project 2025 Challenge (fMRI)
- **Models:** Subject-specific AFM models
- **Baselines:** Non-autoregressive flow-matching, GLM (official challenge baseline)
- **Result:** AFM significantly outperforms both baselines in parcel-wise BOLD prediction

### Key Findings
1. **Past BOLD dynamics** is the dominant driver of prediction performance
2. **Autoregressive factorization** yields consistent, modest gains under short-horizon, context-rich conditions
3. Improved **generalization** and widespread **cortical prediction** coverage
4. Most effective for **short-term** probabilistic forecasting

## When to Use
- Predicting fMRI responses to naturalistic stimuli
- Closed-loop neurotechnology requiring probabilistic forecasts
- When GLM or deterministic models fail to capture neural uncertainty
- Multimodal neuroimaging prediction tasks
- When past neural history provides context for future state prediction

## Related Skills
- `autoregressive-flow-matching-neural-dynamics` (this skill)
- `brain-dit-fmri-foundation-model` — fMRI foundation modeling
- `neural-population-dynamics` — neural population analysis

## Key Concepts
- **Flow Matching**: Transport-based generative modeling that learns vector fields
  pushing noise distribution to data distribution
- **Autoregressive Factorization**: Decomposing joint distribution p(x_1:T) into
  sequential conditionals p(x_t | x_{<t})
- **BOLD**: Blood Oxygenation Level Dependent — fMRI signal proxy for neural activity
- **Algonauts Challenge**: Benchmark for computational models predicting brain activity

## Implementation Considerations
- Requires subject-specific model training (not cross-subject generalization)
- Best suited for short-horizon prediction (where past context is most informative)
- Computationally heavier than GLM but provides full probabilistic predictions
- Sensory feature extraction quality critically impacts downstream prediction
