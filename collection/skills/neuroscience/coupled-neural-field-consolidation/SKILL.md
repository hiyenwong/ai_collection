---
name: coupled-neural-field-consolidation
description: 'Model memory consolidation using coupled neural fields with hippocampus-neocortex interactions, neurogenesis, and distance-dependent synaptic plasticity. Based on Standard Consolidation Theory.'
---

# Coupled Neural Field Model for Memory Consolidation

## Description

A neural field framework modeling the Standard Consolidation Theory where hippocampal short-term memories enable neocortical long-term memory consolidation. Incorporates adult neurogenesis, distance-dependent synaptic plasticity, spike frequency adaptation, and coupled neural field dynamics.

**Source:** arXiv:2404.02938v1
**Utility:** 0.91

## Activation Keywords

- memory consolidation model
- coupled neural fields
- hippocampus neocortex
- standard consolidation theory
- neurogenesis dentate gyrus
- bump attractor memory
- distance-dependent plasticity

## Core Concepts

### 1. Standard Consolidation Theory

```
Hippocampus (fast learning, short-term) → Neocortex (slow learning, long-term)
```

**Key principles:**
- Hippocampus quickly encodes unstable memories
- Neocortex slowly consolidates long-term memories
- Hippocampus provides transient support during consolidation
- After consolidation, neocortex can retrieve without hippocampus

### 2. Neurobiological Mechanisms

| Mechanism | Role |
|-----------|------|
| **Adult neurogenesis** | Dentate gyrus generates new neurons, perturbs hippocampal patterns |
| **Distance-dependent plasticity** | Size difference between neocortex and hippocampus |
| **Synaptic depression** | Short-term plasticity mechanism |
| **Spike frequency adaptation** | Neural adaptation over time |
| **Hippocampal replay** | Periodic reactivation during consolidation |

### 3. Coupled Neural Field Framework

**Architecture:**
- Separate neural fields for hippocampus and neocortex
- Intra-area connections (within each field)
- Inter-area connections (between fields)
- Multiple bump attractor patterns

### 4. Memory Pattern Dynamics

| Phase | Description |
|-------|-------------|
| **Encoding** | Input pattern encoded as bump attractor |
| **Hippocampal storage** | Fast encoding in hippocampal field |
| **Consolidation** | Slow transfer to neocortical field |
| **Retrieval cue** | External input activates pattern |
| **Hippocampal replay** | Periodic reactivation supports consolidation |
| **Neocortical independence** | Pattern retrievable without hippocampus |
| **Hippocampal erasure** | Neurogenesis perturbs, erases hippocampal pattern |

### 5. Bump Attractor Dynamics

**Multiple bump attractor:**
- Encodes memory pattern as spatial bumps
- Bumps closer in hippocampus (smaller distances)
- Bumps farther in neocortex (larger distances)
- Distance affects learning rate

## Step-by-Step Instructions

### 1. Neural Field Model Implementation

