---
name: adaptive-spiking-neurons-asn
description: Adaptive Spiking Neurons (ASN) with trainable membrane potential dynamics and adaptive firing for vision and language modeling. Includes NASN variant with normalization for stable training. Uses integer training + spike inference paradigm.
version: 1.0.0
arxiv: 2604.12365v1
tags:
  - spiking-neural-networks
  - adaptive-neurons
  - trainable-dynamics
  - vision-modeling
  - language-modeling
  - normalization
  - energy-efficiency
---

# Adaptive Spiking Neurons (ASN)

## Overview

This skill implements **Adaptive Spiking Neurons (ASN)** — a new generation of general-purpose spiking neurons with trainable parameters for membrane potential dynamics and adaptive firing. ASN supports an integer training and spike inference paradigm for efficient SNN training, and includes the Normalized Adaptive Spiking Neuron (NASN) variant for enhanced training stability.

## Key Contributions

1. **Functional perspective for neuron design**: A novel framework providing general guidance for designing next-generation spiking neurons
2. **Adaptive Spiking Neuron (ASN)**: Incorporates trainable parameters to learn membrane potential dynamics and enable adaptive firing
3. **Normalized Adaptive Spiking Neuron (NASN)**: Integrates normalization to stabilize training
4. **Integer training + spike inference**: Efficient training paradigm with integer arithmetic during training, spiking during inference
5. **Broad evaluation**: Tested on 19 datasets spanning 5 distinct tasks across vision and language modalities

## ASN Architecture

### Trainable Membrane Dynamics

Unlike standard LIF neurons with fixed time constants, ASN learns the membrane potential update dynamics through trainable parameters:

```
u(t) = f_θ(u(t-1), x(t))    # Learned membrane dynamics
s(t) = g_φ(u(t))             # Learned adaptive firing
```

Where θ and φ are learned parameters, enabling the neuron to adapt its behavior to the task.

### Integer Training + Spike Inference

- **Training**: Uses integer-valued representations for computational efficiency
- **Inference**: Converts to standard spike-based representation for deployment
- This paradigm enables efficient SNN training while maintaining spike-based inference benefits

### NASN Variant

- Adds **normalization layers** to stabilize training dynamics
- Particularly useful for deeper networks and complex tasks
- Prevents gradient explosion/vanishing in multi-layer SNNs

## Evaluation Scope

| Modality | Tasks | Datasets |
|----------|-------|----------|
| Vision | Image classification, object detection, etc. | Multiple |
| Language | Text classification, sequence modeling, etc. | Multiple |
| **Total** | **5 distinct tasks** | **19 datasets** |

## Implementation Guide

See `references/implementation.md` for detailed code patterns including:
- Base ASN with trainable membrane dynamics
- Adaptive firing threshold mechanism
- NASN with normalization
- Integer training + spike inference pipeline
- Multi-modal integration (vision + language)

## Usage

This skill is applicable when:
- Building high-performance SNNs for vision or language tasks
- Designing custom spiking neuron models with learned dynamics
- Training SNNs with improved stability via normalization
- Converting between integer-trained and spike-inference representations
- Developing general-purpose spiking neurons for diverse tasks

## References

- **Paper**: "Adaptive Spiking Neurons for Vision and Language Modeling"
- **arXiv**: 2604.12365v1
