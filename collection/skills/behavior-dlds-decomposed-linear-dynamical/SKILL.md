---
name: behavior-dlds-decomposed-linear-dynamical
version: 1.0.0
created: 2026-04-24
source: arXiv:2603.05612v1
categories: [q-bio.NC, cs.LG, stat.AP, stat.ML]
status: active
trigger: LDS, linear dynamical systems, behavior, decomposition, zebrafish, neural population, latent dynamics, subsystem, large-scale recording
description: Skill for behavior dlds decomposed linear dynamical
---


# Behavior-dLDS: Decomposed Linear Dynamical Systems for Neural Activity Constrained by Behavior

**arXiv**: [2603.05612v1](https://arxiv.org/abs/2603.05612v1)
**Authors**: Eva Yezerets, En Yang, Misha B. Ahrens, Adam S. Charles
**Published**: 2026-03-05
**Categories**: q-bio.NC, cs.LG, stat.AP, stat.ML

## Overview

Brain-wide recordings of large-scale networks of neurons now provide an unprecedented view into how the brain drives behavior. However, brain activity contains both information directly related to behavior as well as the potential for many internal computations. Moreover, observable behavior is executed not only by the brain, but also by the spinal cord and peripheral nervous system. Behavior is a coarse-grained product of neural activity, and we thus take the view that it can be best represented by lower-dimensional latent neural dynamics. Capturing this indirect relationship while disambiguating behavior-generating networks from internal computations running in parallel requires new modeling approaches that can embody the parallel and distributed nature of large-scale neural populations. We thus present behavior-decomposed linear dynamical systems (b-dLDS) to disentangle simultaneously recorded subsystems and identify how the latent neural subsystems relate to behavior. We demonstrate the ability of b-dLDS to decouple behavioral vs. internal computations on controlled, simulated data, showing improvements over a state-of-the-art model that uses behavior to supervise all dynamics based on behavior. We then show that b-dLDS can further scale up to tens of thousands of neurons by applying our model to large-scale recording of a zebrafish hindbrain during the complex positional homeostasis behavior, wherein b-dLDS highlights behavior-related dynamic connectivity networks.

## Methodology

### Core Architecture: Behavior-dLDS

b-dLDS disentangles simultaneously recorded neural subsystems to identify how latent neural subsystems relate to behavior.

### Key Innovation: Behavioral Decomposition

1. **Subsystem Decomposition**
   - Separates behavior-generating dynamics from internal computations
   - Models parallel and distributed nature of large-scale neural populations
   - Each subsystem captured by its own linear dynamical system

2. **Behavior-Constrained Learning**
   - Uses behavioral measurements to partially constrain neural dynamics
   - Lower-dimensional latent dynamics represent behavior-generating subsystem
   - Remaining dynamics capture internal computations running in parallel

3. **Scalable Architecture**
   - Scales to tens of thousands of neurons
   - Applied to large-scale zebrafish hindbrain recordings
   - Complex positional homeostasis behavior analysis

### Model Structure
- **Behavioral subspace**: Low-dimensional latent dynamics linked to observed behavior
- **Internal subspace**: High-dimensional dynamics for ongoing internal computations
- **Coupling mechanism**: Interaction between behavioral and internal subsystems
- **Linear dynamics**: Each subspace modeled as linear dynamical system for interpretability

## Applications

- **Large-scale Neural Recording Analysis**: Tens of thousands of neurons simultaneously
- **Zebrafish Neuroscience**: Positional homeostasis and other complex behaviors
- **Behavioral Neural Dynamics**: Disentangle behavior-related from internal neural computations
- **Neural Circuit Identification**: Highlight behavior-related dynamic connectivity networks
- **Systems Neuroscience**: Understand distributed processing in large neural populations

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

- Original paper: arXiv:2603.05612v1 (2026-03-05)
- Tested on relevant neuroscience datasets as described in the paper

## Relevance to Other Skills

This methodology complements existing skills in brain signal processing, neural dynamics modeling, and computational neuroscience. Related skills include neural dynamics analysis, brain network construction, and neural decoding frameworks.


## Activation Keywords

- behavior-dlds-decomposed-linear-dynamical
- behavior dlds decomposed
- behavior dlds decomposed linear dynamical


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

**User:** 请解释 Behavior Dlds Decomposed Linear Dynamical

**Agent:** Behavior Dlds Decomposed Linear Dynamical 是关于...
