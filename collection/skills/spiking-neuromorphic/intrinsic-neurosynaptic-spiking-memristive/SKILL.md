---
name: intrinsic-neurosynaptic-spiking-memristive
description: "Intrinsic Neuro-Synaptic Spiking Dynamics in Self-Organizing Memristive Networks (arXiv:2604.18015). Demonstrates that self-assembled memristive networks exhibit intrinsic neuro-synaptic spiking dynamics — including neuronal population bursts, STDP-like learning, emergent oscillatory patterns, multi-modal spike distributions, phase transitions, and criticality signatures — without any external neuron models or transistor-based circuits. Activation: memristive network, spiking dynamics, self-organizing, STDP, neuromorphic, criticality, phase transition, spike-timing, memristor, emergent oscillation, intrinsic dynamics, neuro-synaptic."
---

# Intrinsic Neuro-Synaptic Spiking Dynamics in Self-Organizing Memristive Networks

**Paper**: Intrinsic Neuro-Synaptic Spiking Dynamics Emerging in Self-Organizing Memristive Networks
**Authors**: Thomas P.-P. Béra, Maxime Dion, Jean-Sébastien Boisvert, Alessandro Niccolai, Vincent Boucher, Dominique Drouin, Yohan Beillard, Jean Rouat
**arXiv**: 2604.18015
**Date**: April 17, 2026
**Categories**: cond-mat.dis-nn, q-bio.NC, cs.ET

---

## Summary

This paper demonstrates that self-assembled memristive networks — composed purely of memristive devices connected in a network topology — intrinsically produce complex neuro-synaptic spiking dynamics without any external oscillators, transistor-based neuron circuits, or conventional neuron models. The spiking behavior, learning rules, and emergent patterns arise entirely from the nonlinear device physics of individual memristors and the collective dynamics of the network structure.

Key phenomena observed include:
- **Neuronal population bursts**: Coordinated firing events analogous to neural population bursts in biological networks
- **STDP-like learning**: Spike-timing-dependent plasticity emerges naturally from device-level memristive state changes, without being explicitly programmed
- **Emergent oscillatory patterns**: Self-organized rhythmic activity across multiple frequency bands
- **Multi-modal spike distributions**: Heterogeneous spike amplitudes and inter-spike intervals reflecting diverse dynamical regimes
- **Phase transitions**: Sharp transitions between quiescent, oscillatory, and bursting regimes as a function of applied voltage or network parameters
- **Criticality signatures**: Statistical properties (avalanche size distributions, power-law scaling) consistent with operation near a critical point

This work is significant because it shows that the boundary between "neuron" and "synapse" is not rigid — individual memristive junctions can simultaneously play both roles, and complex neural-like computation can emerge from purely physical substrate dynamics.

---

## Key Methodology

### 1. Self-Assembled Memristive Network Fabrication
- Memristive devices are self-assembled into a complex network topology using bottom-up fabrication techniques (e.g., random deposition of memristive nanomaterials, percolation-based connectivity)
- The network topology is not designed but emerges from the self-assembly process, resulting in heterogeneous connectivity patterns
- Each junction in the network acts as a memristive element with nonlinear current-voltage characteristics and state-dependent conductance

### 2. Experimental Characterization
- External voltage stimuli are applied across network electrodes
- Current and voltage responses are measured at high temporal resolution to capture spike dynamics
- Network activity is analyzed using tools from computational neuroscience: spike detection, inter-spike interval (ISI) analysis, avalanche statistics, spectral analysis

### 3. Computational Modeling
- Memristive device physics models (e.g., voltage-dependent state evolution, filament formation/dissolution kinetics) are used to simulate individual junctions
- Network-level simulations capture collective dynamics including emergent synchronization, wave propagation, and plasticity
- Parameter sweeps explore the space of applied voltage, network size, connectivity density, and device parameters

### 4. Statistical and Dynamical Analysis
- **Spike detection**: Threshold-based identification of fast current transients as "spikes"
- **Spike train analysis**: ISI distributions, burst detection, autocorrelation functions
- **Avalanche analysis**: Size and duration distributions tested for power-law scaling (criticality indicator)
- **Phase transition mapping**: Identification of regime boundaries via order parameters (e.g., mean firing rate, synchronization index)

