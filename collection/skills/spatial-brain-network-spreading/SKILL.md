---
name: spatial-brain-network-spreading
description: 'Model spreading dynamics on spatially constrained brain networks. Use neuroimaging data to define cortical geometry. Investigate propagation speed through folded cortical surface. Apply to epileptic seizure modeling.'
---

# Spatial Brain Network Spreading Dynamics

## Description

A framework for modeling spreading dynamics on spatially constrained complex brain networks using neuroimaging data to accurately represent the folded cortical surface. Demonstrates that cortical geometry profoundly influences propagation speed of activation, with high relevance to epileptic seizure modeling.

**Source:** arXiv:1302.5331v1 (J. R. Soc. Interface 2013)
**Utility:** 0.90

## Activation Keywords

- spatial brain network
- spreading dynamics brain
- cortical geometry propagation
- epileptic seizure modeling
- spatially constrained network
- brain network propagation
- cortical surface folding
- activation spreading brain

## Core Concepts

### 1. Spatial Embedding Problem

**Issue with Standard Network Models:**
- Networks used in theoretical studies often bear little relation to spatial embedding
- Connectivity doesn't match actual neural networks
- Cortical folding structure is ignored

**Solution:**
- Use detailed neuroimaging data
- Define network with accurate spatial embedding
- Model folded cortical surface geometry

### 2. Spreading Dynamics

**Propagation Model:**
```
Activation spreads through network:
- Simple spreading rules
- Connectivity constraints
- Spatial geometry influence

Speed depends on:
- Network topology
- Spatial embedding
- Cortical folding patterns
```

**Key Finding:**
Cortical geometry profoundly influences propagation speed.

### 3. Epileptic Seizure Modeling

**Relevance:**
- Seizure propagation follows network pathways
- Spatial constraints affect spread patterns
- Physiological structure matters

**Warning:**
Studies omitting physiological network structure risk simplifying dynamics in potentially significant ways.

## Step-by-Step Instructions

### 1. Spatial Network Construction

```python
import numpy as np
import networkx as nx
from scipy.spatial import distance

class SpatialBrainNetwork:
    """
    Spatially constrained brain network from neuroimaging data.
    
    Args:
        cortical_surface: Cortical surface mesh data
        connectivity_matrix: Structural connectivity
        spatial_coords: 3D coordinates of nodes
    """
    def __init__(
        self,
        cortical_surface: np.ndarray,
        connectivity_matrix: np.ndarray,
        spatial_coords: np.ndarray
    ):
        self.surface = cortical_surface
        self.connectivity = connectivity_matrix
        self.coords = spatial_coords
        self.n_nodes = len(spatial_coords)
        
        # Build network
        self.graph = self._build_network()
        
    def _build_network(self) -> nx.Graph:
        """
        Build spatially embedded network.
        
        Returns:
            G: NetworkX graph with spatial attributes
        """
        G = nx.Graph()
        
        # Add nodes with spatial coordinates
        for i, coord in enumerate(self.coords):
            G.add_node(i, pos=coord)
        
        # Add edges from connectivity
        for i in range(self.n_nodes):
            for j in range(i + 1, self.n_nodes):
                if self.connectivity[i, j] > 0:
                    # Edge weight from connectivity
                    weight = self.connectivity[i, j]
                    # Spatial distance
                    spatial_dist = distance.euclidean(
                        self.coords[i], self.coords[j]
                    )
                    G.add_edge(i, j, 
                              weight=weight, 
                              distance=spatial_dist)
        
        return G
    
    def get_euclidean_distance_matrix(self) -> np.ndarray:
        """
        Compute Euclidean distance matrix between nodes.
        
        Returns:
            dist_matrix: Distance matrix (n_nodes x n_nodes)
        """
        dist_matrix = np.zeros((self.n_nodes, self.n_nodes))
        
        for i in range(self.n_nodes):
            for j in range(i + 1, self.n_nodes):
                dist = distance.euclidean(self.coords[i], self.coords[j])
                dist_matrix[i, j] = dist
                dist_matrix[j, i] = dist
        
        return dist_matrix
```

### 2. Spreading Dynamics Model

