---
name: energy-based-neurocomputation
description: >
  Energy-based dynamical systems framework for neurocomputation, learning, and optimization.
  Unifies Hopfield networks, Boltzmann machines, modern EBMs, and equilibrium propagation
  under a single energy landscape formulation. Covers gradient flow dynamics, attractor
  analysis, contrastive learning, and biologically-plausible learning rules.
  Activation: energy-based models, EBMs, neural dynamics, Hopfield networks, energy landscape,
  attractor dynamics, gradient flow, equilibrium propagation, contrastive learning,
  Lyapunov stability, 能量模型, 能量景观, 神经动力学, 吸引子动力学, 梯度流
version: 2.0.0
metadata:
  hermes:
    source_paper: "Energy-Based Dynamical Models for Neurocomputation, Learning, and Optimization"
    arxiv_id: "2604.05042"
    authors: [Montanari, Bullo, Krotov, Motter]
    categories: [cs.LG, cond-mat.dis-nn, eess.SY, math.DS, q-bio.NC]
    tags: [energy-based-models, neurocomputation, dynamical-systems, hopfield, EBM, attractor, learning]
---

# Energy-Based Dynamical Models for Neurocomputation

Energy-based dynamical systems framework bridging control theory, neuroscience, and machine learning for scalable, robust, energy-efficient computation through energy landscape formulation.

## 1. Energy Landscape Formulation of Neural Dynamics

### 1.1 Core Energy Function

Neural activity evolves to minimize a scalar energy function $E(x)$:

```
E(x) = -½ xᵀ W x - bᵀ x + R(x)
```

| Component | Description |
|-----------|-------------|
| $x \in \mathbb{R}^N$ | Neural activity state vector |
| $W \in \mathbb{R}^{N\times N}$ | Synaptic weight matrix (symmetric for guaranteed convergence) |
| $b \in \mathbb{R}^N$ | External input / bias vector |
| $R(x)$ | Regularization (sparsity, bounds, non-convexity) |

### 1.2 Continuous-Time Dynamics

The neural state evolves according to gradient flow on the energy landscape:

```
τ · dx/dt = -∇ₓE(x) = W·x + b - ∇ₓR(x)
```

With saturating nonlinearity:

```
τ · dx/dt = -x + φ(W·x + b)
```

where $φ(\cdot)$ is a sigmoidal activation (tanh, sigmoid, or softplus).

### 1.3 Discrete-Time Update

```
x(t+1) = φ(W·x(t) + b)
```

### 1.4 Key Properties

- **Monotonicity**: $dE/dt \leq 0$ when $W$ is symmetric
- **Boundedness**: Activation functions constrain state space
- **Convergence**: System reaches fixed points (attractors)
- **Lyapunov Function**: $E(x)$ serves as a Lyapunov function for the dynamics

## 2. Connection: Hopfield Networks ↔ Modern EBMs

### 2.1 Classical Hopfield Networks (1982)

```python
class ClassicalHopfield:
    """Discrete Hopfield network - binary ±1 units."""
    
    def __init__(self, n_units: int):
        self.W = np.zeros((n_units, n_units))  # Symmetric, zero diagonal
        
    def store_patterns(self, patterns: np.ndarray):
        """Hebbian storage: W = (1/N) Σ ξ ξᵀ"""
        n = patterns.shape[1]
        for p in patterns:
            self.W += np.outer(p, p) / n
        np.fill_diagonal(self.W, 0)
    
    def energy(self, state: np.ndarray) -> float:
        """Hopfield energy: E = -½ Σᵢⱼ Wᵢⱼ sᵢ sⱼ"""
        return -0.5 * state @ self.W @ state
    
    def update(self, state: np.ndarray) -> np.ndarray:
        """Asynchronous update: sᵢ ← sign(Σⱼ Wᵢⱼ sⱼ)"""
        new_state = state.copy()
        i = np.random.randint(len(state))
        local_field = self.W[i] @ state
        new_state[i] = np.sign(local_field) if local_field != 0 else state[i]
        return new_state
    
    def recall(self, cue: np.ndarray, max_iter: int = 100) -> np.ndarray:
        """Pattern completion from partial cue."""
        state = cue.copy()
        for _ in range(max_iter):
            new_state = self.update(state)
            if np.array_equal(state, new_state):
                break
            state = new_state
        return state
```

