---
name: self-supervised-neural-circuit-discovery-with-gnn
description: **Source:** arXiv:2509.17174 (NeurIPS 2025)
---

# Self-Supervised Neural Circuit Discovery with GNN

**Source:** arXiv:2509.17174 (NeurIPS 2025)
**Utility:** 0.95
**Created:** 2026-03-25

## Activation Keywords

- neural circuit discovery
- synaptic connectivity inference
- GNN neural inference
- latent connectivity
- self-supervised neural structure
- ring attractor connectivity

## Description

A graph-based neural inference model that simultaneously predicts neural activity and infers latent connectivity by modeling neurons as interacting nodes in a graph, using self-supervised structure learning.

## Core Methodology

### 1. Problem: Connectivity Inference Challenges

- **Partial observability** - Not all neurons are recorded
- **Model-dynamics mismatch** - Inference models may not match true circuit dynamics
- **Spurious correlations** - Observed correlations may not reflect true connectivity

### 2. Architecture: Dual-Module GNN

**Module 1: Structural Connectivity Learning**
- Learns latent synaptic weights between neurons
- Handles unobserved neurons through auxiliary nodes

**Module 2: Spike Prediction GNN**
- Predicts future spiking activity
- Uses learned connectivity as graph structure

### 3. Self-Supervised Learning

**Training Signal:** Spike prediction task

**Key Insight:** By forcing the model to predict future activity, it must learn true connectivity (not just correlations)

### 4. Evaluation

**Synthetic Data:** Ring attractor network models
- Varying recurrent connectivity
- Varying external inputs
- Incomplete observations

**Real Data:** Head direction cells in mice
- Inferred connectivity aligns with continuous attractor model predictions

## Implementation Framework

```python
# Conceptual architecture
class NeuralCircuitGNN:
    def __init__(self, n_observed, n_auxiliary):
        # Module 1: Structure learning
        self.connectivity_encoder = ConnectivityLearner(
            observed_nodes=n_observed,
            auxiliary_nodes=n_auxiliary
        )
        
        # Module 2: Spike prediction
        self.spike_predictor = SpikePredictionGNN()
    
    def forward(self, spike_history):
        # Learn/encode connectivity
        adjacency = self.connectivity_encoder(spike_history)
        
        # Predict future spikes using learned connectivity
        future_spikes = self.spike_predictor(
            spike_history, 
            graph_structure=adjacency
        )
        
        return future_spikes, adjacency
    
    def loss(self, predicted, actual, adjacency):
        # Self-supervised: spike prediction loss
        prediction_loss = spike_prediction_loss(predicted, actual)
        
        # Optional: regularization on connectivity
        structure_reg = connectivity_regularization(adjacency)
        
        return prediction_loss + structure_reg
```

## Key Innovations

1. **Auxiliary Nodes** - Handle unobserved neurons in partially observed circuits
2. **Joint Learning** - Connectivity and dynamics learned together
3. **Self-Supervised** - No need for ground truth connectivity labels
4. **Generalization** - Works on both synthetic and real neural data

## Applications

1. **Connectivity Inference**
   - Infer synaptic weights from calcium imaging / electrophysiology
   - Handle partial observations in real experiments

2. **Circuit Model Validation**
   - Compare inferred connectivity to theoretical predictions
   - Validate continuous attractor models

3. **Neural System Analysis**
   - Head direction system
   - Ring attractors
   - Other recurrent circuits

## When to Use

- Inferring connectivity from population recordings
- Working with partially observed neural populations
- Validating circuit models against real data
- Need self-supervised approach (no ground truth connectivity)

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: Auxiliary Nodes

### Step 2: Joint Learning

### Step 3: Self-Supervised

### Step 4: Generalization

### Step 5: Connectivity Inference

### When to Apply
- Inferring connectivity from population recordings
- Working with partially observed neural populations
- Validating circuit models against real data

## Examples

### Example 1: Basic Application

**User:** I need to apply Self-Supervised Neural Circuit Discovery with GNN to my analysis.

**Agent:** I'll help you apply self-supervised-neural-circuit-gnn. First, let me understand your specific use case...

**Context:** Problem: Connectivity Inference Challenges

### Example 2: Advanced Scenario

**User:** Inferring connectivity from population recordings

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for self-supervised-neural-circuit-gnn?

**Agent:** Let me search for the latest research and best practices...

## Related Skills

- `gnn-transformer-fusion` - GNN architectures for neural data
- `time-varying-brain-connectivity` - Dynamic connectivity analysis
- `geometry-aware-spiking-gnn` - Spiking GNN models

## References

- Yoon, K., et al. "Self-Supervised Discovery of Neural Circuits in Spatially Patterned Neural Responses with Graph Neural Networks." NeurIPS 2025.
- Ring attractor network models
- Continuous attractor neural networks