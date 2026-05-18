---
name: neat-nc-navigation-cells
description: "NEAT-NC: NEAT-guided navigation cells for robot path planning. Combines hippocampal-inspired spatial cognitive cells (place cells, grid cells, head direction cells, border cells, speed cells) with NeuroEvolution of Augmenting Topologies (NEAT) for adaptive robot navigation in static and dynamic environments. Activation: navigation cells, NEAT, robot path planning, hippocampus-inspired, spatial cognition, dynamic environments."
category: neuroscience
tags: [navigation-cells, NEAT, robot-navigation, path-planning, hippocampus, spatial-cognition, evolutionary-algorithms]
trigger_keywords: [navigation cells, NEAT, robot path planning, place cells, grid cells, spatial cognition, hippocampus-inspired navigation]
related_papers:
  - title: "NEAT-NC: NEAT guided Navigation Cells for Robot Path Planning"
    authors: Hibatallah Meliani, Khadija Slimani, Samira Khoulji
    arxiv_id: "2604.15076"
    published: "2026-04-18"
---

# NEAT-NC: NEAT-Guided Navigation Cells for Robot Path Planning

Bio-inspired robot navigation combining hippocampal spatial cognitive cells with NeuroEvolution of Augmenting Topologies (NEAT) for adaptive path planning in static and dynamic environments.

## Overview

The brain constructs internal spatial representations using specialized cell types: place cells, grid cells, head direction cells, border cells, and speed cells. NEAT-NC translates these biological principles into an evolutionary navigation system where navigation cells serve as sensory inputs to NEAT-evolved recurrent neural networks, representing the hippocampal navigation system.

## Core Biological Inspiration

### Spatial Cognitive Cells
- **Place cells**: Fire at specific locations in the environment
- **Grid cells**: Fire in hexagonal grid patterns across space
- **Head direction cells**: Encode orientation relative to environment
- **Border cells**: Activate near environmental boundaries
- **Speed cells**: Encode movement velocity

These cell types collectively provide a rich, biologically-plausible spatial representation that outperforms raw sensor inputs for navigation tasks.

## Architecture

### NEAT Integration
```
Navigation Cells (Input) → NEAT-evolved RNN (Hippocampus) → Navigation Actions (Output)
```

- **Navigation cells** provide spatial context as structured input
- **NEAT** evolves both weights AND topology of the recurrent neural network
- **Recurrent connections** capture temporal dependencies in navigation
- **Topology evolution** discovers optimal network complexity for each environment

### Key Advantages
- **Adaptability**: NEAT discovers optimal network structures for different environments
- **Biological plausibility**: Mirrors hippocampal spatial representation mechanisms
- **Dynamic environments**: Handles moving obstacles and changing conditions
- **Real-time**: Suitable for robotics and game applications

## Methodology

### Input Representation
Navigation cells encode spatial information as a structured vector:
1. Compute place cell activations based on current position
2. Generate grid cell firing patterns
3. Encode head direction as angular representation
4. Detect border proximity
5. Measure current speed

### NEAT Evolution
1. Initialize population of simple networks
2. Evaluate fitness on path planning task
3. Apply speciation to protect innovation
4. Mutate topology (add nodes, add connections)
5. Mutate weights
6. Select survivors for next generation

### Environment Types
- **Static environments**: Fixed obstacles, known layout
- **Dynamic environments**: Moving obstacles, changing conditions
- **Complex environments**: Multiple constraints, narrow passages

## Evaluation Metrics
- Path length efficiency
- Collision rate
- Computation time
- Adaptability to environment changes
- Generalization across environments

## Applications
- Autonomous robot navigation
- Game AI pathfinding
- Drone navigation
- Warehouse logistics
- Search and rescue robotics

## Research Significance

This work bridges computational neuroscience and robotics by showing that biologically-inspired spatial representations, when combined with evolutionary topology search, produce highly adaptable navigation systems. The approach validates the utility of hippocampal cell types as computational primitives for artificial navigation systems.

## Related Skills
- neuro-brain-framework: Neuroscience-inspired AI agent framework
- ember-hybrid-snn-llm-architecture: Hybrid SNN-LLM cognitive architecture
- neuromorphic-spiking-ring-attractor-v2: Spiking ring attractor for navigation