### 2.2 Modern Energy-Based Models

Modern EBMs generalize Hopfield networks by:

| Feature | Classical Hopfield | Modern EBM |
|---------|-------------------|------------|
| State space | Discrete {±1} | Continuous ℝᴺ |
| Energy | Quadratic only | Arbitrary parametric E_θ(x) |
| Learning | Hebbian rule | Contrastive divergence, score matching |
| Inference | Async updates | Langevin dynamics, MCMC |
| Capacity | ~0.14N patterns | Scales with network depth |
| Architecture | Single layer | Deep, multi-layer |

### 2.3 Modern Hopfield Networks (Dense Associative Memory)

```python
class ModernHopfield:
    """Dense associative memory with exponential energy.
    
    Energy: E(x) = -lse(β Xᵀ x) + ½‖x‖²
    where lse is the log-sum-exp function.
    """
    
    def __init__(self, n_features: int, beta: float = 1.0):
        self.beta = beta  # Inverse temperature
        self.memories = []
        
    def store(self, pattern: np.ndarray):
        """Add pattern to memory set."""
        self.memories.append(pattern)
        
    def energy(self, query: np.ndarray) -> float:
        """Modern Hopfield energy function."""
        M = np.array(self.memories)
        # E(x) = -lse(β M x) + ½‖x‖²
        logits = self.beta * M @ query
        lse_val = np.log(np.sum(np.exp(logits)))
        return -lse_val + 0.5 * np.dot(query, query)
    
    def retrieve(self, query: np.ndarray, n_steps: int = 10) -> np.ndarray:
        """Energy minimization via gradient descent."""
        x = query.copy()
        for _ in range(n_steps):
            # ∇E = -Mᵀ softmax(β M x) + x
            logits = self.beta * np.array(self.memories) @ x
            probs = np.exp(logits) / np.sum(np.exp(logits))
            grad = -np.array(self.memories).T @ probs + x
            x = x - 0.1 * grad  # Gradient step
        return x
```

### 2.4 Unified View

```
Classical Hopfield → Continuous Hopfield → Modern Hopfield → Deep EBM
     (1982)              (1984)              (2016)          (2020+)
   Binary ±1         Continuous          Dense assoc.     Parametric
   Quadratic E       Quadratic E         LogSumExp E       Neural net E
   Hebbian W         Gradient flow       Gradient flow     Score matching
```

## 3. Gradient Flow Dynamics

### 3.1 Formal Gradient Flow System

The continuous neural dynamics implement a Riemannian gradient flow:

```
τ · dx/dt = -G(x)⁻¹ ∇ₓE(x)
```

where $G(x)$ is a metric tensor (often identity for Euclidean gradient flow).

### 3.2 Gradient Flow with Nonlinearity

```python
class GradientFlowDynamics:
    """Gradient flow dynamics on energy landscape."""
    
    def __init__(self, W: np.ndarray, b: np.ndarray, tau: float = 1.0):
        self.W = W
        self.b = b
        self.tau = tau
        
    def energy(self, x: np.ndarray) -> float:
        """Energy with integral-of-nonlinearity term."""
        # E(x) = -½ xᵀ W x - bᵀ x + Σᵢ ∫₀^{xᵢ} φ⁻¹(s) ds
        quad = -0.5 * x @ self.W @ x
        linear = -self.b @ x
        # For tanh activation: ∫ tanh⁻¹(s) ds = ½[(1+s)ln(1+s) + (1-s)ln(1-s)]
        reg = 0.5 * np.sum((1+x)*np.log1p(x) + (1-x)*np.log1p(-x))
        return quad + linear + reg
    
    def vector_field(self, x: np.ndarray) -> np.ndarray:
        """Compute dx/dt = (-x + φ(Wx + b)) / τ"""
        return (-x + np.tanh(self.W @ x + self.b)) / self.tau
    
    def simulate(self, x0: np.ndarray, T: float, dt: float = 0.01) -> tuple:
        """Forward Euler integration."""
        t = np.arange(0, T, dt)
        x = x0.copy()
        trajectory = [x.copy()]
        energy_trace = [self.energy(x)]
        
        for _ in t:
            dx = self.vector_field(x) * dt
            x = x + dx
            trajectory.append(x.copy())
            energy_trace.append(self.energy(x))
            
        return np.array(trajectory), np.array(energy_trace)
    
    def check_convergence(self, trajectory: np.ndarray, tol: float = 1e-6) -> bool:
        """Check if trajectory has converged to fixed point."""
        velocities = np.diff(trajectory, axis=0)
        return np.all(np.linalg.norm(velocities[-10:], axis=1) < tol)
```

