---
name: grid-place-co-emergence
description: "A unified recurrent network model instantiating Dale's Law where grid cells and place cells co-emerge from a single sensory-prediction objective without supervision of either type — the first such model to explain co-emergence, grid fragmentation, wall removal merging, and developmental ordering."
tags: [grid-cells, place-cells, hippocampus, entorhinal-cortex, spatial-navigation, computational-neuroscience, dales-law]
---

# A Simple Model of Co-Emergence of Grid and Place Fields

**arXiv:2605.21356** | Submitted: 20 May 2026

**Authors:** Zhaoze Wang, Genela Morris, Dori Derdikman, Pratik Chaudhari, Vijay Balasubramanian

## Summary

Grid cells in the medial entorhinal cortex and place cells in the hippocampus together support spatial navigation. The two regions are reciprocally connected, and there is a **chicken-and-egg problem** for how both arise and reinforce each other during development. Current computational accounts either derive one type from the other or use network dynamics to model the emergence of one type in isolation.

This paper introduces a **unified recurrent network model** that instantiates **Dale's Law** (every neuron is either excitatory or inhibitory), and is trained to predict the next sensory observation from masked previous sensory observations and egocentric motion.

## Key Contributions

1. **First Single-Objective Model**: To the authors' knowledge, this is the first model in which grid and place cells co-emerge from a single training objective without supervision of either type, or reliance on pre-existing spatial-cell representations.

2. **Dale's Law Implementation**: The network respects biological Dale's Law (each neuron is either excitatory or inhibitory), making it more biologically realistic.

3. **Robust Co-Emergence**: Grid and place cell spatial codes coexist across 1,000 different training configurations, with their balance set by the amount of sensory noise and masking.

4. **Reproduces Multiple Experimental Phenomena** (without retraining):
   - Grid fragmentation in hairpin mazes
   - Grid merging after wall removal
   - Lattice alignment across connected rooms
   - Locally ordered 3D fields in freely flying bats
   - Developmental order: place cells precede grid cells

## Methodological Framework

- **Architecture**: Recurrent neural network with Dale's Law constraints
  - Excitatory and inhibitory neuron populations
  - Reciprocal connections between MEC (grid-like) and HC (place-like) regions
- **Training Objective**: Predict next sensory observation from:
  - Masked previous sensory observations
  - Egocentric motion signals
- **Key Parameters**:
  - Sensory noise level → balance between grid vs. place codes
  - Masking ratio → spatial code type
- **Theoretical Interpretation**: Two complementary encoding pressures:
  1. **Reconstruction pressure**: Correcting errors or reconstructing missing components of sensory observations
  2. **Prediction pressure**: Predicting the next sensory state during navigation

## Relation to Experimental Neuroscience

- Offers a circuit-level account of how grid and place cells co-develop
- Predicts that the balance of grid vs. place codes is modulated by sensory reliability
- Explains developmental ordering (place cells before grid cells) through computational principles
- Reproduces diverse experimental perturbations without parameter retuning

## Potential Applications

- Biologically-inspired navigation systems for robotics
- Understanding hippocampal-entorhinal development
- Predictive coding models of spatial cognition
- Neural network models with Dale's Law constraints

## Activation Keywords

- grid-cells, place-cells, co-emergence, spatial-navigation, dales-law, recurrent-network, sensory-prediction, hippocampal-entorhinal

## References

- arXiv:2605.21356 [q-bio.NC]
