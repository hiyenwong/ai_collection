---
name: system-resilience-design-patterns
description: "System resilience and robustness design patterns - analyzing complex system stability, collapse mechanisms, control-oriented digital twins, and distributed system optimization. Activation: system resilience, robust design, complex systems, digital twin, control systems, distributed optimization."
---

# System Resilience Design Patterns

Patterns for designing robust, resilient systems that maintain stability under perturbation and gracefully degrade under stress.

## Core Patterns

### Pattern 1: Temporal Structure for System Robustness

**Source**: Temporal Structure Mediates the Robustness and Collapse of Plant-Pollinator Networks (arXiv:2604.07347)

**Key Insight**: Temporal dynamics organize system diversity into distinct phases, creating potential for alternative stable states and bistable regimes. Temporal structure mediates the nature of transitions—whether systems undergo gradual shifts or catastrophic collapses.

**Application**:
```
┌─────────────────────────────────────────────────────┐
│          TEMPORAL STRUCTURE DESIGN                  │
├─────────────────────────────────────────────────────┤
│  Phase A (High-Diversity) ←→ Phase B (Low-Diversity)│
│                                                     │
│  ┌───────────────┐     ┌───────────────────┐       │
│  │ Temporal      │     │ Bistable Regime   │       │
│  │ Bottleneck    │←───→│ Detection         │       │
│  └───────────────┘     └───────────────────┘       │
│                                                     │
│  Percolation Analysis → Collapse Threshold          │
└─────────────────────────────────────────────────────┘
```

**Methodology**:
1. Model system with explicit temporal turnover
2. Use percolation methods to derive analytical solutions
3. Identify bifurcation points between stable states
4. Design bottlenecks to prevent catastrophic transitions

**Code Example** (Percolation-based Robustness Analysis):
```python
import numpy as np
from scipy.optimize import brentq

def percolation_threshold(connectivity_matrix, temporal_factor):
    """
    Calculate system collapse threshold using percolation theory.
    
    Args:
        connectivity_matrix: Network adjacency matrix
        temporal_factor: Temporal structure coefficient (0-1)
    
    Returns:
        Critical occupation probability p_c
    """
    n = connectivity_matrix.shape[0]
    avg_degree = np.mean(np.sum(connectivity_matrix > 0, axis=1))
    
    # Percolation threshold adjusted by temporal structure
    # p_c = 1 / <k> for random graphs, but temporal factors modify this
    p_c_base = 1.0 / avg_degree
    
    # Temporal bottlenecks reduce robustness
    p_c_adjusted = p_c_base * (1 + temporal_factor * 0.5)
    
    return p_c_adjusted

def bistability_region(parameters, stability_func):
    """
    Identify bistable parameter regions where two stable states coexist.
    
    Returns the parameter range where both high and low diversity states exist.
    """
    # Find saddle-node bifurcation points
    def f(x): return stability_func(x, parameters)
    
    try:
        # Search for multiple equilibria
        equilibria = []
        for guess in np.linspace(0.1, 0.9, 10):
            try:
                eq = brentq(lambda x: f(x) - x, guess - 0.1, guess + 0.1)
                equilibria.append(eq)
            except:
                pass
        
        if len(set(np.round(equilibria, 3))) >= 2:
            return True, sorted(set(np.round(equilibria, 3)))
        return False, []
    except:
        return False, []
```

---

### Pattern 2: Control-Oriented Digital Twins with Partial Observability

**Source**: Graph Neural ODE Digital Twins for Control-Oriented Reactor Forecasting (arXiv:2604.07292)

**Key Insight**: Physics-informed GNN-ODE surrogates enable real-time forecasting of plant-wide states at uninstrumented locations. Message-passing encodes physical connectivity, Neural ODE advances dynamics in continuous time.