### 3.3 Energy Decay Guarantee

For symmetric $W$ and monotone activation $φ$:

```python
def verify_energy_decay(dynamics, x0, T, dt=0.01):
    """Verify that energy decreases monotonically along trajectory."""
    traj, energy = dynamics.simulate(x0, T, dt)
    
    # Energy should be non-increasing
    violations = np.sum(np.diff(energy) > 1e-10)
    is_valid = violations == 0
    
    return {
        'energy_initial': energy[0],
        'energy_final': energy[-1],
        'energy_drop': energy[0] - energy[-1],
        'monotonic': is_valid,
        'violations': violations
    }
```

## 4. Attractor Landscape Analysis

### 4.1 Attractor Classification

| Type | Description | Memory Analogy |
|------|-------------|----------------|
| **Point attractor** | Isolated fixed point | Discrete memory item |
| **Line attractor** | 1D manifold of fixed points | Continuous variable (evidence) |
| **Ring attractor** | Circular manifold | Circular variable (heading) |
| **Chaotic attractor** | Strange attractor | Oscillatory/complex dynamics |
| **Limit cycle** | Closed periodic orbit | Rhythmic pattern |

### 4.2 Landscape Analysis Pipeline

```python
class AttractorLandscapeAnalyzer:
    """Comprehensive attractor landscape analysis."""
    
    def __init__(self, dynamics_model):
        self.model = dynamics_model
        self.fixed_points = []
        self.basins = {}
        
    def find_fixed_points(self, n_initial: int = 100, tol: float = 1e-6, 
                          max_iter: int = 500) -> np.ndarray:
        """Find attractors via multiple initial conditions."""
        attractors = []
        dim = self.model.W.shape[0]
        
        for _ in range(n_initial):
            x0 = np.random.randn(dim) * 0.5
            x = x0.copy()
            
            for _ in range(max_iter):
                dx = self.model.vector_field(x)
                x = x + 0.1 * dx
                if np.linalg.norm(dx) < tol:
                    break
            
            # Check if novel attractor
            is_novel = True
            for existing in attractors:
                if np.linalg.norm(x - existing) < tol * 10:
                    is_novel = False
                    break
            
            if is_novel:
                attractors.append(x)
        
        self.fixed_points = attractors
        return np.array(attractors)
    
    def classify_stability(self, fixed_point: np.ndarray, eps: float = 1e-5) -> dict:
        """Classify stability via Jacobian eigenvalues."""
        n = len(fixed_point)
        J = np.zeros((n, n))
        
        # Numerical Jacobian
        for i in range(n):
            x_plus = fixed_point.copy()
            x_plus[i] += eps
            x_minus = fixed_point.copy()
            x_minus[i] -= eps
            
            v_plus = self.model.vector_field(x_plus)
            v_minus = self.model.vector_field(x_minus)
            J[:, i] = (v_plus - v_minus) / (2 * eps)
        
        eigenvalues = np.linalg.eigvals(J)
        
        # Classification
        real_parts = np.real(eigenvalues)
        if np.all(real_parts < 0):
            stability = 'stable'  # Attractor
        elif np.any(real_parts > 0):
            if np.all(real_parts > 0):
                stability = 'repeller'  # Source
            else:
                stability = 'saddle'
        else:
            stability = 'center'  # Marginally stable
        
        return {
            'eigenvalues': eigenvalues,
            'stability': stability,
            'max_real_part': np.max(real_parts),
            'min_real_part': np.min(real_parts),
            'spectral_radius': np.max(np.abs(eigenvalues))
        }
    
    def map_basins(self, grid_size: int = 50, bounds: tuple = None) -> dict:
        """Map basin of attraction for each attractor."""
        n = self.model.W.shape[0]
        if bounds is None:
            bounds = (-2.0, 2.0)
        
        if n == 2:
            # Full 2D basin mapping
            x1 = np.linspace(bounds[0], bounds[1], grid_size)
            x2 = np.linspace(bounds[0], bounds[1], grid_size)
            X1, X2 = np.meshgrid(x1, x2)
            
            basin_map = np.zeros((grid_size, grid_size), dtype=int)
            
            for i in range(grid_size):
                for j in range(grid_size):
                    x0 = np.array([X1[i,j], X2[i,j]])
                    x_final = self._flow_to_attractor(x0)
                    basin_map[i,j] = self._nearest_attractor_idx(x_final)
            
            return {'map': basin_map, 'grid': (x1, x2)}
        else:
            # Monte Carlo basin estimation
            n_samples = 1000
            counts = np.zeros(len(self.fixed_points))
            
            for _ in range(n_samples):
                x0 = np.random.uniform(bounds[0], bounds[1], n)
                x_final = self._flow_to_attractor(x0)
                idx = self._nearest_attractor_idx(x_final)
                counts[idx] += 1
            
            return {'counts': counts, 'fractions': counts / n_samples}
    
    def _flow_to_attractor(self, x0: np.ndarray, max_iter: int = 500) -> np.ndarray:
        x = x0.copy()
        for _ in range(max_iter):
            dx = self.model.vector_field(x)
            x = x + 0.1 * dx
            if np.linalg.norm(dx) < 1e-6:
                break
        return x
    
    def _nearest_attractor_idx(self, point: np.ndarray) -> int:
        if not self.fixed_points:
            return -1
        dists = [np.linalg.norm(point - fp) for fp in self.fixed_points]
        return np.argmin(dists)
    
    def compute_landscape_metrics(self) -> dict:
        """Compute quantitative landscape descriptors."""
        if not self.fixed_points:
            self.find_fixed_points()
        
        stabilities = [self.classify_stability(fp) for fp in self.fixed_points]
        
        # Basin volumes (via Monte Carlo)
        basin_data = self.map_basins()
        
        # Energy at attractors
        energies = [self.model.energy(fp) for fp in self.fixed_points]
        
        return {
            'n_attractors': sum(1 for s in stabilities if s['stability'] == 'stable'),
            'n_saddles': sum(1 for s in stabilities if s['stability'] == 'saddle'),
            'attractor_energies': sorted(energies),
            'energy_gap': max(energies) - min(energies) if energies else 0,
            'basin_fractions': basin_data.get('fractions', []),
            'deepest_attractor': np.argmin(energies) if energies else None
        }
```

