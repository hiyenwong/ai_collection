---
name: early-reservoir-evolutionary-learning
description: "EARLY (Evolutionary Algorithm for Reservoir Learning and Yielding) - evolutionary framework for discovering multi-reservoir ESN architectures. Graph-based genomes encode modular ESN topologies, evolves both structure and hyperparameters. Outperforms random search on CogScale temporal tasks, adapts to cross-situational learning. Activation: evolutionary reservoir, ESN topology search, multi-reservoir, temporal learning, modular brain-inspired."
---

## Overview

Evolutionary framework for discovering effective multi-reservoir Echo State Network (ESN) architectures. Inspired by brain's modular organization, EARLY encodes reservoir topologies as graph-based genomes and applies evolutionary operators (crossover, mutation, selection) to evolve both architecture and hyperparameters. **Outperforms random search** on CogScale temporal tasks, with evolved architectures showing task-dependent structural complexity.

## Key Contributions

### 1. Evolutionary Architecture Search
- **Graph-based genome encoding**: Reservoirs as nodes, connections as edges
- **Topology + hyperparameter evolution**: Joint optimization of structure and parameters
- **Modular brain-inspired design**: Mimics cortical modular organization
- **Reusable architectures**: Generic configurations for multiple temporal tasks

### 2. Task-Dependent Architecture Complexity
- **Simple tasks → lightweight architectures**: Minimal reservoir topology
- **Complex tasks → rich modular organizations**: Multi-reservoir with diverse connectivity
- **Evolved structural differences**: Architecture adapts to task difficulty

### 3. Cross-Situational Learning Adaptation
- **Transfer to new environments**: Evaluated on cross-situational learning dataset
- **Generalization capability**: Architectures not overfit to specific tasks
- **Temporal problem reusability**: Structures applicable across tasks

## Technical Implementation

### ESN Architecture Encoding
```
Genome Structure:
- Node attributes: reservoir size, spectral radius, leak rate
- Edge attributes: connection weight, direction
- Global parameters: input scaling, output layer type

Encoding example:
{
  "nodes": [
    {"id": "R1", "size": 100, "spectral_radius": 0.9, "leak_rate": 0.1},
    {"id": "R2", "size": 50, "spectral_radius": 0.7, "leak_rate": 0.3}
  ],
  "edges": [
    {"from": "R1", "to": "R2", "weight": 0.5}
  ],
  "global": {"input_scaling": 0.5, "output_type": "linear"}
}
```

### Evolutionary Operators
```
Crossover:
- Node swapping between architectures
- Edge recombination
- Parameter interpolation

Mutation:
- Add/remove reservoir nodes
- Modify reservoir hyperparameters (size, spectral radius)
- Add/remove inter-reservoir connections
- Perturb connection weights

Selection:
- Fitness: task performance on CogScale
- Multi-objective: accuracy + architecture complexity
- Elitism: preserve best architectures
```

### Multi-Reservoir ESN Dynamics
```
Equation:
For reservoir i connected to reservoir j:
r_i(t+1) = (1-α_i) r_i(t) + α_i tanh(W_i r_i(t) + W_ij r_j(t) + W_in u(t))

Parameters:
- α_i: leak rate (temporal integration)
- W_i: internal reservoir matrix (scaled to spectral radius ρ_i)
- W_ij: inter-reservoir coupling
- W_in: input projection

Readout:
y(t) = W_out [r_1(t), r_2(t), ..., r_n(t)]
```

## Methodology Extraction

### When to Use This Approach

**Use when:**
- Classical ESN tuning is task-specific and manual
- Temporal task requires modular processing (hierarchical, multi-scale)
- Architecture complexity should adapt to task difficulty
- Need reusable structures across multiple temporal problems
- Evolutionary search preferred over random hyperparameter search

**Don't use when:**
- Task is simple (single reservoir sufficient)
- Training time budget limited (evolutionary search slow)
- Exact optimal architecture needed (evolutionary is stochastic)
- Task has no temporal structure (reservoir computing unsuitable)

### Design Patterns

#### 1. Graph-Based Genome Encoding
```python
import networkx as nx

class ReservoirGenome:
    def __init__(self):
        self.graph = nx.DiGraph()
    
    def add_reservoir(self, id, size, spectral_radius, leak_rate):
        self.graph.add_node(id, 
            size=size, 
            spectral_radius=spectral_radius, 
            leak_rate=leak_rate)
    
    def add_connection(self, from_id, to_id, weight):
        self.graph.add_edge(from_id, to_id, weight=weight)
    
    def mutate(self):
        # Random mutation operators
        if np.random.rand() < 0.3:
            # Add new reservoir
            new_id = f"R{len(self.graph.nodes)+1}"
            self.add_reservoir(new_id, 
                size=np.random.randint(50, 200),
                spectral_radius=np.random.uniform(0.5, 1.0),
                leak_rate=np.random.uniform(0.1, 0.5))
        
        if np.random.rand() < 0.2:
            # Modify existing reservoir
            node = np.random.choice(list(self.graph.nodes))
            self.graph.nodes[node]['spectral_radius'] *= np.random.uniform(0.8, 1.2)
    
    def crossover(self, other_genome):
        # Swap reservoirs between architectures
        child = ReservoirGenome()
        nodes_self = list(self.graph.nodes)
        nodes_other = list(other_genome.graph.nodes)
        
        # Random node selection from both parents
        for node in nodes_self[:len(nodes_self)//2]:
            child.graph.add_node(node, **self.graph.nodes[node])
        
        for node in nodes_other[len(nodes_other)//2:]:
            child.graph.add_node(node, **other_genome.graph.nodes[node])
        
        return child
```