**Application**:
```
┌──────────────────────────────────────────────────────┐
│     GNN-ODE DIGITAL TWIN ARCHITECTURE               │
├──────────────────────────────────────────────────────┤
│                                                      │
│  Sensors ──→ Directed Graph ──→ Message Passing     │
│                    │                                 │
│              [Physical Connectivity]                 │
│                    │                                 │
│              Neural ODE ──→ Continuous Dynamics      │
│                    │                                 │
│            [Topology-guided Initializer]            │
│                    ↓                                 │
│           State Forecasting + Uncertainty Q          │
└──────────────────────────────────────────────────────┘
```

**Methodology**:
1. Represent system as sensor graph with hydraulic/heat-transfer edges
2. Train physics-informed GNN with message passing
3. Couple with Neural ODE for continuous-time dynamics
4. Use topology-guided initializer for missing nodes
5. Run ensemble rollouts for uncertainty quantification

**Code Example** (GNN-ODE for Digital Twin):
```python
import torch
import torch.nn as nn
from torch_geometric.nn import MessagePassing

class PhysicsMessagePassing(MessagePassing):
    """
    Message passing layer encoding physical connectivity.
    
    Messages carry flow/heat transfer information along hydraulic edges.
    """
    def __init__(self, edge_dim, node_dim):
        super().__init__(aggr='add')
        self.edge_encoder = nn.Linear(edge_dim, node_dim)
        self.node_update = nn.Linear(2 * node_dim, node_dim)
    
    def forward(self, x, edge_index, edge_attr):
        # x: node features [N, node_dim]
        # edge_index: [2, E] source and target nodes
        # edge_attr: edge features (flow rate, heat transfer coefficient)
        
        edge_msg = self.edge_encoder(edge_attr)
        out = self.propagate(edge_index, x=x, edge_msg=edge_msg)
        return self.node_update(torch.cat([x, out], dim=-1))
    
    def message(self, x_j, edge_msg):
        return x_j + edge_msg  # Physical coupling

class NeuralODEController(nn.Module):
    """
    Neural ODE for continuous-time system dynamics.
    
    Enables arbitrary time-step forecasting and smooth trajectories.
    """
    def __init__(self, gnn, ode_func):
        super().__init__()
        self.gnn = gnn
        self.ode_func = ode_func  # dx/dt = f(x, t, control)
    
    def forward(self, x0, t_span, control_input):
        """
        Forecast system state over time span.
        
        Args:
            x0: Initial state [N, state_dim]
            t_span: Time points to forecast [T]
            control_input: Control signals [T, control_dim]
        
        Returns:
            Trajectory [T, N, state_dim]
        """
        from torchdiffeq import odeint
        
        trajectory = odeint(
            lambda t, x: self.ode_func(t, x, control_input),
            x0,
            t_span,
            method='dopri5'  # Adaptive step size
        )
        return trajectory

class MissingNodeInitializer(nn.Module):
    """
    Topology-guided initialization for uninstrumented nodes.
    
    Uses graph structure to estimate initial states at sensor-less locations.
    """
    def __init__(self, graph_structure):
        super().__init__()
        self.graph = graph_structure
    
    def initialize(self, observed_states, observed_mask):
        """
        Initialize missing nodes based on graph connectivity.
        
        Args:
            observed_states: States at instrumented nodes
            observed_mask: Boolean mask of observed nodes
        
        Returns:
            Full state vector with estimated missing values
        """
        full_states = observed_states.clone()
        
        # Propagate from observed to unobserved via graph structure
        for node in range(len(observed_mask)):
            if not observed_mask[node]:
                neighbors = self.graph.neighbors[node]
                observed_neighbors = [n for n in neighbors if observed_mask[n]]
                if observed_neighbors:
                    # Average neighboring observed states
                    neighbor_states = observed_states[observed_neighbors]
                    full_states[node] = neighbor_states.mean(dim=0)
        
        return full_states
```

---

### Pattern 3: Frequency-Aware Communication Optimization

**Source**: SL-FAC: Communication-Efficient Split Learning Framework (arXiv:2604.07316)

