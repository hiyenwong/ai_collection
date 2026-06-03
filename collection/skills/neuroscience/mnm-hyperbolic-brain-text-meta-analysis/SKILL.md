---
name: mnm-hyperbolic-brain-text-meta-analysis
description: "Multi-level Neuroimaging Meta-analysis (MNM) with hyperbolic brain-text representations. Leverages hyperbolic geometry and Lorentz model for hierarchical semantic alignment between neuroscience literature and brain activation maps. Activation: meta-analysis, hyperbolic geometry, Lorentz model, neuroimaging, brain-text alignment, hierarchical, small sample size, literature mining."
---

# MNM: Multi-level Neuroimaging Meta-analysis with Hyperbolic Brain-Text Representations

> Novel framework leveraging hyperbolic geometry to bridge neuroscience literature and brain activation maps for multi-level meta-analysis.

## Metadata
- **Source**: arXiv:2511.21092v1
- **Authors**: Seunghun Baek, Jaejin Lee, Jaeyoon Sim, Minjae Jeong, Won Hwa Kim
- **Published**: 2025-11-26
- **Categories**: cs.LG, cs.AI

## Core Methodology

### Problem Statement
- **Small sample sizes** limit reliability of individual neuroimaging studies
- **Traditional meta-analysis** uses keyword retrieval or linear mappings
- **Overlooked**: Rich hierarchical structure inherent in neuroimaging data

### Solution: Hyperbolic Brain-Text Representations

#### Key Innovation
Use **hyperbolic geometry** (Lorentz model) to embed both:
1. **Text** from research articles
2. **Brain activation maps**

Into a **shared hyperbolic space** that naturally captures hierarchical relationships.

#### Three Core Components

##### 1. Brain-Text Alignment
Align brain activation patterns with corresponding text descriptions in hyperbolic space, enabling:
- Semantic correspondence between literature and imaging
- Cross-modal similarity search

##### 2. Hierarchy Guidance
Guide hierarchical relationships between text and brain activations:
- Specific findings → General concepts
- Local activations → Global networks
- Task-specific → Domain-general

##### 3. Pattern Preservation
Preserve hierarchical relationships within brain activation patterns themselves:
- Subcortical → Cortical
- Primary → Associative regions
- Fine-grained → Coarse patterns

## Why Hyperbolic Space?

### Advantages over Euclidean Space
- **Natural hierarchy**: Tree-like structures embed efficiently
- **Exponential capacity**: Can represent complex taxonomies
- **Distance properties**: Similarity reflects semantic and structural relatedness
- **Biological plausibility**: Brain networks exhibit hierarchical modularity

### Lorentz Model
The hyperboloid model of hyperbolic space provides:
- Differentiable operations for gradient-based learning
- Numerical stability
- Efficient distance computations

## Implementation Guide

### Prerequisites
- PyTorch or TensorFlow
- Neuroimaging data (activation maps, coordinates)
- Text embeddings model (e.g., SciBERT, PubMedBERT)
- Poincaré or Lorentz hyperbolic embedding library

### Mathematical Background

#### Lorentz Hyperboloid Model
```
H^n = {x ∈ R^(n+1) : <x,x>_L = -1, x_0 > 0}

where <x,y>_L = -x_0*y_0 + Σ(x_i * y_i)  (Lorentz inner product)
```

#### Hyperbolic Distance
```
d_H(x, y) = arccosh(-<x, y>_L)
```

#### Exponential and Logarithmic Maps
Map between tangent space (Euclidean) and hyperboloid:
```
exp_x(v) = cosh(||v||) * x + sinh(||v||) * v/||v||
log_x(y) = d_H(x,y) * (y + <x,y>_L * x) / ||...||
```

### Step-by-Step Implementation

