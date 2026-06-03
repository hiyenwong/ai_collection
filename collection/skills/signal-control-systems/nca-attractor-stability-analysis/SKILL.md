---
name: nca-attractor-stability-analysis
description: "Neural Cellular Automata (NCA) attractor stability and geometry analysis methodology. Analyzes learned attractor states in NCAs beyond visual similarity, measuring basin of attraction, convergence properties, and geometric structure. Activation: NCA attractor, neural cellular automata stability, attractor basin analysis, NCA convergence."
---

# NCA Attractor Stability and Geometry Analysis

## Description

Methodology for analyzing the stability and geometry of attractors in Neural Cellular Automata (NCA) beyond simple visual similarity measures. This framework provides rigorous analysis of learned attractor states including basin of attraction characterization, convergence properties, and geometric structure analysis.

Based on research from arXiv:2604.12720v1 - "Stability and Geometry of Attractors in Neural Cellular Automata" by Mia-Katrin Kvalsund and James Stovold.

## Activation Keywords

- NCA attractor
- neural cellular automata stability
- attractor basin analysis
- NCA convergence
- attractor geometry
- cellular automata dynamics
- NCA stability analysis
- 吸引子稳定性分析
- 神经元胞自动机

## Tools Used

- `write`: Create analysis implementations
- `exec`: Run NCA simulations and analysis
- `read`: Load NCA models and configurations
- `patch`: Modify analysis parameters

## Core Concepts

### 1. Attractor States

Attractors in NCAs are states that:
- Are stable under NCA dynamics
- Attract nearby states into their basin
- Represent learned target patterns
- May be fixed points or limit cycles

### 2. Basin of Attraction

The basin characterizes:
- **Size**: Volume of state space attracted
- **Shape**: Geometric structure of basin
- **Boundaries**: Separatrices between basins
- **Robustness**: Stability under perturbations

### 3. Stability Metrics

Quantitative stability measures:
- **Lyapunov exponents**: Rate of convergence
- **Eigenvalue spectrum**: Local stability
- **Convergence time**: Steps to reach attractor
- **Perturbation recovery**: Robustness to noise

## Implementation

### Step 1: NCA Model Setup

```python
import torch
import torch.nn as nn
import numpy as np

class NeuralCellularAutomata(nn.Module):
    """
    Neural Cellular Automata with learnable update rules.
    """
    
    def __init__(self, num_channels=16, hidden_channels=128, fire_rate=0.5):
        super().__init__()
        self.num_channels = num_channels
        self.hidden_channels = hidden_channels
        self.fire_rate = fire_rate
        
        # Perception kernel (Sobel filters for gradients)
        self.register_buffer('sobel_x', torch.tensor([
            [-1, 0, 1], [-2, 0, 2], [-1, 0, 1]
        ], dtype=torch.float32).view(1, 1, 3, 3))
        
        self.register_buffer('sobel_y', torch.tensor([
            [-1, -2, -1], [0, 0, 0], [1, 2, 1]
        ], dtype=torch.float32).view(1, 1, 3, 3))
        
        # Update network
        self.update_net = nn.Sequential(
            nn.Conv2d(num_channels * 3, hidden_channels, 1),
            nn.ReLU(),
            nn.Conv2d(hidden_channels, num_channels, 1)
        )
        
    def perceive(self, state):
        """Apply perception kernels to state."""
        # Identity
        identity = state
        
        # Gradients
        grad_x = torch.nn.functional.conv2d(
            state.view(-1, 1, state.shape[-2], state.shape[-1]),
            self.sobel_x, padding=1
        ).view(state.shape[0], -1, state.shape[-2], state.shape[-1])
        
        grad_y = torch.nn.functional.conv2d(
            state.view(-1, 1, state.shape[-2], state.shape[-1]),
            self.sobel_y, padding=1
        ).view(state.shape[0], -1, state.shape[-2], state.shape[-1])
        
        return torch.cat([identity, grad_x, grad_y], dim=1)
    
    def forward(self, state, steps=1):
        """
        Run NCA for specified steps.
        
        Args:
            state: Current state (batch, channels, height, width)
            steps: Number of steps to run
        
        Returns:
            new_state: Updated state
            trajectory: States at each step
        """
        trajectory = [state.detach()]
        
        for _ in range(steps):
            # Perceive
            perception = self.perceive(state)
            
            # Update
            update = self.update_net(perception)
            
            # Stochastic update (fire rate)
            if self.training:
                mask = torch.rand_like(state[:, :1]) < self.fire_rate
                mask = mask.expand_as(state)
                state = state + update * mask.float()
            else:
                state = state + update
            
            trajectory.append(state.detach())
        
        return state, trajectory
```

