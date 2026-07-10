---
name: multi-objective-optimisation-oscillatory-snn
description: Multi-objective genetic algorithm (NSGA-III) optimisation of Izhikevich neuron-based recurrent spiking neural networks for simultaneously matching neural firing rates and network oscillation frequencies. Based on arXiv:2605.25224 (May 2026). Use when studying SNN parameter fitting, neural oscillations, genetic algorithm optimisation for spiking networks, or brain organoid modeling.
---

# Multi-Objective Optimisation with Oscillatory Dynamics in Spontaneous and Decision Spiking Neural Networks

Methodology from arXiv:2605.25224 (May 2026).
Authors: Divyansh Sethi, Muhammad Faraz, KongFatt Wong-Lin
Subjects: q-bio.NC

## Overview

Spiking neural networks (SNNs) can be used for cost-efficient AI computing or mechanistic modeling of neural data. Fitting recurrent SNNs (RSNNs) to neural data remains challenging — especially when simultaneously matching both neural firing rates and network oscillation frequencies, both of which are known to play important roles in neural function.

This work extends the application of **NSGA-III (Non-dominated Sorting Genetic Algorithm III)** to Izhikevich neuron-based RSNNs by optimizing connectivity parameters to target emergent neuronal (sub)population firing rates AND network oscillation frequencies simultaneously.

## Key Contributions

1. **Multi-objective GA for RSNN parameter fitting**: Uses NSGA-III to simultaneously optimize for firing rates and oscillation frequencies
2. **Validation on three regimes**: Spontaneously active RSNN, low-activation brain organoid, and simulated decision-making RSNN
3. **Parameter sensitivity analysis**: Found that dominant oscillation frequencies are more parameter-sensitive than firing rates
4. **Low-activity regime identification**: Identified distinct low-activity regime for decision-making dynamics

## Methodology

### Network Architecture
- Izhikevich neuron model for cortical excitatory and inhibitory neurons
- Recurrent connectivity with spontaneous firing dynamics
- Models comprise spontaneously firing cortical excitatory and inhibitory populations

### Optimization Framework
- **Algorithm**: NSGA-III (multi-objective genetic algorithm)
- **Objectives**: Minimize RMSE between target and emergent:
  - (Sub)population firing rates
  - Dominant network oscillation frequencies
- **Decision variables**: Connectivity parameters of the RSNN
- **Evaluation**: Pareto frontier analysis

### Three Validation Scenarios

| Scenario | Description | Key Finding |
|----------|-------------|-------------|
| Spontaneous RSNN | Simulated spontaneously active RSNN | Both targets can be simultaneously optimized |
| Brain Organoid | Low-activation brain organoid model | Multi-objective optimization applicable to biological systems |
| Decision-Making RSNN | Transient decision dynamics with temporal epochs | Activity patterns in different time epochs successfully fitted |

## Key Findings

1. **Oscillations are more sensitive**: Dominant oscillation frequencies are harder to fit than firing rates, showing higher parameter sensitivity
2. **Firing rates are more robust**: Firing rate targets are more reliably achieved across different parameter settings
3. **Low-activity decision regime**: Identified distinct low-activity dynamical regime in decision-making networks
4. **Pareto frontier trade-offs**: RMSE-based Pareto frontier enables analysis of multi-objective trade-offs

## Practical Implications

- **Neural data fitting**: Provides methodology for fitting RSNNs to experimental neural recordings with both rate and oscillation constraints
- **Brain organoid modeling**: Demonstrates applicability to biological neural systems ex vivo
- **Neuromorphic computing**: Multi-objective optimization could improve SNN-based AI systems
- **Clinical applications**: Understanding parameter sensitivity can inform brain disorder modeling

## Activation Keywords
- spiking neural network, NSGA-III, multi-objective optimization
- neural oscillations, Izhikevich neuron, recurrent SNN
- brain organoid, neural data fitting, Pareto frontier
- firing rate optimization, oscillation frequency, decision-making dynamics