### 4.3 Energy Barrier Computation

```python
def compute_energy_barrier(attractor_a, attractor_b, dynamics, 
                           n_paths: int = 20) -> dict:
    """Compute energy barrier between two attractors.
    
    Uses nudged elastic band (NEB) style interpolation.
    """
    # Linear interpolation
    path = np.array([attractor_a + t * (attractor_b - attractor_a) 
                     for t in np.linspace(0, 1, 50)])
    
    # Compute energy along path
    energies = np.array([dynamics.energy(x) for x in path])
    
    # Find saddle point (highest energy along MEP)
    saddle_idx = np.argmax(energies)
    barrier_height = energies[saddle_idx] - min(energies[0], energies[-1])
    
    return {
        'barrier_height': barrier_height,
        'saddle_energy': energies[saddle_idx],
        'saddle_point': path[saddle_idx],
        'energy_a': energies[0],
        'energy_b': energies[-1],
        'path_energies': energies
    }
```

## 5. Learning as Landscape Shaping

### 5.1 Conceptual Framework

Learning in EBMs = sculpting the energy landscape:

```
Before Learning:          After Learning:
  ______                    __    __
 /      \                  /  \__/  \
/        \    → TRAIN →   /          \
          \              /            \
           \____________/              \
  Flat landscape          Structured minima at data points
```

| Learning Rule | Landscape Effect |
|---------------|-----------------|
| Hebbian | Deepens minima at stored patterns |
| Contrastive Divergence | Lowers E(data), raises E(model) |
| Equilibrium Propagation | Shapes E via clamped vs free phases |
| Score Matching | Matches ∇E(x) to data score |

### 5.2 Equilibrium Propagation (Scellier & Bengio, 2017)

