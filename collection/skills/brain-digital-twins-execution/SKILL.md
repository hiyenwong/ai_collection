---
name: brain-digital-twins-execution
description: "Brain digital twins execution semantics framework bridging computational neuroscience models to executable neuromorphic systems. Translates theoretical brain models into digital twins with formal execution semantics. Activation: brain digital twin, neuromorphic execution, neurocomputational model, execution semantics, brain simulation."
---

# Brain Digital Twins: Execution Semantics and Neuro-Neuromorphic Systems

A framework for translating computational neuroscience models into executable digital twins with formal execution semantics. This bridges the gap between theoretical brain models and practical neuromorphic implementations.

## Overview

Brain digital twins are executable models that replicate the behavior of biological neural circuits. This framework provides:

1. **Formal execution semantics** for neural models
2. **Automated translation** to neuromorphic hardware
3. **Verification methods** ensuring behavioral equivalence

## Architecture

### Three-Layer Architecture

```
┌─────────────────────────────────────────────────────┐
│         Application Layer                           │
│    (Brain simulations, BCI, AI systems)            │
└─────────────────────────────────────────────────────┘
                         │
┌─────────────────────────────────────────────────────┐
│         Execution Semantics Layer                   │
│    (Formal model, dynamics, constraints)           │
└─────────────────────────────────────────────────────┘
                         │
┌─────────────────────────────────────────────────────┐
│         Hardware Abstraction Layer                  │
│    (Neuromorphic chips, GPUs, CPUs)                │
└─────────────────────────────────────────────────────┘
```

### 1. Formal Model Definition

```python
from dataclasses import dataclass
from typing import Dict, List, Callable, Optional
import numpy as np

@dataclass
class NeuronModel:
    """
    Formal definition of a neuron model.
    
    Executable semantics for single neuron dynamics.
    """
    name: str
    state_variables: Dict[str, float]  # e.g., {'v': -70, 'u': -14}
    parameters: Dict[str, float]       # e.g., {'a': 0.02, 'b': 0.2}
    dynamics: Callable                  # dv/dt, du/dt functions
    spike_condition: Callable           # When does it spike?
    reset: Callable                     # Post-spike reset
    
    def step(self, dt: float, I_ext: float = 0):
        """Execute one timestep."""
        # Compute derivatives
        derivatives = self.dynamics(
            self.state_variables,
            self.parameters,
            I_ext
        )
        
        # Update state
        for var, dv in derivatives.items():
            self.state_variables[var] += dv * dt
        
        # Check spike
        if self.spike_condition(self.state_variables):
            spike = True
            self.reset(self.state_variables, self.parameters)
        else:
            spike = False
        
        return spike


# Example: Izhikevich neuron
izhikevich = NeuronModel(
    name="Izhikevich",
    state_variables={'v': -70.0, 'u': -14.0},
    parameters={'a': 0.02, 'b': 0.2, 'c': -65.0, 'd': 2.0},
    
    dynamics=lambda s, p, I: {
        'v': 0.04 * s['v']**2 + 5 * s['v'] + 140 - s['u'] + I,
        'u': p['a'] * (p['b'] * s['v'] - s['u'])
    },
    
    spike_condition=lambda s: s['v'] >= 30.0,
    
    reset=lambda s, p: (
        s.update({'v': p['c'], 'u': s['u'] + p['d']})
    )
)
```

### 2. Network Execution Model

```python
@dataclass
class NetworkModel:
    """
    Formal network execution semantics.
    
    Defines how neurons and synapses interact.
    """
    neurons: Dict[str, NeuronModel]
    connections: List[Dict]  # [{'from': 'n1', 'to': 'n2', 'weight': 0.5, 'delay': 1}]
    
    # Execution state
    spike_buffer: Dict[str, List[bool]]  # Delayed spike buffers
    current_time: float = 0.0
    
    def __post_init__(self):
        # Initialize delay buffers
        max_delay = max(c.get('delay', 1) for c in self.connections)
        self.spike_buffer = {
            nid: [False] * max_delay for nid in self.neurons
        }
    
    def step(self, dt: float, external_inputs: Dict[str, float] = None):
        """
        Execute one network timestep.
        
        Formal execution semantics:
        1. Propagate spikes through connections (with delays)
        2. Update neuron states
        3. Check for new spikes
        """
        external_inputs = external_inputs or {}
        new_spikes = {}
        
        # Step each neuron
        for nid, neuron in self.neurons.items():
            # Sum synaptic currents from delayed spikes
            I_syn = 0
            for conn in self.connections:
                if conn['to'] == nid:
                    delay = conn.get('delay', 1)
                    if self.spike_buffer[conn['from']][-delay]:
                        I_syn += conn['weight']
            
            # Total input current
            I_total = external_inputs.get(nid, 0) + I_syn
            
            # Update neuron
            spike = neuron.step(dt, I_total)
            new_spikes[nid] = spike
        
        # Update spike buffers (shift and add new)
        for nid in self.neurons:
            self.spike_buffer[nid].pop(0)
            self.spike_buffer[nid].append(new_spikes[nid])
        
        self.current_time += dt
        
        return new_spikes
```

