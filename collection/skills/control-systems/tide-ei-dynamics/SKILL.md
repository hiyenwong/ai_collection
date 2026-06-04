---
name: tide-ei-dynamics
description: TIDE (Temporal Inhibitory-Excitatory Dynamic Engine) methodology — neuro-inspired architecture using asymmetric Excitatory-Inhibitory (E-I) networks with Wilson-Cowan dynamics and lateral inhibition for stabilized neural dynamics. Integrates Dale's principle (80:20 E-I ratio), hierarchical receptive fields, and game-theoretic energy-based optimization. Use when: designing neuro-inspired architectures with stability guarantees, building continuous thought/reasoning systems with internal dynamics, improving training efficiency with biologically-plausible constraints, implementing E-I balanced neural networks, or working with Wilson-Cowan dynamical systems in deep learning. Activation: TIDE, E-I balance, Wilson-Cowan, Dale's principle, neural dynamics stability, continuous thought machine, lateral inhibition, energy-based neural dynamics
---

## TIDE Architecture

TIDE models neural dynamics using asymmetric E-I networks stabilized via network theory principles and expressed as energy-based systems optimized through game-theoretic loss.

### Core Components

1. **Wilson-Cowan Dynamics**: Internal representations computed through neural dynamics governed by Wilson-Cowan equations
2. **Lateral Inhibition**: Stabilization mechanism preventing runaway excitation
3. **Dale's Principle Enforcement**: Strict 80:20 E-I neuron ratio maintained throughout architecture
4. **Hierarchical Receptive Fields (HRF)**: Multi-scale feature extraction mimicking cortical hierarchy
5. **Game-Theoretic Loss**: Energy-based optimization providing convergence proofs

### Key Properties

- **Convergence**: Proven convergence guarantees
- **Stability**: Theoretical stability bounds via network theory
- **Complexity**: Bounded computational complexity
- **Efficiency**: Surpasses CTM baseline with <50% training time and +1.65% top-1 accuracy on ImageNet under perturbations

### Implementation Pattern

```
Input → Hierarchical Receptive Fields → E-I Dynamics (Wilson-Cowan + Lateral Inhibition)
       → Game-theoretic Energy Optimization → Output
```

### When to Apply

- Architecture needs biological realism with mathematical guarantees
- Internal computation should be decoupled from external inputs (like CTM)
- Training efficiency and robustness to perturbations are priorities
- E-I balance is a design constraint (neuro-inspired systems)

### Integration Notes

- Replaces MLP-based internal dynamics in architectures like Continuous Thought Machine
- Energy-based formulation enables game-theoretic optimization
- Dale's principle enforcement requires explicit E/I neuron partitioning