```python
class EquilibriumPropagation:
    """Two-phase equilibrium propagation learning.
    
    Key insight: gradient of loss can be computed as difference
    between clamped and free equilibrium states.
    """
    
    def __init__(self, model, learning_rate: float = 0.01, 
                 beta: float = 0.1, n_relax: int = 100):
        self.model = model
        self.lr = learning_rate
        self.beta = beta  # Clamping strength
        self.n_relax = n_relax  # Relaxation steps
    
    def relax_to_equilibrium(self, x: np.ndarray, 
                              clamp_indices: np.ndarray = None,
                              clamp_values: np.ndarray = None) -> np.ndarray:
        """Run dynamics until equilibrium."""
        for _ in range(self.n_relax):
            dx = self.model.vector_field(x)
            x = x + 0.1 * dx
            
            # Apply clamping
            if clamp_indices is not None:
                x[clamp_indices] += self.beta * (clamp_values - x[clamp_indices])
        
        return x
    
    def train_step(self, x_input: np.ndarray, y_target: np.ndarray,
                   input_indices: np.ndarray, output_indices: np.ndarray) -> np.ndarray:
        """Single equilibrium propagation training step.
        
        ∂L/∂Wᵢⱼ = (1/β) · (xᵢ^β xⱼ^β - xᵢ⁰ xⱼ⁰)
        where x⁰ = free equilibrium, x^β = clamped equilibrium
        """
        # Initialize with input
        x0 = np.zeros(self.model.W.shape[0])
        x0[input_indices] = x_input
        
        # Free phase: network settles with input only
        x_free = self.relax_to_equilibrium(x0)
        
        # Clamped phase: weakly clamp output to target
        x_clamped = self.relax_to_equilibrium(
            x0, 
            clamp_indices=output_indices, 
            clamp_values=y_target
        )
        
        # Weight update: contrastive Hebbian
        dW = (1.0 / self.beta) * (
            np.outer(x_clamped, x_clamped) - np.outer(x_free, x_free)
        )
        
        # Apply update (symmetric)
        self.model.W += self.lr * dW
        np.fill_diagonal(self.model.W, 0)
        
        return {
            'free_energy': self.model.energy(x_free),
            'clamped_energy': self.model.energy(x_clamped),
            'energy_diff': self.model.energy(x_free) - self.model.energy(x_clamped),
            'weight_change_norm': np.linalg.norm(dW)
        }
```

### 5.3 Contrastive Divergence for Deep EBMs

```python
class ContrastiveDivergenceEBM:
    """Training deep energy-based models via CD-k."""
    
    def __init__(self, energy_net, lr: float = 0.001, n_steps: int = 10):
        self.energy_net = energy_net  # Neural net: x → E(x)
        self.lr = lr
        self.n_steps = n_steps  # MCMC steps
    
    def sample_negative(self, x_positive: np.ndarray, temperature: float = 1.0) -> np.ndarray:
        """Langevin dynamics for negative samples."""
        x = x_positive.copy()
        
        for _ in range(self.n_steps):
            # Compute energy gradient
            E_val, dE_dx = self.energy_net.energy_and_grad(x)
            
            # Langevin update
            noise = np.random.randn_like(x) * np.sqrt(2 * temperature)
            x = x - 0.01 * dE_dx + noise * np.sqrt(0.01)
        
        return x
    
    def train_step(self, x_data: np.ndarray) -> dict:
        """CD-k training step.
        
        ∇_θ E(x) = ∇_θ E(x_data) - ∇_θ E(x_negative)
        """
        E_pos, dE_pos = self.energy_net.energy_and_grad(x_data)
        
        x_neg = self.sample_negative(x_data)
        E_neg, dE_neg = self.energy_net.energy_and_grad(x_neg)
        
        # Contrastive gradient
        d_theta = dE_pos - dE_neg
        
        return {
            'gradient': d_theta,
            'energy_positive': E_pos,
            'energy_negative': E_neg,
            'energy_gap': E_pos - E_neg
        }
```

### 5.4 Landscape Sculpting Visualization

```python
def visualize_landscape_evolution(model, initial_W, final_W, b, 
                                   resolution: int = 100, 
                                   bounds: tuple = (-2, 2)):
    """Visualize how learning reshapes the energy landscape."""
    x1 = np.linspace(bounds[0], bounds[1], resolution)
    x2 = np.linspace(bounds[0], bounds[1], resolution)
    X1, X2 = np.meshgrid(x1, x2)
    
    def compute_grid_energy(W):
        energies = np.zeros_like(X1)
        for i in range(resolution):
            for j in range(resolution):
                x = np.array([X1[i,j], X2[i,j]])
                energies[i,j] = -0.5 * x @ W @ x - b @ x
        return energies
    
    E_before = compute_grid_energy(initial_W)
    E_after = compute_grid_energy(final_W)
    
    return {
        'x1': x1, 'x2': x2,
        'energy_before': E_before,
        'energy_after': E_after,
        'energy_change': E_before - E_after
    }
```

