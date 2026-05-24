---
name: spiking-temporal-memory-timing-replay
description: "Spiking Temporal Memory (sTM) model for learning sequence timing and control of replay speed in networks of spiking neurons. Use when: studying temporal sequence learning in spiking neural networks, modeling hippocampal replay, implementing biologically plausible mechanisms for timing-dependent sequence processing, or researching replay speed modulation in neuromorphic systems. Based on Lober et al. (2026, arXiv:2605.22523). Keywords: spiking neural network, temporal memory, sequence timing, replay speed, sTM model, STDP, sequence learning, replay."
---

# Spiking Temporal Memory (sTM) Model for Sequence Timing and Replay

Methodology from paper "Learning sequence timing and control of replay speed in networks of spiking neurons" (Lober, Bouhadjar, Diesmann, Tetzlaff, arXiv:2605.22523, May 2026).

## Overview

The brain processes sequential inputs for sensory perception, language, and motor control. A key challenge is encoding not just the **order** of events but their **precise timing** and **flexible control** of replay speed.

The **Spiking Temporal Memory (sTM)** model is a biologically inspired spiking neural network model that:
1. Learns both the order AND timing of sequence elements
2. Enables flexible control of replay speed without re-training
3. Uses a small set of synchronously firing neurons for each sequence element

## Core Mechanism

### Sequence Representation
- Each sequence element is represented by a small set of neurons firing synchronously
- The set of active neurons encodes the element's identity in its sequential context
- Timing is encoded via synaptic delays and STDP-based weight patterns

### Timing Learning
- Extends the original sTM model (which learned order only) to encode element-specific timing
- Uses spike-timing-dependent plasticity (STDP) to learn temporal relationships
- The temporal structure of sequences emerges from network dynamics

### Replay Speed Control
- Replay (off-line reactivation of learned sequences) is a key function for memory consolidation
- The model demonstrates how replay speed can be flexibly modulated:
  - Via neuromodulatory mechanisms (e.g., acetylcholine, dopamine)
  - Through intrinsic network properties (e.g., adaptation currents)
  - Without requiring re-training or parameter changes

## Key Mechanisms

### Synaptic Delay Learning
- Axonal/dendritic delays are learned to encode precise inter-element timing
- Extends standard STDP to incorporate delay plasticity
- Enables compression or expansion of temporal intervals during replay

### Adaptation-Based Speed Control
- Spike-frequency adaptation (SFA) naturally modulates replay speed
- Slower adaptation → faster replay; faster adaptation → slower replay
- Provides a biologically plausible mechanism for speed control

### Network Architecture
- Recurrent spiking network with structured connectivity
- Sequence-specific neuronal assemblies (cell assemblies)
- Balanced excitation-inhibition for stable dynamics

## Experimental Validation

The model is validated on:
- Learning of precisely-timed sequential patterns
- Variable-speed replay of learned sequences
- Robustness to noise and parameter variations
- Consistency with experimental data on hippocampal replay
- Comparison with experimental data from rodent hippocampus

## Relevance to Neurosciences and AI

- **Neuroscience**: Mechanistic model of hippocampal replay, memory consolidation
- **Neuromorphic computing**: Biologically plausible timing mechanisms for SNNs
- **Sequence learning**: Alternative to transformer-based approaches for temporal processing
- **BCI applications**: Understanding how timing can be decoded from neural signals

## Key Papers and References

- Lober et al. (2026). Learning sequence timing and control of replay speed in networks of spiking neurons. arXiv:2605.22523
- Related: sTM model (Bouhadjar et al.); hippocampal replay literature; STDP sequence learning

## Activation Keywords
- sTM, spiking temporal memory, spike-timing-dependent plasticity, STDP
- sequence timing, replay speed, hippocampal replay, neural sequence learning
- timing-dependent plasticity, spiking neural sequence, replay modulation
