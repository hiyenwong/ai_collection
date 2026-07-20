---
name: multi-view-o-information-brain-dynamics
description: "Multi-view O-Information framework for analyzing higher-order brain interactions in fMRI data. Combines O-information measures with information bottleneck principles for psychiatric diagnosis. Includes O-information computation, Gaussian approximation, and Rényi entropy estimators. Activation: O-information brain, higher-order brain interactions, multi-view brain connectivity, O-information dynamics, brain synergy redundancy, psychiatric diagnosis fMRI."
---

# Multi-View O-Information Framework for Brain Dynamics

## Overview

This skill implements the **Multi-View O-Information Framework** for analyzing higher-order interactions (HOIs) in brain networks from fMRI data. Traditional brain connectivity analysis relies on pairwise connections, but higher-order interactions (triadic, tetradic) are central to complex brain dynamics. This framework uses **O-information** (a signed measure) to characterize whether interactions are **synergy-dominated** or **redundancy-dominated**.

## Key Concepts

### O-Information (Synergy vs. Redundancy)

O-information quantifies the nature of higher-order interactions:
- **Positive O-information**: Redundancy-dominated (shared information)
- **Negative O-information**: Synergy-dominated (emergent information)
- **Near zero**: Independent contributions

### Multi-View Architecture

Integrates three views of brain connectivity:
1. **Pairwise View**: Traditional pairwise functional connectivity
2. **Triadic View**: Third-order (three-region) interactions
3. **Tetradic View**: Fourth-order (four-region) interactions

## Mathematical Framework

### O-Information Definition

For a set of N variables, O-information is defined as:

```
Ω(X₁, ..., Xₙ) = (n-2) · H({Xᵢ}) - Σᵢ H(Xᵢ | X_{\i})
```

Where:
- `H({Xᵢ})`: Joint entropy of all variables
- `H(Xᵢ | X_{\i})`: Conditional entropy of variable i given all others

**Interpretation:**
- Ω > 0: Redundancy dominates
- Ω < 0: Synergy dominates  
- Ω ≈ 0: Mixed or independent

### Information Bottleneck Framework

The multi-view architecture uses information bottleneck principles:

```
L = Σᵢ αᵢ · I(Z; Y|Vᵢ) - β · Σᵢⱼ I(Vᵢ; Vⱼ)
```

Where:
- `Vᵢ`: View i (pairwise, triadic, tetradic)
- `Z`: Latent representation
- `Y`: Diagnosis label
- `I(Vᵢ; Vⱼ)`: Mutual information between views (redundancy penalty)

## Implementation

### O-Information Computation

