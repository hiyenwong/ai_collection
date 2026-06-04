---
name: vencircuit-ven-gradient-scaffold
description: "VENCircuit methodology — Von Economo neurons as residual gradient scaffolds in recurrent spiking neural networks for reliable social skill acquisition. Use when researching: Von Economo neurons (VENs), spiking neural networks for social cognition, gradient flow in recurrent networks, residual connections in SNN, training convergence stability, autism spectrum conditions (ASC) computational models, frontotemporal dementia (bvFTD) cellular basis. Keywords: Von Economo neurons, spiking neural network, gradient scaffold, social cognition, training stability, residual connections."
---

# VENCircuit: Von Economo Neurons as Gradient Scaffolds in Spiking Neural Networks

## Overview

VENCircuit is a biologically motivated spiking neural network (SNN) architecture that embeds a small population of VEN-like projection neurons (K=40, 2% of total) in a recurrent pyramidal circuit. The methodology demonstrates that VENs function as **acquisition scaffolds** — they are necessary for reliably learning social-like computations, not for performing them after learning.

## Key Findings

1. **21x convergence advantage**: VEN-intact networks converge in 98% of cases vs 70% for VEN-ablated networks (Fisher's exact OR=21.0, p=8.7×10⁻⁵)
2. **Gradient pathway theory**: VENs provide a direct gradient pathway structurally immune to Jacobian product instabilities affecting the recurrent pyramidal circuit
3. **Critical gradient-flow boundary**: All networks initialize near the critical boundary (‖Wpp‖₂ ≈ 0.078, α ≈ 1.028)
4. **Mid-training dependency**: VEN removal most disruptive during epochs 5-25 when co-adaptive dependency forms
5. **Inference-time dispensability**: 80% of networks retain full performance when VENs removed at test time (Wilcoxon p=0.022)

## Core Mechanisms

### VEN-like Neuron Properties
- Feedforward-only input connections
- Direct output projection (bypassing recurrent dynamics)
- Faster time constant than pyramidal neurons
- Thick, myelinated apical dendrites morphology
- Sparse local connectivity with long-range subcortical projections

### Gradient Flow Analysis (Proposition 1 & 2)
- **Proposition 1**: The purely recurrent pathway operates near the vanishing/exploding gradient boundary (α ≈ 1.028 at initialization)
- **Proposition 2**: VEN pathway carries gradient that is O(1) regardless of recurrent weight configuration
- VENs act as structural residual connections preventing gradient attenuation

### Clinical Predictions
1. **Developmental VEN reduction (ASC)**: Impairs reliability of entering the learning process → variable social skill acquisition
2. **Adult VEN loss (bvFTD)**: Primarily affects networks that co-adapted strongly to VEN signals; most acquired representations survive
3. **Timing matters**: Social cognitive consequences of VEN loss depend critically on its developmental timing

## Methodology

### Network Architecture
- Recurrent pyramidal circuit with VEN-like projection neurons
- Burst-modulated Poisson spike statistics as stimulus proxy
- Binary classification task
- 50 matched random initializations with/without VENs

### Experimental Protocol
1. Full-training comparison: intact vs ablated across 50 seeds
2. Phase-ablation: remove VENs at different training epochs
3. Inference-time ablation: remove VENs from trained networks
4. Spectral norm analysis of recurrent weight matrices

## Activation Keywords
- Von Economo neurons
- spiking neural network social cognition
- gradient scaffold SNN
- VENCircuit
- residual connections spiking
- training convergence SNN

## References
- Keskin, E. (2026). Von Economo neurons enable reliable social skill acquisition in recurrent spiking neural networks. arXiv:2605.17399
- He et al. (2016). Deep Residual Learning for Image Recognition
- Allman et al. (2011). The von Economo neurons in frontoinsular and anterior cingulate cortex
