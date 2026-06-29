---
name: canns-toolkit-attractor-networks
description: "Comprehensive open-source toolkit for Continuous Attractor Neural Network (CANN) research combining Python library on BrainPy/JAX, Rust acceleration backend, and persistent homology analyzer. Use for implementing 1D/2D CANNs, spike-frequency adaptation variants, grid cell networks, hierarchical path integration models, analyzing attractor geometry in neural recordings via topological methods, recovering ring-like and toroidal attractor signatures. Activation: continuous attractor, CANN, grid cells, place cells, head direction cells, path integration, attractor geometry, persistent homology, BrainPy, JAX, neural recordings analysis, topological data analysis."
metadata:
  arxiv_id: "2606.27783"
  published: "2026-06-26"
  authors: "Sichao He, Aiersi Tuerhong, Shangjun She, Tianhao Chu, Yuling Wu, Junfeng Zuo, Si Wu"
  tags: [continuous-attractor-neural-networks, toolkit, grid-cells, path-integration, persistent-homology, BrainPy, JAX]
---

# CANNs: A Toolkit for Research on Continuous Attractor Neural Networks

**arXiv:2606.27783** | He et al. | 26 Jun 2026

## Overview

First comprehensive open-source toolkit unifying the full CANN research workflow, addressing the fragmentation in CANN research where most results rely on lab-specific implementations.

## Three Integrated Components

### 1. `canns` Python Library (BrainPy/JAX)
- Standardized 1D/2D CANN implementations
- Spike-frequency adaptation (SFA) variants
- Grid cell networks
- Hierarchical path integration models
- Brain-inspired attractor architectures
- Curated datasets and task generators
- Analyzer module for attractor geometry
- Trainer modules for biologically plausible plasticity

### 2. `canns-lib` Rust Backend
- Hundreds-of-times speedup for spatial navigation workloads
- Modest gains for Ripser-based persistent homology
- Production-grade performance for large-scale simulations

### 3. ASA (Attractor Structure Analyzer)
- PySide6 GUI pipeline
- Applies persistent homology and cohomology to experimental neural recordings
- Detects ring-like and toroidal attractor signatures in real data
- Bridges gap between spike trains and attractor geometry

## CANN Fundamentals

### What Are CANNs?
Continuous attractor neural networks are the canonical computational framework for how the brain encodes continuous variables:
- **Spatial position** → place cells (hippocampus)
- **Head direction** → head direction cells
- **Movement direction** → grid cells (entorhinal cortex)

### Key Properties
- Continuous family of stable states (attractor manifold)
- Neutral stability along the manifold
- Robust to perturbations perpendicular to manifold
- Support path integration through asymmetric connectivity

## Core Implementations

### 1D Ring Attractor (Head Direction)
```python
import canns
import brainpy as bp

# Standard 1D ring network
net = canns.RingAttractor(
    num_units=256,
    connectivity='gaussian',
    sigma=0.1,  # width of bump
    tau=10.0    # time constant
)

# Add spike-frequency adaptation
net.add_sfa(tau_sfa=100.0, alpha_sfa=0.1)

# Simulate with head direction input
runner = bp.DSRunner(net, inputs=[('input', head_dir_signal)])
runner.run(duration=5000.)
```

### 2D Toroidal Attractor (Grid Cells)
```python
# 2D grid cell network
net = canns.GridCellNetwork(
    grid_scale=30.0,  # cm
    grid_orientation=0.0,
    num_modules=3
)

# Hierarchical path integration
net.add_path_integration(
    velocity_input='running_velocity',
    gain=1.0
)
```

### Attractor Geometry Analysis
```python
from canns.analyzer import AttractorAnalyzer

analyzer = AttractorAnalyzer(network_activity)

# Compute persistent homology
persistence = analyzer.compute_persistence(dim=1)

# Detect ring-like structure
ring_score = analyzer.detect_ring_topology()

# Visualize attractor manifold
analyzer.plot_manifold_3d()
```

