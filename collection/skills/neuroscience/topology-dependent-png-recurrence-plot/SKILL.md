---
name: topology-dependent-png-recurrence-plot
description: Topology-Dependent Emergence of Polychronous Neuronal Groups via Recurrence Plot characterization. Analyzes how small-world network topology drives PNG formation in spiking networks with STDP and heterogeneous delays.
arxiv_id: "2606.25874"
tags: [spiking-neural-networks, polychronous-groups, STDP, recurrence-plots, small-world-topology, neural-computation]
---

# Topology-Dependent Emergence of Polychronous Neuronal Groups

## Background

Polychronous Neuronal Groups (PNGs) are reproducible, time-locked spatiotemporal firing cascades stabilized by Spike-Timing-Dependent Plasticity (STDP) and heterogeneous axonal delays. They provide a combinatorially rich substrate for neural computation, but their structural determinants remain poorly understood.

## Core Methodology

### Network Simulation Setup

- **Network:** N=1000 Izhikevich neurons, recurrent connectivity
- **Duration:** 10 hours of biological time
- **Plasticity:** STDP with heterogeneous axonal delays
- **Result:** 1545 unique PNGs identified via offline event-driven detection

### Topology Sweep: Watts-Strogatz Model

**Key Finding:** Clustering coefficient C is the PRIMARY structural driver of PNG yield.

| Topology | C value | PNG count | Capacity loss |
|----------|---------|-----------|---------------|
| Ring lattice | ~0.35 | ~850 PNGs | baseline |
| Random graph | ~0.20 | <50 PNGs | >90% loss |

**Implication:** Small-world topology (intermediate clustering + short path lengths) is the structural optimum for polychronization.

### Recurrence Plot (RP) Framework

**Innovation:** Sparse-dot-product Recurrence Plot decoder for PNG identification — entirely independent of anatomical neuron labelling.

**How it works:**
1. Compute phase-space recurrence matrix from spike train data
2. PNGs appear as **unit-slope diagonal structures** in the recurrence matrix
3. Recurrence Quantification Analysis (RQA) yields DET~0.65, quantifying trajectory reproducibility

**Advantage:** Label-free — works without knowing which neuron is which, only requires spike timing data.

## Key Results

1. **Clustering coefficient C** is the dominant predictor of PNG yield (not average path length)
2. Transition from ring lattice → random graph causes >90% representational capacity loss
3. RP decoder provides principled, anatomy-independent PNG identification
4. DET~0.65 quantifies the network's dynamical reproducibility

## Implementation Guide

```python
# Pseudo-code for RP-based PNG detection
def detect_pngs_via_recurrence_plot(spike_trains, neuron_ids, time_bins):
    """
    spike_trains: binary matrix (neurons x time_bins)
    Returns: list of PNGs as diagonal structures in RP
    """
    # 1. Compute sparse dot-product recurrence matrix
    R = sparse_dot_product(spike_trains, spike_trains.T)
    
    # 2. Identify unit-slope diagonal structures
    diagonals = extract_diagonals(R, slope=1.0, min_length=5)
    
    # 3. RQA: compute determinism (DET)
    det = compute_determinism(R, diagonals)
    
    # 4. Each diagonal = one PNG (spatiotemporal firing cascade)
    pngs = [extract_png(diag, spike_trains, neuron_ids) for diag in diagonals]
    return pngs, det
```

### Watts-Strogatz Topology Sweep

```python
def topology_png_yield(n_neurons, p_rewire_range, n_simulations=10):
    """
    Sweep rewiring probability p in Watts-Strogatz model.
    Measure PNG yield as function of clustering coefficient C.
    """
    results = []
    for p in p_rewire_range:
        G = watts_strogatz_graph(n_neurons, k=10, p=p)
        C = nx.clustering(G)  # clustering coefficient
        # Run spiking simulation with STDP
        pngs = simulate_and_detect_pngs(G, duration=10*3600*1000)  # 10h in ms
        results.append((p, C, len(pngs)))
    return results
```

## Pitfalls

- Small-world optimum requires BOTH high clustering AND short paths — random graphs lose PNGs due to low clustering, not long paths
- RP decoder requires sufficient spike density; very sparse firing rates may miss PNGs
- STDP parameters must allow stable cascade formation — too strong depression kills PNGs
- Heterogeneous delays are essential — uniform delays cannot support polychronization

## Verification

- Compare PNG count across Watts-Strogatz p values
- Verify RP diagonals match anatomically-labelled PNG detections
- Check DET correlates with PNG reproducibility across trials

## Activation Triggers

Keywords: polychronous neuronal groups, PNG, recurrence plots, small-world topology, STDP, Izhikevich, clustering coefficient, neural computation, spatiotemporal cascades, Watts-Strogatz
