---
name: causal-learning-neural-assemblies
description: "DIRECT mechanism for causal learning with neural assemblies - local plasticity-based directional learning without backpropagation. Enables neural assembly networks to internalize causal directionality through projection, local plasticity control, and sparse winner selection."
tags: ["neuroscience", "neural-assemblies", "causal-learning", "local-plasticity", "biologically-plausible"]
---

# Causal Learning with Neural Assemblies

This skill implements the DIRECT (DIRectional Edge Coupling/Training) mechanism for enabling neural assemblies to learn the direction of causal influence between variables using purely local plasticity operations.

## Overview

Neural assemblies are groups of neurons that fire together and strengthen through co-activation. This skill demonstrates how these assemblies can learn causal directionality—an ability not previously shown with traditional neural assembly approaches.

## Key Concepts

### Neural Assemblies
- **Definition**: Groups of neurons that exhibit coordinated firing patterns
- **Properties**: Strengthen through co-activation, form via Hebbian-like plasticity
- **Capabilities**: Classification, parsing, planning, and now **causal learning**

### DIRECT Mechanism

DIRECT enables directional learning through three core operations:

1. **Projection**: Source and target assemblies are connected via weighted projections
2. **Local Plasticity Control**: Adaptive gain modulation based on co-activation
3. **Sparse Winner Selection**: Winner-take-all dynamics for assembly activation

### Causal Direction Learning

Unlike correlation-based learning, DIRECT learns:
- **Directionality**: Which variable causes which
- **Asymmetric relations**: A → B is different from B → A
- **Intervention effects**: How manipulating one variable affects another

## When to Use

Use this skill when:
- Building biologically plausible neural networks
- Implementing causal inference without backpropagation
- Designing local-learning-based AI systems
- Modeling directional relationships in neural data
- Creating interpretable causal models

## Methodology

### Core Algorithm

```python
class NeuralAssembly:
    def __init__(self, size, threshold):
        self.neurons = np.zeros(size)
        self.threshold = threshold
        self.projections = {}  # Outgoing connections
        
    def activate(self, input_signal):
        """Sparse winner-take-all activation."""
        potentials = input_signal + self.neurons
        winners = potentials > self.threshold
        self.neurons = potentials * winners  # Sparse activation
        return self.neurons

class DIRECT:
    def __init__(self, learning_rate=0.01, gain_schedule="adaptive"):
        self.lr = learning_rate
        self.gain_schedule = gain_schedule
        
    def train_direction(self, source_assembly, target_assembly, 
                        coactivation_strength, direction="source_to_target"):
        """
        Train causal directionality between two assemblies.
        
        Args:
            source_assembly: Assembly representing potential cause
            target_assembly: Assembly representing potential effect
            coactivation_strength: Strength of joint activation
            direction: Direction of causal influence to learn
        """
        # Adaptive gain based on co-activation history
        gain = self.compute_adaptive_gain(source_assembly, target_assembly)
        
        # Directional plasticity update
        if direction == "source_to_target":
            # Strengthen source→target projection
            delta_w = gain * coactivation_strength * self.lr
            source_assembly.projections[target_assembly] += delta_w
        else:
            # Strengthen target→source projection
            delta_w = gain * coactivation_strength * self.lr
            target_assembly.projections[source_assembly] += delta_w
    
    def compute_adaptive_gain(self, assembly_a, assembly_b):
        """Compute adaptive gain based on activation history."""
        # Higher gain for less frequently co-activated pairs
        history_score = self.get_coactivation_history(assembly_a, assembly_b)
        return 1.0 / (1.0 + history_score)  # Inverse relationship
```

### Training Protocol

```python
class CausalAssemblyNetwork:
    def __init__(self):
        self.assemblies = {}
        self.direct = DIRECT()
        
    def add_assembly(self, name, size, threshold=0.5):
        """Add a new neural assembly."""
        self.assemblies[name] = NeuralAssembly(size, threshold)
        
    def train_causal_relation(self, source_name, target_name, 
                              observations, num_epochs=1000):
        """
        Train causal direction from observations.
        
        Args:
            source_name: Name of source assembly
            target_name: Name of target assembly
            observations: List of (source_pattern, target_pattern, temporal_order)
            num_epochs: Number of training iterations
        """
        source = self.assemblies[source_name]
        target = self.assemblies[target_name]
        
        for epoch in range(num_epochs):
            for source_pattern, target_pattern, temporal_order in observations:
                # Co-activation
                source.activate(source_pattern)
                target.activate(target_pattern)
                
                # Compute co-activation strength
                strength = np.dot(source.neurons, target.neurons)
                
                # Determine direction from temporal order
                if temporal_order == "source_first":
                    self.direct.train_direction(
                        source, target, strength, "source_to_target"
                    )
                elif temporal_order == "target_first":
                    self.direct.train_direction(
                        target, source, strength, "source_to_target"
                    )
```

