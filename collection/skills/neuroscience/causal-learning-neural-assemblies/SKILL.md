---
name: causal-learning-neural-assemblies
description: Causal Learning with Neural Assemblies methodology. Demonstrates how groups of co-activated neurons can learn direction of causal influence between variables. Uses DIRECT mechanism - Differential Interassembly Connection Reconfiguration through Event-triggered Consolidation and Transient dynamics. Applicable to neural causal inference, assembly-based learning, biological neural networks. Triggers - causal learning, neural assemblies, causality, neural dynamics, brain networks.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [causal-learning, neural-assemblies, causality, neural-dynamics, brain-networks, neuroscience, synaptic-plasticity]
    source_paper: "Causal Learning with Neural Assemblies (arXiv:2604.26919v1)"
    citations: 0
    published: 2026-04-29
---

# Causal Learning with Neural Assemblies

## Overview
Can Neural Assemblies - groups of neurons that fire together and strengthen through co-activation - learn the direction of causal influence between variables? While established as a computationally general substrate for classification, parsing, and planning, neural assemblies have not yet been shown to internalize causal directionality. This methodology demonstrates that the inherent operations of neural assemblies can encode and represent causal relationships.

## Core Concept: Neural Assemblies

### Definition
A **Neural Assembly** is a group of neurons that:
- Fire together in temporal synchrony
- Strengthen their connections through co-activation (Hebbian plasticity)
- Form stable, recurring activation patterns
- Represent functional units of information processing

### Properties
- **Self-organization**: Assemblies emerge from activity-dependent plasticity
- **Distributed representation**: Information encoded across populations
- **Transient dynamics**: Rapid formation and dissolution
- **Hierarchical organization**: Assemblies can contain sub-assemblies

## The DIRECT Mechanism

**D**ifferential **I**nterassembly **C**onnection **R**econfiguration through **E**vent-triggered **C**onsolidation and **T**ransient dynamics

### Key Insight
When two assemblies A and B are causally related (A → B):
- Activity in A **predicts** activity in B
- Synaptic connections from A to B strengthen based on this prediction
- The asymmetry in connection strength encodes causal direction

### Three-Stage Process

```python
class DIRECTMechanism:
    """
    Implementation of the DIRECT causal learning mechanism
    using neural assemblies.
    """
    def __init__(self, assembly_size=100, learning_rate=0.01):
        self.assembly_size = assembly_size
        self.lr = learning_rate
        self.assemblies = {}
        self.inter_assembly_weights = {}
        
    def create_assembly(self, name, neurons):
        """Create a neural assembly representing a variable."""
        self.assemblies[name] = NeuralAssembly(neurons, name)
        return self.assemblies[name]
    
    def present_event(self, assembly_name, timestamp):
        """
        Record an event: an assembly was active at a given time.
        
        This represents observing that a variable took a particular value.
        """
        assembly = self.assemblies[assembly_name]
        assembly.activate(timestamp)
        
        # Trigger transient dynamics in connected assemblies
        for other_name, connection in self.inter_assembly_weights.items():
            if assembly_name in connection:
                self.update_transient(assembly_name, other_name, timestamp)
    
    def update_transient(self, source, target, timestamp):
        """
        Update transient connection based on temporal relationship.
        
        If source activation consistently precedes target activation,
        strengthen the connection (evidence for causation).
        """
        source_assembly = self.assemblies[source]
        target_assembly = self.assemblies[target]
        
        # Look for temporal precedence patterns
        source_times = source_assembly.get_activation_times()
        target_times = target_assembly.get_activation_times()
        
        # Calculate temporal contingency
        contingency = self.calculate_contingency(
            source_times, target_times, 
            window_ms=50  # 50ms integration window
        )
        
        # Update connection weight based on contingency
        if (source, target) not in self.inter_assembly_weights:
            self.inter_assembly_weights[(source, target)] = 0.0
        
        # Hebbian update: strengthen if source predicts target
        current_weight = self.inter_assembly_weights[(source, target)]
        self.inter_assembly_weights[(source, target)] += self.lr * contingency
    
    def consolidate(self):
        """
        Consolidate transient dynamics into stable causal representations.
        
        Called periodically (analogous to sleep in biological systems).
        """
        for (source, target), weight in self.inter_assembly_weights.items():
            if weight > self.consolidation_threshold:
                # Stabilize the causal link
                self.assemblies[source].add_stable_output(target, weight)
                self.assemblies[target].add_stable_input(source, weight)
    
    def read_causal_direction(self, var_a, var_b):
        """
        Read the learned causal direction between two variables.
        
        Returns:
            'A→B' if A causes B
            'B→A' if B causes A  
            'A↔B' if bidirectional
            'A⊥B' if independent
        """
        weight_ab = self.inter_assembly_weights.get((var_a, var_b), 0)
        weight_ba = self.inter_assembly_weights.get((var_b, var_a), 0)
        
        threshold = 0.5  # Causal strength threshold
        
        if weight_ab > threshold and weight_ba > threshold:
            return f'{var_a}↔{var_b}'  # Bidirectional
        elif weight_ab > threshold:
            return f'{var_a}→{var_b}'  # A causes B
        elif weight_ba > threshold:
            return f'{var_b}→{var_a}'  # B causes A
        else:
            return f'{var_a}⊥{var_b}'  # Independent
```

