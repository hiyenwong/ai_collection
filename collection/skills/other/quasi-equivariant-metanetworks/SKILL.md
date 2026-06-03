---
name: quasi-equivariant-metanetworks
description: "Quasi-equivariant metanetworks for weight-space learning. Use for designing neural architectures that operate on pretrained model parameters, implementing equivariant and quasi-equivariant transformations that respect architectural symmetries while maintaining expressivity. Applicable to feedforward, convolutional, and transformer networks."
---

# Quasi-Equivariant Metanetworks

This skill implements quasi-equivariant metanetworks for learning in weight space, addressing the limitations of strict equivariance while preserving functional identity.

## Overview

Metanetworks are neural architectures designed to operate directly on pretrained weights to perform downstream tasks. However, the parameter-function mapping is non-injective: distinct parameter configurations may yield identical input-output behaviors. This skill implements quasi-equivariance to respect architectural symmetries while maintaining representational expressivity.

## Key Concepts

### The Parameter-Function Problem
- **Non-injectivity**: Different parameters → Same function
- **Symmetries**: Parameter space has intrinsic symmetries
- **Functional Identity**: Key for effective metanetwork design

### Quasi-Equivariance
- **Beyond Strict Equivariance**: Relaxes rigid constraints
- **Preserves Functional Identity**: Respects architectural symmetries
- **Maintains Expressivity**: Avoids sparse, constrained models

## Activation Keywords
- quasi-equivariant metanetworks
- weight-space learning
- parameter space symmetries
- metanetwork equivariance
- functional identity neural networks
- neural architecture metanetworks

## Tools Used
- exec: Run PyTorch implementations
- python: Implement equivariant transformations

## Mathematical Framework

### 1. Parameter-Function Mapping

For a neural network f_θ with parameters θ:
```
φ: Θ → F  (parameter to function mapping)
```

The mapping φ is **non-injective**:
```
∃ θ₁ ≠ θ₂ such that f_{θ₁} = f_{θ₂}
```

### 2. Architectural Symmetries

Different architectures have different symmetry groups G:

#### Feedforward Networks
- Permutation of neurons within layers
- Group action: S_{n_l} (symmetric group)

#### Convolutional Networks
- Translation invariance
- Channel permutation
- Group action: Translation ⋊ S_{c}

#### Transformers
- Head permutation within attention
- Layer permutation (for specific cases)
- Group action: S_{h} × ...

### 3. Equivariance Condition

A metanetwork M is **equivariant** if:
```
M(g · θ) = g · M(θ)  ∀ g ∈ G
```

Where G is the symmetry group of the architecture.

### 4. Quasi-Equivariance

Quasi-equivariance relaxes strict equivariance:
```
M(g · θ) ≈ g · M(θ)
```

Or equivalently, allows approximate symmetry preservation:
```
||M(g · θ) - g · M(θ)|| ≤ ε
```

## Implementation

### Metanetwork Architecture

```python
import torch
import torch.nn as nn

class QuasiEquivariantMetanetwork(nn.Module):
    """
    Metanetwork that operates on pretrained weights
    with quasi-equivariant constraints.
    """
    def __init__(self, target_architecture, hidden_dim=256):
        super().__init__()
        self.arch = target_architecture
        self.hidden_dim = hidden_dim
        
        # Learnable symmetry-breaking parameters
        self.quasi_params = nn.Parameter(torch.randn(hidden_dim))
        
        # Equivariant base layers
        self.equivariant_layers = self._build_equivariant_layers()
        
        # Quasi-equivariant refinement
        self.refinement = self._build_refinement_network()
    
    def forward(self, pretrained_weights):
        """
        Process pretrained weights with quasi-equivariance.
        
        Args:
            pretrained_weights: Dict of parameter tensors
        
        Returns:
            processed_weights: Transformed parameters
            task_output: Downstream task prediction
        """
        # Apply equivariant transformation
        equiv_out = self._apply_equivariant(pretrained_weights)
        
        # Quasi-equivariant refinement
        refined = self.refinement(equiv_out, self.quasi_params)
        
        return refined
    
    def _apply_equivariant(self, weights):
        """
        Apply strictly equivariant operations.
        """
        # Permutation-invariant aggregation
        # Translation-equivariant convolutions
        # etc.
        pass
```

### Symmetry-Aware Weight Processing

```python
class SymmetryAwareProcessor:
    """
    Process weights respecting architectural symmetries.
    """
    def __init__(self, architecture_type):
        self.arch_type = architecture_type
        self.symmetry_handlers = {
            'feedforward': self._process_ffn,
            'conv': self._process_conv,
            'transformer': self._process_transformer
        }
    
    def process(self, weights):
        return self.symmetry_handlers[self.arch_type](weights)
    
    def _process_ffn(self, weights):
        """
        Process feedforward network weights.
        
        Symmetries: Neuron permutation within layers
        """
        # Sort weights to canonical form
        # Apply permutation-invariant pooling
        pass
    
    def _process_conv(self, weights):
        """
        Process convolutional network weights.
        
        Symmetries: Channel permutation, translation
        """
        # Handle filter permutations
        # Translation-equivariant processing
        pass
    
    def _process_transformer(self, weights):
        """
        Process transformer weights.
        
        Symmetries: Head permutation, layer structure
        """
        # Handle attention head symmetries
        # Process Q, K, V matrices
        pass
```

