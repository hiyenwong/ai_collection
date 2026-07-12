# Single-Neuron Model Comparison Reference

## Detailed Parameter Guide

### Izhikevich Model Parameters

The Izhikevich model uses 4 parameters (a, b, c, d) to reproduce different firing patterns:

| Neuron Type | a | b | c | d | Firing Pattern |
|-------------|---|---|---|---|----------------|
| Regular Spiking (RS) | 0.02 | 0.2 | -65 | 6 | Adaptation, regular spikes |
| Intrinsically Bursting (IB) | 0.02 | 0.2 | -55 | 4 | Bursting, clusters of spikes |
| Chattering (CH) | 0.02 | 0.2 | -50 | 2 | Repetitive bursting |
| Fast Spiking (FS) | 0.1 | 0.2 | -65 | 2 | No adaptation, fast spikes |
| Thalamo-Cortical (TC) | 0.02 | 0.25 | -65 | 0.05 | Tonic/bursting modes |
| Resonator (RZ) | 0.1 | 0.26 | -65 | 2 | Subthreshold oscillations |
| Low-Threshold Spiking (LTS) | 0.02 | 0.25 | -65 | 2 | Post-inhibitory rebound |

**Validation**: Always compare model output against target neuron type data. Wrong parameter combinations produce non-physical behavior (e.g., negative membrane potentials, infinite firing rates).

### Adaptive Exponential IF (AdEx) Parameters

| Parameter | Typical Range | Biological Meaning |
|-----------|---------------|-------------------|
| τ_m (membrane time constant) | 10-30 ms | Membrane charging speed |
| V_rest (resting potential) | -70 to -60 mV | Baseline membrane potential |
| V_th (threshold) | -50 to -40 mV | Spike initiation threshold |
| Δ_T (slope factor) | 1-5 mV | Sharpness of spike onset |
| τ_w (adaptation time constant) | 100-1000 ms | Adaptation speed |
| a (subthreshold adaptation) | 0-10 nS | Subthreshold adaptation strength |
| b (spike-triggered adaptation) | 10-100 pA | Post-spike adaptation current |

**Critical**: τ_w must match biological data for the target neuron type. Default values (e.g., τ_w=100ms) may not fit all neuron types. Cortical pyramidal neurons typically have τ_w ~ 200-500ms.

## Model Selection Decision Tree

```
Start: What is your use case?
│
├─ Large-scale network simulation (>10⁴ neurons)?
│  ├─ Yes → Need biological realism?
│  │  ├─ Yes → Izhikevich (best trade-off)
│  │  └─ No → LIF (fastest)
│  └─ No → Continue
│
├─ Small circuit with adaptation?
│  ├─ Yes → AdEx (most flexible)
│  └─ No → Continue
│
├─ Theoretical analysis of excitability?
│  ├─ Yes → FitzHugh-Nagumo (analytically tractable)
│  └─ No → Continue
│
├─ Biophysical detail needed?
│  ├─ Yes → Hodgkin-Huxley (gold standard)
│  └─ No → Continue
│
└─ Hardware implementation?
   ├─ FPGA/ASIC → LIF or EIF (simple dynamics)
   └─ Neuromorphic chip → LIF (Loihi, TrueNorth)
```

## Numerical Integration Methods

### Explicit Euler (Simple but Unstable for HH)
```python
# LIF: dt = 0.1ms is usually safe
V[t+1] = V[t] + dt * (-(V[t] - V_rest) + R*I) / τ_m

# HH: dt must be < 0.01ms or use adaptive solver
# Explicit Euler unstable due to stiffness
```

### Runge-Kutta 4 (RK4)
```python
# Good for most models, stable for dt = 0.05-0.1ms
# 4x more expensive per step than Euler, but allows larger dt
```

### Adaptive Solvers (CVODE, RK45)
```python
# Required for HH and multi-compartment models
# Automatically adjusts dt based on error estimates
# scipy.integrate.solve_ivp(method='RK45') or method='BDF'
```

**Rule of thumb**: 
- LIF/EIF: dt = 0.1ms, Euler OK
- AdEx/Izhikevich: dt = 0.05ms, Euler or RK4
- HH/Morris-Lecar: dt < 0.01ms or use adaptive solver

## Spike Timing Precision

### Event-Driven Simulation
For models where exact spike timing matters:
- Detect threshold crossing between t and t+dt
- Use bisection or Newton's method to find exact spike time
- Reset membrane potential at exact spike time
- More accurate but slower than fixed-dt simulation

### Fixed-Dt Simulation
- Spike time error: up to dt/2 per spike
- For dt=0.1ms: error up to 0.05ms per spike
- Accumulates over long simulations
- Acceptable for rate-coded networks, not for precise timing

**Recommendation**: Use event-driven simulation when spike timing precision < 1ms is required. Use fixed-dt (dt ≤ 0.1ms) for rate-coded networks or when computational cost is critical.

## Hardware Implementation Notes

### FPGA Implementation
- LIF: ~100 LUTs, ~50 MHz, ~10⁴ neurons/chip
- EIF: ~200 LUTs, ~30 MHz, ~5000 neurons/chip
- Izhikevich: ~300 LUTs, ~20 MHz, ~3000 neurons/chip

### Neuromorphic Chips
- **Intel Loihi**: LIF with learning rules, 130k neurons/chip
- **IBM TrueNorth**: LIF, 1M neurons/chip, ultra-low power
- **BrainScaleS-2**: AdEx, analog implementation, 10⁴ neurons/wafer

### Trade-offs
- Biological realism vs. neuron count per chip
- Power consumption vs. simulation speed
- Programmability vs. efficiency

**Key insight**: Hardware constraints drive model simplification. LIF dominates neuromorphic hardware because it's the simplest model that captures essential spiking behavior.
