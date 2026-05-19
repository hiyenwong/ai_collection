---
name: alzheimer-prediction-fmri
description: Graph Neural Network-based model for predicting Alzheimer's disease progression using resting-state fMRI and historical clinical data. Predicts transitions between cognitive stages (CN → MCI → AD) using functional connectivity graphs.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [neuroscience, alzheimer, fMRI, GNN, brain-network, disease-progression, clinical-neuroimaging]
    source_paper: "Predicting Alzheimer's disease progression using rs-fMRI and a history-aware graph neural network (arXiv:2604.06469)"
    citations: 0
    published: "2026-04-07"
---

# Alzheimer's Disease Progression Prediction

## Overview

This skill implements a **history-aware Graph Neural Network (GNN)** for predicting Alzheimer's disease (AD) progression using resting-state functional MRI (rs-fMRI). The model predicts whether a subject will transition to a more severe stage of cognitive impairment at their next clinical visit.

## Clinical Context

### Alzheimer's Disease Stages
- **CN (Cognitively Normal)**: No cognitive impairment
- **MCI (Mild Cognitive Impairment)**: Early stage with mild symptoms
- **AD (Alzheimer's Disease)**: Dementia with significant impairment

### The Prediction Challenge
- Early detection enables intervention to slow progression
- Current diagnosis often occurs after significant brain changes
- Need for predictive models using neuroimaging biomarkers

## Key Innovation

**History-Aware Prediction**: Incorporates longitudinal clinical history (previous visits, diagnoses) along with current rs-fMRI data to predict future cognitive decline.

## Core Concepts

### 1. Functional Connectivity Graphs
Transform rs-fMRI data into brain network graphs:

```python
import numpy as np
import scipy.stats as stats

def build_functional_connectivity_graph(fmri_timeseries, atlas_regions):
    """
    Build functional connectivity graph from rs-fMRI time series.
    
    Args:
        fmri_timeseries: Array of shape (n_regions, n_timepoints)
        atlas_regions: List of brain region names/labels
    
    Returns:
        adjacency_matrix: Functional connectivity matrix (n_regions x n_regions)
        node_features: Regional time series features
    """
    n_regions = len(atlas_regions)
    
    # Compute Pearson correlation between region time series
    adjacency_matrix = np.corrcoef(fmri_timeseries)
    
    # Fisher z-transform to normalize correlations
    adjacency_matrix = np.arctanh(adjacency_matrix)
    np.fill_diagonal(adjacency_matrix, 0)  # Remove self-connections
    
    # Extract node features (regional activity statistics)
    node_features = np.zeros((n_regions, 5))
    for i in range(n_regions):
        ts = fmri_timeseries[i]
        node_features[i] = [
            np.mean(ts),      # Mean activity
            np.std(ts),       # Standard deviation
            np.max(ts),       # Maximum
            np.min(ts),       # Minimum
            stats.skew(ts)    # Skewness
        ]
    
    return adjacency_matrix, node_features

# Common brain atlases
ATLASES = {
    'aal': 116,      # Automated Anatomical Labeling
    'harvard_oxford': 48,
    'schaefer': 400, # Schaefer 2018
    'destrieux': 148
}
```

### 2. History-Aware GNN Architecture
```python
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.nn import GCNConv, global_mean_pool

class HistoryAwareGNN(nn.Module):
    """
    Graph Neural Network for AD progression prediction with clinical history.
    """
    
    def __init__(self, 
                 n_node_features=5, 
                 n_hidden=64, 
                 n_classes=3,
                 history_dim=32):
        super(HistoryAwareGNN, self).__init__()
        
        # Graph convolutional layers
        self.conv1 = GCNConv(n_node_features, n_hidden)
        self.conv2 = GCNConv(n_hidden, n_hidden)
        self.conv3 = GCNConv(n_hidden, n_hidden)
        
        # History encoder (RNN for longitudinal data)
        self.history_encoder = nn.GRU(
            input_size=10,  # Previous diagnoses, scores, etc.
            hidden_size=history_dim,
            num_layers=2,
            batch_first=True
        )
        
        # Fusion and classification
        self.fusion = nn.Sequential(
            nn.Linear(n_hidden + history_dim, 128),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(128, n_classes)
        )
    
    def forward(self, x, edge_index, batch, history=None):
        """
        Args:
            x: Node features (n_nodes, n_features)
            edge_index: Graph connectivity (2, n_edges)
            batch: Batch assignment for each node
            history: Clinical history features (batch_size, seq_len, history_features)
        
        Returns:
            logits: Class logits for progression prediction
        """
        # Graph feature extraction
        x = F.relu(self.conv1(x, edge_index))
        x = F.relu(self.conv2(x, edge_index))
        x = self.conv3(x, edge_index)
        
        # Global graph pooling
        graph_embedding = global_mean_pool(x, batch)
        
        # History encoding (if available)
        if history is not None:
            _, history_embedding = self.history_encoder(history)
            history_embedding = history_embedding[-1]  # Last layer
        else:
            history_embedding = torch.zeros(graph_embedding.size(0), 32).to(graph_embedding.device)
        
        # Fusion and prediction
        combined = torch.cat([graph_embedding, history_embedding], dim=1)
        logits = self.fusion(combined)
        
        return logits
```

### 3. Longitudinal Data Processing
```python
class LongitudinalClinicalData:
    """
    Process and encode longitudinal clinical history.
    """
    
    def __init__(self):
        self.stage_encoding = {'CN': 0, 'MCI': 1, 'AD': 2}
    
    def encode_history(self, visits):
        """
        Encode clinical history from multiple visits.
        
        Args:
            visits: List of dicts with visit data
                [{"date": "2020-01", "diagnosis": "CN", "mmse": 28, ...}, ...]
        
        Returns:
            history_vector: Encoded history features
        """
        features = []
        
        for visit in visits:
            # Encode diagnosis
            diag_code = self.stage_encoding.get(visit['diagnosis'], 0)
            
            # Encode cognitive scores
            mmse = visit.get('mmse', 0) / 30.0  # Normalize
            cdr = visit.get('cdr', 0)  # Clinical Dementia Rating
            
            # Time since last visit (normalized)
            time_delta = visit.get('months_since_last', 6) / 12.0
            
            # Combine features
            visit_features = [diag_code, mmse, cdr, time_delta]
            features.append(visit_features)
        
        # Pad or truncate to fixed length
        max_visits = 5
        if len(features) < max_visits:
            features.extend([[0, 0, 0, 0]] * (max_visits - len(features)))
        else:
            features = features[-max_visits:]
        
        return np.array(features)
```

## Implementation Pattern

### Complete Training Pipeline
```python
from torch_geometric.data import Data, DataLoader
import torch.optim as optim

class ADProgressionPipeline:
    """
    Complete pipeline for AD progression prediction.
    """
    
    def __init__(self, n_regions=116, n_classes=3):
        self.n_regions = n_regions
        self.n_classes = n_classes
        
        # Initialize model
        self.model = HistoryAwareGNN(
            n_node_features=5,
            n_hidden=64,
            n_classes=n_classes,
            history_dim=32
        )
        
        self.optimizer = optim.Adam(self.model.parameters(), lr=0.001)
        self.criterion = nn.CrossEntropyLoss()
    
    def prepare_graph_data(self, fmri_data, clinical_history, label):
        """
        Prepare PyTorch Geometric Data object.
        
        Args:
            fmri_data: rs-fMRI time series (n_regions, n_timepoints)
            clinical_history: Encoded history features (seq_len, n_features)
            label: Target label (0=CN, 1=MCI, 2=AD or stable/converted)
        
        Returns:
            data: PyTorch Geometric Data object
        """
        # Build functional connectivity graph
        adjacency, node_features = build_functional_connectivity_graph(
            fmri_data, 
            list(range(self.n_regions))
        )
        
        # Convert to edge_index format
        edge_index = self._adjacency_to_edge_index(adjacency)
        
        # Create Data object
        data = Data(
            x=torch.FloatTensor(node_features),
            edge_index=torch.LongTensor(edge_index),
            history=torch.FloatTensor(clinical_history),
            y=torch.LongTensor([label])
        )
        
        return data
    
    def _adjacency_to_edge_index(self, adjacency, threshold=0.3):
        """Convert adjacency matrix to edge_index format."""
        # Threshold to create sparse graph
        mask = np.abs(adjacency) > threshold
        edges = np.argwhere(mask)
        edge_index = edges.T
        return edge_index
    
    def train(self, train_loader, epochs=100):
        """Train the model."""
        self.model.train()
        
        for epoch in range(epochs):
            total_loss = 0
            correct = 0
            total = 0
            
            for batch in train_loader:
                self.optimizer.zero_grad()
                
                # Forward pass
                out = self.model(
                    batch.x, 
                    batch.edge_index, 
                    batch.batch,
                    batch.history
                )
                
                # Compute loss
                loss = self.criterion(out, batch.y)
                
                # Backward pass
                loss.backward()
                self.optimizer.step()
                
                # Statistics
                total_loss += loss.item()
                pred = out.argmax(dim=1)
                correct += (pred == batch.y).sum().item()
                total += batch.y.size(0)
            
            accuracy = 100 * correct / total
            if (epoch + 1) % 10 == 0:
                print(f'Epoch {epoch+1}/{epochs}, Loss: {total_loss/len(train_loader):.4f}, Accuracy: {accuracy:.2f}%')
    
    def predict_progression(self, fmri_data, clinical_history):
        """
        Predict next cognitive stage.
        
        Returns:
            prediction: Predicted stage (0=CN, 1=MCI, 2=AD)
            probabilities: Probability for each stage
        """
        self.model.eval()
        
        data = self.prepare_graph_data(fmri_data, clinical_history, 0)
        
        with torch.no_grad():
            logits = self.model(
                data.x.unsqueeze(0),
                data.edge_index,
                torch.zeros(1, dtype=torch.long),  # Single graph batch
                data.history.unsqueeze(0)
            )
            probabilities = F.softmax(logits, dim=1)
            prediction = logits.argmax(dim=1).item()
        
        return prediction, probabilities[0].numpy()
```

## Applications

1. **Early Detection**: Identify at-risk individuals before symptoms worsen
2. **Clinical Trial Stratification**: Enroll appropriate subjects for trials
3. **Treatment Monitoring**: Track disease progression over time
4. **Resource Planning**: Anticipate care needs for patient populations

## Performance Metrics

| Metric | Description |
|--------|-------------|
| Accuracy | Overall prediction accuracy |
| Sensitivity | True positive rate (correctly identifying converters) |
| Specificity | True negative rate (correctly identifying non-converters) |
| AUC-ROC | Area under ROC curve |
| Time to Conversion | Predicted vs. actual time to stage transition |

## References

- Moghaddami, M., et al. (2026). Predicting Alzheimer's disease progression using rs-fMRI and a history-aware graph neural network. arXiv:2604.06469.
- Related: ADNI dataset, Brain connectivity analysis (Fornito & Bullmore, 2015)

## See Also

- `eeg-cnn-autoencoder`: Neural signal classification
- `in-context-brain-decoding`: Brain decoding methods
