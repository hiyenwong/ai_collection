---
name: single-entity-spiking-neuron-models
category: ai_collection
created: 2026-07-13
arxiv_id: "2607.07429"
description: Comprehensive survey of single-entity spiking neuron models — classification of biologically plausible neural systems including discrete and continuous analogs, membrane potential dynamics, and components affecting neural dynamics for accurate simulation of biological processes.
trigger_words:
  - single-entity spiking neuron
  - spiking neuron models survey
  - biologically plausible neuron models
  - membrane potential dynamics
  - neuron model classification
  - discrete neuron analogs
  - continuous neuron models
  - computational neuron modeling
---

# Single-Entity Spiking Neuron Models: Comprehensive Survey

## Paper Reference

- **Title**: Single-Entity Spiking Neuron Models: Survey
- **Authors**: Leon Parepko, Danila Shulepin, Albert Nasybullin
- **Published**: 2026-07-08
- **arXiv**: [2607.07429](https://arxiv.org/abs/2607.07429)
- **Categories**: cs.NE, q-bio.NC

## Core Concept

A comprehensive survey classifying and characterizing different approaches to mathematical modeling of biologically plausible neural systems. The review covers spiking models alongside discrete and continuous analogs designed to accurately simulate biological processes, including membrane potential dynamics and various components encountered in neural systems.

## Model Classification Framework

The survey organizes neuron models along several dimensions:

### 1. Biophysical Fidelity Axis
- **Detailed biophysical models**: Hodgkin-Huxley, Morris-Lecar, etc.
- **Reduced biophysical models**: Izhikevich, Adaptive Exponential (AdEx), etc.
- **Phenomenological models**: Leaky Integrate-and-Fire (LIF), Spike Response Model (SRM), etc.
- **Abstract/discrete models**: Binary neurons, McCulloch-Pitts, etc.

### 2. Continuity Dimension
- **Continuous models**: Differential equation-based (HH, AdEx, QIF)
- **Discrete models**: Map-based, event-driven, threshold-crossing
- **Hybrid models**: Continuous evolution with discrete spike events (LIF, Izhikevich)

### 3. Component Complexity
- **Single-compartment**: Point neuron models
- **Multi-compartment**: Models including dendritic and axonal compartments
- **Extended components**: Models incorporating astrocyte coupling, synaptic plasticity, ion channels

## Key Model Categories Covered

### Conductance-Based Models
- Hodgkin-Huxley (HH) — gold standard with voltage-gated ion channels
- Morris-Lecar — simplified two-dimensional model
- Wang-Buzsáki — interneuron model with specific ion channel kinetics

### Phenomenological Models
- Leaky Integrate-and-Fire (LIF) — simplest spiking model
- Adaptive Exponential (AdEx) — captures adaptation with exponential spike initiation
- Izhikevich — two-dimensional model capturing 20+ firing patterns
- Quadratic Integrate-and-Fire (QIF) — canonical model for Type I excitability

### Discrete/Map-Based Models
- Rulkov map — fast-slow map reproducing bursting and spiking
- Chialvo map — two-dimensional discrete map
- Izhikevich map — discrete version capturing rich dynamics

### Extended Models
- Models with astrocyte coupling (tripartite synapse)
- Models with short-term plasticity (Tsodyks-Markram)
- Models with adaptation currents
- Models with dendritic compartments

## Selection Criteria for Model Choice

| Use Case | Recommended Model Class |
|----------|------------------------|
| Large-scale network simulation | LIF, Izhikevich, map-based |
| Detailed ion channel dynamics | Hodgkin-Huxley variants |
| Bursting/spiking diversity | Izhikevich, Rulkov map |
| Analytical tractability | QIF, LIF, AdEx |
| Hardware implementation | LIF, discrete models |
| Astrocyte-neuron interaction | Tripartite synapse models |

## Implementation Patterns

### For Large-Scale SNNs
- Use LIF or Izhikevich for computational efficiency
- Consider quantized versions for neuromorphic hardware
- Map-based models for extreme efficiency needs

### For Biophysical Accuracy
- Hodgkin-Huxley for detailed channel dynamics
- AdEx for balance of accuracy and efficiency
- Multi-compartment models when spatial effects matter

### For Analytical Work
- QIF for bifurcation analysis (canonical Type I)
- AdEx for adaptive dynamics analysis
- LIF for closed-form solutions

## Pitfalls

1. **Model-Task Mismatch**: Choosing overly complex models for tasks that don't need biophysical detail wastes computation.
2. **Parameter Sensitivity**: Biophysical models require careful parameter tuning — small changes in channel kinetics can dramatically alter dynamics.
3. **Discretization Artifacts**: Map-based models may miss continuous-time phenomena like subthreshold oscillations.
4. **Validation Gap**: Many models are validated against limited experimental data — always check model assumptions against your use case.

## Applications

- **Spiking neural network design**: Selecting appropriate neuron models for specific tasks
- **Neuromorphic hardware**: Choosing models that match hardware capabilities
- **Computational neuroscience**: Understanding which model captures relevant biological phenomena
- **Brain-inspired AI**: Building more biologically realistic artificial networks

## Related Skills
- `spiking-neural-network-analysis`
- `spiking-neuron-biological-plausibility-assessment`
- `qif-neurons-superior-lif-gradient-descent`
- `sn-learning-survey`