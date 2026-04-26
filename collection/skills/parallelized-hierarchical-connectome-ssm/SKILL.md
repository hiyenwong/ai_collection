---
name: parallelized-hierarchical-connectome-ssm
description: "Parallelized Hierarchical Connectome (PHC) framework for spatiotemporal recurrent networks. Upgrades temporal-only State-Space Models (SSMs) into spatiotemporal recurrent networks with intra-slice spatial recurrence via Multi-Transmission Loop. Integrates neuro-physical priors including adaptive LIF dynamics, Dale's Law, short-term plasticity, and reward-modulated STDP. PHCSSM instantiation achieves O(logT) parallelism while enforcing biological constraints. Use when implementing biologically-constrained SSMs, spatiotemporal sequence modeling, parallel spiking neural networks, or brain-inspired recurrent architectures."
---

# Parallelized Hierarchical Connectome (PHC) for SSMs

## Overview

PHC is a general framework that upgrades temporal-only State-Space Models (SSMs) into spatiotemporal recurrent networks. By mapping SSM components to hierarchical brain-like structures, PHC enables parallel training while incorporating neuro-physical priors typically intractable for standard SSMs.

**Key Innovation:** Unifies recurrent spiking neural network dynamics with diagonal SSM parallelism while enforcing biological constraints.

**Paper:** arXiv:2604.01295v1 (April 2026)  
**Source:** Parallelized Hierarchical Connectome: A Spatiotemporal Recurrent Framework for Spiking State-Space Models

## Core Architecture

### PHC Component Mapping

```
Standard SSM          →    PHC Framework
─────────────────────────────────────────
Diagonal SSM Core     →    Shared Neuron Layer
Inter-SSM Connections →    Shared Synapse Layer
Temporal Scan         →    Multi-Transmission Loop
Input Projection      →    Sensory Pathway
Output Projection     →    Motor Pathway
```

### Hierarchical Organization

```
┌─────────────────────────────────────────────────────────────┐
│                 PHC Architecture                            │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐     │
│  │  Sensory    │───→│   Concept   │───→│  Category   │     │
│  │   Input     │    │    Layer    │    │   Layer     │     │
│  └─────────────┘    └─────────────┘    └─────────────┘     │
│         │                  │                  │              │
│         ↓                  ↓                  ↓              │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐     │
│  │   Neuron    │    │   Neuron    │    │   Neuron    │     │
│  │    Pool     │    │    Pool     │    │    Pool     │     │
│  │  (Layer 1)  │    │  (Layer 2)  │    │  (Layer 3)  │     │
│  └─────────────┘    └─────────────┘    └─────────────┘     │
│         ↑                  ↑                  ↑              │
│         └──────────────────┴──────────────────┘              │
│                    Synapse Layer                             │
│              (Connectome Topology)                           │
│                                                              │
│  Multi-Transmission Loop (Intra-slice recurrence)            │
│  ↳ Enables spatial propagation within temporal window        │
│  ↳ Preserves O(logT) parallelism                             │
└─────────────────────────────────────────────────────────────┘
```

## Biological Constraints

PHC enforces 5 key biological constraints:

| Constraint | Implementation | Biological Basis |
|------------|----------------|------------------|
| **Adaptive LIF Dynamics** | Membrane with adaptive threshold | Neuronal adaptation |
| **Dale's Law** | Separate E/I neuron populations | Neurophysiology |
| **Short-term Plasticity** | Dynamic synaptic weights | Tsodyks-Markram model |
| **STDP Learning** | Online spike-based learning | Synaptic plasticity |
| **Lateral Connectivity** | Within-layer connections | Cortical microcircuits |

### 1. Adaptive Leaky Integrate-and-Fire

```python
class AdaptiveLIF:
    """
    Adaptive LIF neuron with learnable parameters
    """
    def __init__(self, tau_m=20.0, tau_adapt=100.0):
        self.tau_m = tau_m          # Membrane time constant
        self.tau_adapt = tau_adapt  # Adaptation time constant
        self.v = 0.0                # Membrane potential
        self.theta = 1.0            # Adaptive threshold
    
    def step(self, I_syn, dt=1.0):
        # Membrane dynamics
        dv = (-self.v + I_syn) / self.tau_m * dt
        self.v += dv
        
        # Spike generation
        spike = (self.v >= self.theta)
        
        # Adaptation
        self.theta += (spike * 0.1 - (self.theta - 1.0) / self.tau_adapt) * dt
        
        # Reset
        if spike:
            self.v = 0.0
        
        return float(spike)
```

