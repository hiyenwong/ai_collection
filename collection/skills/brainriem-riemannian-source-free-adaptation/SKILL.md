---
name: brainriem-riemannian-source-free-adaptation
description: >
  Source-free domain adaptation for multi-site fMRI brain network diagnosis using Riemannian geometry on SPD manifolds.
  BrainRiem learns compact prototypes via bi-level optimization with Log-Euclidean Metric and Dirichlet Energy calibration,
  enabling privacy-preserving cross-site transfer without source data access.
tags: [brain-network, domain-adaptation, riemannian-geometry, spd-manifold, fMRI, privacy-preserving]
paper: arXiv:2606.29200
venue: ECCV 2026
---

# BrainRiem: Riemannian Source-Free Domain Adaptation for Brain Networks

## Core Innovation

**Problem**: Multi-site fMRI studies suffer from domain shifts (scanner heterogeneity, demographics, acquisition protocols). Traditional domain adaptation requires concurrent source/target data access, violating clinical privacy regulations.

**Solution**: BrainRiem learns compact Riemannian brain prototypes that:
- Remain valid SPD (Symmetric Positive Definite) matrices on the manifold
- Can be transmitted to target sites without source data
- Serve as stable anchors for local model training

## Key Technical Components

### 1. Log-Euclidean Metric
- Operates on SPD manifold where Euclidean operations cause geometric distortions
- Formula: d_LE(A,B) = ||log(A) - log(B)||_F
- Ensures prototypes remain valid SPD matrices throughout optimization

### 2. Dirichlet Energy Spectral Calibration
- Aligns prototype frequency characteristics with real brain networks
- Minimizes: E_D = ∫||∇u||² dx (measures smoothness of graph signals)
- Prevents prototypes from learning unrealistic frequency patterns

### 3. Bi-Level Optimization
```
Upper level: min_θ Σ_i L_target(f_θ(P_i))  # Adapt prototypes to target
Lower level: min_φ Σ_j L_source(g_φ(x_j))   # Learn source prototypes
```
- Prototypes P_i are adapted to target domain
- Source models g_φ generate initial prototypes from source data
- Only prototypes are transmitted (not source data)

## Implementation Pattern

```python
import torch
import torch.nn as nn
from torch.autograd import grad

class RiemannianPrototype(nn.Module):
    def __init__(self, n_prototypes, n_regions):
        super().__init__()
        # Initialize as identity matrices (valid SPD)
        self.prototypes = nn.Parameter(
            torch.stack([torch.eye(n_regions) for _ in range(n_prototypes)])
        )
    
    def log_euclidean_distance(self, A, B):
        """Compute Log-Euclidean distance between SPD matrices"""
        log_A = torch.matrix_exp(A).log()  # Matrix logarithm
        log_B = torch.matrix_exp(B).log()
        return torch.norm(log_A - log_B, p='fro')
    
    def dirichlet_energy(self, L, x):
        """Compute Dirichlet energy on graph Laplacian L"""
        return torch.einsum('ij,ij->', x.T @ L @ x, torch.eye(x.shape[1]))
    
    def forward(self, x):
        # x: input connectivity matrix (SPD)
        distances = torch.stack([
            self.log_euclidean_distance(x, p) for p in self.prototypes
        ])
        return torch.softmax(-distances, dim=0)  # Soft assignment

class BrainRiem:
    def __init__(self, source_model, n_prototypes, n_regions):
        self.source_model = source_model
        self.prototypes = RiemannianPrototype(n_prototypes, n_regions)
        self.target_model = self._build_target_model()
    
    def _build_target_model(self):
        """Build target model that uses prototypes as anchors"""
        return nn.Sequential(
            nn.Flatten(),
            nn.Linear(self.prototypes.n_prototypes * self.prototypes.n_regions**2, 128),
            nn.ReLU(),
            nn.Linear(128, 2)  # Binary classification (e.g., ASD vs control)
        )
    
    def bilevel_optimization_step(self, source_batch, target_batch, graph_laplacian):
        """One step of bi-level optimization"""
        # Lower level: update source model
        source_loss = self.source_model.loss(source_batch)
        grad(source_loss, self.source_model.parameters())
        
        # Generate prototypes from source model
        with torch.no_grad():
            prototypes = self.source_model.generate_prototypes()
        
        # Upper level: adapt prototypes to target
        target_loss = self.target_model.loss(target_batch, prototypes)
        
        # Dirichlet energy regularization
        dirichlet_reg = sum(
            self.prototypes.dirichlet_energy(graph_laplacian, p)
            for p in prototypes
        )
        
        total_loss = target_loss + 0.1 * dirichlet_reg
        grad(total_loss, self.prototypes.parameters())
```

## When to Use

- **Multi-site fMRI studies** with privacy constraints
- **Cross-scanner diagnosis** (different manufacturers, field strengths)
- **Demographic shifts** (age, gender, ethnicity differences across sites)
- **Clinical deployment** where source data cannot be shared

## Pitfalls

1. **SPD violation**: Euclidean operations on connectivity matrices can produce non-SPD results
   - **Fix**: Always use Log-Euclidean or affine-invariant Riemannian metrics
   
2. **Prototype collapse**: Prototypes may converge to identical solutions
   - **Fix**: Add diversity regularization: Σ_{i≠j} exp(-d(P_i, P_j))
   
3. **Dirichlet energy mismatch**: Real brain networks have specific frequency profiles
   - **Fix**: Calibrate using empirical power spectral density from target site data
   
4. **Privacy leakage**: Prototypes may inadvertently encode source subject information
   - **Fix**: Add differential privacy noise during prototype transmission

## Validation

Tested on:
- **ABIDE** (Autism Brain Imaging Data Exchange): 17 sites, 1000+ subjects
- **REST-meta-MDD** (Major Depressive Disorder): 21 sites, 2000+ subjects

Results: BrainRiem consistently outperforms:
- Traditional DA methods (requires source data access)
- Source-free DA baselines (Euclidean space)
- Graph DA methods (ignores manifold structure)

## Neuroscience Interpretability

Learned prototypes exhibit biologically meaningful connectivity patterns:
- **Default Mode Network** prototypes: Strong posterior cingulate ↔ medial prefrontal connectivity
- **Salience Network** prototypes: Anterior insula ↔ dorsal anterior cingulate connectivity
- Align with established findings in ASD and MDD literature

## References

- Paper: https://arxiv.org/abs/2606.29200
- Venue: ECCV 2026 (Accepted)
- Authors: Kunyu Zhang, Tianxiang Xu

## Activation Triggers

Use this skill when encountering:
- Cross-site fMRI analysis
- Source-free domain adaptation
- SPD manifold learning
- Privacy-preserving brain network analysis
- Riemannian geometry in neuroimaging