---
name: growing-neural-network-breadth-depth-time
version: 1.0.0
description: Differentiable cost framework for breadth, depth, and time in recurrent convolutional neural networks, enabling neural architectures to grow organically under resource constraints.
category: computational-neuroscience
tags: [neural-architecture, resource-constraints, breadth-depth-time, recurrent-convolutional-network, differentiable-costs, computational-graph, reaction-times, normative-framework]
activation_keywords: [neural network growth, breadth depth time, resource constraints, computational graph, reaction time, lattice network, recurrent convolutional]
papers:
  - title: "Growing a Neural Network in Breadth, Depth, and Time"
    url: https://arxiv.org/abs/2605.25174
    authors: "Eivinas Butkus, Kedar Garzón Gupta, Nikolaus Kriegeskorte"
    year: 2026
---

# Growing a Neural Network in Breadth, Depth, and Time

> A differentiable cost framework for breadth, depth, and time that allows recurrent convolutional neural networks to grow organically under resource pressures, with emergent computation time correlating with human reaction times.

## Overview

Spatial and temporal resource constraints are critical for both biological and artificial intelligent systems. This paper defines differentiable cost terms for breadth (number of units per layer), depth (number of layers), and time (number of recurrent computational steps) within a recurrent convolutional neural network (RCNN) conceived as a finite subset of an infinite lattice. These cost terms are optimized jointly with task errors via backpropagation, allowing the network architecture to emerge organically through training.

By setting different pressures on breadth, depth, and time, the framework produces diverse computational graphs that naturally arise from the training process rather than being hand-designed. The key insight is that all three resources — breadth, depth, and time — can be traded off against each other to achieve a given level of accuracy, revealing a fundamental resource allocation manifold in neural computation. Networks grow in all three dimensions as task complexity increases and spontaneously take more recurrent steps when inputs are occluded.

A particularly striking finding is that the computation time used by the model correlates with human reaction times in an object recognition task, suggesting that the framework captures something fundamental about how biological systems allocate temporal resources to perception. The framework provides a normative account of how resource constraints shape neural architectures, connecting to questions about brain design in neuroscience and illuminating the diversity of neural solutions found in nature.

## Key Methodology

### Infinite Lattice Conception
The network is conceived as a finite subset of an infinite lattice of processing units. This conceptualization allows breadth and depth to be treated as continuous, differentiable quantities that can be optimized via gradient descent. The finite network that is actually implemented is a learnable window into this infinite lattice, and its extent in breadth, depth, and time is determined by the optimization process itself.

### Differentiable Cost Terms
Three distinct cost terms are defined and jointly optimized with task performance:
- **Breadth cost**: penalizes the number of units per layer (width of the network), encouraging efficient use of parallel processing capacity.
- **Depth cost**: penalizes the number of layers (sequential depth of the network), encouraging shallow processing where possible.
- **Time cost**: penalizes the number of recurrent computational steps, encouraging rapid processing where possible.
Each cost term is differentiable and can be weighted independently, allowing exploration of different resource allocation regimes.

### Joint Optimization via Backpropagation
The resource costs are added to the task loss function and the entire system is trained end-to-end with backpropagation through time. This means the network simultaneously learns (1) what computations to perform (weights), (2) how many units and layers to use (architecture), and (3) how many recurrent steps to take (computation time). The gradient signal flows through both the weight parameters and the architectural parameters.

## Core Findings

1. **Breadth-Depth-Time Trade-offs**: All three resources can be traded off against each other to achieve a given accuracy level. A network constrained to be narrow can compensate with more depth or more recurrent steps; a shallow network can compensate with more breadth or time; and a fast network can compensate with more breadth or depth.

2. **Growth with Task Complexity**: Networks organically grow in all three dimensions as task complexity increases. Simple tasks yield small, shallow, fast networks while complex tasks yield larger, deeper, slower networks — mirroring observations in biological neural systems.

3. **Adaptive Temporal Processing**: Networks spontaneously take more recurrent computational steps when inputs are occluded or partially visible, without being explicitly instructed to do so. This adaptive allocation of computation time emerges naturally from the cost-optimization framework.

