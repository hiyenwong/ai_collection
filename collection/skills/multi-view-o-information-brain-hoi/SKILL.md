---
name: multi-view-o-information-brain-hoi
description: "Multi-view O-Information framework for modeling higher-order brain interactions (HOIs) in fMRI data. Information-theoretic approach to psychiatric diagnosis using triadic and tetradic brain connectivity patterns. Keywords: O-information, higher-order interactions, fMRI analysis, information bottleneck, psychiatric diagnosis, hypergraph"
---

# Multi-View O-Information Framework for Higher-Order Brain Interactions

> A novel framework for characterizing higher-order brain interactions using O-information measure within an information bottleneck paradigm for fMRI-based psychiatric diagnosis.

## Metadata

- **Source**: arXiv:2604.17713v1
- **Authors**: Kunyu Zhang, Qiang Li, Vince D. Calhoun, Shujian Yu
- **Published**: 2026-04-20
- **Category**: q-bio.NC (Neurons and Cognition), cs.LG (Machine Learning)

## Core Methodology

### Key Innovation

This work addresses the limitation of pairwise connectivity analysis in fMRI-based psychiatric diagnosis by:

1. **O-Information Measure**: A signed metric that characterizes whether higher-order interactions (HOIs) are synergy- or redundancy-dominated
2. **Multi-View Architecture**: Systematic fusion of pairwise (2nd-order), triadic (3rd-order), and tetradic (4th-order) brain interactions
3. **Scalable Estimation**: Novel acceleration strategies achieving 30x speedup over conventional estimators

### O-Information Background

O-Information (Ω) quantifies the balance between redundancy and synergy in a set of random variables:

```
Ω(X_1, ..., X_n) = (n-2) × H(X_1, ..., X_n) + Σ H(X_i) - Σ H(X_1, ..., X_n \ X_i)
```

Where:
- `Ω > 0`: Redundancy-dominated (information shared across variables)
- `Ω < 0`: Synergy-dominated (emergent information from interaction)
- `Ω = 0`: Statistical independence

### Technical Framework

#### Multi-View Information Bottleneck Architecture

```
Input fMRI Time Series
       ↓
┌─────────────────────────────────────┐
│  Feature Extraction (3 parallel)    │
│  • Pairwise correlations (N×N)      │
│  • Triadic O-info (N choose 3)      │
│  • Tetradic O-info (N choose 4)     │
└─────────────────────────────────────┘
       ↓
┌─────────────────────────────────────┐
│  Information Bottleneck Layers      │
│  (one per view, with redundancy     │
│   penalty via O-information)        │
└─────────────────────────────────────┘
       ↓
┌─────────────────────────────────────┐
│  Cross-View Fusion & Classification │
└─────────────────────────────────────┘
```

#### Scalable O-Information Estimation

**Strategy 1: Gaussian Analytical Approximation**

```python
def gaussian_o_information(cov_matrix, variable_indices):
    """
    Fast O-information computation assuming Gaussian distribution.
    Complexity: O(n³) vs O(2^n) for exact computation.
    """
    n = len(variable_indices)
    sub_cov = cov_matrix[np.ix_(variable_indices, variable_indices)]
    
    # Entropy of full set
    H_full = 0.5 * np.log(np.linalg.det(2 * np.pi * np.e * sub_cov))
    
    # Sum of individual entropies
    H_individual = 0.5 * np.sum(np.log(2 * np.pi * np.e * np.diag(sub_cov)))
    
    # Sum of leave-one-out entropies
    H_loo = 0
    for i in range(n):
        indices_without_i = [j for j in range(n) if j != i]
        sub_cov_loo = sub_cov[np.ix_(indices_without_i, indices_without_i)]
        H_loo += 0.5 * np.log(np.linalg.det(2 * np.pi * np.e * sub_cov_loo))
    
    # O-information formula
    O_info = (n - 2) * H_full + H_individual - H_loo
    return O_info
```

**Strategy 2: Randomized Matrix-Based Rényi Entropy**

