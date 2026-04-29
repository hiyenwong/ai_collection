---
name: developmental-minimal-neural-circuits
description: "Cortical neurogenesis simulation from stem cell to 85 neurons/200K synapses. Developmental rules from mouse transcriptomic data create domain-general topology achieving 90%+ MNIST after one epoch. Activation: neurogenesis, developmental circuits, cortical simulation, structural priors."
---

# Structure as Computation: Developmental Generation of Minimal Neural Circuits

> arXiv:2604.15143 — Duan Zhou

## Metadata
- **Source**: arXiv:2604.15143
- **Authors**: Duan Zhou
- **Published**: 2025-04
- **Relevance**: high
- **URL**: https://arxiv.org/abs/2604.15143

## Core Methodology

### Key Innovation
This work simulates the developmental process of cortical neurogenesis, initiating from a single stem cell and governed by gene regulatory rules derived from mouse single-cell transcriptomic data. The developmental process spontaneously generates a heterogeneous population of 5,000 cells, yet yields only 85 mature neurons - merely 1.7% of the total population. These 85 neurons form a densely interconnected core of 200,400 synapses, corresponding to an average degree of 4,715 per neuron. At itera

### Technical Framework
tion zero, this minimal circuit performs at chance level on MNIST. However, after a single epoch of standard training, accuracy surges to over 90% - a gain exceeding 80 percentage points - with typical runs falling in the 89-94% range depending on developmental stochasticity. The identical circuit, without any architectural modification or data augmentation, achieves 40.53% on CIFAR-10 after one epoch. These findings demonstrate that developmental rules sculpt a domain-general topological substrate exceptionally amenable to rapid learning, suggesting that biological developmental processes inherently encode powerful structural priors for efficient computation.

## Implementation Guide

### Prerequisites
- Python environment with scientific computing libraries
- Access to paper's supplementary materials at https://arxiv.org/abs/2604.15143

### Step-by-Step
1. Read the full paper at https://arxiv.org/abs/2604.15143
2. Identify the core algorithm/framework from the methodology section
3. Implement the key components as described in the paper
4. Validate using the paper's reported benchmarks

## Applications
- Neuroscience research
- Computational neuroscience
- Neural network design and optimization

## Pitfalls
- Results may be preliminary (preprint)
- Reproducibility depends on availability of code/data

## Related Skills
- computational-neuroscience-models
- neural-population-dynamics
- spiking-neural-network-training
