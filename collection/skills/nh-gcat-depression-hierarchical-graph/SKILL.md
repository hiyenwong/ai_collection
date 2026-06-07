---
name: nh-gcat-depression-hierarchical-graph
description: "NH-GCAT: Nested Hierarchical Graph Causal Attention Networks for Explainable Depression Identification from fMRI. Neurocircuitry-inspired architecture integrating brain hierarchy, causal interactions, and attention mechanisms for Major Depressive Disorder diagnosis."
---

# NH-GCAT: Nested Hierarchical Graph Causal Attention Networks for Explainable Depression Identification

> Neurocircuitry-inspired hierarchical graph causal attention framework that integrates brain hierarchy, causal interactions, and attention mechanisms for explainable Major Depressive Disorder identification from fMRI.

## Metadata
- **Source**: arXiv:2511.17622v1
- **Authors**: Weidao Chen, Yuxiao Yang, Yueming Wang
- **Published**: 2025-11-18
- **Category**: q-bio.NC, cs.LG, cs.AI

## Core Methodology

### Key Innovation
Major Depressive Disorder (MDD) manifests through disrupted brain network dynamics, but existing graph neural networks operate as black boxes lacking neurobiological interpretability. This methodology introduces **NH-GCAT**, which combines:
- **Neurocircuitry-inspired hierarchical structure**: Multi-scale brain organization (regions → functional networks → whole brain)
- **Causal attention mechanisms**: Directional connectivity modeling
- **Explainable architecture**: Attention weights map to neurobiological mechanisms

### Theoretical Foundation

#### Hierarchical Brain Organization

**Three-Level Hierarchy**:
```
Level 3: Whole Brain
    ↓
Level 2: Functional Networks (e.g., DMN, FPN, SAL)
    ↓
Level 1: Brain Regions (e.g., amygdala, hippocampus, prefrontal cortex)
```

**Neurobiological Motivation**:
- Depression involves dysregulation across multiple functional networks
- Default Mode Network (DMN) hyperconnectivity
- Fronto-limbic disconnection
- Salience network imbalances

#### Causal Attention

**Problem with Standard Attention**:
- Standard GNNs: A_ij = attention(H_i, H_j) - undirected
- Brain connectivity is inherently directed (effective connectivity)

**Solution - Causal Attention**:
```
A_{i→j} = attention(H_i, H_j, causal_prior)  # Directed

where causal_prior encodes:
- Anatomical connectivity (structural priors)
- Effective connectivity from DCM
- Neurotransmitter systems (dopaminergic, serotonergic)
```

### Architecture Overview

```
fMRI Time Series
    ↓
Region-level Encoding (Transformer)
    ↓
Hierarchical Graph Construction
    - Intra-level edges (within functional networks)
    - Inter-level edges (cross-network connections)
    ↓
Nested Causal Attention
    - Level 1: Region-region attention (causal)
    - Level 2: Network-network attention
    - Level 3: Global integration
    ↓
Hierarchical Readout
    ↓
MDD Classification + Explanation
```

### Technical Components

#### 1. Region-Level Feature Encoding

**Transformer-based Temporal Encoder**:
```python
H_regions = TransformerEncoder(fMRI_time_series)
# Output: [n_regions, d_model]
```

Captures temporal dynamics of each brain region's activity.

#### 2. Hierarchical Graph Construction

**Node Definition**:
- **L1 nodes**: Individual brain regions (N ≈ 100-200)
- **L2 nodes**: Functional networks (7 canonical networks)
- **L3 node**: Global brain state (1 node)

**Edge Definition**:
- **L1-L1 edges**: Functional connectivity between regions
- **L1-L2 edges**: Region → Network membership
- **L2-L2 edges**: Inter-network connectivity
- **L2-L3 edges**: Network → Global integration

#### 3. Nested Causal Attention (NCA)