### Step 2: Attractor Identification

```python
class AttractorAnalyzer:
    """
    Analyze attractors in trained NCA.
    """
    
    def __init__(self, nca_model, device='cuda'):
        self.nca = nca_model.to(device)
        self.nca.eval()
        self.device = device
        
    def find_attractors(self, initial_states, max_steps=1000, tolerance=1e-4):
        """
        Find attractor states from initial conditions.
        
        Args:
            initial_states: Initial state configurations
            max_steps: Maximum steps to simulate
            tolerance: Convergence tolerance
        
        Returns:
            attractors: Dictionary of found attractors
            convergence_info: Convergence data for each initial state
        """
        attractors = {}
        convergence_info = []
        
        for idx, init_state in enumerate(initial_states):
            state = init_state.to(self.device)
            
            # Run until convergence
            converged = False
            prev_state = None
            
            for step in range(max_steps):
                state, _ = self.nca(state, steps=1)
                
                # Check convergence
                if prev_state is not None:
                    diff = torch.abs(state - prev_state).max().item()
                    
                    if diff < tolerance:
                        converged = True
                        break
                
                prev_state = state.clone()
            
            # Identify attractor
            attractor_id = self._identify_attractor(state, attractors, tolerance)
            
            convergence_info.append({
                'initial_idx': idx,
                'attractor_id': attractor_id,
                'steps_to_convergence': step if converged else max_steps,
                'converged': converged,
                'final_state': state.cpu()
            })
        
        return attractors, convergence_info
    
    def _identify_attractor(self, state, attractors, tolerance):
        """Identify which attractor state converged to."""
        state_flat = state.flatten()
        
        for attr_id, attr_state in attractors.items():
            diff = torch.abs(state_flat - attr_state.flatten()).max().item()
            if diff < tolerance:
                return attr_id
        
        # New attractor
        new_id = len(attractors)
        attractors[new_id] = state.cpu()
        return new_id
```

### Step 3: Basin of Attraction Analysis