#### Step 1: Text Embedding in Hyperbolic Space
```python
import torch
import torch.nn as nn
import numpy as np

class LorentzEmbedding(nn.Module):
    """Embed text features into Lorentz hyperboloid"""
    def __init__(self, vocab_size, embed_dim=128):
        super().__init__()
        self.embed_dim = embed_dim
        # Initialize in tangent space (Euclidean-like)
        self.euclidean_embed = nn.Embedding(vocab_size, embed_dim)
        
    def euclidean_to_lorentz(self, x_euclid):
        """
        Map from Euclidean to Lorentz hyperboloid
        x_euclid: [batch, embed_dim]
        Returns: [batch, embed_dim+1] on H^n
        """
        # Time component
        x_0 = torch.sqrt(1 + torch.sum(x_euclid**2, dim=-1, keepdim=True))
        # Concatenate: [batch, embed_dim+1]
        x_lorentz = torch.cat([x_0, x_euclid], dim=-1)
        return x_lorentz
    
    def lorentz_distance(self, x, y):
        """Compute hyperbolic distance on Lorentz hyperboloid"""
        # Lorentz inner product: -x_0*y_0 + sum(x_i*y_i)
        lor_prod = -x[:, 0] * y[:, 0] + torch.sum(x[:, 1:] * y[:, 1:], dim=-1)
        # Numerical stability
        lor_prod = torch.clamp(lor_prod, max=-1.0001)
        return torch.arccosh(-lor_prod)
    
    def forward(self, text_indices):
        x_euclid = self.euclidean_embed(text_indices)
        x_lorentz = self.euclidean_to_lorentz(x_euclid)
        return x_lorentz

# Alternative: Using pre-trained text encoder
def embed_text_hyperbolic(texts, text_encoder, projection_layer):
    """
    texts: List of article abstracts/summaries
    text_encoder: Pre-trained model (BERT, SciBERT)
    projection_layer: Learned projection to hyperbolic space
    """
    # Get text embeddings
    text_features = text_encoder(texts)  # [batch, hidden_dim]
    
    # Project to Lorentz space
    lorentz_coords = projection_layer(text_features)
    
    # Ensure on hyperboloid
    lorentz_coords = lorentz_normalize(lorentz_coords)
    
    return lorentz_coords

def lorentz_normalize(x):
    """Project arbitrary point to Lorentz hyperboloid"""
    # Time component must satisfy x_0^2 - ||x_space||^2 = 1
    x_space = x[:, 1:]
    x_0 = torch.sqrt(1 + torch.sum(x_space**2, dim=-1, keepdim=True))
    return torch.cat([x_0, x_space], dim=-1)
```

#### Step 2: Brain Activation Embedding
```python
class BrainActivationEmbedder(nn.Module):
    """Embed fMRI activation maps into hyperbolic space"""
    def __init__(self, num_voxels, embed_dim=128):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(num_voxels, 512),
            nn.ReLU(),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Linear(256, embed_dim)  # Output in tangent space
        )
    
    def forward(self, activation_map):
        """
        activation_map: [batch, num_voxels] or [batch, X, Y, Z]
        Returns: [batch, embed_dim+1] on Lorentz hyperboloid
        """
        if activation_map.dim() == 4:  # 3D volume
            activation_map = activation_map.view(activation_map.size(0), -1)
        
        # Encode to Euclidean space
        features = self.encoder(activation_map)
        
        # Map to Lorentz space
        x_0 = torch.sqrt(1 + torch.sum(features**2, dim=-1, keepdim=True))
        lorentz_coords = torch.cat([x_0, features], dim=-1)
        
        return lorentz_coords
```

#### Step 3: Multi-level Alignment Losses
```python
class MultiLevelAlignmentLoss(nn.Module):
    """Three-component loss for brain-text alignment"""
    def __init__(self, margin=0.1):
        super().__init__()
        self.margin = margin
    
    def component1_brain_text_alignment(self, brain_emb, text_emb):
        """
        Align brain activations with corresponding text
        Minimize distance between matched pairs
        """
        distances = self.hyperbolic_distance(brain_emb, text_emb)
        return torch.mean(distances)
    
    def component2_hierarchy_guidance(self, embeddings, hierarchy_labels):
        """
        Enforce hierarchical relationships
        parent should be closer to origin than children
        distances reflect hierarchy depth
        """
        # Using hyperbolic property: deeper in hierarchy = farther from origin
        origin = torch.zeros_like(embeddings)
        origin[:, 0] = 1.0  # Origin of hyperboloid
        
        distances_to_origin = self.hyperbolic_distance(embeddings, origin)
        
        # Higher hierarchy label = closer to origin
        loss = torch.mean((distances_to_origin - (1.0 / hierarchy_labels))**2)
        return loss
    
    def component3_pattern_preservation(self, embeddings, similarity_matrix):
        """
        Preserve similarity structure from original space
        """
        # Compute pairwise hyperbolic distances
        n = embeddings.size(0)
        distances = torch.zeros(n, n)
        for i in range(n):
            for j in range(i+1, n):
                distances[i, j] = self.hyperbolic_distance(
                    embeddings[i:i+1], embeddings[j:j+1]
                )
                distances[j, i] = distances[i, j]
        
        # Match to original similarity structure
        loss = torch.mean((distances - (1 - similarity_matrix))**2)
        return loss
    
    def hyperbolic_distance(self, x, y):
        """Compute Lorentz distance"""
        lor_prod = -x[:, 0] * y[:, 0] + torch.sum(x[:, 1:] * y[:, 1:], dim=-1)
        lor_prod = torch.clamp(lor_prod, max=-1.0001)
        return torch.arccosh(-lor_prod)
    
    def forward(self, brain_emb, text_emb, hierarchy_labels, similarity_matrix):
        loss1 = self.component1_brain_text_alignment(brain_emb, text_emb)
        loss2 = self.component2_hierarchy_guidance(brain_emb, hierarchy_labels)
        loss3 = self.component3_pattern_preservation(brain_emb, similarity_matrix)
        
        return loss1 + 0.5 * loss2 + 0.3 * loss3
```

