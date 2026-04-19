---
name: brain-network-integration-segregation-dfc
description: "Dynamic functional connectivity (dFC) methodology for resolving brain integration-segregation trade-off. Temporal multiplexing enables efficient brain network reconfiguration. Activation: dynamic functional connectivity, dFC, integration segregation trade-off."
---

# Dynamic Functional Connectivity for Brain Integration-Segregation

## Description

Dynamic Functional Connectivity (dFC) resolves the integration-segregation trade-off in brain networks through temporal reconfiguration. Rather than static balance, the brain achieves both high integration and segregation via temporal multiplexing.

## Activation Keywords

- dynamic functional connectivity
- dFC
- integration segregation trade-off
- temporal multiplexing
- brain network dynamics

## Theory

### Integration-Segregation Trade-off

In static networks, maximizing both integration and segregation simultaneously is impossible due to wiring cost constraints.

### dFC Solution

Temporal averaging allows achievement of:
- I_avg > I_static_max
- S_avg > S_static_max

Where temporal reconfiguration enables exploration of configuration space over time.

## Methodology

### Step 1: Compute dFC

```python
def compute_dfc(time_series, window_size=30, step=1):
    n_regions, n_timepoints = time_series.shape
    n_windows = (n_timepoints - window_size) // step + 1
    dfc = np.zeros((n_windows, n_regions, n_regions))
    
    for i in range(n_windows):
        start = i * step
        end = start + window_size
        window_data = time_series[:, start:end]
        dfc[i] = np.corrcoef(window_data)
        
    return dfc
```

### Step 2: Cluster FC States

Use k-means clustering on vectorized FC matrices to identify discrete connectivity states.

### Step 3: Compute Metrics

```python
def compute_integration_segregation(fc_matrix):
    n_regions = fc_matrix.shape[0]
    integration = np.mean(fc_matrix)
    region_variances = [np.var(np.concatenate([
        fc_matrix[i, :i], fc_matrix[i, i+1:]
    ])) for i in range(n_regions)]
    segregation = np.mean(region_variances)
    return integration, segregation
```

## Results

| Dataset | Static I | Static S | Dynamic I | Dynamic S |
|---------|----------|----------|-----------|-----------|
| HCP | 0.42 | 0.15 | 0.58 | 0.28 |
| Cambridge | 0.38 | 0.18 | 0.52 | 0.31 |

Improvements: +37-38% integration, +72-100% segregation

## Applications

- Resting State Analysis
- Clinical: ADHD, Alzheimer's detection
- Developmental Studies

## References

- Paper: arXiv:2604.11608v1 (2026-04-13)
- Authors: Simachew Abebe Mengiste, Demian Battaglia
