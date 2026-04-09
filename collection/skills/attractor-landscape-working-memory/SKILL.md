# SKILL.md - Attractor Landscape Working Memory

## Activation Keywords

- attractor landscape, working memory, energy landscape brain
- multistable attractors, brain state transition, minimum action path
- distributed working memory, cortical hierarchy, memory stability
- landscape topography, kinetic transition path

## What It Does

Quantifies the multistable attractor landscape of distributed working memory in large-scale brain networks. Reveals how working memory function is governed by landscape topography and state transitions, with insights into memory stability and information flow through cortical hierarchy.

## When To Use

**Use this skill when:**
- Analyzing working memory in large-scale brain networks
- Quantifying attractor landscapes and state stability
- Modeling brain state transitions
- Understanding memory robustness to distractors
- Studying information flow through cortical hierarchy

**Do NOT use for:**
- Single-region memory models (no distributed network)
- Static connectivity analysis (no dynamics)
- Non-landscape based approaches

## How To Use

### Step-by-Step Workflow

1. **Construct Large-Scale Brain Network**
   - Anatomically constrained connectivity
   - Multiple cortical regions
   - Weighted directed graph

2. **Build Computational Model**
   - Neural population dynamics
   - Synaptic interactions
   - Stochastic noise

3. **Compute Energy Landscape**
   - Probability distribution of states
   - Energy = -log(P(state))
   - Identify attractors (energy minima)

4. **Quantify Attractor Properties**
   - Barrier heights (stability)
   - Basin sizes (attractor strength)
   - Transition rates

5. **Analyze Transition Paths**
   - Minimum action path (MAP)
   - Intermediate states
   - Information flow direction

### Key Concepts

**Attractor Landscape:**
- Energy minima = stable brain states
- Barriers = transition costs
- Basins = state accessibility

**Working Memory States:**
- Spontaneous state (rest)
- Memory state 1 (stimulus A)
- Memory state 2 (stimulus B)

**Landscape Topography:**
- Controls state stability
- Determines transition paths
- Influences memory robustness

### Mathematical Framework

**Energy landscape:**
```
E(x) = -log P(x)
```

**Barrier height:**
```
ΔE = E(saddle) - E(attractor)
```

**Minimum action path:**
```
S = ∫ L(x, ẋ) dt
```

## Example Usage

### Computing Attractor Landscape

**Problem:** Analyze working memory attractors in macaque cortex model

**Implementation:**
```python
import numpy as np
from scipy.optimize import minimize

class AttractorLandscapeWM:
    def __init__(self, connectivity_matrix, noise_level=0.1):
        self.W = connectivity_matrix
        self.noise = noise_level
        self.n_regions = connectivity_matrix.shape[0]
    
    def compute_landscape(self, n_samples=10000):
        """
        Compute energy landscape from network dynamics
        
        Returns:
        --------
        attractors : list of arrays
            Stable state configurations
        energies : array
            Energy of each state
        """
        # Sample from network dynamics
        states = self._sample_dynamics(n_samples)
        
        # Estimate probability distribution
        # (simplified - use kernel density in practice)
        hist, bins = self._estimate_distribution(states)
        
        # Compute energy
        energy = -np.log(hist + 1e-10)
        
        # Find attractors (local minima)
        attractors = self._find_attractors(energy, bins)
        
        return attractors, energy
    
    def compute_barrier_height(self, attractor1, attractor2):
        """
        Compute barrier height between two attractors
        """
        # Find saddle point on transition path
        saddle = self._find_saddle(attractor1, attractor2)
        
        # Barrier = saddle energy - attractor energy
        E1 = self._compute_energy(attractor1)
        E_saddle = self._compute_energy(saddle)
        
        return E_saddle - E1
    
    def minimum_action_path(self, attractor1, attractor2, n_steps=100):
        """
        Find minimum action path between attractors
        
        Uses geometric action minimization
        """
        # Initialize path
        path = np.linspace(attractor1, attractor2, n_steps)
        
        # Minimize action
        def action(path_flat):
            path = path_flat.reshape(n_steps, -1)
            # Geodesic action in state space
            velocities = np.diff(path, axis=0)
            action = np.sum(np.linalg.norm(velocities, axis=1)**2)
            return action
        
        result = minimize(action, path.flatten())
        optimal_path = result.x.reshape(n_steps, -1)
        
        return optimal_path
    
    def analyze_memory_stability(self, memory_state):
        """
        Analyze stability of memory state
        """
        # Barrier to spontaneous state
        barrier = self.compute_barrier_height(memory_state, self.spontaneous_state)
        
        # Robustness to noise
        robustness = barrier / self.noise
        
        # Basin size (approximation)
        basin = self._estimate_basin_size(memory_state)
        
        return {
            'barrier_height': barrier,
            'robustness': robustness,
            'basin_size': basin
        }
```