```python
import numpy as np
from scipy.integrate import solve_ivp

class NeuralField:
    """
    Neural field with bump attractor dynamics.
    
    Args:
        space_size: Spatial domain size
        n_points: Number of discretization points
        tau: Time constant
        sigma: Spatial spread of connections
        threshold: Activation threshold
    """
    def __init__(self, space_size, n_points, tau, sigma, threshold):
        self.space_size = space_size
        self.n_points = n_points
        self.tau = tau
        self.sigma = sigma
        self.threshold = threshold
        
        # Spatial discretization
        self.x = np.linspace(0, space_size, n_points)
        self.dx = space_size / n_points
        
        # Connectivity kernel
        self.kernel = self._create_kernel()
        
        # State variable
        self.u = np.zeros(n_points)
        
    def _create_kernel(self):
        """
        Create Gaussian connectivity kernel.
        
        Returns:
            kernel: Connectivity matrix [n_points, n_points]
        """
        kernel = np.zeros((self.n_points, self.n_points))
        
        for i in range(self.n_points):
            for j in range(self.n_points):
                distance = np.abs(self.x[i] - self.x[j])
                # Periodic boundary
                distance = min(distance, self.space_size - distance)
                kernel[i, j] = np.exp(-distance**2 / (2 * self.sigma**2))
        
        return kernel
    
    def firing_rate(self, u):
        """
        Sigmoid firing rate function.
        
        Args:
            u: Neural activity
        
        Returns:
            f: Firing rate
        """
        return 1 / (1 + np.exp(-self.threshold * (u - 0.5)))
    
    def dynamics(self, t, u, external_input=None, adaptation=None):
        """
        Neural field dynamics.
        
        Args:
            t: Time
            u: Current state
            external_input: External input (optional)
            adaptation: Spike frequency adaptation (optional)
        
        Returns:
            du/dt: Rate of change
        """
        # Compute firing rate
        f = self.firing_rate(u)
        
        # Convolution with kernel
        convolution = np.dot(self.kernel, f) * self.dx
        
        # External input
        if external_input is not None:
            convolution += external_input
        
        # Spike frequency adaptation
        if adaptation is not None:
            convolution -= adaptation
        
        # Dynamics
        du_dt = (-u + convolution) / self.tau
        
        return du_dt
    
    def simulate(self, t_span, external_input=None, adaptation=None):
        """
        Simulate neural field dynamics.
        
        Args:
            t_span: Time span [t_start, t_end]
            external_input: External input function
            adaptation: Adaptation function
        
        Returns:
            solution: ODE solution
        """
        solution = solve_ivp(
            lambda t, u: self.dynamics(t, u, external_input, adaptation),
            t_span,
            self.u,
            method='RK45',
            dense_output=True
        )
        
        return solution
```

### 2. Coupled Neural Fields (Hippocampus-Neocortex)

```python
class CoupledNeuralFieldSystem:
    """
    Coupled neural field system for memory consolidation.
    
    Args:
        hippocampus_config: Hippocampal field config
        neocortex_config: Neocortical field config
        coupling_strength: Inter-area coupling strength
    """
    def __init__(self, hippocampus_config, neocortex_config, coupling_strength):
        # Create neural fields
        self.hippocampus = NeuralField(**hippocampus_config)
        self.neocortex = NeuralField(**neocortex_config)
        
        # Coupling
        self.coupling_strength = coupling_strength
        
        # Distance-dependent plasticity
        self.hippo_distances = self._compute_distances(
            hippocampus_config['space_size']
        )
        self.neo_distances = self._compute_distances(
            neocortex_config['space_size']
        )
        
    def _compute_distances(self, space_size):
        """
        Compute distance-dependent plasticity factor.
        
        Args:
            space_size: Spatial size
        
        Returns:
            distances: Distance matrix
        """
        # Smaller hippocampus → faster learning
        # Larger neocortex → slower learning
        return space_size
    
    def coupled_dynamics(self, t, state):
        """
        Coupled dynamics of hippocampus and neocortex.
        
        Args:
            t: Time
            state: Combined state [hippocampus, neocortex]
        
        Returns:
            dstate/dt: Rate of change
        """
        # Split state
        n_hippo = self.hippocampus.n_points
        u_hippo = state[:n_hippo]
        u_neo = state[n_hippo:]
        
        # Hippocampal dynamics with neocortical input
        neo_to_hippo = self.coupling_strength * self.neocortex.firing_rate(u_neo)
        du_hippo = self.hippocampus.dynamics(t, u_hippo, neo_to_hippo)
        
        # Neocortical dynamics with hippocampal input
        hippo_to_neo = self.coupling_strength * self.hippocampus.firing_rate(u_hippo)
        du_neo = self.neocortex.dynamics(t, u_neo, hippo_to_neo)
        
        # Scale by distance-dependent plasticity
        du_hippo *= 1 / self.hippo_distances  # Faster
        du_neo *= 1 / self.neo_distances  # Slower
        
        return np.concatenate([du_hippo, du_neo])
    
    def simulate(self, t_span, initial_pattern=None):
        """
        Simulate coupled system.
        
        Args:
            t_span: Time span
            initial_pattern: Initial memory pattern
        
        Returns:
            solution: ODE solution
        """
        if initial_pattern is not None:
            # Set initial pattern in hippocampus
            self.hippocampus.u = initial_pattern['hippocampus']
            self.neocortex.u = initial_pattern['neocortex']
        
        initial_state = np.concatenate([
            self.hippocampus.u,
            self.neocortex.u
        ])
        
        solution = solve_ivp(
            self.coupled_dynamics,
            t_span,
            initial_state,
            method='RK45',
            dense_output=True
        )
        
        return solution
```

