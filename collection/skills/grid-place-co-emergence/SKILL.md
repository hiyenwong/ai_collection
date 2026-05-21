---
name: grid-place-co-emergence
description: "Co-emergence of grid and place fields methodology — unified recurrent network model showing grid and place cells emerge simultaneously from a single sensory-prediction objective. Use when: (1) modeling hippocampal-entorhinal spatial representations, (2) studying grid cell emergence from path integration, (3) studying place cell emergence from sensory encoding, (4) implementing RNNs with Dale's Law for spatial navigation, (5) generating experimentally testable predictions about spatial codes in MEC and hippocampus. Keywords: grid cells, place cells, co-emergence, hippocampal-entorhinal circuit, spatial navigation, recurrent neural network, Dale's Law, path integration, sensory prediction."
---
# A Simple Model of Co-Emergence of Grid and Place Fields

Methodology from arXiv:2605.21356 (May 2026). Authors: Zhaoze Wang, Genela Morris, Dori Derdikman, Pratik Chaudhari, Vijay Balasubramanian.

## Core Idea

Grid cells (MEC) and place cells (hippocampus) together support spatial navigation, but there is a chicken-and-egg problem for how both arise and reinforce each other. This paper presents the **first single-objective unified recurrent network model** where grid and place cells **co-emerge without supervision** of either type, or reliance on pre-existing spatial-cell representations.

## Key Results

1. **Unified model**: Single recurrent network with Dale's Law (every neuron is excitatory or inhibitory) trained to predict next sensory observation from masked previous observations + egocentric motion.

2. **Co-emergence**: Both grid and place cells coexist across 1,000+ different training configurations — the balance set by sensory noise and masking levels.

3. **Experimental validation**: Without retraining, the network reproduces:
   - Grid fragmentation in hairpin mazes
   - Grid merging after wall removal
   - Lattice alignment across connected rooms
   - Locally ordered 3D fields (freely flying bats)
   - Developmental order: place cells precede grid cells

## Method Details

### Network Architecture
- Recurrent neural network with Dale's Law (each neuron strictly excitatory or inhibitory)
- Input: masked sensory observations + egocentric motion
- Output: predict next sensory observation
- Single objective (no auxiliary losses)

### Two Complementary Encoding Pressures
1. **Reconstruction pressure**: Correcting errors or reconstructing missing components of sensory observations → drives **place-like** representations
2. **Prediction pressure**: Predicting the next sensory state during navigation → drives **grid-like** representations

### Training
- 1,000+ different training configurations tested
- Balance of grid vs. place cells controlled by amount of sensory noise and masking
- No spatial cell supervision at any point

## Key Findings

- Grid and place cells arise from a **single sensory prediction objective** — no need for separate modules
- The two encoding pressures (sensory reconstruction vs. navigation prediction) naturally produce different spatial codes
- Experimentally testable predictions: manipulating sensory noise should shift the balance between grid and place representations
- Suggests a circuit-level account where hippocampal-entorhinal interactions arise from a unified computational goal

## Activation
- grid cells, place cells, spatial navigation, hippocampal-entorhinal, co-emergence, path integration, sensory prediction, Dale's Law, recurrent neural network
