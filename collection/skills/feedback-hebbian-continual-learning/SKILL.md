---
name: feedback-hebbian-continual-learning
description: Backpropagation-free continual learning using feedback-aligned Hebbian plasticity. Replaces backpropagation with local Hebbian updates guided by random feedback connections, enabling biologically plausible continual learning without catastrophic forgetting. Use for bio-inspired learning, continual/incremental learning, and backprop-free neural network training. Activation: backprop-free learning, feedback alignment, Hebbian continual learning, local learning rules, biologically plausible training, feedback Hebbian
version: 1.0.0
metadata:
  hermes:
    source_paper: "A Backpropagation-Free Feedback-Hebbian Network for Continual Learning Dynamics (arXiv:2601.06758v3)"
    published: "2026-01-11"
    categories: ['cs.NE', 'cs.LG']
    authors: Josh Li, Fow-sen Choa
---

# Backpropagation-Free Feedback-Hebbian Continual Learning

## Overview
Training framework that eliminates backpropagation by combining random feedback alignment with local Hebbian plasticity rules. Error signals are transmitted through fixed random feedback connections, while forward weights are updated using biologically plausible local learning rules.

## Core Architecture

### Forward Path
- Standard feedforward or recurrent network
- Forward weights updated via local Hebbian rules
- No gradient computation or backpropagation

### Feedback Path
- Fixed random feedback weights (initialized once, never updated)
- Transmit error signals from output to hidden layers
- Replace the need for weight transport (symmetric backprop)

### Local Learning Rule
- Hebbian plasticity modulated by feedback error signals
- Each synapse updates based only on local pre/post activity and global error
- No need to store gradients or compute Jacobians

## Implementation Pattern
```python
class FeedbackHebbianNetwork:
    def __init__(self, layers, feedback_scale=0.1, hebbian_lr=0.001):
        self.layers = layers
        self.forward_weights = [torch.randn(l, n) * 0.1 
                                for l, n in zip(layers[:-1], layers[1:])]
        self.feedback_weights = [torch.randn(n, l) * feedback_scale 
                                 for l, n in zip(layers[:-1], layers[1:])]
        self.lr = hebbian_lr
        
    def forward(self, x):
        activations = [x]
        for w in self.forward_weights:
            h = torch.relu(activations[-1] @ w)
            activations.append(h)
        return activations
    
    def hebbian_update(self, activations, target):
        output = activations[-1]
        error = output - target
        for i in range(len(self.forward_weights) - 1, -1, -1):
            local_error = error if i == len(self.forward_weights) - 1 else local_error
            local_error = local_error @ self.feedback_weights[i]
            pre = activations[i]
            delta_w = self.lr * (pre.T @ local_error)
            self.forward_weights[i] += delta_w
```

## Continual Learning Properties
- **No catastrophic forgetting**: Local updates don't overwrite all weights simultaneously
- **No replay buffer needed**: Natural resilience to sequential task learning
- **Biological plausibility**: No weight transport, no global error gradient
- **Scalability**: No backpropagation memory overhead

## References
- Josh Li, Fow-sen Choa, "A Backpropagation-Free Feedback-Hebbian Network for Continual Learning Dynamics", arXiv:2601.06758v3, 2026-01-11
