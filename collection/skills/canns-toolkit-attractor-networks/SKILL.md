---
name: canns-toolkit-attractor-networks
description: "CANNs toolkit for continuous attractor neural network research - unified Python/Rust/PySide6 framework for modeling spatial navigation, grid cells, head-direction cells, and attractor dynamics analysis. Activation: CANNs toolkit, continuous attractor neural networks, BrainPy JAX, grid cell simulation, head-direction cells, place cells, path integration, persistent homology attractor, Rust neural simulation, PySide6 neuroscience, anticipative tracking, theta sweep"
metadata:
  arxiv_id: "2606.27783"
  authors: ["Sichao He", "Aiersi Tuerhong", "Shangjun She", "Tianhao Chu", "Yuling Wu", "Junfeng Zuo", "Si Wu"]
  published: "2026-06-26"
  tags: ["continuous attractor neural networks", "BrainPy", "JAX", "Rust acceleration", "PySide6", "persistent homology", "grid cells", "place cells", "head-direction cells", "path integration", "spatial navigation"]
---

# CANNs Toolkit: Continuous Attractor Neural Networks

Comprehensive open-source toolkit for continuous attractor neural network (CANN) research, integrating simulation, acceleration, and analysis in a unified workflow.

## Overview

CANNs are the canonical computational framework for how the brain encodes continuous variables (spatial position, head direction, movement direction) and explain hippocampal place cells, entorhinal grid cells, and head-direction cells. This toolkit addresses fragmentation in CANN research by providing standardized implementations, acceleration, and analysis tools.

## Core Components

### 1. canns (Python Library)

Built on BrainPy/JAX framework, provides:

- **Standardized CANNs**: 1D and 2D continuous attractor networks
- **Spike-frequency adaptation (SFA) variants**: For anticipative tracking
- **Grid cell networks**: Hexagonal pattern formation and maintenance
- **Hierarchical path integration models**: Multi-scale spatial navigation
- **Brain-inspired attractor architectures**: Biologically plausible implementations
- **Curated datasets**: Standard benchmarks for CANN evaluation
- **Task generators**: Spatial navigation and memory tasks
- **Analyzer module**: Attractor geometry and dynamics analysis
- **Trainer modules**: Biologically plausible plasticity rules (STDP, Hebbian, homeostatic)

**Key features**:
- GPU acceleration via JAX
- Differentiable programming for gradient-based optimization
- Integration with Brain ecosystem (BrainPy, BrainState, BrainUnit)

### 2. canns-lib (Rust Backend)

High-performance acceleration layer:

- **Spatial navigation workloads**: Hundreds-of-times speedups over pure Python
- **Persistent homology computation**: Modest gains for Ripser-based topological analysis
- **Memory-efficient implementations**: Optimized data structures for large-scale simulations
- **Parallel computation**: Multi-threaded attractor dynamics

**Use cases**:
- Large-scale grid cell network simulations (>10,000 neurons)
- Long-timescale path integration (hours of simulated time)
- Topological analysis of attractor manifolds

### 3. ASA (Attractor Structure Analyzer)

PySide6-based GUI pipeline for experimental data analysis:

- **Persistent homology**: Detect ring-like and toroidal attractor signatures
- **Cohomology analysis**: Higher-order topological features
- **Spike train processing**: Convert experimental recordings to attractor geometry
- **Interactive visualization**: 3D attractor manifold exploration
- **Export capabilities**: Publication-ready figures and data

**Workflow**:
1. Load spike train data (NWBI, HDF5, or custom formats)
2. Preprocess (binning, smoothing, rate estimation)
3. Compute topological features (persistence diagrams, barcodes)
4. Identify attractor type (ring, torus, sphere, etc.)
5. Visualize and export results

## Key Methodologies

### Spike-Frequency Adaptation (SFA)

SFA enables anticipative tracking - the network predicts future states rather than representing current states. Critical for:
- Moving object tracking
- Smooth pursuit eye movements
- Path integration with velocity input

**Implementation**: Adaptation current with timescale τ_adapt ~ 100-500ms

### Theta Sweep Dynamics

Theta oscillations (4-10 Hz) modulate attractor dynamics:
- **Head-direction cells**: Theta-phase precession
- **Place cells**: Forward sweep of place field sequences
- **Grid cells**: Theta-rhythmic grid pattern updates

**Modeling approach**: Oscillatory input modulating synaptic weights or external drive

### Hierarchical Path Integration

Multi-scale integration from local cues to global map:
- **Local**: Velocity integration (dead reckoning)
- **Intermediate**: Landmark-based correction
- **Global**: Map alignment and drift correction

**Architecture**: Stacked CANNs with different spatial scales and update rules

### Persistent Homology for Attractor Detection

Topological data analysis to identify attractor manifold structure:

1. **Point cloud construction**: Embed neural activity in state space
2. **Filtration**: Build simplicial complex at multiple scales
3. **Persistence computation**: Track topological features across scales
4. **Barcode interpretation**: 
   - Long bars = stable topological features
   - Ring attractor: 1 persistent H1 feature
   - Torus attractor: 2 persistent H1 features + 1 H2 feature

**Tools**: Ripser (C++ backend), Gudhi (Python wrapper)

## Installation

```bash
# Install canns Python library
pip install canns

# Install Rust backend (optional, for acceleration)
pip install canns-lib

# Install ASA GUI
pip install canns-asa
# Or download standalone binary from releases
```

**Dependencies**:
- Python 3.8+
- JAX 0.4+ (with GPU support recommended)
- BrainPy 2.0+
- PySide6 (for ASA GUI)
- Rust toolchain (for canns-lib compilation)

## Usage Examples

### Basic 1D Ring Attractor

