---
name: growing-neural-network-breadth-depth-time
description: "Differentiable cost framework for jointly optimizing neural network breadth, depth, and time - reveals resource trade-offs and human reaction time correlation"
trigger_words:
  - neural network architecture
  - resource constraints
  - breadth depth time
  - recurrent network
  - computational graphs
  - reaction time
  - task complexity
activation_keywords:
  - architecture growth
  - resource optimization
  - breadth depth
  - recurrent convolutional network
  - human reaction time
  - finite lattice
  - computational resource
version: 1.0.0
last_updated: 2026-06-19
paper_source: arXiv:2605.25174
authors: Eivinas Butkus, Kedar Garzón Gupta, Nikolaus Kriegeskorte
submitted: 2026-05-24
---

# Growing a Neural Network in Breadth, Depth, and Time

## Background

Spatial and temporal resource constraints are critical for both **biological and artificial intelligent systems**. This paper defines differentiable cost terms for three key dimensions of neural computation:

1. **Breadth** - Number of parallel units/layers
2. **Depth** - Number of sequential processing stages  
3. **Time** - Number of recurrent processing steps

## Core Innovation

Define a **recurrent convolutional neural network** as a finite subset of an infinite lattice, then optimize **resource costs jointly with task errors via backpropagation**.

### Key Framework Features

- Differentiable cost functions for all three dimensions
- Joint optimization (accuracy + resource constraints)
- Emergent architecture based on task demands
- Direct comparison with human behavior

## Methodology

### Network Architecture

Conceptualized as **finite subset of infinite lattice**:
- Each position has breadth, depth, and temporal extent
- Recurrent connections enable time dimension
- Convolutional structure for spatial processing

### Cost Terms

```python
# Conceptual form
total_loss = task_error + λ_b * breadth_cost + λ_d * depth_cost + λ_t * time_cost

# Where:
# breadth_cost = number of parallel units activated
# depth_cost = number of sequential layers used  
# time_cost = number of recurrent steps taken
```

### Training Process

1. Initialize with minimal architecture
2. Apply different pressures via λ coefficients
3. Networks **grow organically** to meet task demands
4. All three dimensions trade-off against each other

## Key Findings

### 1. Resource Trade-offs

- **All three resources can be traded off** against each other
- To achieve same accuracy: can use:
  - More breadth, less depth
  - More depth, less time
  - More time, less breadth
- **Task complexity determines growth** in all dimensions

### 2. Adaptive Behavior

- Networks **spontaneously take more recurrent steps** when inputs are occluded
- Temporal adaptation emerges without explicit instructions
- Suggests principled computation allocation

### 3. Human Correlation

**Surprising finding**: Model's time correlates with **human reaction times** in object recognition tasks.

- More complex objects → more recurrent steps → longer reaction time
- Validates computational relevance of time dimension

## Implications

### For Neuroscience

Provides **normative account** of how resource constraints shape neural architectures:
- Why brains have particular breadth/depth structure
- Why processing time varies by complexity
- Connection to cortical hierarchy design

### For AI/ML

- **Architecture search without explicit design**
- Principled resource allocation
- Task-driven complexity scaling
- Performance-resource trade-offs explicit

### For Brain-Model Alignment

- **Reaction time alignment** is novel behavioral metric
- Beyond accuracy: temporal dynamics matter
- Resource constraints mirror biological reality

## Technical Implementation

### Recurrent Convolutional Lattice

```
Position (x, y, layer, time) in lattice
- Spatial coordinates: x, y (convolution)
- Layer coordinate: depth
- Time coordinate: recurrent iteration

Activation: a[x, y, layer, time]
Costs computed over active subset
```

### Differentiable Optimization

```python
# Joint loss
L = L_task + λ_b * C_breadth + λ_d * C_depth + λ_t * C_time

# Backpropagation through lattice
∂L/∂weights includes resource gradients
```

## Experimental Validation

- Object recognition tasks
- Input occlusion experiments
- Comparison with human reaction times
- Varying λ pressures → varying architectures

## Connection to Nature

Framework helps illuminate **diversity of neural solutions**:
- Different species might have different resource pressures
- Evolution trades off breadth/depth/time
- Task demands shape architecture

## Applications

1. **Neuromorphic Design** - Resource-aware architecture selection
2. **Model Efficiency** - Optimal accuracy-resource trade-offs
3. **Brain Modeling** - Simulate biological resource constraints
4. **Behavioral Prediction** - Reaction time forecasting
5. **Architecture Search** - Principled growth strategies

## Key Takeaways

- **Normative framework**: Why architectures are shaped as they are
- **Behavioral validation**: Human reaction time correlation
- **Organic growth**: Architectures emerge from optimization
- **Explicit trade-offs**: No free lunch in breadth/depth/time
- **Task-driven scaling**: Complexity determines resource needs

## Critical Insight

This work bridges **computational resource theory** and **biological neural design**:
- Brain doesn't just optimize accuracy
- Constraints shape architecture profoundly
- Time dimension matters for behavior prediction
- Recurrence adapts to input complexity

## Future Directions

- Extend to attention mechanisms
- Connection to cortical column organization
- Hardware-specific resource costs
- Multi-task resource allocation
- Sleep/wake cycle resource differences