---
name: dcgl-multimodal-mdd-detection
description: "Dual Cross-Attention Graph Learning Framework for multimodal MRI-based Major Depressive Disorder (MDD) detection. Integrates sMRI and fMRI through graph neural networks with cross-modal attention. Use when: MDD detection, multimodal brain imaging, graph neural network for psychiatric diagnosis, MRI fusion, depression classification, cross-modal brain analysis."
---

# Dual Cross-Attention Graph Learning for MDD Detection

## Overview

Major Depressive Disorder (MDD) detection via multimodal MRI using:
- **Intra-modal graph learning**: sMRI (structural) and fMRI (functional) processed independently via GNNs
- **Cross-modal attention**: Bidirectional attention between modalities for complementary information fusion
- **Joint classification**: Unified prediction from fused multimodal representations

## Source

**Paper:** A Dual Cross-Attention Graph Learning Framework For Multimodal MRI-Based Major Depressive Disorder Detection
**arXiv:** 2604.10116v1

## Architecture

Each modality builds a brain graph (nodes=ROIs, edges=connectivity), then bidirectional cross-attention fuses the representations.

## Implementation

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class GraphConvBlock(nn.Module):
    def __init__(self, in_dim, out_dim):
        super().__init__()
        self.linear = nn.Linear(in_dim, out_dim)
        self.bn = nn.BatchNorm1d(out_dim)
    
    def forward(self, x, adj):
        out = torch.bmm(adj, x)
        out = self.linear(out)
        out = self.bn(out)
        return F.elu(out)

class DualCrossAttentionGNN(nn.Module):
    def __init__(self, node_dim=64, hidden=128, n_regions=90):
        super().__init__()
        
        self.smri_gnn = nn.Sequential(
            GraphConvBlock(node_dim, hidden),
            GraphConvBlock(hidden, hidden),
            GraphConvBlock(hidden, hidden)
        )
        self.fmri_gnn = nn.Sequential(
            GraphConvBlock(node_dim, hidden),
            GraphConvBlock(hidden, hidden),
            GraphConvBlock(hidden, hidden)
        )
        
        self.smri_to_fmri = nn.MultiheadAttention(hidden, num_heads=4, batch_first=True)
        self.fmri_to_smri = nn.MultiheadAttention(hidden, num_heads=4, batch_first=True)
        
        self.classifier = nn.Sequential(
            nn.Linear(hidden * 2, hidden),
            nn.ELU(),
            nn.Dropout(0.5),
            nn.Linear(hidden, 1)
        )
    
    def forward(self, smri_x, smri_adj, fmri_x, fmri_adj):
        smri_repr = self.smri_gnn(smri_x, smri_adj)
        fmri_repr = self.fmri_gnn(fmri_x, fmri_adj)
        
        smri_enhanced, _ = self.smri_to_fmri(smri_repr, fmri_repr, fmri_repr)
        fmri_enhanced, _ = self.fmri_to_smri(fmri_repr, smri_repr, smri_repr)
        
        smri_out = (smri_repr + smri_enhanced).mean(dim=1)
        fmri_out = (fmri_repr + fmri_enhanced).mean(dim=1)
        
        fused = torch.cat([smri_out, fmri_out], dim=-1)
        return self.classifier(fused)
```

## Key Insights

1. **MDD is multimodal**: Structural (gray matter volume) AND functional (network connectivity) changes
2. **Cross-modal attention > simple concatenation**: Each modality selectively attends to relevant information in the other
3. **Graph structure is essential**: Brain networks are inherently graph-structured

## Applications

- Automated MDD screening and diagnosis
- Biomarker discovery for depression subtypes
- Treatment response prediction
- Multi-site clinical studies

## Activation Keywords
- MDD detection, depression classification, multimodal MRI, cross-attention GNN
- brain graph learning, psychiatric diagnosis, sMRI fMRI fusion
