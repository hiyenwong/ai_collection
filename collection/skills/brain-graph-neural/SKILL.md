---
name: brain-graph-neural
description: "Graph Neural Network methods for brain connectivity analysis. Use when analyzing fMRI/EEG brain network data, modeling brain structure-function relationships, predicting cognitive outcomes from connectome data, or applying GNN to neuroscience problems. Keywords: brain graph, connectome GNN, neural network brain, fMRI GNN, brain connectivity analysis, 脑网络图神经网络, 脑连接性分析, 认知预测."
---

# Brain Graph Neural Network Skill

Graph Neural Network methods for analyzing brain connectivity and modeling brain structure-function relationships.

## Activation Keywords

- brain graph neural
- connectome GNN
- brain connectivity analysis
- fMRI GNN
- 脑网络图神经网络
- 脑连接性分析
- 认知预测 GNN
- brain network modeling
- functional connectome

## Tools Used

- `exec`: Run Python scripts for data processing
- `read`: Load brain network data, atlases, and reference materials
- `write`: Save analysis results and visualizations
- `image`: Analyze brain connectivity visualizations

## Core Concepts

### Brain Connectivity Types

1. **Structural Connectivity**: Physical connections (DTI, tractography)
2. **Functional Connectivity**: Statistical dependencies (fMRI, EEG)
3. **Effective Connectivity**: Directional causal relationships

### Common Brain Atlases

- AAL-90/116: Anatomical Automatic Labeling
- Brainnetome 246: Fine-grained parcellation
- Schaefer 100/200/400: Functional atlas
- Power 264: Network-based atlas

### Graph Neural Network Architectures

1. **Graph Convolutional Network (GCN)**: Spatial convolution on graphs
2. **Graph Attention Network (GAT)**: Attention mechanism on edges
3. **GraphSAGE**: Inductive learning with sampling
4. **Message Passing Neural Network (MPNN)**: General framework

## Usage Patterns

### Pattern 1: Brain Network Construction from fMRI

**Input**: fMRI time series data
**Output**: Brain graph with nodes (brain regions) and edges (functional correlations)

**Steps**:
1. Preprocess fMRI data (motion correction, normalization)
2. Extract time series for each brain region using atlas
3. Compute correlation matrix (Pearson, partial correlation)
4. Threshold matrix to create sparse graph
5. Apply GNN for analysis task

### Pattern 2: Cognitive Prediction from Connectome

**Input**: Functional connectome + behavioral/cognitive measures
**Output**: Prediction of cognitive scores, disease classification

**Steps**:
1. Load connectome data
2. Construct graph with node features (regional properties)
3. Train GNN model on labeled data
4. Predict cognitive outcomes
5. Interpret results (important brain regions, connections)

### Pattern 3: Multi-Modal Brain Network Fusion

**Input**: Structural + functional connectivity data
**Output**: Unified brain network representation

**Steps**:
1. Load structural and functional connectivity matrices
2. Create multi-layer graph (multiplex network)
3. Apply multi-modal GNN architecture
4. Learn joint representation
5. Perform downstream task (prediction, classification)

## Instructions for Agents

### Step 1: Understand the Task

Identify the specific brain analysis task:
- Cognitive prediction?
- Disease classification?
- Network visualization?
- Structure-function relationship modeling?

Ask clarifying questions:
- What type of brain data? (fMRI, EEG, DTI)
- Which brain atlas to use?
- What's the prediction target?
- Any specific GNN architecture preference?

### Step 2: Data Preparation

1. **Load brain data**:
   ```python
   # Example: Load fMRI connectivity matrix
   import numpy as np
   connectivity = np.load('connectivity_matrix.npy')
   ```

2. **Apply brain atlas**:
   - Choose atlas based on task requirements
   - AAL for anatomical regions
   - Schaefer for functional networks
   - Power for network-based analysis

3. **Construct graph**:
   ```python
   # Create brain graph
   import torch
   from torch_geometric.data import Data
   
   # Nodes: brain regions
   # Edges: functional connections
   # Node features: regional properties
   graph = Data(x=node_features, edge_index=edge_index, edge_attr=edge_weights)
   ```

### Step 3: GNN Model Selection

Choose appropriate architecture:

| Task | Recommended Architecture |
|------|------------------------|
| Classification | GCN, GAT |
| Prediction | GraphSAGE, MPNN |
| Multi-modal fusion | Multi-layer GNN |
| Temporal dynamics | Spatio-temporal GNN |
| Interpretability | Attention-based GNN |

### Step 4: Implementation

1. **Setup environment**:
   ```bash
   pip install torch-geometric nilearn nibabel
   ```

