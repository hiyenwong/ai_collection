---
name: canns-toolkit-attractor-networks
description: "Comprehensive open-source toolkit unifying CANN research workflow with BrainPy/JAX, Rust acceleration, and topological analysis. Use when working with continuous attractor neural networks for spatial coding, head direction, grid cells, or any continuous variable encoding in neural circuits."
---

## CANNs Toolkit for Continuous Attractor Neural Networks

### Description

Continuous attractor neural networks (CANNs) are the canonical computational framework for how the brain encodes continuous variables (spatial position, head direction, movement direction). This skill provides methodology from the unified CANNs toolkit that bridges fragmented lab-specific implementations into a general-purpose research framework with BrainPy/JAX integration, Rust-accelerated simulation, and topological analysis of attractor manifolds.

### Activation Keywords
- CANN
- continuous attractor neural network
- 连续吸引子网络
- head direction cell
- grid cell simulation
- spatial coding neural network
- attractor manifold
- bump attractor
- 吸引子网络
- place cell simulation
- CANNs toolkit

### Core Concepts

#### 1. Attractor Manifold Theory
CANNs maintain stable activity patterns (bumps) that can be continuously translated across the network through external input or internal dynamics. The attractor manifold is a low-dimensional subspace where network activity evolves — typically a ring (head direction), torus (grid cells), or line (1D position).

#### 2. Key CANN Variants
- **Ring CANN**: Encodes angular variables (head direction, orientation)
- **Torus CANN**: Encodes 2D periodic variables (grid cell phase)
- **Line CANN**: Encodes 1D continuous variables (spatial position)
- **Spherical CANN**: Encodes variables on spherical manifolds

#### 3. Toolkit Architecture
The unified CANNs toolkit provides:
- **BrainPy/JAX backend**: GPU-accelerated simulation with automatic differentiation
- **Rust-accelerated core**: High-performance CPU simulation for large networks
- **Topological analysis**: Persistent homology and manifold learning for attractor structure verification
- **Spike-to-attractor pipeline**: Converting spike trains to attractor geometry visualization

### Usage Patterns

#### Pattern 1: Building a Ring CANN for Head Direction

```python
import brainpy as bp
import brainpy.math as bm
import numpy as np

class RingCANN(bp.DynamicalSystem):
    def __init__(self, num_neurons=256, sigma=0.1, tau=10.0):
        super().__init__()
        self.num = num_neurons
        self.sigma = sigma  # Connection width
        self.tau = tau      # Time constant
        
        # Initialize activity
        self.r = bp.Variable(bm.zeros(num_neurons))
        
        # Precompute weight matrix (Mexican hat)
        theta = bm.linspace(0, 2*np.pi, num_neurons, endpoint=False)
        dist = bm.abs(theta[:, None] - theta[None, :])
        dist = bm.minimum(dist, 2*np.pi - dist)
        self.W = bm.exp(-dist**2 / (2*sigma**2)) * 2 - 1.0
        
    def update(self, t, dt, external_input=0.0):
        # Recurrent input
        recurrent = bm.dot(self.W, self.r) / self.num
        # Update dynamics
        dr = (-self.r + recurrent + external_input) / self.tau
        self.r.value += dt * dr
        
cann = RingCANN(num_neurons=256, sigma=0.1)
```

#### Pattern 2: Topological Analysis of Attractor Structure

```python
from gudhi import ripser
from sklearn.manifold import MDS

def analyze_attractor_topology(spike_trains, max_dim=2):
    """Extract topological features of CANN attractor manifold.
    
    Args:
        spike_trains: (T, N) spike count matrix
        max_dim: Maximum homology dimension to compute
    
    Returns:
        persistence_diagrams: List of (birth, death) pairs per dimension
    """
    # Embed spike trains into low-dimensional space
    mds = MDS(n_components=3, dissimilarity='precomputed')
    dist_matrix = np.linalg.norm(spike_trains[:, None, :] - spike_trains[None, :, :], axis=2)
    embedding = mds.fit_transform(dist_matrix)
    
    # Compute persistent homology
    rips = ripser.RipsComplex(points=embedding, max_edge_length=1.0)
    simplex_tree = rips.create_simplex_tree(max_dimension=max_dim)
    simplex_tree.persistence()
    
    diagrams = simplex_tree.persistence_intervals_in_dimension()
    return diagrams
```

#### Pattern 3: Input-Driven Bump Translation

```python
def drive_cann_with_input(cann, input_profile, duration=1000, dt=0.1):
    """Drive CANN with external input to move bump attractor.
    
    Args:
        cann: CANN instance
        input_profile: Function of (position, time) returning input vector
        duration: Simulation duration (ms)
        dt: Time step (ms)
    """
    num_steps = int(duration / dt)
    positions = np.linspace(0, 2*np.pi, cann.num)
    
    trajectory = []
    for step in range(num_steps):
        t = step * dt
        inp = input_profile(positions, t)
        cann.update(t, dt, external_input=inp)
        trajectory.append(cann.r.value.copy())
    
    return np.array(trajectory)
```

### Implementation Steps

1. **Define network architecture**: Choose CANN variant (ring/torus/line) based on encoded variable
2. **Set connectivity**: Mexican-hat (local excitation, global inhibition) or difference-of-Gaussians
3. **Initialize activity**: Random or targeted bump initialization
4. **Simulate dynamics**: Run with BrainPy/JAX or Rust backend
5. **Analyze attractor**: 
   - Track bump position over time
   - Compute persistent homology for topological validation
   - Measure drift velocity and diffusion constant
6. **Add input**: External drive for position encoding or velocity control
7. **Validate**: Compare to biological data (place cells, grid cells, HD cells)

### Error Handling

#### Bump Collapse
If the attractor bump collapses (uniform activity):
- Increase local excitation strength
- Decrease global inhibition
- Check connectivity normalization (sum of weights should preserve bump)

#### Drift Without Input
If the bump drifts without external input:
- Ensure translational symmetry in weight matrix
- Check boundary conditions (periodic vs open)
- Verify no bias in initial conditions

#### GPU Memory Issues
For large CANNs on GPU:
- Use sparse connectivity matrices
- Batch spike train analysis
- Consider Rust backend for CPU-based simulation

### Pitfalls

1. **Weight matrix symmetry**: Mexican-hat weights must be symmetric for stable bumps. Asymmetric weights cause systematic drift.
2. **Finite-size effects**: Small networks (< 64 neurons) show significant discretization artifacts. Use > 128 neurons for smooth attractor manifolds.
3. **Input scaling**: External input must be carefully scaled — too weak and the bump doesn't move, too strong and it fragments.
4. **Topology validation**: Always verify attractor topology (ring vs line) via persistent homology before drawing conclusions about encoding properties.
5. **Cross-lab reproducibility**: The toolkit addresses fragmentation — use standardized parameter ranges: sigma ∈ [0.05, 0.2], tau ∈ [5, 20]ms for biological plausibility.

### Resources
- CANNs toolkit: unified framework for attractor network research
- BrainPy: JAX-based neural simulation framework
- GUDHI: Topological data analysis library
- Persistent homology: For attractor manifold verification