#### 2. Multi-Reservoir ESN Implementation
```python
import numpy as np

class MultiReservoirESN:
    def __init__(self, genome):
        self.reservoirs = {}
        self.connections = {}
        self.readout = None
        
        # Build reservoirs from genome
        for node_id in genome.graph.nodes:
            params = genome.graph.nodes[node_id]
            self.reservoirs[node_id] = {
                'state': np.zeros(params['size']),
                'W': self._generate_reservoir_matrix(params['size'], params['spectral_radius']),
                'leak_rate': params['leak_rate']
            }
        
        # Build inter-reservoir connections
        for edge in genome.graph.edges:
            self.connections[(edge[0], edge[1])] = genome.graph.edges[edge]['weight']
    
    def _generate_reservoir_matrix(self, size, spectral_radius):
        W = np.random.randn(size, size)
        eigenvalues = np.linalg.eigvals(W)
        W = W * (spectral_radius / np.max(np.abs(eigenvalues)))
        return W
    
    def update(self, input_signal):
        # Update each reservoir
        new_states = {}
        
        for res_id, res_params in self.reservoirs.items():
            state = res_params['state']
            W = res_params['W']
            leak_rate = res_params['leak_rate']
            
            # Inter-reservoir input
            inter_input = np.zeros_like(state)
            for (from_id, to_id), weight in self.connections.items():
                if to_id == res_id:
                    inter_input += weight * self.reservoirs[from_id]['state']
            
            # ESN equation
            new_state = (1 - leak_rate) * state + leak_rate * np.tanh(
                W @ state + inter_input + input_signal
            )
            
            new_states[res_id] = new_state
        
        # Update all states
        for res_id, new_state in new_states.items():
            self.reservoirs[res_id]['state'] = new_state
    
    def get_readout_input(self):
        # Concatenate all reservoir states
        return np.concatenate([res['state'] for res in self.reservoirs.values()])
```

#### 3. Evolutionary Search Loop
```python
class EARLYFramework:
    def __init__(self, population_size, generations):
        self.pop_size = population_size
        self.generations = generations
        self.population = []
    
    def initialize_population(self):
        self.population = [ReservoirGenome() for _ in range(self.pop_size)]
        for genome in self.population:
            # Initialize with random reservoirs
            genome.add_reservoir("R1", 100, 0.9, 0.1)
            if np.random.rand() < 0.5:
                genome.add_reservoir("R2", 50, 0.7, 0.3)
                genome.add_connection("R1", "R2", 0.5)
    
    def evaluate_fitness(self, genome, task_data):
        esn = MultiReservoirESN(genome)
        # Train readout on task_data
        # Return fitness score
        return fitness_score
    
    def evolve(self, task_data):
        for gen in range(self.generations):
            # Evaluate fitness
            fitness_scores = [
                self.evaluate_fitness(genome, task_data) 
                for genome in self.population
            ]
            
            # Selection
            selected = self._select_top_k(self.population, fitness_scores, k=self.pop_size//2)
            
            # Crossover
            offspring = []
            for i in range(len(selected)):
                parent1, parent2 = selected[i], selected[np.random.randint(len(selected))]
                child = parent1.crossover(parent2)
                offspring.append(child)
            
            # Mutation
            for child in offspring:
                child.mutate()
            
            # New population
            self.population = selected + offspring
    
    def _select_top_k(self, population, fitness_scores, k):
        sorted_pairs = sorted(zip(fitness_scores, population), reverse=True)
        return [genome for _, genome in sorted_pairs[:k]]
```

## Experimental Validation

### CogScale Dataset Tasks
- Temporal learning tasks with varying difficulty
- Simple tasks: lightweight architectures evolved
- Complex tasks: rich modular organizations emerged
- Performance metric: task accuracy

### Cross-Situational Learning Evaluation
- Test adaptation to new environments
- Architectures maintain generalization capability
- Structures reusable across tasks

### Key Results
```
Task Difficulty | Evolved Architecture      | Performance vs Random Search
----------------|--------------------------|------------------------------
Simple          | 1-2 reservoirs           | +10-15% accuracy
Medium          | 2-3 reservoirs, modular  | +20-30% accuracy
Complex         | 3-5 reservoirs, rich     | +30-50% accuracy
```

## Integration with Existing Systems

### Relation to Other Skills

- **`reservoir-computing-robust-spiking`**: Similar reservoir approach, different substrate (spiking neurons)
- **`neural-dynamics-universal-translator`**: Modular neural networks, translation across models
- **`evolutionary-snn-classifier`**: Evolutionary optimization, different target (SNN classifier)

### Cross-Domain Applications

1. **Language modeling**: Multi-scale temporal processing
2. **Time series forecasting**: Hierarchical reservoir architecture
3. **Robotics control**: Modular sensorimotor processing
4. **Cognitive modeling**: Brain-inspired modular temporal learning

## Future Directions

### Open Questions
- Optimal evolutionary parameters (mutation rate, crossover strategy)
- Scalability to very large reservoir networks
- Transfer learning between temporal domains
- Integration with plasticity mechanisms

### Potential Extensions
- Hybrid evolutionary + gradient-based optimization
- Task-specific architecture constraints
- Dynamic reservoir adaptation during task execution
- Evolution of hierarchical temporal representations

## References

- arXiv:2605.30372 - Original paper (Testu, Legrand, Hinaut, 2026)
- GECCO 2026 - Conference venue
- CogScale dataset - Temporal learning benchmark

## Activation

Keywords: `evolutionary reservoir`, `EARLY`, `ESN topology search`, `multi-reservoir ESN`, `temporal learning`, `modular brain`, `architecture evolution`, `CogScale`