```python
import numpy as np
from scipy import stats
from scipy.spatial.distance import cdist
import torch
import torch.nn as nn

class OInformationCalculator:
    """
    O-Information calculator for higher-order brain interactions
    
    Implements both exact computation (Gaussian) and 
    approximate methods (Rényi entropy estimator)
    """
    def __init__(self, method='gaussian', n_bootstrap=100):
        """
        Args:
            method: 'gaussian' for analytical, 'renyi' for estimator
            n_bootstrap: Number of bootstrap samples for Rényi method
        """
        self.method = method
        self.n_bootstrap = n_bootstrap
        
    def compute_joint_entropy_gaussian(self, X: np.ndarray) -> float:
        """
        Compute joint entropy assuming Gaussian distribution
        
        H(X) = 0.5 * log((2πe)^d · |Σ|)
        
        Args:
            X: Data matrix (samples × dimensions)
            
        Returns:
            Joint entropy in nats
        """
        n_samples, n_vars = X.shape
        
        # Compute covariance matrix
        cov = np.cov(X.T)
        
        # Add small regularization for stability
        cov += np.eye(n_vars) * 1e-6
        
        # Compute determinant
        sign, logdet = np.linalg.slogdet(cov)
        if sign <= 0:
            # Add more regularization if needed
            cov += np.eye(n_vars) * 1e-4
            sign, logdet = np.linalg.slogdet(cov)
        
        # Entropy of Gaussian: 0.5 * log((2πe)^d * |Σ|)
        d = n_vars
        entropy = 0.5 * (d * np.log(2 * np.pi * np.e) + logdet)
        
        return entropy
        
    def compute_conditional_entropy_gaussian(self, X: np.ndarray, 
                                           target_idx: int) -> float:
        """
        Compute conditional entropy H(X_target | X_others)
        assuming Gaussian distribution
        
        Uses: H(X|Y) = H(X,Y) - H(Y)
        
        Args:
            X: Data matrix (samples × dimensions)
            target_idx: Index of target variable
            
        Returns:
            Conditional entropy in nats
        """
        n_vars = X.shape[1]
        
        # Joint entropy H(X_target, X_others) = H(all)
        joint_H = self.compute_joint_entropy_gaussian(X)
        
        # Marginal entropy of others H(X_others)
        others_idx = [i for i in range(n_vars) if i != target_idx]
        X_others = X[:, others_idx]
        marginal_H = self.compute_joint_entropy_gaussian(X_others)
        
        # Conditional: H(X|Y) = H(X,Y) - H(Y)
        conditional_H = joint_H - marginal_H
        
        return conditional_H
        
    def compute_o_information_gaussian(self, X: np.ndarray) -> float:
        """
        Compute O-information using Gaussian approximation
        
        Ω(X₁,...,Xₙ) = (n-2)H({Xᵢ}) - Σᵢ H(Xᵢ|X_{\i})
        
        Args:
            X: Data matrix (samples × n variables)
            
        Returns:
            O-information value
        """
        n_samples, n_vars = X.shape
        
        # Joint entropy H({Xᵢ})
        joint_entropy = self.compute_joint_entropy_gaussian(X)
        
        # Sum of conditional entropies Σᵢ H(Xᵢ|X_{\i})
        conditional_sum = 0
        for i in range(n_vars):
            cond_H = self.compute_conditional_entropy_gaussian(X, i)
            conditional_sum += cond_H
        
        # O-information
        o_info = (n_vars - 2) * joint_entropy - conditional_sum
        
        return o_info
        
    def compute_renyi_entropy_matrix_estimator(self, X: np.ndarray, 
                                                alpha: float = 1.5) -> float:
        """
        Compute Rényi entropy using matrix-based randomized estimator
        
        Provides ~30x speedup over conventional estimation
        
        Args:
            X: Data matrix (samples × dimensions)
            alpha: Rényi entropy order (default: 1.5)
            
        Returns:
            Rényi entropy estimate
        """
        n_samples = X.shape[0]
        
        # Compute distance matrix
        dists = cdist(X, X, metric='euclidean')
        
        # Apply kernel (Gaussian)
        sigma = np.median(dists) / np.sqrt(2)  # Median heuristic
        K = np.exp(-dists**2 / (2 * sigma**2))
        
        # Normalize to get density estimate
        K = K / K.sum(axis=1, keepdims=True)
        
        # Matrix-based Rényi entropy
        # H_α = (1/(1-α)) log(tr(K^α))
        K_power = np.linalg.matrix_power(K, int(alpha))
        trace = np.trace(K_power)
        
        entropy = (1 / (1 - alpha)) * np.log(trace + 1e-10)
        
        return entropy

class BrainOInformationAnalyzer:
    """
    Analyzer for higher-order brain interactions using O-information
    """
    def __init__(self, n_regions: int, order: int = 3):
        """
        Args:
            n_regions: Number of brain regions (nodes)
            order: Interaction order (3=triadic, 4=tetradic)
        """
        self.n_regions = n_regions
        self.order = order
        self.calculator = OInformationCalculator(method='gaussian')
        
        # Pre-compute region combinations
        from itertools import combinations
        self.region_combinations = list(combinations(range(n_regions), order))
        
    def extract_roi_timeseries(self, fmri_data: np.ndarray, 
                               atlas_labels: np.ndarray) -> np.ndarray:
        """
        Extract region-wise time series from fMRI data
        
        Args:
            fmri_data: 4D fMRI data (x, y, z, time)
            atlas_labels: Atlas parcellation (x, y, z)
            
        Returns:
            Time series matrix (time × n_regions)
        """
        n_timepoints = fmri_data.shape[-1]
        time_series = np.zeros((n_timepoints, self.n_regions))
        
        for region_idx in range(self.n_regions):
            mask = (atlas_labels == region_idx)
            if mask.sum() > 0:
                time_series[:, region_idx] = fmri_data[mask].mean(axis=0)
        
        # Standardize
        time_series = (time_series - time_series.mean(axis=0)) / \
                      (time_series.std(axis=0) + 1e-8)
        
        return time_series
        
    def compute_hoi_matrix(self, time_series: np.ndarray) -> np.ndarray:
        """
        Compute higher-order interaction O-information for all combinations
        
        Args:
            time_series: Region time series (time × n_regions)
            
        Returns:
            HOI matrix of shape (n_combinations,)
        """
        oi_values = []
        
        for regions in self.region_combinations:
            # Extract data for these regions
            X = time_series[:, list(regions)]
            
            # Compute O-information
            oi = self.calculator.compute_o_information_gaussian(X)
            oi_values.append(oi)
        
        return np.array(oi_values)
```

