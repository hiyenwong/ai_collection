---
name: chaotic-regularization-recurrent-networks
description: Link microscopic chaos in recurrent neural networks to macroscopic geometry of neural representations using kernel methods and dynamical mean-field theory. Chaotic dynamics act as intrinsic regularizer enhancing generalization while preserving expressivity.
keywords: [recurrent neural networks, chaos, neural representations, kernel methods, dynamical mean-field theory, cortical circuits, population codes, power-law spectral signatures, regularization]
authors: [Jan Bauer, Christian Keup, Jonathan Kadmon, Moritz Helias]
arxiv_id: 2606.04426
date_added: 2026-06-04
paper_url: https://arxiv.org/abs/2606.04426
pdf_url: https://arxiv.org/pdf/2606.04426
doi: https://doi.org/10.48550/arXiv.2606.04426
subjects: [q-bio.NC, cond-mat.dis-nn]
---

# Chaotic Regularization in Recurrent Neural Networks

## Overview
Cortical circuits operate in intrinsic chaos regimes, yet population codes vary smoothly with stimuli, forming coherent representational manifolds. This paper develops a theoretical framework linking microscopic chaos to macroscopic representation geometry, explaining how chaotic spiking networks sustain smooth, differentiable population codes.

## Core Methodology

### 1. Theoretical Framework
- **Kernel Methods**: Combine kernel methods with dynamical mean-field theory
- **Local vs Global Smoothness**: Chaotic dynamics induce:
  - **Local roughness**: Sharp distortions at small scales
  - **Global smoothness**: Preserved across larger stimulus variations
- **Intrinsic Regularization**: Structural property acts as regularizer enhancing generalization while maintaining expressivity

### 2. Power-Law Spectral Signatures
- Chaotic networks naturally produce power-law spectral signatures
- Closely matches experimental observations in cortical recordings
- Links network dynamics to recorded neural activity

### 3. Computational Structure
- Establishes connection between:
  - Network dynamics
  - Computational structure
  - Recorded neural activity

## Key Insights

### Chaos as Benefit
- **Challenge**: Tiny input changes → divergent neural responses
- **Solution**: Chaos provides intrinsic regularization
- **Result**: Smooth population codes emerge from chaotic dynamics

### Representation Geometry
- Local roughness improves generalization
- Global smoothness maintains expressivity
- Power-law spectra match cortical observations

## Technical Implementation

### Dynamical Mean-Field Theory
- Analyze chaotic dynamics in recurrent networks
- Connect microscopic chaos to macroscopic representations
- Derive spectral properties matching experiments

### Kernel Methods
- Apply kernel methods to neural representations
- Characterize local vs global smoothness
- Quantify regularization effects

## Applications

### Brain Modeling
- Explain chaotic spiking networks sustaining smooth codes
- Model cortical circuit dynamics
- Predict population code geometry

### AI/ML
- Design chaotic regularization strategies
- Balance expressivity vs generalization
- Optimize recurrent network training

### Neuroscience Research
- Interpret cortical power-law spectra
- Connect dynamics to computational structure
- Validate theoretical predictions experimentally

## Experimental Validation
- Power-law signatures match cortical recordings
- Population codes remain smooth despite chaos
- Spectral properties align with observations

## Implementation Notes

### When to Use
- Modeling cortical circuits with chaotic dynamics
- Explaining smooth population codes from chaos
- Designing regularization from network dynamics
- Interpreting cortical spectral signatures

### Key Parameters
- Chaotic regime strength
- Kernel method selection
- Mean-field approximations
- Spectral signature validation

### Complementary Methods
- Dynamical systems theory
- Statistical mechanics
- Kernel learning
- Information geometry

## References
- arXiv:2606.04426 (original paper)
- Dynamical mean-field theory literature
- Kernel methods in neural networks
- Cortical dynamics experimental studies

## See Also
- [[neural-critical-dynamics-theory]] - Critical dynamics in neural networks
- [[chaos-freezing-without-plasticity]] - Chaos stabilization methods
- [[efficient-coding-criticality-sloppiness]] - Efficient coding under constraints
- [[representation-geometry-neural-networks]] - Representation geometry analysis