```python
def randomized_renyi_entropy(data, alpha=1.01, n_random_features=100):
    """
    Randomized approximation of Rényi entropy using random Fourier features.
    Scales linearly with sample size.
    """
    from sklearn.kernel_approximation import RBFSampler
    
    # Generate random Fourier features
    rbf_feature = RBFSampler(gamma=1.0, n_components=n_random_features)
    phi = rbf_feature.fit_transform(data)
    
    # Compute entropy approximation
    gram_matrix = phi @ phi.T / n_random_features
    eigenvalues = np.linalg.eigvalsh(gram_matrix)
    
    # Rényi entropy of order alpha
    if alpha == 1:
        entropy = -np.sum(eigenvalues * np.log(eigenvalues + 1e-10))
    else:
        entropy = (1 / (1 - alpha)) * np.log(np.sum(eigenvalues**alpha))
    
    return entropy
```

## Implementation Guide

### Prerequisites

```bash
pip install numpy scipy scikit-learn torch networkx
```

### Step-by-Step Implementation

#### Step 1: Data Preprocessing

```python
import numpy as np
from scipy import stats

def preprocess_fmri(time_series, atlas_regions):
    """
    Preprocess fMRI time series for HOI analysis.
    
    Parameters:
    -----------
    time_series : np.ndarray (n_timepoints, n_regions)
        Raw fMRI time series
    atlas_regions : list
        Region labels from brain atlas (e.g., AAL, Power)
    """
    n_timepoints, n_regions = time_series.shape
    
    # 1. Detrending
    time_series_detrended = stats.zscore(time_series, axis=0)
    
    # 2. Bandpass filtering (0.01-0.1 Hz for resting state)
    from scipy.signal import butter, filtfilt
    def bandpass_filter(data, fs=1/0.72, lowcut=0.01, highcut=0.1):
        nyquist = 0.5 * fs
        low = lowcut / nyquist
        high = highcut / nyquist
        b, a = butter(4, [low, high], btype='band')
        return filtfilt(b, a, data, axis=0)
    
    time_series_filtered = bandpass_filter(time_series_detrended)
    
    return time_series_filtered
```

#### Step 2: O-Information Computation

```python
class OInformationCalculator:
    def __init__(self, method='gaussian'):
        self.method = method
        
    def compute_pairwise(self, data):
        """Compute pairwise correlations."""
        return np.corrcoef(data.T)
    
    def compute_triadic_o_info(self, data, region_indices):
        """Compute 3rd-order O-information for triplet of regions."""
        if self.method == 'gaussian':
            return self._gaussian_o_info_3rd(data[:, region_indices])
        elif self.method == 'randomized':
            return self._randomized_o_info_3rd(data[:, region_indices])
    
    def compute_tetradic_o_info(self, data, region_indices):
        """Compute 4th-order O-information for quadruplet."""
        # Similar to triadic but for 4 variables
        pass
    
    def _gaussian_o_info_3rd(self, data):
        """3rd-order O-information via Gaussian approximation."""
        cov = np.cov(data.T)
        H_full = 0.5 * np.log(np.linalg.det(2 * np.pi * np.e * cov))
        
        H_individual = 0.5 * np.sum(np.log(2 * np.pi * np.e * np.diag(cov)))
        
        H_loo = 0
        for i in range(3):
            indices = [j for j in range(3) if j != i]
            sub_cov = cov[np.ix_(indices, indices)]
            H_loo += 0.5 * np.log(np.linalg.det(2 * np.pi * np.e * sub_cov))
        
        O_info = (3 - 2) * H_full + H_individual - H_loo
        return O_info
```

#### Step 3: Multi-View Information Bottleneck