```python
    def analyze_basins(self, attractors, num_samples=1000, noise_levels=None):
        """
        Analyze basin of attraction for each attractor.
        
        Args:
            attractors: Dictionary of attractor states
            num_samples: Number of random initial samples
            noise_levels: List of noise magnitudes to test
        
        Returns:
            basin_stats: Statistics for each basin
        """
        if noise_levels is None:
            noise_levels = [0.1, 0.2, 0.5, 1.0]
        
        basin_stats = {attr_id: {
            'count': 0,
            'avg_convergence_time': 0,
            'noise_robustness': {}
        } for attr_id in attractors}
        
        # Sample from random initial conditions
        total_samples = 0
        
        for _ in range(num_samples):
            # Random initial state
            init_state = torch.randn(1, self.nca.num_channels, 64, 64).to(self.device)
            
            # Find attractor
            _, convergence_info = self.find_attractors([init_state], max_steps=500)
            
            if convergence_info[0]['converged']:
                attr_id = convergence_info[0]['attractor_id']
                basin_stats[attr_id]['count'] += 1
                basin_stats[attr_id]['avg_convergence_time'] += convergence_info[0]['steps_to_convergence']
                total_samples += 1
        
        # Normalize
        for attr_id in basin_stats:
            if basin_stats[attr_id]['count'] > 0:
                basin_stats[attr_id]['avg_convergence_time'] /= basin_stats[attr_id]['count']
                basin_stats[attr_id]['basin_fraction'] = basin_stats[attr_id]['count'] / total_samples
        
        # Test noise robustness
        for noise_level in noise_levels:
            for attr_id, attractor in attractors.items():
                robust_count = 0
                num_perturbations = 100
                
                for _ in range(num_perturbations):
                    # Perturb attractor
                    noise = torch.randn_like(attractor) * noise_level
                    perturbed = (attractor + noise).to(self.device)
                    
                    # Check if returns to attractor
                    final_state, _ = self.find_attractors([perturbed], max_steps=200)
                    
                    # Identify final attractor
                    final_id = self._identify_attractor(
                        convergence_info[0]['final_state'].to(self.device),
                        {attr_id: attractor},
                        tolerance=1e-3
                    )
                    
                    if final_id == attr_id:
                        robust_count += 1
                
                basin_stats[attr_id]['noise_robustness'][noise_level] = robust_count / num_perturbations
        
        return basin_stats
```

### Step 4: Stability Analysis

```python
    def compute_stability_metrics(self, attractor, num_perturbations=100):
        """
        Compute stability metrics for an attractor.
        
        Args:
            attractor: Attractor state tensor
            num_perturbations: Number of perturbations to test
        
        Returns:
            metrics: Dictionary of stability metrics
        """
        attractor = attractor.to(self.device)
        
        # Linear stability analysis
        jacobian = self._compute_jacobian(attractor)
        eigenvalues = torch.linalg.eigvals(jacobian)
        
        # Lyapunov exponents (simplified - full computation is expensive)
        lyapunov = self._estimate_lyapunov(attractor, num_perturbations)
        
        # Return time analysis
        return_times = []
        perturbation_magnitudes = []
        
        for _ in range(num_perturbations):
            # Random perturbation
            magnitude = np.random.uniform(0.01, 0.5)
            perturbation = torch.randn_like(attractor) * magnitude
            perturbed = attractor + perturbation
            
            # Simulate return
            state = perturbed
            for step in range(500):
                prev_state = state.clone()
                state, _ = self.nca(state, steps=1)
                
                # Check if returned
                if torch.abs(state - attractor).max() < 1e-3:
                    return_times.append(step)
                    perturbation_magnitudes.append(magnitude)
                    break
        
        metrics = {
            'max_eigenvalue_real': eigenvalues.real.max().item(),
            'max_eigenvalue_imag': eigenvalues.imag.abs().max().item(),
            'is_stable': eigenvalues.real.max().item() < 0,
            'lyapunov_exponent': lyapunov,
            'avg_return_time': np.mean(return_times) if return_times else float('inf'),
            'return_time_vs_magnitude': list(zip(perturbation_magnitudes, return_times))
        }
        
        return metrics
    
    def _compute_jacobian(self, state, eps=1e-4):
        """
        Compute Jacobian matrix numerically.
        
        Args:
            state: State at which to compute Jacobian
            eps: Perturbation size
        
        Returns:
            jacobian: Jacobian matrix
        """
        state_flat = state.flatten()
        dim = state_flat.shape[0]
        jacobian = torch.zeros(dim, dim, device=self.device)
        
        # Compute next state
        next_state, _ = self.nca(state, steps=1)
        next_flat = next_state.flatten()
        
        # Numerical differentiation
        for i in range(min(dim, 1000)):  # Limit for efficiency
            perturbed = state.clone()
            perturbed.flatten()[i] += eps
            
            next_perturbed, _ = self.nca(perturbed, steps=1)
            derivative = (next_perturbed.flatten() - next_flat) / eps
            
            jacobian[:, i] = derivative
        
        return jacobian
    
    def _estimate_lyapunov(self, attractor, num_samples=50):
        """
        Estimate largest Lyapunov exponent.
        
        Args:
            attractor: Attractor state
            num_samples: Number of samples for estimation
        
        Returns:
            lyapunov: Estimated largest Lyapunov exponent
        """
        divergences = []
        
        for _ in range(num_samples):
            # Initial perturbation
            perturbation = torch.randn_like(attractor) * 1e-4
            state1 = attractor.clone()
            state2 = attractor + perturbation
            
            # Track divergence
            distances = []
            
            for _ in range(20):
                state1, _ = self.nca(state1, steps=1)
                state2, _ = self.nca(state2, steps=1)
                
                distance = torch.norm(state2 - state1).item()
                distances.append(distance)
                
                # Renormalize
                if distance > 1e-3:
                    diff = state2 - state1
                    state2 = state1 + diff * (1e-4 / distance)
            
            # Compute local divergence rate
            if len(distances) > 1:
                log_dists = np.log(distances[1:])
                local_exp = np.mean(np.diff(log_dists))
                divergences.append(local_exp)
        
        return np.mean(divergences) if divergences else 0.0
```

