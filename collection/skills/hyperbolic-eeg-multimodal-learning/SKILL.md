---
name: hyperbolic-eeg-multimodal-learning
description: "Hyperbolic Mixture-of-Curvature Experts framework for EEG-based multimodal learning. Uses hyperbolic geometry to capture hierarchical relationships in brain signals with multiple experts specializing in different curvature geometries. Activation: hyperbolic EEG, mixture-of-curvature experts, hierarchical brain signal learning, hyperbolic neural representation."
---

# Hyperbolic EEG Multimodal Learning

Hyperbolic Mixture-of-Curvature Experts (HyperMoCE) framework for EEG-based multimodal learning that captures hierarchical relationships in brain signals.

## Motivation

EEG data exhibits unique hierarchical and tree-like structure:
- **Frequency bands**: Delta < Theta < Alpha < Beta < Gamma (hierarchy)
- **Spatial organization**: Local potentials → Regional activity → Global patterns
- **Temporal structure**: Single spikes → Bursts → Rhythmic activity

**Problem**: Euclidean space cannot adequately represent these hierarchical relationships.
**Solution**: Hyperbolic space with mixture of curvature experts.

## Core Concepts

### Hyperbolic Geometry for Hierarchies

Hyperbolic space expands exponentially, making it ideal for hierarchical data:

```
Euclidean vs Hyperbolic Distance
─────────────────────────────────────

Euclidean: Distance grows linearly with depth
Hyperbolic: Distance grows exponentially with depth

Hierarchical Tree in Hyperbolic Space:

              Root
            /  |  \
           /   |   \
         Node Node Node
         /|\   /|\   /|\
        ... (exponential expansion)
```

### Poincaré Ball Model

Maps hyperbolic space to unit ball:

```python
def poincare_distance(x, y, c=1.0):
    """
    Distance in Poincaré ball model
    
    d(x,y) = arccosh(1 + 2c||x-y||² / ((1-c||x||²)(1-c||y||²)))
    """
    sqrt_c = np.sqrt(c)
    
    x_sqnorm = np.sum(x * x, axis=-1, keepdims=True)
    y_sqnorm = np.sum(y * y, axis=-1, keepdims=True)
    
    xy_norm_sq = np.sum((x - y) ** 2, axis=-1, keepdims=True)
    
    num = 2 * c * xy_norm_sq
    denom = (1 - c * x_sqnorm) * (1 - c * y_sqnorm)
    
    return np.arccosh(1 + num / denom) / sqrt_c
```

## Architecture

### Mixture-of-Curvature Experts

```
┌─────────────────────────────────────────────────────────────────────┐
│              HYPERBOLIC MIXTURE-OF-CURVATURE EXPERTS                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Input: EEG Features + Auxiliary Modality (e.g., Eye Tracking)      │
│                                                                     │
│           ┌─────────┐  ┌─────────┐  ┌─────────┐                    │
│           │ Expert 0│  │ Expert 1│  │ Expert N│                    │
│           │(c=low)  │  │(c=med)  │  │(c=high) │                    │
│           │ ─────── │  │ ─────── │  │ ─────── │                    │
│     ────►│Euclid-like│►│Balanced │►│Hyperbolic│                   │
│           │ Flat    │  │ Curved  │  │ Strong  │                    │
│           └────┬────┘  └────┬────┘  └────┬────┘                    │
│                │            │            │                          │
│                └────────────┼────────────┘                          │
│                             ▼                                       │
│                    ┌─────────────────┐                              │
│                    │  Gating Network │                              │
│                    │  (Attention)    │                              │
│                    └────────┬────────┘                              │
│                             ▼                                       │
│                    Weighted Combination                             │
│                             │                                       │
│                             ▼                                       │
│                    ┌─────────────────┐                              │
│                    │  Classification/│                              │
│                    │  Regression     │                              │
│                    └─────────────────┘                              │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Different Curvature Values

```python
# Curvature determines the "strength" of hyperbolicity
curvature_experts = {
    'expert_0': {'c': 0.0,   'type': 'Euclidean-like'},  # Flat
    'expert_1': {'c': 0.1,   'type': 'Mild hyperbolic'},
    'expert_2': {'c': 0.5,   'type': 'Moderate hyperbolic'},
    'expert_3': {'c': 1.0,   'type': 'Strong hyperbolic'},
}

