---
name: canns-toolkit-attractor-networks
description: Comprehensive open-source toolkit unifying continuous attractor neural network (CANN) research workflow. Three co-designed components (Python/Rust/GUI) for 1D/2D attractor modeling, spike-frequency adaptation, grid cells, path integration, and persistent homology-based attractor detection in neural recordings.
version: 1.0.0
tags: [neuroscience, continuous-attractor, grid-cells, place-cells, head-direction, path-integration, persistent-homology, topological-data-analysis, BrainPy, JAX, hippocampus, entorhinal-cortex]
arxiv: "2606.27783"
authors: ["Sichao He", "Aiersi Tuerhong", "Shangjun She", "Tianhao Chu", "Yuling Wu", "Junfeng Zuo", "Si Wu"]
institution: "Peking University"
published: "2026-06-30"
---

# CANNs: A Toolkit for Research on Continuous Attractor Neural Networks

## Core Methodology

### 1. What are Continuous Attractor Neural Networks (CANNs)?

**Canonical computational framework** for how the brain encodes continuous variables:
- **Spatial position** (hippocampal place cells)
- **Head direction** (head-direction cells)
- **Movement direction** (entorhinal grid cells)

**Key properties:**
- Recurrently connected population with localized "bump" of activity
- Bump smoothly translates along low-dimensional manifold
- Provides stability, noise robustness, and integration
- Manifold topology: ring (S¹) for 1D, torus (T²) for 2D