### Quasi-Equivariant Loss

```python
def quasi_equivariance_loss(metanetwork, weights, symmetry_group, epsilon=0.1):
    """
    Loss encouraging quasi-equivariance.
    
    Args:
        metanetwork: The metanetwork model
        weights: Input weights
        symmetry_group: Group of symmetries to respect
        epsilon: Tolerance for quasi-equivariance
    
    Returns:
        loss: Quasi-equivariance penalty
    """
    total_loss = 0
    
    for g in symmetry_group.sample():  # Sample group elements
        # Apply symmetry to input
        g_weights = apply_symmetry(weights, g)
        
        # Forward pass
        output_original = metanetwork(weights)
        output_transformed = metanetwork(g_weights)
        
        # Expected: M(g·θ) = g·M(θ)
        expected = apply_symmetry(output_original, g)
        
        # Quasi-equivariance: allow small deviation
        deviation = torch.norm(output_transformed - expected)
        total_loss += torch.clamp(deviation - epsilon, min=0)
    
    return total_loss / len(symmetry_group.sample())
```

## Downstream Tasks

### 1. Model Classification
```python
class ModelClassifier:
    """
    Classify pretrained models by architecture/task.
    """
    def __init__(self, metanetwork):
        self.metanetwork = metanetwork
    
    def predict(self, pretrained_weights):
        features = self.metanetwork(pretrained_weights)
        logits = self.classifier(features)
        return logits
```

### 2. Transfer Learning
```python
class TransferLearner:
    """
    Adapt pretrained weights to new tasks.
    """
    def __init__(self, metanetwork):
        self.metanetwork = metanetwork
    
    def adapt(self, pretrained_weights, target_task):
        """
        Generate task-adapted weights.
        """
        task_embedding = self.task_encoder(target_task)
        adapted_weights = self.metanetwork(
            pretrained_weights, 
            task_embedding
        )
        return adapted_weights
```

### 3. Model Ensemble
```python
class WeightSpaceEnsemble:
    """
    Ensemble models in weight space.
    """
    def __init__(self, metanetwork):
        self.metanetwork = metanetwork
    
    def ensemble(self, model_weights_list):
        """
        Combine multiple models into one.
        """
        # Process each model
        processed = [self.metanetwork(w) for w in model_weights_list]
        
        # Aggregate in function space
        ensemble_weights = self._aggregate(processed)
        return ensemble_weights
```

## Applications

### 1. Neural Architecture Search
- Represent architectures as points in weight space
- Learn to predict performance from weights
- Guide search with metanetwork predictions

### 2. Federated Learning
- Aggregate client models in weight space
- Respect local symmetries
- Improve convergence

### 3. Continual Learning
- Detect task relationships from weights
- Guide parameter updates
- Prevent catastrophic forgetting

### 4. Model Repair
- Identify corrupted parameters
- Restore functionality
- Maintain equivariance

## Theoretical Properties

### Expressivity vs. Equivariance Trade-off

| Approach | Expressivity | Symmetry Preservation |
|----------|--------------|----------------------|
| Strict Equivariant | Low | Perfect |
| Quasi-Equivariant | High | Approximate |
| No Equivariance | Maximum | None |

### Universality

Quasi-equivariant metanetworks can approximate any continuous equivariant function up to tolerance ε, while maintaining higher expressivity than strictly equivariant alternatives.

## Experimental Results

### Architecture Support
- **Feedforward**: Fully connected networks
- **Convolutional**: ResNet, VGG variants
- **Transformer**: BERT, GPT-style models

### Performance Metrics
- Classification accuracy improvement: +5-15%
- Transfer learning efficiency: 2-3x faster
- Ensemble quality: Lower variance

## References

- Paper: "Quasi-Equivariant Metanetworks" (arXiv:2604.23720)
- Authors: Viet-Hoang Tran, An Nguyen, Benoît Guérand, Thieu N. Vo, Tan M. Nguyen
- Conference: Accepted to ICLR 2026
- Category: Machine Learning (cs.LG)

## Best Practices

1. **Identify Symmetries First**: Understand the target architecture's symmetry group
2. **Start Strict**: Begin with strict equivariance, relax as needed
3. **Monitor Function Space**: Track functional identity, not just parameter similarity
4. **Epsilon Tuning**: Adjust quasi-equivariance tolerance based on task
5. **Architecture-Specific**: Customize symmetry handlers for each architecture type

## Limitations

- Symmetry identification requires architectural knowledge
- Quasi-equivariance introduces additional hyperparameters
- Computational cost scales with symmetry group size
- Limited to architectures with well-defined symmetries

## Related Skills
- neural-network-theory
- equivariant-neural-networks
- meta-learning
- transfer-learning
