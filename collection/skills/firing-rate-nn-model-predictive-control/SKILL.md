---
name: firing-rate-nn-model-predictive-control
version: 1.0.0
created: 2026-04-24
source: arXiv:2603.25959v1
categories: [eess.SY]
status: active
trigger: firing rate, model predictive control, MPC, planning, sparse network, inverted pendulum, contraction theory, biological plausibility, neural dynamics
description: "Firing Rate Neural Network Implementations of Model Predictive Control"
---

# Firing Rate Neural Network Implementations of Model Predictive Control

**arXiv**: [2603.25959v1](https://arxiv.org/abs/2603.25959v1)
**Authors**: Jaidev Gill, Jing Shuang Li
**Published**: 2026-03-26
**Categories**: eess.SY

## Overview

Human and animal brains perform planning to enable complex movements and behaviors. This process can be effectively described using model predictive control (MPC); that is, brains can be thought of as implementing some version of MPC. How is this done? In this work, we translate model predictive controllers into firing rate neural networks, offering insights into the nonlinear neural dynamics that underpin planning. This is done by first applying the projected gradient method to the dual problem, then generating alternative networks through factorization and contraction analysis. This allows us to explore many biologically plausible implementations of MPC. We present a series of numerical simulations to study different neural networks performing MPC to balance an inverted pendulum on a cart (i.e., balancing a stick on a hand). We illustrate that sparse neural networks can effectively implement MPC; this observation aligns with the sparse nature of the brain.

## Methodology

### Core Architecture: Neural Network MPC Translation

Translates model predictive controllers into firing rate neural networks, offering insights into nonlinear neural dynamics underlying planning.

### Key Innovation: MPC → Neural Network Translation

1. **Projected Gradient Method on Dual Problem**
   - Reformulates MPC optimization as neural-network-compatible computation
   - Applies projected gradient descent to the dual formulation
   - Maps optimization steps to neural network layers

2. **Factorization and Contraction Analysis**
   - Generates alternative network implementations through weight factorization
   - Contraction theory ensures stability of neural dynamics
   - Explores biologically plausible implementations

3. **Sparse Neural Network Discovery**
   - Demonstrates that sparse neural networks can effectively implement MPC
   - Aligns with observed sparse connectivity in biological brains
   - Provides computational justification for brain sparsity

### Validation: Inverted Pendulum
- Cart-pole balancing task (stick balancing on hand)
- Multiple neural network implementations compared
- Sparse networks shown effective for real-time control
- Biological plausibility verified through dynamics analysis

## Applications

- **Computational Neuroscience**: Explain how brains implement planning via MPC
- **Neural Circuit Design**: Design biologically plausible circuits for control tasks
- **Neuromorphic Engineering**: Implement MPC on neuromorphic hardware
- **Brain-inspired Robotics**: Sparse neural controllers for robot planning
- **Motor Control Theory**: Bridge between control theory and neural implementation

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

- Original paper: arXiv:2603.25959v1 (2026-03-26)
- Tested on relevant neuroscience datasets as described in the paper

## Relevance to Other Skills

This methodology complements existing skills in brain signal processing, neural dynamics modeling, and computational neuroscience. Related skills include neural dynamics analysis, brain network construction, and neural decoding frameworks.