## Implementation

### Step 1: Define Neural Assemblies

```python
import numpy as np
from typing import Dict, List, Tuple

class NeuralAssembly:
    """
    Neural assembly with sparse winner-take-all dynamics.
    
    Attributes:
        size: Number of neurons in assembly
        threshold: Activation threshold for winner selection
        activation: Current activation state
        projections: Dictionary of outgoing connections
    """
    
    def __init__(self, size: int, threshold: float = 0.5):
        self.size = size
        self.threshold = threshold
        self.activation = np.zeros(size)
        self.projections: Dict['NeuralAssembly', np.ndarray] = {}
        self.activation_history = []
        
    def activate(self, input_pattern: np.ndarray) -> np.ndarray:
        """
        Sparse winner-take-all activation.
        
        Args:
            input_pattern: Input activation pattern
            
        Returns:
            Activation vector after winner selection
        """
        # Combine with current activation (persistence)
        combined = input_pattern + 0.3 * self.activation
        
        # Winner-take-all: only top k neurons activate
        k = max(1, int(0.1 * self.size))  # 10% sparsity
        top_k_indices = np.argsort(combined)[-k:]
        
        self.activation = np.zeros_like(combined)
        self.activation[top_k_indices] = combined[top_k_indices]
        
        # Record history
        self.activation_history.append(self.activation.copy())
        
        return self.activation
    
    def project_to(self, target: 'NeuralAssembly', 
                   weight_matrix: np.ndarray = None):
        """Create projection to target assembly."""
        if weight_matrix is None:
            weight_matrix = np.random.randn(self.size, target.size) * 0.1
        self.projections[target] = weight_matrix
        
    def get_projection_output(self) -> Dict['NeuralAssembly', np.ndarray]:
        """Compute outputs through all projections."""
        outputs = {}
        for target, weights in self.projections.items():
            outputs[target] = self.activation @ weights
        return outputs
```

### Step 2: Implement DIRECT Learning

```python
class DIRECTLearner:
    """
    DIRECT (DIRectional Edge Coupling/Training) learner.
    
    Implements causal direction learning through local plasticity
    operations without backpropagation.
    """
    
    def __init__(self, 
                 learning_rate: float = 0.01,
                 gain_decay: float = 0.95,
                 min_gain: float = 0.1):
        self.lr = learning_rate
        self.gain_decay = gain_decay
        self.min_gain = min_gain
        self.coactivation_counts: Dict[Tuple, int] = {}
        self.gains: Dict[Tuple, float] = {}
        
    def train_causal_edge(self, 
                          source: NeuralAssembly,
                          target: NeuralAssembly,
                          temporal_order: str = "source_first",
                          coactivation_strength: float = None):
        """
        Train causal direction on a directed edge.
        
        Args:
            source: Source assembly (potential cause)
            target: Target assembly (potential effect)
            temporal_order: "source_first" or "target_first"
            coactivation_strength: Override strength computation
        """
        assembly_pair = (id(source), id(target))
        
        # Initialize gain if new pair
        if assembly_pair not in self.gains:
            self.gains[assembly_pair] = 1.0
            self.coactivation_counts[assembly_pair] = 0
        
        # Compute co-activation strength
        if coactivation_strength is None:
            coactivation_strength = np.dot(
                source.activation, 
                target.activation
            )
        
        # Get current adaptive gain
        current_gain = self.gains[assembly_pair]
        
        # Update based on temporal order
        if temporal_order == "source_first":
            # Source causes target: strengthen source→target
            if target in source.projections:
                delta = current_gain * coactivation_strength * self.lr
                source.projections[target] += delta
                
        elif temporal_order == "target_first":
            # Target causes source: strengthen target→source
            if source in target.projections:
                delta = current_gain * coactivation_strength * self.lr
                target.projections[source] += delta
        
        # Update adaptive gain (decreases with more co-activations)
        self.coactivation_counts[assembly_pair] += 1
        self.gains[assembly_pair] = max(
            self.min_gain,
            1.0 / (1 + 0.1 * self.coactivation_counts[assembly_pair])
        )
    
    def test_direction(self, source: NeuralAssembly, 
                       target: NeuralAssembly) -> Dict[str, float]:
        """
        Test learned causal direction.
        
        Returns:
            Dictionary with direction scores
        """
        forward_strength = 0.0
        backward_strength = 0.0
        
        if target in source.projections:
            forward_strength = np.linalg.norm(source.projections[target])
        if source in target.projections:
            backward_strength = np.linalg.norm(target.projections[source])
        
        total = forward_strength + backward_strength
        if total > 0:
            return {
                "source_to_target": forward_strength / total,
                "target_to_source": backward_strength / total,
                "direction": "source→target" if forward_strength > backward_strength else "target→source"
            }
        return {"direction": "undetermined"}
```