---

## Core Model/Physics

### Memristive Device Model

Each memristive junction in the network is governed by:

1. **State equation** (internal state variable `w` evolves with applied voltage):
   ```
   dw/dt = f(V, w)
   ```
   where `w` represents the internal state (e.g., filament extent, oxygen vacancy concentration) and `f` is a nonlinear function of voltage and current state.

2. **Conductance equation** (memristance depends on state):
   ```
   G(w) = G_off + (G_on - G_off) * g(w)
   ```
   where `G_on` and `G_off` are the conductance bounds, and `g(w)` maps the state to a [0,1] interval.

3. **Current-voltage relationship**:
   ```
   I = G(w) * V
   ```

### Network-Level Dynamics

- **Kirchhoff's laws** govern current flow through the network at each instant
- The coupled system of nonlinear ODEs (one per memristive junction) creates a high-dimensional dynamical system
- **Positive feedback loops**: Voltage-driven state changes alter conductances, which redistribute voltages, which drive further state changes — producing threshold-and-fire dynamics
- **Negative feedback / relaxation**: State saturation bounds and reverse-bias recovery provide relaxation mechanisms analogous to neural refractory periods

### Emergent Spiking Mechanism

1. **Threshold behavior**: When applied voltage across a memristive junction exceeds a threshold, a rapid conductance change occurs (analogous to neural firing)
2. **Cascade propagation**: A spike at one junction redistributes voltage to neighboring junctions, potentially triggering cascades (avalanches)
3. **STDP from device physics**: The timing-dependent conductance change at each junction depends on the relative timing of pre- and post-synaptic voltage spikes. When a memristive junction sits between two spiking nodes, its state evolves based on the coincidence of spikes from both sides — naturally implementing STDP
4. **Oscillatory regimes**: For certain voltage ranges, the network settles into limit-cycle oscillations arising from coupled relaxation oscillators
5. **Burst dynamics**: Collective transitions between high-activity and low-activity states produce population bursts

### Criticality

- Avalanche size and duration distributions follow power laws: P(s) ~ s^(-τ), P(T) ~ T^(-α)
- This is consistent with self-organized criticality (SOC), where the network naturally tunes itself to a critical point
- Critical operation is hypothesized to maximize information processing capacity, analogous to the critical brain hypothesis

---

## Implementation Notes

### Simulating a Memristive Spiking Network