# Higher c = more curved = better for deep hierarchies
```

## Implementation

### 1. Hyperbolic Neural Networks

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class HyperbolicLinear(nn.Module):
    """Linear layer in hyperbolic space"""
    
    def __init__(self, in_dim, out_dim, c=1.0):
        super().__init__()
        self.c = c
        self.linear = nn.Linear(in_dim, out_dim, bias=True)
        
    def poincare_proj(self, x):
        """Project to Poincaré ball"""
        norm = torch.norm(x, dim=-1, keepdim=True)
        # Ensure ||x|| < 1/sqrt(c)
        max_norm = (1 - 1e-5) / torch.sqrt(torch.tensor(self.c))
        return x * torch.min(torch.ones_like(norm), max_norm / (norm + 1e-5))
    
    def forward(self, x):
        """Forward pass with hyperbolic operations"""
        # Map to tangent space
        x_tangent = self.poincare_to_tangent(x)
        
        # Linear operation in tangent space
        y_tangent = self.linear(x_tangent)
        
        # Map back to hyperbolic space
        y = self.tangent_to_poincare(y_tangent, x)
        
        return y
    
    def poincare_to_tangent(self, x):
        """Map from Poincaré ball to tangent space at origin"""
        return x * 2.0 / (1 - self.c * torch.sum(x ** 2, dim=-1, keepdim=True))
    
    def tangent_to_poincare(self, v, x):
        """Map from tangent space back to Poincaré ball"""
        # Möbius addition
        v_norm = torch.norm(v, dim=-1, keepdim=True)
        x_norm = torch.norm(x, dim=-1, keepdim=True)
        
        lambda_x = 2.0 / (1 - self.c * x_norm ** 2)
        
        numerator = (1 + 2 * self.c * torch.sum(x * v, dim=-1, keepdim=True) + 
                    self.c * v_norm ** 2) * x + (1 - self.c * x_norm ** 2) * v
        denominator = 1 + 2 * self.c * torch.sum(x * v, dim=-1, keepdim=True) + \
                     self.c ** 2 * x_norm ** 2 * v_norm ** 2
        
        return numerator / (denominator + 1e-5)
```

### 2. Curvature Expert

```python
class CurvatureExpert(nn.Module):
    """Single expert with specific curvature"""
    
    def __init__(self, input_dim, hidden_dim, output_dim, curvature=1.0):
        super().__init__()
        self.curvature = curvature
        self.curvature_type = 'flat' if curvature < 0.01 else 'hyperbolic'
        
        if self.curvature_type == 'flat':
            # Euclidean layers
            self.layers = nn.Sequential(
                nn.Linear(input_dim, hidden_dim),
                nn.ReLU(),
                nn.Linear(hidden_dim, hidden_dim),
                nn.ReLU(),
                nn.Linear(hidden_dim, output_dim)
            )
        else:
            # Hyperbolic layers
            self.layers = nn.Sequential(
                HyperbolicLinear(input_dim, hidden_dim, curvature),
                nn.ReLU(),
                HyperbolicLinear(hidden_dim, hidden_dim, curvature),
                nn.ReLU(),
                HyperbolicLinear(hidden_dim, output_dim, curvature)
            )
    
    def forward(self, x):
        return self.layers(x)
```

### 3. Gating Network

```python
class GatingNetwork(nn.Module):
    """Adaptive gating for expert mixture"""
    
    def __init__(self, input_dim, num_experts):
        super().__init__()
        self.num_experts = num_experts
        
        # Multi-head attention for gating
        self.attention = nn.MultiheadAttention(
            embed_dim=input_dim,
            num_heads=4,
            batch_first=True
        )
        
        # Output layer for expert weights
        self.gate = nn.Sequential(
            nn.Linear(input_dim, input_dim // 2),
            nn.ReLU(),
            nn.Linear(input_dim // 2, num_experts)
        )
        
    def forward(self, x):
        """
        Compute expert weights
        
        Returns:
            weights: (batch, num_experts) softmax weights
        """
        # Self-attention
        attended, _ = self.attention(x, x, x)
        
        # Global pooling
        pooled = torch.mean(attended, dim=1)
        
        # Compute gates
        logits = self.gate(pooled)
        weights = F.softmax(logits, dim=-1)
        
        return weights
```

### 4. Full HyperMoCE Model

