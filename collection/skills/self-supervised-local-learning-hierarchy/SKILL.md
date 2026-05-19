---
name: self-supervised-local-learning-hierarchy
description: "Self-supervised local learning rules for discovering hidden hierarchical structure in high-dimensional data. Demonstrates that layerwise self-supervised learning (contrastive/non-contrastive) succeeds where direct-feedback methods fail on the Random Hierarchy Model (RHM). Use when: (1) designing biologically plausible learning algorithms, (2) studying local vs. backprop learning, (3) implementing self-supervised learning in neural networks, (4) analyzing hierarchical structure learning, (5) comparing biological plasticity rules to backpropagation. Activation: self-supervised local learning, biological plasticity, contrastive learning, non-contrastive learning, Random Hierarchy Model, RHM, local learning rules, Gerstner, Bellec, biologically plausible backprop"
---

# Self-Supervised Local Learning for Hierarchical Structure Discovery

**Paper**: Delrocq et al. (2026). *Self-supervised local learning rules learn the hidden hierarchical structure of high-dimensional data*. arXiv:2605.18557.

## Core Insight

Two classes of biologically plausible local learning rules behave fundamentally differently on hierarchical tasks:

- **Type 1 (direct feedback)**: FAIL — cannot solve RHM tasks due to missing input-specific nonlinearities (masking) essential for complex learning
- **Type 2 (layerwise self-supervised)**: SUCCEED — data-efficient as supervised backpropagation, compatible with cortical synaptic plasticity

## The Random Hierarchy Model (RHM)

Artificial dataset designed to study how neural networks learn intrinsic hierarchical structure of high-dimensional data. Tests whether learning algorithms can discover hidden compositional rules.

## Type 1: Direct Feedback Methods

### What They Do
Use direct feedback signals from output layer to approximate error propagation to hidden layers.

### Why They Fail
- Backpropagation implements **input-specific nonlinearities** ("masking") that are essential for learning complex tasks
- Direct feedback approximations miss these masking operations
- Cannot learn hierarchical hidden structure regardless of training duration

## Type 2: Layerwise Self-Supervised Methods

### What They Do
- Use layerwise self-supervised contrastive or non-contrastive loss functions
- Do NOT explicitly approximate output-layer errors
- Each layer learns to discover structure independently

### Why They Succeed
- Self-supervised objectives naturally capture hierarchical structure
- As data-efficient as supervised backpropagation
- Compatible with known rules of synaptic plasticity in cortex
- Avoid long convergence time and symmetric error network requirements

### Specific Rules

#### Contrastive Learning
- Pull similar representations together, push diss apart
- Layerwise application discovers hierarchical features

#### Non-Contrastive Learning
- Learn without explicit negative samples
- Still captures hierarchical structure through feature redundancy minimization

## Key Findings

1. **All Type 1 rules fail** on RHM tasks — traced to missing masking operations in backprop equivalence
2. **Type 2 rules succeed** — learn hierarchical hidden structure as efficiently as backprop
3. **Data efficiency**: Self-supervised local learning matches supervised backprop data requirements
4. **Biological plausibility**: Type 2 rules compatible with known cortical plasticity mechanisms

## Implications for Brain Learning

The brain likely uses **layerwise self-supervised objectives** (Type 2) rather than approximate backpropagation (Type 1) for learning abstract representations:
- No symmetric error feedback network needed
- No long convergence time
- Consistent with observed synaptic plasticity rules
- Explains how cortex learns hierarchical representations from sensory input

## Applications

- **Biologically plausible deep learning**: Replace backprop with layerwise self-supervised objectives
- **Neuromorphic computing**: Implement local learning rules on spiking hardware
- **Representation learning**: Discover hierarchical structure without labels
- **Neuroscience**: Testable predictions about cortical plasticity mechanisms

## Experimental Protocol

1. Use RHM as benchmark dataset for hierarchical structure learning
2. Compare direct feedback vs. layerwise self-supervised rules
3. Measure data efficiency (samples needed to reach target performance)
4. Verify biological plausibility (no symmetric weights, no error propagation)
5. Test on natural data with known hierarchical structure

## Pitfalls

- **Do not assume direct feedback ≈ backprop**: Missing masking operations make them fundamentally different
- **Contrastive AND non-contrastive both work**: Either type of self-supervised objective can succeed
- **Input-specific nonlinearities are critical**: The "masking" property of backprop cannot be approximated by simple feedback
- **RHM is the right benchmark**: Standard datasets may not reveal the fundamental differences between rule types

## Activation Keywords

- self-supervised local learning
- biological plasticity rules
- contrastive learning neuroscience
- non-contrastive learning
- Random Hierarchy Model
- RHM benchmark
- Gerstner Bellec
- biologically plausible backprop
- layerwise self-supervised
- hierarchical structure learning
