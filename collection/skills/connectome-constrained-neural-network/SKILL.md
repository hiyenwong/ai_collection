---
name: connectome-constrained-neural-network
description: "Connectome-Constrained Neural Network (CCNN) methodology for brain-inspired AI. Integrates biological structural connectivity (connectome) into artificial neural network architectures to improve generalization and biological plausibility. Activation: connectome constraint, structural connectivity, brain-inspired architecture, connectome-based AI, wiring cost, brain network prior, diffusion MRI connectivity."
tags: ["connectome", "brain-networks", "structural-connectivity", "wiring-cost", "brain-inspired", "DWI", "diffusion-mri", "network-constraint"]
---

# Connectome-Constrained Neural Networks

## Overview

Connectome-Constrained Neural Networks (CCNNs) integrate biological brain connectivity patterns into artificial neural network architectures. The core insight is that the brain's wiring diagram (connectome) has been optimized through evolution for efficient computation, and these structural constraints can improve AI systems.

## Core Concepts

### Why Connectome Constraints?

```
Traditional Neural Network:
  - Fully connected or simple local patterns
  - No wiring cost consideration
  - Prone to overfitting
  - Biologically implausible

Connectome-Constrained Network:
  - Structured by biological connectivity
  - Wiring efficiency built-in
  - Better generalization
  - Biologically grounded
```

### Types of Connectome Constraints

1. **Structural Connectivity**: Physical wiring from diffusion MRI
2. **Functional Connectivity**: Correlation-based connections from fMRI/EEG
3. **Wiring Cost**: Metabolic/physical costs of connections
4. **Modular Organization**: Community structure of brain networks

## Implementation

### Loading Brain Connectome Data

```python
import numpy as np
import scipy.io as sio
from nilearn import datasets

def load_human_connectome(atlas='aal', n_regions=116):
    """
    Load human structural connectivity matrix.
    
    Args:
        atlas: 'aal', 'desikan', 'destrieux', 'harvard_oxford'
        n_regions: Number of brain regions
    
    Returns:
        connectivity: (n_regions, n_regions) connectivity matrix
        region_labels: List of region names
        coordinates: 3D coordinates of regions
    """
    # Fetch atlas
    if atlas == 'aal':
        atlas_data = datasets.fetch_atlas_aal()
    elif atlas == 'desikan':
        atlas_data = datasets.fetch_atlas_destrieux_2009()
    elif atlas == 'harvard_oxford':
        atlas_data = datasets.fetch_atlas_harvard_oxford('cort-maxprob-thr25-2mm')
    
    # Load or compute connectivity matrix
    # In practice, use pre-computed connectomes or compute from dMRI
    connectivity = load_diffusion_connectivity(atlas_data)
    
    return connectivity, atlas_data.labels, atlas_data.coordinates


def load_diffusion_connectivity(atlas_data, dataset='hcp'):
    """
    Load structural connectivity from diffusion MRI.
    
    Args:
        atlas_data: Atlas information
        dataset: 'hcp', 'ukb' (Human Connectome Project, UK Biobank)
    
    Returns:
        SC: Structural connectivity matrix (streamline counts)
    """
    # HCP minimally preprocessed connectomes
    if dataset == 'hcp':
        # Load from HCP dataset
        SC = fetch_hcp_connectome(atlas_data)
    
    # Normalize and threshold
    SC = SC / SC.max()  # Normalize to [0, 1]
    SC[SC < 0.01] = 0   # Threshold weak connections
    
    return SC
```