### 2. Dale's Law

```python
class DaleConstraint:
    """
    Enforces Dale's Law: neurons are either excitatory or inhibitory
    """
    def __init__(self, n_neurons, excitatory_ratio=0.8):
        self.n_neurons = n_neurons
        self.n_exc = int(n_neurons * excitatory_ratio)
        self.n_inh = n_neurons - self.n_exc
        
        # Create neuron type mask
        self.ei_mask = torch.ones(n_neurons)
        self.ei_mask[self.n_exc:] = -1  # Inhibitory neurons
    
    def apply(self, weights):
        """
        Apply Dale's Law constraint to weights
        
        Args:
            weights: Weight matrix [n_pre, n_post]
        
        Returns:
            constrained_weights: With correct sign per neuron
        """
        # Ensure excitatory weights are positive
        # Ensure inhibitory weights are negative
        return torch.abs(weights) * self.ei_mask.unsqueeze(0)
```

### 3. Short-term Plasticity

```python
class ShortTermPlasticity:
    """
    Tsodyks-Markram short-term plasticity model
    """
    def __init__(self, U=0.15, tau_d=200.0, tau_f=600.0):
        self.U = U          # Utilization factor
        self.tau_d = tau_d  # Depression time constant
        self.tau_f = tau_f  # Facilitation time constant
        
        # State variables
        self.R = 1.0        # Available resources
        self.u = 0.0        # Utilization
    
    def step(self, spike, dt=1.0):
        # Update utilization
        du = (self.U - self.u) / self.tau_f * dt
        if spike:
            du += self.U * (1 - self.u)
        self.u += du
        
        # Update resources
        dR = (1 - self.R) / self.tau_d * dt
        if spike:
            dR -= self.u * self.R
        self.R += dR
        
        # Effective weight
        return self.u * self.R
```

### 4. Reward-modulated STDP

```python
class RewardModulatedSTDP:
    """
    Reward-modulated spike-timing-dependent plasticity
    """
    def __init__(self, A_plus=0.01, A_minus=0.01, 
                 tau_plus=20.0, tau_minus=20.0):
        self.A_plus = A_plus
        self.A_minus = A_minus
        self.tau_plus = tau_plus
        self.tau_minus = tau_minus
        
        # Eligibility traces
        self.pre_trace = 0.0
        self.post_trace = 0.0
        self.eligibility = 0.0
    
    def pre_spike(self, dt=1.0):
        self.pre_trace += 1.0
        self.eligibility -= self.A_minus * self.post_trace
    
    def post_spike(self, dt=1.0):
        self.post_trace += 1.0
        self.eligibility += self.A_plus * self.pre_trace
    
    def update_traces(self, dt=1.0):
        self.pre_trace *= np.exp(-dt / self.tau_plus)
        self.post_trace *= np.exp(-dt / self.tau_minus)
    
    def apply_reward(self, reward, learning_rate=0.01):
        """Modulate plasticity by reward signal"""
        weight_change = learning_rate * reward * self.eligibility
        self.eligibility *= 0.9  # Decay eligibility
        return weight_change
```

## Activation Keywords

- parallelized hierarchical connectome
- PHC spatiotemporal SSM
- biological state space model
- spiking SSM
- connectome topology neural network
- dale's law neural network
- parallel spiking network training
- 层次化连接组
- 并行脉冲状态空间模型

## Workflow

### Phase 1: Connectome Design

**1.1 Define Hierarchy**
```python
connectome_config = {
    'regions': [
        {'name': 'sensory', 'n_neurons': 512, 'layer': 1},
        {'name': 'concept', 'n_neurons': 1024, 'layer': 2},
        {'name': 'category', 'n_neurons': 512, 'layer': 3},
        {'name': 'meta', 'n_neurons': 256, 'layer': 4},
    ],
    'intra_connectivity': 0.1,  # 10% within-region
    'inter_connectivity': 0.05,  # 5% between-regions
}
```