## Key Results Recovered

The toolkit ships with reproducible pipelines recovering recent CANN results:

### 1. SFA-Driven Anticipative Tracking
Spike-frequency adaptation enables anticipative shift of activity bump, matching experimental observations of look-ahead in place cells.

### 2. Theta Sweeps in Head Direction/Place/Grid Systems
SFA generates theta-frequency sweeps across the attractor manifold, reproducing experimental theta sequences.

### 3. Hierarchical Path Integration
Multi-scale grid modules with different spatial periods enable robust path integration over long distances.

## Usage Patterns

### When to Use `canns`
- Implementing new CANN variants
- Testing hypotheses about attractor dynamics
- Analyzing neural recordings for attractor signatures
- Teaching CANN concepts with working code
- Benchmarking new methods against established baselines

### Workflow Example
1. **Define network**: Choose 1D/2D, add SFA/plasticity
2. **Simulate**: Run with behavioral inputs (velocity, head direction)
3. **Analyze**: Compute attractor geometry, persistence diagrams
4. **Compare**: Match against experimental data or theoretical predictions

### Installation
```bash
pip install canns
# Rust backend (optional, for performance)
cargo install canns-lib
# ASA GUI (requires Qt)
pip install canns-asa
```

## Topological Data Analysis

### Persistent Homology for Attractors
- **H1 persistence**: Detects ring-like topology (1D attractors)
- **H2 persistence**: Detects toroidal topology (2D attractors)
- **Betti curves**: Track topological features across scales

### Practical Analysis
```python
from canns.analyzer import TopologicalAnalyzer

# Load neural activity (time x neurons)
activity = load_experiment_data()

# Compute pairwise correlations
corr_matrix = np.corrcoef(activity.T)

# Build filtration and compute persistence
analyzer = TopologicalAnalyzer(corr_matrix)
diagram = analyzer.compute_persistence(max_dim=2)

# Extract topological features
ring_persistence = diagram.get_persistence(dim=1)
torus_persistence = diagram.get_persistence(dim=2)

# Classify attractor type
if ring_persistence > threshold and torus_persistence < threshold:
    print("Ring attractor detected")
elif torus_persistence > threshold:
    print("Toroidal attractor detected")
```

## Integration with Experimental Data

### From Spike Trains to Attractor Geometry
1. Record neural activity (e.g., calcium imaging, electrophysiology)
2. Preprocess: bin spikes, compute firing rates
3. Build correlation matrix or use raw activity
4. Run ASA pipeline to detect attractor signatures
5. Validate with simulated data from `canns` library

### Case Studies
- **Mouse hippocampus**: Detect ring attractor in head direction cells
- **Rat entorhinal cortex**: Identify toroidal attractor in grid cells
- **Monkey PFC**: Analyze working memory as continuous attractor

## Performance Considerations

### Python vs Rust Backend
- **Python (BrainPy/JAX)**: Flexible, GPU acceleration, easy prototyping
- **Rust (canns-lib)**: 100-1000x faster for large spatial navigation simulations
- **Recommendation**: Use Python for development, Rust for production/large-scale

### Scaling
- Small networks (<1000 neurons): Python sufficient
- Medium networks (1000-10000 neurons): Consider Rust backend
- Large networks (>10000 neurons): Rust backend essential

## Limitations and Future Work

### Current Limitations
- Focus on rate-based CANNs (spiking CANNs under development)
- Limited plasticity rules (Hebbian, homeostatic)
- Single-brain-region models (multi-region integration planned)

### Roadmap
- Spiking CANN implementations
- Additional plasticity rules (STDP, meta-plasticity)
- Multi-region hierarchical CANNs
- Integration with large-scale brain simulators

## Activation Keywords

continuous attractor, CANN, grid cells, place cells, head direction cells, path integration, attractor geometry, persistent homology, BrainPy, JAX, neural recordings analysis, topological data analysis, ring attractor, toroidal attractor, spike-frequency adaptation, theta sweeps
