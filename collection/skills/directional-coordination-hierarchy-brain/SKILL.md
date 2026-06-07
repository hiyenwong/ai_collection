---
name: directional-coordination-hierarchy-brain
version: 1.0.0
description: Directional coordination hierarchy in large-scale brain dynamics — identifies three recurrent resting-state coordination regimes (feedback-dominated, feedforward-dominated, integrative), shows this framework is disrupted in schizophrenia, and links directional functional dynamics to symptom severity and cognition.
triggers:
  - directional brain coordination
  - large-scale brain dynamics hierarchy
  - resting-state directional coordination
  - cortical hierarchy dynamics
  - brain coordination regimes
  - feedforward feedback brain dynamics
  - integrative coordination brain
  - schizophrenia brain dynamics
  - directional functional connectivity
  - cortical information flow hierarchy
authors:
  - Wiafe, S.-L.
  - Soleimani, N.
  - Fu, Z.
  - Miller, R.
  - Calhoun, V.
source: "biorxiv:10.64898/2026.05.25.727703"
published: "2026-05-25"
---

# Directional Coordination Hierarchy in Large-Scale Brain Dynamics

## Overview

This methodology reveals that **resting-state brain dynamics are fundamentally organized along a directional coordination axis** that recapitulates the classical cortical hierarchy. Using directed measures of interregional coordination on fMRI data, the work identifies three stable **recurrent coordination regimes** and demonstrates their disruption in schizophrenia.

## Core Framework

### Three Coordination Regimes

1. **Feedback-dominated mode**: Transmodal cortex (prefrontal, default mode) leads sensory systems — top-down information flow
2. **Feedforward-dominated mode**: Sensory systems lead transmodal cortex — bottom-up processing
3. **Integrative mode**: Balanced bidirectional exchange across all cortical areas

These three modes define a **low-dimensional coordination landscape** that:
- Replicates across four independent cohorts (high stability)
- Constitutes a fundamental property of the adult brain
- Tracks hierarchical information flow known from structural connectivity

### Analytical Approach

```
Step 1: Extract directionality of interregional coordination
  - Use directed functional connectivity measures (e.g., Granger causality, transfer entropy)
  - Apply to resting-state fMRI time series
  - Focus on temporal dynamics of coupling direction

Step 2: Identify recurrent coordination regimes
  - Cluster directors of interregional coordination
  - Identify stable 3-mode solution across cohorts

Step 3: Characterize the coordination landscape
  - Compute persistence/dwell time per regime
  - Measure global convergence rate and entropy
  - Map regimes onto cortical hierarchy axis (unimodal → transmodal)

Step 4: Apply to clinical population
  - Compare coordination landscapes in schizophrenia vs controls
  - Correlate with symptom severity (PANSS), cognition, medication
  - Mediation analysis for medication effects
```

## Key Findings

### Schizophrenia Disrupts the Coordination Landscape
- **Feedback-dominated coordination becomes less persistent** → reduced top-down control
- **Integrative coordination becomes more persistent** → excessive integration
- **Global dynamics shift**: faster convergence, reduced entropy → loss of dynamical flexibility and directional constraint

### Clinical Correlates
- Coordination landscape alterations **track symptom severity** (positive/negative symptoms)
- Predict **cognitive performance** independently
- **Medication exposure** modulates integrative coordination through feedforward dynamics

### Dopaminergic Mechanism
- Mediation analyses suggest medication-related effects on integrative coordination are statistically routed through feedforward dynamics
- Consistent with **dopaminergic modulation of recurrent cortical loops** as a mechanistic candidate

## Applications

| Use Case | Approach |
|----------|----------|
| Biomarker development | Coordination regime persistence as psychiatric biomarker |
| Treatment monitoring | Track coordination landscape changes with antipsychotics |
| Cognitive neuroscience | Map task-evoked coordination to resting-state modes |
| Brain stimulation targeting | Identify regime transitions for optimal intervention timing |
| Normative development | Track coordination hierarchy emergence across lifespan |

## Implementation Notes

```python
# Pseudocode for directional coordination analysis
import numpy as np
from scipy import signal

def compute_directional_coordination(fmri_timeseries, TR=2.0):
    """
    Compute directed coordination from fMRI timeseries.
    
    Parameters:
        fmri_timeseries: (n_timepoints, n_regions) array
        TR: repetition time in seconds
    
    Returns:
        directional_matrix: (n_regions, n_regions) directed coupling
    """
    n_t, n_roi = fmri_timeseries.shape
    
    # Option 1: Phase-based directionality (e.g., phase lead/lag)
    # Apply Hilbert transform to get instantaneous phase
    analytic = signal.hilbert(fmri_timeseries, axis=0)
    phases = np.angle(analytic)
    
    # Compute phase differences between all pairs
    # Positive = region i leads region j
    phase_diff = phases[:, :, None] - phases[:, None, :]  # (T, ROI, ROI)
    
    # Average phase lead
    directionality = np.mean(np.sin(phase_diff), axis=0)
    
    return directionality

def identify_coordination_regimes(directionality_timeseries, n_regimes=3):
    """
    Cluster directional coordination states into regimes.
    """
    from sklearn.cluster import KMeans
    
    # Reshape for clustering
    T, R, R = directionality_timeseries.shape
    X = directionality_timeseries.reshape(T, R*R)
    
    # Fit 3-regime model
    kmeans = KMeans(n_clusters=n_regimes, random_state=42)
    labels = kmeans.fit_predict(X)
    centers = kmeans.cluster_centers_.reshape(n_regimes, R, R)
    
    return labels, centers
```

## Comparison to Prior Work

| Method | This Work | Prior Art |
|--------|-----------|-----------|
| Connectivity type | Directed (dynamic) | Undirected (static) |
| Hierarchy expression | Tested in spontaneous dynamics | Only in task/structural data |
| Clinical translation | 3-regime landscape as biomarker | Single connectivity metric |
| Replication | 4 cohorts | Typically 1-2 |

## Pitfalls

- **Directional measures are sensitive to hemodynamic response delays** — control for HRF differences between regions
- **Three-mode solution must be validated** across scanning parameters and demographics before clinical use
- Mediation analyses are correlational — mechanism remains hypothetical
- Faster convergence in schizophrenia could reflect altered signal-to-noise rather than neural changes

## Related Skills

- `brain-state-transition-network-control` — state space models of brain dynamics
- `brain-criticality-hypothesis-assessment` — dynamical criticality in brain networks
- `time-varying-brain-connectivity` — time-varying functional connectivity methods
- `adaptive-flow-routing-brain-networks` — flow-based brain connectivity routing
