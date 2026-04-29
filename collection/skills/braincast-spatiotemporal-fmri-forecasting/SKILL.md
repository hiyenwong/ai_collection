---
name: braincast-spatiotemporal-fmri-forecasting
version: 1.0.0
created: 2026-04-24
source: arXiv:2603.13361v1
categories: [cs.CV, cs.AI, stat.ML]
status: active
trigger: fmri, forecasting, brain network, time series, spatio-temporal, HCP, functional connectivity, ROI, whole-brain
description: Skill for braincast spatiotemporal fmri forecasting
---


# BrainCast: Spatio-Temporal Forecasting Model for Whole-Brain fMRI Time Series Prediction

**arXiv**: [2603.13361v1](https://arxiv.org/abs/2603.13361v1)
**Authors**: Yunlong Gao, Jinbo Yang, Li Xiao, Haiye Huo, Yang Ji et al. (8 authors)
**Published**: 2026-03-09
**Categories**: cs.CV, cs.AI, stat.ML

## Overview

Functional magnetic resonance imaging (fMRI) enables noninvasive investigation of brain function, while short clinical scan durations, arising from human and non-human factors, usually lead to reduced data quality and limited statistical power for neuroimaging research. In this paper, we propose BrainCast, a novel spatio-temporal forecasting framework specifically tailored for whole-brain fMRI time series forecasting, to extend informative fMRI time series without additional data acquisition. It formulates fMRI time series forecasting as a multivariate time series prediction task and jointly models temporal dynamics within regions of interest (ROIs) and spatial interactions across ROIs. Specifically, BrainCast integrates a Spatial Interaction Awareness module to characterize inter-ROI dependencies via embedding every ROI time series as a token, a Temporal Feature Refinement module to capture intrinsic neural dynamics within each ROI by enhancing both low- and high-energy temporal components of fMRI time series at the ROI level, and a Spatio-temporal Pattern Alignment module to combine spatial and temporal representations for producing informative whole-brain features. Experimental results on resting-state and task fMRI datasets from the Human Connectome Project demonstrate the superiority of BrainCast over state-of-the-art time series forecasting baselines. Moreover, fMRI time series extended by BrainCast improve downstream cognitive ability prediction, highlighting the clinical and neuroscientific impact brought by whole-brain fMRI time series forecasting in scenarios with restricted scan durations.

## Methodology

### Core Architecture: BrainCast

BrainCast formulates whole-brain fMRI time series forecasting as a multivariate time series prediction task, jointly modeling:
- **Temporal dynamics** within regions of interest (ROIs)
- **Spatial interactions** across ROIs

### Three Key Modules

1. **Spatial Interaction Awareness (SIA) Module**
   - Embeds every ROI time series as a token
   - Characterizes inter-ROI dependencies via attention mechanisms
   - Captures whole-brain functional connectivity patterns

2. **Temporal Feature Refinement (TFR) Module**
   - Captures intrinsic neural dynamics within each ROI
   - Enhances both low-energy and high-energy temporal components of fMRI time series
   - Operates at ROI level for fine-grained temporal modeling

3. **Spatio-temporal Pattern Alignment (SPA) Module**
   - Combines spatial and temporal representations
   - Produces informative whole-brain features for forecasting
   - Aligns multi-scale representations for prediction

### Training & Evaluation
- Trained and evaluated on Human Connectome Project (HCP) data
- Both resting-state and task fMRI datasets
- Demonstrated superiority over SOTA time series forecasting baselines
- Extended fMRI time series improve downstream cognitive ability prediction

## Applications

- **Clinical Scan Extension**: Extend short clinical fMRI scans without additional acquisition time
- **Cognitive Ability Prediction**: Improve downstream prediction from extended time series
- **Data Augmentation**: Generate realistic fMRI data for training other models
- **Missing Data Imputation**: Fill gaps in interrupted fMRI recordings

## Technical Details

### Input Specifications
- Neural signal modality and format appropriate to the methodology
- Sampling rate and temporal resolution requirements vary by application
- Spatial resolution depends on recording technique (EEG, fMRI, neural recording)

### Output Specifications
- Task-specific output format (forecasting, generation, control, decoding)
- Confidence/uncertainty estimates where applicable
- Interpretable representations for neuroscientific analysis

### Computational Requirements
- GPU recommended for training deep learning components
- Memory requirements scale with data dimensionality
- Real-time inference feasible for control and BCI applications

## Limitations & Considerations

- Model performance depends on data quality, quantity, and preprocessing
- Generalization across subjects, recording setups, and tasks may be limited
- Interpretability vs. performance trade-offs should be evaluated
- Biological plausibility assumptions should be validated experimentally

## References

- Original paper: arXiv:2603.13361v1 (2026-03-09)
- Tested on relevant neuroscience datasets as described in the paper

## Relevance to Other Skills

This methodology complements existing skills in brain signal processing, neural dynamics modeling, and computational neuroscience. Related skills include neural dynamics analysis, brain network construction, and neural decoding frameworks.


## Activation Keywords

- braincast-spatiotemporal-fmri-forecasting
- braincast spatiotemporal fmri
- braincast spatiotemporal fmri forecasting


## Tools Used

- `read` - 读取技能文档
- `write` - 创建输出
- `exec` - 执行相关命令


## Instructions for Agents

1. 理解技能的核心方法论
2. 根据用户问题提供针对性回答
3. 遵循最佳实践


## Examples

### Example 1: 基本查询

**User:** 请解释 Braincast Spatiotemporal Fmri Forecasting

**Agent:** Braincast Spatiotemporal Fmri Forecasting 是关于...
