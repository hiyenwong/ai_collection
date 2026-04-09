# SKILL.md - Modularity Maximization Brain Network Analysis

## Activation Keywords

- modularity maximization, brain network modularity, community detection
- network exploratory analysis, modular structure, brain network communities
- Louvain algorithm, network partition, functional modules

## What It Does

Provides a flexible and generic framework for detecting modular structure in brain networks using modularity maximization. Can be adapted to address a wide range of neuroscientific research questions through reparameterization and modification.

## When To Use

**Use this skill when:**
- Detecting community structure in brain networks
- Exploratory analysis of functional/structural connectivity
- Comparing modular structure across groups
- Testing hypotheses about brain organization
- Adapting modularity for domain-specific questions

**Do NOT use for:**
- Pre-defined network parcellation (no community detection needed)
- Single-node analysis (no network structure)
- Non-graph data (modularity requires networks)

## How To Use

### Step-by-Step Workflow

1. **Construct Brain Network**
   - Functional connectivity (fMRI correlation)
   - Structural connectivity (DTI tractography)
   - Represent as weighted graph G(V, E, W)

2. **Choose Null Model**
   - Standard: Configuration model (degree-preserving)
   - Spatial: Distance-constrained null model
   - Custom: Domain-specific null model

3. **Apply Modularity Maximization**
   - Use Louvain, Leiden, or similar algorithm
   - Optimize modularity Q
   - Find community assignments

4. **Interpret Communities**
   - Map to known functional networks
   - Analyze community properties
   - Compare across conditions/groups

5. **Validate and Compare**
   - Resolution parameter sensitivity
   - Statistical significance testing
   - Cross-group comparison

### Modularity Formula

**Standard modularity:**
```
Q = (1/2m) Σᵢⱼ [Aᵢⱼ - (kᵢkⱼ/2m)] δ(cᵢ, cⱼ)
```

**With resolution parameter γ:**
```
Q = (1/2m) Σᵢⱼ [Aᵢⱼ - γ(kᵢkⱼ/2m)] δ(cᵢ, cⱼ)
```

Where:
- Aᵢⱼ: Adjacency matrix
- kᵢ: Degree of node i
- m: Total edge weight
- δ(cᵢ, cⱼ): 1 if same community, 0 otherwise
- γ: Resolution parameter

### Key Parameters

| Parameter | Range | Effect |
|-----------|-------|--------|
| Resolution γ | 0.5-2.0 | Smaller = fewer, larger communities |
| Null model | Standard/Spatial | Controls expected connectivity |
| Weighted | Yes/No | Use edge weights or binarize |

## Example Usage

### Community Detection Pipeline

**Problem:** Detect functional communities in brain network

**Implementation:**
```python
import numpy as np
import networkx as nx
from community import best_partition  # python-louvain

class ModularityBrainNetworks:
    def __init__(self, resolution=1.0, n_runs=100):
        self.resolution = resolution
        self.n_runs = n_runs
    
    def detect_communities(self, connectivity_matrix, weights=None):
        """
        Detect communities using modularity maximization
        
        Parameters:
        -----------
        connectivity_matrix : array (n_regions, n_regions)
            Brain connectivity matrix
        weights : array, optional
            Edge weights (default: use connectivity values)
            
        Returns:
        --------
        communities : dict
            Node -> community assignment
        modularity : float
            Optimized modularity value
        """
        # Create graph
        G = nx.from_numpy_array(connectivity_matrix)
        
        # Run Louvain algorithm multiple times
        best_Q = -np.inf
        best_partition = None
        
        for _ in range(self.n_runs):
            partition = best_partition(
                G, 
                resolution=self.resolution,
                weight='weight'
            )
            Q = self.compute_modularity(G, partition)
            
            if Q > best_Q:
                best_Q = Q
                best_partition = partition
        
        return best_partition, best_Q
    
    def compute_modularity(self, G, partition):
        """Compute modularity for a partition"""
        from community import modularity
        return modularity(partition, G, weight='weight')
    
    def consensus_partition(self, connectivity_matrix, threshold=0.5):
        """
        Find consensus partition across multiple runs
        """
        # Collect partitions
        all_partitions = []
        for _ in range(self.n_runs):
            partition, _ = self.detect_communities(connectivity_matrix)
            all_partitions.append(partition)
        
        # Build co-assignment matrix
        n = connectivity_matrix.shape[0]
        co_assignment = np.zeros((n, n))
        
        for partition in all_partitions:
            for i in range(n):
                for j in range(n):
                    if partition[i] == partition[j]:
                        co_assignment[i, j] += 1
        
        co_assignment /= self.n_runs
        
        # Threshold and re-cluster
        consensus_matrix = (co_assignment > threshold).astype(float)
        final_partition, _ = self.detect_communities(consensus_matrix)
        
        return final_partition
```