**Multi-Head Causal Attention**:
```python
# For each attention head h:
Q_i^h = W_q^h * H_i
K_j^h = W_k^h * H_j
V_j^h = W_v^h * H_j

# Causal attention score (directed)
A_{i→j}^h = softmax(Q_i^h · K_j^h / √d_k + C_{ij})

where C_{ij} = causal_prior(i, j)  # Neurobiologically-informed prior

Output_i^h = Σ_j A_{i→j}^h · V_j^h
```

**Causal Prior Formulation**:
```python
def causal_prior(i, j, anatomical_matrix, dcm_matrix):
    """
    Compute causal prior for directed attention.
    
    Args:
        i: source region
        j: target region
        anatomical_matrix: structural connectivity from DTI
        dcm_matrix: effective connectivity from DCM
    
    Returns:
        prior: scalar bias for attention
    """
    struct_term = log(anatomical_matrix[i, j] + ε)
    dcm_term = dcm_matrix[i, j]  # Can be negative (inhibitory)
    
    # Combine with learnable weights
    prior = α * struct_term + β * dcm_term
    
    return prior
```

#### 4. Hierarchical Readout

**Level-wise Aggregation**:
```python
# Level 1 (Regions): Mean pooling per functional network
network_features[k] = mean({H_i : region i ∈ network k})

# Level 2 (Networks): Attention-weighted aggregation
global_feature = attention_pool(network_features)

# Level 3 (Global): Final classification
prediction = MLP(global_feature)
```

## Implementation Guide

### Prerequisites
```python
# Required libraries
pip install torch torch-geometric
pip install nilearn nibabel
pip install scipy scikit-learn
pip install matplotlib seaborn
```

### Complete Implementation

#### Step 1: Data Preparation and Network Parcellation
```python
import numpy as np
from nilearn import datasets, connectome
from nilearn.maskers import NiftiLabelsMasker

class BrainDataLoader:
    """Load and preprocess fMRI data with hierarchical structure."""
    
    def __init__(self, atlas_name='schaefer', n_rois=200):
        self.atlas = self._load_atlas(atlas_name, n_rois)
        self.network_mapping = self._load_network_mapping()
    
    def _load_atlas(self, name, n_rois):
        """Load brain parcellation atlas."""
        if name == 'schaefer':
            return datasets.fetch_atlas_schaefer_2018(n_rois=n_rois)
        elif name == 'aal':
            return datasets.fetch_atlas_aal()
    
    def _load_network_mapping(self):
        """
        Map regions to functional networks.
        
        Returns:
            dict: {region_id: network_name}
        """
        # Schaefer 200-region mapping to 7 canonical networks
        # Networks: Visual, Somatomotor, Dorsal Attention, 
        #           Ventral Attention, Limbic, Frontoparietal, Default
        
        network_mapping = {
            0: 'Visual', 1: 'Visual',
            2: 'Somatomotor', 3: 'Somatomotor',
            # ... full mapping
            6: 'Frontoparietal', 7: 'Default'
        }
        
        return network_mapping
    
    def load_subject(self, fmri_file, confounds_file=None):
        """Load and preprocess single subject."""
        # Extract time series
        masker = NiftiLabelsMasker(
            labels_img=self.atlas.maps,
            standardize=True,
            detrend=True,
            low_pass=0.1,
            high_pass=0.01,
            t_r=2.0  # Repetition time
        )
        
        time_series = masker.fit_transform(
            fmri_file, 
            confounds=confounds_file
        )
        
        return time_series  # [n_timepoints, n_regions]
```

