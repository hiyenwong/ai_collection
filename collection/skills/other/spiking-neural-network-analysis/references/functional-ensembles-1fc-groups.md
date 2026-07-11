# Functional Ensembles as Units of Computation in Deep Spiking Networks

**arXiv ID**: 2606.00073  
**Source**: Deep Spiking Neural Networks paper (June 2026)  
**Added**: 2026-06-05

## Overview

This reference documents the **1FC (First-order Functional Connectivity) groups** framework from the paper "Functional Ensembles as Units of Computation in Deep Spiking Networks", introducing a new theoretical lens for understanding computational units in deep SNNs through functional connectivity analysis.

## Core Innovation: 1FC Groups

**Definition**: A group of neurons in a layer that all share statistically significant pairwise correlation with a neuron in the subsequent layer.

**Key Insight**: Traditional layer-based SNN analysis misses functional groupings. 1FC groups reveal hidden computational structure through inter-layer functional connectivity.

### Methodology

```python
# Identify 1FC groups
def identify_1fc_groups(layer_neurons, next_layer_neurons, threshold=0.05):
    """
    1FC Group Detection Algorithm
    
    For each neuron in next layer:
    1. Compute pairwise correlations with all neurons in current layer
    2. Identify neurons with statistically significant correlation (p < threshold)
    3. Group these neurons as an 1FC ensemble
    
    Returns: Dict mapping next_layer neuron ID → 1FC group neuron IDs
    """
    1fc_groups = {}
    for next_neuron in next_layer_neurons:
        correlated_neurons = []
        for neuron in layer_neurons:
            corr, p_value = compute_correlation(neuron, next_neuron)
            if p_value < threshold:
                correlated_neurons.append(neuron.id)
        if correlated_neurons:
            1fc_groups[next_neuron.id] = correlated_neurons
    return 1fc_groups
```

### Statistical Significance Testing

- Pearson correlation coefficient between spike trains
- Hypothesis test: H0 = no correlation (corr = 0)
- Significance threshold: p-value < 0.05 (adjustable)
- Multiple comparison correction: Bonferroni or FDR

## Computational Significance

### Function vs Layer Organization

| Aspect | Layer-based View | 1FC Group View |
|--------|------------------|----------------|
| Structure | Fixed architecture | Dynamic functional clustering |
| Connections | All-to-all (dense) | Selective functional pathways |
| Information Flow | Parallel broadcast | Targeted ensemble communication |
| Interpretability | Low (black box) | High (functional role identified) |

### Biological Motivation

- **Neural assemblies in cortex**: Functionally correlated neuron groups
- **Synaptic efficacy**: Stronger functional connectivity → specialized processing
- **Energy efficiency**: Sparse activation of relevant ensembles vs full-layer activation

## Experimental Findings

### Architecture Tested

- Deep SNN with 5+ layers
- Surrogate gradient training (SpikeProp, BP-with-threshold)
- Classification tasks (image recognition, event-based vision)

### 1FC Group Properties

1. **Sparse Activation**: Only subset of groups active per stimulus
2. **Functional Specialization**: Different groups respond to different input features
3. **Hierarchical Composition**: 1FC groups in early layers → more abstract groups in deep layers
4. **Stability**: Groups persist across training epochs (once converged)

## Applications in SNN Analysis

### Use Case 1: Network Debugging

```
Problem: SNN classification accuracy drops on specific inputs
Solution: 
1. Identify 1FC groups responding to problematic inputs
2. Check if specific groups are under-active/over-active
3. Trace functional pathway back to input layer
4. Adjust training to strengthen/ weaken specific groups
```

### Use Case 2: Architecture Optimization

```
Goal: Reduce SNN size while maintaining performance
Method:
1. Identify all 1FC groups across layers
2. Find redundant groups (similar activation patterns)
3. Merge redundant groups → prune unnecessary neurons
4. Re-train with sparsity constraint on group membership
```

### Use Case 3: Transfer Learning

```
Scenario: Pre-trained SNN on task A → adapt to task B
Approach:
1. Extract 1FC group structure from task A
2. Identify groups relevant for task B (functional similarity)
3. Freeze task-A-specific groups
4. Train only task-B-specific groups with new data
```

## Integration with SNN Analysis Pipeline

### Step 1: Data Collection

```python
# Record spike trains during inference
spike_data = {
    'layer_1': {'neuron_0': [0, 0.5, 1.2, ...], 'neuron_1': [...]},
    'layer_2': {'neuron_0': [0.1, 0.8, ...], ...},
    ...
}
```

### Step 2: Correlation Matrix

```python
import numpy as np
from scipy.stats import pearsonr

# Compute inter-layer correlation
def compute_inter_layer_corr(layer1_spikes, layer2_spikes):
    """
    Returns: correlation_matrix[layer1_neuron][layer2_neuron]
    """
    n1 = len(layer1_spikes)
    n2 = len(layer2_spikes)
    corr_matrix = np.zeros((n1, n2))
    p_matrix = np.zeros((n1, n2))
    
    for i, sp1 in enumerate(layer1_spikes.values()):
        for j, sp2 in enumerate(layer2_spikes.values()):
            corr, p = pearsonr(sp1, sp2)
            corr_matrix[i, j] = corr
            p_matrix[i, j] = p
    
    return corr_matrix, p_matrix
```

### Step 3: Group Extraction

```python
# Threshold significance matrix
significant_corr = p_matrix < 0.05

# Extract 1FC groups
for j, next_neuron in enumerate(layer2_spikes.keys()):
    1fc_group = [neuron_i for neuron_i in range(n1) 
                 if significant_corr[neuron_i, j]]
    # Store group membership
```

## Comparison with Other SNN Analysis Methods

| Method | Focus | Scale | Interpretability |
|--------|-------|-------|------------------|
| **1FC Groups** | Functional connectivity | Layer-to-layer | High |
| **Neuron Receptive Fields** | Input sensitivity | Single neuron | Medium |
| **Weight Visualization** | Synaptic strength | Connection-level | Low |
| **Layer Activation Statistics** | Population dynamics | Layer-level | Low |

## Limitations & Pitfalls

1. **Correlation ≠ Causation**: Functional correlation doesn't prove computational role
2. **Temporal Window**: Correlation depends on time window size (experiment design)
3. **Noise Sensitivity**: Noisy spike trains → spurious correlations
4. **Static Analysis**: 1FC groups identified post-training; dynamic during training?

## Future Research Directions

- **Higher-order FC groups**: 2FC (groups-of-groups)?
- **Temporal 1FC**: Track group evolution across training epochs
- **Cross-layer 1FC**: Groups spanning multiple layers
- **Task-specific 1FC**: Compare group structure across different tasks

## References

- Paper: arXiv 2606.00073 (June 2026)
- Skill: `functional-ensembles-deep-spiking-networks` (ai_collection)
- Obsidian: `2505.21-functional-ensembles-deep-spiking-networks.md`
- KG Entity: `arxiv_2606.00073`

## Related SNN Concepts

- **Winner-Take-All (WTA)**: Competitive activation (connects to group sparsity)
- **STDP**: Synaptic plasticity (shapes functional connectivity)
- **Neural Manifold**: Population dynamics (alternative to layer-based view)
- **Energy-based Models**: Hopfield networks (functional ensemble = attractor basin)