---
name: evolutionary-snn-classifier
description: "Evolutionary feature selection for spiking neural network pattern classifiers using the biologically realistic JASTAP model. Combines evolutionary algorithms with SNN training for simultaneous architecture and feature optimization."
---

# Evolutionary SNN Classifier with JASTAP

Research methodology from paper "Evolutionary feature selection for spiking neural network pattern classifiers" (2026-04-29).

## Core Approach
Applies **evolutionary feature selection** to the **JASTAP** (biologically realistic spiking neural network model) for pattern classification tasks.

## JASTAP Neural Network Model
- Biologically realistic alternative to standard multi-layer perceptrons
- Incorporates spiking neuron dynamics
- More faithful to biological neural computation than traditional ANNs

## Evolutionary Procedure
The paper applies an evolutionary procedure for:
1. **Simultaneous feature selection** - identifying optimal input feature subsets
2. **Architecture optimization** - finding optimal network configurations
3. **Parameter tuning** - optimizing synaptic weights and neuron parameters

## Key Benefits
- Reduces input dimensionality automatically
- Finds biologically plausible network architectures
- Avoids manual feature engineering
- Jointly optimizes features and network structure

## When to Use
- Classification tasks with high-dimensional input
- Need for biologically plausible neural models
- Scenarios where feature selection is critical
- Applications requiring interpretable feature importance

## Workflow

```
1. Define feature space and JASTAP network architecture
2. Initialize evolutionary population (feature subsets + network configs)
3. Evaluate fitness (classification accuracy + model complexity)
4. Apply selection, crossover, mutation
5. Iterate until convergence
6. Deploy best individual's feature subset + network
```

## Related Skills
- `spiking-neural-network-analysis`
- `bio-neuron-snn-learning`
- `multi-plasticity-snn-training`

## Paper Reference
- **arXiv:** 2604.26654
- **Authors:** Michal Valko, Nuno C. Marques, Marco Castelani
- **Date:** 2026-04-29
- **Categories:** cs.NE