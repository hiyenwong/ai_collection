---
name: self-supervised-local-learning-rhm
description: "Layerwise self-supervised local learning rules for deep networks on the Random Hierarchy Model (RHM). Direct feedback approximations fail due to input-specific masking nonlinearity; layerwise contrastive/non-contrastive self-supervised rules succeed and match backprop data efficiency while being cortex-compatible. Use when: designing biologically plausible learning rules, local learning algorithms, self-supervised contrastive learning, solving weight transport problem, hierarchical structure learning, cortical-compatible plasticity."
---

# Self-Supervised Local Learning on Random Hierarchy Model (RHM)

## Core Problem

How do biological neural networks learn abstract hierarchical representations without backpropagation's symmetric weight requirement (weight transport problem)?

## Key Finding from arXiv:2605.18557

Two classes of local learning rules tested on RHM:

### Class 1: Direct Feedback Approximations → **FAIL**
- Use direct feedback signals to approximate error propagation from output layer
- Fail because they miss **input-specific nonlinear masking** that is essential in full backprop
- Cannot learn complex hierarchical tasks

### Class 2: Layerwise Self-Supervised Rules → **SUCCEED**
- Use layerwise contrastive or non-contrastive loss functions
- Do **not** approximate errors at the output layer
- **As data-efficient as supervised backpropagation**
- Compatible with known cortical synaptic plasticity rules

## Mechanism

Full backprop implements input-specific masking:
```
∂L/∂w_l = δ_l · x_l  where δ_l depends on downstream Jacobian AND input-specific gates
```
Direct feedback rules approximate δ_l globally but miss the input-specific component, causing failure on hierarchical tasks.

Self-supervised rules bypass this by learning structure directly at each layer.

## Application Patterns

```python
class LayerwiseSelfSupervisedLearning:
    def __init__(self, layers):
        self.layers = layers
        
    def train_step(self, x):
        h = x
        for i, layer in enumerate(self.layers):
            # Layerwise self-supervised objective
            # e.g., contrastive: maximize agreement between augmented views
            loss = self.contrastive_loss(layer(h))
            layer.update(loss)  # Local update, no global error signal needed
            h = layer(h)
```

## When to Apply

- Building biologically plausible deep learning models
- Solving the weight transport problem
- Training deep networks without symmetric feedback weights
- Learning hierarchical representations with local plasticity rules
- Neuromorphic computing implementations
