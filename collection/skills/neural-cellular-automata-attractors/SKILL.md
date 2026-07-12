---
name: neural-cellular-automata-attractors
description: "Neural Cellular Automata (NCA) attractor analysis methodology. Studies stability, geometry, and dynamics of learned attractors in self-organizing neural systems using dynamical systems theory. Methods for analyzing ordered vs chaotic behavior, long-horizon stability estimation, and perturbation responses in NCA. Activation: NCA attractor, neural cellular automata, self-organizing neural, attractor stability, dynamical systems NCA."
---

# Neural Cellular Automata: Attractor Analysis

## Description
This skill provides methodology for rigorously analyzing the attractors learned by Neural Cellular Automata (NCA) systems. Rather than assuming attractor behavior based on visual similarity, it applies dynamical systems theory to characterize attractor geometry, stability, ordered/chaotic behavior, and response to perturbations.

## Background

### What are Neural Cellular Automata?
NCAs combine cellular automata with neural networks:
- **Grid-based**: Cells arranged in spatial grid
- **Local update rules**: Each cell updates based on neighbors
- **Neural network parameterization**: Update rules learned by neural nets
- **Self-organizing**: Global patterns emerge from local interactions

### The Attractor Problem
NCAs are often trained to reach target patterns:
- Training: Minimize distance to target after T steps
- Observation: Visual similarity to target after many steps
- **Missing**: Rigorous characterization of attractor properties

## Core Methodology

### 1. Attractor Identification
```python
def find_attractors(nca, initial_states, n_steps=1000, tolerance=1e-6):
    """
    Identify attractors by running NCA from multiple initial conditions
    and clustering final states.
    """
    final_states = []
    
    for init in initial_states:
        state = init
        for _ in range(n_steps):
            state = nca.update(state)
        final_states.append(state)
    
    # Cluster similar final states
    attractors = cluster_states(final_states, tolerance)
    return attractors
```

### 2. Attractor Type Classification
```python
def classify_attractor_type(trajectory, max_period=100):
    """
    Classify attractor as:
    - Fixed point: state(t) == state(t+1)
    - Limit cycle: state(t) == state(t+period)
    - Strange attractor: chaotic, fractal structure
    - Quasi-periodic: multiple incommensurate frequencies
    """
    # Check for fixed point
    if distance(trajectory[-1], trajectory[-2]) < epsilon:
        return "FIXED_POINT"
    
    # Check for periodicity
    for period in range(2, max_period):
        if is_periodic(trajectory, period):
            return f"LIMIT_CYCLE_{period}"
    
    # Compute Lyapunov exponents
    lyapunovs = compute_lyapunov_exponents(trajectory)
    if max(lyapunovs) > 0:
        return "STRANGE_ATTRACTOR"
    
    return "QUASI_PERIODIC"
```

### 3. Stability Analysis

#### Basin of Attraction
```python
def compute_basin_of_attraction(nca, attractor, grid_resolution=100):
    """
    Map the region of state space that converges to each attractor.
    """
    basin = np.zeros((grid_resolution, grid_resolution))
    
    for i, x in enumerate(np.linspace(-1, 1, grid_resolution)):
        for j, y in enumerate(np.linspace(-1, 1, grid_resolution)):
            init_state = create_state(x, y)
            final = simulate_to_convergence(nca, init_state)
            
            # Assign to nearest attractor
            attractor_id = find_nearest_attractor(final, attractors)
            basin[i, j] = attractor_id
    
    return basin
```

#### Lyapunov Exponents
```python
def compute_lyapunov_exponents(nca, initial_state, n_steps=1000, n_transient=100):
    """
    Compute the spectrum of Lyapunov exponents to characterize
    attractor stability and chaos.
    
    Positive exponent → Chaos (sensitive to initial conditions)
    Negative exponent → Stability
    Zero exponent → Marginal stability (bifurcation point)
    """
    state = initial_state
    perturbations = initialize_orthogonal_basis(state_dim)
    lyapunovs = np.zeros(state_dim)
    
    for t in range(n_steps):
        # Evolve state
        state = nca.update(state)
        
        # Evolve perturbations (linearized dynamics)
        jacobian = compute_jacobian(nca, state)
        perturbations = jacobian @ perturbations
        
        # Orthogonalize and record growth rates
        if t >= n_transient:
            perturbations, growth_rates = gram_schmidt(perturbations)
            lyapunovs += np.log(growth_rates)
    
    lyapunovs /= (n_steps - n_transient)
    return lyapunovs
```

### 4. Geometry Characterization

#### Fractal Dimension
```python
def compute_correlation_dimension(trajectory, r_min=1e-4, r_max=1.0, n_r=50):
    """
    Estimate fractal dimension using correlation sum method.
    
    For strange attractors: non-integer dimension
    For simple attractors: integer dimension
    """
    rs = np.logspace(np.log10(r_min), np.log10(r_max), n_r)
    correlation_sums = []
    
    for r in rs:
        C_r = correlation_sum(trajectory, r)
        correlation_sums.append(C_r)
    
    # Slope of log(C) vs log(r) gives dimension
    dimension = np.gradient(np.log(correlation_sums), np.log(rs))
    return dimension
```

#### Embedding Space Analysis
```python
def takens_embedding(trajectory, delay=1, dimension=3):
    """
    Reconstruct attractor geometry from time series using
    Takens' embedding theorem.
    """
    embedded = np.zeros((len(trajectory) - (dimension-1)*delay, dimension))
    
    for i in range(dimension):
        embedded[:, i] = trajectory[i*delay : len(trajectory)-(dimension-1-i)*delay]
    
    return embedded
```

