---
name: pathwise-metastability-galves-locherbach-models
description: "Rigorous mathematical framework for analyzing metastability in stochastic spiking neural networks using the pathwise approach. Reviews Galves-Löcherbach (GL) models, connecting statistical physics to neural dynamics. Covers metastable state transitions, typical trajectory identification, and probability estimation. Use when studying neural state transitions, brain criticality, or applying statistical physics to computational neuroscience."
metadata:
  arxiv_id: "2607.05652"
  published: "2026-07-06"
  authors: "Morgan André, Kádmo Laxa"
  tags: [metastability, stochastic-processes, spiking-neural-network, statistical-physics, Galves-Löcherbach, pathwise-approach, neural-dynamics]
---

# Pathwise Metastability in Galves-Löcherbach Models

## Overview

Comprehensive 48-page review connecting metastability theory from statistical physics to stochastic spiking neural network models. Provides rigorous mathematical framework for understanding how neural systems dwell in apparent equilibrium before rare fluctuations trigger rapid transitions.

## Core Concepts

### Metastability Definition
The tendency of a system to remain for extended periods near an apparently stable equilibrium, until an unlikely perturbation triggers transition to another equilibrium on a much shorter timescale. Perturbation is typically endogenous, creating impression of spontaneous transition.

### Galves-Löcherbach (GL) Models
Stochastic spiking neural network models with:
- **Binary neurons**: Active/inactive states
- **Stochastic dynamics**: Probabilistic spike generation
- **Interaction structure**: Network connectivity determines dynamics
- **Leakage**: Memory decay over time
- **Mean-field variants**: Complete interaction (all-to-all connectivity)

### Pathwise Approach
Mathematical framework for metastability analysis:
1. **Identify typical trajectories**: Characteristic paths of stochastic dynamics
2. **Estimate trajectory probabilities**: Quantify likelihood of different paths
3. **Determine transition timescales**: Metastable dwell time vs transition time
4. **Characterize transition mechanisms**: What triggers state changes

## Historical Context

Theory evolution:
- **Chemistry origins**: Reactive compound transitions
- **Statistical physics**: Phase transitions, nucleation theory
- **Rigorous probability**: Markov processes, large deviations
- **Neural applications**: GL models, brain metastability

## Key Results

### Mean-Field Settings
All current metastability results for GL models obtained in:
- Mean-field (complete interaction)
- Perfectly symmetric networks
- No spatial/topological structure
- Exception: 1D lattice results (binary neurons, total leakage)

### Open Problems

1. **Beyond mean-field**: Generalize to realistic network structures
   - d-dimensional lattices (biologically relevant: cerebellar cortex)
   - Trees, power-law graphs, Erdős-Rényi networks
   - Spatial structure effects on metastability

2. **Realistic GL variants**: Extend to more biologically plausible models
   - Continuous neuron states
   - Heterogeneous interactions
   - Time-varying connectivity

3. **Rigorous proofs**: Establish metastability for general cases
   - Adapt interacting particle systems techniques
   - Handle spatial structure mathematically

## Methodology

### Pathwise Analysis Steps

1. **Define metastable states**: Identify apparent equilibria
2. **Characterize typical paths**: Most probable trajectories within states
3. **Compute transition probabilities**: Large deviation estimates
4. **Estimate dwell times**: Expected time in metastable state
5. **Identify transition mechanisms**: Critical fluctuations, nucleation events

### Mathematical Tools

- **Large deviation theory**: Rare event probabilities
- **Markov process theory**: Stochastic dynamics
- **Interacting particle systems**: Network effects
- **Statistical mechanics**: Ensemble methods

## Applications to Neuroscience

### Brain Metastability
- **Neural state transitions**: Resting state → task state
- **Criticality**: Brain operating near phase transitions
- **Cognitive flexibility**: Rapid switching between mental states
- **Consciousness**: Global workspace transitions

### Predictions
- Metastable dwell times follow exponential distributions
- Transition timescales much shorter than dwell times
- Network structure affects metastability properties
- Biological networks may exploit metastability for computation

## Connections to Other Frameworks

### Critical Brain Hypothesis
Metastability relates to criticality:
- Critical systems exhibit scale-free dynamics
- Metastable states near critical points
- Phase transitions in neural activity

### Attractor Networks
- Metastable states as attractors
- Transition mechanisms between attractors
- Noise-induced switching

### Predictive Coding
- Metastable states as predictions
- Transitions as prediction errors
- Hierarchical metastability

## Key Insights

1. **Endogenous transitions**: System generates its own perturbations
2. **Timescale separation**: Long dwell, short transition
3. **Network structure matters**: Connectivity determines metastability
4. **Biological relevance**: Brain may exploit metastable dynamics
5. **Computational advantages**: Flexible state switching, memory, decision-making

## Activation Keywords

metastability, Galves-Löcherbach, stochastic neural networks, pathwise approach, statistical physics, phase transitions, neural dynamics, criticality, attractor networks, brain states
