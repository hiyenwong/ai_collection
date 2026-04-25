---
name: group-intervention-causal-discovery-subsystems
description: "Group intervention-based causal discovery for identifying causal subsystems in deep neural networks and complex systems. Uses targeted perturbations to reveal causal structure within learned representations. Activation: causal discovery, group intervention, causal subsystem, deep network, causal structure learning, interventional data, representation analysis, do-calculus."
---

# gCDMI: Group Interventions on Deep Networks for Causal Discovery

> Discover causal subsystems within deep neural networks by applying group interventions (targeted perturbations) and measuring information flow changes, revealing the causal structure of learned representations.

## Metadata
- **Source**: arXiv:2510.23906
- **Authors**: Wasim Ahmad, Jan Bím, Sebastian Weichwald, Giuseppe Jurman, Cesare Furlanello, Jonas Peters, Moritz Grosse-Wentrup
- **Published**: 2025-10-27

## Core Methodology

### Key Innovation
gCDMI (group Conditional Dependence Measure via Interventions) performs **causal discovery within deep neural networks** by systematically applying group interventions — perturbing subsets of neurons and measuring conditional dependence changes in downstream representations. This reveals causal subsystems: groups of neurons that causally influence specific output functions, going beyond correlation-based feature attribution.

### Problem Addressed
- Understanding what deep networks learn requires knowing causal (not just correlational) relationships between neurons
- Individual neuron perturbations are insufficient — causal effects often emerge at the group level
- Existing methods (e.g., activation patching) test single directions, missing multi-neuron causal pathways
- No principled framework for discovering causal subsystems from interventional data in neural networks

### Technical Framework
1. **Define neuron groups**: Partition network layers into candidate groups (by function, region, or clustering)
2. **Perform group interventions**: Apply do-interventions (set group activations to fixed values, noise, or counterfactuals)
3. **Measure conditional dependence**: Compute gCDMI = conditional mutual information between intervened group and output, given non-intervened groups
4. **Discover causal subsystems**: Groups with high gCDMI form causal subsystems that drive specific network behaviors
5. **Validate**: Test discovered subsystems on held-out data and compare with known neurobiological structure (if applicable)

## Implementation Guide

### Prerequisites
- Trained deep neural network (any architecture)
- Python: `torch`, `numpy`, `sklearn`
- Test dataset for intervention experiments

### Step-by-Step
1. **Extract activations**: Record intermediate representations for test inputs
2. **Define intervention groups**: Cluster neurons by correlation, spatial proximity, or task relevance
3. **Apply interventions**: For each group, replace activations with mean/noise/counterfactual
4. **Compute gCDMI**: Measure how output changes conditionally depend on the intervention
5. **Build causal graph**: Connect groups with significant causal influence

### Code Example
```python
import torch
import numpy as np
from sklearn.metrics import mutual_info_score

def group_intervention(model, x, layer_name, group_indices, intervention_value='mean'):
    """Apply do-intervention on a neuron group.
    
    Args:
        model: neural network
        x: input data
        layer_name: target layer for intervention
        group_indices: indices of neurons to intervene on
        intervention_value: 'mean', 'zero', or specific tensor
    Returns:
        output with intervention applied
    """
    hooks = []
    activations = {}
    
    def get_hook(name):
        def hook(module, input, output):
            activations[name] = output.clone()
            if name == layer_name and intervention_value == 'zero':
                output[:, group_indices] = 0
            elif name == layer_name and intervention_value == 'mean':
                output[:, group_indices] = output[:, group_indices].mean(dim=0)
        return hook
    
    for name, module in model.named_modules():
        if isinstance(module, torch.nn.Linear):
            hooks.append(module.register_forward_hook(get_hook(name)))
    
    with torch.no_grad():
        output_intervened = model(x)
    
    for h in hooks:
        h.remove()
    
    return output_intervened, activations

def compute_gcdmi(model, x, layer_name, group_a, group_b, n_bins=20):
    """Compute group Conditional Dependence Measure via Interventions.
    
    Measures causal influence of group_a on output, conditional on group_b.
    """
    # Baseline output
    with torch.no_grad():
        y_baseline = model(x).argmax(dim=-1).numpy()
    
    # Intervene on group_a
    y_intervened, _ = group_intervention(model, x, layer_name, group_a, 'zero')
    y_intervened = y_intervened.argmax(dim=-1).numpy()
    
    # Intervene on group_b (for conditioning)
    y_cond, _ = group_intervention(model, x, layer_name, group_b, 'zero')
    y_cond = y_cond.argmax(dim=-1).numpy()
    
    # Compute conditional mutual information approximation
    delta = (y_baseline != y_intervened).astype(int)
    # gCDMI ≈ I(group_a; delta_output | group_b)
    gcdmi = mutual_info_score(y_cond, delta) if len(np.unique(delta)) > 1 else 0.0
    
    return gcdmi

def discover_causal_subsystems(model, x, layer_name, n_groups=10, group_size=20):
    """Discover causal subsystems via group interventions."""
    n_neurons = 256  # adjust to layer size
    
    # Create random groups (or use clustering)
    groups = [np.random.choice(n_neurons, group_size, replace=False) 
              for _ in range(n_groups)]
    
    causal_scores = {}
    for i, ga in enumerate(groups):
        for j, gb in enumerate(groups):
            if i != j:
                score = compute_gcdmi(model, x, layer_name, ga, gb)
                causal_scores[(i, j)] = score
    
    # Identify high-scoring causal subsystems
    threshold = np.percentile(list(causal_scores.values()), 90)
    subsystems = [k for k, v in causal_scores.items() if v > threshold]
    
    return subsystems, causal_scores
```

## Applications
- **Mechanistic interpretability**: Understanding causal computation in deep networks
- **Neuroscience-inspired AI**: Discovering modular causal structure analogous to brain subsystems
- **Feature attribution**: Causal (not correlational) attribution of network behaviors to neuron groups
- **Model debugging**: Identifying causal pathways responsible for errors or biases
- **Brain network analysis**: Applying group intervention framework to neural data

## Pitfalls
- Computationally expensive — O(n_groups²) intervention experiments
- Intervention design matters — poor groups may miss important causal pathways
- Conditional mutual information estimation requires sufficient samples
- Discrete output binning can lose information — use continuous estimators when possible

## Related Skills
- causal-brain-network-inference
- neural-encoding-evaluation-ground-truth
- brain-network-controllability