### Step 5: Geometric Analysis

```python
    def analyze_attractor_geometry(self, attractors, num_samples_per_attractor=100):
        """
        Analyze geometric properties of attractors.
        
        Args:
            attractors: Dictionary of attractors
            num_samples_per_attractor: Samples near each attractor
        
        Returns:
            geometry_stats: Geometric properties
        """
        geometry_stats = {}
        
        for attr_id, attractor in attractors.items():
            attractor = attractor.to(self.device)
            attractor_flat = attractor.flatten()
            
            # Sample points near attractor
            samples = []
            for _ in range(num_samples_per_attractor):
                # Random direction
                direction = torch.randn_like(attractor)
                direction = direction / torch.norm(direction)
                
                # Random distance (log scale)
                distance = 10 ** np.random.uniform(-4, 0)
                sample = attractor + direction * distance
                samples.append(sample)
            
            # Compute distances to attractor after evolution
            final_distances = []
            for sample in samples:
                final_state, _ = self.find_attractors([sample], max_steps=100)
                dist = torch.norm(final_state - attractor_flat).item()
                final_distances.append(dist)
            
            # Estimate basin boundary distance
            threshold = 0.1
            boundary_samples = [d for d in final_distances if d > threshold]
            
            geometry_stats[attr_id] = {
                'attractor_norm': torch.norm(attractor).item(),
                'attractor_mean': attractor.mean().item(),
                'attractor_std': attractor.std().item(),
                'estimated_basin_radius': np.mean(boundary_samples) if boundary_samples else float('inf'),
                'convergence_rate': np.mean([1 if d < threshold else 0 for d in final_distances]),
                'fractal_dimension': self._estimate_fractal_dimension(attractor)
            }
        
        return geometry_stats
    
    def _estimate_fractal_dimension(self, state, num_scales=10):
        """
        Estimate fractal dimension using box counting.
        
        Args:
            state: State tensor
            num_scales: Number of scales to test
        
        Returns:
            dimension: Estimated fractal dimension
        """
        # Simplified box counting on 2D projection
        state_np = state[0].cpu().numpy().mean(axis=0)  # Average over channels
        
        # Normalize
        state_np = (state_np - state_np.min()) / (state_np.max() - state_np.min() + 1e-8)
        
        # Box counting
        H, W = state_np.shape
        scales = np.logspace(0, np.log10(min(H, W) / 4), num_scales).astype(int)
        scales = np.unique(scales)
        
        counts = []
        for scale in scales:
            if scale < 1:
                continue
            # Count non-empty boxes
            boxes = []
            for i in range(0, H, scale):
                for j in range(0, W, scale):
                    box = state_np[i:i+scale, j:j+scale]
                    if box.max() > 0.1:  # Threshold
                        boxes.append(1)
            counts.append(len(boxes))
        
        # Compute dimension from slope
        if len(counts) > 1:
            log_scales = np.log(1.0 / np.array(scales[:len(counts)]))
            log_counts = np.log(counts)
            slope, _ = np.polyfit(log_scales, log_counts, 1)
            return slope
        
        return 2.0  # Default to 2D
```