### Multi-View Information Bottleneck Network

```python
class MultiViewOInformationNet(nn.Module):
    """
    Tri-view neural network for multi-modal brain connectivity analysis
    Fuses pairwise, triadic, and tetradic O-information
    """
    def __init__(
        self,
        n_regions: int,
        hidden_dim: int = 256,
        n_classes: int = 2,
        dropout: float = 0.5
    ):
        super().__init__()
        
        self.n_regions = n_regions
        self.hidden_dim = hidden_dim
        
        # Pairwise view encoder
        n_pairwise = n_regions * (n_regions - 1) // 2
        self.pairwise_encoder = nn.Sequential(
            nn.Linear(n_pairwise, hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.ReLU()
        )
        
        # Triadic view encoder (3rd order O-information)
        n_triadic = len(list(itertools.combinations(range(n_regions), 3)))
        self.triadic_encoder = nn.Sequential(
            nn.Linear(n_triadic, hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.ReLU()
        )
        
        # Tetradic view encoder (4th order O-information)
        n_tetradic = len(list(itertools.combinations(range(n_regions), 4)))
        self.tetradic_encoder = nn.Sequential(
            nn.Linear(n_tetradic, hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.ReLU()
        )
        
        # View fusion
        view_dim = hidden_dim // 2
        self.fusion = nn.Sequential(
            nn.Linear(view_dim * 3, hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.ReLU()
        )
        
        # Classification head
        self.classifier = nn.Linear(hidden_dim // 2, n_classes)
        
    def forward(
        self,
        pairwise_features: torch.Tensor,
        triadic_features: torch.Tensor,
        tetradic_features: torch.Tensor
    ) -> torch.Tensor:
        """
        Forward pass through multi-view network
        
        Args:
            pairwise_features: Pairwise connectivity (batch, n_pairwise)
            triadic_features: Triadic O-information (batch, n_triadic)
            tetradic_features: Tetradic O-information (batch, n_tetradic)
            
        Returns:
            Class logits (batch, n_classes)
        """
        # Encode each view
        z_pairwise = self.pairwise_encoder(pairwise_features)
        z_triadic = self.triadic_encoder(triadic_features)
        z_tetradic = self.tetradic_encoder(tetradic_features)
        
        # Concatenate views
        z_fused = torch.cat([z_pairwise, z_triadic, z_tetradic], dim=1)
        
        # Fusion
        z = self.fusion(z_fused)
        
        # Classification
        logits = self.classifier(z)
        
        return logits

class InformationBottleneckLoss(nn.Module):
    """
    Information Bottleneck loss with redundancy penalty
    """
    def __init__(self, beta: float = 0.1):
        super().__init__()
        self.beta = beta
        
    def forward(
        self,
        z: torch.Tensor,
        views: list,
        labels: torch.Tensor
    ) -> torch.Tensor:
        """
        Compute IB loss
        
        L = Σᵢ I(Z;Y|Vᵢ) - β · Σᵢⱼ I(Vᵢ;Vⱼ)
        
        Args:
            z: Fused representation
            views: List of view representations
            labels: Ground truth labels
            
        Returns:
            Total loss
        """
        # Classification loss (approximates I(Z;Y))
        ce_loss = F.cross_entropy(z, labels)
        
        # Redundancy penalty (approximate mutual information between views)
        redundancy = 0
        for i in range(len(views)):
            for j in range(i+1, len(views)):
                # Simple approximation: correlation penalty
                redundancy += torch.mean((views[i] - views[j])**2)
        
        total_loss = ce_loss + self.beta * redundancy
        
        return total_loss
```

## Usage Pipeline

### Complete Analysis Workflow