```python
import numpy as np
from scipy.integrate import solve_ivp

class MemristiveJunction:
    """Single memristive element with voltage-dependent state dynamics."""
    
    def __init__(self, G_on=1e-3, G_off=1e-6, v_threshold=0.8,
                 tau_w=1e-3, alpha=2.0, beta=3.0):
        self.G_on = G_on       # Maximum conductance (S)
        self.G_off = G_off     # Minimum conductance (S)
        self.v_th = v_threshold # Switching threshold (V)
        self.tau_w = tau_w     # State evolution time constant (s)
        self.alpha = alpha     # Forward switching nonlinearity
        self.beta = beta       # Reverse switching nonlinearity
        self.w = 0.0          # State variable [0, 1]
    
    def conductance(self):
        return self.G_off + (self.G_on - self.G_off) * self.w
    
    def current(self, voltage):
        return self.conductance() * voltage
    
    def dw_dt(self, voltage):
        """Nonlinear state evolution: forward/reverse switching."""
        if voltage > self.v_th:
            # Forward switching (SET)
            return (1.0 / self.tau_w) * (1.0 - self.w) * \
                   np.tanh(self.alpha * (voltage - self.v_th))
        elif voltage < -self.v_th:
            # Reverse switching (RESET)
            return (1.0 / self.tau_w) * (-self.w) * \
                   np.tanh(self.beta * (-voltage - self.v_th))
        return 0.0


class MemristiveNetwork:
    """Network of memristive junctions exhibiting emergent spiking."""
    
    def __init__(self, n_nodes, connectivity_prob=0.3, seed=42):
        np.random.seed(seed)
        self.n = n_nodes
        # Random adjacency matrix for network topology
        self.adj = (np.random.rand(n_nodes, n_nodes) < connectivity_prob).astype(float)
        self.adj = np.triu(self.adj, k=1)  # Upper triangle only
        self.adj += self.adj.T              # Symmetric
        np.fill_diagonal(self.adj, 0)
        
        # Create memristive junctions for each edge
        self.junctions = {}
        for i in range(n_nodes):
            for j in range(i+1, n_nodes):
                if self.adj[i, j]:
                    self.junctions[(i, j)] = MemristiveJunction()
    
    def get_conductance_matrix(self):
        """Build conductance matrix from junction states."""
        G = np.zeros((self.n, self.n))
        for (i, j), junc in self.junctions.items():
            g = junc.conductance()
            G[i, j] = g
            G[j, i] = g
        return G
    
    def simulate(self, V_applied, electrodes, t_span, dt=1e-5):
        """
        Simulate network dynamics with voltage applied across electrodes.
        
        Args:
            V_applied: Applied voltage magnitude (V)
            electrodes: Tuple of (source_node, ground_node)
            t_span: Simulation duration (s)
            dt: Time step (s)
        """
        src, gnd = electrodes
        n_steps = int(t_span / dt)
        n = self.n
        
        # Recordings
        node_voltages = np.zeros((n_steps, n))
        junction_currents = np.zeros((n_steps, len(self.junctions)))
        spike_times = {idx: [] for idx in self.junctions}
        
        for step in range(n_steps):
            t = step * dt
            
            # Build conductance matrix
            G = self.get_conductance_matrix()
            
            # Kirchhoff's current law: solve for node voltages
            # G_total[i] * V[i] - sum_j G[i,j] * V[j] = I_external[i]
            A = np.diag(np.sum(G, axis=1)) - G
            b = np.zeros(n)
            
            # Apply boundary conditions
            b[src] = V_applied
            b[gnd] = 0.0
            # Fix electrode voltages (large conductance to source/ground)
            A[src, :] = 0; A[src, src] = 1e6
            A[gnd, :] = 0; A[gnd, gnd] = 1e6
            
            V = np.linalg.solve(A, b)
            node_voltages[step] = V
            
            # Update junction states and record currents
            for k, ((i, j), junc) in enumerate(self.junctions.items()):
                v_junc = V[i] - V[j]
                junc.w += junc.dw_dt(v_junc) * dt
                junc.w = np.clip(junc.w, 0, 1)
                
                current = junc.current(v_junc)
                junction_currents[step, k] = current
                
                # Detect spikes (rapid conductance change)
                if junc.w > 0.9:
                    spike_times[(i, j)].append(t)
        
        return node_voltages, junction_currents, spike_times


# Example usage
if __name__ == "__main__":
    net = MemristiveNetwork(n_nodes=20, connectivity_prob=0.3)
    voltages, currents, spikes = net.simulate(
        V_applied=3.0,
        electrodes=(0, 19),
        t_span=0.1,
        dt=1e-5
    )
    print(f"Total spikes detected: {sum(len(v) for v in spikes.values())}")
```

### Key Parameters to Tune

| Parameter | Range | Effect |
|-----------|-------|--------|
| `V_applied` | 1–10 V | Controls activity regime (quiescent → oscillatory → bursting) |
| `connectivity_prob` | 0.1–0.5 | Network density; affects synchronization and cascade size |
| `G_on / G_off` | 10²–10⁶ ratio | Memristive dynamic range; larger ratio → sharper spikes |
| `v_threshold` | 0.5–2.0 V | Switching threshold; controls firing threshold |
| `tau_w` | 10⁻⁴–10⁻² s | State evolution speed; determines spike width |
| `n_nodes` | 10–1000 | Network size; larger networks show richer dynamics |

### Tools and Libraries

