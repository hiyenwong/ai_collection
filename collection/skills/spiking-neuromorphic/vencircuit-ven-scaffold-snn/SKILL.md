---
name: vencircuit-ven-scaffold-snn
description: Computational framework showing Von Economo neurons (VENs) function as acquisition scaffolds in recurrent spiking neural networks. Provides gradient pathways immune to Jacobian instabilities, explaining VEN loss in bvFTD and ASC.
category: ai_collection
keywords: Von Economo neurons, spiking neural networks, social learning, gradient pathways, frontotemporal dementia, autism, recurrent circuits, acquisition scaffold
created: 2026-05-21
arxiv_id: "2605.17399"
arxiv_url: "https://arxiv.org/abs/2605.17399"
source: cron-neuroscience-research
---

# VENCircuit: Von Economo Neurons as Acquisition Scaffolds in Recurrent Spiking Networks

## Paper
- **Title**: Von Economo neurons enable reliable social skill acquisition in recurrent spiking neural networks: a computational account with clinical predictions
- **Author**: Esila Keskin
- **arXiv**: 2605.17399 (2026-05-17)
- **URL**: https://arxiv.org/abs/2605.17399

## Problem
Von Economo neurons (VENs) are large, spindle-shaped neurons found in anterior cingulate cortex (ACC) and frontoinsular cortex (FI). They are:
- Selectively lost in behavioral-variant frontotemporal dementia (bvFTD)
- Reduced in autism spectrum conditions (ASC)
- Their computational role in social learning remains unexplained

## Core Methodology: VENCircuit

### Network Architecture
- **Recurrent Pyramidal Circuit**: Base network of pyramidal-like neurons
- **VEN-like Projection Neurons**: K=40 specialized neurons (2% of total) embedded in recurrent circuit
- **Matched Controls**: 50 random initializations with and without VENs

### Key Findings

#### 1. Training Reliability
- VEN-intact networks: 49/50 converged (98%)
- VEN-ablated networks: 35/50 converged (70%)
- Fisher's exact: OR=21.0, 95% CI 2.7-167, p=8.7e-5
- Failed ablated networks showed complete learning absence (not just slower)

#### 2. Phase-Ablation Experiments
- VEN removal most disruptive during mid-training (epochs 5-25)
- Co-adaptive dependency forms in pyramidal circuit during this phase
- Early and late ablation less disruptive

#### 3. Formal Gradient Analysis
- VENs provide direct gradient pathway immune to Jacobian instabilities
- Recurrent circuits suffer from vanishing/exploding gradient issues
- VENs bypass these instabilities via their specialized connectivity

#### 4. Inference-Time Ablation
- Performance drop ranges from no change (16/20) to catastrophic collapse (0.989→0.620)
- Bimodal outcome mirrors variable social skill presentation in ASC

### Theoretical Contribution
**VENs as Acquisition Scaffolds**:
- Not merely speed-enhancing but essential for reliable convergence
- Developmental absence produces stochastic learning failure
- Computational analogue of variable social skill acquisition in ASC

## Activation Triggers
- Von Economo neurons, VENs, spindle neurons
- Social learning computational modeling
- Spiking neural network architecture design
- bvFTD, autism spectrum computational models
- Gradient pathways in recurrent networks
- Brain-inspired reliable learning
- Organoid/electrophysiology predictions

## Pitfalls
- Binary classification task doesn't directly model social cognition
- K=40 VENs is a simplification of biological VEN populations
- Results from controlled task may not generalize to complex social learning
- Falsifiable predictions require organoid/electrophysiology validation

## Related Skills
- `spiking-neural-network-analysis`: SNN paper analysis
- `neurobiological-craving-signature-social`: Social neuroscience modeling
- `cognitive-flexibility-task-structure`: Neural network models of cognition
- `attractor-metadynamics-neural`: Neural attractor dynamics
