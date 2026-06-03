---
name: clockless-fpga-neuromorphic-scaling
description: >
  Scalable neuromorphic computing via clockless (asynchronous) FPGA-based Boolean spiking neurons.
  Use when: designing scalable neuromorphic architectures, implementing autonomous time-continuous
  spiking dynamics on commercial FPGAs, building energy-efficient Boolean neural processors without
  custom ASIC, or studying emergent spiking behavior from asynchronous digital circuits.
  Covers excitatory/inhibitory synaptic weight configuration, audio classification benchmarks,
  and scaling strategies for multi-FPGA neuromorphic systems.
  arXiv: 2605.16114 (2026-05-15)
---

# Clockless FPGA Neuromorphic Scaling

## Paper Reference

**Title:** Scalable neuromorphic computing from autonomous spiking dynamics in a clockless reconfigurable chip  
**arXiv:** 2605.16114 (2026-05-15)  
**Category:** cs.NE

## Core Concept

Proposes a **scalable neuromorphic architecture** where spiking dynamics emerge from
the **autonomous time-continuous evolution of clockless (asynchronous) digital circuits**.
Implemented on **commercial FPGAs**, eliminating the need for custom neuromorphic ASICs
while maintaining event-driven energy efficiency.

## Key Innovation

Unlike prior clockless neuromorphic approaches (e.g., Loihi, TrueNorth, or earlier
Boolean spiking neuron implementations), this work achieves **scalability** on
commercial reconfigurable hardware. The key insight: Boolean spiking neurons
can be arranged such that **spiking dynamics emerge naturally** from the
asynchronous circuit's autonomous time-continuous evolution, without requiring
a global clock or custom silicon.

## Architecture

### Boolean Spiking Neurons on FPGA
- Each neuron is a **clockless digital circuit** with internal feedback
- State transitions triggered by **input spike arrivals**, not clock edges
- **Excitatory and inhibitory synaptic weights** implemented through configurable
  logic gates and routing delays on the FPGA fabric
- No PLL or clock tree needed — eliminates 30-40% of typical chip power

### Scalability Mechanism
- Network topology configured via FPGA interconnect programming
- Multiple FPGA chips can be **cascaded** for larger networks
- Reconfigurable: change network structure without hardware redesign
- Commercial FPGAs sufficient — no custom neuromorphic chip required

### Emergent Dynamics
- Spiking patterns **emerge autonomously** from the circuit's time-continuous evolution
- No external timing controller or global synchronization needed
- The asynchronous nature provides natural temporal processing capabilities

## Implementation Pipeline

```
Input Data → Spike Encoder → FPGA Neuromorphic Core → Spike Decoder → Output
                  ↓                    ↓                     ↓
             Event/Temporal      Boolean neurons        Classification
             Coding              with E/I weights       or regression
             (rate, temporal,                           (voting, readout)
              delta modulation)
```

### Spike Encoding Strategies

```python
def rate_encode(signal, max_rate=1000, window_ms=100):
    """Convert continuous signal to spike train via rate coding"""
    # Map signal amplitude to spike frequency
    pass

def temporal_encode(signal):
    """Encode via precise spike timing (latency coding)"""
    # Lower value → earlier spike
    pass

def delta_encode(signal, threshold=0.1):
    """Delta modulation: spike on significant change"""
    # Event-based encoding for sparse data
    pass
```

### FPGA Configuration

```
FPGA Resources Used:
├── Lookup Tables (LUTs) → Boolean neuron logic
├── Flip-flops → State storage (asynchronous)
├── Routing fabric → Synaptic connectivity
├── BRAM → Weight configuration (optional)
└── I/O pins → Spike input/output channels
```

## Energy Efficiency

| Metric | Value |
|--------|-------|
| Clock tree power | Eliminated (30-40% savings) |
| Active power | Proportional to spike rate |
| Idle power | Near-zero (no clock) |
| vs. DNN equivalent | 10-100x lower for sparse patterns |

## Demonstrated Applications

### Audio Classification
- MFCC features → spike encoding → neuromorphic classification
- **Competitive accuracy** vs. traditional DNNs on standard benchmarks
- Significantly lower power consumption for deployment

### Potential Applications
- Event-based vision (DVS sensor → direct spike input)
- Temporal pattern recognition (gesture, anomaly detection)
- Edge AI deployment on FPGA-based embedded systems
- Real-time low-power signal processing

## Design Guidelines

1. **Start small**: Begin with 10s of neurons, validate spiking dynamics
2. **Verify timing**: Check for race conditions in asynchronous circuits
3. **Profile power**: Measure actual energy consumption vs. clocked baseline
4. **Optimize encoding**: Spike encoding scheme critically affects performance
5. **Scale gradually**: Cascade FPGAs while monitoring inter-chip timing

## Pitfalls

- **Timing hazards**: Asynchronous circuits may have race conditions or metastability
- **Synthesis tools**: May optimize away intended asynchronous behavior
- **Verification**: Standard formal verification tools assume synchronous design
- **Debugging**: No clock edge makes state capture difficult
- **Portability**: FPGA-specific implementations may not transfer to ASIC directly
- **Thermal drift**: Temperature affects gate delays, potentially altering dynamics

## Comparison with Related Approaches

| Approach | Hardware | Clock | Scalability | Custom Chip |
|----------|----------|-------|-------------|-------------|
| This work | Commercial FPGA | No | High (cascadable) | No |
| Loihi | Intel ASIC | Event-driven | Medium | Yes |
| TrueNorth | IBM ASIC | Event-driven | High | Yes |
| SpiNNaker | ARM array | Yes | High | Yes |
| Earlier Boolean | FPGA | No | Low | No |

## Related Skills

- [[clockless-asynchronous-neuromorphic-computing]]: Earlier clockless Boolean spiking neuron work
- [[spiking-neural-network-analysis]]: SNN paper analysis methodology
- [[spikingjelly-framework]]: SNN deep learning framework
- [[edgespike-edge-iot-snn]]: Edge SNN deployment

## Activation Keywords

- clockless FPGA neuromorphic
- asynchronous spiking dynamics
- Boolean spiking neurons FPGA
- scalable neuromorphic computing
- 2605.16114