**Key Insight**: Frequency decomposition separates high-energy (critical) and low-energy (compressible) components. Adaptive quantization preserves convergence-critical information while reducing bandwidth.

**Application**:
```
┌────────────────────────────────────────────────────┐
│     FREQUENCY-AWARE COMPRESSION PIPELINE          │
├────────────────────────────────────────────────────┤
│                                                    │
│  Smashed Data ──→ Adaptive Frequency Decomposition │
│         │                    │                     │
│         │              ┌─────┴─────┐              │
│         │              │           │              │
│         │         High-Energy  Low-Energy         │
│         │         (8-bit)      (2-bit)            │
│         │              │           │              │
│         │              └─ Frequency-based         │
│         │                 Quantization            │
│         │                    │                    │
│         └─ Compressed Transmission ──→            │
│                                    Reconstruction  │
└────────────────────────────────────────────────────┘
```

**Methodology**:
1. Transform activations/gradients to frequency domain (FFT/DCT)
2. Decompose into spectral components by energy
3. Assign bit widths inversely proportional to spectral energy
4. Transmit with entropy coding
5. Reconstruct at receiver

**Code Example** (Frequency-Aware Compression):
```python
import numpy as np
from scipy.fftpack import dct, idct

class AdaptiveFrequencyDecomposition:
    """
    Decompose data into frequency components based on spectral energy.
    """
    def __init__(self, threshold_ratio=0.7):
        self.threshold_ratio = threshold_ratio
    
    def decompose(self, data):
        """
        Transform to frequency domain and separate components.
        
        Args:
            data: Activation tensor [B, C, H, W] or gradient
        
        Returns:
            high_energy: Critical frequency components (preserve)
            low_energy: Compressible frequency components (quantize)
        """
        # Transform to frequency domain
        freq = dct(data, type=2, axis=-1, norm='ortho')
        
        # Calculate spectral energy
        energy = np.abs(freq) ** 2
        total_energy = np.sum(energy)
        
        # Identify threshold for high-energy components
        cumulative_energy = np.cumsum(np.sort(energy.flatten())[::-1])
        threshold_idx = np.searchsorted(
            cumulative_energy / total_energy,
            self.threshold_ratio
        )
        threshold = np.sort(energy.flatten())[::-1][threshold_idx]
        
        # Decompose
        high_mask = energy >= threshold
        low_mask = ~high_mask
        
        high_energy = freq * high_mask
        low_energy = freq * low_mask
        
        return high_energy, low_energy, energy

class FrequencyBasedQuantization:
    """
    Quantize frequency components with adaptive bit widths.
    """
    def __init__(self, high_bits=8, low_bits=2):
        self.high_bits = high_bits
        self.low_bits = low_bits
    
    def quantize(self, high_freq, low_freq, energy):
        """
        Apply frequency-aware quantization.
        
        High-energy components: preserve with high precision
        Low-energy components: aggressive quantization
        """
        # High-energy quantization (8-bit, preserve convergence)
        high_scale = 2 ** (self.high_bits - 1) - 1
        high_quantized = np.round(high_freq / np.max(np.abs(high_freq)) * high_scale)
        high_quantized = high_quantized.astype(np.int16)
        
        # Low-energy quantization (2-bit, bandwidth reduction)
        low_scale = 2 ** (self.low_bits - 1) - 1
        low_quantized = np.round(low_freq / np.max(np.abs(low_freq)) * low_scale)
        low_quantized = low_quantized.astype(np.uint8)  # 2-bit packed
        
        return high_quantized, low_quantized
    
    def dequantize(self, high_quant, low_quant, original_scale):
        """Reconstruct from quantized representation."""
        high_freq = high_quant.astype(np.float32) / (2 ** (self.high_bits - 1) - 1)
        low_freq = low_quant.astype(np.float32) / (2 ** (self.low_bits - 1) - 1)
        
        # Scale back to original magnitude
        high_freq *= original_scale['high']
        low_freq *= original_scale['low']
        
        return high_freq + low_freq

def reconstruct_from_frequency(freq_data, original_shape):
    """Inverse DCT to reconstruct original data."""
    return idct(freq_data, type=2, axis=-1, norm='ortho')
```

