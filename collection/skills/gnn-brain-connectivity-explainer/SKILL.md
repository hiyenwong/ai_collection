# SKILL.md - GNN Brain Connectivity with GNNExplainer

## Activation Keywords

- GNN brain connectivity, GNNExplainer, graph neural network EEG
- brain connectivity prediction, explainable GNN, EEG classification
- task-dependent connectivity, schizophrenia detection, mental disorder prediction

## What It Does

Provides a GNN-based framework for analyzing brain connectivity from EEG data, with GNNExplainer for interpretability. Enables: 1) mental disorder prediction, 2) state differentiation (listening vs resting), 3) recognition of task-dependent connectivity patterns.

## When To Use

**Use this skill when:**
- Analyzing EEG/MEG data with graph methods
- Predicting mental disorders from brain connectivity
- Explaining GNN predictions on brain networks
- Detecting task-dependent connectivity changes
- Building interpretable brain network models

**Do NOT use for:**
- Non-graph EEG analysis (traditional signal processing)
- Classification without interpretability needs
- Static connectivity analysis (no temporal dynamics)

## How To Use

### Step-by-Step Workflow

1. **Construct Brain Graph from EEG**
   - Define nodes (electrodes or regions)
   - Compute connectivity edges (correlation, coherence)
   - Create node features (signal statistics, spectral features)

2. **Build GNN Model**
   - Graph convolution layers (GCN, GAT, GraphSAGE)
   - Pooling for graph-level predictions
   - Classification head for mental disorders

3. **Train GNN on EEG Data**
   - Input: graph with node features and edge weights
   - Output: classification (disorder, state, task)
   - Loss: cross-entropy with class weights

4. **Apply GNNExplainer**
   - Identify important nodes and edges
   - Generate explanations for predictions
   - Visualize task-dependent connectivity

5. **Validate and Interpret**
   - Cross-validation for accuracy
   - Compare explanations with known neuroscience
   - Extract biomarkers

### Key Components

| Component | Purpose | Implementation |
|-----------|---------|----------------|
| Graph construction | EEG → brain network | Correlation, PLV, coherence |
| GNN layers | Learn graph representations | GCN, GAT, GraphSAGE |
| Pooling | Graph-level predictions | Global mean/max pooling |
| GNNExplainer | Interpretability | Mask optimization |

### GNNExplainer Algorithm

GNNExplainer learns masks that maximize mutual information between predictions and graph structure:

```
maximize I(Y, (M_X ⊙ X, M_A ⊙ A))
```

Where:
- Y: prediction
- X: node features
- A: adjacency matrix
- M_X, M_A: learned masks

## Example Usage

### EEG Classification with GNN

**Problem:** Predict schizophrenia from EEG connectivity

**Implementation:**
```python
import torch
import torch.nn as nn
from torch_geometric.nn import GCNConv, global_mean_pool

class BrainConnectivityGNN(nn.Module):
    def __init__(self, node_features, hidden_dim=64, num_classes=2):
        super().__init__()
        
        self.conv1 = GCNConv(node_features, hidden_dim)
        self.conv2 = GCNConv(hidden_dim, hidden_dim)
        self.classifier = nn.Linear(hidden_dim, num_classes)
        
    def forward(self, x, edge_index, edge_weight=None, batch=None):
        # Graph convolution layers
        x = torch.relu(self.conv1(x, edge_index, edge_weight))
        x = torch.relu(self.conv2(x, edge_index, edge_weight))
        
        # Graph pooling
        if batch is None:
            batch = torch.zeros(x.size(0), dtype=torch.long)
        x = global_mean_pool(x, batch)
        
        # Classification
        return self.classifier(x)

def construct_brain_graph(eeg_data, method='correlation'):
    """
    Construct brain connectivity graph from EEG
    
    Parameters:
    -----------
    eeg_data : array (n_channels, n_timepoints)
        EEG recording
    method : str
        Connectivity measure
        
    Returns:
    --------
    node_features : array (n_channels, n_features)
    edge_index : array (2, n_edges)
    edge_weight : array (n_edges,)
    """
    n_channels = eeg_data.shape[0]
    
    # Node features: signal statistics
    node_features = np.column_stack([
        np.mean(eeg_data, axis=1),
        np.std(eeg_data, axis=1),
        np.max(eeg_data, axis=1) - np.min(eeg_data, axis=1)
    ])
    
    # Compute connectivity
    if method == 'correlation':
        connectivity = np.corrcoef(eeg_data)
    elif method == 'coherence':
        connectivity = compute_coherence(eeg_data)
    
    # Threshold and create edges
    threshold = np.percentile(np.abs(connectivity), 90)
    edges = np.where(np.abs(connectivity) > threshold)
    edge_index = np.array(edges)
    edge_weight = connectivity[edges]
    
    return node_features, edge_index, edge_weight
```

