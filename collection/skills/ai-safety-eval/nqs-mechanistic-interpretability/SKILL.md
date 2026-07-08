---
name: nqs-mechanistic-interpretability
description: Apply sparse autoencoders to analyze internal representations of neural quantum states and steer quantum properties.
trigger_keywords: ["nqs interpretability", "neural quantum states analysis", "sparse autoencoder quantum", "feature steering NQS", "mechanistic interpretability quantum"]
---

# NQS Mechanistic Interpretability

## Description

Methodology from arXiv:2607.01336 that applies sparse autoencoders (SAEs) to analyze the internal activations of Neural Quantum States. Despite being trained only on variational objectives, NQS learn interpretable physical concepts including spin correlations, symmetries, and topological order. Causal feature steering enables controlled manipulation of learned quantum properties.

## Core Methodology

1. **Feature Extraction**: Train sparse autoencoders on NQS residual stream activations to extract interpretable features
2. **Concept Identification**: Map extracted features to physical concepts (spin correlations, symmetries, topological order)
3. **Causal Steering**: Intervene on specific feature dimensions to manipulate quantum properties controllably
4. **Physical Grounding**: Verify that learned features correspond to actual physical observables

## Key Patterns

- **Residual Stream Analysis**: Extract features from intermediate layers of the NQS architecture
- **Sparse Decomposition**: Use SAEs to decompose dense activations into sparse, interpretable feature vectors
- **Feature-Concept Mapping**: Correlate individual SAE features with known physical quantities (magnetization, correlation functions, topological invariants)
- **Causal Intervention**: Zero-out, amplify, or swap specific features to test their causal role in quantum property prediction

## Applications

- Understanding what NQS actually learn about quantum systems
- Debugging and improving variational ansätze design
- Discovering emergent physical concepts from neural representations
- Guiding architecture design based on interpretability insights

## Activation

Use when: analyzing what neural quantum states learn, applying mechanistic interpretability to physics models, extracting physical concepts from neural activations, steering quantum model behavior.

**Keywords**: sparse autoencoders, mechanistic interpretability, neural quantum states, feature steering, physical concepts, residual stream, topological order, spin correlations
