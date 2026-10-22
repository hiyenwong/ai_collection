---
name: bio-inspired-auditory-snn
description: "Bio-Inspired Auditory Processing: coupling parallel resonate-and-fire dynamics with ternary recurrent networks for speech recognition using SNNs."
paper_id: 2610.29720
utility_score: 0.79
categories: [cs.SD, cs.AI, cs.NE, eess.AS]
date: 2026-10-21
tags: [spiking-neural-networks, auditory-processing, speech-recognition, bio-inspired, resonate-and-fire]
---

# Bio-Inspired Auditory Processing: Coupling Parallel Resonate-and-Fire Dynamics with Ternary Recurrent Networks for Speech Recognition

## Key Contribution
Addresses the bottleneck in Spiking Neural Networks (SNNs) for automatic speech recognition (ASR): the Leaky Integrate-and-Fire (LIF) neuron's membrane decay erases information across pauses and phonetic boundaries. Proposes coupling parallel Resonate-and-Fire (RF) dynamics with Ternary Recurrent Networks.

## Core Method
- **Problem**: LIF neurons in SNNs lose information during pauses (between phonemes/words) due to membrane decay. This makes SNNs struggle with continuous, context-dependent tasks like ASR.
- **Solution**: 
  - **Resonate-and-Fire (RF) neurons**: Oscillatory dynamics that maintain state across pauses (unlike LIF decay)
  - **Parallel processing**: Multiple RF populations process different frequency bands in parallel (mimicking cochlear processing)
  - **Ternary Recurrent Networks**: {-1, 0, +1} weights for efficient computation + sparse connectivity
  - **Coupling**: RF outputs feed into ternary recurrent network for temporal integration and classification
- **Bio-inspiration**: Mimics auditory pathway (cochlea → brainstem → cortex) with spiking dynamics at each stage

## Why It Matters
- First SNN architecture that handles continuous speech without information loss at pauses
- Energy-efficient: spiking computation + ternary weights = low power
- Bio-plausible: matches known auditory processing mechanisms
- Competitive with non-spiking architectures on ASR benchmarks while maintaining energy efficiency
- Opens door for SNNs in other continuous sequence tasks (not just audio)

## Application Scenarios
- Energy-efficient speech recognition on edge devices
- Neuromorphic hardware deployment (Loihi, TrueNorth, etc.)
- Bio-inspired audio processing for hearing aids, cochlear implants
- Any continuous sequence task where pauses shouldn't erase state

## Implementation Notes
- RF neurons: complex-valued state (amplitude + phase) vs. LIF's real-valued membrane potential
- Parallel frequency bands: typically 40-80 channels (matching cochlear filter bank)
- Ternary weights: {-1, 0, +1} enable bit-shift computation (no multiplication)
- Training: surrogate gradient methods (SNNs are non-differentiable at spike threshold)
- Key hyperparameters: RF resonance frequency, ternary sparsity ratio, recurrent time constant