- **NumPy/SciPy**: Numerical simulation of coupled ODEs
- **NetworkX**: Network topology generation and analysis
- **Brian2**: Spiking neural network simulator (can be adapted for memristive network modeling)
- **MATLAB**: Alternative for circuit-level simulation with SPICE integration
- **NEROscape / M-Tortoise**: Specialized memristive network simulators (if available)

---

## Results

### Main Findings from the Paper

1. **Intrinsic Spiking Without Neurons**: Memristive networks produce voltage spikes with characteristic shapes (fast rise, slower decay) purely from device physics. No external neuron model or oscillator circuit is required.

2. **Multi-Modal Spike Distributions**: Spike amplitude and width distributions show multiple modes, indicating coexistence of different spiking mechanisms (e.g., single-junction switching vs. collective cascades).

3. **STDP-Like Plasticity**: When spike timing between connected nodes is varied, the resulting conductance change at the intervening memristive junction follows a curve qualitatively similar to biological STDP — potentiating for causal (pre-before-post) timing and depressing for anti-causal timing.

4. **Phase Transitions**: As applied voltage increases, the network exhibits sharp transitions between:
   - **Quiescent regime**: Low activity, no spikes
   - **Oscillatory regime**: Periodic or quasi-periodic spiking
   - **Bursting regime**: Intermittent population bursts with quiet intervals
   - **Saturated regime**: Continuous high activity (loss of spike structure)

5. **Criticality Signatures**:
   - Avalanche size distributions follow power laws with exponents τ ≈ 1.5 (consistent with branching process theory)
   - Avalanche duration distributions scale as T^(-α) with α ≈ 2.0
   - Scaling relation τ = (α-1)/(α-1) approximately holds, suggesting self-organized criticality

6. **Emergent Oscillatory Patterns**: Network-wide oscillations emerge in specific frequency bands, with frequency content depending on network size, connectivity, and applied voltage.

7. **Self-Organization**: The network autonomously organizes its activity patterns without external control signals, driven by the interplay of memristive state dynamics and network-level current redistribution.

---

## Activation Triggers

This skill should be activated when the user's query involves:

- **Memristive networks** or **memristor-based computing**
- **Neuromorphic hardware** without conventional neuron circuits
- **Emergent spiking dynamics** from physical substrates
- **Self-organizing** neural-like systems
- **STDP** (spike-timing-dependent plasticity) emerging from device physics
- **Criticality** in memristive or resistive switching networks
- **Phase transitions** in memristive systems
- **Intrinsic neuron-like dynamics** from nonlinear device physics
- **Reservoir computing** using memristive networks
- **Brain-inspired computing** using self-assembled nanowire or nanoparticle networks
- **In-materio computing** or **physical neural networks**
- **Avalanche dynamics** and power-law scaling in hardware
- **Neuro-synaptic dynamics** from passive electronic components
- Keywords: memristive spiking, intrinsic neuro-synaptic, self-assembled network, emergent neural dynamics, critical memristor, phase transition memristive, STDP memristor

---

## Related Skills

- `ember-hybrid-snn-llm-architecture`: Hybrid SNN-LLM cognitive architecture with STDP
- `dual-timescale-memory-spiking-neuron-astrocyte-network-efficient`: Spiking neuron-astrocyte networks
- `neuroscience/emergent-ei-reservoir-networks`: Emergent dynamics in E/I reservoir networks
- `research/wta-spiking-transformer-language`: Winner-take-all spiking mechanisms

---

## References

- **Paper**: Béra, T.P.-P., Dion, M., Boisvert, J.-S., Niccolai, A., Boucher, V., Drouin, D., Beillard, Y., Rouat, J. (2026). *Intrinsic Neuro-Synaptic Spiking Dynamics Emerging in Self-Organizing Memristive Networks*. arXiv:2604.18015.
- **Related**: Pershin, Y.V. & Di Ventra, M. (2011). *Practical approach to memristive circuit design*. IEEE TCAD.
- **Related**: Stieg, A.Z. et al. (2012). *Emergent criticality in complex nanowire networks*. Nature Nanotechnology.
- **Related**: Hochstetter, J. et al. (2021). *Avalanches and edge-of-chaos learning in memristive nanowire networks*. Nature Communications.