#### Step 2: Hierarchical Graph Construction
```python
import torch
from torch_geometric.data import HeteroData

class HierarchicalBrainGraph:
    """Build hierarchical graph from fMRI data."""
    
    def __init__(self, network_mapping, n_regions):
        self.network_mapping = network_mapping
        self.n_regions = n_regions
        self.n_networks = len(set(network_mapping.values()))
    
    def build_graph(self, time_series):
        """
        Construct hierarchical graph.
        
        Args:
            time_series: [n_timepoints, n_regions]
        
        Returns:
            HeteroData: PyG heterogeneous graph
        """
        data = HeteroData()
        
        # Level 1: Region features
        # Temporal encoding using Transformer or simple statistics
        region_features = self._encode_temporal(time_series)
        data['region'].x = torch.FloatTensor(region_features)
        data['region'].id = torch.arange(self.n_regions)
        
        # Level 2: Network features (initially aggregated)
        network_features = []
        network_nodes = []
        for net_id in range(self.n_networks):
            regions_in_net = [
                r for r in range(self.n_regions) 
                if self.network_mapping.get(r) == net_id
            ]
            if regions_in_net:
                net_feat = region_features[regions_in_net].mean(axis=0)
                network_features.append(net_feat)
                network_nodes.append(net_id)
        
        data['network'].x = torch.FloatTensor(network_features)
        data['network'].id = torch.LongTensor(network_nodes)
        
        # Level 3: Global node
        data['global'].x = torch.FloatTensor(
            network_features.mean(axis=0, keepdims=True)
        )
        
        # Edges: Region-Region (functional connectivity)
        corr_matrix = np.corrcoef(time_series.T)
        edge_index_rr, edge_weight_rr = self._fc_to_edges(corr_matrix)
        data['region', 'connects', 'region'].edge_index = edge_index_rr
        data['region', 'connects', 'region'].edge_attr = edge_weight_rr
        
        # Edges: Region-Network (membership)
        edge_index_rn = []
        for r in range(self.n_regions):
            net_id = self.network_mapping.get(r)
            if net_id is not None:
                edge_index_rn.append([r, net_id])
        
        data['region', 'belongs_to', 'network'].edge_index = (
            torch.LongTensor(edge_index_rn).t()
        )
        
        # Edges: Network-Network (inter-network FC)
        # Compute from region-level connectivity
        edge_index_nn, edge_weight_nn = self._compute_network_fc(
            corr_matrix, self.network_mapping
        )
        data['network', 'interacts', 'network'].edge_index = edge_index_nn
        data['network', 'interacts', 'network'].edge_attr = edge_weight_nn
        
        # Edges: Network-Global
        edge_index_ng = [[i, 0] for i in range(len(network_nodes))]
        data['network', 'integrates', 'global'].edge_index = (
            torch.LongTensor(edge_index_ng).t()
        )
        
        return data
    
    def _encode_temporal(self, time_series):
        """Encode temporal dynamics into region features."""
        # Simple statistical encoding
        features = np.concatenate([
            time_series.mean(axis=0, keepdims=True).T,
            time_series.std(axis=0, keepdims=True).T,
            np.percentile(time_series, 25, axis=0, keepdims=True).T,
            np.percentile(time_series, 75, axis=0, keepdims=True).T
        ], axis=1)
        return features
    
    def _fc_to_edges(self, corr_matrix, threshold=0.3):
        """Convert correlation matrix to edge index."""
        edges = []
        weights = []
        for i in range(self.n_regions):
            for j in range(i+1, self.n_regions):
                if abs(corr_matrix[i, j]) > threshold:
                    edges.append([i, j])
                    edges.append([j, i])  # Undirected
                    weights.extend([corr_matrix[i, j]] * 2)
        
        edge_index = torch.LongTensor(edges).t()
        edge_weight = torch.FloatTensor(weights)
        return edge_index, edge_weight
    
    def _compute_network_fc(self, corr_matrix, network_mapping):
        """Compute inter-network functional connectivity."""
        # Aggregate region-level to network-level
        # Implementation omitted for brevity
        pass
```

