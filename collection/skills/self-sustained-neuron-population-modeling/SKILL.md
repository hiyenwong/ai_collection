---
name: self-sustained-neuron-population-modeling
description: "Modeling autonomous spiking activity in recurrent Hodgkin-Huxley networks with STDP and intrinsic stochasticity, demonstrating long-duration self-sustained firing after brief initialization"
version: "0.1.0"
arxiv: "2604.13719v1"
paper_title: "Modeling of Self-sustained Neuron Population without External Stimulus"
tags:
  - hodgkin-huxley
  - self-sustained-activity
  - stdp
  - stochastic-synapses
  - neural-dynamics
  - recurrent-networks
  - autonomous-activity
---

# Self-Sustained Neuron Population Modeling

## Overview

This work studies whether a **recurrent network of Hodgkin-Huxley neurons** with STDP and intrinsic stochasticity can maintain autonomous activity after brief transient stimulation — a fundamental feature of nervous system dynamics that remains incompletely understood.

## Key Principles

### Network Architecture

- **200 neurons**: 160 excitatory, 40 inhibitory (4:1 E/I ratio)
- **80% connection probability**: Dense recurrent connectivity
- Both **excitatory and inhibitory STDP** for synaptic plasticity
- **Probabilistic vesicle release**: Stochastic neurotransmitter dynamics
- **Probabilistic synapse formation**: Variable connectivity
- **Receptor variability**: Heterogeneous synaptic responses
- **Voltage-dependent inhibition**: Non-linear inhibitory gating

### Simulation Protocol

1. Brief **200 ms initialization stimulus** applied to 30 excitatory neurons
2. **No further external input** after initialization
3. Network maintains sparse, irregular activity autonomously

### Key Results

- In an **1800 s simulation**, 67% of neurons had mean firing rates **below 1 Hz**
- Population mean firing rate: **1.13 ± 1.34 Hz**
- Participation increased across longer observation windows
- Population-mean **Fano factors near 1–2**, consistent with irregular spike timing
- Spontaneous qualitative reorganizations in collective firing patterns over time
- Results replicated in two additional **500 s simulations**

## Implementation Guidance

1. Build a recurrent Hodgkin-Huxley network with 80/20 E/I split and 80% connectivity
2. Implement both excitatory and inhibitory STDP rules
3. Add stochasticity: probabilistic vesicle release, variable synapse formation, receptor variability
4. Apply voltage-dependent inhibition for non-linear gating
5. Initialize with a brief stimulus pulse, then run with zero external input
6. Monitor firing rates, Fano factors, and population-level pattern reorganizations

## References

See `references/implementation.md` for code patterns and implementation details.