**1.2 Topology Construction**
```python
def build_connectome(config):
    """
    Build hierarchical connectome topology
    
    Args:
        config: Connectome configuration
    
    Returns:
        connectome: Graph structure with connections
    """
    G = nx.DiGraph()
    
    # Add neurons as nodes
    for region in config['regions']:
        for i in range(region['n_neurons']):
            node_id = f"{region['name']}_{i}"
            G.add_node(node_id, 
                      layer=region['layer'],
                      region=region['name'])
    
    # Add connections
    for region1 in config['regions']:
        for region2 in config['regions']:
            if region1['layer'] <= region2['layer']:
                # Feedforward + lateral connections
                p = config['intra_connectivity'] if region1 == region2 else config['inter_connectivity']
                
                for i in range(region1['n_neurons']):
                    for j in range(region2['n_neurons']):
                        if np.random.random() < p:
                            G.add_edge(f"{region1['name']}_{i}",
                                      f"{region2['name']}_{j}")
    
    return G
```

### Phase 2: SSM Mapping

**2.1 Diagonal SSM Core → Neuron Layer**
```python
class SharedNeuronLayer:
    """
    Maps diagonal SSM to shared neuron population
    """
    def __init__(self, connectome, neuron_type=AdaptiveLIF):
        self.connectome = connectome
        self.neurons = {}
        
        # Initialize neurons
        for node in connectome.nodes():
            self.neurons[node] = neuron_type()
    
    def step(self, inputs, dt=1.0):
        """
        Single timestep evolution
        
        Args:
            inputs: Input currents to each neuron
        
        Returns:
            spikes: Spike output from each neuron
        """
        spikes = {}
        for node, neuron in self.neurons.items():
            # Sum synaptic inputs
            I_syn = inputs.get(node, 0.0)
            
            # Neuron dynamics
            spikes[node] = neuron.step(I_syn, dt)
        
        return spikes
```

**2.2 Multi-Transmission Loop**
```python
class MultiTransmissionLoop:
    """
    Enables intra-slice spatial recurrence while preserving parallelism
    """
    def __init__(self, connectome, max_hops=3):
        self.connectome = connectome
        self.max_hops = max_hops
    
    def propagate(self, initial_activity, n_iterations):
        """
        Spatial propagation within a temporal window
        
        Args:
            initial_activity: Initial neural activity
            n_iterations: Number of propagation steps
        
        Returns:
            final_activity: Activity after spatial propagation
        """
        activity = initial_activity.copy()
        
        for _ in range(n_iterations):
            new_activity = {}
            for node in self.connectome.nodes():
                # Aggregate from neighbors
                neighbor_sum = sum(
                    activity.get(neighbor, 0.0) * weight
                    for neighbor, weight in 
                    self.connectome[node].items()
                )
                new_activity[node] = activity.get(node, 0.0) + neighbor_sum
            activity = new_activity
        
        return activity
```

### Phase 3: Parallel Training

**3.1 Parallel Scan Implementation**
```python
class ParallelSpikingSSM:
    """
    Parallelizable spiking SSM with biological constraints
    """
    def __init__(self, connectome, timesteps):
        self.connectome = connectome
        self.timesteps = timesteps
        self.neuron_layer = SharedNeuronLayer(connectome)
        self.synapse_layer = SharedSynapseLayer(connectome)
        self.mtl = MultiTransmissionLoop(connectome)
    
    def parallel_forward(self, sequence):
        """
        Parallel forward pass using associative scan
        
        Args:
            sequence: Input sequence [T, input_dim]
        
        Returns:
            outputs: Output sequence [T, output_dim]
        """
        T = len(sequence)
        
        # Phase 1: Encode inputs to initial activity
        activities = []
        for t in range(T):
            activity = self.encode_input(sequence[t])
            activities.append(activity)
        
        # Phase 2: Multi-transmission loops (parallel)
        activities = [
            self.mtl.propagate(act, n_iterations=3)
            for act in activities
        ]
        
        # Phase 3: SSM associative scan
        outputs = self.associative_scan(activities)
        
        return outputs
    
    def associative_scan(self, activities):
        """
        Parallel scan for logT complexity
        
        Implementation: Blelloch parallel prefix scan
        """
        # Up-sweep phase
        # ... (see SSM literature for implementation)
        
        # Down-sweep phase
        # ...
        
        return outputs
```

## PHCSSM: Complete Implementation

