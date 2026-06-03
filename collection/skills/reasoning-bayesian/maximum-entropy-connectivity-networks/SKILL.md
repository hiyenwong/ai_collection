---
name: maximum-entropy-connectivity-networks
description: Maximum entropy principle for neural network connectivity — describe connectivity as a probability distribution over single-neuron weights, express task requirements as constraints, maximize Shannon entropy. From arXiv:2605.25607.
license: MIT
---

# Maximum Entropy Connectivity Networks

Methodology from arXiv:2605.25607 (Hruza & Ostojic, May 2026). A normative framework for understanding how network function constrains neural connectivity using the maximum entropy principle, independent of any particular learning algorithm.

## Core Idea

Describe connectivity as a probability distribution over single-neuron weights, express task requirements as constraints on this distribution, and determine the unique distribution maximizing Shannon entropy subject to these constraints.

## Key Concepts

1. **Maximum Entropy Principle for Connectivity**: Instead of training networks with gradient descent and analyzing resulting connectivity, directly compute the most random connectivity that satisfies task constraints.

2. **Weight Scale Parameter** (β): Controls the balance between randomness (low β) and task-induced structure (high β). Drives transitions from structured to random stimulus selectivity.

3. **Gain-Modulated Linear Models**: Maximum entropy inference becomes analytically tractable by mapping nonlinear 2-layer networks onto gain-modulated linear models.

4. **Emergent Populations**: Maximizing entropy under task constraints leads to emergence of neuronal populations, each defined by its pattern of contextual gain modulation.

## Framework

### Setup
- 2-layer feed-forward networks for context-dependent input-selection tasks
- Connectivity = probability distribution over single-neuron weights
- Task requirements = constraints on this distribution
- Maximize: H[w] = -∫ p(w) log p(w) dw subject to task constraints

### Key Results
- Starting from homogeneous prior → entropy maximization yields emergent neuronal populations
- Increasing number of contexts → transition from context-specialized to unspecialized random populations
- Increasing weight scale → parallel transition from structured to random stimulus selectivity
- Maximum entropy connectivity matches gradient-descent-trained networks both qualitatively and quantitatively

### Phase Transitions
| Parameter | Low Value | High Value |
|-----------|-----------|------------|
| # Contexts | Specialized populations | Unspecialized random |
| Weight scale β | Random connectivity | Structured stimulus selectivity |

## Applications

- **Theoretical neuroscience**: Normative account of connectivity-structure relationships
- **Network analysis**: Predict connectivity from task demands without training
- **Model comparison**: Compare against gradient-descent-trained networks
- **Population analysis**: Understand emergence of functional neuronal populations

## Activation
- Constrained by task objectives, trained-to-randomness transition, emergent-populations, gain-modulated-linear-models, maximum-entropy-connectivity

## References
- Hruza, L. & Ostojic, S. (2026). Balancing structure and randomness: maximum entropy networks for context-dependent computations. arXiv:2605.25607.
