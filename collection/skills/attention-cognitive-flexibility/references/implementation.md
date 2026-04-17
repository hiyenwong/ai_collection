# Attention-Based Cognitive Flexibility — Implementation Patterns

## 1. Multi-Task Environment as Graph

```python
import networkx as nx
import numpy as np

class MultiTaskEnvironment:
    """
    Multi-task environment where tasks are defined by combinations
    of two cue dimensions. The environment is characterized via
    graph-theory methods.
    """
    def __init__(self, cue_dim_1, cue_dim_2):
        """
        Args:
            cue_dim_1: Number of values for first cue dimension
            cue_dim_2: Number of values for second cue dimension
        """
        self.cue_dim_1 = cue_dim_1
        self.cue_dim_2 = cue_dim_2
        self.graph = nx.Graph()
        self._build_task_graph()
    
    def _build_task_graph(self):
        """
        Build graph where nodes are tasks and edges represent
        shared cue dimensions between tasks.
        """
        tasks = [(c1, c2) for c1 in range(self.cue_dim_1) 
                          for c2 in range(self.cue_dim_2)]
        
        for i, task_i in enumerate(tasks):
            self.graph.add_node(i, task=task_i)
            for j, task_j in enumerate(tasks):
                if i < j:
                    # Edge weight: number of shared cue dimensions
                    shared = sum(a == b for a, b in zip(task_i, task_j))
                    if shared > 0:
                        self.graph.add_edge(i, j, weight=shared)
    
    def connectivity_metrics(self):
        """Graph-theory based connectivity metrics."""
        return {
            'density': nx.density(self.graph),
            'avg_clustering': nx.average_clustering(self.graph),
            'avg_path_length': nx.average_shortest_path_length(self.graph),
            'degree_centrality': nx.degree_centrality(self.graph),
        }
    
    def task_input(self, task_id):
        """Generate input for a specific task."""
        c1, c2 = self.graph.nodes[task_id]['task']
        return np.array([c1, c2])
```

## 2. Gating-Based (Multiplicative) Attention Model

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class GatingAttentionModel(nn.Module):
    """
    Gating-based (multiplicative) attention model that decomposes tasks
    into components and sequentially allocates attention.
    """
    def __init__(self, n_components, component_dim, hidden_dim, output_dim):
        super().__init__()
        self.n_components = n_components
        self.component_dim = component_dim
        
        # Component-specific encoders
        self.component_encoders = nn.ModuleList([
            nn.Linear(component_dim, hidden_dim) 
            for _ in range(n_components)
        ])
        
        # Gating networks for each component
        self.gate_nets = nn.ModuleList([
            nn.Sequential(
                nn.Linear(component_dim, hidden_dim),
                nn.Sigmoid()
            ) for _ in range(n_components)
        ])
        
        # Output layer
        self.output_layer = nn.Linear(hidden_dim, output_dim)
    
    def forward(self, component_inputs):
        """
        Multiplicative gating: output = ∏ gate(c_i) * f(c_i)
        
        Args:
            component_inputs: List of tensors, one per component
            
        Returns:
            Output predictions
        """
        encoded = []
        gates = []
        
        for i, inp in enumerate(component_inputs):
            encoded_i = self.component_encoders[i](inp)
            gate_i = self.gate_nets[i](inp)
            encoded.append(encoded_i)
            gates.append(gate_i)
        
        # Sequential multiplicative gating
        # Each component's representation is gated by the product of all gates
        aggregated = torch.zeros_like(encoded[0])
        for enc, gate in zip(encoded, gates):
            # Multiplicative interaction
            aggregated += enc * gate
        
        return self.output_layer(aggregated)
    
    def sequential_attention(self, component_inputs, order=None):
        """
        Sequentially allocate attention to components.
        """
        if order is None:
            order = list(range(self.n_components))
        
        state = None
        for i in order:
            enc = self.component_encoders[i](component_inputs[i])
            gate = self.gate_nets[i](component_inputs[i])
            
            if state is None:
                state = enc * gate
            else:
                # Update state with new component
                state = state + enc * gate
        
        return self.output_layer(state)