```python
class SpreadingDynamics:
    """
    Model activation spreading through spatial brain network.
    
    Args:
        network: SpatialBrainNetwork instance
        spreading_rate: Rate of activation spread
        threshold: Activation threshold
    """
    def __init__(
        self,
        network: SpatialBrainNetwork,
        spreading_rate: float = 0.1,
        threshold: float = 0.5
    ):
        self.network = network
        self.rate = spreading_rate
        self.threshold = threshold
        self.n_nodes = network.n_nodes
        
        # Activation state
        self.activation = np.zeros(self.n_nodes)
        self.activation_history = []
        
    def initialize_seed(self, seed_nodes: list):
        """
        Initialize activation at seed nodes.
        
        Args:
            seed_nodes: List of seed node indices
        """
        self.activation = np.zeros(self.n_nodes)
        self.activation[seed_nodes] = 1.0
        self.activation_history = [self.activation.copy()]
        
    def spreading_step(self) -> np.ndarray:
        """
        Execute one spreading step.
        
        Returns:
            new_activation: Updated activation state
        """
        new_activation = self.activation.copy()
        
        for i in range(self.n_nodes):
            if self.activation[i] > 0:
                # Spread to neighbors
                neighbors = list(self.network.graph.neighbors(i))
                for j in neighbors:
                    if self.activation[j] < self.threshold:
                        # Spreading rate modulated by spatial distance
                        edge_data = self.network.graph.edges[i, j]
                        spatial_factor = 1.0 / (1.0 + edge_data['distance'] * 0.01)
                        
                        spread = self.rate * spatial_factor * self.activation[i]
                        new_activation[j] += spread
        
        # Clip to [0, 1]
        new_activation = np.clip(new_activation, 0, 1)
        
        self.activation = new_activation
        self.activation_history.append(self.activation.copy())
        
        return self.activation
    
    def run_simulation(
        self,
        seed_nodes: list,
        n_steps: int = 100
    ) -> list:
        """
        Run spreading simulation.
        
        Args:
            seed_nodes: Initial activation seeds
            n_steps: Number of simulation steps
        
        Returns:
            history: List of activation states
        """
        self.initialize_seed(seed_nodes)
        
        for _ in range(n_steps):
            self.spreading_step()
            
            # Check if spreading complete
            if np.sum(self.activation) > 0.9 * self.n_nodes:
                break
        
        return self.activation_history
    
    def compute_propagation_speed(self) -> float:
        """
        Compute average propagation speed.
        
        Returns:
            speed: Propagation speed (nodes per step)
        """
        if len(self.activation_history) < 2:
            return 0.0
        
        speeds = []
        for t in range(1, len(self.activation_history)):
            prev_active = np.sum(self.activation_history[t-1] > self.threshold)
            curr_active = np.sum(self.activation_history[t] > self.threshold)
            speeds.append(curr_active - prev_active)
        
        return np.mean(speeds)
```

### 3. Comparison with Standard Networks

```python
class NetworkComparison:
    """
    Compare spatially constrained vs standard network models.
    
    Args:
        spatial_network: Spatially constrained network
        random_network: Standard random network
    """
    def __init__(
        self,
        spatial_network: SpatialBrainNetwork,
        random_network: nx.Graph
    ):
        self.spatial = spatial_network
        self.random = random_network
        
    def compare_propagation_speed(self, seed_nodes: list) -> dict:
        """
        Compare propagation speeds between networks.
        
        Args:
            seed_nodes: Seed nodes for activation
        
        Returns:
            comparison: Speed comparison results
        """
        # Spatial network spreading
        spatial_spreading = SpreadingDynamics(self.spatial)
        spatial_history = spatial_spreading.run_simulation(seed_nodes)
        spatial_speed = spatial_spreading.compute_propagation_speed()
        
        # Random network spreading (simplified)
        random_speed = self._estimate_random_speed()
        
        comparison = {
            'spatial_network_speed': spatial_speed,
            'random_network_speed': random_speed,
            'speed_ratio': spatial_speed / random_speed if random_speed > 0 else 0,
            'spatial_history': spatial_history
        }
        
        return comparison
    
    def _estimate_random_speed(self) -> float:
        """
        Estimate spreading speed on random network.
        
        Returns:
            speed: Estimated speed
        """
        # Simplified estimation
        n_edges = self.random.number_of_edges()
        n_nodes = self.random.number_of_nodes()
        avg_degree = 2 * n_edges / n_nodes if n_nodes > 0 else 0
        
        return avg_degree * 0.1
```

### 4. Epileptic Seizure Modeling

```python
class SeizurePropagationModel:
    """
    Model epileptic seizure propagation on spatial brain network.
    
    Args:
        network: SpatialBrainNetwork instance
        seizure_threshold: Threshold for seizure activity
    """
    def __init__(
        self,
        network: SpatialBrainNetwork,
        seizure_threshold: float = 0.7
    ):
        self.network = network
        self.seizure_threshold = seizure_threshold
        self.spreading = SpreadingDynamics(network)
        
    def simulate_seizure_onset(
        self,
        onset_region: int,
        duration: int = 200
    ) -> dict:
        """
        Simulate seizure propagation from onset region.
        
        Args:
            onset_region: Initial seizure focus
            duration: Simulation duration
        
        Returns:
            results: Seizure simulation results
        """
        # Initialize seizure at onset
        self.spreading.initialize_seed([onset_region])
        
        # Run propagation
        history = []
        seizure_regions = []
        
        for t in range(duration):
            activation = self.spreading.spreading_step()
            history.append(activation.copy())
            
            # Track regions exceeding seizure threshold
            seizure_active = np.where(activation > self.seizure_threshold)[0]
            seizure_regions.append(seizure_active)
        
        results = {
            'onset_region': onset_region,
            'duration': duration,
            'history': history,
            'seizure_regions': seizure_regions,
            'final_extent': len(seizure_regions[-1]),
            'propagation_speed': self.spreading.compute_propagation_speed()
        }
        
        return results
    
    def identify_critical_regions(self) -> list:
        """
        Identify critical regions for seizure propagation.
        
        Returns:
            critical_regions: List of critical node indices
        """
        critical_regions = []
        
        # Test each region as potential onset
        for region in range(self.network.n_nodes):
            results = self.simulate_seizure_onset(region, duration=50)
            
            # If seizure spreads to > 50% of network, region is critical
            if results['final_extent'] > 0.5 * self.network.n_nodes:
                critical_regions.append(region)
        
        return critical_regions
```