#### Step 3: Nested Hierarchical Causal Attention Network
```python
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.nn import HeteroConv, Linear, MessagePassing
from torch_geometric.utils import softmax

class CausalAttention(MessagePassing):
    """Causal attention layer with directed edges."""
    
    def __init__(self, in_channels, out_channels, heads=4):
        super().__init__(aggr='add', node_dim=0)
        self.heads = heads
        self.out_channels = out_channels
        self.head_dim = out_channels // heads
        
        self.q_linear = nn.Linear(in_channels, out_channels)
        self.k_linear = nn.Linear(in_channels, out_channels)
        self.v_linear = nn.Linear(in_channels, out_channels)
        
        # Causal prior (learnable or fixed)
        self.causal_prior = nn.Parameter(torch.randn(1))
    
    def forward(self, x, edge_index, causal_bias=None):
        """
        Args:
            x: Node features [N, in_channels]
            edge_index: Directed edges [2, E]
            causal_bias: Optional pre-computed causal bias [E]
        """
        Q = self.q_linear(x).view(-1, self.heads, self.head_dim)
        K = self.k_linear(x).view(-1, self.heads, self.head_dim)
        V = self.v_linear(x).view(-1, self.heads, self.head_dim)
        
        # Propagate
        out = self.propagate(edge_index, Q=Q, K=K, V=V, causal_bias=causal_bias)
        return out.view(-1, self.out_channels)
    
    def message(self, Q_i, K_j, V_j, edge_index_i, causal_bias, index, ptr, size_i):
        """Compute messages with causal attention."""
        # Attention scores
        attn = (Q_i * K_j).sum(dim=-1) / (self.head_dim ** 0.5)
        
        # Add causal bias
        if causal_bias is not None:
            attn = attn + causal_bias.view(-1, 1)
        else:
            attn = attn + self.causal_prior
        
        # Softmax normalization
        attn = softmax(attn, index, ptr, size_i)
        
        # Weighted messages
        return attn.unsqueeze(-1) * V_j


class NHGCATLayer(nn.Module):
    """Single layer of NH-GCAT."""
    
    def __init__(self, hidden_dim, num_heads=4):
        super().__init__()
        
        # Heterogeneous convolution
        self.conv = HeteroConv({
            # Region-level causal attention
            ('region', 'connects', 'region'): CausalAttention(
                hidden_dim, hidden_dim, num_heads
            ),
            # Region to Network
            ('region', 'belongs_to', 'network'): Linear(-1, hidden_dim),
            # Network to Network
            ('network', 'interacts', 'network'): CausalAttention(
                hidden_dim, hidden_dim, num_heads
            ),
            # Network to Global
            ('network', 'integrates', 'global'): Linear(-1, hidden_dim),
        }, aggr='mean')
        
        self.norm = nn.LayerNorm(hidden_dim)
        self.ffn = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim * 4),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(hidden_dim * 4, hidden_dim)
        )
    
    def forward(self, x_dict, edge_index_dict):
        # Message passing
        x_dict = self.conv(x_dict, edge_index_dict)
        
        # Residual and normalization
        for key in x_dict:
            x_dict[key] = self.norm(x_dict[key] + self.ffn(x_dict[key]))
        
        return x_dict


class NHGCAT(nn.Module):
    """Complete NH-GCAT model."""
    
    def __init__(self, in_channels, hidden_channels, num_classes, num_layers=3):
        super().__init__()
        
        # Input projection
        self.input_proj = nn.Linear(in_channels, hidden_channels)
        
        # NH-GCAT layers
        self.layers = nn.ModuleList([
            NHGCATLayer(hidden_channels) for _ in range(num_layers)
        ])
        
        # Hierarchical readout
        self.readout = nn.Sequential(
            nn.Linear(hidden_channels * 3, hidden_channels),  # 3 levels
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(hidden_channels, num_classes)
        )
    
    def forward(self, data):
        # Initial projection
        x_dict = {
            key: self.input_proj(x) 
            for key, x in data.x_dict.items()
        }
        
        # NH-GCAT layers
        for layer in self.layers:
            x_dict = layer(x_dict, data.edge_index_dict)
        
        # Hierarchical readout
        region_feat = x_dict['region'].mean(dim=0, keepdim=True)
        network_feat = x_dict['network'].mean(dim=0, keepdim=True)
        global_feat = x_dict['global']
        
        combined = torch.cat([region_feat, network_feat, global_feat], dim=-1)
        
        return self.readout(combined)
```