---

### Pattern 4: Bottom-Up Energy Modeling for Infrastructure Planning

**Source**: Generative AI Workload Power Profiles for Data Center Planning (arXiv:2604.07345)

**Key Insight**: High-resolution power measurements (0.1s) linked to whole-facility demand via bottom-up event-driven models. Enables infrastructure planning for grid connection, on-site generation, and microgrids.

**Application**:
```
┌─────────────────────────────────────────────────────┐
│   BOTTOM-UP DATA CENTER ENERGY MODEL               │
├─────────────────────────────────────────────────────┤
│                                                     │
│  Workload Profile ──→ GPU Power (0.1s resolution)   │
│         │                                           │
│         │                                           │
│  MLCommons/vLLM    ──→  Standardized Benchmarks     │
│         │                                           │
│         ↓                                           │
│  ┌─────────────────────────────────┐               │
│  │   Event-Driven Facility Model   │               │
│  │  • Cooling system dynamics       │               │
│  │  • Power distribution losses     │               │
│  │  • User behavior simulation      │               │
│  └─────────────────────────────────┘               │
│         │                                           │
│         ↓                                           │
│  Whole-Facility Energy Profile ──→                 │
│  Grid Connection + Microgrid Planning               │
└─────────────────────────────────────────────────────┘
```

**Methodology**:
1. Measure workload power at sub-second resolution
2. Profile using standardized benchmarks (MLCommons, vLLM)
3. Build bottom-up facility model (cooling, distribution, users)
4. Scale to facility-level with event-driven simulation
5. Plan grid/microgrid infrastructure

**Code Example** (Bottom-Up Energy Model):
```python
import numpy as np
from collections import defaultdict

class WorkloadPowerProfiler:
    """
    Measure and profile AI workload power consumption.
    """
    def __init__(self, sampling_rate=10):  # 0.1s = 10 Hz
        self.sampling_rate = sampling_rate
        self.power_samples = defaultdict(list)
    
    def profile_workload(self, workload_type, duration_s, gpu_power_func):
        """
        Profile power consumption for training/finetuning/inference.
        
        Args:
            workload_type: 'training', 'finetuning', 'inference'
            duration_s: Profile duration in seconds
            gpu_power_func: Function returning instantaneous GPU power
        
        Returns:
            Power profile array [samples,]
        """
        n_samples = int(duration_s * self.sampling_rate)
        samples = []
        
        for i in range(n_samples):
            t = i / self.sampling_rate
            power = gpu_power_func(t, workload_type)
            samples.append(power)
        
        self.power_samples[workload_type] = np.array(samples)
        return np.array(samples)
    
    def get_statistics(self, workload_type):
        """Return power statistics for workload."""
        samples = self.power_samples[workload_type]
        return {
            'mean': np.mean(samples),
            'peak': np.max(samples),
            'std': np.std(samples),
            'energy_total': np.sum(samples) / self.sampling_rate,  # Joules
        }

class BottomUpFacilityModel:
    """
    Event-driven model scaling workload power to facility-level.
    """
    def __init__(self, n_gpus, cooling_efficiency=0.8, pdu_efficiency=0.95):
        self.n_gpus = n_gpus
        self.cooling_efficiency = cooling_efficiency
        self.pdu_efficiency = pdu_efficiency
    
    def scale_to_facility(self, gpu_power_profile, user_arrival_pattern):
        """
        Calculate whole-facility energy demand.
        
        Args:
            gpu_power_profile: Single GPU power samples
            user_arrival_pattern: User request arrival times
        
        Returns:
            Facility-level power profile
        """
        facility_power = np.zeros_like(gpu_power_profile)
        
        # Aggregate active GPUs based on user arrivals
        active_gpus = np.zeros(len(gpu_power_profile))
        for arrival in user_arrival_pattern:
            # Simulate workload duration
            start_idx = int(arrival['time'] * self.sampling_rate)
            duration_idx = int(arrival['duration'] * self.sampling_rate)
            active_gpus[start_idx:start_idx + duration_idx] += arrival['n_gpus']
        
        # GPU power contribution
        gpu_total = gpu_power_profile * np.minimum(active_gpus, self.n_gpus)
        
        # Add cooling overhead (PUE = 1 / cooling_efficiency)
        cooling = gpu_total / self.cooling_efficiency - gpu_total
        
        # Add PDU losses
        pdu_loss = (gpu_total + cooling) * (1 - self.pdu_efficiency)
        
        facility_power = gpu_total + cooling + pdu_loss
        
        return facility_power
    
    def plan_infrastructure(self, facility_power, peak_margin=1.2):
        """
        Determine grid connection and microgrid requirements.
        
        Returns capacity recommendations for:
        - Grid connection capacity
        - On-site generation capacity
        - Battery storage sizing
        """
        peak_power = np.max(facility_power)
        mean_power = np.mean(facility_power)
        
        return {
            'grid_capacity_kw': peak_power * peak_margin / 1000,
            'generation_capacity_kw': mean_power / 1000,  # Solar/generator
            'battery_capacity_kwh': (peak_power - mean_power) * 4 / 1000 / 3600,
            'pue_target': 1.0 / self.cooling_efficiency,
        }
```