### 5. Complete Workflow

```python
def spatial_brain_network_workflow(
    cortical_data: np.ndarray,
    connectivity: np.ndarray,
    coords: np.ndarray,
    seed_regions: list
) -> dict:
    """
    Complete spatial brain network analysis workflow.
    
    Args:
        cortical_data: Cortical surface data
        connectivity: Structural connectivity matrix
        coords: Node coordinates
        seed_regions: Seed regions for activation
    
    Returns:
        results: Complete analysis results
    """
    # 1. Build spatial network
    network = SpatialBrainNetwork(cortical_data, connectivity, coords)
    
    # 2. Model spreading dynamics
    spreading = SpreadingDynamics(network)
    history = spreading.run_simulation(seed_regions)
    
    # 3. Compute propagation speed
    speed = spreading.compute_propagation_speed()
    
    # 4. Seizure modeling
    seizure_model = SeizurePropagationModel(network)
    seizure_results = seizure_model.simulate_seizure_onset(seed_regions[0])
    
    results = {
        'network_stats': {
            'n_nodes': network.n_nodes,
            'n_edges': network.graph.number_of_edges()
        },
        'spreading_speed': speed,
        'activation_history': history,
        'seizure_simulation': seizure_results
    }
    
    return results
```

## Tools Used

- `numpy` - Numerical computations
- `networkx` - Network analysis
- `scipy.spatial` - Spatial distance calculations
- `matplotlib` - Visualization

## Example Use Cases

### 1. Basic Spreading Simulation

```python
# Create spatial network
coords = np.random.rand(100, 3)  # 100 nodes in 3D
connectivity = np.random.rand(100, 100)
connectivity = (connectivity + connectivity.T) / 2  # Symmetric
connectivity[connectivity < 0.9] = 0  # Sparse

network = SpatialBrainNetwork(None, connectivity, coords)

# Run spreading
spreading = SpreadingDynamics(network)
history = spreading.run_simulation([0, 1, 2])  # Seed at first 3 nodes

print(f"Propagation speed: {spreading.compute_propagation_speed():.3f}")
```

### 2. Seizure Propagation

```python
# Model seizure
seizure = SeizurePropagationModel(network, seizure_threshold=0.7)
results = seizure.simulate_seizure_onset(onset_region=10, duration=100)

print(f"Seizure spread to {results['final_extent']} regions")
print(f"Propagation speed: {results['propagation_speed']:.3f}")
```

### 3. Critical Region Identification

```python
# Find critical regions
critical = seizure.identify_critical_regions()
print(f"Critical regions for seizure propagation: {critical}")
```

## Key Findings from Paper

1. **Cortical geometry profoundly influences propagation speed**
2. **Standard network models with same coarse statistics behave differently**
3. **Physiological network structure is essential for accurate modeling**
4. **High relevance to epileptic seizure event modeling**

## Instructions for Agents

1. **Understand the Request**: Analyze what the user needs related to this skill's domain.
2. **Search for Information**: Use web_search to find relevant papers or documentation.
3. **Apply the Framework**: Follow the methodology described in the skill's key concepts.
4. **Provide Results**: Summarize findings and actionable recommendations.
5. **Verify Accuracy**: Cross-check key facts before presenting to user.

## Examples

### Example 1: Basic Usage

**User:** How can I apply spatial-brain-network-spreading?

**Agent:** I'll help you understand and apply spatial-brain-network-spreading...

### Example 2: Advanced Application

**User:** What are the key considerations for spatial-brain-network-spreading?

**Agent:** Let me search for the latest research and best practices...

## Related Skills

- `brain-network-controllability` - Controllability of brain networks
- `kuramoto-brain-network` - Kuramoto model for brain dynamics
- `eeg-brain-connectivity-bci` - EEG connectivity analysis

## References

- Crofts, J. et al. (2013). "Spreading dynamics on spatially constrained complex brain networks" J. R. Soc. Interface 10(81), 20130016

---

**Created:** 2026-03-30 02:05
**Author:** Aerial (from arXiv:1302.5331v1)