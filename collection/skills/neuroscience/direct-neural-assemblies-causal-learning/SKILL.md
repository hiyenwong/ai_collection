---
name: direct-neural-assemblies-causal-learning
description: "DIRECT (DIRectional Edge Coupling/Training) methodology for causal learning with neural assemblies using local plasticity. Enables neural assemblies to internalize causal directionality without backpropagation. Activation triggers: neural assemblies, causal learning, directional learning, local plasticity, DIRECT mechanism, synaptic asymmetry, explainable causality."
---

# DIRECT: Causal Learning with Neural Assemblies

> A mechanism enabling neural assemblies to internalize causal directionality through local plasticity, providing an "explainable by design" framework for causal inference.

## Metadata
- **Source**: arXiv:2604.26919v1
- **Authors**: Evangelia Kopadi, Dimitris Kalles
- **Published**: 2026-04-29
- **Category**: cs.LG (Machine Learning)

## Core Methodology

### Problem Statement
Neural assemblies (groups of neurons that fire together and strengthen through co-activation) have been established as computationally general substrates for classification, parsing, and planning. However, a critical gap remained: can neural assemblies learn the direction of causal influence between variables?

### DIRECT Framework

The DIRECT mechanism leverages three inherent operations of neural assemblies:

1. **Projection**: Forward signal propagation through assembly connectivity
2. **Local Plasticity Control**: Hebbian-like weight updates based on co-activation
3. **Sparse Winner Selection**: Competition-based activation of dominant neurons

#### Key Innovation: Directional Learning

DIRECT co-activates source and target assemblies under an adaptive gain schedule to internalize directed relations:

```
Source Assembly → [Projection + Gain Modulation] → Target Assembly
                    ↓
              Synaptic Strengthening (Asymmetric)
```

### Mechanism Components

#### 1. Adaptive Gain Schedule
```python
# Pseudocode representation
def adaptive_gain(source_assembly, target_assembly, causality_strength):
    """
    Modulate connection strength based on temporal causality.
    Source activation preceding target activation → strengthen
    Reverse temporal order → weaken or no change
    """
    gain = sigmoid(causality_strength - threshold)
    return gain * learning_rate
```

#### 2. Directional Edge Coupling
- Forward connections (source → target) are strengthened when source precedes target
- Reverse connections are not strengthened (asymmetry emerges naturally)
- This temporal asymmetry encodes causal direction

#### 3. Dual-Readout Validation

The framework provides two complementary validation metrics:

##### (i) Synaptic-Strength Asymmetry
```python
asymmetry_score = (W_forward - W_reverse) / (W_forward + W_reverse + epsilon)
```
- Measures emergent weight gap between forward and reverse links
- High asymmetry indicates clear causal direction learned

##### (ii) Functional Propagation Overlap
- Quantifies reliability of directional signal flow
- Measures consistency of activation patterns along causal paths

## Implementation Guide

### Prerequisites
- Python 3.8+
- NumPy for matrix operations
- Basic understanding of Hebbian learning and neural dynamics

### Step-by-Step Implementation

#### Step 1: Assembly Initialization
```python
import numpy as np

class NeuralAssembly:
    """Represents a group of co-activating neurons."""
    
    def __init__(self, size, activation_threshold=0.5):
        self.size = size
        self.neurons = np.zeros(size)
        self.threshold = activation_threshold
        self.weights = np.random.randn(size, size) * 0.01
        
    def activate(self, input_signal):
        """Sparse winner selection."""
        potentials = np.dot(self.weights, input_signal)
        # k-winners-take-all
        top_k = np.argsort(potentials)[-int(self.size * 0.1):]
        self.neurons.fill(0)
        self.neurons[top_k] = potentials[top_k]
        return self.neurons
```

#### Step 2: DIRECT Learning Rule
```python
class DIRECTMechanism:
    """Directional Edge Coupling/Training mechanism."""
    
    def __init__(self, learning_rate=0.01, gain_decay=0.95):
        self.lr = learning_rate
        self.gain_decay = gain_decay
        self.cumulative_gain = 0
        
    def update(self, source_assembly, target_assembly, temporal_order):
        """
        Update weights based on directional co-activation.
        
        Args:
            source_assembly: Activating assembly
            target_assembly: Target assembly
            temporal_order: +1 if source precedes target, -1 if reverse, 0 if simultaneous
        """
        # Adaptive gain based on temporal causality
        if temporal_order > 0:
            self.cumulative_gain = (self.cumulative_gain * self.gain_decay + 
                                   temporal_order * (1 - self.gain_decay))
        
        # Hebbian update with directional modulation
        delta_w = np.outer(target_assembly.neurons, source_assembly.neurons)
        
        # Apply directional gain
        if temporal_order > 0:
            delta_w *= self.cumulative_gain * self.lr
        elif temporal_order < 0:
            delta_w *= -0.1 * self.lr  # Weak anti-Hebbian for reverse
        else:
            delta_w *= 0  # No update for simultaneous
            
        return delta_w
```

