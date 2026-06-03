---
name: gat-asd-detection-brain-connectivity
description: "Graph Attention Network-based detection of Autism Spectrum Disorder using fMRI functional connectivity. Attention mechanisms for interpretable brain connectivity analysis. Activation: autism, ASD, graph attention network, GAT, functional connectivity, fMRI, ABIDE, neurodevelopmental, brain network."
---

# GATGraphClassifier: Graph Attention Network for Autism Spectrum Disorder Detection

> Novel computational framework using Attention-Based Graph Convolutional Networks for detecting ASD from fMRI functional connectivity data.

## Metadata
- **Source**: arXiv:2603.26971v1
- **Authors**: Abigail Kelly, Ramchandra Rimal, Arpan Sainju
- **Published**: 2026-03-27
- **Categories**: stat.AP, cs.LG

## Core Methodology

### Problem Statement
Autism Spectrum Disorder (ASD) is characterized by **atypical brain connectivity**. Early detection is crucial for intervention. Traditional methods lack interpretability and accuracy.

### Solution: GATGraphClassifier

#### Data Pipeline
1. **fMRI data** from ABIDE (Autism Brain Imaging Data Exchange)
2. **Functional connectivity matrices** via Pearson correlation
3. **Graph representation**: Nodes = brain regions, Edges = functional connections

#### Model Architecture
- **Graph Attention Networks (GAT)** identify critical connectivity patterns
- **Attention mechanisms** enhance interpretability
- **Diagnostic accuracy** superior to state-of-the-art

## Implementation Guide

### Prerequisites
- PyTorch Geometric or DGL
- Nilearn for fMRI preprocessing
- ABIDE dataset access
- scikit-learn for evaluation

### Step-by-Step Implementation

#### Step 1: Data Preprocessing
```python
import nibabel as nib
import numpy as np
from nilearn import datasets, connectome

def load_abide_data(data_dir):
    """Load ABIDE fMRI data and phenotypic information"""
    # Download or load preprocessed ABIDE data
    # Typically uses CPAC preprocessing pipeline
    abide = datasets.fetch_abide_pcp(data_dir=data_dir, 
                                     pipeline='cpac',
                                     band_pass_filtering=True)
    return abide.func_preproc, abide.phenotypic

def extract_time_series(func_img, atlas='cc200'):
    """Extract time series from regions of interest"""
    from nilearn.input_data import NiftiLabelsMasker
    
    # Load atlas (e.g., Craddock 200, AAL, etc.)
    atlas_img = datasets.fetch_atlas_craddock_2012()['maps']
    
    masker = NiftiLabelsMasker(labels_img=atlas_img,
                               standardize=True,
                               memory='nilearn_cache')
    
    time_series = masker.fit_transform(func_img)
    return time_series
```

#### Step 2: Build Functional Connectivity Graphs
```python
from nilearn.connectome import ConnectivityMeasure

def build_connectivity_graph(time_series_list, labels):
    """
    Build graph from functional connectivity matrices
    Args:
        time_series_list: List of time series arrays [num_subjects, num_timepoints, num_regions]
        labels: Diagnosis labels (ASD=1, Control=0)
    Returns:
        graphs: List of NetworkX graphs
        edge_indices: Edge connectivity for PyG
    """
    correlation_measure = ConnectivityMeasure(kind='correlation')
    
    graphs = []
    edge_indices = []
    
    for time_series, label in zip(time_series_list, labels):
        # Compute Pearson correlation
        connectivity_matrix = correlation_measure.fit_transform([time_series])[0]
        
        # Threshold to create sparse graph (keep top K connections)
        k = 50  # Keep top 50 connections per node
        adj_matrix = threshold_connections(connectivity_matrix, k)
        
        # Convert to edge index format for PyG
        edge_index = np.array(np.nonzero(adj_matrix))
        edge_indices.append(edge_index)
        
        # Node features: can use connectivity values or additional features
        node_features = connectivity_matrix  # [num_regions, num_regions]
        graphs.append((node_features, edge_index, label))
    
    return graphs, edge_indices

def threshold_connections(matrix, k):
    """Keep top k connections per node"""
    adj = np.zeros_like(matrix)
    for i in range(matrix.shape[0]):
        top_k_idx = np.argsort(matrix[i])[-k:]
        adj[i, top_k_idx] = matrix[i, top_k_idx]
        adj[top_k_idx, i] = matrix[top_k_idx, i]  # Symmetrize
    return adj
```

