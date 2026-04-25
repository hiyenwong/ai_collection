---
name: gnn-visual-category-decoding-functional-networks
description: "GNN-based visual category decoding from fMRI functional brain networks — signed graph neural network with sparse edge masks and class-specific saliency for decoding sports, food, and vehicles from 7T fMRI data. Activation: fMRI decoding, visual category, GNN, brain network, graph neural network, saliency, functional connectivity."
---

# GNN Visual Category Decoding from Functional Brain Networks

> Decodes visual object categories (sports, food, vehicles) from 7T fMRI data using signed Graph Neural Networks with learned sparse edge masks and class-specific saliency maps, revealing category-discriminative brain network patterns.

## Metadata
- **Source**: arXiv:2603.28931
- **Authors**: Shira Karmi, Galia Avidan, Tamara Riklin Raviv
- **Published**: 2026-03-30
- **Categories**: cs.CV, q-bio.NC

## Core Methodology

### Key Innovation
A signed Graph Neural Network framework that simultaneously learns to decode visual categories from fMRI brain activity while discovering which functional connections are most discriminative for each category. The method introduces sparse edge masks and class-specific saliency, enabling interpretable brain network analysis.

### Technical Framework

#### 1. Brain Network Construction from 7T fMRI
- Ultra-high-field 7 Tesla fMRI data provides superior spatial resolution
- Brain regions treated as graph nodes
- Functional connectivity (correlation) between region time-series defines edge weights
- Signed edges: positive correlations (co-activation) and negative correlations (anti-correlation) preserved

#### 2. Signed Graph Neural Network (Signed GNN)
- Operates on signed graphs where edges carry both positive and negative weights
- Message passing respects edge sign: excitatory vs. inhibitory influence
- Node features: fMRI activity patterns per region
- Edge features: signed functional connectivity values

#### 3. Sparse Edge Mask Learning
- Learnable binary/soft masks on graph edges
- Promotes sparsity via L1 regularization or hard thresholding
- Identifies the minimal set of functional connections needed for decoding
- Reduces overfitting on high-dimensional fMRI connectivity matrices

#### 4. Class-Specific Saliency Maps
- Separate saliency computation per visual category
- Highlights brain connections most informative for sports vs. food vs. vehicles
- Enables neuroscientific interpretation: which network patterns distinguish categories
- Gradient-based or perturbation-based saliency methods

## Implementation Guide

### Prerequisites
- fMRI preprocessing pipeline (FSL, SPM, or nilearn)
- PyTorch Geometric (PyG) for GNN implementation
- 7T fMRI dataset with visual category labels

### Step-by-Step

1. **Preprocess fMRI and extract ROI time-series**
   - Standard preprocessing: motion correction, spatial normalization, smoothing
   - Parcellate brain into ROIs using atlas (e.g., Glasser, Schaefer)
   - Extract mean time-series per ROI per trial

2. **Construct signed functional connectivity graphs**
   ```python
   import numpy as np
   
   def build_signed_graph(roi_timeseries, threshold=0.1):
       """Build signed FC graph from ROI time-series."""
       n_rois = roi_timeseries.shape[0]
       corr_matrix = np.corrcoef(roi_timeseries)
       # Keep signed values, apply threshold for sparsity
       adj_matrix = corr_matrix * (np.abs(corr_matrix) > threshold)
       return adj_matrix  # Contains both + and - values
   ```

3. **Implement Signed GNN with sparse edge masks**
   ```python
   import torch
   import torch.nn as nn
   
   class SignedGNNLayer(nn.Module):
       def __init__(self, in_dim, out_dim):
           super().__init__()
           self.linear_pos = nn.Linear(in_dim, out_dim)
           self.linear_neg = nn.Linear(in_dim, out_dim)
       
       def forward(self, x, adj):
           # Separate positive and negative edges
           pos_adj = torch.clamp(adj, min=0)
           neg_adj = torch.clamp(adj, max=0).abs()
           
           # Signed message passing
           pos_msg = torch.matmul(pos_adj, self.linear_pos(x))
           neg_msg = torch.matmul(neg_adj, self.linear_neg(x))
           return pos_msg - neg_msg
   
   class SparseEdgeMask(nn.Module):
       def __init__(self, n_edges):
           super().__init__()
           self.logits = nn.Parameter(torch.randn(n_edges))
       
       def forward(self, hard=False):
           if hard:
               return (self.logits > 0).float()
           return torch.sigmoid(self.logits)
   ```

4. **Train with category labels and compute saliency**
   - Cross-entropy loss for category classification
   - Sparsity penalty on edge masks
   - Compute class-specific saliency via gradient attribution

5. **Interpret saliency maps**
   - Map high-saliency edges back to brain anatomy
   - Identify category-selective network motifs
   - Compare with known visual processing hierarchies

## Applications
- **Visual neuroscience**: Identify brain network signatures for object categories
- **Brain-computer interfaces**: Decode perceived content from brain activity
- **Clinical biomarkers**: Altered visual processing in neurological conditions
- **Neuroimaging analysis**: Interpretable GNN framework for connectivity-based classification
- **Cognitive neuroscience**: Understand how visual categories are represented in distributed networks

## Key Results
- Successful decoding of sports, food, and vehicle categories from 7T fMRI
- Signed GNN outperforms unsigned alternatives
- Sparse edge masks reveal interpretable discriminative connections
- Class-specific saliency maps highlight distinct network patterns per category

## Pitfalls
- 7T fMRI data is not universally available — field strength matters for resolution
- Signed graph construction requires careful thresholding to avoid spurious negative correlations
- Small sample sizes typical in fMRI studies risk overfitting — sparsity regularization is critical
- Motion artifacts can introduce false functional connections
- Atlas choice (parcellation) affects graph structure and downstream results

## Related Skills
- brain-graph-neural
- multimodal-brain-connectivity-gnn
- brain-network-controllability
- visual-imagery-decoding-fmri
- eeg2vision-multimodal-eeg-framework-2d-visual