2. **Implement GNN**:
   ```python
   import torch_geometric.nn as gnn
   
   # Example: GCN for brain network
   class BrainGCN(torch.nn.Module):
       def __init__(self, num_features, num_classes):
           super().__init__()
           self.conv1 = gnn.GCNConv(num_features, 64)
           self.conv2 = gnn.GCNConv(64, 32)
           self.classifier = torch.nn.Linear(32, num_classes)
       
       def forward(self, data):
           x, edge_index = data.x, data.edge_index
           x = self.conv1(x, edge_index).relu()
           x = self.conv2(x, edge_index)
           return self.classifier(x)
   ```

3. **Train and evaluate**:
   - Split data (train/val/test)
   - Use appropriate metrics (accuracy, AUC, correlation)
   - Cross-validation for robustness

### Step 5: Result Interpretation

1. **Identify important regions**:
   - Use attention weights or node embeddings
   - Map back to brain atlas
   - Visualize on brain surface

2. **Extract key connections**:
   - Edge importance analysis
   - Network hubs identification
   - Community detection

3. **Clinical relevance**:
   - Relate findings to neuroscience literature
   - Identify disease-relevant patterns
   - Suggest biomarkers

## Common Challenges

### Challenge 1: Atlas Selection
- Different atlases have different resolutions
- Choose atlas matching research question
- Consider registration accuracy

**Solution**: Use multiple atlases and compare results

### Challenge 2: Connectivity Thresholding
- Too dense: computational burden
- Too sparse: lose information

**Solution**: Use adaptive thresholding or multi-threshold analysis

### Challenge 3: Small Sample Size
- Neuroimaging studies often have limited subjects
- Risk of overfitting

**Solution**: 
- Use regularization (dropout, L2)
- Transfer learning from larger datasets
- Leave-one-out cross-validation

### Challenge 4: Interpretability
- GNN predictions need clinical interpretation
- Black-box models are problematic for medical applications

**Solution**:
- Use attention-based GNN for transparency
- Extract node/edge importance
- Validate with domain experts

## Key Research Papers

1. **MAGNet**: Multi-scale Adaptive Graph Network for structure-function fusion
2. **NeuroBRIDGE**: Behavior-conditioned Koopman dynamics for longitudinal connectome
3. **BrainGNN**: Graph neural network for functional brain networks
4. **Graph-variate auto-encoder**: Multi-modal brain network learning

## Related Skills

- **gnn-transformer-fusion**: For combining GNN with transformer architectures
- **multimodal-brain-connectivity-gnn**: Specialized for multi-modal fusion
- **federated-brain-trajectory-gnn**: For federated learning on brain data

## Examples

### Example 1: Alzheimer's Disease Classification

**Request**: "Use GNN to classify Alzheimer's patients from fMRI connectivity data"

**Process**:
1. Load fMRI connectivity matrices from ADNI dataset
2. Apply AAL atlas (90 regions)
3. Construct brain graphs with correlation matrices
4. Train GCN/GAT for binary classification (AD vs healthy)
5. Evaluate with AUC, accuracy
6. Identify disease-relevant brain regions

### Example 2: Cognitive Score Prediction

**Request**: "Predict fluid intelligence scores from brain functional connectivity"

**Process**:
1. Load connectome data from ABCD dataset
2. Use Schaefer 200 atlas
3. Extract node features (regional activation, connectivity strength)
4. Train GraphSAGE regression model
5. Predict cognitive scores
6. Correlate predictions with actual scores

### Example 3: Multi-Modal Fusion

**Request**: "Combine structural and functional connectivity for disease prediction"

**Process**:
1. Load DTI (structural) and fMRI (functional) data
2. Create multi-layer graph
3. Apply multi-modal GNN architecture
4. Learn joint representation
5. Improve prediction accuracy vs single-modal

## Best Practices

1. **Data quality**: Check for motion artifacts, noise
2. **Atlas consistency**: Use same atlas across subjects
3. **Network sparsity**: Optimize edge density
4. **Cross-validation**: Essential for medical applications
5. **Interpretability**: Always extract and validate key findings
6. **Reproducibility**: Save code, parameters, and results

## Resources

- **nilearn**: Python library for neuroimaging analysis
- **torch-geometric**: Graph neural network library
- **BrainNet Viewer**: MATLAB toolbox for brain network visualization
- **ABCD dataset**: Large-scale adolescent brain development data
- **ADNI dataset**: Alzheimer's disease neuroimaging data

## Notes

- Brain GNN is an emerging field with rapid developments
- Always validate with domain experts (neuroscientists, clinicians)
- Consider ethical implications of medical predictions
- Combine machine learning with neuroscience domain knowledge