```

## 3. Concatenation-Based Attention Model

```python
class ConcatenationAttentionModel(nn.Module):
    """
    Concatenation-based attention model that decomposes tasks
    via concatenation of component representations.
    """
    def __init__(self, n_components, component_dim, hidden_dim, output_dim):
        super().__init__()
        self.n_components = n_components
        
        # Component-specific encoders
        self.component_encoders = nn.ModuleList([
            nn.Linear(component_dim, hidden_dim) 
            for _ in range(n_components)
        ])
        
        # Attention over concatenated components
        self.attention = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.Tanh(),
            nn.Linear(hidden_dim, 1)
        )
        
        # Output layer
        self.output_layer = nn.Linear(hidden_dim, output_dim)
    
    def forward(self, component_inputs):
        """
        Concatenation-based attention.
        """
        encoded = []
        for i, inp in enumerate(component_inputs):
            encoded.append(self.component_encoders[i](inp))
        
        # Stack: [n_components, hidden_dim]
        stacked = torch.stack(encoded, dim=0)
        
        # Compute attention weights
        attn_weights = self.attention(stacked)  # [n_components, 1]
        attn_weights = F.softmax(attn_weights, dim=0)
        
        # Weighted sum
        aggregated = (stacked * attn_weights).sum(dim=0)
        
        return self.output_layer(aggregated)
```

## 4. Evaluation: Stability and Generalization

```python
def evaluate_cognitive_flexibility(model, env, train_tasks, test_tasks, n_epochs=100):
    """
    Systematically evaluate generalization and stability.
    
    Stability: retention of performance on learned tasks
    Generalization: performance on unseen tasks
    """
    # Training phase
    train_performances = []
    for epoch in range(n_epochs):
        for task_id in train_tasks:
            inp = env.task_input(task_id)
            target = get_task_target(task_id)
            pred = model(inp)
            loss = F.cross_entropy(pred, target)
            loss.backward()
            # ... optimizer step
        train_performances.append(evaluate_tasks(model, env, train_tasks))
    
    # Generalization: test on unseen tasks
    generalization_perf = evaluate_tasks(model, env, test_tasks)
    
    # Stability: re-evaluate on training tasks
    stability_perf = evaluate_tasks(model, env, train_tasks)
    
    return {
        'stability': stability_perf,
        'generalization': generalization_perf,
        'flexibility_score': stability_perf * generalization_perf
    }

def vary_environment_connectivity(env_configs):
    """
    Systematically vary environmental richness and task connectivity.
    """
    results = {}
    for config in env_configs:
        env = MultiTaskEnvironment(
            cue_dim_1=config['dim1'], 
            cue_dim_2=config['dim2']
        )
        connectivity = env.connectivity_metrics()
        results[config['name']] = {
            'connectivity': connectivity,
            'model_perf': evaluate_cognitive_flexibility(
                model=config['model'], 
                env=env,
                train_tasks=config['train'],
                test_tasks=config['test']
            )
        }
    return results
```

## 5. Comparison with MLP Baseline

```python
class MLPBaseline(nn.Module):
    """Standard multilayer perceptron for comparison."""
    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, output_dim)
        )
    
    def forward(self, x):
        return self.net(x)

def compare_models(attention_model, mlp_model, env, n_runs=10):
    """
    Compare attention-based models against MLP baselines
    across environments with varying task connectivity.
    """
    results = {'attention': [], 'mlp': []}
    
    for run in range(n_runs):
        # Evaluate both models
        attn_perf = evaluate_cognitive_flexibility(attention_model, env, ...)
        mlp_perf = evaluate_cognitive_flexibility(mlp_model, env, ...)
        
        results['attention'].append(attn_perf)
        results['mlp'].append(mlp_perf)
    
    return results
```

## References

- Paper: "Attention to task structure for cognitive flexibility" (2604.13281v1)
- NetworkX: https://networkx.org/
- PyTorch: https://pytorch.org/
