---
name: growing-neural-breadth-depth-time
description: Differentiable cost terms for breadth, depth, and time in recurrent convolutional neural networks — resource constraints shape neural architectures. Time correlates with human reaction times. From arXiv:2605.25174.
license: MIT
---

# Growing a Neural Network in Breadth, Depth, and Time

Methodology from arXiv:2605.25174 (Butkus, Garzón Gupta & Kriegeskorte, May 2026). A normative framework showing how spatial and temporal resource constraints shape neural architectures by defining differentiable cost terms for breadth, depth, and time.

## Core Idea

Define differentiable cost terms for breadth, depth, and time within a recurrent convolutional neural network (conceived as a finite subset of an infinite lattice). Optimize these costs jointly with task errors via backpropagation to let computational graphs emerge organically.

## Key Concepts

1. **Three Resource Dimensions**:
   - **Breadth**: Number of neurons/channels per layer
   - **Depth**: Number of layers
   - **Time**: Number of recurrent processing steps

2. **Resource Trade-offs**: All three resources can be traded off against each other to achieve a given accuracy level.

3. **Emergent Computation Graphs**: Different pressures on breadth, depth, and time lead to diverse computational graphs emerging organically through training.

4. **Task-Specific Growth**: Networks grow in all three dimensions with task complexity and spontaneously take more recurrent steps when inputs are occluded.

## Framework

### Cost Function
```
L_total = L_task + λ_breadth · C_breadth + λ_depth · C_depth + λ_time · C_time
```

### Key Results
- Networks organically grow in breadth, depth, and time with increasing task complexity
- All three resources can be traded off against each other
- More recurrent steps spontaneously emerge when inputs are occluded
- **Surprisingly**: Time used by the model correlates with human reaction times in object recognition tasks

### Resource Trade-offs
| Resource | Measured by | Effect when constrained |
|-----------|-------------|------------------------|
| Breadth | Number of channels/neurons per layer | Forces deeper or slower processing |
| Depth | Number of processing layers | Forces wider or slower processing |
| Time | Recurrent steps | Forces wider or deeper networks |

## Neuroscience Connection

- Provides a normative account of how resource constraints shape neural architectures in the brain
- Time-resource correlation with human reaction times suggests shared computational principles
- Helps explain the diversity of neural solutions found in nature
- Connects AI architecture design to questions about brain design

## Applications
- **AI architecture design**: Resource-aware network growth without manual architecture search
- **Neuroscience**: Normative theory of neural resource allocation across brain areas
- **Cognitive science**: Model of how processing time relates to task difficulty
- **Object recognition**: Models that explain human reaction time patterns

## Activation
- resource-constrained-network-growth, breadth-depth-time-tradeoffs, emergent-computation-graphs, reaction-time-correlation, normative-neural-architecture, occluded-input-recurrence

## References
- Butkus, E., Garzón Gupta, K., & Kriegeskorte, N. (2026). Growing a Neural Network in Breadth, Depth, and Time. arXiv:2605.25174.
