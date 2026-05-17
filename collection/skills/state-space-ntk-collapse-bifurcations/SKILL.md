---
name: state-space-ntk-collapse-bifurcations
description: >
  Local theory of gradient descent near bifurcations via state-space neural tangent
  kernel (sNTK). Bifurcations collapse sNTK to rank-one operators corresponding to
  classical normal forms, funneling gradient descent into critical dynamical directions.
  Use when: analyzing RNN learning dynamics near bifurcations, studying NTK collapse,
  understanding gradient-based training of recurrent systems, bifurcation analysis in
  deep learning, neural tangent kernel for temporal tasks, normal form learning theory.
---

# State-Space NTK Collapse Near Bifurcations

## Paper Reference

- **Title:** State-Space NTK Collapse Near Bifurcations
- **Authors:** James Hazelden, Eric Shea-Brown
- **arXiv:** 2605.12763 (May 2026)
- **Categories:** cs.LG, math.DS, math.OC, q-bio.NC

## Core Methodology

### Empirical State-Space NTK (sNTK)

The sNTK describes gradient descent dynamics in function space for temporal models:

$$K_{sNTK}(t, t') = \frac{\partial h(t)}{\partial \theta}^\top \frac{\partial h(t')}{\partial \theta}$$

where $h(t)$ is the hidden state at time $t$ and $\theta$ are model parameters.

### Key Finding: Bifurcation Dominance

Near bifurcations, the sNTK reduces to a **rank-one operator**:

$$K_{sNTK} \approx \lambda \cdot v \cdot v^\top$$

where $v$ corresponds to the critical eigendirection of the normal form.

This means learning near bifurcations is **dominated by a single parameter direction**,
making the learning geometry predictable from classical bifurcation theory.

### Bifurcation Channel Decomposition

Procedure:
1. Compute sNTK at the current parameter configuration
2. Decompose into bifurcation-relevant channel and residual channel
3. Near codimension-1 bifurcations, the relevant channel is rank-one and highly amplified
4. This amplification causes the bifurcation channel to dominate the full sNTK

### Normal Form Correspondence

| Bifurcation Type | Normal Form | Learning Geometry |
|---|---|---|
| Saddle-node | $\dot{x} = \mu + x^2$ | Single dominant direction |
| Pitchfork | $\dot{x} = \mu x - x^3$ | Symmetric bifurcation in parameter space |
| Hopf | $\dot{z} = (\mu + i\omega)z - |z|^2 z$ | Oscillatory mode emergence |

### Learning Instability Resolution

Low-rank natural gradient methods resolve learning instability near bifurcations:
- Standard SGD becomes unstable as sNTK effective rank collapses
- Natural gradient restricted to the dominant bifurcation direction stabilizes training
- Very little overhead compared to SGD

## Student-Teacher RNN Illustration

In the student-teacher RNN setup:
- First learned bifurcation coincides with sharp sNTK effective rank collapse
- Emergence of dominant parameter direction
- Restricted sNTK closely matches pitchfork normal form landscape

## Practical Applications

### RNN Training Diagnostics
- Monitor sNTK effective rank during training
- Sharp drops indicate the network is learning bifurcations
- Use this signal to adapt learning rates or switch to natural gradient

### Architecture Design
- Bifurcations are necessary for rich temporal feature learning
- Design architectures that facilitate controlled bifurcation passage
- Use normal form theory to predict learning behavior

### Optimization Strategy
- When sNTK rank collapses, switch to low-rank natural gradient
- Avoid standard SGD instability near bifurcation boundaries
- Exploit rank-one structure for efficient second-order updates

## Activation Keywords

- state-space NTK, sNTK collapse, bifurcation learning dynamics
- RNN training bifurcation, neural tangent kernel recurrent
- normal form learning theory, gradient descent near bifurcation
- pitchfork bifurcation neural network, Hopf bifurcation learning
- low-rank natural gradient RNN, bifurcation channel decomposition
- temporal feature learning, recurrent network dynamics analysis