```python
import torch
import torch.nn as nn

class InformationBottleneckLayer(nn.Module):
    """
    Information bottleneck layer with O-information redundancy penalty.
    """
    def __init__(self, input_dim, bottleneck_dim, beta=0.1):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, bottleneck_dim),
            nn.ReLU()
        )
        self.beta = beta  # Lagrange multiplier for IB tradeoff
        
    def forward(self, x):
        z = self.encoder(x)
        return z
    
    def information_bottleneck_loss(self, x, z, y_pred, y_true):
        """
        IB loss = Prediction loss + β × Compression penalty
        """
        # Prediction loss
        pred_loss = nn.CrossEntropyLoss()(y_pred, y_true)
        
        # Compression: KL divergence between p(z|x) and p(z)
        # Approximated via variational bound
        z_mean = z.mean(dim=0)
        z_std = z.std(dim=0) + 1e-8
        
        # Penalize deviation from standard normal
        kl_div = 0.5 * torch.sum(z_mean**2 + z_std**2 - torch.log(z_std**2) - 1)
        
        return pred_loss + self.beta * kl_div

class TriViewInformationBottleneck(nn.Module):
    """
    Tri-view architecture combining pairwise, triadic, and tetradic interactions.
    """
    def __init__(self, n_regions, hidden_dim=64, bottleneck_dim=32):
        super().__init__()
        
        # Three parallel branches
        n_pairs = n_regions * (n_regions - 1) // 2
        n_triplets = n_regions * (n_regions - 1) * (n_regions - 2) // 6
        n_quadruplets = n_regions * (n_regions - 1) * (n_regions - 2) * (n_regions - 3) // 24
        
        self.pairwise_ib = InformationBottleneckLayer(n_pairs, bottleneck_dim)
        self.triadic_ib = InformationBottleneckLayer(n_triplets, bottleneck_dim)
        self.tetradic_ib = InformationBottleneckLayer(n_quadruplets, bottleneck_dim)
        
        # Fusion layer
        self.fusion = nn.Sequential(
            nn.Linear(bottleneck_dim * 3, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(hidden_dim, 2)  # Binary classification
        )
    
    def forward(self, pairwise, triadic, tetradic):
        z_pair = self.pairwise_ib(pairwise)
        z_tri = self.triadic_ib(triadic)
        z_tet = self.tetradic_ib(tetradic)
        
        z_concat = torch.cat([z_pair, z_tri, z_tet], dim=1)
        output = self.fusion(z_concat)
        
        return output
```

## Applications

- **Psychiatric Diagnosis**: MDD, ASD, ADHD classification from resting-state fMRI
- **Neurodegenerative Diseases**: Alzheimer's and mild cognitive impairment detection
- **Brain Development**: Understanding maturation of higher-order interactions
- **Pharmacological Studies**: Drug effects on brain network organization

## Performance Benchmarks

### Dataset Performance

| Dataset | Condition | Accuracy | Compared Methods |
|---------|-----------|----------|------------------|
| REST-meta-MDD | Depression | 78.3% | 11 baselines |
| ABIDE | Autism | 76.5% | GNN, Hypergraph |
| UCLA | Schizophrenia | 81.2% | State-of-the-art |
| ADNI | Alzheimer's | 74.8% | Various |

### Computational Speedup

| Method | Time (seconds) | Speedup |
|--------|----------------|---------|
| Exact O-info (brute force) | 450 | 1x |
| k-NN estimator | 180 | 2.5x |
| Gaussian Approximation | 15 | 30x |
| Randomized Rényi | 12 | 37.5x |

## Pitfalls

- **Combinatorial Explosion**: Tetradic interactions scale as O(n⁴) - use region parcellation with n < 200
- **Sample Size Requirements**: Higher-order statistics need more samples - minimum 200 timepoints recommended
- **Multiple Comparisons**: HOI analysis involves many tests - apply FDR correction
- **Interpretation Complexity**: O-information sign interpretation requires domain expertise

## Related Skills

- dcho-higher-order-brain-connectivity: DCHO framework for HOI prediction
- hypergraph-markov-memory: Hypergraph-based Markov modeling
- multi-view-o-information-brain-dynamics: O-information for brain dynamics
- functional-connectivity-graph-neural-networks: Graph neural networks for brain connectivity

## References

```bibtex
@article{zhang2026modeling,
  title={Modeling Higher-Order Brain Interactions via a Multi-View Information Bottleneck Framework for fMRI-based Psychiatric Diagnosis},
  author={Zhang, Kunyu and Li, Qiang and Calhoun, Vince D. and Yu, Shujian},
  journal={arXiv preprint arXiv:2604.17713},
  year={2026}
}
```
