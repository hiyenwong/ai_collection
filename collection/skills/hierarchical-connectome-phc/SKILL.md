---
name: hierarchical-connectome-phc
description: Parallelized Hierarchical Connectome (PHC) framework for spatiotemporal recurrent spiking neural networks. Upgrades State-Space Models (SSMs) into spatiotemporal networks with biological constraints including Dale's Law, short-term plasticity, and reward-modulated STDP. Activation: spiking neural networks, SSM, connectome, spatiotemporal modeling, biological neural networks.
---

# Parallelized Hierarchical Connectome (PHC)

## Overview

This work presents the Parallelized Hierarchical Connectome (PHC), a general framework that upgrades temporal-only State-Space Models (SSMs) into spatiotemporal recurrent networks by mapping SSM components to hierarchical neuronal architectures with biological constraints.

## Paper Reference

- **Title:** Parallelized Hierarchical Connectome: A Spatiotemporal Recurrent Framework for Spiking State-Space Models
- **arXiv ID:** 2604.01295v1
- **Authors:** Po-Han Chiang
- **Published:** 2026-04-01
- **Category:** q-bio.NC (Neurons and Cognition)
- **PDF:** https://arxiv.org/pdf/2604.01295v1

## Core Innovation

PHC maps the diagonal SSM core to a shared **Neuron Layer** and inter-neuronal communication to a shared **Synapse Layer**, where neurons are partitioned into hierarchical regions governed by the connectome topology.

### Key Features

1. **Multi-Transmission Loop**: Enables intra-slice spatial recurrence within each temporal window while preserving O(logT) parallelism
2. **Biological Constraints**: Supports intractable neuro-physical priors including:
   - Adaptive leaky integrate-and-fire (ALIF) dynamics
   - Dale's Law (excitatory/inhibitory neuron separation)
   - Short-term plasticity
   - Reward-modulated spike-timing-dependent plasticity (STDP)

3. **Parameter Efficiency**: Reduces complexity from Θ(D²L) for L-layer stacked architectures to Θ(D²)

## PHCSSM Implementation

PHCSSM is the first model to unify:
- Recurrent spiking neural network dynamics
- Diagonal SSM parallelism
- Five biological constraints
- Learnable lateral connections
- Fully parallelizable training pipeline

## Architecture Components

### Neuron Layer (NL)
Maps diagonal SSM core to hierarchical neuronal regions

### Synapse Layer (SL)  
Inter-neuronal communication with connectome topology

### Multi-Transmission Loop
- Intra-slice spatial recurrence
- Preserves parallel scan efficiency
- Enables lateral/feedback interactions within single timestep

## Biological Constraints Supported

| Constraint | Description |
|------------|-------------|
| ALIF | Adaptive leaky integrate-and-fire dynamics |
| Dale's Law | Excitatory/inhibitory neuron separation |
| STP | Short-term plasticity |
| R-STDP | Reward-modulated spike-timing-dependent plasticity |

## Empirical Results

Evaluated on physiological benchmarks from the UEA multivariate time-series archive:
- Performance: Competitive with state-of-the-art SSMs
- Parameter complexity: Reduced from Θ(D²L) to Θ(D²)
- Training: Fully parallelizable pipeline

## Methodology Applications

Use this framework when:
- Building biologically grounded sequence models
- Implementing spiking neural networks with SSM efficiency
- Researching brain-inspired parameter-efficient architectures
- Studying spatiotemporal dynamics in neural systems

## Trigger Keywords

- spiking neural network
- state-space model
- connectome
- spatiotemporal recurrence
- biological neural network
- Dale's Law
- short-term plasticity
- reward-modulated STDP
- parallel scan
- parameter-efficient SSM