### Connectome-Constrained Layer

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class ConnectomeLinear(nn.Module):
    """
    Linear layer with connectome-inspired sparse connectivity.
    
    Implements constrained weight matrix where connections follow
    biological connectivity patterns.
    """
    
    def __init__(self, in_features, out_features, connectivity_matrix,
                 constraint_type='hard', sparsity_target=0.1):
        """
        Args:
            in_features: Input dimension
            out_features: Output dimension
            connectivity_matrix: Binary or weighted connectivity (n_out, n_in)
            constraint_type: 'hard' (fixed), 'soft' (regularized), 'init' (initialization only)
            sparsity_target: Target connection density
        """
        super().__init__()
        
        self.in_features = in_features
        self.out_features = out_features
        self.constraint_type = constraint_type
        
        # Register connectivity as buffer (non-trainable)
        if connectivity_matrix is not None:
            # Resize connectivity to match layer dimensions if needed
            connectivity = self._resize_connectivity(
                connectivity_matrix, 
                (out_features, in_features)
            )
            self.register_buffer('connectivity_mask', 
                               torch.tensor(connectivity, dtype=torch.float32))
        else:
            # Random sparse connectivity
            self.connectivity_mask = torch.rand(out_features, in_features) < sparsity_target
            self.connectivity_mask = self.connectivity_mask.float()
        
        # Learnable parameters (only for existing connections in hard mode)
        if constraint_type == 'hard':
            # Count actual connections
            n_connections = int(self.connectivity_mask.sum().item())
            self.weight_values = nn.Parameter(torch.randn(n_connections) * 0.01)
            self.register_buffer('weight_indices', self._create_sparse_indices())
        else:
            self.weight = nn.Parameter(torch.randn(out_features, in_features) * 0.01)
        
        self.bias = nn.Parameter(torch.zeros(out_features))
        
        # Wiring cost regularization (for soft constraint)
        if constraint_type == 'soft':
            # Distance-based wiring cost from 3D coordinates
            self.wiring_cost = self._compute_wiring_cost()
        
    def _resize_connectivity(self, connectivity, target_shape):
        """Resize connectivity matrix to match layer dimensions."""
        from scipy.ndimage import zoom
        
        if connectivity.shape == target_shape:
            return connectivity
        
        # Use interpolation for resizing
        zoom_factors = (target_shape[0] / connectivity.shape[0],
                       target_shape[1] / connectivity.shape[1])
        resized = zoom(connectivity, zoom_factors, order=1)
        
        # Binarize based on threshold
        return (resized > np.percentile(resized, 90)).astype(float)
    
    def _create_sparse_indices(self):
        """Create indices for sparse weight representation."""
        rows, cols = torch.where(self.connectivity_mask > 0)
        return torch.stack([rows, cols], dim=0)
    
    def _compute_wiring_cost(self, coordinates=None):
        """Compute wiring cost based on 3D distance between regions."""
        if coordinates is None:
            # Use random coordinates as placeholder
            coords_out = torch.randn(self.out_features, 3)
            coords_in = torch.randn(self.in_features, 3)
        else:
            coords_out = coordinates[:self.out_features]
            coords_in = coordinates[:self.in_features]
        
        # Pairwise distances
        distances = torch.cdist(coords_out, coords_in)
        return distances / distances.max()
    
    def forward(self, x):
        if self.constraint_type == 'hard':
            # Build sparse weight matrix
            weight = torch.zeros(self.out_features, self.in_features, 
                               device=x.device)
            weight[self.weight_indices[0], self.weight_indices[1]] = self.weight_values
        else:
            weight = self.weight
            
            if self.constraint_type == 'soft':
                # Apply soft connectivity constraint
                # Weights encouraged to follow connectivity pattern
                weight = weight * (0.5 + 0.5 * self.connectivity_mask)
                
            elif self.constraint_type == 'init':
                # Only use connectivity for initialization
                pass
        
        return F.linear(x, weight, self.bias)
    
    def get_wiring_cost_loss(self, lambda_wiring=0.001):
        """Compute wiring cost regularization loss."""
        if self.constraint_type != 'soft':
            return 0.0
        
        # Penalize connections proportional to distance
        cost = (self.weight.abs() * self.wiring_cost.to(self.weight.device)).sum()
        return lambda_wiring * cost
    
    def extra_repr(self):
        return (f'in_features={self.in_features}, '
                f'out_features={self.out_features}, '
                f'constraint_type={self.constraint_type}, '
                f'connection_density={self.connectivity_mask.mean():.3f}')