### 3. Adult Neurogenesis Model

```python
class NeurogenesisModel:
    """
    Adult neurogenesis in dentate gyrus.
    
    Args:
        neurogenesis_rate: Rate of new neuron generation
        perturbation_strength: Strength of perturbation
        hippocampus_field: Hippocampal neural field
    """
    def __init__(self, neurogenesis_rate, perturbation_strength, hippocampus_field):
        self.rate = neurogenesis_rate
        self.perturbation_strength = perturbation_strength
        self.hippocampus = hippocampus_field
        
        # New neuron counter
        self.new_neurons = 0
        
    def perturbation(self, t):
        """
        Neurogenesis perturbation effect.
        
        Args:
            t: Time
        
        Returns:
            perturbation: Perturbation signal
        """
        # Periodic neurogenesis
        if t > 0 and int(t) % self.rate == 0:
            # New neurons perturb existing pattern
            perturbation = self.perturbation_strength * np.random.randn(
                self.hippocampus.n_points
            )
            self.new_neurons += 1
            return perturbation
        else:
            return np.zeros(self.hippocampus.n_points)
    
    def erasure_effect(self, t):
        """
        Gradual erasure of hippocampal pattern.
        
        Args:
            t: Time
        
        Returns:
            erasure: Erasure factor (0 to 1)
        """
        # Neurogenesis gradually erases pattern
        erasure = np.exp(-self.new_neurons * self.perturbation_strength / 10)
        return erasure
```

### 4. Memory Pattern Encoding

```python
def encode_memory_pattern(space_size, n_points, pattern_positions):
    """
    Encode memory as multiple bump attractor pattern.
    
    Args:
        space_size: Spatial size
        n_points: Number of points
        pattern_positions: Positions of bumps
    
    Returns:
        pattern: Bump attractor pattern
    """
    pattern = np.zeros(n_points)
    x = np.linspace(0, space_size, n_points)
    
    for pos in pattern_positions:
        # Add Gaussian bump at position
        bump = np.exp(-(x - pos)**2 / 0.1)
        pattern += bump
    
    return pattern

def create_hippocampus_pattern(space_size_small, pattern_positions):
    """
    Create hippocampal memory pattern (smaller distances).
    
    Args:
        space_size_small: Smaller hippocampal space
        pattern_positions: Bump positions
    
    Returns:
        pattern: Hippocampal pattern
    """
    return encode_memory_pattern(space_size_small, 100, pattern_positions)

def create_neocortex_pattern(space_size_large, pattern_positions):
    """
    Create neocortical memory pattern (larger distances).
    
    Args:
        space_size_large: Larger neocortical space
        pattern_positions: Bump positions
    
    Returns:
        pattern: Neocortical pattern
    """
    return encode_memory_pattern(space_size_large, 200, pattern_positions)
```

### 5. Consolidation Simulation

