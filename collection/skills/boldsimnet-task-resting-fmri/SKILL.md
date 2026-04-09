# boldsimnet-task-resting-fmri - BOLDSimNet: Examining Brain Network Similarity between Task and Resting-State fMRI

## Description

A novel framework using Multivariate Transfer Entropy (MTE) to measure causal connectivity and network similarity across different cognitive states. Groups functionally similar ROIs rather than spatially adjacent nodes for improved network alignment accuracy.

**Source:** arXiv:2504.01274v1
**Utility:** 0.91

## Activation Keywords

- BOLDSimNet
- task resting fMRI comparison
- multivariate transfer entropy
- causal connectivity similarity
- network reconfiguration
- attention network development
- DAN DMN similarity

## Core Concepts

### 1. Framework Overview

```
Task fMRI + Resting fMRI → MTE Causal Connectivity → ROI Grouping → Network Similarity Score
```

**Key insight:** Measure network reconfiguration between cognitive states using transfer entropy.

### 2. Multivariate Transfer Entropy (MTE)

| Concept | Description |
|---------|-------------|
| **Causal connectivity** | Directed information flow between ROIs |
| **Multivariate** | Captures dependencies across multiple regions |
| **Noise robust** | Better than traditional causal methods |

### 3. ROI Grouping Strategy

**Functional similarity** over spatial adjacency:
- Groups ROIs by functional similarity
- Improves network alignment accuracy
- Better comparison across cognitive states

### 4. Network Similarity Metrics

| Network | Finding |
|---------|---------|
| **DAN (Dorsal Attention Network)** | Adolescents show more task-rest differences |
| **DMN (Default Mode Network)** | Adolescents show more task-rest differences |
| **Children vs Adolescents** | Children have higher task-rest similarity |

## Step-by-Step Instructions

### 1. Compute Multivariate Transfer Entropy

```python
import numpy as np
from scipy.stats import entropy

def compute_transfer_entropy(source, target, lag=1, bins=10):
    """
    Compute transfer entropy from source to target.
    
    TE(X→Y) = H(Y_t+1 | Y_t) - H(Y_t+1 | Y_t, X_t)
    
    Args:
        source: Source time series
        target: Target time series
        lag: Time lag
        bins: Number of bins for discretization
    
    Returns:
        Transfer entropy value
    """
    # Discretize
    source_discrete = np.histogram(source, bins=bins)[0]
    target_discrete = np.histogram(target, bins=bins)[0]
    
    # Shift for lag
    target_future = target_discrete[lag:]
    target_present = target_discrete[:-lag]
    source_present = source_discrete[:-lag]
    
    # Compute joint distributions
    # P(Y_t+1, Y_t)
    joint_Y = np.histogram2d(target_future, target_present, bins=bins)[0]
    
    # P(Y_t+1, Y_t, X_t)
    joint_YX = np.histogramdd([target_future, target_present, source_present], 
                               bins=[bins, bins, bins])[0]
    
    # Compute conditional entropies
    # H(Y_t+1 | Y_t)
    p_joint_Y = joint_Y / joint_Y.sum()
    p_Y_present = target_present / target_present.sum()
    H_Y_given_Y = entropy(p_joint_Y) - entropy(p_Y_present)
    
    # H(Y_t+1 | Y_t, X_t)
    p_joint_YX = joint_YX / joint_YX.sum()
    H_Y_given_YX = entropy(p_joint_YX) - entropy(np.histogramdd(
        [target_present, source_present], bins=[bins, bins])[0] / 
        np.histogramdd([target_present, source_present], bins=[bins, bins])[0].sum())
    
    # Transfer entropy
    TE = H_Y_given_Y - H_Y_given_YX
    
    return TE

def compute_mte_matrix(timeseries_data, lag=1, bins=10):
    """
    Compute multivariate transfer entropy matrix.
    
    Args:
        timeseries_data: ROI timeseries (n_rois, n_timepoints)
        lag: Time lag
        bins: Discretization bins
    
    Returns:
        MTE matrix (n_rois, n_rois)
    """
    n_rois = timeseries_data.shape[0]
    mte_matrix = np.zeros((n_rois, n_rois))
    
    for i in range(n_rois):
        for j in range(n_rois):
            if i != j:
                mte_matrix[i, j] = compute_transfer_entropy(
                    timeseries_data[i], timeseries_data[j], lag, bins
                )
    
    return mte_matrix
```

### 2. ROI Functional Grouping

```python
def group_rois_by_function(mte_matrix, n_groups=10):
    """
    Group ROIs by functional similarity (not spatial adjacency).
    
    Args:
        mte_matrix: Transfer entropy matrix
        n_groups: Number of functional groups
    
    Returns:
        Group assignments for each ROI
    """
    from sklearn.cluster import SpectralClustering
    
    # Use MTE matrix as similarity
    # Normalize
    similarity = (mte_matrix + mte_matrix.T) / 2
    
    # Spectral clustering
    clustering = SpectralClustering(n_clusters=n_groups, affinity='precomputed')
    groups = clustering.fit_predict(similarity)
    
    return groups

def compute_group_connectivity(mte_matrix, groups):
    """
    Compute connectivity between functional groups.
    
    Args:
        mte_matrix: ROI-level MTE matrix
        groups: Group assignments
    
    Returns:
        Group-level connectivity matrix
    """
    n_groups = len(np.unique(groups))
    group_conn = np.zeros((n_groups, n_groups))
    
    for i in range(n_groups):
        for j in range(n_groups):
            # Average MTE between groups
            rois_i = np.where(groups == i)[0]
            rois_j = np.where(groups == j)[0]
            
            mte_values = []
            for ri in rois_i:
                for rj in rois_j:
                    mte_values.append(mte_matrix[ri, rj])
            
            group_conn[i, j] = np.mean(mte_values)
    
    return group_conn
```

