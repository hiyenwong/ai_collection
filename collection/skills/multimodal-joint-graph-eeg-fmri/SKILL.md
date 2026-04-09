# Multimodal Joint Graph Representation EEG-fMRI

**Source:** arXiv:2201.08747
**Utility:** 0.94
**Created:** 2026-03-25

## Activation Keywords

- EEG-fMRI joint representation
- multimodal brain dynamics
- EEG fMRI fusion
- joint graph representation
- nonlinear fusion brain
- spatiotemporal neural dynamics

## Description

A framework for inferring brain dynamics through multimodal joint graph representation of simultaneously acquired EEG and fMRI data, using nonlinear fusion methods to extract brain components across temporal and spatial dimensions.

## Core Methodology

### 1. Problem: Multimodal Brain Analysis

**Challenge:**
- EEG: High temporal resolution, low spatial resolution
- fMRI: High spatial resolution, low temporal resolution
- Each modality alone provides incomplete picture

**Solution:** Joint representation combining complementary strengths

### 2. Key Concepts

**Joint Graph Representation:**
- Represents both modalities in unified graph structure
- Captures spatiotemporal dynamics
- Preserves modality-specific features

**Nonlinear Fusion:**
- Extracts brain components in different dimensions
- Temporal: EEG dynamics
- Spatial: fMRI activation patterns

**Graph-Based Analysis:**
- Similarities to brain structure
- Overcomes complexity of brain mapping
- Enables cross-modal correlation

### 3. Technical Approach

1. **EEG Graph Construction**
   - Nodes: Electrodes
   - Edges: Functional connectivity

2. **fMRI Graph Construction**
   - Nodes: Brain regions (ROIs)
   - Edges: Functional connectivity

3. **Joint Representation**
   - Cross-modal alignment
   - Shared latent space
   - Temporal-spatial mapping

## Implementation Framework

```python
# Conceptual multimodal joint graph framework
import torch
import torch.nn as nn
from torch_geometric.nn import GCNConv

class MultimodalJointGraphEncoder(nn.Module):
    """
    Joint graph representation for EEG-fMRI
    """
    
    def __init__(self, eeg_channels, fmri_rois, hidden_dim=128):
        super().__init__()
        
        # EEG encoder (temporal focus)
        self.eeg_gcn = nn.ModuleList([
            GCNConv(eeg_channels, hidden_dim),
            GCNConv(hidden_dim, hidden_dim)
        ])
        
        # fMRI encoder (spatial focus)
        self.fmri_gcn = nn.ModuleList([
            GCNConv(fmri_rois, hidden_dim),
            GCNConv(hidden_dim, hidden_dim)
        ])
        
        # Joint fusion layer
        self.fusion = nn.Sequential(
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim)
        )
    
    def forward(self, eeg_data, fmri_data, eeg_adj, fmri_adj):
        """
        Args:
            eeg_data: EEG signals [batch, channels, time]
            fmri_data: fMRI signals [batch, rois, time]
            eeg_adj: EEG connectivity [batch, channels, channels]
            fmri_adj: fMRI connectivity [batch, rois, rois]
        Returns:
            Joint representation [batch, hidden_dim]
        """
        # Encode EEG
        eeg_embed = eeg_data
        for gcn in self.eeg_gcn:
            eeg_embed = torch.relu(gcn(eeg_embed, eeg_adj))
        
        # Encode fMRI
        fmri_embed = fmri_data
        for gcn in self.fmri_gcn:
            fmri_embed = torch.relu(gcn(fmri_embed, fmri_adj))
        
        # Fuse modalities
        joint = torch.cat([eeg_embed.mean(dim=1), fmri_embed.mean(dim=1)], dim=-1)
        joint = self.fusion(joint)
        
        return joint

class NonlinearFusionModule(nn.Module):
    """
    Nonlinear fusion for extracting cross-modal components
    """
    
    def __init__(self, input_dim, output_dim):
        super().__init__()
        self.temporal_branch = nn.Sequential(
            nn.Linear(input_dim, output_dim),
            nn.ReLU(),
            nn.Linear(output_dim, output_dim)
        )
        self.spatial_branch = nn.Sequential(
            nn.Linear(input_dim, output_dim),
            nn.ReLU(),
            nn.Linear(output_dim, output_dim)
        )
    
    def forward(self, eeg_features, fmri_features):
        # Temporal components from EEG
        temporal = self.temporal_branch(eeg_features)
        
        # Spatial components from fMRI
        spatial = self.spatial_branch(fmri_features)
        
        # Cross-modal correlation
        correlation = torch.matmul(temporal, spatial.transpose(-1, -2))
        
        return temporal, spatial, correlation
```

## Applications

### 1. Brain Dynamics Analysis
- Simultaneous spatiotemporal mapping
- Neural dynamics inference
- Brain component extraction

### 2. Neuroplasticity Studies
- Functional change diagnosis
- Temporal shift correlations
- Cross-modal overlap detection

### 3. Clinical Applications
- Epilepsy monitoring
- Sleep studies
- Cognitive state assessment

## When to Use

- Simultaneously acquired EEG-fMRI data
- Need spatiotemporal brain dynamics
- Multimodal brain analysis
- Neuroplasticity research

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: EEG Graph Construction

### Step 2: fMRI Graph Construction

### Step 3: Joint Representation

### Step 4: Understand the Request

### Step 5: Search for Information

### When to Apply
- Simultaneously acquired EEG-fMRI data
- Need spatiotemporal brain dynamics
- Multimodal brain analysis

## Examples

### Example 1: Basic Application

**User:** I need to apply Multimodal Joint Graph Representation EEG-fMRI to my analysis.

**Agent:** I'll help you apply multimodal-joint-graph-eeg-fmri. First, let me understand your specific use case...

**Context:** Problem: Multimodal Brain Analysis

### Example 2: Advanced Scenario

**User:** Simultaneously acquired EEG-fMRI data

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for multimodal-joint-graph-eeg-fmri?

**Agent:** Let me search for the latest research and best practices...

## Related Skills

- `multimodal-brain-connectivity-gnn` - Multi-modal GNN approaches
- `eeg-brain-connectivity-bci` - EEG connectivity analysis
- `time-varying-brain-connectivity` - Dynamic connectivity

## References

- Mirakhorli, J., et al. "Inferring Brain Dynamics via Multimodal Joint Graph Representation EEG-fMRI." arXiv:2201.08747 (2022)
- EEG-fMRI fusion literature
- Multimodal neuroimaging analysis