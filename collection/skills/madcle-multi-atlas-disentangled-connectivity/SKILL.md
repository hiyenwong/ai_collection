---
name: madcle-multi-atlas-disentangled-connectivity
description: >
  Multi-Atlas Disentangled Connectivity LEarning (MADCLE) methodology for
  brain disorder identification from functional connectivity (FC) matrices.
  Addresses atlas dependency heterogeneity by jointly encoding FC matrices
  from different brain atlases with cross-atlas distributional alignment,
  covariate similarity supervision, and decorrelation constraints.
  Use when working with multi-atlas fMRI FC analysis, cross-atlas
  consistency learning, brain disorder classification (ADNI, ADHD-200),
  disentangled representation learning for neuroimaging, or functional
  connectivity-based disease identification under heterogeneous parcellation.
  Triggers: multi-atlas, disentangled connectivity, cross-atlas, MADCLE,
  FC heterogeneity, atlas parcellation, functional connectivity disorder.
---

# MADCLE: Multi-Atlas Disentangled Connectivity Learning

Multi-branch representation learning framework that jointly encodes functional
connectivity (FC) matrices from different brain atlases, learning atlas-wise
disease-related representations that are cross-atlas consistent through
distributional alignment while separately modeling covariate-related and
atlas-dependent residual factors.

## Problem Statement

FC construction critically depends on brain atlas choice. Different parcellations
emphasize distinct organizational features, leading to heterogeneous and
sometimes inconsistent disorder representations. Single-atlas disentanglement
methods don't address cross-atlas heterogeneity; existing multi-atlas approaches
fuse features at shallow levels.

## Core Architecture

### Multi-Branch Encoding

Each atlas branch independently encodes its FC matrix:

```
FC_atlas_i → Encoder_i → Latent_i
```

### Disentangled Representation

Each latent splits into three factors:
- **Disease-related** (z_d): Shared pathology signal across atlases
- **Covariate-related** (z_c): Subject demographics (age, sex, site)
- **Atlas-specific residual** (z_r): Parcellation-dependent information

### Cross-Atlas Consistency

Disease-related representations are aligned via distributional matching:

```
MMD(z_d_atlas1, z_d_atlas2, ...) → minimize
```

## Key Mechanisms

### 1. Distributional Alignment

Maximum Mean Discrepancy (MMD) between disease-related latents across all atlas
branches ensures consistent pathology representation regardless of parcellation.

### 2. Covariate Similarity Supervision

Covariate-related latents are supervised to predict known subject covariates:

```
L_cov = BCE(z_c → covariate_labels)
```

### 3. Atlas-Specific Reconstruction

Each atlas branch reconstructs its own FC matrix from the atlas-specific
residual, ensuring parcellation-specific information is captured separately:

```
L_rec_i = MSE(Decoder_i(z_r_i), FC_i)
```

### 4. Decorrelation Constraints

Independence constraints prevent leakage between representation factors:

```
L_decor = ||Cov(z_d, z_c)||_F^2 + ||Cov(z_d, z_r)||_F^2 + ||Cov(z_c, z_r)||_F^2
```

## Total Loss

```
L = L_cls(disease_prediction)
  + λ_mmd * Σ MMD(z_di, z_dj)    # cross-atlas alignment
  + λ_cov * L_cov                 # covariate supervision
  + λ_rec * Σ L_rec_i            # atlas-specific reconstruction
  + λ_dec * L_decor               # factor decorrelation
```

## Implementation Pattern

```python
import torch
import torch.nn as nn

class MADCLE(nn.Module):
    def __init__(self, n_atlases, fc_dim, latent_dim, n_covariates, n_classes):
        super().__init__()
        self.n_atlases = n_atlases
        # Per-atlas encoders
        self.encoders = nn.ModuleList([
            nn.Sequential(
                nn.Linear(fc_dim, 256), nn.ReLU(),
                nn.Linear(256, latent_dim * 3)  # z_d + z_c + z_r
            ) for _ in range(n_atlases)
        ])
        # Disease classifier (shared)
        self.classifier = nn.Linear(latent_dim, n_classes)
        # Covariate predictor
        self.cov_predictor = nn.Linear(latent_dim, n_covariates)
        # Per-atlas decoders
        self.decoders = nn.ModuleList([
            nn.Linear(latent_dim, fc_dim) for _ in range(n_atlases)
        ])

    def forward(self, fc_matrices):
        """fc_matrices: list of FC tensors, one per atlas"""
        latents = []
        for i, fc in enumerate(fc_matrices):
            h = self.encoders[i](fc)
            z_d = h[:, :self.latent_dim]
            z_c = h[:, self.latent_dim:2*self.latent_dim]
            z_r = h[:, 2*self.latent_dim:]
            latents.append((z_d, z_c, z_r))

        # Disease prediction from averaged z_d
        z_d_avg = torch.stack([l[0] for l in latents]).mean(0)
        disease_pred = self.classifier(z_d_avg)

        # Covariate prediction from z_c
        cov_pred = self.cov_predictor(latents[0][1])

        # Atlas-specific reconstruction
        reconstructions = [
            self.decoders[i](latents[i][2]) for i in range(self.n_atlases)
        ]

        return disease_pred, cov_pred, latents, reconstructions
```

## MMD Computation

```python
def mmd_loss(z1, z2, kernel_type='rbf'):
    """Maximum Mean Discrepancy between two distributions."""
    if kernel_type == 'rbf':
        # Gaussian kernel
        diff = z1.unsqueeze(1) - z2.unsqueeze(0)
        sigma = z1.size(1)  # median heuristic
        K1 = torch.exp(-torch.sum(diff**2, dim=2) / (2 * sigma))
        # E[K(x,x')] + E[K(y,y')] - 2E[K(x,y)]
        mmd = K1.mean() + K1.mean() - 2 * K1.mean()
        # Simplified; use full kernel matrix in practice
    return mmd
```

## Workflow

1. **Preprocess FC matrices**: Compute FC for each atlas (e.g., AAL, Harvard-Oxford, Schaefer)
2. **Build multi-branch model**: One encoder-decoder pair per atlas
3. **Train with combined loss**: Classification + MMD + covariate + reconstruction + decorrelation
4. **Evaluate cross-atlas consistency**: Compare disease representations across atlases
5. **Deploy for disorder identification**: Use averaged z_d for classification

## Datasets Used

- **ADNI**: Alzheimer's Disease Neuroimaging Initiative
- **ADHD-200**: ADHD dataset for cross-site validation

## Advantages Over Baselines

| Method | Limitation | MADCLE Improvement |
|--------|-----------|-------------------|
| Single-atlas | Atlas-dependent results | Cross-atlas consistent |
| Feature fusion | Shlevel combination | Deep disentanglement |
| Multi-atlas GNN | Implicit alignment | Explicit distributional alignment |

## Activation Keywords

- multi-atlas functional connectivity
- cross-atlas consistency
- disentangled connectivity learning
- MADCLE
- atlas parcellation heterogeneity
- FC-based disorder identification
- brain atlas disentanglement