### Application to Distributed Working Memory

**Analysis:**
```python
# Load macaque cortex connectivity
connectivity = load_macaque_connectivity()  # (30, 30) regions

# Initialize landscape analyzer
analyzer = AttractorLandscapeWM(connectivity, noise_level=0.05)

# Compute landscape
attractors, energy = analyzer.compute_landscape()

print(f"Found {len(attractors)} attractors:")
for i, att in enumerate(attractors):
    print(f"  Attractor {i+1}: energy = {analyzer._compute_energy(att):.3f}")

# Analyze memory state stability
memory_state1 = attractors[1]  # Memory state for stimulus A
stability = analyzer.analyze_memory_stability(memory_state1)

print(f"\nMemory state stability:")
print(f"  Barrier height: {stability['barrier_height']:.3f}")
print(f"  Robustness: {stability['robustness']:.3f}")

# Find transition path between memory states
memory_state2 = attractors[2]  # Memory state for stimulus B
path = analyzer.minimum_action_path(memory_state1, memory_state2)

# Identify intermediate states
intermediate = path[len(path)//2]
print(f"\nIntermediate state during transition:")
print(f"  Closest attractor: spontaneous state")
```

## Key Findings from the Paper

1. **Three Stable Attractors:**
   - Spontaneous state (rest)
   - Two memory states (stimulus-specific)

2. **Memory Stability:**
   - Barrier height quantifies robustness
   - Higher cortical hierarchy → more stable memory

3. **Transition Dynamics:**
   - Spontaneous state as intermediate
   - Information flow follows hierarchy

## Description
Framework from arXiv papers. See paper reference for details.
## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents

1. **Understand the Request**: Analyze what the user needs related to this skill's domain.
2. **Search for Information**: Use web_search to find relevant papers or documentation.
3. **Apply the Framework**: Follow the methodology described in the skill's key concepts.
4. **Provide Results**: Summarize findings and actionable recommendations.
5. **Verify Accuracy**: Cross-check key facts before presenting to user.

## Examples

### Example 1: Basic Usage

**User:** How can I apply attractor-landscape-working-memory?

**Agent:** I'll help you understand and apply attractor-landscape-working-memory...

### Example 2: Advanced Application

**User:** What are the key considerations for attractor-landscape-working-memory?

**Agent:** Let me search for the latest research and best practices...

## Related Skills

- **neural-dynamics-decision-making** - Decision dynamics
- **attractor-metadynamics-neural** - Attractor dynamics
- **brain-network-controllability** - Network control

## Source

- arXiv:2209.05002v1
- Title: Quantifying the attractor landscape and transition path of distributed working memory from large-scale brain network
- Utility: 0.87
- Authors: Chunhe Li et al.

## Notes

- Key innovation: Energy landscape for distributed WM
- Based on macaque cortex anatomical model
- Three attractors: spontaneous + 2 memory states
- Barrier height quantifies memory stability
- Minimum action path reveals transition mechanism
- Applications: working memory, cognitive dynamics, brain state analysis

---

_Created: 2026-04-01_