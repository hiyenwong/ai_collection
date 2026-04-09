# SKILL.md - Algebraic Topological Brain Network Comparison

## Activation Keywords

- algebraic topology, brain network comparison, multimodal networks
- persistent homology, network distance, graph comparison
- structural functional connectivity, DTI fMRI comparison
- topological data analysis, TDA brain networks

## What It Does

Provides an algebraic topological method for comparing multimodal brain networks (e.g., structural DTI vs functional fMRI). Uses persistent homology to preserve connected components and identify common underlying network structures across subjects and modalities.

## When To Use

**Use this skill when:**
- Comparing structural vs functional brain connectivity
- Analyzing multimodal neuroimaging data
- Identifying network differences across groups (patients vs healthy)
- Extracting aggregated networks from multiple subjects
- Preserving topological features in network comparison

**Do NOT use for:**
- Single modality analysis (no comparison needed)
- Simple correlation-based network comparison
- Non-graph neuroimaging data

## How To Use

### Step-by-Step Workflow

1. **Construct Networks from Each Modality**
   - DTI: Structural connectivity (white matter tracts)
   - fMRI: Functional connectivity (correlation)
   - Both as weighted graphs G₁, G₂, ..., Gₙ

2. **Build Filtration for Each Network**
   - Start with empty graph
   - Add edges by decreasing weight
   - Track topological changes (connected components)

3. **Compute Persistent Homology**
   - H₀: Connected components (most relevant for brain networks)
   - Birth/death times for each component
   - Generate persistence diagram

4. **Compare Networks via Persistence Diagrams**
   - Use bottleneck distance or Wasserstein distance
   - d(G₁, G₂) = W₂(PD₁, PD₂)
   - Lower distance = more similar topology

5. **Extract Aggregated Network**
   - Combine persistence diagrams from multiple subjects
   - Identify common topological features
   - Reconstruct representative network

### Key Equations

**Persistence diagram distance:**
```
d_W(PD₁, PD₂) = [Σᵢ min_j |pᵢ - qⱼ|^p]^(1/p)
```

**Aggregated network extraction:**
```
G_agg = f(PD₁ ∪ PD₂ ∪ ... ∪ PDₙ)
```

### Parameters

| Parameter | Purpose | Typical Value |
|-----------|---------|---------------|
| Weight threshold | Network sparsification | 0.1-0.3 |
| Max filtration | Homology range | Max weight |
| Distance metric | Network comparison | Wasserstein-2 |

## Example Usage

### Comparing DTI and fMRI Networks

**Problem:** Compare structural and functional connectivity in same subjects

**Pipeline:**
```python
import numpy as np
from gudhi import RipsComplex

def compare_multimodal_networks(dti_matrix, fmri_matrix, threshold=0.2):
    """
    Compare structural (DTI) and functional (fMRI) brain networks
    using persistent homology
    """
    # Threshold networks
    G_dti = (dti_matrix > threshold).astype(float)
    G_fmri = (np.abs(fmri_matrix) > threshold).astype(float)
    
    # Compute persistence diagrams
    pd_dti = compute_persistence(G_dti)
    pd_fmri = compute_persistence(G_fmri)
    
    # Compute distance
    distance = wasserstein_distance(pd_dti, pd_fmri)
    
    # Identify differing regions
    diff_regions = find_topological_differences(G_dti, G_fmri)
    
    return distance, diff_regions

def compute_persistence(adj_matrix):
    """
    Compute H₀ persistence diagram from adjacency matrix
    """
    # Convert to distance matrix
    dist_matrix = 1 - adj_matrix
    
    # Build Rips complex
    rips = RipsComplex(distance_matrix=dist_matrix, max_edge_length=1.0)
    simplex_tree = rips.create_simplex_tree(max_dimension=1)
    
    # Get persistence (H₀ = connected components)
    persistence = simplex_tree.persistence(homology_coeff_field=2)
    
    # Extract H₀ features
    pd_h0 = [(b, d) for dim, (b, d) in persistence if dim == 0]
    
    return pd_h0
```

### Aggregating Networks Across Subjects

**Input:** Functional networks from N subjects

**Analysis:**
```python
def aggregate_networks(subject_networks):
    """
    Extract common network structure from multiple subjects
    """
    # Compute persistence for each subject
    all_pds = [compute_persistence(net) for net in subject_networks]
    
    # Find common features (appear in most subjects)
    common_features = []
    for feature in all_pds[0]:
        count = sum(1 for pd in all_pds if is_similar(feature, pd))
        if count > 0.8 * len(all_pds):  # 80% threshold
            common_features.append(feature)
    
    # Reconstruct network from common features
    aggregated = reconstruct_network(common_features)
    
    return aggregated
```

**Output:** Representative network preserving common topology

## Key Advantages

| Advantage | Benefit |
|-----------|---------|
| Topology preservation | Keeps connected components |
| Multimodal comparison | Direct DTI-fMRI comparison |
| Subject aggregation | Common structure extraction |
| Statistical power | Group-level analysis |

## Applications

1. **Patient vs Healthy Comparison**
   - Identify topological differences in disease
   - Network biomarkers

2. **Multimodal Integration**
   - Compare structural-functional relationships
   - Identify modality-specific regions

3. **Group Analysis**
   - Aggregate networks across subjects
   - Statistical significance testing

## Description
Framework from arXiv papers. See paper reference for details.
## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents

1. **Understand the Request**: Analyze what the user needs related to this skill's domain.
2. **Search for Information**: Use web_search to find relevant papers or documentation.
3. **Apply the Framework**: Follow the methodology described in the skill's key concepts.
4. **Provide Results**: Summarize findings and actionable recommendations.
5. **Verify Accuracy**: Cross-check key facts before presenting to user.

## Examples

### Example 1: Basic Usage

**User:** How can I apply algebraic-topological-brain-networks?

**Agent:** I'll help you understand and apply algebraic-topological-brain-networks...

### Example 2: Advanced Application

**User:** What are the key considerations for algebraic-topological-brain-networks?

**Agent:** Let me search for the latest research and best practices...

## Related Skills

- **brain-higher-order-structures** - Higher-order connectivity
- **discrete-heat-kernels-simplicial** - Simplicial methods
- **dynamic-brain-connectivity-topology** - Dynamic topology analysis

## Source

- arXiv:1504.02265v2
- Title: An Algebraic Topological Method for Multimodal Brain Networks Comparisons
- Utility: 0.87
- Authors: Tiago Simas et al.
- Published: Frontiers in Psychology 2015

## Notes

- Key innovation: Algebraic topology for network comparison
- Preserves connected components across modalities
- Enables DTI-fMRI direct comparison
- Published in Frontiers in Psychology
- Applications: multimodal neuroimaging, clinical neuroscience
- Can identify resting state network differences

---

_Created: 2026-04-01_