#### Step 3: GAT Model
```python
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.nn import GATConv, global_mean_pool

class GATGraphClassifier(nn.Module):
    def __init__(self, in_channels, hidden_channels=64, num_heads=4, num_classes=2):
        super().__init__()
        
        # First GAT layer
        self.conv1 = GATConv(in_channels, hidden_channels, heads=num_heads, dropout=0.6)
        # Second GAT layer
        self.conv2 = GATConv(hidden_channels * num_heads, hidden_channels, heads=num_heads, dropout=0.6)
        
        # Classification head
        self.classifier = nn.Sequential(
            nn.Linear(hidden_channels * num_heads, 64),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(64, num_classes)
        )
    
    def forward(self, x, edge_index, batch):
        # First GAT layer
        x = self.conv1(x, edge_index)
        x = F.elu(x)
        x = F.dropout(x, p=0.6, training=self.training)
        
        # Second GAT layer
        x = self.conv2(x, edge_index)
        x = F.elu(x)
        
        # Global pooling
        x = global_mean_pool(x, batch)
        
        # Classification
        out = self.classifier(x)
        return out
    
    def get_attention_weights(self, x, edge_index):
        """Extract attention weights for interpretability"""
        # Returns attention coefficients from GAT layers
        _, attn_weights = self.conv1(x, edge_index, return_attention_weights=True)
        return attn_weights
```

#### Step 4: Training and Evaluation
```python
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def train_gat_model(model, train_loader, optimizer, criterion):
    model.train()
    total_loss = 0
    
    for data in train_loader:
        optimizer.zero_grad()
        out = model(data.x, data.edge_index, data.batch)
        loss = criterion(out, data.y)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    
    return total_loss / len(train_loader)

def evaluate_model(model, test_loader):
    model.eval()
    predictions = []
    labels = []
    
    with torch.no_grad():
        for data in test_loader:
            out = model(data.x, data.edge_index, data.batch)
            pred = out.argmax(dim=1)
            predictions.extend(pred.cpu().numpy())
            labels.extend(data.y.cpu().numpy())
    
    accuracy = accuracy_score(labels, predictions)
    precision = precision_score(labels, predictions, average='weighted')
    recall = recall_score(labels, predictions, average='weighted')
    f1 = f1_score(labels, predictions, average='weighted')
    
    return {'accuracy': accuracy, 'precision': precision, 
            'recall': recall, 'f1': f1}

# Cross-validation
skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
results = []

for fold, (train_idx, test_idx) in enumerate(skf.split(X, y)):
    # Create train/test loaders
    train_loader = create_data_loader(X[train_idx], y[train_idx])
    test_loader = create_data_loader(X[test_idx], y[test_idx])
    
    # Initialize model
    model = GATGraphClassifier(in_channels=200)  # For CC200 atlas
    optimizer = torch.optim.Adam(model.parameters(), lr=0.005, weight_decay=5e-4)
    criterion = nn.CrossEntropyLoss()
    
    # Training loop
    for epoch in range(200):
        loss = train_gat_model(model, train_loader, optimizer, criterion)
    
    # Evaluation
    fold_results = evaluate_model(model, test_loader)
    results.append(fold_results)

# Average results across folds
avg_results = {k: np.mean([r[k] for r in results]) for k in results[0].keys()}
print(f"Average Accuracy: {avg_results['accuracy']:.4f}")
```

#### Step 5: Interpretability - Critical Brain Regions
```python
def identify_critical_regions(model, data_loader, region_names):
    """Identify brain regions most important for ASD classification"""
    model.eval()
    all_attention_weights = []
    
    with torch.no_grad():
        for data in data_loader:
            attn = model.get_attention_weights(data.x, data.edge_index)
            all_attention_weights.append(attn)
    
    # Aggregate attention across all samples
    mean_attention = torch.mean(torch.stack(all_attention_weights), dim=0)
    
    # Sum attention per node
    node_importance = mean_attention.sum(dim=1).cpu().numpy()
    
    # Rank regions
    region_importance = list(zip(region_names, node_importance))
    region_importance.sort(key=lambda x: x[1], reverse=True)
    
    return region_importance
```

## Results

### Performance Metrics
- **Average accuracy**: 88.79% (test data, 30 independent runs)
- **Improvement over benchmark**: +12.27%
- **Robustness**: Consistent across validation folds

### Identified Critical Brain Regions
- **Consistent with previous studies**: Known ASD-related regions
- **Novel regions**: Previously unreported connectivity patterns
- **Interpretable**: Attention weights show which connections matter most

## Applications
- **ASD early detection**: Screening tool for clinical use
- **Brain connectivity analysis**: Understanding ASD mechanisms
- **Generalizable framework**: Adaptable to other neurodevelopmental conditions
- **Complex relational data**: Beyond neuroimaging (social networks, etc.)

## Pitfalls
- **Dataset bias**: ABIDE has site-specific variability
- **Preprocessing sensitivity**: Pipeline choice affects results
- **Atlas dependency**: Results vary with parcellation scheme
- **Threshold selection**: K value for graph sparsity is arbitrary
- **Attention interpretation**: High attention doesn't always mean clinical importance

## Related Skills
- brain-connectivity-analysis
- graph-laplacian-denoising
- bleg-llm-brain-graph-enhancer
- higher-order-brain-networks
