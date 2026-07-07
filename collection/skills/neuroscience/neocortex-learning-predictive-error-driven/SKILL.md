---
name: neocortex-learning-predictive-error-driven
description: "Neocortex learning framework via error-driven predictive learning using temporal derivatives, corticothalamic circuits, and competitive kinase synaptic plasticity. Implemented in Axon spiking neural simulation framework. Activation: neocortex learning, predictive coding, error-driven learning, temporal derivatives, corticothalamic circuits, kinase plasticity, spiking neurons, Axon framework, competitive learning"
metadata:
  arxiv_id: "2606.08720"
  submitted: "2026-06-07"
  authors: "Randall C. O'Reilly"
  tags: [neuroscience, neocortex, learning, predictive-coding, spiking-neural-network, synaptic-plasticity, thalamus, computational-neuroscience]
license: Complete terms in LICENSE.txt
---

# Neocortex Learning via Predictive Error-Driven Temporal Derivatives

## Context

A sufficient account of how the neocortex learns must meet three criteria: computational (powerful general-purpose learning algorithm), algorithmic (implementable with known neural circuits), and implementational (detailed neurochemical account). Error-driven predictive learning via temporal derivatives, driven by corticothalamic circuits and competitive kinase synaptic plasticity, is the only framework meeting all three criteria.

## Core Methodology

### Three-Criterion Framework

1. **Computational Criterion**: Must approximate a powerful, general-purpose learning algorithm known to scale to human-level intelligence
2. **Algorithmic Criterion**: Must be implementable using known, well-established neural circuits within neocortex and associated brain structures
3. **Implementation Criterion**: Must provide detailed account of how all algorithmic mechanisms function at neurochemical level

### Error-Driven Predictive Learning

1. **Temporal Derivative Mechanism**: Learning driven by temporal differences in predictions vs outcomes
2. **Predictive Coding**: Cortex generates predictions about incoming inputs
3. **Error Signal Generation**: Mismatch between predictions and actual inputs produces error signals
4. **Synaptic Plasticity Induction**: Errors drive synaptic weight updates via competitive kinase mechanisms

### Corticothalamic Circuit Architecture

1. **Thalamic Relay**: Thalamus acts as relay station for sensory inputs
2. **Cortical Feedback**: Cortex sends predictive feedback to thalamus
3. **Error Detection**: Thalamic circuits detect prediction errors by comparing input vs feedback
4. **Error Propagation**: Errors propagate back to cortex for learning

### Competitive Kinase Plasticity

1. **Kinase Competition**: Multiple kinases compete for synaptic modification control
2. **Timing-Dependent Plasticity**: Plasticity depends on temporal dynamics of error signals
3. **Neurochemical Cascade**: Detailed biochemical pathway from error detection to synapse modification
4. **Stability Mechanism**: Competition ensures stable, non-destructive learning

## Implementation in Axon Framework

### Spiking Neuron Implementation

1. **Axon Framework**: Neural simulation framework using spiking neurons
2. **Biological Realism**: Implements realistic neural dynamics and circuit architecture
3. **Circuit Topology**: Corticothalamic loops with proper connectivity patterns
4. **Temporal Dynamics**: Spike-timing-dependent error signal generation

### Learning Mechanisms

1. **Prediction Generation**: Cortical layers generate spike-based predictions
2. **Error Computation**: Temporal derivative computed from prediction vs actual spikes
3. **Plasticity Application**: Synaptic weights modified based on error signals
4. **Task Learning**: Demonstrated across cognitively motivated tasks

### Verification Approach

1. **Task Performance**: Test learning across challenging cognitive tasks
2. **Circuit Validation**: Verify corticothalamic circuit implementation matches biological data
3. **Plasticity Verification**: Confirm kinase-based plasticity matches neurochemical evidence
4. **Scalability Testing**: Demonstrate generalization across task complexity

## Key Results

- Implemented in Axon framework using spiking neurons
- Demonstrated learning across wide range of cognitively motivated tasks
- Meets all three criteria: computational, algorithmic, implementational
- Provides complete account from algorithm to neurochemistry

## Applications

1. **Computational Neuroscience**: Unified theory of cortical learning
2. **Spiking Neural Networks**: Biologically plausible learning rules for SNNs
3. **Brain-Computer Interfaces**: Understanding cortical plasticity for BCI design
4. **Neuromorphic Computing**: Implementing predictive learning in neuromorphic hardware
5. **Clinical Translation**: Understanding learning deficits in neurological disorders

## Pitfalls

- **Temporal Precision**: Error computation requires precise spike timing — ensure sufficient temporal resolution in simulation
- **Circuit Complexity**: Corticothalamic loops have many subcircuits — validate each component independently
- **Kinase Dynamics**: Multiple kinase cascades — track competition dynamics carefully to avoid instability
- **Prediction Accuracy**: Predictions must be sufficiently accurate to generate useful error signals — tune prediction generation mechanism
- **Stability Trade-off**: Competitive plasticity can suppress learning — balance stability vs plasticity mechanisms

## Verification

1. **Computational Power**: Verify learning algorithm scales to complex tasks (target: human-level performance on standard benchmarks)
2. **Circuit Match**: Compare implemented corticothalamic circuit with biological data (target: >80% topological similarity)
3. **Neurochemical Accuracy**: Validate kinase plasticity mechanisms with experimental data
4. **Task Generalization**: Test across diverse cognitive tasks (pattern recognition, sequence learning, decision making)
5. **Stability Analysis**: Verify learned representations remain stable over time

## Activation Keywords

- neocortex learning
- predictive coding
- error-driven learning
- temporal derivatives
- corticothalamic circuits
- kinase synaptic plasticity
- spiking neurons
- Axon framework
- cortical learning theory
- thalamic feedback
- competitive plasticity