```python
class HyperbolicMoCE(nn.Module):
    """
    Hyperbolic Mixture-of-Curvature Experts for EEG Multimodal Learning
    """
    
    def __init__(self, 
                 eeg_dim=64,
                 aux_dim=32,
                 hidden_dim=128,
                 output_dim=10,
                 num_experts=4,
                 curvatures=[0.0, 0.1, 0.5, 1.0]):
        super().__init__()
        
        self.num_experts = num_experts
        
        # Input projection for each modality
        self.eeg_proj = nn.Linear(eeg_dim, hidden_dim)
        self.aux_proj = nn.Linear(aux_dim, hidden_dim)
        
        # Fusion layer
        self.fusion = nn.Sequential(
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.3)
        )
        
        # Expert networks with different curvatures
        self.experts = nn.ModuleList([
            CurvatureExpert(hidden_dim, hidden_dim, hidden_dim, c)
            for c in curvatures
        ])
        
        # Gating network
        self.gating = GatingNetwork(hidden_dim, num_experts)
        
        # Output head
        self.output = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.ReLU(),
            nn.Linear(hidden_dim // 2, output_dim)
        )
        
    def forward(self, eeg_features, aux_features):
        """
        Forward pass
        
        Args:
            eeg_features: (batch, seq, eeg_dim)
            aux_features: (batch, aux_dim) auxiliary modality
            
        Returns:
            predictions: (batch, output_dim)
        """
        # Project modalities
        eeg_h = self.eeg_proj(eeg_features)  # (batch, seq, hidden)
        aux_h = self.aux_proj(aux_features)  # (batch, hidden)
        
        # Expand aux to match seq length
        aux_h = aux_h.unsqueeze(1).expand(-1, eeg_h.size(1), -1)
        
        # Concatenate and fuse
        fused = torch.cat([eeg_h, aux_h], dim=-1)
        fused = self.fusion(fused)  # (batch, seq, hidden)
        
        # Get expert weights from gating network
        expert_weights = self.gating(fused)  # (batch, num_experts)
        
        # Compute expert outputs
        expert_outputs = []
        for expert in self.experts:
            # Average pooling over sequence
            pooled = torch.mean(fused, dim=1)
            out = expert(pooled)
            expert_outputs.append(out)
        
        expert_outputs = torch.stack(expert_outputs, dim=1)  # (batch, num_experts, hidden)
        
        # Weighted combination
        expert_weights = expert_weights.unsqueeze(-1)  # (batch, num_experts, 1)
        combined = torch.sum(expert_outputs * expert_weights, dim=1)  # (batch, hidden)
        
        # Output prediction
        prediction = self.output(combined)
        
        return prediction, expert_weights.squeeze(-1)
```

## Training

```python
def train_hypermocoe(model, train_loader, val_loader, epochs=100):
    """Training procedure with auxiliary loss for gating diversity"""
    
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    criterion = nn.CrossEntropyLoss()
    
    for epoch in range(epochs):
        model.train()
        total_loss = 0
        
        for batch in train_loader:
            eeg, aux, labels = batch
            
            # Forward
            predictions, expert_weights = model(eeg, aux)
            
            # Task loss
            task_loss = criterion(predictions, labels)
            
            # Diversity loss (encourage different experts to specialize)
            diversity_loss = -torch.std(expert_weights, dim=1).mean()
            
            # Balance loss (prevent one expert from dominating)
            usage = expert_weights.mean(dim=0)
            balance_loss = torch.std(usage)
            
            # Total loss
            loss = task_loss + 0.1 * diversity_loss + 0.1 * balance_loss
            
            # Backward
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            total_loss += loss.item()
        
        print(f"Epoch {epoch}: Loss = {total_loss / len(train_loader):.4f}")
```

## Key Advantages

1. **Hierarchical Representation**: Better captures tree-like EEG structure
2. **Adaptive Geometry**: Different experts for different data substructures
3. **Multimodal Fusion**: Integrates EEG with auxiliary modalities
4. **Interpretable**: Expert weights show which geometry fits the data
5. **Efficient**: Hyperbolic space reduces dimensionality for hierarchical data

## Applications

- **Emotion Recognition**: EEG + facial expressions
- **Mental State Assessment**: EEG + physiological signals
- **Sleep Stage Classification**: EEG + EOG + EMG
- **Clinical Diagnosis**: EEG + clinical data

## Activation Keywords

- hyperbolic EEG
- mixture-of-curvature experts
- hierarchical brain signals
- hyperbolic neural representation
- Poincaré ball model
- hyperbolic multimodal learning

## References

- Zhou, R., Li, S., Huang, G., et al. (2026). EEG-Based Multimodal Learning via Hyperbolic Mixture-of-Curvature Experts. arXiv:2604.12579v1

## Related Skills

- eeg-brain-connectivity-bci
- hyperdimensional-computing-neuroscience
- brain-connectivity-analysis