#### Step 4: Complete MNM Model
```python
class MNMFramework(nn.Module):
    """Complete Multi-level Neuroimaging Meta-analysis framework"""
    def __init__(self, vocab_size, num_voxels, embed_dim=128):
        super().__init__()
        self.text_embedder = LorentzEmbedding(vocab_size, embed_dim)
        self.brain_embedder = BrainActivationEmbedder(num_voxels, embed_dim)
        self.alignment_loss = MultiLevelAlignmentLoss()
    
    def forward(self, text_indices, brain_maps, hierarchy_labels, similarity_matrix):
        # Embed to hyperbolic space
        text_emb = self.text_embedder(text_indices)
        brain_emb = self.brain_embedder(brain_maps)
        
        # Compute multi-level alignment loss
        loss = self.alignment_loss(brain_emb, text_emb, hierarchy_labels, similarity_matrix)
        
        return loss, brain_emb, text_emb
    
    def meta_analyze(self, studies_text, studies_brain):
        """
        Perform meta-analysis by aggregating embeddings
        """
        text_emb = self.text_embedder(studies_text)
        brain_emb = self.brain_embedder(studies_brain)
        
        # Hyperbolic centroid (Frechet mean)
        consensus_text = self.hyperbolic_mean(text_emb)
        consensus_brain = self.hyperbolic_mean(brain_emb)
        
        return consensus_text, consensus_brain
    
    def hyperbolic_mean(self, embeddings, max_iter=10):
        """Compute Frechet mean in hyperbolic space"""
        # Initialize as Euclidean mean projected to hyperboloid
        mean = embeddings.mean(dim=0, keepdim=True)
        mean = lorentz_normalize(mean)
        
        for _ in range(max_iter):
            # Gradient descent on squared distances
            distances = []
            for emb in embeddings:
                dist = self.alignment_loss.hyperbolic_distance(mean, emb.unsqueeze(0))
                distances.append(dist)
            # Update mean...
        
        return mean
```

## Applications
- **Multi-study aggregation**: Combine findings from small neuroimaging studies
- **Literature-based brain mapping**: Predict activation patterns from text
- **Novel finding detection**: Identify studies that deviate from consensus
- **Research gap identification**: Find underexplored hierarchical regions
- **Knowledge graph construction**: Build neuroimaging knowledge bases

## Performance
- **Outperforms baselines**: Euclidean embeddings, keyword-based retrieval
- **Robust**: Handles small sample sizes better than traditional methods
- **Interpretable**: Hierarchical structure is explicit in embedding space

## Pitfalls
- **Optimization difficulty**: Hyperbolic optimization is less stable than Euclidean
- **Numerical precision**: Requires careful handling of arccosh for numerical stability
- **Hierarchy annotation**: Requires manual or semi-automatic hierarchy labels
- **Embedding dimension**: Trade-off between capacity and optimization difficulty
- **Computational cost**: Pairwise distance computations are O(n²)

## Related Skills
- bleg-llm-brain-graph-enhancer
- hermes-brain-connectivity
- brain-connectivity-analysis
- graph-laplacian-denoising
- hyperbolic-eeg-multimodal-learning