#### Step 3: Causal Structure Learning
```python
class DIRECTCausalNetwork:
    """Network of assemblies learning causal structure."""
    
    def __init__(self, num_assemblies, assembly_size):
        self.assemblies = [NeuralAssembly(assembly_size) for _ in range(num_assemblies)]
        self.connections = {}  # (i,j) -> weight matrix
        
    def train_episode(self, observations, temporal_window=5):
        """
        Train on sequential observations.
        
        Args:
            observations: List of (time, active_assembly) pairs
            temporal_window: Time steps to consider for causality
        """
        for i, (t1, asm1) in enumerate(observations):
            for j, (t2, asm2) in enumerate(observations):
                if i != j and abs(t1 - t2) <= temporal_window:
                    temporal_order = np.sign(t2 - t1)
                    
                    # Get or initialize connection
                    if (asm1, asm2) not in self.connections:
                        self.connections[(asm1, asm2)] = np.random.randn(
                            self.assemblies[asm1].size,
                            self.assemblies[asm2].size
                        ) * 0.01
                    
                    # DIRECT update
                    updater = DIRECTMechanism()
                    delta = updater.update(
                        self.assemblies[asm1],
                        self.assemblies[asm2],
                        temporal_order
                    )
                    self.connections[(asm1, asm2)] += delta
```

#### Step 4: Validation Metrics
```python
class DIRECTValidator:
    """Dual-readout validation for causal learning."""
    
    def synaptic_asymmetry(self, connection_weights):
        """Calculate synaptic-strength asymmetry."""
        w_forward = np.mean(connection_weights)
        w_reverse = np.mean(connection_weights.T)  # Reverse direction
        
        asymmetry = (w_forward - w_reverse) / (abs(w_forward) + abs(w_reverse) + 1e-8)
        return asymmetry
    
    def propagation_overlap(self, source_assembly, target_assembly, trials=100):
        """Measure functional propagation reliability."""
        overlaps = []
        
        for _ in range(trials):
            # Activate source and propagate
            source_pattern = np.random.randn(source_assembly.size)
            source_assembly.activate(source_pattern)
            
            # Measure target response
            target_response = target_assembly.activate(source_assembly.neurons)
            
            # Check consistency
            overlaps.append(np.corrcoef(source_assembly.neurons, target_response)[0,1])
        
        return np.mean(overlaps), np.std(overlaps)
```

## Applications

### 1. Causal Discovery from Time Series
- Learn causal graphs from sequential data without backpropagation
- Auditable causal claims at the synaptic level

### 2. Explainable AI Systems
- "Explainable by design" framework where causal claims trace to specific neural winners
- Mechanism-level auditability for safety-critical applications

### 3. Biological Plausibility Studies
- Bridge between biologically plausible neural dynamics and formal causal models
- Test hypotheses about biological neural assemblies encoding causality

### 4. Neuromorphic Causal Inference
- Implement on neuromorphic hardware for energy-efficient causal reasoning
- Local plasticity suitable for edge deployment

## Theoretical Properties

### Convergence Guarantees
- Under supervised known-structure settings: perfect structural recovery
- Asymmetric weight matrices emerge naturally from temporal ordering

### Biological Plausibility
- Uses only local Hebbian-like plasticity
- No backpropagation required
- Sparse winner selection matches observed cortical dynamics

### Explainability
- Causal claims traceable to specific neural assemblies
- Synaptic asymmetry provides direct evidence of learned direction
- Functional propagation quantifies confidence in causal relations

## Pitfalls

### 1. Temporal Resolution Sensitivity
- Requires sufficiently fine temporal resolution to detect precedence
- Coarse time bins may miss causal ordering

### 2. Latent Confounders
- May conflate indirect causation with direct causation
- Requires careful experimental design or additional validation

### 3. Assembly Definition
- Predefined assembly structure required
- Dynamic assembly formation is future work

### 4. Scale Limitations
- Current demonstrations on moderate-scale networks
- Large-scale causal graphs may require hierarchical organization

## Related Skills
- causal-learning-neural-assemblies: Related work on neural assembly causality
- spiking-neural-network-analysis: Analysis of SNN dynamics
- neuromorphic-computing: Hardware implementations
- synaptic-plasticity-rules: Various plasticity mechanisms

## References
- Kopadi, E., & Kalles, D. (2026). Causal Learning with Neural Assemblies. arXiv:2604.26919v1
- Related: Neural assembly theory, Hebbian learning, causal inference literature

## Example Workflow

```python
# Complete example of using DIRECT

# 1. Create assemblies
source = NeuralAssembly(size=100)
target = NeuralAssembly(size=100)

# 2. Initialize DIRECT
direct = DIRECTMechanism(learning_rate=0.01)

# 3. Simulate causal observations
causal_pairs = []
for t in range(1000):
    # Source causes target with 70% probability
    if np.random.random() < 0.7:
        source.activate(np.random.randn(100))
        time.sleep(0.01)  # Small delay
        target.activate(source.neurons + np.random.randn(100)*0.1)
        causal_pairs.append((source, target, +1))  # Forward causation
    else:
        # Random activation
        source.activate(np.random.randn(100))
        target.activate(np.random.randn(100))

# 4. Train
for src, tgt, order in causal_pairs:
    direct.update(src, tgt, order)

# 5. Validate
validator = DIRECTValidator()
asymmetry = validator.synaptic_asymmetry(connection_weights)
print(f"Learned asymmetry: {asymmetry:.3f}")  # Should be close to 1.0
```

## Key Takeaways

1. **Novelty**: First demonstration of neural assemblies learning causal directionality
2. **Mechanism**: Local plasticity + sparse winners + temporal ordering = causal learning
3. **Explainability**: Causal claims auditable at the mechanism level
4. **Efficiency**: No backpropagation required, suitable for neuromorphic hardware
