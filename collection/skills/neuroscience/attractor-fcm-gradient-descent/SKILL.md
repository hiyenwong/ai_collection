---
name: attractor-fcm-gradient-descent
description: "Gradient descent-based physics-constrained Jacobian Fuzzy Cognitive Map (FCM) with attractor dynamics, residual memory, and BPTT. Uses Newton's method for fixed point attractor finding with adaptive landscape manipulation. Triggers: attractor FCM, fuzzy cognitive map gradient, FCM attractor dynamics, physics-constrained FCM, Jacobian FCM."
---

# Attractor FCM: Gradient Descent-Based Fuzzy Cognitive Maps

> A physics-constrained, Jacobian-based Fuzzy Cognitive Map using gradient descent with attractor dynamics, residual memory, and backpropagation through time.

## Metadata
- **Source**: arXiv:2604.27947
- **Authors**: Alexis Kafantaris
- **Published**: 2026-04-30
- **Categories**: cs.NE (Neural and Evolutionary Computing)

## Core Methodology

### Key Innovation
This FCM variant departs from traditional Hebbian or agentic learning, instead using **gradient descent with physics constraints** on the Jacobian matrix of the FCM dynamics.

### Technical Framework

1. **Residual Memory Mechanism**:
   - Residuals update the recursive component without losing system memory
   - Maintains state continuity during weight updates

2. **Fixed Point Anchor**:
   - Recursively implemented to update weights
   - Converges to a fixed point attractor
   - BPTT (Backpropagation Through Time) unrolls from this anchor
   - Ensures error minimization targets accurate gradient computation

3. **Newton's Method + Gradient Descent**:
   - Newton's method finds the system's fixed point attractor
   - Gradient descent adaptively changes the optimization landscape
   - An **adaptive term** directly manipulates weights through attractor dynamics

4. **Adaptive Landscape Control**:
   - Descent adjusts according to sigmoid saturation levels
   - Prevents premature convergence to local minima

5. **Causal Mask Filtering**:
   - Updates filtered by causal mask encoding physics constraints
   - Respects initial expert-based opinions
   - Reduces error to target efficiently

### Learning Algorithm
```
1. Initialize FCM weights from expert knowledge
2. Apply causal mask to constrain physics-consistent updates
3. Use Newton's method to find fixed point attractor
4. Unroll BPTT from attractor for gradient computation
5. Apply adaptive gradient descent (modulated by sigmoid saturation)
6. Update weights via residual memory mechanism
7. Repeat until convergence
```

## Implementation Guide

### Prerequisites
- Expert knowledge for initial weight matrix (FCM requires domain knowledge)
- Physics/domain constraints for causal mask

### Key Parameters
- **Fixed point tolerance**: Controls convergence criterion for Newton's method
- **BPTT unroll length**: Determines temporal credit assignment depth
- **Adaptive term coefficient**: Controls landscape manipulation strength
- **Causal mask**: Encodes domain-specific update constraints

## Applications
- Causal system modeling with expert knowledge
- Dynamic system prediction with physics constraints
- Fuzzy cognitive map-based decision support
- Knowledge-guided neural network training

## Pitfalls
- Requires good initial expert knowledge (FCM is not data-only)
- Newton's method may be computationally expensive for large maps
- Sigmoid saturation monitoring is critical — ignoring it causes premature convergence
- Causal mask design requires domain expertise

## Related Skills
- brain-inspired-capture-evidence-driven-neuromimetic-perceptual
- computational-linguistics-brain-perspective
- hippocampus-multi-attractor-memory
- triple-loop-consolidation-non-gradient-memory
