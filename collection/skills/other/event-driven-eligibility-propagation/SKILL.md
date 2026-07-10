---
name: event-driven-eligibility-propagation
description: "Event-driven eligibility propagation (e-prop) extension for large sparse recurrent spiking networks. Biologically plausible learning rule with continuous dynamics, strict locality, and sparse connectivity. Scales to millions of neurons without compromising performance. Integrates neuromorphic principles into AI learning algorithms. Keywords: e-prop, event-driven learning, eligibility trace, sparse SNN, biologically plausible, recurrent connectivity, neuromorphic MNIST, scalable learning, local plasticity."
tags: ["spiking-neural-network", "e-prop", "event-driven", "biologically-plausible", "sparse-connectivity", "recurrent-network", "local-learning", "neuromorphic", "scalable-learning", "eligibility-trace"]
---

# Event-driven Eligibility Propagation for Large Sparse Networks

## Paper Information

- **arXiv ID**: 2511.21674
- **Title**: Event-driven eligibility propagation in large sparse networks: efficiency shaped by biological realism
- **Authors**: Agnes Korcsak-Gorzo, Jesús A. Espinoza Valverde, Jonas Stapmanns, Hans Ekkehard Plesser, David Dahmen, Matthias Bolten, Sacha J. van Albada, Markus Diesmann
- **Submission Date**: 2025-11-26
- **Categories**: cs.NE (Neural and Evolutionary Computing), q-bio.NC (Neurons and Cognition)
- **DOI**: https://doi.org/10.48550/arXiv.2511.21674

## Core Innovation

Extends the **eligibility propagation (e-prop)** learning rule from time-driven to **event-driven** computation, enabling scalable biologically plausible learning in large sparse recurrent spiking networks.

### Key Breakthrough

- **Scalability**: Demonstrates learning in networks with **millions of neurons**
- **Biological Plausibility**: Maintains strict locality and sparse connectivity
- **Efficiency**: Event-driven updates significantly reduce computational overhead
- **Neuromorphic Integration**: Compatible with neuromorphic hardware platforms

## Eligibility Propagation Fundamentals

### Original E-prop Concept
E-prop (Bellec et al., 2020) enables credit assignment in recurrent spiking networks through:

1. **Eligibility Traces**: Temporary memory of activity that marks synapses eligible for modification
2. **Feedback Signals**: Global learning signal propagated through network
3. **Local Computation**: Synaptic updates computed locally at each synapse

### Event-driven Extension

The paper transforms time-driven e-prop into event-driven formulation:

```python
# Time-driven e-prop (original)
for t in range(simulation_time):
    compute_eligibility_trace()
    accumulate_gradient()

# Event-driven e-prop (this paper)
for spike_event in spike_sequence:
    compute_eligibility_trace(spike_event)
    accumulate_gradient(spike_event)
```

**Key Advantage**: Only processes computation when neurons spike, dramatically reducing overhead in sparse networks.

## Biological Constraints Incorporated

### 1. Continuous Dynamics and Weight Updates
- **Continuous-time neuronal models**: Leaky integrate-and-fire with continuous membrane potential dynamics
- **Continuous eligibility traces**: Traces evolve continuously, not discretely
- **Smooth weight updates**: Plasticity rules operate on continuous signals

### 2. Strict Locality
- **Synaptic locality**: Each synapse uses only locally available information
- **No global backpropagation**: Learning signals don't require network-wide gradient flow
- **Biologically realistic**: Matches observed synaptic plasticity mechanisms

**Locality Principle**:
```
Δw_ij = eligibility_ij × learning_signal_j
         ↑               ↑
     local only      feedback from target
```

### 3. Sparse Connectivity
- **Biological connectivity**: ~10% connectivity probability (matching cortical data)
- **Structural efficiency**: Reduces synaptic operations by ~90%
- **Event-driven benefit**: Sparse networks generate fewer spike events

## Event-driven Algorithm Design

### Spike-triggered Eligibility Computation

```python
class EventDrivenEProp:
    def __init__(self, neuron, eligibility_decay_rate):
        self.eligibility_trace = 0.0
        self.decay_rate = eligibility_decay_rate
    
    def on_spike(self, time, learning_signal):
        # Update eligibility trace at spike time
        self.eligibility_trace += self.compute_contribution()
        
        # Apply weight update
        weight_update = self.eligibility_trace * learning_signal
        self.synapse.weight += weight_update
    
    def between_spikes(self, time):
        # Continuous decay between spike events
        self.eligibility_trace *= exp(-self.decay_rate * dt)
```

### Implementation Strategy

1. **Event Queue**: Maintain priority queue of spike events
2. **Eligibility Trace Buffer**: Store continuous eligibility values
3. **Learning Signal Accumulation**: Aggregate feedback signals over simulation
4. **Sparse Matrix Operations**: Optimize for sparse connectivity structure

## Network Architecture

### Recurrent Spiking Network Model