### 3. Execution Semantics Definition

```python
class ExecutionSemantics:
    """
    Formal execution semantics for brain models.
    
    Defines precise meaning of model execution.
    """
    
    def __init__(self, precision: str = 'float64'):
        self.precision = precision
        self.timing_semantics = 'discrete'  # or 'continuous'
        self.spike_semantics = 'event'       # or 'rate'
    
    def define_dynamics(self, model: NeuronModel) -> Callable:
        """
        Define precise dynamics semantics.
        
        e.g., Euler vs Runge-Kutta, fixed vs adaptive timestep
        """
        if self.timing_semantics == 'discrete':
            return self._discrete_dynamics(model)
        else:
            return self._continuous_dynamics(model)
    
    def _discrete_dynamics(self, model: NeuronModel) -> Callable:
        """Discrete-time execution."""
        def step(state, params, dt, I):
            derivatives = model.dynamics(state, params, I)
            new_state = {
                k: state[k] + derivatives[k] * dt
                for k in state
            }
            return new_state
        return step
    
    def _continuous_dynamics(self, model: NeuronModel) -> Callable:
        """Continuous-time with numerical integration."""
        from scipy.integrate import odeint
        
        def step(state, params, dt, I):
            # Define ODE system
            def system(y, t):
                s = dict(zip(state.keys(), y))
                derivatives = model.dynamics(s, params, I)
                return [derivatives[k] for k in state.keys()]
            
            # Integrate
            y0 = [state[k] for k in state.keys()]
            t_span = [0, dt]
            solution = odeint(system, y0, t_span)
            
            new_state = {
                k: solution[-1][i] for i, k in enumerate(state.keys())
            }
            return new_state
        
        return step
```

## Translation to Neuromorphic Hardware

### 1. Hardware Abstraction

```python
class NeuromorphicBackend:
    """
    Abstract interface for neuromorphic hardware.
    """
    
    def allocate_neurons(self, n_neurons: int, neuron_type: str):
        """Allocate physical neurons."""
        raise NotImplementedError
    
    def configure_synapses(self, connections: List[Dict]):
        """Configure synaptic connections."""
        raise NotImplementedError
    
    def run(self, duration_ms: float, inputs: Dict):
        """Execute on hardware."""
        raise NotImplementedError
    
    def read_spikes(self) -> Dict[str, List[float]]:
        """Read spike times from hardware."""
        raise NotImplementedError


class LoihiBackend(NeuromorphicBackend):
    """Intel Loihi neuromorphic chip backend."""
    
    def __init__(self):
        import nxsdk
        self.board = nxsdk.NxBoard()
    
    def allocate_neurons(self, n_neurons, neuron_type='LIF'):
        # Loihi-specific neuron allocation
        core = self.board.modules[0].chips[0].cores[0]
        
        for i in range(n_neurons):
            neuron = core.neurons[i]
            if neuron_type == 'LIF':
                neuron.threshold = 100
                neuron.decayU = 4096  # Current decay
                neuron.decayV = 2048  # Voltage decay
        
        return list(range(n_neurons))
    
    def configure_synapses(self, connections):
        for conn in connections:
            # Map to Loihi synaptic connections
            synapse = self.board.modules[0].chips[0].cores[0].synapses
            synapse[conn['from']][conn['to']].weight = int(conn['weight'] * 100)
    
    def run(self, duration_ms, inputs):
        self.board.run(duration_ms * 1000)  # Convert to microseconds
    
    def read_spikes(self):
        return self.board.spikes
```