## 6. Implementation Patterns

### 6.1 Modern Hopfield with PyTorch

```python
import torch
import torch.nn as nn

class ModernHopfieldLayer(nn.Module):
    """Modern Hopfield layer for associative memory in deep networks.
    
    Retrieval: x_new = X · softmax(β Xᵀ x)
    where X are stored patterns (memory matrix).
    """
    
    def __init__(self, dim: int, n_patterns: int, beta: float = 1.0):
        super().__init__()
        self.memories = nn.Parameter(torch.randn(n_patterns, dim) * 0.1)
        self.beta = nn.Parameter(torch.tensor(beta))
        self.dim = dim
        
    def energy(self, x: torch.Tensor) -> torch.Tensor:
        """E(x) = -lse(β Xᵀ x) + ½‖x‖²"""
        logits = self.beta * (self.memories @ x.T).T  # (batch, n_patterns)
        lse = torch.logsumexp(logits, dim=-1)
        return -lse + 0.5 * (x ** 2).sum(dim=-1)
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """One-step retrieval: x → X · softmax(β Xᵀ x)"""
        logits = self.beta * (x @ self.memories.T)  # (batch, n_patterns)
        attention = torch.softmax(logits, dim=-1)
        return attention @ self.memories
    
    def retrieve(self, x: torch.Tensor, n_steps: int = 5) -> torch.Tensor:
        """Iterative retrieval."""
        for _ in range(n_steps):
            x = self.forward(x)
        return x


class DeepEBM(nn.Module):
    """Deep energy-based model.
    
    E_θ(x) = -‖f_θ(x)‖² where f_θ is a neural network.
    Low energy = high probability.
    """
    
    def __init__(self, input_dim: int, hidden_dims: list = [128, 64]):
        super().__init__()
        layers = []
        dims = [input_dim] + hidden_dims
        for i in range(len(dims)-1):
            layers.extend([
                nn.Linear(dims[i], dims[i+1]),
                nn.LayerNorm(dims[i+1]),
                nn.SiLU()
            ])
        layers.append(nn.Linear(dims[-1], 1))
        self.feature_net = nn.Sequential(*layers)
    
    def energy(self, x: torch.Tensor) -> torch.Tensor:
        """E(x) = -‖f(x)‖² (unnormalized)"""
        features = self.feature_net(x)
        return -(features ** 2).sum(dim=-1)
    
    def energy_and_grad(self, x: torch.Tensor) -> tuple:
        """Compute energy and its gradient w.r.t. input."""
        x = x.requires_grad_(True)
        E = self.energy(x).sum()
        dE_dx = torch.autograd.grad(E, x)[0]
        return E.detach(), dE_dx.detach()
```

### 6.2 Score Matching for Training EBMs

```python
class ScoreMatchingTrainer:
    """Train EBMs via score matching (Hyvärinen, 2005).
    
    Avoids intractable partition function by matching
    ∇ₓ log p(x) = -∇ₓ E(x) to data score.
    """
    
    def __init__(self, model, lr: float = 0.001):
        self.model = model
        self.lr = lr
        self.optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    
    def compute_score_loss(self, x_data: torch.Tensor) -> torch.Tensor:
        """Sliced score matching loss.
        
        L = E[½‖∇ₓE(x)‖² - tr(∇²ₓₓE(x))]
        
        Using Hutchinson's trace estimator:
        tr(∇²E) ≈ E[vᵀ ∇²E v] for random v ~ N(0, I)
        """
        x = x_data.requires_grad_(True)
        
        # First derivative
        E = self.model.energy(x).sum()
        dE_dx = torch.autograd.grad(E, x, create_graph=True)[0]
        
        # Gradient norm term
        grad_norm_sq = (dE_dx ** 2).sum(dim=-1).mean()
        
        # Hutchinson trace estimator
        v = torch.randn_like(x)
        v_dot_grad = (dE_dx * v).sum()
        hutchinson_trace = torch.autograd.grad(
            v_dot_grad, x, create_graph=False
        )[0]
        trace_term = (hutchinson_trace * v).sum(dim=-1).mean()
        
        loss = 0.5 * grad_norm_sq - trace_term
        return loss
    
    def train_step(self, x_data: torch.Tensor) -> dict:
        self.optimizer.zero_grad()
        loss = self.compute_score_loss(x_data)
        loss.backward()
        self.optimizer.step()
        
        return {'loss': loss.item()}
```

