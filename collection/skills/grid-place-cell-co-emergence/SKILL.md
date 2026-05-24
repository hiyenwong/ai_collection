---
name: grid-place-co-emergence
description: "First unified recurrent network model implementing Dale's Law (every neuron is either excitatory or inhibitory) that trains via masked next-observation prediction to co-emerge both grid and place cells from a single architecture. Use when researching: grid cell emergence, place cell models, entorhinal-hippocampal circuits, spatial navigation neural networks, Dale's Law in computational models, co-emergence of spatial representations, MEC-HPC reciprocal connectivity, developmental spatial cognition."
---

# A Simple Model of Co-emergence of Grid and Place Fields

## Overview

Grid cells in the medial entorhinal cortex (MEC) and place cells in the hippocampus (HPC) together support spatial navigation. The two regions are reciprocally connected, creating a **chicken-and-egg problem**: how do both arise and reinforce each other during development? Current computational accounts either derive one type from the other or model emergence in isolation.

This paper introduces the **first unified recurrent network model** that:
1. Instantiates **Dale's Law** (each neuron is either exclusively excitatory or exclusively inhibitory)
2. Is trained to predict the **next sensory observation** from masked observations
3. **Co-emerges** both grid-like and place-like spatial representations within a single network

## Key Findings

1. **Co-emergence**: Grid and place fields emerge simultaneously, not sequentially — one does not cause the other
2. **Dale's Law compatibility**: The model respects biological Dale's Law while still producing both cell types
3. **Self-supervised learning**: Trained via masked next-observation prediction (no explicit spatial labels)
4. **Grid-like patterns**: Regular hexagonal firing patterns emerge in model units resembling MEC grid cells
5. **Place-like patterns**: Localized spatial firing fields emerge resembling hippocampal place cells
6. **Mutual reinforcement**: The two cell types mutually reinforce each other through the reciprocal architecture

## Core Mechanisms

### Unified Recurrent Architecture
- Single recurrent neural network with Dale's Law constraints
- Excitatory and inhibitory populations with biologically realistic connectivity
- Trained end-to-end via self-supervised prediction objective

### Training Objective
- **Masked next-observation prediction**: Given partial sensory observations, predict the next observation
- No explicit spatial supervision (no coordinates, no place labels)
- Forces the network to develop internal spatial representations to solve the task

### Emergent Properties
- **Grid cells**: Neurons with periodic, hexagonal spatial firing fields
- **Place cells**: Neurons with localized, single-peak spatial firing fields
- Both emerge from the same training objective without architectural specialization

## Methodology

### Model Architecture
- Recurrent neural network with Dale's Law constraints
- Excitatory/inhibitory balanced network dynamics
- Sensory input → recurrent processing → prediction output

### Training
- Self-supervised on spatial navigation trajectories
- Masked prediction objective
- No spatial label supervision

### Evaluation Metrics
- Spatial information content
- Gridness score (hexagonal regularity measure)
- Place field size and number of fields
- Spatial correlation between model units and biological recordings

## Significance

### For Neuroscience
- Resolves the chicken-and-egg problem: grid and place cells co-emerge through reciprocal connectivity
- Shows Dale's Law is compatible with complex spatial representations
- Provides a unified learning framework for entorhinal-hippocampal development
- Predicts that grid cells can arise without path integration (contra some theories)

### For AI / Machine Learning
- Demonstrates self-supervised spatial representation learning without explicit spatial labels
- Shows that biological constraints (Dale's Law) are compatible with complex emergent representations
- Provides a blueprint for biologically inspired spatial navigation in artificial agents
- Suggests masked prediction as a general principle for representation learning

## Activation Keywords
- grid cell co-emergence
- place cell model
- Dale's Law neural networks
- entorhinal-hippocampal circuit
- spatial navigation self-supervised learning
- grid cell emergence from prediction
- MEC-HPC unified model
- spatial representation learning

## References
- Wang, Z., Morris, G., Derdikman, D., Chaudhari, P., & Balasubramanian, V. (2026). A Simple Model of Co-emergence of Grid and Place Fields. arXiv:2605.21356
- Hafting et al. (2005). Microstructure of a spatial map in the entorhinal cortex
- O'Keefe & Dostrovsky (1971). The hippocampus as a spatial map
- Moser, Moser & Roudi (2014). Neural representations of space
- Cueva & Wei (2018). Emergence of grid-like representations by training recurrent networks
- Banino et al. (2018). Vector-based navigation using grid-like representations in artificial agents