```

### Full Connectome-Constrained Network

```python
class ConnectomeConstrainedNN(nn.Module):
    """
    Full neural network with connectome constraints at multiple layers.
    
    Architecture inspired by cortical hierarchy:
    - Early layers: Sensory-like (local connectivity)
    - Middle layers: Association (long-range connectivity)
    - Late layers: Output (task-specific)
    """
    
    def __init__(self, input_dim, output_dim, hidden_dims=[512, 256, 128],
                 connectome_data=None, constraint_layers=[1, 2]):
        """
        Args:
            input_dim: Input feature dimension
            output_dim: Output dimension (classes)
            hidden_dims: List of hidden layer dimensions
            connectome_data: Dictionary with connectivity matrices
            constraint_layers: Which layers to apply connectome constraints
        """
        super().__init__()
        
        self.layers = nn.ModuleList()
        dims = [input_dim] + hidden_dims + [output_dim]
        
        for i in range(len(dims) - 1):
            if i in constraint_layers and connectome_data is not None:
                # Use connectome-constrained layer
                layer = ConnectomeLinear(
                    dims[i], dims[i+1],
                    connectivity_matrix=connectome_data.get(f'layer_{i}'),
                    constraint_type='soft'
                )
            else:
                # Standard linear layer
                layer = nn.Linear(dims[i], dims[i+1])
            
            self.layers.append(layer)
            
            # Add activation (except for last layer)
            if i < len(dims) - 2:
                self.layers.append(nn.ReLU())
                self.layers.append(nn.Dropout(0.3))
    
    def forward(self, x):
        for layer in self.layers:
            x = layer(x)
        return x
    
    def get_wiring_cost(self):
        """Total wiring cost across all constrained layers."""
        total_cost = 0.0
        for layer in self.layers:
            if isinstance(layer, ConnectomeLinear):
                total_cost += layer.get_wiring_cost_loss()
        return total_cost
```

## Connectome-Based Graph Neural Networks

```python
import torch_geometric as pyg
from torch_geometric.nn import GCNConv, GATConv

class ConnectomeGNN(nn.Module):
    """
    Graph Neural Network using brain connectome as graph structure.
    
    Nodes = Brain regions
    Edges = Structural connectivity
    Node features = Neural activity or ROI features
    """
    
    def __init__(self, n_regions, feature_dim, hidden_dim=64, output_dim=10,
                 connectome_edge_index=None, connectome_weights=None):
        """
        Args:
            n_regions: Number of brain regions (nodes)
            feature_dim: Dimension of node features
            hidden_dim: Hidden layer dimension
            output_dim: Output classes
            connectome_edge_index: (2, n_edges) connectivity
            connectome_weights: Edge weights from connectome
        """
        super().__init__()
        
        self.n_regions = n_regions
        
        # Create edge index from connectome if not provided
        if connectome_edge_index is None:
            self.edge_index = self._connectome_to_edges(n_regions)
        else:
            self.register_buffer('edge_index', connectome_edge_index)
        
        # Edge weights (connection strengths)
        if connectome_weights is not None:
            self.register_buffer('edge_weights', connectome_weights)
        else:
            self.edge_weights = None
        
        # GNN layers
        self.conv1 = GCNConv(feature_dim, hidden_dim)
        self.conv2 = GCNConv(hidden_dim, hidden_dim)
        self.conv3 = GCNConv(hidden_dim, hidden_dim)
        
        # Global pooling and output
        self.global_pool = nn.AdaptiveAvgPool1d(1)
        self.classifier = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.ReLU(),
            nn.Linear(hidden_dim // 2, output_dim)
        )
    
    def _connectome_to_edges(self, connectome_matrix):
        """Convert connectivity matrix to edge index format."""
        rows, cols = np.where(connectome_matrix > 0)
        edge_index = torch.tensor(np.stack([rows, cols]), dtype=torch.long)
        return edge_index
    
    def forward(self, x, batch=None):
        """
        Args:
            x: (n_nodes, feature_dim) or (batch, n_nodes, feature_dim)
            batch: Batch assignment for nodes
        """
        # Graph convolution layers
        x = self.conv1(x, self.edge_index, self.edge_weights)
        x = F.relu(x)
        x = F.dropout(x, p=0.3, training=self.training)
        
        x = self.conv2(x, self.edge_index, self.edge_weights)
        x = F.relu(x)
        
        x = self.conv3(x, self.edge_index, self.edge_weights)
        
        # Global pooling over regions
        if batch is None:
            # Single graph
            x = x.mean(dim=0)  # (hidden_dim,)
        else:
            # Batch of graphs
            x = pyg.nn.global_mean_pool(x, batch)
        
        # Classification
        out = self.classifier(x)
        return out