### 6.3 Langevin Sampling from EBMs

```python
class LangevinSampler:
    """Generate samples from EBM via Langevin dynamics.
    
    dx = -∇ₓE(x) dt + √(2T) dW
    """
    
    def __init__(self, model, temperature: float = 1.0):
        self.model = model
        self.temperature = temperature
    
    def sample(self, x0: torch.Tensor, n_steps: int = 1000,
               step_size: float = 0.01) -> torch.Tensor:
        """Generate sample starting from noise."""
        x = x0.clone().requires_grad_(True)
        
        for _ in range(n_steps):
            E, dE_dx = self.model.energy_and_grad(x)
            
            # Langevin update
            noise = torch.randn_like(x) * np.sqrt(2 * self.temperature * step_size)
            x = x.detach() - step_size * dE_dx + noise
            x = x.requires_grad_(True)
            
            # Optional: clip to valid range
            x = torch.clamp(x, -5.0, 5.0)
        
        return x.detach()
    
    def annealed_sample(self, shape: tuple, n_temperatures: int = 10,
                        steps_per_temp: int = 100) -> torch.Tensor:
        """Annealed Langevin: gradually decrease temperature."""
        temperatures = np.linspace(10.0, 0.1, n_temperatures)
        x = torch.randn(shape) * np.sqrt(temperatures[0])
        
        for T in temperatures:
            x = self.sample(x, steps_per_temp, step_size=0.01 * T)
        
        return x
```

### 6.4 Modern Hopfield for Sequence Modeling

```python
class HopfieldTransformerBlock(nn.Module):
    """Transformer block using modern Hopfield retrieval."""
    
    def __init__(self, dim: int, n_heads: int = 4, beta: float = 1.0):
        super().__init__()
        self.heads = nn.ModuleList([
            ModernHopfieldLayer(dim, dim // n_heads, beta)
            for _ in range(n_heads)
        ])
        self.proj = nn.Linear(dim, dim)
        self.norm = nn.LayerNorm(dim)
        self.mlp = nn.Sequential(
            nn.Linear(dim, dim * 4),
            nn.GELU(),
            nn.Linear(dim * 4, dim)
        )
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """x shape: (batch, seq_len, dim)"""
        # Hopfield attention (replaces standard attention)
        head_outputs = []
        for head in self.heads:
            head_out = head(x)
            head_outputs.append(head_out)
        
        attn_out = self.proj(torch.cat(head_outputs, dim=-1))
        x = self.norm(x + attn_out)
        
        # MLP
        x = self.norm(x + self.mlp(x))
        return x
```

## 7. Pitfalls and Best Practices

### 7.1 Common Pitfalls

| Pitfall | Symptom | Solution |
|---------|---------|----------|
| **Spurious attractors** | Network converges to wrong pattern | Use modern Hopfield with log-sum-exp energy; increase capacity |
| **Energy not decreasing** | `dE/dt > 0` during dynamics | Ensure W is symmetric; check activation monotonicity; verify Lyapunov conditions |
| **Mode collapse** | All samples converge to one attractor | Add regularization; use temperature scheduling; increase noise |
| **Intractable partition function** | Cannot compute normalized probabilities | Use score matching; use contrastive divergence; use noise-contrastive estimation |
| **Slow convergence** | Dynamics take too long to settle | Tune τ (time constant); use adaptive step sizes; check conditioning of W |
| **Overfitting landscape** | Perfect training energy, poor generalization | Regularize weights; use dropout in energy function; validate on held-out energy gaps |
| **Gradient vanishing/exploding** | Training unstable | Gradient clipping; weight normalization; spectral normalization of W |
| **Non-convergence in high dim** | Dynamics never reach equilibrium in large networks | Use layer-wise training; constrain spectral radius; use residual connections |

### 7.2 Best Practices Checklist