## Usage Patterns

### Pattern 1: Complete Attractor Analysis

```python
# Load trained NCA
nca = NeuralCellularAutomata(num_channels=16)
nca.load_state_dict(torch.load('nca_model.pth'))

# Create analyzer
analyzer = AttractorAnalyzer(nca)

# Generate diverse initial conditions
initial_states = [torch.randn(1, 16, 64, 64) for _ in range(100)]

# Find attractors
attractors, convergence_info = analyzer.find_attractors(
    initial_states, 
    max_steps=1000
)

print(f"Found {len(attractors)} attractors")

# Analyze basins
basin_stats = analyzer.analyze_basins(attractors, num_samples=500)

# Stability analysis
for attr_id, attractor in attractors.items():
    metrics = analyzer.compute_stability_metrics(attractor)
    print(f"Attractor {attr_id}: Stable={metrics['is_stable']}, "
          f"Lyapunov={metrics['lyapunov_exponent']:.4f}")

# Geometry analysis
geometry = analyzer.analyze_attractor_geometry(attractors)
```

### Pattern 2: Visualize Attractor Landscape

```python
def visualize_attractor_landscape(analyzer, grid_size=20):
    """Visualize attractor basins in 2D projection."""
    import matplotlib.pyplot as plt
    
    # Create grid of initial conditions
    x = np.linspace(-2, 2, grid_size)
    y = np.linspace(-2, 2, grid_size)
    
    attractor_map = np.zeros((grid_size, grid_size))
    
    for i, xi in enumerate(x):
        for j, yj in enumerate(y):
            # Create initial state from coordinates
            init = torch.randn(1, 16, 64, 64)
            init[0, 0, 32, 32] = xi  # Use first channel center
            init[0, 1, 32, 32] = yj
            
            # Find attractor
            _, info = analyzer.find_attractors([init], max_steps=200)
            attractor_map[j, i] = info[0]['attractor_id']
    
    # Plot
    plt.figure(figsize=(10, 8))
    plt.imshow(attractor_map, origin='lower', cmap='tab10')
    plt.colorbar(label='Attractor ID')
    plt.title('Basin of Attraction Landscape')
    plt.xlabel('Dimension 1')
    plt.ylabel('Dimension 2')
    plt.savefig('attractor_landscape.png')
```

## Error Handling

### No Convergence

If states don't converge:
1. Increase max_steps
2. Check tolerance (may be too strict)
3. Verify NCA model is trained
4. Check for chaotic dynamics

### Numerical Instability

If Jacobian computation fails:
1. Reduce eps (perturbation size)
2. Limit dimensionality
3. Use sparse Jacobian approximation
4. Check for NaN/Inf in states

### Memory Issues

For large state spaces:
1. Process in batches
2. Use smaller grid sizes
3. Limit number of perturbations
4. Use low-memory mode

## References

- Kvalsund, M. K., & Stovold, J. (2026). Stability and Geometry of Attractors in Neural Cellular Automata. arXiv:2604.12720v1.
- Mordvintsev, A., Randazzo, E., Niklasson, E., & Levin, M. (2020). Growing neural cellular automata. Distill.
- Randazzo, E., Mordvintsev, A., Niklasson, E., & Levin, M. (2021). Self-organising textures. Neural Computing and Applications.

## Related Skills

- `brain-digital-twins-execution-semantics`: Execution semantics
- `neural-cellular-automata-attractors`: NCA attractor analysis
- `neuroscience`: General neuroscience methods
