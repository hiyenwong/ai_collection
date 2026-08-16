---
name: exact-first-passage-time-response-theory
title: Exact First-Passage Time Response Theory
description: Use for MFPT response analysis in neural dynamics.
trigger_words:
  - first-passage time
  - MFPT response
  - steady-state response
  - Markov processes neuroscience
---

# Exact First-Passage Time Response Theory from Steady-State Response

## Overview
This skill provides a compact theoretical framework for linear and nonlinear mean first-passage time (MFPT) response in continuous-time Markov processes, with applications to neural dynamics, spiking neurons, and biological systems.

## Core Methodology

### Exact Correspondence Framework
- **Transient-to-Steady Mapping**: Maps intrinsically transient MFPT response onto steady-state response of auxiliary system
- **Universal Response Relations**: Yields exact response relations for MFPTs between arbitrary state pairs
- **Factorized Decomposition**: Physical decomposition into linear upstream, linear downstream, and nonlinear contributions
- **Mathematical Foundation**: Expressed entirely in terms of unperturbed MFPTs and steady-state probabilities

### Key Applications
1. **Neural Dynamics**: Analyze response of spiking neuron timing to perturbations
2. **Biological Systems**: Understand transport, reaction, search, and switching processes
3. **Prediction and Control**: Systematic theory for predicting how MFPTs respond to changes
4. **Computational Advantages**: Efficient calculation of both MFPTs and steady-state distributions

## Implementation Guidelines

### Analysis Framework
1. Identify the Markov process representing your neural or biological system
2. Determine unperturbed MFPTs and steady-state probabilities
3. Apply the exact correspondence to map transient response to steady-state auxiliary system
4. Use factorized decomposition to understand upstream/downstream/nonlinear contributions

### Practical Applications
- **Neuron Modeling**: Predict how synaptic perturbations affect spike timing
- **Network Dynamics**: Analyze response of neural network switching times to external inputs
- **Biological Transport**: Model molecular transport processes in neurons
- **Control Theory**: Design interventions to control timing in biological systems

## Key Benefits
- **Exact Results**: Provides exact rather than approximate response relations
- **Universal Applicability**: Works for arbitrary state pairs in Markov processes
- **Physical Interpretability**: Factorized decomposition provides clear mechanistic insights
- **Computational Efficiency**: Offers advantages in calculating MFPTs and steady-state distributions
- **Theoretical Foundation**: Resolves paradoxes and provides fundamental bounds on responses

## Advanced Features
- **Response-Curve Inference**: Rules for inferring complete response curves from limited data
- **Higher-Order Responses**: Analytical expressions for higher-order MFPT responses
- **Multi-Rate Formulas**: Handles systems with multiple time scales
- **Fundamental Bounds**: Provides theoretical limits on possible MFPT responses

## References
- Bao, R., & Liang, S. (2026). Exact First-Passage Time Response Theory from Steady-State Response. arXiv:2608.11202
- Companion paper: arXiv:2608.06368

## Activation Conditions
Use this skill when:
- Analyzing how perturbations affect timing in neural or biological systems
- Studying spiking neuron response to synaptic inputs
- Modeling transport, reaction, or switching processes in biological contexts
- Needing exact rather than approximate response relations for Markov processes
- Working with first-passage time problems in computational neuroscience