- [ ] **Symmetry check**: Verify W = Wᵀ for convergence guarantee
- [ ] **Spectral radius**: Ensure ρ(W) < 1 for stable dynamics (or tune appropriately)
- [ ] **Energy monitoring**: Track E(x(t)) to confirm monotonic decrease
- [ ] **Equilibration time**: Run dynamics long enough to reach fixed points
- [ ] **Temperature scheduling**: Anneal from high T (exploration) to low T (exploitation)
- [ ] **Multiple initial conditions**: Test convergence from diverse starting points
- [ ] **Basin validation**: Verify attractor basins match expected memory patterns
- [ ] **Gradient verification**: Numerically check gradients vs. analytical

### 7.3 Capacity Bounds

```python
def hopfield_capacity(n_neurons: int, alpha: float = 0.14) -> int:
    """Classical Hopfield capacity: p_max ≈ 0.14N patterns."""
    return int(alpha * n_neurons)

def modern_hopfield_capacity(n_neurons: int, n_patterns: int) -> float:
    """Modern Hopfield can store exponentially many patterns.
    
    Capacity scales as exp(n_neurons) rather than linear.
    """
    # Theoretical bound for dense associative memory
    return np.log2(n_patterns) / n_neurons
```

## 8. Activation Keywords

### English
energy-based models, EBMs, neural dynamics, Hopfield networks, energy landscape, attractor dynamics, gradient flow, equilibrium propagation, contrastive learning, Lyapunov stability, associative memory, pattern completion, Boltzmann machine, score matching, Langevin sampling, modern Hopfield, dense associative memory, energy minimization, dynamical systems, biologically-plausible learning

### 中文
能量模型, 能量景观, 神经动力学, 吸引子动力学, 梯度流, 平衡传播, 对比学习, 李雅普诺夫稳定性, 联想记忆, 模式补全, 波尔兹曼机, 分数匹配, 朗之万采样, 现代Hopfield网络, 密集联想记忆, 能量最小化, 动力系统, 生物可学习规则

## 9. Related Skills

- **eeg-hopfield-emotion-energy** — Energy landscapes for EEG emotion analysis using Hopfield framework
- **neuro-attractor-landscape-working-memory** — Attractor dynamics in working memory neural circuits
- **spikingjelly-framework** — Spiking neural network framework (complementary dynamics paradigm)
- **spiking-neural-network-analysis** — Analysis of SNN dynamics and energy efficiency
- **brain-inspired-snn-pattern-analysis** — Brain-inspired pattern recognition with spiking dynamics
- **thermodynamic-brain-connectivity** — Thermodynamic analysis of brain networks
- **neural-emulator-theory** — Neural emulation theory and dynamical systems
- **brain-graph-neural** — Graph-based brain network analysis
- **complex-kuramoto-control** — Kuramoto model for coupled oscillator dynamics
- **tsodyks-markram-chaotic-dynamics** — Chaotic dynamics in synaptic transmission models

## References

1. **Primary Paper**: "Energy-Based Dynamical Models for Neurocomputation, Learning, and Optimization" — Montanari, Bullo, Krotov, Motter (arXiv:2604.05042, 2026)
2. Hopfield, J.J. (1982). "Neural networks and physical systems with emergent collective computational abilities." *PNAS*, 79(8):2554–2558.
3. Hopfield, J.J. (1984). "Neurons with graded response have collective computational properties like those of two-state neurons." *PNAS*, 81(10):3088–3092.
4. Scellier, B. & Bengio, Y. (2017). "Equilibrium Propagation: Bridging the gap between energy-based models and backpropagation." *Frontiers in Computational Neuroscience*, 11:24.
5. Krotov, D. & Hopfield, J.J. (2016). "Dense Associative Memory for Pattern Recognition." *NeurIPS 2016*.
6. Hinton, G.E. (2002). "Training Products of Experts by Minimizing Contrastive Divergence." *Neural Computation*, 14(8):1771–1800.
7. Ramsauer, H. et al. (2021). "Hopfield Networks is All You Need." *ICLR 2021*.
8. LeCun, Y. et al. (2006). "A Tutorial on Energy-Based Learning." *Predicting Structured Data*, MIT Press.
9. Hyvärinen, A. (2005). "Estimation of Non-Normalized Statistical Models by Score Matching." *JMLR*, 6:695–709.
