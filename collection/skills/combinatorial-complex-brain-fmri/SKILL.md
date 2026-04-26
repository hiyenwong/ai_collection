---
name: combinatorial-complex-brain-fmri
description: "Framework for constructing combinatorial complexes (CCs) from fMRI time series that captures both pairwise and higher-order neural interactions via O-information and S-information measures. Bridges topological deep learning and network neuroscience. Activation: combinatorial complex, higher-order brain network, topological deep learning, O-information, S-information, synergistic dependencies, fMRI, higher-order interaction."
---

# The Human Brain as a Combinatorial Complex

> Construct combinatorial complexes from fMRI data that preserve higher-order neural interactions invisible to traditional graph methods, enabling topological deep learning on brain networks.

## Metadata
- **Source**: arXiv:2511.20692
- **Authors**: Valentina Sánchez, Çiçek Güven, Koen Haak, Theodore Papamarkou, Gonzalo Nápoles, Marie Šafář Postma
- **Published**: 2025-11-22

## Core Methodology

### Key Innovation
Directly constructs **combinatorial complexes (CCs)** from fMRI statistical dependencies using information-theoretic measures (O-information, S-information), preserving both pairwise connections AND higher-order cells (triplets, quadruplets) based on synergistic dependencies. Unlike topological lifting approaches, this method directly builds CCs from data rather than mapping existing graphs.

### Problem Addressed
- Traditional graph representations of brain networks miss higher-order dependencies
- Neural information processing involves synergistic interactions beyond pairwise relationships
- Existing topological lifting approaches map structures into higher-order domains rather than discovering them from data
- Brain networks are inherently multi-scale and hierarchical — graphs cannot capture this

### Technical Framework
1. **Compute pairwise dependencies**: Mutual information between all region pairs from fMRI time series
2. **Compute higher-order dependencies**: O-information and S-information for triplets, quadruplets, etc.
   - O-information: Distinguishes redundancy-dominated from synergy-dominated interactions
   - S-information: Measures total statistical dependence including higher-order
3. **Construct CC**: Build rank-1 (edges) from pairwise MI, rank-2+ (higher-order cells) from significant O/S-information
4. **Apply TDL**: Use topological deep learning architectures (CC-based neural networks) on the constructed complex

## Implementation Guide

### Prerequisites
- fMRI time series data (preprocessed, region-extracted)
- Python: `numpy`, `scipy`, `itertools`, `jidata` (or custom MI/O-information code)
- Topological deep learning library (e.g., TopoNetX)

### Step-by-Step
1. **Extract regional time series**: Parcellate fMRI into N brain regions
2. **Estimate pairwise MI**: Compute mutual information for all (N choose 2) pairs
3. **Estimate higher-order measures**: Compute O-information for triplets/quadruplets
4. **Threshold and construct CC**: Include edges with significant MI; include higher-order cells with significant synergy
5. **Apply CC neural network**: Train topological deep learning model on the CC

### Code Example
```python
import numpy as np
from itertools import combinations
from scipy.stats import entropy

def estimate_mi(X, Y, bins=20):
    """Estimate mutual information between two variables."""
    hist_2d, _, _ = np.histogram2d(X, Y, bins=bins)
    pxy = hist_2d / hist_2d.sum()
    px = pxy.sum(axis=1)
    py = pxy.sum(axis=0)
    hx = entropy(px)
    hy = entropy(py)
    hxy = entropy(pxy.flatten())
    return hx + hy - hxy

def compute_o_information(data, regions):
    """Compute O-information for a set of regions.
    
    O > 0: redundancy-dominated
    O < 0: synergy-dominated
    """
    n = len(regions)
    sub_data = data[:, list(regions)]
    
    # Total entropy
    h_total = entropy(
        np.histogramdd(sub_data, bins=10)[0].flatten() + 1e-10
    )
    
    # Sum of individual entropies
    h_individual = sum(
        entropy(np.histogram(sub_data[:, i], bins=10)[0] + 1e-10)
        for i in range(n)
    )
    
    # Sum of pairwise conditional entropies (approximation)
    # Full O-information requires all subset decompositions
    # Simplified: O ≈ sum(H(Xi)) - H(X1,...,Xn)
    o_info = h_individual - h_total
    return o_info

def build_combinatorial_complex(fmri_data, mi_threshold=0.01, o_threshold=-0.1):
    """Build combinatorial complex from fMRI data.
    
    Args:
        fmri_data: (T, N) time series for N brain regions
        mi_threshold: Minimum MI for pairwise edges
        o_threshold: O-information threshold for higher-order cells (negative = synergy)
    Returns:
        CC specification: dict with 'edges' and 'higher_order_cells'
    """
    T, N = fmri_data.shape
    
    # Step 1: Pairwise edges
    edges = []
    for i, j in combinations(range(N), 2):
        mi = estimate_mi(fmri_data[:, i], fmri_data[:, j])
        if mi > mi_threshold:
            edges.append((i, j))
    
    # Step 2: Higher-order cells (triplets)
    cells = []
    for trio in combinations(range(N), 3):
        o = compute_o_information(fmri_data, trio)
        if o < o_threshold:  # Synergy-dominated
            cells.append(trio)
    
    return {'edges': edges, 'higher_order_cells': cells}
```

## Applications
- **Higher-order brain connectivity**: Capturing synergistic interactions among 3+ brain regions
- **Topological deep learning on brain data**: Enabling TDL architectures for brain network analysis
- **Network neuroscience**: More faithful representations of neural complexity
- **Multi-scale brain analysis**: Naturally accommodating hierarchical neural processing

## Pitfalls
- O-information computation scales combinatorially — limit to small cell ranks (3-4)
- Requires sufficient time series length for reliable MI estimation
- Threshold selection for significance of higher-order cells is non-trivial
- Validated on NetSim simulations — real fMRI validation still developing

## Related Skills
- higher-order-brain-networks
- multimodal-higher-order-brain-networks
- topological-signal-processing-brain-networks
- multi-view-o-information-brain-networks