```python
def analyze_brain_hois(
    fmri_files: List[str],
    atlas_file: str,
    labels: np.ndarray,
    n_regions: int = 116  # AAL atlas
) -> dict:
    """
    Complete pipeline for higher-order brain interaction analysis
    
    Args:
        fmri_files: List of fMRI data files
        atlas_file: Atlas parcellation file
        labels: Diagnostic labels
        n_regions: Number of brain regions
        
    Returns:
        Results dictionary with HOI features and model
    """
    from nilearn import image, datasets
    
    # Load atlas
    atlas_img = image.load_img(atlas_file)
    atlas_data = atlas_img.get_fdata()
    
    # Initialize analyzers
    pairwise_analyzer = PairwiseConnectivity(n_regions)
    triadic_analyzer = BrainOInformationAnalyzer(n_regions, order=3)
    tetradic_analyzer = BrainOInformationAnalyzer(n_regions, order=4)
    
    features = {
        'pairwise': [],
        'triadic': [],
        'tetradic': []
    }
    
    # Process each subject
    for fmri_file in fmri_files:
        # Load fMRI data
        fmri_img = image.load_img(fmri_file)
        fmri_data = fmri_img.get_fdata()
        
        # Extract time series
        time_series = triadic_analyzer.extract_roi_timeseries(
            fmri_data, atlas_data
        )
        
        # Compute features
        pairwise_conn = pairwise_analyzer.compute(time_series)
        triadic_oi = triadic_analyzer.compute_hoi_matrix(time_series)
        tetradic_oi = tetradic_analyzer.compute_hoi_matrix(time_series)
        
        features['pairwise'].append(pairwise_conn)
        features['triadic'].append(triadic_oi)
        features['tetradic'].append(tetradic_oi)
    
    # Convert to arrays
    for key in features:
        features[key] = np.array(features[key])
    
    # Train multi-view model
    model = MultiViewOInformationNet(n_regions)
    
    # Train (simplified - full training loop omitted)
    # ...
    
    return {
        'features': features,
        'model': model,
        'interpretation': interpret_hois(features)
    }

def interpret_hois(features: dict) -> dict:
    """
    Interpret HOI patterns (synergy vs redundancy)
    """
    interpretation = {}
    
    # Triadic interactions
    triadic_mean = features['triadic'].mean(axis=0)
    synergy_regions = np.where(triadic_mean < -0.1)[0]  # Negative = synergy
    redundancy_regions = np.where(triadic_mean > 0.1)[0]  # Positive = redundancy
    
    interpretation['triadic_synergy'] = synergy_regions
    interpretation['triadic_redundancy'] = redundancy_regions
    
    # Similar for tetradic
    tetradic_mean = features['tetradic'].mean(axis=0)
    interpretation['tetradic_synergy'] = np.where(tetradic_mean < -0.1)[0]
    interpretation['tetradic_redundancy'] = np.where(tetradic_mean > 0.1)[0]
    
    return interpretation
```

## Performance Metrics

From paper evaluation on benchmark datasets:

| Dataset | Baseline SOTA | Multi-View O-Info | Improvement |
|---------|--------------|-------------------|-------------|
| REST-meta-MDD | 0.72 AUC | 0.78 AUC | +8.3% |
| ABIDE | 0.75 AUC | 0.81 AUC | +8.0% |
| UCLA | 0.70 AUC | 0.76 AUC | +8.6% |
| ADNI | 0.73 AUC | 0.79 AUC | +8.2% |

**Computational Speedup:**
- Gaussian approximation: ~30x faster than conventional estimators
- Rényi matrix estimator: Additional 2x speedup

## Applications

- **Psychiatric Diagnosis**: MDD, ASD, ADHD classification
- **Neurodegenerative Disease**: Alzheimer's, Parkinson's
- **Brain Network Analysis**: Understanding complex interactions
- **Biomarker Discovery**: Synergy/redundancy patterns as features

## References

- Paper: "Modeling Higher-Order Brain Interactions via a Multi-View Information Bottleneck Framework for fMRI-based Psychiatric Diagnosis" (arXiv:2604.17713)
- Authors: Zhang et al., 2026
- Categories: cs.LG

## Related Skills

- `brain-higher-order-structures`: Topological data analysis for brain networks
- `brain-graph-neural`: Graph neural networks for brain connectivity
- `functional-connectome-fingerprint`: Individual brain fingerprinting

_Last updated: 2026-04-27_