```python
def simulate_consolidation(system, neurogenesis, t_encoding, t_consolidation, 
                           t_erasure, pattern_positions):
    """
    Full memory consolidation simulation.
    
    Args:
        system: Coupled neural field system
        neurogenesis: Neurogenesis model
        t_encoding: Encoding phase duration
        t_consolidation: Consolidation phase duration
        t_erasure: Erasure phase duration
        pattern_positions: Memory pattern positions
    
    Returns:
        results: Simulation results
    """
    results = {
        'encoding': None,
        'consolidation': None,
        'erasure': None,
        'timeline': []
    }
    
    # Phase 1: Encoding (hippocampus fast)
    print("Phase 1: Encoding in hippocampus...")
    
    hippo_pattern = create_hippocampus_pattern(
        system.hippocampus.space_size,
        pattern_positions
    )
    neo_pattern = create_neocortex_pattern(
        system.neocortex.space_size,
        pattern_positions
    )
    
    initial_pattern = {
        'hippocampus': hippo_pattern,
        'neocortex': neo_pattern * 0.1  # Initially weak in neocortex
    }
    
    results['encoding'] = system.simulate(
        [0, t_encoding],
        initial_pattern
    )
    
    results['timeline'].append({
        'phase': 'encoding',
        'time': t_encoding,
        'hippocampus_strength': np.max(system.hippocampus.u),
        'neocortex_strength': np.max(system.neocortex.u)
    })
    
    # Phase 2: Consolidation (replay + retrieval cue)
    print("Phase 2: Consolidation...")
    
    # Add hippocampal replay periods
    t_start = t_encoding
    t_end = t_encoding + t_consolidation
    
    for t_replay in range(int(t_start), int(t_end)):
        # Replay: periodic reactivation
        if t_replay % 10 == 0:  # Replay every 10 time units
            replay_input = hippo_pattern * 0.5
            system.hippocampus.u += replay_input
        
        # Short simulation step
        system.simulate([t_replay, t_replay + 1])
    
    results['consolidation'] = system.simulate(
        [t_start, t_end]
    )
    
    results['timeline'].append({
        'phase': 'consolidation',
        'time': t_end,
        'hippocampus_strength': np.max(system.hippocampus.u),
        'neocortex_strength': np.max(system.neocortex.u)
    })
    
    # Phase 3: Erasure (neurogenesis)
    print("Phase 3: Neurogenesis erasure...")
    
    t_start = t_end
    t_end = t_start + t_erasure
    
    for t_gen in range(int(t_start), int(t_end)):
        # Neurogenesis perturbation
        perturbation = neurogenesis.perturbation(t_gen)
        system.hippocampus.u += perturbation
        
        # Apply erasure effect
        erasure = neurogenesis.erasure_effect(t_gen)
        system.hippocampus.u *= erasure
        
        # Short simulation step
        system.simulate([t_gen, t_gen + 1])
    
    results['erasure'] = system.simulate(
        [t_start, t_end]
    )
    
    results['timeline'].append({
        'phase': 'erasure',
        'time': t_end,
        'hippocampus_strength': np.max(system.hippocampus.u),
        'neocortex_strength': np.max(system.neocortex.u)
    })
    
    return results
```

### 6. Analysis and Visualization