#### Step 4: Training and Explainability
```python
class ExplainableMDDClassifier:
    """NH-GCAT with explanation capabilities."""
    
    def __init__(self, model, device='cuda'):
        self.model = model.to(device)
        self.device = device
        self.optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)
        self.criterion = nn.CrossEntropyLoss()
    
    def train_epoch(self, dataloader):
        self.model.train()
        total_loss = 0
        
        for batch in dataloader:
            data = batch.to(self.device)
            label = data.y.to(self.device)
            
            self.optimizer.zero_grad()
            out = self.model(data)
            loss = self.criterion(out, label)
            loss.backward()
            self.optimizer.step()
            
            total_loss += loss.item()
        
        return total_loss / len(dataloader)
    
    def explain_prediction(self, data):
        """
        Generate explanation for MDD prediction.
        
        Returns:
            dict: Explanation with attention weights and important regions
        """
        self.model.eval()
        with torch.no_grad():
            # Forward pass with attention capture
            out, attention_weights = self.model.forward_with_attention(data)
            
            # Analyze attention patterns
            explanation = {
                'prediction': out.argmax().item(),
                'confidence': out.softmax(dim=1).max().item(),
                'region_importance': attention_weights['region'].cpu().numpy(),
                'network_importance': attention_weights['network'].cpu().numpy(),
                'critical_connections': self._get_critical_connections(
                    attention_weights['region-region']
                )
            }
            
            return explanation
    
    def _get_critical_connections(self, attention_matrix, top_k=10):
        """Identify most important region-region connections."""
        # Flatten and sort
        flat_attn = attention_matrix.flatten()
        top_indices = flat_attn.argsort(descending=True)[:top_k]
        
        # Convert to region pairs
        n = attention_matrix.shape[0]
        connections = []
        for idx in top_indices:
            i, j = idx // n, idx % n
            connections.append({
                'source': i.item(),
                'target': j.item(),
                'weight': flat_attn[idx].item()
            })
        
        return connections
```

## Applications
- **MDD diagnosis** from resting-state fMRI
- **Depression severity prediction**
- **Treatment response prediction**
- **Neurobiological mechanism discovery**
- **Personalized medicine** in psychiatry

## Performance Benchmarks

| Dataset | Method | Accuracy | AUC | Interpretability |
|---------|--------|----------|-----|------------------|
| REST-MDD | GCN | 72.3% | 0.78 | Low |
| REST-MDD | BrainNetCNN | 75.1% | 0.81 | Low |
| REST-MDD | NH-GCAT | **84.7%** | **0.89** | **High** |

## Pitfalls
- **Data scarcity**: MDD datasets are often small (100-500 subjects)
- **Heterogeneity**: Depression is highly heterogeneous; subtype consideration needed
- **Causal prior quality**: Depends on quality of structural/DCM priors
- **Overfitting**: High model complexity requires regularization
- **Clinician interpretation**: Attention weights need clinical validation

## Related Skills
- brain-graph-neural
- brain-network-controllability
- higher-order-brain-networks
- gnn-visual-decoding-brain-network

## References
```bibtex
@article{chen2025nhgcat,
  title={Neurocircuitry-Inspired Hierarchical Graph Causal Attention Networks for Explainable Depression Identification},
  author={Chen, Weidao and Yang, Yuxiao and Wang, Yueming},
  journal={arXiv preprint arXiv:2511.17622},
  year={2025}
}
```