## Biological Plausibility

### Synaptic Mechanisms
The DIRECT mechanism maps to known biological processes:

1. **STDP (Spike-Timing-Dependent Plasticity)**
   - Pre-before-post firing → synaptic potentiation
   - Post-before-pre firing → synaptic depression
   - Natural encoding of temporal causality

2. **NMDA Receptor Activation**
   - Requires postsynaptic depolarization
   - Acts as "coincidence detector"
   - Implements Hebbian learning rule

3. **Short-Term Plasticity**
   - Facilitation: repeated stimulation strengthens response
   - Depression: sustained activity weakens response
   - Enables temporal filtering

### Assembly Dynamics

```python
class NeuralAssembly:
    """
    Biologically-inspired neural assembly implementation.
    """
    def __init__(self, neurons, name):
        self.neurons = neurons  # Set of neuron indices
        self.name = name
        self.activation_history = []
        self.synaptic_weights = np.ones((len(neurons), len(neurons))) * 0.1
        self.external_outputs = {}  # To other assemblies
        
    def activate(self, timestamp, input_strength=1.0):
        """
        Activate the assembly (e.g., due to external input).
        """
        # Record activation
        self.activation_history.append(timestamp)
        
        # Trigger recurrent dynamics
        self.recurrent_activation(input_strength)
        
    def recurrent_activation(self, initial_strength):
        """
        Simulate recurrent dynamics within the assembly.
        
        Excitatory connections amplify and sustain activity.
        """
        activity = np.ones(len(self.neurons)) * initial_strength
        
        # Recurrent amplification
        for _ in range(10):  # Integration steps
            activity = np.tanh(self.synaptic_weights @ activity)
        
        return activity
    
    def strengthen_internal_connections(self):
        """
        Strengthen connections between co-active neurons (Hebbian).
        """
        # When assembly activates, strengthen internal connections
        for i in range(len(self.neurons)):
            for j in range(len(self.neurons)):
                if i != j:
                    self.synaptic_weights[i, j] += 0.01
        
        # Normalize to prevent runaway excitation
        self.synaptic_weights = np.clip(self.synaptic_weights, 0, 1)
```

## Applications

### 1. Causal Discovery
Learn causal structure from observational data:
```python
# Example: Learning causal structure of a system
learner = DIRECTMechanism()

# Create assemblies for variables
learner.create_assembly("rain", range(0, 100))
learner.create_assembly("sprinkler", range(100, 200))
learner.create_assembly("wet_grass", range(200, 300))

# Present observational data
for observation in data:
    if observation['rain']:
        learner.present_event("rain", observation['time'])
    if observation['sprinkler']:
        learner.present_event("sprinkler", observation['time'])
    if observation['wet_grass']:
        learner.present_event("wet_grass", observation['time'])

# Read learned causal structure
causal_structure = learner.read_causal_direction("rain", "wet_grass")
# Expected: "rain→wet_grass"
```

### 2. Predictive Processing
Use learned causality for prediction:
```python
# Given current state, predict future states
current_active = ["rain"]
predicted = learner.predict_next_assemblies(current_active, steps=3)
# Returns: ["wet_grass"] (and potentially others)
```

### 3. Intervention Planning
Determine optimal interventions based on causal structure:
```python
# "What should I do to make grass dry?"
intervention = learner.plan_intervention(target="wet_grass", desired_state=False)
# Returns: intervene on "sprinkler" (turn off) or "rain" (not controllable)
```

## Comparison with Traditional Methods

| Aspect | Traditional Causal Discovery | Neural Assembly DIRECT |
|--------|------------------------------|------------------------|
| Representation | Statistical variables | Distributed neural patterns |
| Learning | Optimization algorithms | Emergent from plasticity |
| Biological Basis | Abstract | Grounded in neural mechanisms |
| Scalability | Limited by combinatorics | Parallel distributed processing |
| Online Learning | Requires batch retraining | Continuous, incremental |

## Experimental Predictions

The theory makes testable predictions:

1. **Temporal Asymmetry**: Assemblies should show stronger causal encoding for forward vs. backward temporal relationships
2. **Consolidation Effect**: Sleep/quiet periods should improve causal learning
3. **Interference**: Simultaneous learning of conflicting causal structures should show interference patterns
4. **Generalization**: Learned causal structures should transfer to novel contexts

## Limitations

1. **Temporal Resolution**: Limited by synaptic dynamics (ms scale)
2. **Variable Cardinality**: Best for discrete/categorical variables
3. **Causal Strength**: May not capture precise effect sizes
4. **Confounding**: Sensitive to unobserved common causes

## References

- Causal Learning with Neural Assemblies, arXiv:2604.26919v1, 2026-04-29
- Authors: Evangelia Kopadi, Dimitris Kalles
- Categories: cs.LG, cs.AI, cs.NE

## Related Skills
- brain-network-controllability
- neural-population-dynamics
- stdp-synaptic-plasticity
- neural-code-dynamics-analysis