```

## Wiring Cost Optimization

```python
class WiringCostOptimizer:
    """
    Optimize network connectivity for minimal wiring cost
    while maintaining performance.
    """
    
    def __init__(self, network, coordinates, lambda_wiring=0.001):
        """
        Args:
            network: Neural network to optimize
            coordinates: 3D coordinates of neurons/regions
            lambda_wiring: Weight of wiring cost in loss
        """
        self.network = network
        self.coordinates = coordinates
        self.lambda_wiring = lambda_wiring
        self.distances = self._compute_all_distances()
    
    def _compute_all_distances(self):
        """Compute pairwise distances between all neurons."""
        coords = torch.tensor(self.coordinates)
        return torch.cdist(coords, coords)
    
    def compute_wiring_loss(self):
        """
        Compute total wiring cost as weighted sum of connection distances.
        """
        total_cost = 0.0
        
        for layer in self.network.modules():
            if isinstance(layer, nn.Linear):
                weights = layer.weight.abs()
                
                # Sample distance matrix to match layer dimensions
                n_out, n_in = weights.shape
                dist_sample = self._sample_distances(n_out, n_in)
                
                # Wiring cost = sum of (weight * distance)
                cost = (weights * dist_sample.to(weights.device)).sum()
                total_cost += cost
        
        return self.lambda_wiring * total_cost
    
    def _sample_distances(self, n_out, n_in):
        """Sample distance matrix to match layer size."""
        # Random sampling with replacement
        indices_out = torch.randint(0, len(self.coordinates), (n_out,))
        indices_in = torch.randint(0, len(self.coordinates), (n_in,))
        return self.distances[indices_out][:, indices_in]
    
    def prune_by_wiring_cost(self, pruning_ratio=0.3):
        """
        Prune connections with highest wiring cost.
        
        Returns:
            pruned_network: Network with pruned connections
        """
        pruned_network = copy.deepcopy(self.network)
        
        for layer in pruned_network.modules():
            if isinstance(layer, nn.Linear):
                weights = layer.weight.data
                n_out, n_in = weights.shape
                
                # Get distances for this layer
                dist_sample = self._sample_distances(n_out, n_in)
                
                # Compute cost per connection
                costs = weights.abs() * dist_sample
                
                # Find threshold for pruning
                threshold = torch.quantile(costs.flatten(), 1 - pruning_ratio)
                
                # Prune high-cost connections
                mask = costs < threshold
                weights *= mask.float().to(weights.device)
        
        return pruned_network
```

## Applications

### 1. Brain Age Prediction

```python
def brain_age_prediction(connectomes, ages, train_idx, test_idx):
    """
    Predict biological age from structural connectome.
    
    Uses connectome-constrained GNN to learn age-related connectivity changes.
    """
    # Prepare data
    data = prepare_connectome_data(connectomes, ages)
    
    # Create connectome-constrained model
    model = ConnectomeGNN(
        n_regions=connectomes.shape[1],
        feature_dim=connectomes.shape[0],  # Use connectivity as features
        hidden_dim=128,
        output_dim=1,  # Regression for age
        connectome_edge_index=data.edge_index,
        connectome_weights=data.edge_weights
    )
    
    # Training
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    criterion = nn.MSELoss()
    
    for epoch in range(100):
        model.train()
        optimizer.zero_grad()
        
        pred = model(data.x, data.batch)
        loss = criterion(pred[train_idx], data.y[train_idx])
        
        loss.backward()
        optimizer.step()
    
    # Evaluation
    model.eval()
    with torch.no_grad():
        pred_age = model(data.x, data.batch)
        mae = (pred_age[test_idx] - data.y[test_idx]).abs().mean()
    
    return model, mae
```

### 2. Disease Classification

```python
def disease_classification(connectomes, labels, disease='Alzheimer'):
    """
    Classify neurological disease from connectome alterations.
    
    Uses connectome constraints to focus on biologically plausible patterns.
    """
    # Create model with disease-specific connectivity patterns
    model = ConnectomeConstrainedNN(
        input_dim=connectomes.shape[1],
        output_dim=2,  # Healthy vs Disease
        hidden_dims=[256, 128],
        connectome_data={'layer_1': connectomes.mean(axis=0)},
        constraint_layers=[1]
    )
    
    # Train with wiring cost regularization
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001, weight_decay=1e-5)
    criterion = nn.CrossEntropyLoss()
    
    for epoch in range(50):
        optimizer.zero_grad()
        
        logits = model(connectomes)
        class_loss = criterion(logits, labels)
        wiring_loss = model.get_wiring_cost()
        
        total_loss = class_loss + wiring_loss
        total_loss.backward()
        optimizer.step()
    
    return model
