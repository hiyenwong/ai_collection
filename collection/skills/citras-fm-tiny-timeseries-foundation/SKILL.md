---
name: citras-fm-tiny-timeseries-foundation
description: CITRAS-FM tiny 7M-parameter time series foundation model with covariate-informed zero-shot forecasting using Shifted Attention and CovSynth synthetic covariate generation
version: 1.0.0
author: extracted from arXiv:2606.10798v1
date: 2026-06-11
activation_keywords: [time series, foundation model, zero-shot forecasting, covariate, tiny model, CPU inference, Transformer, patch-based]
---

# CITRAS-FM: Tiny Time Series Foundation Model

## Overview

CITRAS-FM is a tiny 7M-parameter time series foundation model (TSFM) that supports univariate, multivariate, and covariate-informed zero-shot forecasting with real-time CPU inference. It achieves state-of-the-art zero-shot accuracy among sub-10M TSFMs with sub-0.1-second inference.

## Core Innovation

**Tiny Foundation Model Pattern:**
- **7M parameters**: Tiny model achieving SOTA among sub-10M TSFMs
- **Covariate-informed**: Shifted Attention exploits known covariates throughout forecast horizon
- **Zero-shot forecasting**: Works on unseen target series without training
- **Real-time deployment**: Sub-0.1-second CPU inference for production use

## Problem Addressed

**TSFM Challenges:**
1. **High computational cost**: Existing TSFMs often expensive to deploy
2. **Limited variable types**: Poor support for diverse covariate types
3. **Covariate scarcity**: Limited covariate-rich corpora for pretraining
4. **Exogenous influence**: Failing to account for covariates affecting target variability

## Methodology

### Architecture Components

1. **Patch-based Decoder-only Transformer**
   - Efficient time series patch processing
   - Decoder-only architecture for forecasting
   - Tiny 7M parameter count

2. **Shifted Attention (Cross-variate Module)**
   - Exploits known covariates accessible throughout forecast horizon
   - Shift mechanism aligns covariate information with target
   - Cross-variate attention for multivariate/covariate scenarios

3. **CovSynth (Covariate Synthesis)**
   - Synthesizes realistic covariates from decomposed target series components
   - Enables covariate-aware pretraining despite scarce covariate-rich corpora
   - Decomposed components generate synthetic covariates

### Pretraining Protocol

1. **Target Decomposition**: Decompose time series into components
2. **Covariate Synthesis**: Use components to generate synthetic covariates (CovSynth)
3. **Covariate-aware Training**: Train with synthetic covariates for generalization
4. **Zero-shot Deployment**: Apply to unseen targets with real covariates

## Performance Metrics

- **fev-bench**: State-of-the-art zero-shot accuracy among sub-10M TSFMs
- **100 tasks**: Evaluated across various forecasting settings
- **CPU inference**: Sub-0.1-second real-time inference
- **Model size**: 7M parameters (tiny category)

## Use Cases

- Zero-shot time series forecasting on unseen data
- Covariate-informed forecasting with known exogenous variables
- Real-time production deployment with CPU inference
- Multivariate forecasting with multiple target series
- Foundation model approach for time series domains

## Implementation Guidelines

1. **Patch Processing**: Use patch-based input for time series segments
2. **Decoder Architecture**: Decoder-only Transformer for autoregressive forecasting
3. **Shifted Attention**: Implement shift mechanism in cross-variate module
4. **CovSynth**: Generate synthetic covariates from target decomposition
5. **Tiny Model Design**: Balance parameter count with accuracy

## Key Parameters

- Model parameters: 7M (tiny foundation model)
- Architecture: Patch-based decoder-only Transformer
- Attention type: Shifted Attention for cross-variate
- Covariate synthesis: CovSynth from decomposed components
- Inference: Sub-0.1-second CPU deployment

## Advantages Over Previous Methods

- **Computational cost**: Tiny 7M model vs expensive larger TSFMs
- **Covariate support**: Full support for diverse variable types
- **Pretraining data**: CovSynth solves covariate corpus scarcity
- **Real-time deployment**: CPU inference for production scenarios
- **Zero-shot capability**: Works on unseen targets without adaptation

## Technical Details

### Model Architecture

```
Input: Time series patches + Covariates
  ↓
Patch-based Processing: Segmented time series representation
  ↓
Shifted Attention: Cross-variate module for covariate exploitation
  ↓
Decoder-only Transformer: Autoregressive forecasting
  ↓
Output: Zero-shot forecasts with covariate influence
```

### CovSynth Process

- Target decomposition: Time series → Components (trend, seasonality, residuals)
- Covariate generation: Components → Synthetic covariates
- Pretraining: Use synthetic covariates to train covariate-aware model
- Zero-shot: Deploy on real covariates without fine-tuning

## References

- arXiv:2606.10798v1 - CITRAS-FM: Tiny Time Series Foundation Model for Covariate-Informed Zero-Shot Forecasting
- fev-bench benchmark (100 tasks across various settings)
- Sub-10M TSFM category comparisons

## Related Skills

- `time-series-foundation-model` - General TSFM patterns
- `zero-shot-forecasting` - Zero-shot forecasting methodologies
- `covariate-modeling` - Covariate-aware modeling approaches
- `tiny-model-design` - Tiny foundation model design patterns
- `patch-transformer` - Patch-based Transformer architectures