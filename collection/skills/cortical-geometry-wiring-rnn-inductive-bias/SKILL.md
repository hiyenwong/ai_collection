---
name: cortical-geometry-wiring-rnn-inductive-bias
description: Harnessing cortical geometry, wiring, and function as inductive biases for recurrent neural networks — biologically grounded RNNs using MICrONS connectomics data (spatial coordinates, anatomical connectivity, functional relationships) to achieve superior learning performance.
version: 1.0.0
category: neuroscience
tags: [RNN, cortical-geometry, connectomics, MICrONS, inductive-bias, biological-neural-networks, spatial-constraints, functional-connectivity]
arxiv: 2606.14975
authors: [Mo Shakiba, Rana Rokni, Mohammad Mohammadi, Nima Dehghani]
published: 2026-06-12
activation_keywords: [cortical geometry, biological RNN, MICrONS, inductive bias, spatial embedding, functional weight initialization, neuronal constraints, connectomics]
---

# Harnessing Cortical Geometry, Wiring, and Function as Inductive Biases for RNNs

## Overview

Biologically grounded recurrent neural networks using cortical geometry, anatomical wiring, and functional relationships from MICrONS connectomics data to achieve superior learning performance on cognitive tasks.

**arXiv**: 2606.14975  
**Authors**: Mo Shakiba, Rana Rokni, Mohammad Mohammadi, Nima Dehghani  
**Published**: June 12, 2026  
**Categories**: cs.NE, cs.AI, cs.LG, physics.data-an, q-bio.NC

## Core Innovation

Demonstrates that **neuronal constraints** (geometry, wiring, function) as inductive biases:
- Improve RNN learning performance across cognitive tasks
- Develop low-entropy, modular, small-world organization
- Retain strong performance with positive-only weights
- Converge toward biological organizational principles

## Key Methodology

### 1. Data Source: MICrONS Program
- **~12,000 co-registered excitatory neurons**
- Dense calcium imaging + electron microscopy reconstruction
- Mouse visual cortex multiple areas
- Same animal functional-connectomics mapping

### 2. Biological Constraints
- **Spatial coordinates**: Neuron positions in cortex
- **Anatomical connectivity**: EM-derived wiring
- **Functional relationships**: Calcium imaging-derived correlations

### 3. Three Constraint Types
1. **Functional weight initialization**: Largest performance gain
2. **Spatial embedding constraints**: Robust additional improvements
3. **Communication-aware constraints**: Distance-based message passing

## Architecture Design

### Biological Grounding
```python
class CorticallyConstrainedRNN:
    def __init__(self, microns_data):
        # Extract biological priors
        self.neuron_positions = microns_data.spatial_coords  # 12k neurons
        self.anatomical_wiring = microns_data.em_connectivity
        self.functional_corr = microns_data.ca_imaging_correlations
        
        # Initialize with functional weights
        self.rnn_weights = self.functional_weight_init()
        
        # Apply spatial constraints
        self.spatial_constraint = self.compute_distance_penalty()
```

### Weight Initialization
- **Functional**: Calcium correlation-based initialization
- **Anatomical**: EM connectivity as structural prior
- **Combined**: Hybrid functional + structural

### Spatial Constraints
- Communication-aware distance penalty
- Local wiring preference (biological)
- 3D cortical geometry embedding

## Key Results

### Performance Gains
- **Functional initialization**: Largest improvement
- **Spatial embedding**: Robust across conditions
- **Combined**: Best overall performance
- **Positive weights**: Strong even without negative weights

### Structural Organization
Biologically grounded networks develop:
- **Low entropy**: More organized representations
- **Modular architecture**: Functional modules
- **Small-world topology**: Efficient connectivity
- **Biological convergence**: Match cortical principles

### Task Performance
Evaluated on **three cognitive decision-making tasks**:
- Baseline RNNs: Standard performance
- Partially constrained: Moderate improvement
- **Fully constrained: Superior performance**

## Implementation Patterns

### 1. Functional Weight Initialization
```python
def functional_weight_init(ca_correlations, threshold=0.1):
    """
    Initialize RNN weights from calcium imaging correlations.
    
    Args:
        ca_correlations: Functional correlations from calcium imaging
        threshold: Minimum correlation for connection
    
    Returns:
        Initialized weight matrix
    """
    # Normalize correlations
    weights = (ca_correlations - ca_correlations.mean()) / ca_correlations.std()
    
    # Threshold for connectivity
    weights = weights * (weights > threshold)
    
    return weights
```

### 2. Spatial Constraint Layer
```python
def spatial_distance_penalty(positions, communication_radius):
    """
    Apply distance-based communication constraints.
    
    Args:
        positions: 3D coordinates of neurons
        communication_radius: Max distance for communication
    
    Returns:
        Distance penalty matrix
    """
    distances = torch.cdist(positions, positions)
    penalty = torch.exp(-distances / communication_radius)
    return penalty
```

### 3. Training with Constraints
```python
def constrained_training_step(model, batch, spatial_penalty):
    output, hidden = model(batch)
    loss = task_loss(output, batch.target)
    
    # Add spatial constraint
    constraint_loss = torch.mean(model.rnn_weights * spatial_penalty)
    total_loss = loss + constraint_loss
    
    return total_loss
```

## Why This Matters

### Neuroscience Impact
1. **Biological validation**: Constraints match cortical structure
2. **Organizational convergence**: Networks develop biological features
3. **Connectomics utility**: MICrONS as computational resource

### Machine Learning Impact
1. **Inductive bias power**: Biological constraints improve learning
2. **Structure → function**: Wiring shapes computation
3. **Positive weights work**: Excitatory-only networks effective

## Applications

### When to Use
- Building biologically plausible neural networks
- Understanding cortical computation mechanisms
- Improving RNN performance via structural priors
- Connectomics-informed architecture design
- Neuromorphic hardware design

### Trigger Words
- cortical geometry RNN
- MICrONS connectomics
- biological inductive bias
- functional weight initialization
- spatial neural constraints
- neuron wiring constraints

## Experimental Insights

### Constraint Ranking
1. **Functional weights**: Largest gain (most important)
2. **Spatial embedding**: Additional robust improvement
3. **Combined**: Best performance

### Architectural Features
- Modular organization emerges naturally
- Small-world topology from constraints
- Low entropy in hidden representations
- Positive-weight recurrence viable

## Related Skills

- `connectome-constrained-neural-network` — CCNN methodology
- `cortico-cerebellar-modular-rnn` — Cortico-cerebellar RNNs
- `cortical-microcircuit-information-flux` — Information flux optimization
- `functional-whole-brain-models` — Whole-brain functional models

## References

- Shakiba et al. (2026) arXiv:2606.14975
- MICrONS Program: Bock et al. (2011)
- Functional connectomics: Lee et al. (2016)
- Biological RNNs: Dehghani et al. (2020)

## Pitfalls

- Requires MICrONS-scale connectomics data
- Functional initialization most critical
- Spatial constraints require 3D coordinates
- Performance varies by task type
- Mouse cortex data; human may differ