## Analysis Pipeline

### Step-by-Step Workflow
```python
class NCAAttractorAnalyzer:
    def __init__(self, nca_model):
        self.nca = nca_model
        
    def full_analysis(self, initial_conditions):
        results = {}
        
        # 1. Find attractors
        print("Finding attractors...")
        attractors = self.find_attractors(initial_conditions)
        results['attractors'] = attractors
        
        # 2. Classify each attractor
        print("Classifying attractor types...")
        for i, attractor in enumerate(attractors):
            trajectory = self.simulate_attractor(attractor)
            attractor_type = classify_attractor_type(trajectory)
            results[f'attractor_{i}_type'] = attractor_type
        
        # 3. Stability analysis
        print("Computing Lyapunov exponents...")
        for i, attractor in enumerate(attractors):
            lyapunovs = compute_lyapunov_exponents(self.nca, attractor)
            results[f'attractor_{i}_lyapunovs'] = lyapunovs
            results[f'attractor_{i}_max_lyapunov'] = max(lyapunovs)
        
        # 4. Basin structure
        print("Mapping basins of attraction...")
        basins = self.compute_basins(attractors)
        results['basins'] = basins
        
        # 5. Geometry
        print("Characterizing geometry...")
        for i, attractor in enumerate(attractors):
            dim = compute_correlation_dimension(attractor)
            results[f'attractor_{i}_dimension'] = dim
        
        return results
```

## Case Study: Growing Gecko NCA

### Analysis Results
Based on the paper's analysis of Mordvintsev et al. (2020):

| Property | Finding | Interpretation |
|----------|---------|----------------|
| Attractor type | Strange attractor | Complex, chaotic dynamics |
| Max Lyapunov | λ ≈ 0.1 | Weak chaos, some predictability |
| Fractal dimension | D ≈ 2.3 | Non-integer, complex structure |
| Basin complexity | High | Sensitive to initial conditions |

### Perturbation Response
```python
def analyze_perturbation_response(nca, attractor, perturbation_strengths):
    """
    Study how perturbations affect attractor behavior.
    """
    results = {}
    
    for strength in perturbation_strengths:
        perturbed = attractor + np.random.randn(*attractor.shape) * strength
        
        # Simulate recovery
        trajectory = [perturbed]
        for _ in range(100):
            trajectory.append(nca.update(trajectory[-1]))
        
        # Measure return to attractor
        distances = [distance(state, attractor) for state in trajectory]
        
        # Classify response
        if distances[-1] < 1e-3:
            response_type = "RECOVERY"
        elif oscillates(distances):
            response_type = "LIMIT_CYCLE"
        else:
            response_type = "BASIN_SWITCH"
        
        results[strength] = {
            'trajectory': trajectory,
            'distances': distances,
            'response_type': response_type
        }
    
    return results
```

## Long-Horizon Stability

### Challenge
NCA trained for T steps may behave differently at >>T steps.

### Method
```python
def estimate_long_term_stability(nca, initial_state, horizons=[100, 1000, 10000]):
    """
    Estimate stability over very long time horizons.
    """
    results = {}
    
    for T in horizons:
        state = initial_state
        trajectory = []
        
        for t in range(T):
            state = nca.update(state)
            
            # Periodically checkpoint
            if t % 100 == 0:
                trajectory.append(state.copy())
        
        # Analyze
        results[T] = {
            'final_state': state,
            'trajectory': trajectory,
            'is_periodic': check_periodicity(trajectory),
            'divergence_measure': compute_divergence(trajectory)
        }
    
    return results
```

## Practical Applications

### 1. Robustness Testing
```python
def test_robustness(nca, n_perturbations=1000):
    """Test if NCA reliably reaches target pattern."""
    success_count = 0
    
    for _ in range(n_perturbations):
        init = add_noise(target_pattern, noise_level=0.1)
        final = simulate(nca, init, steps=1000)
        
        if distance(final, target_pattern) < threshold:
            success_count += 1
    
    return success_count / n_perturbations
```

### 2. Attractor Engineering
```python
def design_target_attractor(target_pattern, constraints):
    """
    Train NCA with explicit attractor constraints.
    """
    nca = initialize_nca()
    
    for epoch in range(n_epochs):
        # Standard reconstruction loss
        loss = reconstruction_loss(nca, target_pattern)
        
        # Add attractor stability penalty
        lyapunovs = compute_lyapunov_exponents(nca, target_pattern)
        stability_penalty = max(0, max(lyapunovs))
        
        # Add basin size penalty (encourage large basin)
        basin_volume = estimate_basin_volume(nca, target_pattern)
        basin_penalty = -basin_volume  # Maximize
        
        total_loss = loss + lambda_1 * stability_penalty + lambda_2 * basin_penalty
        
        optimize(total_loss)
    
    return nca
```

## References

- **Paper**: Stability and Geometry of Attractors in Neural Cellular Automata (arXiv:2604.12720, 2026)
- **Authors**: Mia-Katrin Kvalsund, James Stovold
- **Case study**: Growing Gecko NCA (Mordvintsev et al., 2020)
- **Methods**: Lyapunov exponents, correlation dimension, basin analysis

## Activation Keywords
- NCA attractor
- neural cellular automata
- self-organizing neural
- attractor stability
- dynamical systems NCA
- chaos analysis NCA
- Lyapunov exponent NCA

## Related Skills
- brain-inspired-nca: Brain-inspired NCA for morphogenesis
- attractor-metadynamics-neural: Neural attractor metadynamics
- chaos-freezing-without-plasticity: Stabilizing neural chaos
