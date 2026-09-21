---
name: scale-aware-pretraining-time-series-foundation
description: "Scale-aware pretraining for time series foundation models."
metadata:
  arxiv_id: "2608.20005"
  published: "2026-08-22"
  authors: "Unknown"
  tags: [time-series, foundation-models, pretraining, scale-aware]
license: Complete terms in LICENSE.txt
---

# Scale-Aware Pretraining of Time Series Foundation Models

## Overview
This methodology addresses the challenge of pretraining time series foundation models across heterogeneous datasets with varying sampling frequencies. It proposes SATS (Scale-Aware Token Alignment) featuring a scale-aware token alignment mechanism that treats patch size as an explicit notion of scale.

## Core Principles

### Scale-Aware Token Alignment
The approach treats patch size as an explicit notion of scale and incorporates a contrastive-inspired alignment regularizer to align representation spaces across scales while preserving distinct modeling capacities.

### Multi-Patch Token Alignment
By using different patch sizes for different temporal scales, the model can effectively handle both high-frequency and low-frequency patterns in time series data.

### Hybrid Masking Strategy
A hybrid masking strategy combining random and contiguous masking is introduced to capture multi-scale temporal structures effectively.

## Implementation Workflow

### 1. Dataset Preparation
- Collect heterogeneous time series datasets with varying sampling frequencies
- Normalize and preprocess data appropriately for each dataset

### 2. Scale-Aware Architecture Design
- Implement multiple patch sizes corresponding to different temporal scales
- Design separate feed-forward networks (FFNs) for each scale or use adaptive mechanisms
- Ensure proper token alignment across scales

### 3. Contrastive Alignment Regularization
- Implement contrastive-inspired alignment regularizer
- Align representation spaces across different scales
- Preserve distinct modeling capacities for each scale

### 4. Hybrid Masking Implementation
- Combine random masking with contiguous masking
- Tune masking ratios for optimal multi-scale structure capture
- Validate masking effectiveness on downstream tasks

### 5. Pretraining and Fine-tuning
- Pretrain on heterogeneous datasets using the scale-aware approach
- Fine-tune on specific downstream tasks
- Evaluate performance improvements

## Benefits
- 9.2% improvement in MSE on LSTF benchmarks
- 8.3% gain in GIFT-Eval MASE compared to competitive baselines
- 65.6% increase in model efficiency over advanced baselines
- SOTA performance across multiple time series tasks

## Use Cases
- Financial time series analysis
- IoT sensor data processing
- Healthcare monitoring systems
- Climate and weather forecasting
- Any domain with heterogeneous time series data

## Activation Keywords
- scale-aware pretraining
- time series foundation models
- multi-patch token alignment
- hybrid masking
- heterogeneous time series
- SATS

## References
- Original paper: https://arxiv.org/abs/2608.20005