### 3. Network Similarity Score

```python
def compute_network_similarity(task_matrix, resting_matrix, groups):
    """
    Compute similarity between task and resting networks.
    
    Args:
        task_matrix: Task state MTE matrix
        resting_matrix: Resting state MTE matrix
        groups: ROI group assignments
    
    Returns:
        Similarity score
    """
    # Group-level connectivity
    task_group = compute_group_connectivity(task_matrix, groups)
    resting_group = compute_group_connectivity(resting_matrix, groups)
    
    # Similarity metric (correlation)
    from scipy.stats import pearsonr
    
    # Flatten matrices
    task_flat = task_group.flatten()
    resting_flat = resting_group.flatten()
    
    # Correlation
    similarity, _ = pearsonr(task_flat, resting_flat)
    
    return similarity

def compare_task_rest_similarity(task_data, resting_data, n_groups=10):
    """
    Full pipeline for task-rest comparison.
    
    Args:
        task_data: Task fMRI timeseries
        resting_data: Resting fMRI timeseries
        n_groups: Number of functional groups
    
    Returns:
        Similarity analysis results
    """
    # Compute MTE matrices
    task_mte = compute_mte_matrix(task_data)
    resting_mte = compute_mte_matrix(resting_data)
    
    # Group ROIs
    groups = group_rois_by_function((task_mte + resting_mte) / 2, n_groups)
    
    # Compute similarity
    similarity = compute_network_similarity(task_mte, resting_mte, groups)
    
    return {
        'task_mte': task_mte,
        'resting_mte': resting_mte,
        'groups': groups,
        'similarity': similarity
    }
```

### 4. Developmental Analysis

```python
def compare_age_groups(children_data, adolescents_data):
    """
    Compare task-rest similarity across age groups.
    
    Args:
        children_data: List of (task, resting) tuples for children
        adolescents_data: List of (task, resting) tuples for adolescents
    
    Returns:
        Developmental comparison results
    """
    children_sim = []
    adolescents_sim = []
    
    for task, resting in children_data:
        result = compare_task_rest_similarity(task, resting)
        children_sim.append(result['similarity'])
    
    for task, resting in adolescents_data:
        result = compare_task_rest_similarity(task, resting)
        adolescents_sim.append(result['similarity'])
    
    from scipy.stats import ttest_ind
    
    t_stat, p_value = ttest_ind(children_sim, adolescents_sim)
    
    return {
        'children_mean': np.mean(children_sim),
        'adolescents_mean': np.mean(adolescents_sim),
        't_stat': t_stat,
        'p_value': p_value
    }
```

### 5. DAN/DMN Analysis

```python
def analyze_attention_networks(mte_matrix, roi_labels):
    """
    Analyze DAN and DMN connectivity.
    
    Args:
        mte_matrix: MTE connectivity matrix
        roi_labels: ROI network labels
    
    Returns:
        DAN and DMN specific connectivity
    """
    # Identify DAN and DMN ROIs
    dan_rois = np.where(roi_labels == 'DAN')[0]
    dmn_rois = np.where(roi_labels == 'DMN')[0]
    
    # Within-network connectivity
    dan_within = mte_matrix[dan_rois, dan_rois].mean()
    dmn_within = mte_matrix[dmn_rois, dmn_rois].mean()
    
    # Between-network connectivity
    dan_dmn = mte_matrix[dan_rois, dmn_rois].mean()
    dmn_dan = mte_matrix[dmn_rois, dan_rois].mean()
    
    return {
        'dan_within': dan_within,
        'dmn_within': dmn_within,
        'dan_to_dmn': dan_dmn,
        'dmn_to_dan': dmn_dan
    }
```

## Tools Used

- `numpy` - Numerical computations
- `scipy.stats` - Statistical tests
- `sklearn.cluster` - Spectral clustering
- `exec` - Run analysis scripts
- `read` - Load fMRI data

## Example Use Cases

### 1. Task-Rest Similarity

```python
# Compute similarity
result = compare_task_rest_similarity(task_fmri, resting_fmri)
print(f"Task-Rest Similarity: {result['similarity']:.3f}")
```

### 2. Developmental Comparison

```python
# Compare children vs adolescents
dev_result = compare_age_groups(children_data, adolescents_data)
print(f"Children: {dev_result['children_mean']:.3f}")
print(f"Adolescents: {dev_result['adolescents_mean']:.3f}")
print(f"p-value: {dev_result['p_value']:.4f}")
```

### 3. Network Analysis

```python
# Analyze DAN/DMN
network_result = analyze_attention_networks(task_mte, roi_labels)
print(f"DAN within-network: {network_result['dan_within']:.3f}")
print(f"DMN within-network: {network_result['dmn_within']:.3f}")
```

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: Compute Multivariate Transfer Entropy

## Examples

### Example 1: Basic Application

**User:** I need to apply boldsimnet-task-resting-fmri - BOLDSimNet: Examining Brain Network Similarity between Task and Resting-State fMRI to my analysis.

**Agent:** I'll help you apply boldsimnet-task-resting-fmri. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for boldsimnet-task-resting-fmri?

**Agent:** Let me search for the latest research and best practices...

## Related Skills

- `entropy-brain-connectivity-paths` - Entropy as connectivity indicators
- `task-aware-brain-connectivity` - Task-based connectivity
- `time-varying-brain-connectivity` - Time-varying connectivity

## References

- Kim, B. (2025). "BOLDSimNet: Examining Brain Network Similarity between Task and Resting-State fMRI" arXiv:2504.01274v1 [q-bio.NC]

---

**Created:** 2026-03-29 17:05
**Author:** Aerial (from arXiv:2504.01274v1)