### Resolution Parameter Sensitivity

**Analysis:**
```python
def resolution_sweep(connectivity_matrix, gamma_range=np.linspace(0.5, 2.0, 10)):
    """
    Sweep resolution parameter to find stable communities
    """
    results = []
    
    for gamma in gamma_range:
        detector = ModularityBrainNetworks(resolution=gamma)
        partition, Q = detector.detect_communities(connectivity_matrix)
        
        n_communities = len(set(partition.values()))
        
        results.append({
            'gamma': gamma,
            'modularity': Q,
            'n_communities': n_communities,
            'partition': partition
        })
    
    return results
```

### Group Comparison

**Problem:** Compare modular structure between patients and controls

**Analysis:**
```python
def compare_modularity(patient_networks, control_networks, resolution=1.0):
    """
    Compare modular structure across groups
    """
    detector = ModularityBrainNetworks(resolution=resolution)
    
    # Detect communities for each subject
    patient_partitions = []
    control_partitions = []
    
    for net in patient_networks:
        partition, Q = detector.detect_communities(net)
        patient_partitions.append({'partition': partition, 'Q': Q})
    
    for net in control_networks:
        partition, Q = detector.detect_communities(net)
        control_partitions.append({'partition': partition, 'Q': Q})
    
    # Compare modularity values
    patient_Q = [p['Q'] for p in patient_partitions]
    control_Q = [p['Q'] for p in control_partitions]
    
    # Statistical test
    from scipy import stats
    t, p = stats.ttest_ind(patient_Q, control_Q)
    
    return {
        'patient_modularity': np.mean(patient_Q),
        'control_modularity': np.mean(control_Q),
        't_stat': t,
        'p_value': p
    }
```

## Adaptations for Different Hypotheses

| Hypothesis | Modification | Null Model |
|------------|--------------|------------|
| Spatial organization | Distance-weighted | Spatial null model |
| Hierarchical structure | Multi-resolution sweep | Standard |
| Dynamic communities | Time-varying modularity | Temporal null |
| Multilayer networks | Multilayer modularity | Inter-layer coupling |

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

**User:** How can I apply modularity-brain-network-framework?

**Agent:** I'll help you understand and apply modularity-brain-network-framework...

### Example 2: Advanced Application

**User:** What are the key considerations for modularity-brain-network-framework?

**Agent:** Let me search for the latest research and best practices...

## Related Skills

- **weighted-brain-community-detection** - Weighted community detection
- **brain-higher-order-structures** - Higher-order structures
- **task-aware-brain-connectivity** - Task-based connectivity

## Source

- arXiv:2106.15428v1
- Title: Modularity maximization as a flexible and generic framework for brain network exploratory analysis
- Utility: 0.87
- Authors: Farnaz Zamani Esfahlani, Youngheun Jo, et al.
- Published: NeuroImage 2021

## Notes

- Key insight: Modularity maximization is a flexible framework
- Can be adapted for various hypotheses through reparameterization
- Review article covering applications and extensions
- Published in NeuroImage 2021
- Applications: exploratory brain network analysis, group comparison
- Multiple frontiers for future research

---

_Created: 2026-04-01_