### 2. Model-to-Hardware Compilation

```python
class ModelCompiler:
    """
    Compile brain models to neuromorphic hardware.
    """
    
    def __init__(self, backend: NeuromorphicBackend):
        self.backend = backend
    
    def compile(self, network: NetworkModel) -> 'CompiledModel':
        """
        Compile abstract network to hardware configuration.
        
        Steps:
        1. Neuron mapping
        2. Synapse configuration
        3. Parameter quantization
        4. Timing calibration
        """
        # Allocate neurons
        neuron_ids = self.backend.allocate_neurons(
            len(network.neurons),
            neuron_type=self._detect_neuron_type(network)
        )
        
        # Map abstract to physical
        id_map = {
            nid: physical_id
            for nid, physical_id in zip(network.neurons.keys(), neuron_ids)
        }
        
        # Configure synapses
        physical_connections = [
            {
                'from': id_map[conn['from']],
                'to': id_map[conn['to']],
                'weight': self._quantize_weight(conn['weight']),
                'delay': self._calibrate_delay(conn.get('delay', 1)),
            }
            for conn in network.connections
        ]
        
        self.backend.configure_synapses(physical_connections)
        
        return CompiledModel(
            backend=self.backend,
            id_map=id_map,
            original_network=network,
        )
    
    def _detect_neuron_type(self, network):
        """Detect neuron type from model parameters."""
        # Simplified: check first neuron
        first_neuron = list(network.neurons.values())[0]
        if 'a' in first_neuron.parameters:
            return 'Izhikevich'
        return 'LIF'
    
    def _quantize_weight(self, weight, bits=8):
        """Quantize synaptic weight for hardware."""
        max_val = 2 ** (bits - 1) - 1
        return int(np.clip(weight * max_val, -max_val, max_val))
    
    def _calibrate_delay(self, delay_ms):
        """Convert ms delay to hardware timesteps."""
        # Hardware timestep (e.g., 1 ms on Loihi)
        return max(1, int(delay_ms))


@dataclass
class CompiledModel:
    """Compiled model ready for execution."""
    backend: NeuromorphicBackend
    id_map: Dict[str, int]
    original_network: NetworkModel
    
    def run(self, duration_ms: float, inputs: Dict[str, float]):
        """Execute on hardware."""
        # Convert inputs to hardware format
        hardware_inputs = {
            self.id_map[nid]: val
            for nid, val in inputs.items()
        }
        
        # Run
        self.backend.run(duration_ms, hardware_inputs)
        
        # Read results
        hardware_spikes = self.backend.read_spikes()
        
        # Convert back to abstract IDs
        abstract_spikes = {
            nid: hardware_spikes.get(hid, [])
            for nid, hid in self.id_map.items()
        }
        
        return abstract_spikes
```

## Verification and Validation

```python
class ModelVerifier:
    """
    Verify equivalence between model and hardware execution.
    """
    
    def __init__(self, tolerance: float = 0.05):
        self.tolerance = tolerance
    
    def verify_spike_trains(
        self,
        simulated_spikes: Dict[str, List[float]],
        hardware_spikes: Dict[str, List[float]],
    ) -> Dict[str, float]:
        """
        Compare spike trains from simulation and hardware.
        
        Returns:
            Metrics: spike count difference, timing error, correlation
        """
        metrics = {}
        
        for neuron_id in simulated_spikes:
            sim = simulated_spikes[neuron_id]
            hw = hardware_spikes.get(neuron_id, [])
            
            # Spike count match
            count_diff = abs(len(sim) - len(hw)) / max(len(sim), 1)
            
            # Timing precision (using Victor-Purpura metric)
            timing_cost = self.victor_purpura_distance(sim, hw)
            
            # Van Rossum distance
            rossum_dist = self.van_rossum_distance(sim, hw)
            
            metrics[neuron_id] = {
                'count_difference': count_diff,
                'timing_cost': timing_cost,
                'van_rossum_distance': rossum_dist,
                'passed': count_diff < self.tolerance,
            }
        
        return metrics
    
    def victor_purpura_distance(self, spike_train1, spike_train2, q=0.1):
        """Compute Victor-Purpura spike train distance."""
        # Simplified implementation
        # Cost of adding/removing spike: 1
        # Cost of shifting spike: q * |t1 - t2|
        
        # Use dynamic programming for optimal alignment
        m, n = len(spike_train1), len(spike_train2)
        dp = np.zeros((m + 1, n + 1))
        
        for i in range(m + 1):
            dp[i, 0] = i
        for j in range(n + 1):
            dp[0, j] = j
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                cost = min(
                    dp[i-1, j] + 1,      # Delete from train1
                    dp[i, j-1] + 1,      # Delete from train2
                    dp[i-1, j-1] + q * abs(spike_train1[i-1] - spike_train2[j-1])
                )
                dp[i, j] = cost
        
        return dp[m, n] / max(m, n, 1)
```

