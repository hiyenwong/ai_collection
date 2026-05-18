---
name: clockless-asynchronous-neuromorphic-computing
description: >
  Clockless asynchronous neuromorphic computing methodology using FPGAs. Use when:
  designing neuromorphic hardware systems, implementing asynchronous/spiking digital
  circuits, building energy-efficient neural processors on FPGAs, or studying
  clockless Boolean spiking neuron architectures. Covers autonomous time-continuous
  spiking dynamics, excitatory/inhibitory synaptic weights on reconfigurable chips.
---

# Clockless Asynchronous Neuromorphic Computing

## Core Concept

Implement neuromorphic computing using **clockless (asynchronous) digital circuits** 
on standard FPGAs. Boolean spiking neurons evolve continuously without a global clock,
emerging spiking dynamics from autonomous circuit behavior.

## Architecture

### Boolean Spiking Neurons
- Each neuron: a clockless digital circuit with feedback
- State transitions triggered by input spikes, not clock edges
- Excitatory and inhibitory weights implemented as configurable delays/gates
- Autonomous oscillation emerges from network connectivity

### FPGA Implementation
- Map neuron circuits to FPGA lookup tables (LUTs) and routing
- No PLL/clock distribution needed - eliminates clock tree power
- Reconfigurable: change topology by reprogramming interconnect
- Commercial FPGAs sufficient - no custom neuromorphic ASIC needed

### Spike Encoding
- Input data → spike trains (rate or temporal coding)
- Output spikes → decoded to classification/regression results
- Event-driven processing: computation only on spike events

## Implementation Pipeline

```
Input Data → Spike Encoder → FPGA Neuromorphic Core → Spike Decoder → Output
                  ↓                    ↓                     ↓
             Rate/Temporal      Boolean neurons        Classification
             Coding             with E/I weights       or regression
```

### Spike Encoding Strategies
```python
def rate_encode(signal, max_rate=1000, window_ms=100):
    """Convert continuous signal to spike train via rate coding"""
    # Map signal amplitude to spike frequency
    # Higher value → more spikes per time window
    pass

def temporal_encode(signal):
    """Encode via precise spike timing"""
    # First spike latency coding
    # Lower value → earlier spike
    pass

def delta_encode(signal, threshold=0.1):
    """Delta modulation: spike on significant change"""
    # Event-based: only spike when signal changes significantly
    # Most efficient for sparse/temporally varying data
    pass
```

### Neuron Circuit Design
```verilog
// Simplified Boolean spiking neuron (asynchronous)
module bool_neuron (
    input wire [N-1:0] synapses,  // E/I weighted inputs
    output wire spike              // Output spike
);
    // Asynchronous threshold logic
    // No clock - state changes on input transitions
    // Membrane potential → threshold → spike → reset
    assign spike = (weighted_sum(synapses) >= threshold);
endmodule
```

## Energy Efficiency Analysis

| Component | Power | Notes |
|---|---|---|
| Clock distribution | 30-40% of chip | Eliminated in clockless design |
| Active neurons | Proportional to spikes | Event-driven, no idle power |
| Memory (weights) | Static when idle | Configuration RAM |
| Routing | Dynamic | Depends on spike activity |

Clockless designs achieve **10-100x lower power** than clocked equivalents for 
sparse spike patterns.

## Key Advantages

1. **No custom hardware**: Uses commercial FPGAs, no ASIC needed
2. **Reconfigurable**: Change network topology by reprogramming
3. **Energy efficient**: Eliminates clock tree, event-driven computation
4. **Scalable**: Can chain multiple FPGAs for larger networks
5. **Quasi-analog**: Continuous-time behavior from digital circuits

## Applications

### Audio Classification
- MFCC features → spike encoding → neuromorphic classification
- Demonstrated competitive accuracy vs. traditional DNNs
- Significantly lower power consumption

### Event-based Vision
- DVS (Dynamic Vision Sensor) output → direct spike input
- No encoding needed - sensor already produces events
- Ideal for real-time, low-power visual processing

### Temporal Pattern Recognition
- Sequence learning through spike timing
- Natural fit for asynchronous dynamics
- Applications: gesture recognition, anomaly detection

## Design Guidelines

1. **Start simple**: Begin with small networks (10s of neurons)
2. **Validate dynamics**: Verify spiking behavior matches biological expectations
3. **Profile power**: Measure actual vs. theoretical energy savings
4. **Optimize encoding**: Spike encoding scheme strongly affects performance
5. **Scale gradually**: Increase network size while monitoring timing behavior

## Pitfalls

- **Timing hazards**: Asynchronous circuits may have race conditions
- **Verification difficulty**: Standard formal verification tools assume synchronous design
- **Synthesis tools**: May optimize away intended asynchronous behavior
- **Portability**: FPGA-specific implementations may not transfer to ASIC
- **Debugging**: No clock edge means harder to capture state snapshots

## Key Research (arXiv:2605.16114)

Gomes & Rontani (2026) demonstrated a complete B-SNN (Boolean Spiking Neural Network) pipeline:
- 196 neurons on FPGA in a 7×7×4 grid with local connectivity (cortical column inspired)
- Dale's principle: separate excitatory/inhibitory populations (20% inhibitory)
- Receptive neurons (CM=2) vs regular neurons (CM=4) for differentiated responsiveness
- Synaptic weights embedded in circuit structure (not registers) via delayed-path replication
- Synaptic delays via inverter chains (τp = 560±20 ps per stage)
- Distance-based connectivity: P(a,b) = Γ·exp(‖a-b‖²/λ²) with λ=2.2
- Liquid State Machine approach for audio classification (SHD dataset)
- Nanosecond-scale spikes (2.07 ns width) vs 10 ns measurement clock
- UDP/Ethernet interface for real-time spike event streaming

## Related Skills

- [[spiking-neural-networks]]: SNN algorithms and training
- [[neuromorphic-hardware]]: Neuromorphic chip architectures
- [[fpga-acceleration]]: FPGA design and optimization