### GNNExplainer for Interpretability

**Analysis:**
```python
from torch_geometric.nn import GNNExplainer

def explain_brain_connectivity(model, graph, target_class=1):
    """
    Use GNNExplainer to identify important connectivity
    
    Parameters:
    -----------
    model : trained GNN model
    graph : tuple (x, edge_index, edge_weight)
    target_class : int
        Class to explain
        
    Returns:
    --------
    node_importance : array
    edge_importance : array
    """
    x, edge_index, edge_weight = graph
    
    # Initialize explainer
    explainer = GNNExplainer(model, epochs=100, lr=0.01)
    
    # Get explanation
    node_mask, edge_mask = explainer.explain_graph(
        x, edge_index, edge_weight, target=target_class
    )
    
    return node_mask, edge_mask

def visualize_explanation(node_mask, edge_mask, electrode_positions):
    """
    Visualize important connectivity
    """
    import matplotlib.pyplot as plt
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Plot electrodes
    ax.scatter(electrode_positions[:, 0], 
               electrode_positions[:, 1],
               c=node_mask, cmap='Reds', s=100)
    
    # Plot important edges
    for i, (src, dst) in enumerate(edge_index.T):
        if edge_mask[i] > 0.5:  # Threshold
            ax.plot([electrode_positions[src, 0], electrode_positions[dst, 0]],
                   [electrode_positions[src, 1], electrode_positions[dst, 1]],
                   'r-', alpha=edge_mask[i], linewidth=2)
    
    plt.title('Important Connectivity for Prediction')
    return fig
```

### Task-Dependent Connectivity Detection

**Analysis:**
```python
def detect_task_connectivity(resting_graphs, task_graphs, model):
    """
    Detect connectivity differences between states
    """
    # Get explanations for each state
    resting_masks = []
    for graph in resting_graphs:
        _, edge_mask = explain_brain_connectivity(model, graph)
        resting_masks.append(edge_mask)
    
    task_masks = []
    for graph in task_graphs:
        _, edge_mask = explain_brain_connectivity(model, graph)
        task_masks.append(edge_mask)
    
    # Compare
    resting_avg = np.mean(resting_masks, axis=0)
    task_avg = np.mean(task_masks, axis=0)
    
    diff = task_avg - resting_avg
    
    # Identify task-specific connections
    task_specific = np.where(diff > 0.2)[0]
    
    return task_specific, diff
```

## Key Advantages

| Advantage | Benefit |
|-----------|---------|
| Graph representation | Natural brain connectivity modeling |
| End-to-end learning | No manual feature engineering |
| Interpretability | GNNExplainer provides explanations |
| Multiple tasks | Disorder prediction, state detection |

## Related Skills

- **explainable-gnn-eeg-neurological** - Explainable GNN for EEG
- **eeg-brain-connectivity-bci** - EEG connectivity BCI
- **multimodal-brain-connectivity-gnn** - Multimodal GNN

## Source

- arXiv:2206.01930v1
- Title: Investigating Brain Connectivity with Graph Neural Networks and GNNExplainer
- Utility: 0.87
- Authors: (from arxiv)
- Published: IEEE Transactions on Signal Processing

## Notes

- Key innovation: GNN + GNNExplainer for EEG analysis
- Applications: schizophrenia detection, state classification
- Enables explainable predictions on brain networks
- Published in IEEE TSP
- Three capabilities: disorder prediction, state differentiation, task recognition

---

_Created: 2026-04-01_