**Biological grounding:**
- Place cells (O'Keefe & Dostrovsky, 1971)
- Grid cells (Hafting et al., 2005)
- Head-direction cells (Taube et al., 1990)

### 2. Mathematical Core (Wu-Amari-Wong Model)

**Network architecture:**
- N neurons on 1D ring or 2D torus
- Translation-invariant recurrent connectivity (Gaussian kernel)
- Divisive normalization implements global inhibition
- Continuum of stable bump states parameterized by continuous variable

**Dynamics:**
```
τ du/dt = -u + ∫ J(u,v) r(v) dv + I_ext
r = [u]² / (1 + k ∫ [u]² du)  # divisive normalization
```

Where:
- u: internal state
- r: firing rate
- J: recurrent connectivity kernel (Gaussian)
- k: global inhibition strength
- I_ext: external input

**Energy landscape:**
```
E(r) = -1/2 r^T W r + I^T r
```

**Key behaviors:**
- Bump can be moved arbitrarily by localized input
- When input disappears, bump remains (short-term memory)
- Attractor structure provides built-in integrator

### 3. CANNs Toolkit Architecture

**Three co-designed components:**

#### A. canns (Python library on BrainPy/JAX)

**Modules:**
1. **Models** (`canns.models`): Neural network dynamics
   - 1D ring CANN (head-direction)
   - 2D torus CANN (place fields)
   - 2D grid-cell network (path integration)
   - Spike-frequency adaptation (SFA) variants
   - Theta-rhythmic modulation
   - Hierarchical path integration models
   - Brain-inspired attractor architectures

2. **Tasks** (`canns.task`): Experimental paradigms
   - Spatial navigation
   - Head-direction tracking
   - Grid cell firing field generation
   - Parametric working memory

3. **Analyzers** (`canns.analyzer`): Visualization and analysis
   - Energy landscape computation
   - Manifold extraction (PCA, UMAP)
   - Tuning curve fitting
   - Topological data analysis integration

4. **Trainers** (`canns.trainer`): Biologically plausible learning
   - Hebbian plasticity
   - STDP-like rules
   - Homeostatic mechanisms

5. **Pipeline** (`canns.pipeline`): Orchestration
   - Full workflow from simulation to analysis
   - Reproducible experiment scripts

#### B. canns-lib (Rust acceleration backend)

**Performance-critical operations:**
- Ripser-based persistent homology (hundreds-of-times speedup)
- Long spatial navigation trajectories
- Bulk task generation
- Python FFI for seamless integration

**Installation:**
```bash
pip install canns-lib  # hard dependency for canns
```

#### C. ASA (Attractor Structure Analyzer - PySide6 GUI)

**Purpose:** Detect attractor topology in experimental neural recordings

**Pipeline:**
1. Data ingestion (.npz format)
2. Preprocessing (spike/rate extraction)
3. Point cloud construction (time-indexed or spatially-indexed)
4. Persistent homology computation
5. Shuffle controls (statistical significance)
6. Persistent cohomology decoding (CohoMap/EcohoMap)
7. Circular coordinate extraction
8. Grid score computation
9. Module-level workflows
10. GUI + CLI interfaces

**Topological signatures:**
- **Ring (S¹):** One dominant H₁ barcode → head-direction cells, band cells, 1D CANN
- **Torus (T² = S¹×S¹):** Two stable H₁ features → grid-cell modules, 2D CANN

### 4. Advanced CANN Variants

#### A. Spike-Frequency Adaptation (SFA)

**Mechanism:** Activity-dependent negative feedback
- Turns static bump into moving wave
- Enables anticipative tracking
- Models theta sweeps and phase precession

**Implementation:**
```python
# SFA variable (adaptation current)
τ_a da/dt = -a + b * r

# Modified dynamics
τ du/dt = -u + ∫ J r dv - g_a * a + I_ext
```

Where:
- a: adaptation current
- b: adaptation strength
- g_a: adaptation conductance

#### B. Theta-Rhythmic Modulation

**Phenomena captured:**
- Theta sweeps (forward/backward)
- Phase precession
- Phase procession

**Implementation:**
```python
# Theta oscillation
theta(t) = sin(2π f_theta t + φ)

# Modulate network dynamics
I_mod = I_baseline + A_theta * theta(t)
```

#### C. Hierarchical Path Integration

**Architecture:** Multiple grid-cell modules with different spatial scales
- Coarse modules: large grid spacing
- Fine modules: small grid spacing
- Hierarchical combination → precise position coding

### 5. Topological Data Analysis (TDA) for Attractor Detection

**Persistent Homology:**
- Track topological features (connected components, loops, voids) across scales
- Barcode: persistence of features vs. scale parameter
- Stable features = true topology; transient = noise

**Application to neural data:**
```python
from ripser import ripser

# Population activity vectors
r(t) = [r₁(t), r₂(t), ..., rₙ(t)]^T ∈ ℝ^N

# Point cloud
X_t = {r(tⱼ) : j = 1, ..., T} ⊂ ℝ^N

# Compute persistent homology
result = ripser(X_t, maxdim=2)  # H₀, H₁, H₂
diagrams = result['dgms']

# Ring attractor: one dominant H₁ feature
ring_signature = len(diagrams[1]) > 0 and diagrams[1][0, 1] > threshold

# Torus attractor: two stable H₁ features
torus_signature = len(diagrams[1]) >= 2 and diagrams[1][1, 1] > threshold
```

**Persistent Cohomology Decoding:**
- Extract circular coordinates from cohomology generators
- Map high-dimensional activity to S¹ (ring) or T² (torus)
- Validate by alignment with behavioral variables

**CohoMap/EcohoMap:**
- Efficient cohomology computation
- Cache-aware result management
- Module-level workflows

**Shuffle controls:**
- Surrogate data with destroyed topology
- Statistical significance testing
- Distinguish true attractor from noise

### 6. Reproducible Research Pipelines

**Example: 1D Ring CANN (Head Direction)**

```python
from canns.models import CANN1D
from canns.task import HeadDirectionTracking
from canns.analyzer import EnergyLandscape, ManifoldAnalysis

# Initialize network
net = CANN1D(N=512, J0=1.0, a=0.5, k=0.1)

# Generate task
task = HeadDirectionTracking(n_directions=4, delay=500)

# Simulate
inputs = task.sample()
outputs, states = net.simulate(inputs, T=2000)

# Analyze
energy = EnergyLandscape(net.W)
energy.plot()

manifold = ManifoldAnalysis(states)
manifold.pca(n_components=3)
manifold.umap(n_neighbors=15)

# Verify ring attractor
from canns.analyzer import PersistentHomology
ph = PersistentHomology()
barcode = ph.compute(states)
assert ph.is_ring_attractor(barcode)
```

**Example: Real Neural Recording Analysis with ASA**

```python
from asa import AttractorStructureAnalyzer

# Load data (spike trains or rates)
data = asa.load('mec_grid_cells.npz')

# Preprocess
rates = asa.extract_rates(data, bin_size=50)

# Run ASA pipeline
asa_pipeline = AttractorStructureAnalyzer()
result = asa_pipeline.analyze(
    rates,
    method='persistent_cohomology',
    maxdim=2,
    shuffle_controls=100
)

# Interpret
if result.is_torus():
    print("Grid-cell module detected: toroidal topology")
    circular_coords = result.decode_circular_coordinates()
    grid_score = result.compute_grid_score(circular_coords)
elif result.is_ring():
    print("Head-direction or band-cell ring attractor")
    phase = result.decode_ring_phase()
```

### 7. Key Capabilities

**Reproduced studies:**
1. SFA-driven anticipative tracking
2. Theta sweeps in head-direction/place/grid systems
3. Hierarchical path integration
4. Real MEC grid-cell module analysis (heterogeneous topology)
5. Head-direction cell ring attractor detection

**Analysis tools:**
- GridScore: quantify hexagonal firing fields
- CohoScore: topological signature strength
- PathCompare: compare trajectories across conditions
- Module-level workflows for common analyses

### 8. Installation and Usage

```bash
# Install main library
pip install canns

# GUI (optional)
pip install canns[gui]

# ASA standalone
pip install asa-attractor-analyzer
```

**Quick start:**
```python
import canns

# Load pre-built model
net = canns.models.GridCellNetwork(module_id=1)

# Run spatial navigation
positions, firing_rates = net.simulate_navigation(
    trajectory='random_walk',
    duration=600  # seconds
)

# Analyze grid fields
from canns.analyzer import GridFieldAnalysis
gfa = GridFieldAnalysis()
grid_score = gfa.compute_score(firing_rates, positions)
gfa.plot_firing_fields(firing_rates, positions)
```

## Key Insights

### 1. Unification of CANN Research

**Problem:** CANN research fragmented across:
- Lab-specific implementations
- General-purpose simulators (NEURON, BRIAN) lack CANN-specific abstractions
- No standardized path from spike trains to attractor geometry

**Solution:** Unified toolkit covering:
- Modeling (canns)
- Acceleration (canns-lib)
- Experimental analysis (ASA)
- Reproducible pipelines

### 2. Topological Signatures as Biomarkers

**Finding:** Real MEC grid-cell modules show heterogeneous topology
- Some modules: clear toroidal signature
- Others: partial or unstable topology
- Suggests: not all grid-cell modules are perfect CANNs

**Implication:** Persistent homology provides quantitative biomarker for:
- Attractor quality (how "perfect" is the CANN?)
- Disease states (does Alzheimer's degrade toroidal topology?)
- Development (how does topology emerge during learning?)

### 3. Rust Acceleration Matters

**Performance gains:**
- Persistent homology: 100-1000× speedup
- Spatial navigation: efficient long trajectories
- Enables: real-time analysis of large datasets

**Why Rust?**
- Memory safety without garbage collection
- Zero-cost abstractions
- Seamless Python FFI

### 4. Separation of Concerns

**Design principle:**
- Models: define dynamics
- Tasks: generate inputs
- Analyzers: visualize/analyze (no state modification)
- Trainers: update parameters
- Pipeline: orchestrate

**Benefit:** Modular, extensible, reproducible

## Experimental Validation

### Predictions for Empirical Testing

1. **Topology heterogeneity:** Different grid-cell modules should show varying topological "perfection" (testable with large-scale MEC recordings)

2. **Disease biomarkers:** Neurodegenerative diseases should degrade toroidal topology (Alzheimer's → entorhinal cortex degradation)

3. **Development trajectory:** Toroidal topology should emerge during learning (young animals → less stable topology)

4. **SFA signature:** Theta sweeps and phase precession should correlate with SFA strength (testable via pharmacological manipulation)

## Limitations

- Rate-based models (most implementations) → cannot capture spike timing
- Assumes translation-invariant connectivity → biological networks have variability
- Persistent homology computationally expensive for very large populations (>10,000 neurons)
- No direct spike-train analysis (requires rate conversion)

## Extensions

1. **Spiking CANNs:** Implement leaky integrate-and-fire or adaptive exponential integrate-and-fire neurons
2. **Learning rules:** Add biologically plausible synaptic plasticity (STDP, homeostatic)
3. **Multi-region models:** Connect hippocampus, entorhinal cortex, head-direction circuits
4. **Behavioral coupling:** Link attractor dynamics to decision-making and navigation behavior
5. **GPU acceleration:** JAX backend already supports GPU; extend Rust backend for CUDA

## References

- arXiv:2606.27783 - Original paper
- Amari (1977a) - Lateral-inhibition neural fields
- Wu et al. (2008, 2016) - Analytically solvable CANN model
- Gardner et al. (2022) - Toroidal population geometry in grid cells
- Mi et al. (2014) - Spike-frequency adaptation in CANNs
- Chu et al. (2024, 2025) - Theta rhythms and hierarchical path integration

## Activation Keywords

continuous attractor neural network, CANN, grid cells, place cells, head-direction cells, path integration, persistent homology, topological data analysis, BrainPy, JAX, hippocampus, entorhinal cortex, spatial navigation, ring attractor, torus attractor, spike-frequency adaptation, theta sweeps, phase precession, manifold learning, neural manifold, attractor analysis, ASA toolkit