```python
class SparseRecurrentSNN:
    def __init__(self, N_neurons, connectivity_prob=0.1):
        self.neurons = [LIFNeuron() for _ in range(N_neurons)]
        
        # Sparse connectivity (biologically realistic)
        self.connectivity = create_sparse_matrix(
            N_neurons, N_neurons, 
            probability=connectivity_prob
        )
        
        # Event-driven simulation
        self.event_queue = PriorityQueue()
```

### Biological Neuron Model

```python
class LIFNeuron:
    def __init__(self, tau_m=20ms, v_th=1.0, v_reset=0.0):
        self.membrane_potential = 0.0
        self.tau_m = tau_m  # Membrane time constant
        self.v_th = v_th    # Threshold
        self.v_reset = v_reset
    
    def update(self, input_current, dt):
        # Continuous dynamics
        dv = (-self.v + input_current) / self.tau_m * dt
        self.v += dv
        
        # Spike detection
        if self.v > self.v_th:
            self.v = self.v_reset
            return True  # Spike event
        return False
```

## Performance Results

### Neuromorphic MNIST
- Successfully trained on event-based vision tasks
- Demonstrates classification accuracy comparable to time-driven e-prop
- **Energy efficiency**: Significant reduction in computation due to event-driven updates

### Scalability Benchmarks
- **Network size**: Tested up to **millions of neurons**
- **Connectivity**: Maintains biological sparsity (10% connectivity)
- **Learning speed**: No performance degradation with scale

### Key Metrics
| Metric | Time-driven E-prop | Event-driven E-prop |
|--------|-------------------|---------------------|
| Computational events | O(T × N) | O(S) where S << T×N |
| Memory usage | High (dense traces) | Low (sparse events) |
| Biological plausibility | Medium | High |
| Scalability | Limited | Excellent |

*Where T = simulation time, N = neurons, S = total spike count*

## Biological Inspiration

### Cortical Learning Mechanisms
Event-driven e-prop aligns with three key biological observations:

1. **Spike-triggered Plasticity**
   - Synaptic changes occur primarily at spike times
   - Eligibility traces mirror synaptic tagging mechanisms

2. **Local Credit Assignment**
   - Individual synapses compute updates autonomously
   - Feedback signals provide coarse guidance, not precise gradients

3. **Sparse Cortical Connectivity**
   - Brain uses sparse connectivity (~10-20% in cortex)
   - Event-driven algorithms exploit this structure

### Eligibility Trace as Synaptic Tag

**Synaptic Tag-and-Capture Hypothesis**:
- Late-phase LTP requires synaptic tags from early activity
- Event-driven eligibility traces function as these tags
- Learning signal acts as "capture" mechanism consolidating changes

## Practical Implementation Guidelines

### Step 1: Sparse Connectivity Setup

```python
import scipy.sparse as sp

def create_bio_sparse_connectivity(N, probability=0.1):
    """Create biologically realistic sparse connectivity"""
    random_matrix = sp.random(N, N, density=probability, format='csr')
    return random_matrix
```

### Step 2: Event-driven Simulation

```python
class EventDrivenSimulator:
    def simulate(self, duration, input_spikes):
        time = 0.0
        spike_queue = PriorityQueue()
        
        # Add input spikes to queue
        for spike_time, neuron_id in input_spikes:
            spike_queue.push((spike_time, neuron_id))
        
        # Process events chronologically
        while time < duration and not spike_queue.empty():
            spike_time, neuron_id = spike_queue.pop()
            time = spike_time
            
            # Propagate spike through sparse connectivity
            self.process_spike(neuron_id, spike_queue)
```

### Step 3: Eligibility Trace Management

```python
class EligibilityManager:
    def __init__(self, decay_rate=0.01):
        self.traces = {}  # neuron_id -> trace_value
        self.decay_rate = decay_rate
    
    def update_on_spike(self, neuron_id):
        # Increment eligibility at spike
        self.traces[neuron_id] = self.traces.get(neuron_id, 0) + 1.0
    
    def decay_between_events(self, time_elapsed):
        # Continuous exponential decay
        for neuron_id in self.traces:
            self.traces[neuron_id] *= exp(-self.decay_rate * time_elapsed)
```

### Step 4: Local Weight Update

```python
def compute_weight_update(synapse, eligibility_trace, learning_signal):
    """Local plasticity rule"""
    # Strict locality: only local info + global signal
    delta_w = eligibility_trace * learning_signal
    
    # Apply update
    synapse.weight += delta_w
    
    # Optional: weight decay, bounds
    synapse.weight = clip(synapse.weight, -w_max, w_max)
```

## Neuromorphic Hardware Implications

### Hardware Efficiency
- **Event-driven computation**: Matches neuromorphic chip architecture (Loihi, SpiNNaker)
- **Sparse operations**: Reduces memory bandwidth requirements
- **Local updates**: Eliminates need for global gradient storage

### Deployment Considerations

