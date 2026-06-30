---
name: common-synaptic-input-estimation-hdemg
description: "Practical methodology for estimating common synaptic input to spinal motor neurons from high-density surface EMG motor unit spike trains using openhdemg. Three complementary approaches: time-domain, frequency-domain, and network-information methods."
category: neuroscience
tags: [EMG, motor-neurons, synaptic-input, HDsEMG, openhdemg, coherence, graph-theory, motor-control, BCI]
date_created: "2026-06-29"
arxiv_id: "2606.23066v1"
authors: ["Helio V. Cabral", "Giacomo Valli", "Roberto Zanotti", "Ioannis Delis", "Francesco Negro"]
activation: "common synaptic input estimation, motor unit decomposition, HDsEMG analysis, openhdemg, coherence analysis, motor neuron control"
---

# Common Synaptic Input Estimation from Motor Unit Spike Trains

## Overview

Common synaptic input (CSI) represents the dominant component of neural drive transmitted from motor neurons to muscle. This methodology provides a practical, physiologically grounded guide for estimating CSI from populations of motor unit (MU) spike trains using **openhdemg**, an open-source Python framework.

## Three Complementary Approaches

### 1. Time-Domain: Smoothed Discharge Rates
- **Principle**: Apply smoothing to instantaneous discharge rates, then compute correlation
- **Physiological Interpretation**: Captures shared low-frequency fluctuations in motor neuron drive
- **Key Parameters**: Smoothing window width (critical choice), epoch duration
- **Implementation**: `openhdemg.csi.time_domain()`

### 2. Frequency-Domain: Cumulative Spike Train Coherence
- **Principle**: Compute coherence between cumulative spike trains (CST)
- **Physiological Interpretation**: Identifies frequency-specific common oscillatory inputs
- **Key Parameters**: Segment length, overlap, frequency bands of interest
- **Implementation**: `openhdemg.csi.coherence()`
- **Bands**: Typically 0-5 Hz (common drive), 5-20 Hz (beta), 20-40 Hz (gamma)

### 3. Network-Information: Pairwise Dependencies + Graph Theory
- **Principle**: Nonlinear pairwise dependencies modeled as graph edges
- **Physiological Interpretation**: Reveals network topology of shared inputs
- **Key Parameters**: Dependency measure (mutual information, transfer entropy), graph threshold
- **Implementation**: `openhdemg.csi.network()`

## Methodology Workflow

### Step 1: HDsEMG Decomposition
```python
import openhdemg

# Load HDsEMG data
data = openhdemg.load("emg_recording.h5")

# Decompose into motor unit spike trains
mus = openhdemg.decompose(data, method="fastica")
# Returns: list of MotorUnit objects with spike_trains attribute
```

### Step 2: Motor Unit Cleaning
```python
# Filter MUs by quality metrics
mus_clean = openhdemg.filter_mu(mus, 
    min_discharges=50,          # Minimum spike count
    maxisi_ratio=3.0,           # Maximum ISI ratio (refractory check)
    min_sil=0.9)                # Minimum silhouette score for decomposition quality
```

### Step 3: CSI Estimation

#### Time-Domain Method
```python
# Smoothed discharge rate correlation
csi_td = openhdemg.csi.time_domain(
    spike_trains=[mu.spike_train for mu in mus_clean],
    smoothing_window=0.4,  # seconds (critical parameter)
    bin_size=0.001,         # 1ms bins
    epoch_duration=5.0      # seconds per epoch
)
# Returns: correlation matrix (N_MUs x N_MUs)
```

#### Frequency-Domain Method
```python
# Cumulative spike train coherence
csi_freq = openhdemg.csi.coherence(
    spike_trains=[mu.spike_train for mu in mus_clean],
    fs=1000,                # sampling frequency
    n_segments=10,          # number of segments for averaging
    overlap=0.5,            # 50% overlap
    f_range=(0, 50)         # frequency range of interest
)
# Returns: coherence spectrum, common_drive_strength per frequency band
```

#### Network-Information Method
```python
# Pairwise nonlinear dependencies as graph
csi_net = openhdemg.csi.network(
    spike_trains=[mu.spike_train for mu in mus_clean],
    method="mutual_information",  # or "transfer_entropy"
    threshold=0.1,           # graph edge threshold
    bin_size=0.01            # discretization bin
)
# Returns: graph object with nodes=MUs, edges=shared input strength
```

## Critical Parameter Selection Guide

| Parameter | Recommended Range | Effect of Too Small | Effect of Too Large |
|-----------|-------------------|---------------------|---------------------|
| Smoothing window | 200-500 ms | High-frequency noise included | Temporal resolution lost |
| Segment length (freq) | 2-5 s | Poor frequency resolution | Fewer averages |
| Overlap | 0.5 | Fewer segments | Redundant computation |
| MI threshold (network) | 0.05-0.2 | Dense graph, many false edges | Sparse graph, misses connections |
| Bin size | 5-20 ms | Computationally expensive | Loss of temporal precision |

## Key Findings from Literature

1. **Decomposition Quality Directly Affects Estimates**: Poor MU decomposition propagates errors into CSI estimates
2. **Time-Domain is Most Robust**: For general common drive assessment
3. **Frequency-Domain Reveals Oscillatory Structure**: Essential for studying beta/gamma oscillations
4. **Network Method Reveals Topology**: Shows which MUs share inputs (not just strength)
5. **No Single Method is Best**: Use complementary approaches for complete picture

## Pitfalls and Warnings

1. **Smoothing Window**: Most critical parameter in time-domain method. Default values may not suit all datasets. Always perform sensitivity analysis.
2. **Number of MUs**: Methods require sufficient MU population (>20 MUs recommended for stable estimates)
3. **Non-stationarity**: CSI can change during fatiguing contractions. Use sliding windows for time-varying analysis.
4. **Crosstalk**: Ensure decomposition is from single muscle; crosstalk contaminates CSI estimates.
5. **Discharge Rate Confound**: Common input estimates correlate with mean discharge rate. Control for this confound.

## Applications

- **Motor Control Research**: Quantify shared neural drive during different tasks
- **Clinical Assessment**: Detect changes in common input in neurological disorders
- **Aging Studies**: Track changes in synaptic input organization with age
- **Fatigue Research**: Monitor how common input evolves during sustained contractions
- **BCI/Neuroprosthetics**: Decode motor intent from shared input patterns

## Reference

Cabral, H.V., Valli, G., Zanotti, R., Delis, I., & Negro, F. (2026). Estimating common synaptic inputs to spinal motor neurons from motor unit spike trains using openhdemg. arXiv:2606.23066v1

## Related Skills

- `eeg-brain-connectivity-bci`: Brain connectivity for BCI applications
- `bci-rehabilitation-protocols`: BCI rehabilitation protocols
- `eeg-preprocessing-reliability`: EEG preprocessing reliability assessment