```python
import matplotlib.pyplot as plt

def analyze_consolidation_results(results):
    """
    Analyze consolidation simulation results.
    
    Args:
        results: Simulation results
    
    Returns:
        analysis: Analysis summary
    """
    timeline = results['timeline']
    
    # Track pattern strengths
    hippo_strengths = [t['hippocampus_strength'] for t in timeline]
    neo_strengths = [t['neocortex_strength'] for t in timeline]
    times = [t['time'] for t in timeline]
    
    analysis = {
        'hippocampus_evolution': hippo_strengths,
        'neocortex_evolution': neo_strengths,
        'consolidation_success': neo_strengths[-1] > hippo_strengths[-1],
        'timeline': timeline
    }
    
    # Plot evolution
    plt.figure(figsize=(10, 6))
    plt.plot(times, hippo_strengths, 'b-', label='Hippocampus')
    plt.plot(times, neo_strengths, 'r-', label='Neocortex')
    plt.xlabel('Time')
    plt.ylabel('Pattern Strength')
    plt.title('Memory Consolidation Dynamics')
    plt.legend()
    plt.grid(True)
    plt.savefig('consolidation_dynamics.png')
    
    return analysis

def check_neocortical_independence(system):
    """
    Check if neocortex can retrieve without hippocampus.
    
    Args:
        system: Coupled neural field system
    
    Returns:
        independence: Independence score
    """
    # Test retrieval without hippocampal support
    original_hippo = system.hippocampus.u.copy()
    
    # Zero out hippocampus
    system.hippocampus.u = np.zeros(system.hippocampus.n_points)
    
    # Simulate neocortex alone
    neo_initial = system.neocortex.u.copy()
    solution = system.neocortex.simulate([0, 10])
    
    # Check if neocortex maintains pattern
    final_pattern = solution.y[:, -1]
    independence = np.max(final_pattern) / np.max(neo_initial)
    
    # Restore hippocampus
    system.hippocampus.u = original_hippo
    
    return independence
```

## Tools Used

- `numpy` - Numerical computations
- `scipy` - ODE integration
- `matplotlib` - Visualization
- `exec` - Run simulations
- `read` - Load model parameters

## Example Use Cases

### 1. Basic Consolidation Simulation

```python
# Create coupled system
hippo_config = {
    'space_size': 1.0,  # Small hippocampus
    'n_points': 100,
    'tau': 0.1,  # Fast dynamics
    'sigma': 0.05,
    'threshold': 10
}

neo_config = {
    'space_size': 5.0,  # Large neocortex
    'n_points': 200,
    'tau': 1.0,  # Slow dynamics
    'sigma': 0.2,
    'threshold': 10
}

system = CoupledNeuralFieldSystem(
    hippo_config, neo_config, coupling_strength=0.3
)

# Neurogenesis
neurogenesis = NeurogenesisModel(
    neurogenesis_rate=50,
    perturbation_strength=0.1,
    hippocampus_field=system.hippocampus
)

# Simulate consolidation
results = simulate_consolidation(
    system, neurogenesis,
    t_encoding=20,
    t_consolidation=100,
    t_erasure=50,
    pattern_positions=[0.3, 0.5, 0.7]
)

# Analyze
analysis = analyze_consolidation_results(results)
print(f"Consolidation success: {analysis['consolidation_success']}")
```

### 2. Check Neocortical Independence

```python
# After consolidation, check if neocortex works alone
independence = check_neocortical_independence(system)
print(f"Neocortical independence: {independence:.2%}")
# Expected: > 80% after successful consolidation
```

### 3. Compare Learning Rates

```python
# Distance-dependent plasticity comparison
hippo_learning_rate = 1 / system.hippo_distances  # Fast
neo_learning_rate = 1 / system.neo_distances  # Slow

print(f"Hippocampus learning rate: {hippo_learning_rate}")
print(f"Neocortex learning rate: {neo_learning_rate}")
# Expected: Hippocampus >> Neocortex
```

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: Neural Field Model Implementation

## Examples

### Example 1: Basic Application

**User:** I need to apply Coupled Neural Field Model for Memory Consolidation to my analysis.

**Agent:** I'll help you apply coupled-neural-field-consolidation. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for coupled-neural-field-consolidation?

**Agent:** Let me search for the latest research and best practices...

## Related Skills

- `neuromodulated-synaptic-plasticity` - Synaptic plasticity mechanisms
- `spiking-mode-neural-networks` - Spiking dynamics
- `kuramoto-brain-network` - Oscillatory dynamics

## References

- Berry, H. (2024). "A Coupled Neural Field Model for the Standard Consolidation Theory" arXiv:2404.02938v1 [q-bio.NC]

---

**Created:** 2026-03-29 20:05
**Author:** Aerial (from arXiv:2404.02938v1)