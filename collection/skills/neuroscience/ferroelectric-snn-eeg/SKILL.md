---
name: ferroelectric-snn-eeg
description: >
  Personalized Spiking Neural Networks with Ferroelectric Synapses for EEG Signal Processing.
  Covers deployment of SNNs on ferroelectric memristive hardware for adaptive EEG-based
  motor imagery decoding, mixed-precision training with device-aware updates, and
  subject-specific transfer learning on neuromorphic platforms.
  Use when working with: ferroelectric synapses, memristive SNN deployment,
  EEG-based BCI personalization, neuromorphic hardware constraints,
  mixed-precision spiking training, or device-aware weight updates.
  Activation: ferroelectric SNN, memristive EEG, neuromorphic BCI,
  ferroelectric synapse, personalized SNN, device-aware training,
  EEG motor imagery, hardware-constrained SNN
---

# Ferroelectric SNN for EEG Signal Processing

Based on arXiv:2601.00020 (Garg et al., May 2026).

## Paper Overview

**Title:** Personalized Spiking Neural Networks with Ferroelectric Synapses for EEG Signal Processing

**Authors:** Nikhil Garg, Anxiong Song, Niklas Plessnig, Nathan Savoia, Laura Bégon-Lours

**Published:** Submitted Dec 2025, revised May 6, 2026 (v3)

**DOI:** 10.1063/5.0319912

**Categories:** cs.NE, cs.AI, cs.ET, cs.LG, eess.SY

## Core Problem

EEG-based BCIs suffer from non-stationary neural signals varying across sessions and individuals,
limiting subject-agnostic model generalization. Programmable memristive hardware enables
post-deployment adaptation but faces challenges: limited weight resolution, device variability,
nonlinear programming dynamics, and finite device endurance.

## Key Contributions

### 1. Ferroelectric Memristive Synapses for SNN

- Fabricated and characterized ferroelectric synapses for spiking neural network deployment
- Modeled weight update dynamics under realistic device constraints
- Demonstrated SNN deployment on ferroelectric memristive synaptic arrays

### 2. Mixed-Precision Training Strategy

- Gradient-based updates accumulated digitally
- Converted to discrete programming events only when threshold exceeded
- Device-aware weight updates accounting for nonlinear, state-dependent programming dynamics
- Mitigates endurance and energy constraints during learning/adaptation

### 3. Subject-Specific Transfer Learning

- Software-trained weights transferred to hardware
- Low-overhead on-device re-tuning of final network layers only
- Achieves classification performance comparable to software-based SNNs
- Enables personalized neuromorphic processing of neural signals

## Architecture

```
Convolutional-Recurrent SNN
├── Convolutional layers (feature extraction from EEG)
├── Recurrent layers (temporal dynamics)
└── Ferroelectric memristive synapses (hardware deployment)
    ├── Mixed-precision accumulation (digital)
    └── Threshold-based programming events (analog)
```

## Device-Aware Training Algorithm

1. Compute gradients digitally (high precision)
2. Accumulate weight updates in digital memory
3. When accumulated update exceeds threshold:
   - Map to discrete programming events
   - Account for nonlinear, state-dependent device dynamics
   - Apply to ferroelectric synapses
4. Repeat for adaptation phase

## Transfer Learning Pipeline

1. Train SNN in software on population data
2. Transfer weights to ferroelectric hardware
3. Retrain only final layers with subject-specific data
4. Achieve personalized model with minimal hardware overhead

## Key Insights

- Ferroelectric hardware supports robust low-overhead adaptation
- Mixed-precision strategy bridges software-hardware performance gap
- Subject-specific transfer learning outperforms subject-agnostic models
- Device-aware training mitigates endurance constraints
- Classification accuracy comparable to software SNNs despite hardware constraints

## Activation Keywords

- ferroelectric SNN
- memristive EEG processing
- neuromorphic BCI
- personalized spiking networks
- device-aware training
- mixed-precision SNN
- ferroelectric synapse
- EEG motor imagery decoding
- hardware-constrained neural networks
- neuromorphic adaptation

## Related Skills

- spiking-neural-network-analysis
- eeg-brain-connectivity-bci
- snn-learning-survey
- snn-performance-analysis