---

## Unified Framework: System Resilience Design Cycle

```
┌─────────────────────────────────────────────────────────────┐
│          SYSTEM RESILIENCE DESIGN CYCLE                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────┐    ┌───────────────┐    ┌─────────────┐  │
│  │  1. Model    │───→│  2. Analyze   │───→│  3. Optimize │  │
│  │  Structure   │    │  Stability    │    │  Design      │  │
│  └──────────────┘    └───────────────┘    └─────────────┘  │
│        │                    │                   │          │
│        ↓                    ↓                   ↓          │
│  [Temporal Model]    [Percolation/ODE]    [Freq/Energy]    │
│                                                             │
│  ┌──────────────┐    ┌───────────────┐    ┌─────────────┐  │
│  │  4. Validate │←───│  5. Deploy    │←───│  4. Monitor  │  │
│  │  Robustness  │    │  & Control    │    │  & Adapt     │  │
│  └──────────────┘    └───────────────┘    └─────────────┘  │
│        │                    │                   │          │
│        ↓                    ↓                   ↓          │
│  [Digital Twin]      [GNN-ODE Control]   [Event-Driven]    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Decision Guide

| Problem Type | Pattern | Key Method |
|-------------|---------|------------|
| System collapse prediction | Pattern 1 | Percolation + bistability |
| State forecasting at unobserved locations | Pattern 2 | GNN-ODE + topology init |
| Distributed system bandwidth bottleneck | Pattern 3 | Frequency-aware quantization |
| Infrastructure capacity planning | Pattern 4 | Bottom-up event-driven model |

## Related Skills

- `complex-systems-analysis`: Network science methods
- `control-system-design`: MPC and feedback control
- `distributed-ml-optimization`: Split learning frameworks
- `physics-informed-neural-networks`: PINNs and Neural ODE

## References

See `references/` directory for detailed paper summaries:
- `plant-pollinator-networks.md`: Temporal robustness analysis
- `gnn-ode-digital-twin.md`: Control-oriented forecasting
- `sl-fac-compression.md`: Frequency-aware communication
- `data-center-power-profiles.md`: Infrastructure energy modeling

## Tools Required

- `torch`, `torch_geometric`, `torchdiffeq`: Neural networks and ODE solvers
- `numpy`, `scipy`: Numerical analysis and FFT
- `networkx`: Network science analysis

## Activation Keywords

- system resilience
- robust design
- complex systems
- digital twin
- control systems
- distributed optimization
- infrastructure planning
- 系统韧性
- 稳健设计

---

_Skill generated from arXiv papers on 2026-04-09_