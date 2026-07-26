---
name: mt-direction-maps-spatiotemporal
description: >
  Spatiotemporal TDANN for modeling self-organized MT direction selectivity maps in the dorsal stream.
  Uses 3D ResNet with Momentum Contrast (MoCo) self-supervised learning and biological spatial loss
  to produce direction-selective pinwheel structures matching macaque MT physiology.
  Use when modeling cortical topographic self-organization, dorsal stream computation,
  direction selectivity, or spatiotemporal contrastive learning for visual neuroscience.
  arXiv: 2605.11718 (q-bio.NC, cs.AI, cs.NE). Gu, Li, Su, Liu, Qian, Wang.
---

# Spatiotemporal TDANN for MT Direction Maps

> 3D ResNet with MoCo self-supervised learning + spatial loss produces brain-like direction maps
> and topological pinwheel structures in MT area, matching in vivo macaque physiology.

## Metadata
- **Source**: arXiv:2605.11718
- **Authors**: Zhaotian Gu, Molan Li, Jie Su, Chang Liu, Tianyi Qian, Dahui Wang
- **Published**: 2026-05-12
- **Subjects**: q-bio.NC, cs.AI, cs.NE

## Core Problem

While TDANN has successfully modeled ventral stream topography (e.g., IT cortex), the computational
origins of dorsal stream topographies — particularly direction-selective maps in MT (middle temporal)
area — remained unresolved. This work unifies ventral and dorsal stream origins under one mechanism.

## Key Innovation

**Spatiotemporal TDANN**: Extends Topographic Deep Artificial Neural Network to 3D (spatiotemporal)
domain with two training objectives:

1. **Task-driven discriminative pressure**: MoCo (Momentum Contrast) self-supervised learning on
   naturalistic videos produces motion-direction-selective representations
2. **Spatial regularization**: Biological spatial loss enforces local connectivity patterns

The **strict optimization trade-off** between these two objectives produces:
- Strong direction selectivity with residual axial component
- Spontaneous emergence of brain-like direction maps
- Topological pinwheel structures matching biology

## Technical Framework

### Architecture
- 3D ResNet backbone for spatiotemporal feature extraction
- Trained on naturalistic video stimuli
- MoCo self-supervised paradigm (contrastive learning)
- Biologically inspired spatial loss function

### Emergent Properties
- Direction-selective maps in MT-like units
- Pinwheel structures with biologically realistic density
- Tuning properties matching in vivo macaque MT recordings:
  - Direction selectivity index (DSI)
  - Circular variance
  - Pinwheel density

### Core Mechanism
MT tuning emerges from the balance:
- Discriminative pressure → direction selectivity
- Spatial regularization → topographic organization
- The trade-off produces the characteristic residual axial component of MT neurons

## Applications
- Modeling dorsal stream visual processing
- Cortical topographic self-organization research
- Understanding computational origins of direction selectivity
- Neuro-inspired computer vision with biological inductive biases

## Related Skills
- self-organized-criticality-brain-body-resonance
- neuroscience-of-transformers
- primary-visual-cortex-v1-functions
- untrained-cnns-match-backprop-v1