4. **Correlation with Human Reaction Times**: The number of recurrent steps used by the model on individual trials correlates with human reaction times in an object recognition task. This suggests that the model's emergent temporal resource allocation reflects a fundamental principle shared with biological perception.

## Technical Details

### Mathematical Framework
- **Lattice model**: The network is defined as a finite subgraph of an infinite 3D lattice indexed by (breadth position, depth position, time step). Units at position (b, d, t) receive inputs from units at (b', d-1, t) and (b', d, t-1), implementing both feedforward and recurrent connectivity.
- **Cost functions**: The total loss is L_total = L_task + λ_B · C_breadth + λ_D · C_depth + λ_T · C_time, where λ_B, λ_D, λ_T are hyperparameters controlling the pressure on each resource.
- **Differentiable architecture parameters**: The effective breadth B, depth D, and time T are parameterized by continuous variables with soft (differentiable) boundaries, allowing gradient-based optimization of the architecture.
- **Masking mechanism**: Units beyond the current breadth/depth/time boundary are masked out with a smooth differentiable mask, enabling gradual inclusion/exclusion of units during optimization.

### Algorithm / Implementation
1. Initialize a sufficiently large recurrent convolutional lattice with units indexed by (breadth, depth, time).
2. Define differentiable masks for breadth, depth, and time boundaries, parameterized by continuous variables.
3. Set resource cost weights λ_B, λ_D, λ_T to impose desired pressures.
4. Forward pass: apply masks, run the RCNN for the current number of recurrent steps, compute task loss and resource costs.
5. Backward pass: compute gradients with respect to both weight parameters and architecture parameters (breadth, depth, time boundaries).
6. Update all parameters via gradient descent.
7. After training, the effective architecture is read off from the learned boundary parameters.
8. Evaluate: compare emergent computation times against human reaction time data.

## Practical Applications

### When to Use
- Designing neural architectures that must operate under resource constraints (compute, memory, latency)
- Modeling how biological neural circuits might self-organize under metabolic and spatial constraints
- Predicting human reaction times from computational principles in perceptual tasks
- Exploring the space of equivalent-performing architectures to understand neural diversity
- Building adaptive systems that allocate more computation time to harder inputs

### How to Apply
1. Define the task and select an appropriate base recurrent convolutional architecture with lattice structure.
2. Initialize the lattice to be larger than the expected final architecture.
3. Set resource cost weights based on the desired trade-off regime (e.g., prioritize speed vs. compactness).
4. Train end-to-end with joint loss optimization, monitoring both task performance and resource usage.
5. Analyze the emergent architecture: how many units, layers, and time steps the network uses.
6. Probe temporal adaptation by varying input difficulty or occlusion levels and measuring the network's adaptive computation time.
7. For neuroscience applications, compare emergent computation patterns against behavioral and neural data.

## Limitations & Future Directions

- The framework is demonstrated on relatively simple recurrent convolutional architectures; scaling to modern deep architectures (transformers, large-scale CNNs) may require additional engineering.
- The correlation with human reaction times, while striking, is demonstrated on a single object recognition task; broader validation across tasks and modalities is needed.
- The current cost terms treat breadth, depth, and time as independent; in biological systems, these resources interact in complex ways (e.g., metabolic cost per spike depends on connectivity).
- The framework does not model the developmental process of network growth; it optimizes the final architecture but not the growth trajectory.
- Incorporating additional biological constraints (e.g., wiring length, Dale's law, sparse connectivity) would increase relevance to neuroscience.
- The relationship between the learned architectures and optimal architectures (in an information-theoretic sense) remains to be explored.

## Key References

- Original paper: [Growing a Neural Network in Breadth, Depth, and Time](https://arxiv.org/abs/2605.25174)
- neuronal energetics and metabolic constraints on neural computation (Attwell & Laughlin, 2001)
- Adaptive computation time (Graves, 2016)
- Neural architecture search (Zoph & Le, 2017; Real et al., 2019)
- Human reaction times and perceptual difficulty (Palmer et al., 2005)

## Related Skills

- maximum-entropy-network-structure-function
- neural-architecture-search
- adaptive-computation-time
- recurrent-neural-network-dynamics
- resource-rational-cognition
- computational-principles-neural-circuits
