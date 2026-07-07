---
name: topology-dependent-polychronous-groups-recurrence
description: Topology-Dependent Emergence of Polychronous Neuronal Groups - Recurrence-plot characterization of how network topology (small-world, scale-free, random) influences the formation and stability of polychronous neuronal groups in spiking neural networks.
trigger_words: ["polychronous groups", "recurrence plot", "network topology SNN", "small-world spiking", "polychrony", "neuronal groups topology"]
arxiv_id: 2606.26123
authors: ["Research Group"]
date: 2026-06-24
categories: ["q-bio.NC", "cs.NE"]
---

# Topology-Dependent Emergence of Polychronous Neuronal Groups

## Overview

Polychronous neuronal groups (PNGs) are reliable spatiotemporal firing patterns that emerge in spiking neural networks through precise timing of spikes. This work investigates how network topology (small-world, scale-free, random) affects the formation, stability, and computational properties of PNGs using recurrence plot analysis.

## Core Concepts

### Polychronous Neuronal Groups (PNGs)
- **Definition**: Sequences of neurons that fire with precise millisecond timing, triggered by specific input patterns
- **Key property**: Not synfire chains — PNGs allow for "polychrony" where multiple groups can be active simultaneously with different timing patterns
- **Computational role**: Form the substrate for temporal coding and memory in SNNs

### Recurrence Plot Analysis
- **Recurrence**: A state recurrence occurs when the network returns to a similar state at different times
- **Recurrence Plot (RP)**: 2D visualization showing when states recur: $R_{i,j} = \Theta(\epsilon - ||x_i - x_j||)$
- **Quantification**: 
  - Recurrence Rate (RR): Density of recurrent points
  - Determinism (DET): Proportion of recurrent points forming diagonal lines
  - Laminarity (LAM): Proportion of recurrent points forming vertical/horizontal structures

## Methodology

### Network Topologies Tested
1. **Random Networks**: Erdős-Rényi random graphs, uniform connection probability
2. **Small-World Networks**: Watts-Strogatz model with high clustering + short path length
3. **Scale-Free Networks**: Barabási-Albert preferential attachment, power-law degree distribution

### Simulation Protocol
1. Generate network with specific topology (N=1000 neurons)
2. Use Izhikevich neuron model with STDP learning
3. Present repeated input patterns over time
4. Record spike trains and compute recurrence plots
5. Quantify PNG emergence and stability

### Key Metrics
- **PNG Detection**: Identify groups of neurons with reliable temporal firing sequences
- **Stability Index**: Measure how consistently PNGs recur across trials
- **Capacity**: Number of distinct PNGs the network can maintain
- **Lifetime**: How long PNGs persist before degrading

## Key Findings

### 1. Topology-Dependent PNG Emergence
- **Small-World**: Highest PNG capacity and stability
  - High clustering supports local pattern formation
  - Short paths enable global coordination
  - Optimal balance for complex temporal patterns

- **Scale-Free**: Moderate capacity, high robustness
  - Hub neurons act as pacemakers for PNGs
  - Robust to random failures but vulnerable to hub removal
  - Hierarchical structure supports multi-scale temporal coding

- **Random**: Lowest PNG capacity, unstable
  - Lack of structure prevents reliable pattern formation
  - High variance in PNG properties
  - Poor temporal coding capability

### 2. Recurrence Plot Signatures
- **Small-World**: Rich diagonal structures in RP, high determinism (DET > 0.7)
- **Scale-Free**: Block-like structures corresponding to hub activity
- **Random**: Scattered points, low determinism (DET < 0.3)

### 3. Computational Implications
- **Small-World optimal for temporal coding**: Supports maximum number of distinct temporal patterns
- **Scale-Free optimal for robustness**: PNGs persist despite neuron loss
- **Random networks**: Cannot support complex temporal computations

## Connection to Neuroscience

### Biological Plausibility
- Real neural networks exhibit small-world and scale-free properties
- PNG theory provides mechanism for temporal binding and sequence learning
- Recurrence analysis applicable to EEG/MEG data for detecting brain state dynamics

### Brain Disorders
- Alzheimer's: Disruption of small-world topology may impair PNG formation
- Epilepsy: Excessive synchronization visible in recurrence plots
- Schizophrenia: Altered small-world properties may affect temporal coding

## Implementation Patterns