### Step 3: Build Causal Learning Network

```python
class CausalAssemblyNetwork:
    """
    Network of neural assemblies capable of causal learning.
    """
    
    def __init__(self):
        self.assemblies: Dict[str, NeuralAssembly] = {}
        self.learner = DIRECTLearner()
        self.observations = []
        
    def add_variable(self, name: str, assembly_size: int = 100):
        """Add a variable represented by a neural assembly."""
        self.assemblies[name] = NeuralAssembly(assembly_size)
        
    def connect(self, var_a: str, var_b: str, 
                bidirectional: bool = False):
        """Create connections between variable assemblies."""
        assembly_a = self.assemblies[var_a]
        assembly_b = self.assemblies[var_b]
        
        assembly_a.project_to(assembly_b)
        if bidirectional:
            assembly_b.project_to(assembly_a)
    
    def observe(self, var_a: str, var_b: str, 
                value_a: np.ndarray, value_b: np.ndarray,
                temporal_order: str):
        """
        Record an observation for causal learning.
        
        Args:
            var_a: First variable name
            var_b: Second variable name
            value_a: Activation pattern for variable A
            value_b: Activation pattern for variable B
            temporal_order: "a_first", "b_first", or "simultaneous"
        """
        self.observations.append({
            "var_a": var_a,
            "var_b": var_b,
            "value_a": value_a,
            "value_b": value_b,
            "temporal_order": temporal_order
        })
    
    def train(self, epochs: int = 100):
        """Train causal relations from observations."""
        for epoch in range(epochs):
            for obs in self.observations:
                # Activate assemblies
                assembly_a = self.assemblies[obs["var_a"]]
                assembly_b = self.assemblies[obs["var_b"]]
                
                assembly_a.activate(obs["value_a"])
                assembly_b.activate(obs["value_b"])
                
                # Determine temporal order for training
                if obs["temporal_order"] == "a_first":
                    order = "source_first"
                elif obs["temporal_order"] == "b_first":
                    order = "target_first"
                else:
                    continue  # Skip simultaneous
                
                # Train
                self.learner.train_causal_edge(
                    assembly_a, assembly_b, order
                )
    
    def infer_causality(self, var_a: str, var_b: str) -> Dict:
        """Infer causal direction between two variables."""
        assembly_a = self.assemblies[var_a]
        assembly_b = self.assemblies[var_b]
        
        return self.learner.test_direction(assembly_a, assembly_b)
```

## Usage Example

```python
# Create network
network = CausalAssemblyNetwork()

# Define variables (e.g., weather, ice cream sales)
network.add_variable("temperature", assembly_size=100)
network.add_variable("ice_cream_sales", assembly_size=100)

# Connect bidirectionally for learning
network.connect("temperature", "ice_cream_sales", bidirectional=True)

# Generate synthetic observations
np.random.seed(42)
for i in range(500):
    # Temperature affects ice cream sales (temperature comes first)
    temp_pattern = np.random.randn(100)
    sales_pattern = temp_pattern + np.random.randn(100) * 0.3
    
    network.observe(
        "temperature", "ice_cream_sales",
        temp_pattern, sales_pattern,
        temporal_order="a_first"
    )

# Train
network.train(epochs=50)

# Infer causality
result = network.infer_causality("temperature", "ice_cream_sales")
print(f"Causal direction: {result['direction']}")
# Output: Causal direction: source→target (temperature → ice_cream_sales)
```

## Advantages

1. **Biologically Plausible**: Uses only local plasticity, no backpropagation
2. **Interpretable**: Clear causal direction representation
3. **Efficient**: O(n) complexity per learning step
4. **Flexible**: Can learn from temporal patterns in data

## Limitations

1. **Requires Temporal Information**: Needs temporal ordering of events
2. **Sparse Activation**: Performance depends on winner-take-all parameters
3. **Assembly Structure**: Requires pre-defined assembly architecture

## References

- Paper: "Causal Learning with Neural Assemblies" (arXiv:2604.26919)
- Authors: Evangelia Kopadi, Dimitris Kalles
- Category: cs.LG, Published: 2026-04-29

## Related Skills

- `neural-assembly-learning`: General neural assembly operations
- `synaptic-plasticity`: Synaptic plasticity mechanisms
- `spiking-neural-networks`: SNN implementation techniques