```python
# Neuromorphic chip mapping
class NeuromorphicDeployment:
    def map_network(self, sparse_snn):
        # Map sparse connectivity to chip routing
        routing_table = create_sparse_routing(snn.connectivity)
        
        # Configure local learning circuits
        plasticity_config = configure_local_learning(
            eligibility_decay=self.decay_rate,
            learning_signal_routing='broadcast'
        )
        
        return NeuromorphicConfig(routing_table, plasticity_config)
```

## Key Insights

### Efficiency vs. Biological Plausibility Trade-off

**Paradox Resolved**: Event-driven formulation shows biological constraints **improve** efficiency:
- Sparse connectivity reduces computation
- Event-triggering matches spike-based hardware
- Local updates eliminate expensive backpropagation

### Scalability Breakthrough

**Previous Limitation**: Time-driven algorithms computational cost grows with simulation time
**Event-driven Solution**: Cost scales with spike count, which is much smaller in sparse networks

### Machine Learning ↔ Neuroscience Bridge

**Bidirectional Benefit**:
- Neuroscience informs efficient AI algorithms
- AI advances provide insights into brain learning mechanisms

## Comparison with Alternative Learning Rules

| Rule | Locality | Scalability | Bio-plausibility | Hardware |
|------|----------|-------------|------------------|----------|
| Backpropagation | Global | Poor | None | GPUs only |
| E-prop (time-driven) | Semi-local | Medium | Medium | Hybrid |
| **Event-driven E-prop** | **Strict local** | **Excellent** | **High** | **Neuromorphic-native** |
| STDP | Strict local | Excellent | High | Neuromorphic-native |

## Limitations and Considerations

1. **Task Complexity**: May require more sophisticated learning signals for complex tasks
2. **Hyperparameter Sensitivity**: Eligibility trace decay rate needs tuning
3. **Network Structure**: Benefits most from biologically sparse connectivity
4. **Training Time**: May converge slower than gradient-based methods

## Future Research Directions

### Algorithm Extensions
- **Multi-layer Event-driven E-prop**: Extend to hierarchical architectures
- **Reward-modulated E-prop**: Add reinforcement learning signals
- **Adaptive Eligibility Decay**: Learn optimal decay rates per synapse

### Hardware Co-design
- **Loihi 2 Integration**: Implement on Intel's advanced neuromorphic chip
- **SpiNNaker 2 Deployment**: Scale to million-neuron simulations
- **Custom ASIC**: Design chips optimized for event-driven learning

### Neuroscience Validation
- **In-vivo Comparison**: Test if brain uses similar eligibility mechanisms
- **Synaptic Tagging Experiments**: Validate trace biology
- **Connectivity Matching**: Compare learned weights with cortical data

## Related Work

### E-prop Origins
- Bellec et al. (2020): "A solution to the learning dilemma for recurrent spiking networks"
- Introduces eligibility traces for recurrent SNNs

### Event-driven Computing
- Neuron simulation platforms: NEST, Brian2 event-driven modes
- Neuromorphic hardware: Loihi's event-based architecture

### Biological Learning
- Synaptic tagging and capture hypothesis
- Spike-timing dependent plasticity (STDP)
- Three-factor learning rules (neuromodulated plasticity)

## Implementation Resources

### Simulation Platforms
- **NEST Simulator**: Supports event-driven spike processing
- **Brian2**: Flexible SNN simulation with custom learning rules
- **SpikingJelly**: PyTorch-based SNN framework (can implement event-driven)

### Code Availability
- Paper likely provides implementation details
- Can be implemented in existing neuromorphic simulators

## Citation

```bibtex
@article{korcsak2025event,
  title={Event-driven eligibility propagation in large sparse networks: efficiency shaped by biological realism},
  author={Korcsak-Gorzo, Agnes and Espinoza Valverde, Jes{\'u}s A and Stapmanns, Jonas and Plesser, Hans Ekkehard and Dahmen, David and Bolten, Matthias and van Albada, Sacha J and Diesmann, Markus},
  journal={arXiv preprint arXiv:2511.21674},
  year={2025}
}
```

## Activation Triggers

Use this skill when working on:
- **Large-scale SNN training**: Networks with millions of neurons
- **Biologically plausible learning**: Strict locality requirements
- **Neuromorphic deployment**: Hardware-native learning algorithms
- **Sparse network optimization**: Exploit sparse connectivity structure
- **Event-driven architecture**: Spike-triggered computation
- **Recurrent SNN credit assignment**: Eligibility trace mechanisms
- **Energy-efficient learning**: Reduce computational overhead

**Keywords**: `event-driven e-prop`, `eligibility propagation`, `sparse snn`, `biologically plausible`, `local plasticity`, `event-driven learning`, `recurrent snn`, `neuromorphic mnist`, `scalable learning`, `eligibility trace`, `synaptic tag`, `neuromorphic hardware`, `continuous dynamics`, `sparse connectivity`, `million neurons`, `strict locality`, `recurrent connectivity`