```

### 3. Transfer Learning with Connectome Priors

```python
def connectome_transfer_learning(source_connectomes, source_labels,
                                 target_connectomes, target_labels,
                                 n_finetune_regions=10):
    """
    Transfer learning using connectome structure as prior.
    
    Source: Large dataset (e.g., HCP)
    Target: Small disease dataset
    """
    # Train on source with full connectome constraints
    source_model = ConnectomeGNN(
        n_regions=source_connectomes.shape[1],
        feature_dim=source_connectomes.shape[2],
        connectome_edge_index=source_connectomes.edge_index
    )
    train_model(source_model, source_connectomes, source_labels)
    
    # Transfer to target with partial fine-tuning
    # Only update regions most affected by disease
    target_model = copy.deepcopy(source_model)
    
    # Identify disease-affected regions
    affected_regions = identify_altered_regions(
        source_connectomes, target_connectomes
    )
    
    # Freeze non-disease regions
    freeze_non_disease_regions(target_model, affected_regions)
    
    # Fine-tune on target
    train_model(target_model, target_connectomes, target_labels)
    
    return target_model
```

## Evaluation Metrics

```python
def evaluate_connectome_constraints(model, test_data):
    """
    Evaluate the effect of connectome constraints.
    
    Metrics:
    1. Performance (accuracy, etc.)
    2. Efficiency (sparsity, wiring cost)
    3. Biological plausibility
    """
    results = {}
    
    # 1. Task performance
    model.eval()
    with torch.no_grad():
        predictions = model(test_data.x)
        results['accuracy'] = compute_accuracy(predictions, test_data.y)
    
    # 2. Network efficiency
    total_params = sum(p.numel() for p in model.parameters())
    results['total_parameters'] = total_params
    
    # Count non-zero connections
    nonzero = 0
    for layer in model.modules():
        if isinstance(layer, (nn.Linear, ConnectomeLinear)):
            nonzero += (layer.weight.abs() > 0.01).sum().item()
    results['nonzero_connections'] = nonzero
    results['sparsity'] = nonzero / total_params
    
    # 3. Wiring cost
    wiring_cost = 0.0
    if hasattr(model, 'get_wiring_cost'):
        wiring_cost = model.get_wiring_cost().item()
    results['wiring_cost'] = wiring_cost
    
    # 4. Brain similarity
    # Compare learned connectivity to biological connectome
    if hasattr(model, 'extract_connectivity'):
        learned_conn = model.extract_connectivity()
        biological_conn = test_data.connectome
        results['connectome_correlation'] = compute_connectivity_correlation(
            learned_conn, biological_conn
        )
    
    return results
```

## References

1. Bettens, D., et al. (2024). Connectome-constrained deep learning improves prediction accuracy and reveals whole-brain dynamics. bioRxiv.
2. Brünn, A., et al. (2024). Brain-inspired learning in artificial neural networks with neuroanatomical connectomes. bioRxiv.
3. Oldham, S., et al. (2022). Connectome smoothing via low-dimensional structural embeddings. NeuroImage.
4. Sarwar, T., et al. (2021). Connectome-based prediction of brain network response to targeted stimulation. PNAS.
5. Shafiei, G., et al. (2020). Spatiotemporal dynamics of functional connectivity in the human brain. NeuroImage.

## Related Skills

- `brain-graph-neural`: GNN methods for brain connectivity
- `functional-connectivity-graph-neural-networks`: Functional connectivity analysis
- `structural-functional-brain-gnn`: Structural-functional fusion
- `geometric-brain-dynamics-mapping`: Geometric methods for brain dynamics

## Activation Keywords

- connectome constraint
- structural connectivity
- wiring cost
- brain network prior
- connectome-based AI
- diffusion MRI connectivity
- brain-inspired architecture
- connectome constrained neural network
- wiring efficiency
- brain graph neural network

## Tools Used

- `read` - Read connectome data files and research papers
- `write` - Save analysis results and model configurations
- `exec` - Run Python scripts for connectome-constrained neural network training

## Instructions for Agents

Follow these steps when helping users with connectome-constrained neural networks:

1. **Identify the constraint type**: Structural connectivity, wiring cost, or connectome-based graph
2. **Load connectome data**: Use provided data loaders for brain connectivity matrices
3. **Build the architecture**: Apply connectome constraints to neural network layers
4. **Train and evaluate**: Run training with connectome-aware architecture

## Examples

### Example 1: Connectome-Constrained Network

```
User: "构建基于连接组约束的神经网络"

Execute:
1. Load connectome structural connectivity matrix
2. Build connectome-constrained layer
3. Wire into full network architecture
4. Train with wiring cost regularization
```

### Example 2: Connectome GNN

```
User: "用连接组数据做脑图神经网络分析"

Execute:
1. Load connectome graph data
2. Build GNN with connectome adjacency matrix
3. Run training for target task
4. Evaluate with connectome-specific metrics
```
