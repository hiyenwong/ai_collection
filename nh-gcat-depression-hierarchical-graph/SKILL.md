---
name: nh-gcat-depression-hierarchical-graph
description: "NH-GCAT: Neurocircuitry-Inspired Hierarchical Graph Causal Attention Networks for explainable depression (MDD) identification from neuroimaging. Integrates neurobiological prior knowledge with graph causal attention for interpretable psychiatric diagnosis. Activation: depression, MDD, major depressive disorder, graph neural network, causal attention, neuroimaging, psychiatric diagnosis, explainable GNN, fMRI, hierarchical graph."
---

# NH-GCAT: Neurocircuitry-Inspired Hierarchical Graph Causal Attention Networks

> Neurobiologically interpretable GNN for MDD diagnosis that integrates brain circuit prior knowledge with hierarchical graph causal attention, producing explainable biomarker-level predictions.

## Metadata
- **Source**: arXiv:2511.17622
- **Authors**: Weidao Chen, Jiajin Liu, Hang He, Wei Zhang, Chen Qian, Yinghui Huang, Jiabo Hu, Yanjie Fu, Rui Liu, Hao Guo, Yuanyuan Xie, Dachuan Liu, Wenwen Ouyang, Lei Gao, Jianliang Fu, Xianjing Liu, Yong Liu
- **Published**: 2025-11-18

## Core Methodology

### Key Innovation
NH-GCAT combines **neurocircuitry-inspired architecture** with **hierarchical graph causal attention** to create an explainable depression diagnosis system. Unlike black-box GNNs, it encodes known depression-related neurocircuits (e.g., default mode network, limbic system) as graph topology priors, then uses causal attention to discover biomarkers that have causal relationships with MDD.

### Problem Addressed
- Existing GNN-based psychiatric diagnosis methods are black boxes
- Brain graph construction ignores known neurobiological circuitry
- No causal reasoning between discovered biomarkers and clinical outcomes
- Depression diagnosis needs both accuracy AND interpretability for clinical adoption

### Technical Framework
1. **Neurocircuitry-guided graph construction**: Build brain graphs where edges reflect known functional circuits implicated in MDD
2. **Hierarchical graph attention**: Multi-level attention captures both local circuit dynamics and global network patterns
3. **Causal attention mechanism**: Identifies causal (not just correlational) relationships between brain features and depression
4. **Explainable output**: Produces attention-weighted brain region importance maps aligned with neurobiological knowledge

## Implementation Guide

### Prerequisites
- fMRI or structural MRI data (preprocessed, parcellated)
- Depression labels (MDD vs healthy control)
- Python: `torch`, `torch_geometric`, `numpy`
- Brain atlas (e.g., AAL, Desikan-Killiany)

### Step-by-Step
1. **Construct neurocircuitry graph**: Define adjacency based on known MDD-related circuits (DMN, CEN, SN, limbic)
2. **Build hierarchical GNN**: Stack graph attention layers at multiple scales (region → circuit → network)
3. **Train with causal attention**: Use causal discovery loss to ensure attention weights reflect causal biomarkers
4. **Extract explanations**: Visualize attention maps on brain surface for clinical interpretation

### Code Example
```python
import torch
import torch.nn as nn
from torch_geometric.nn import GATConv, global_mean_pool

class NHGCATLayer(nn.Module):
    """Neurocircuitry-inspired Hierarchical Graph Causal Attention Layer."""
    
    def __init__(self, in_dim, out_dim, n_heads=4):
        super().__init__()
        self.gat = GATConv(in_dim, out_dim // n_heads, heads=n_heads, dropout=0.3)
        self.causal_gate = nn.Sequential(
            nn.Linear(out_dim, out_dim),
            nn.Sigmoid()
        )
    
    def forward(self, x, edge_index, circuit_mask=None):
        # Graph attention
        h, attn_weights = self.gat(x, edge_index, return_attention_weights=True)
        
        # Causal gating: modulate by circuit prior
        if circuit_mask is not None:
            gate = self.causal_gate(h)
            h = h * gate * circuit_mask.unsqueeze(-1)
        
        return h, attn_weights

class NHGCAT(nn.Module):
    """Full NH-GCAT model for depression classification."""
    
    def __init__(self, n_regions, n_features, hidden_dim=64, n_classes=2):
        super().__init__()
        # Hierarchical layers: region → circuit → network
        self.layer1 = NHGCATLayer(n_features, hidden_dim)
        self.layer2 = NHGCATLayer(hidden_dim, hidden_dim)
        self.layer3 = NHGCATLayer(hidden_dim, hidden_dim)
        self.classifier = nn.Sequential(
            nn.Linear(hidden_dim, 32),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(32, n_classes)
        )
    
    def forward(self, x, edge_index, batch, circuit_masks=None):
        masks = circuit_masks or [None, None, None]
        h, _ = self.layer1(x, edge_index, masks[0])
        h = torch.relu(h)
        h, _ = self.layer2(h, edge_index, masks[1])
        h = torch.relu(h)
        h, attn = self.layer3(h, edge_index, masks[2])
        
        # Pool to graph-level
        graph_emb = global_mean_pool(h, batch)
        logits = self.classifier(graph_emb)
        return logits, attn
```

## Applications
- **MDD diagnosis**: Automated depression identification from brain imaging with explainable biomarkers
- **Psychiatric neuroimaging**: Framework adaptable to other disorders (schizophrenia, anxiety)
- **Clinical decision support**: Attention maps help clinicians understand model predictions
- **Neurocircuitry validation**: Discovered causal circuits can validate or challenge neurobiological theories

## Pitfalls
- Requires carefully curated neurocircuitry priors — poor priors hurt performance
- Small clinical sample sizes common in neuroimaging — use data augmentation
- Causal claims require careful validation (interventional data preferred)
- Cross-site generalization remains challenging

## Related Skills
- explainable-gnn-eeg-neurological
- brain-graph-neural
- multimodal-brain-connectivity-gnn
- drl-gnn-brain-network