```python
class PHCSSM(nn.Module):
    """
    Complete PHC-based Spiking State-Space Model
    """
    def __init__(self, config):
        super().__init__()
        
        # Connectome
        self.connectome = build_connectome(config['connectome'])
        
        # Biological components
        self.neurons = SharedNeuronLayer(
            self.connectome,
            neuron_type=AdaptiveLIF
        )
        self.synapses = SharedSynapseLayer(
            self.connectome,
            with_stdp=True,
            with_stp=True
        )
        self.dale_constraint = DaleConstraint(
            n_neurons=config['n_neurons']
        )
        
        # Multi-transmission loop
        self.mtl = MultiTransmissionLoop(self.connectome)
        
        # Projections
        self.input_proj = nn.Linear(config['input_dim'], config['n_neurons'])
        self.output_proj = nn.Linear(config['n_neurons'], config['output_dim'])
    
    def forward(self, x, timesteps=100):
        """
        Forward pass
        
        Args:
            x: Input sequence [batch, seq_len, input_dim]
            timesteps: Number of spiking timesteps per input
        
        Returns:
            output: [batch, seq_len, output_dim]
        """
        batch_size, seq_len, _ = x.shape
        
        outputs = []
        for b in range(batch_size):
            # Initialize states
            self.reset_states()
            
            batch_outputs = []
            for t in range(seq_len):
                # Input projection
                input_current = self.input_proj(x[b, t])
                
                # Spiking dynamics (with MTL)
                spikes = self.spiking_step(
                    input_current, 
                    n_mtl_iterations=3
                )
                
                # Output projection
                out = self.output_proj(spikes)
                batch_outputs.append(out)
            
            outputs.append(torch.stack(batch_outputs))
        
        return torch.stack(outputs)
    
    def spiking_step(self, input_current, n_mtl_iterations):
        """Single step with multi-transmission loop"""
        # Initial activation
        activity = self.neurons.compute_current(input_current)
        
        # Spatial propagation (MTL)
        for _ in range(n_mtl_iterations):
            activity = self.mtl.propagate(activity)
            activity = self.neurons.apply_threshold(activity)
        
        # Generate spikes
        spikes = self.neurons.fire(activity)
        
        # STDP learning
        self.synapses.stdp_update(spikes)
        
        # Apply Dale's Law
        self.synapses.apply_constraint(self.dale_constraint)
        
        return spikes
```

## Experimental Results

### Parameter Efficiency

```
Architecture Comparison:
┌────────────────────────┬─────────────────┬─────────────┐
│ Model                  │ Parameters      │ Performance │
├────────────────────────┼─────────────────┼─────────────┤
│ LSTM (6 layers)        │ θ(D²L)          │ Baseline    │
│ Transformer            │ θ(D²)           │ +15%        │
│ S4/DSSM                │ θ(D²)           │ +18%        │
│ PHCSSM                 │ θ(D²)           │ +17%        │
└────────────────────────┴─────────────────┴─────────────┘

Note: L = layers, D = hidden dimension
PHCSSM matches SSM efficiency with biological realism
```

### Biological Fidelity

| Property | Standard SSM | PHCSSM |
|----------|--------------|--------|
| Adaptive thresholds | ✗ | ✓ |
| Dale's Law | ✗ | ✓ |
| Short-term plasticity | ✗ | ✓ |
| STDP learning | ✗ | ✓ |
| Lateral connections | ✗ | ✓ |

## Resources

### Paper
- **arXiv:** https://arxiv.org/abs/2604.01295
- **PDF:** https://arxiv.org/pdf/2604.01295v1
- **Published:** April 1, 2026

### Related Skills
- `spiking-neural-network-training`: SNN training
- `ssm-contraction-control`: SSM control theory
- `neuromodulated-synaptic-plasticity`: Neuromodulated learning

### Citation
```bibtex
@article{chiang2026phc,
  title={Parallelized Hierarchical Connectome: A Spatiotemporal Recurrent Framework for Spiking State-Space Models},
  author={Chiang, Po-Han},
  journal={arXiv preprint arXiv:2604.01295},
  year={2026}
}
```

## Applications

- **Physiological time series:** EEG, ECG, neural recordings
- **Brain-computer interfaces:** Real-time decoding
- **Neuromorphic computing:** Efficient edge deployment
- **Computational neuroscience:** Large-scale brain simulation