## Applications

### 1. Cortical Microcircuit Model

```python
def create_cortical_microcircuit():
    """Create digital twin of cortical microcircuit."""
    
    # Layer structure: L2/3, L4, L5, L6
    layers = ['L2/3', 'L4', 'L5', 'L6']
    neurons_per_layer = 100
    
    network = NetworkModel(
        neurons={},
        connections=[]
    )
    
    # Create neurons for each layer
    for layer in layers:
        for i in range(neurons_per_layer):
            nid = f"{layer}_{i}"
            network.neurons[nid] = NeuronModel(
                name=nid,
                state_variables={'v': -70, 'u': -14},
                parameters={'a': 0.02, 'b': 0.2, 'c': -65, 'd': 8},
                dynamics=izhikevich_dynamics,
                spike_condition=lambda s: s['v'] >= 30,
                reset=izhikevich_reset,
            )
    
    # Add connections between layers (simplified)
    connection_pattern = {
        'L4': ['L2/3'],
        'L2/3': ['L5'],
        'L5': ['L6', 'L2/3'],
    }
    
    for source_layer, target_layers in connection_pattern.items():
        for target_layer in target_layers:
            # Random connections
            for i in range(neurons_per_layer):
                for j in range(neurons_per_layer):
                    if np.random.random() < 0.1:  # 10% connection probability
                        network.connections.append({
                            'from': f"{source_layer}_{i}",
                            'to': f"{target_layer}_{j}",
                            'weight': np.random.randn() * 0.5,
                            'delay': np.random.randint(1, 5),
                        })
    
    return network
```

### 2. Hippocampal Place Cell Model

```python
def create_hippocampal_place_cells(n_cells=100, n_positions=50):
    """
    Create digital twin of hippocampal place cells.
    
    Place cells fire when animal is in specific location.
    """
    network = NetworkModel(neurons={}, connections=[])
    
    # Create place cells
    for i in range(n_cells):
        nid = f"place_cell_{i}"
        
        # Each cell has preferred position
        preferred_pos = np.random.uniform(0, n_positions)
        
        network.neurons[nid] = NeuronModel(
            name=nid,
            state_variables={'v': -70, 'u': -14},
            parameters={
                'a': 0.02, 'b': 0.2, 'c': -65, 'd': 8,
                'preferred_position': preferred_pos,
                'field_width': 5.0,
            },
            dynamics=place_cell_dynamics,
            spike_condition=lambda s: s['v'] >= 30,
            reset=standard_reset,
        )
    
    return network


def place_cell_dynamics(state, params, I_ext):
    """Dynamics modulated by position."""
    position_input = I_ext.get('position', 0)
    
    # Gaussian place field
    distance = abs(position_input - params['preferred_position'])
    field_response = np.exp(-(distance ** 2) / (2 * params['field_width'] ** 2))
    
    # Standard Izhikevich with position-modulated input
    I = I_ext.get('base', 0) + field_response * 20
    
    return izhikevich_dynamics(state, params, I)
```

## References

- Muzy, A. (2026). From Brain Models to Executable Digital Twins: Execution Semantics and Neuro-Neuromorphic Systems. arXiv:2604.13574
- Brette et al. (2007). Simulation of spiking neural networks
- Furber et al. (2014). The SpiNNaker project
- Davies et al. (2018). Loihi: A neuromorphic manycore processor

## Activation Keywords

- brain digital twin
- neuromorphic execution
- neurocomputational model
- execution semantics
- brain simulation
- cortical microcircuit model
- hippocampal place cells
