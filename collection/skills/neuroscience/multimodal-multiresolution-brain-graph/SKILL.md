---
name: skill.md---multimodal-multiresolution-brain-graph-
description: Skill for AI agent capabilities
---

# SKILL.md - Multimodal Multiresolution Brain Graph Integration

## Activation Keywords

- M2GraphIntegrator, connectional brain template, CBT
- multimodal brain graph, multiresolution integration
- brain connectivity mapping, graph autoencoder
- brain connectome augmentation, cross-modality

## What It Does

M2GraphIntegrator is a multimodal multiresolution graph integration framework that maps a population of brain connectomes (from different modalities and resolutions) into a centered Connectional Brain Template (CBT). The CBT can generate realistic multimodal brain connectomes for downstream tasks.

## When To Use

**Use this skill when:**
- Integrating brain graphs from multiple modalities (fMRI, DTI)
- Unifying brain graphs at different resolutions
- Generating connectional brain templates
- Augmenting brain connectome datasets
- Building population-level brain connectivity fingerprints

**Do NOT use for:**
- Single modality analysis (no integration needed)
- Fixed resolution brain networks
- Individual brain network analysis (CBT is population-level)

## How To Use

### Step-by-Step Workflow

1. **Collect Multimodal Brain Graphs**
   - Functional connectivity (fMRI)
   - Structural connectivity (DTI)
   - Different resolutions (parcellations)

2. **Unify Resolutions**
   - Use resolution-specific graph autoencoders
   - Map to fixed-size latent space
   - Preserve graph structure

3. **Integrate Modalities**
   - Cross-modality graph fusion
   - Learn universal representation
   - Generate centered CBT

4. **Preserve Population Diversity**
   - Clustering-based sample selection
   - Use heterogeneous training samples
   - Avoid mode collapse

5. **Generate New Connectomes**
   - Sample from CBT
   - Generate multimodal graphs
   - Augment datasets

### Key Components

| Component | Purpose | Method |
|-----------|---------|--------|
| Resolution autoencoder | Unify graph sizes | Graph VAE |
| Modality integrator | Cross-modality fusion | Attention/GNN |
| CBT generator | Population template | Centered learning |
| Topological loss | Biological validity | Gromov-Hausdorff |

### CBT Properties

**Centeredness:**
```
CBT = argmin_T Σᵢ d(T, Gᵢ)
```

**Topological soundness:**
```
L_topo = Σᵢ |topology(T) - topology(Gᵢ)|
```

## Example Usage

### Building Connectional Brain Template

**Problem:** Integrate multimodal brain graphs into universal CBT

**Implementation:**
```python
import torch
import torch.nn as nn
from torch_geometric.nn import GCNConv, GAE

class M2GraphIntegrator(nn.Module):
    def __init__(self, input_dims, hidden_dim=64, latent_dim=32):
        """
        Multimodal Multiresolution Brain Graph Integrator
        
        Parameters:
        -----------
        input_dims : dict
            {resolution: {modality: dim}} for each input type
        hidden_dim : int
            Hidden layer dimension
        latent_dim : int
            Latent space dimension
        """
        super().__init__()
        
        # Resolution-specific autoencoders
        self.resolution_encoders = nn.ModuleDict()
        self.resolution_decoders = nn.ModuleDict()
        
        for res in input_dims:
            encoders = nn.ModuleDict()
            decoders = nn.ModuleDict()
            for mod, dim in input_dims[res].items():
                encoders[mod] = GCNConv(dim, latent_dim)
                decoders[mod] = GCNConv(latent_dim, dim)
            self.resolution_encoders[res] = encoders
            self.resolution_decoders[res] = decoders
        
        # Modality integrator
        self.integrator = nn.MultiheadAttention(latent_dim, num_heads=4)
        
        # CBT generator
        self.cbt_head = nn.Linear(latent_dim, latent_dim)
    
    def encode(self, graphs, resolution, modality, edge_index):
        """
        Encode graph to latent space
        """
        encoder = self.resolution_encoders[resolution][modality]
        z = encoder(graphs, edge_index)
        return z
    
    def integrate_modalities(self, latent_reps):
        """
        Integrate latent representations from multiple modalities
        """
        # Stack and apply attention
        stacked = torch.stack(latent_reps, dim=0)  # (n_modalities, batch, latent)
        integrated, _ = self.integrator(stacked, stacked, stacked)
        return integrated.mean(dim=0)  # (batch, latent)
    
    def forward(self, graphs_list, edge_indices, resolutions, modalities):
        """
        Generate CBT from multimodal multiresolution graphs
        """
        # Encode all graphs
        latent_reps = []
        for graphs, edge_idx, res, mod in zip(graphs_list, edge_indices, resolutions, modalities):
            z = self.encode(graphs, res, mod, edge_idx)
            latent_reps.append(z)
        
        # Integrate
        integrated = self.integrate_modalities(latent_reps)
        
        # Generate CBT
        cbt = self.cbt_head(integrated)
        
        return cbt
    
    def generate_connectomes(self, cbt, target_resolution, target_modality, edge_index):
        """
        Generate brain graphs from CBT
        """
        decoder = self.resolution_decoders[target_resolution][target_modality]
        graphs = decoder(cbt, edge_index)
        return graphs
```