```python
import canns
from canns.models import RingAttractor
from canns.tasks import HeadDirectionTask

# Create network
net = RingAttractor(
    n_neurons=256,
    connectivity='mexican_hat',
    adaptation=True
)

# Create task
task = HeadDirectionTask(
    duration=10000,  # ms
    angular_velocity=10  # deg/s
)

# Run simulation
activity = net.simulate(task.inputs)

# Analyze
analyzer = canns.Analyzer(activity)
analyzer.plot_attractor_manifold()
analyzer.compute_persistence_diagram()
```

### Grid Cell Network with Rust Acceleration

```python
from canns.models import GridCellNetwork
from cannsLib import accelerate

# Create grid cell network
net = GridCellNetwork(
    grid_scales=[0.3, 0.5, 0.8],  # meters
    grid_orientations=[0, 60, 120],  # degrees
    n_neurons_per_module=1000
)

# Accelerate with Rust backend
fast_net = accelerate(net)

# Simulate spatial navigation
trajectory = canns.tasks.RandomWalk2D(duration=60000)
activity = fast_net.simulate(trajectory.positions)

# Analyze grid patterns
analyzer = canns.GridAnalyzer(activity)
grid_scores = analyzer.compute_gridness_scores()
```

### Experimental Data Analysis with ASA

```python
from canns.asa import AttractorStructureAnalyzer

# Load experimental data
data = canns.load('neural_recording.nwb')

# Initialize analyzer
asa = AttractorStructureAnalyzer()

# Preprocess
rates = asa.estimate_firing_rates(data.spike_trains, bin_size=50)

# Compute topology
persistence = asa.compute_persistent_homology(
    rates, 
    max_dimension=2,
    filtration='rips'
)

# Identify attractor type
attractor_type = asa.classify_attractor(persistence)
print(f"Detected: {attractor_type}")  # "Ring attractor" or "Torus attractor"

# Visualize
asa.plot_persistence_diagram(persistence)
asa.plot_3d_manifold(rates)
```

## Reproducible Pipelines

The toolkit ships with complete pipelines reproducing recent CANN results:

### SFA-Driven Anticipative Tracking

```bash
python -m canns.pipelines.sfa_tracking \
    --config configs/anticipative_tracking.yaml \
    --output results/sfa_tracking/
```

**Recovers**: Anticipative head-direction cell responses with ~100ms lookahead

### Theta Sweeps in HD/Place/Grid Systems

```bash
python -m canns.pipelines.theta_sweeps \
    --system place_cells \
    --theta_freq 8.0 \
    --output results/theta_sweeps/
```

**Recovers**: Forward sweep of place field sequences during theta cycles

### Hierarchical Path Integration

```bash
python -m canns.pipelines.hierarchical_pi \
    --n_scales 3 \
    --landmark_correction True \
    --output results/hierarchical_pi/
```

**Recovers**: Drift-resistant path integration with landmark anchoring

## Advanced Topics

### Custom Plasticity Rules

```python
from canns.plasticity import STDP, HomeostaticScaling

# Combine multiple plasticity mechanisms
plasticity = [
    STDP(tau_plus=20, tau_minus=20, A_plus=0.01, A_minus=0.012),
    HomeostaticScaling(target_rate=5.0, timescale=1000)
]

net = RingAttractor(plasticity_rules=plasticity)
```

### Multi-Scale attractor Networks

```python
from canns.models import HierarchicalAttractor

# Stack attractors with different spatial scales
hierarchy = HierarchicalAttractor([
    {'scale': 'local', 'n_neurons': 100, 'update_rate': 100},
    {'scale': 'medium', 'n_neurons': 50, 'update_rate': 20},
    {'scale': 'global', 'n_neurons': 20, 'update_rate': 5}
])
```

### GPU-Accelerated Training

```python
import jax
from canns.training import train_attractor

# Define loss (e.g., match experimental firing patterns)
def loss_fn(params, inputs, targets):
    activity = net.apply(params, inputs)
    return jax.numpy.mean((activity - targets)**2)

# Train with gradient descent
trained_params = train_attractor(
    net, loss_fn, 
    optimizer='adam', 
    learning_rate=1e-3,
    n_epochs=1000
)
```

## Pitfalls

- **JAX compilation time**: First call to JAX functions triggers compilation (10-60s). Subsequent calls are fast. Use `jax.jit` to cache compiled functions.

- **Rust backend requires toolchain**: `canns-lib` installation requires Rust compiler. Install via `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`

- **Memory usage**: Large CANNs (>10k neurons) require significant GPU memory. Use `canns-lib` acceleration to reduce memory footprint.

- **Persistent homology scaling**: Ripser computation is O(n²) in number of points. Subsample neural activity if >1000 timepoints.

- **Theta phase interpretation**: Theta-phase precession depends on reference frame. Ensure consistent alignment across neurons before analysis.

- **Grid cell orientation ambiguity**: Grid orientation is defined up to 60° rotation. Use landmark cues to disambiguate.

## Related Skills

- `spiking-neural-network-analysis` - SNN analysis methods
- `brain-network-connectivity` - Brain network analysis
- `computational-neuroscience-methods` - General computational neuroscience

## Resources

- **GitHub**: https://github.com/brainpy/canns
- **Documentation**: https://canns.readthedocs.io
- **Rust backend**: https://github.com/brainpy/canns-lib
- **Paper**: arXiv:2606.27783

## Citation

```bibtex
@article{he2026canns,
  title={CANNs: A Toolkit for Research on Continuous Attractor Neural Networks},
  author={He, Sichao and Tuerhong, Aiersi and She, Shangjun and Chu, Tianhao and Wu, Yuling and Zuo, Junfeng and Wu, Si},
  journal={arXiv preprint arXiv:2606.27783},
  year={2026}
}
```