### Pattern 1: Network Generation
```python
import networkx as nx

def create_small_world(n=1000, k=10, p=0.1):
    """Watts-Strogatz small-world network"""
    return nx.watts_strogatz_graph(n, k, p)

def create_scale_free(n=1000, m=10):
    """Barabási-Albert scale-free network"""
    return nx.barabasi_albert_graph(n, m)

def create_random(n=1000, p=0.01):
    """Erdős-Rényi random network"""
    return nx.erdos_renyi_graph(n, p)
```

### Pattern 2: Recurrence Plot Computation
```python
import numpy as np
from pyunicorn.timeseries import RecurrencePlot

def compute_recurrence_plot(spike_trains, embedding_dim=3, time_delay=10, epsilon=0.1):
    """
    Compute recurrence plot from spike train data
    
    Args:
        spike_trains: Binary spike matrix (time x neurons)
        embedding_dim: Embedding dimension for phase space reconstruction
        time_delay: Time delay for embedding
        epsilon: Recurrence threshold
    """
    # Convert spike trains to continuous signal (e.g., firing rate)
    signal = compute_firing_rate(spike_trains, window=50)
    
    # Create recurrence plot
    rp = RecurrencePlot(signal, dim=embedding_dim, tau=time_delay, 
                        threshold=epsilon, normalize=True)
    
    # Extract recurrence quantification measures
    RR = rp.recurrence_rate()
    DET = rp.determinism()
    LAM = rp.laminarity()
    
    return rp, {'RR': RR, 'DET': DET, 'LAM': LAM}
```

### Pattern 3: PNG Detection
```python
def detect_polychronous_groups(spike_trains, time_window=100, min_neurons=5):
    """
    Detect polychronous groups from spike trains
    
    Args:
        spike_trains: Binary spike matrix (time x neurons)
        time_window: Time window for pattern detection (ms)
        min_neurons: Minimum neurons in a group
    """
    # Find spike sequences with precise timing
    pngs = []
    
    # For each time point, find co-active neurons
    for t in range(spike_trains.shape[0] - time_window):
        window = spike_trains[t:t+time_window]
        active_neurons = np.where(window.sum(axis=0) > 0)[0]
        
        if len(active_neurons) >= min_neurons:
            # Extract precise timing pattern
            pattern = extract_temporal_pattern(window, active_neurons)
            pngs.append(pattern)
    
    # Cluster similar patterns
    unique_pngs = cluster_patterns(pngs, similarity_threshold=0.8)
    
    return unique_pngs
```

## Pitfalls & Considerations

### 1. Parameter Sensitivity
- PNG detection highly sensitive to time window and similarity threshold
- **Solution**: Use grid search with stability metrics
- **Pitfall**: Overly permissive thresholds create spurious PNGs

### 2. Network Size Effects
- Small networks may not show topology-dependent effects
- **Solution**: Use networks with N > 500 neurons
- **Pitfall**: Finite-size effects dominate in small networks

### 3. Neuron Model Choice
- Izhikevich model parameters affect PNG formation
- **Solution**: Use biologically plausible parameters
- **Pitfall**: Unphysiological parameters may create artifacts

### 4. STDP Parameters
- Learning rate and timing window affect PNG stability
- **Solution**: Match to biological constraints
- **Pitfall**: Too strong STDP leads to runaway excitation

### 5. Recurrence Plot Interpretation
- Visual patterns can be misleading without quantification
- **Solution**: Always compute RQA measures (RR, DET, LAM)
- **Pitfall**: Recurrence can arise from periodicity, not complexity

## Applications

### SNN Design
- **Optimize topology**: Use small-world for temporal coding tasks
- **Robust systems**: Scale-free for fault-tolerant SNNs
- **Benchmark**: Compare new architectures against topology baselines

### Neuroscience Research
- **Brain network analysis**: Apply recurrence plots to EEG/MEG data
- **Disease modeling**: Simulate topology disruptions in disorders
- **Developmental studies**: Track topology evolution during learning

### Machine Learning
- **Temporal coding**: Design SNNs for temporal pattern recognition
- **Memory systems**: Use PNGs as memory substrate
- **Neuromorphic computing**: Optimize hardware topology for PNG support

## Activation Triggers

Use this skill when:
- Designing SNNs with specific temporal coding capabilities
- Analyzing temporal patterns in neural data
- Studying relationship between network structure and dynamics
- Implementing recurrence-based analysis methods
- Modeling brain disorders affecting network topology
- Optimizing neuromorphic hardware architectures
