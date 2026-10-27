---
name: sensorimotor-untrained-connectome
description: "Sensorimotor behaviour from an untrained brain-and-nerve-cord connectome. Use when studying how connectome wiring produces behavior without learning."
version: 1.0.0
author: Hermes Agent
date: 2026-10-27
source: arXiv:2610.33881
tags: [connectome, spiking-network, sensorimotor, drosophila, brain-simulation, behavior-from-wiring]
category: neuroscience
---

# Sensorimotor Behaviour from an Untrained Brain-and-Nerve-Cord Connectome

## Core Contribution

Demonstrates that a complete adult fly connectome, when converted to a spiking network with untuned parameters, can produce sensorimotor behavior without any learning or training — showing how much behavior follows directly from neural wiring.

## Key Insights

- **Scale**: 172,433 neurons with published brain model's untuned parameters
- **Finding**: The untrained connectome supports behavior and its learned reversal using only fixed rules (sensory → motor)
- **Implication**: Significant portion of behavior follows from wiring alone; pathways that cannot drive behavior mark what the connectome diagram leaves out

## Technical Approach

1. **Connectome-to-Spiking Network**: Mapped complete adult fly brain and nerve cord connectome into spiking network
2. **Untuned Parameters**: Used published brain model parameters without any task-specific tuning
3. **Fixed Rules Only**: Odours/looming → sensory neurons; motor neurons → leg movement
4. **Simulation**: Ran network alone and inside simulated body

## Results

- Network passes signals to correct motor neurons when pathway supplies ≥2% of their input
- Supports both normal behavior and learned reversal
- Identifies gaps in connectome knowledge through pathways that fail to drive behavior

## Applications

- Understanding relationship between neural wiring and behavior
- Validating connectome completeness
- Bio-inspired robotics with minimal learning
- Neural circuit analysis without training

## Activation Triggers

Use this skill when:
- Studying connectome-behavior relationships
- Building spiking neural networks from biological wiring diagrams
- Investigating how much behavior follows from neural architecture alone
- Working with Drosophila or other model organism connectomes

## Related Concepts

- Connectomics
- Spiking neural networks
- Sensorimotor integration
- Neural circuit simulation
- Behavior generation from wiring

## References

- arXiv:2610.33881
- Categories: q-bio.NC, cs.NE