### Training with Topological Loss

**Analysis:**
```python
def train_cbt(model, population_graphs, epochs=100):
    """
    Train M2GraphIntegrator to learn CBT
    """
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    
    for epoch in range(epochs):
        # Select heterogeneous samples
        samples = select_diverse_samples(population_graphs)
        
        # Forward pass
        cbt = model(samples.graphs, samples.edges, 
                   samples.resolutions, samples.modalities)
        
        # Reconstruction loss
        recon_loss = 0
        for res in samples.resolutions:
            for mod in samples.modalities:
                generated = model.generate_connectomes(cbt, res, mod, samples.edges[res])
                recon_loss += F.mse_loss(generated, samples.originals[res][mod])
        
        # Topological loss
        topo_loss = compute_topological_loss(cbt, samples)
        
        # Centeredness loss
        center_loss = compute_centeredness_loss(cbt, samples)
        
        # Total loss
        loss = recon_loss + 0.1 * topo_loss + 0.1 * center_loss
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    
    return model

def compute_topological_loss(cbt, samples):
    """
    Minimize topological gap between CBT and ground truth
    """
    # Compute graph invariants
    cbt_topology = compute_graph_invariants(cbt)
    sample_topology = [compute_graph_invariants(g) for g in samples]
    
    # Topological distance
    topo_dist = sum(abs(cbt_topology - s_top) for s_top in sample_topology)
    
    return topo_dist.mean()
```

### Augmenting Brain Connectome Datasets

**Analysis:**
```python
def augment_dataset(model, cbt, n_samples=100, resolutions=['low', 'high'], 
                   modalities=['fMRI', 'DTI']):
    """
    Generate new brain connectomes from CBT
    """
    augmented = []
    
    for _ in range(n_samples):
        # Add noise for diversity
        z = cbt + torch.randn_like(cbt) * 0.1
        
        for res in resolutions:
            for mod in modalities:
                graphs = model.generate_connectomes(z, res, mod)
                augmented.append({
                    'resolution': res,
                    'modality': mod,
                    'graph': graphs.detach()
                })
    
    return augmented
```

## Key Advantages

| Advantage | Benefit |
|-----------|---------|
| Multimodal integration | Combines fMRI + DTI |
| Multiresolution | Works across parcellations |
| CBT generation | Population fingerprint |
| Augmentation | Generates new connectomes |
| Topological soundness | Biologically valid |

## Description

SKILL.md - Multimodal Multiresolution Brain Graph Integration

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: Collect Multimodal Brain Graphs

### Step 2: Unify Resolutions

### Step 3: Integrate Modalities

### Step 4: Preserve Population Diversity

### Step 5: Generate New Connectomes

## Examples

### Example 1: Basic Application

**User:** I need to apply SKILL.md - Multimodal Multiresolution Brain Graph Integration to my analysis.

**Agent:** I'll help you apply multimodal-multiresolution-brain-graph. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for multimodal-multiresolution-brain-graph?

**Agent:** Let me search for the latest research and best practices...

## Related Skills

- **multimodal-brain-connectivity-gnn** - Multimodal GNN
- **brain-graph-augmentation-template** - Graph augmentation
- **functional-connectome-fingerprint** - Brain fingerprinting

## Source

- arXiv:2209.13529v1
- Title: Deep Cross-Modality and Resolution Graph Integration for Universal Brain Connectivity Mapping and Augmentation
- Utility: 0.87
- Authors: Islem Rekik et al.

## Notes

- Key innovation: First multimodal multiresolution graph integration
- Uses resolution-specific graph autoencoders
- Clustering-based diverse sample selection
- Topological loss for biological validity
- Applications: brain state classification, dataset augmentation
- Can generate CBT from heterogeneous connectomic data

---

_Created: 2026-04-01_