---
name: nbox-memristor-visuotactile-snn
version: "1.0"
description: >
  Self-oscillating NbOx memristor neuron for ultra-low-latency visuotactile perception.
  NbOx devices leverage intrinsic Mott metal-insulator transition and parasitic capacitance
  for simultaneous TTFS (time-to-first-spike) + rate encoding with 260 ns first-spike
  latency. Use when: neuromorphic hardware design, memristive spiking neurons, tactile/visual
  sensor fusion, embodied intelligence hardware, low-latency spike encoding circuits.
tags:
  - memristor
  - NbOx
  - neuromorphic-hardware
  - visuotactile
  - spiking-neuron
  - TTFS
  - rate-coding
  - Mott-insulator
  - metal-insulator-transition
  - embodied-intelligence
activation_keywords:
  - NbOx memristor
  - self-oscillating neuron
  - Mott transition
  - metal-insulator transition
  - visuotactile
  - low latency spike
  - TTFS encoding
  - time-to-first-spike hardware
  - memristive spiking
source:
  pmid: "42183948"
  journal: "Small"
  year: 2026
  title: "Low-Latency Visuotactile Neuron Using Self-Oscillating Memristor"
  authors: ["Li Pengzhan", "Huang Anping", "Huang Jiangshun", "Yang Qiaofeng"]
---

# NbOx Memristor Visuotactile SNN Neuron

## Overview

This skill covers the design and modeling of **self-oscillating NbOx memristor neurons** that achieve ultra-low-latency (260 ns first spike) simultaneous encoding of visual and tactile stimuli. The core innovation is eliminating external capacitors by leveraging **intrinsic parasitic capacitance** of the NbOx device — simplifying circuit integration while achieving biologically plausible TTFS + rate encoding.

**Key contribution**: A single NbOx memristor device functions as a complete integrate-and-fire neuron with:
- Self-oscillating threshold via Mott metal-insulator transition
- 260 ns time-to-first-spike latency
- Simultaneous TTFS and firing rate encoding
- Multimodal (visual + pressure) input fusion

## NbOx Mott Transition Physics

### Metal-Insulator Transition (MIT)
NbOx (typically Nb₂O₄·₅ → NbO₂) undergoes a **thermally-driven Mott transition**:

```
NbO₂ (insulator, R_high ~ MΩ) ←→ NbO (metal, R_low ~ kΩ)
         ↑                              ↑  
   T < T_MIT (~1080 K)         T > T_MIT (Joule heating)
```

**Self-oscillation mechanism**:
1. Apply voltage → current flows → Joule heating
2. Local temperature rises → MIT occurs (resistance drops)
3. Lower resistance → more current → runaway heating avoided by LC/RC circuit
4. Device cools → resistance rises → cycle repeats
5. → **Intrinsic oscillation** at frequency determined by thermal RC time constant

### Circuit Model
```
V_supply
   │
   R_load
   │
   ├── Parasitic C (device capacitance ~1-10 fF)
   │
   NbOx device (R_MIT, thermal model)
   │
  GND
```

The device's threshold switching replaces the need for external capacitors in standard RC integrate-and-fire circuits.

## Spike Encoding Modes

### 1. Time-to-First-Spike (TTFS) Encoding
- **Stronger stimulus** → faster Joule heating → shorter time to reach T_MIT → **earlier first spike**
- Maps stimulus intensity to spike latency
- Enables population coding with relative timing

```python
def ttfs_model(I_stimulus, R_load, C_parasitic, T_ambient=300):
    """
    Simplified TTFS model for NbOx self-oscillating neuron.
    Returns estimated time-to-first-spike in seconds.
    """
    # Thermal capacitance and resistance of NbOx
    C_thermal = 1e-12  # J/K (estimated)
    R_thermal = 1e4    # K/W (estimated)
    T_mit = 1080       # K (Mott transition temperature for NbO2)
    
    # Heating rate at initial resistance (insulating state)
    R_device_initial = 1e6  # Ω (insulating state)
    P_initial = I_stimulus**2 * R_device_initial
    
    # Time to reach MIT temperature (simplified RC thermal model)
    delta_T = T_mit - T_ambient
    tau_thermal = C_thermal * R_thermal
    
    # t = -tau * ln(1 - delta_T / (P * R_thermal))
    import math
    if P_initial * R_thermal <= delta_T:
        return float('inf')  # never reaches MIT
    
    t_first_spike = -tau_thermal * math.log(1 - delta_T / (P_initial * R_thermal))
    return t_first_spike
```

### 2. Rate Encoding
- **After first spike**: oscillation frequency scales with stimulus amplitude
- Rate encoding for sustained stimuli
- Combined with TTFS for temporal precision at onset + rate for sustained response

```python
def oscillation_frequency(I_stimulus, device_params):
    """
    Estimate NbOx oscillation frequency from stimulus current.
    """
    R_on = device_params['R_on']    # ~1 kΩ (metallic state)
    R_off = device_params['R_off']  # ~1 MΩ (insulating state)
    C_par = device_params['C_par']  # parasitic capacitance
    V_th = device_params['V_th']    # threshold voltage
    
    # Charging time (insulating state)
    tau_charge = R_off * C_par
    # Discharging time (metallic state)  
    tau_discharge = R_on * C_par
    
    # Simplified: frequency dominated by charging time
    # In practice, need to solve full thermal + electrical ODE
    f = 1.0 / (tau_charge * -np.log(1 - V_th / (I_stimulus * R_off)))
    return f
```

## Multimodal Sensor Integration

### Visual (Photodetector) + Pressure Sensor Architecture
```
Visual Input (photodetector)        Pressure Input (piezoresistive)
        │                                    │
   I_photo                              I_pressure
        │                                    │
        └────────────┬─────────────────────┘
                     │
            I_total = I_photo + I_pressure
                     │
              NbOx Neuron
              (TTFS + Rate encoder)
                     │
             Spike output to SNN
```

**Key advantage**: Single NbOx device integrates multimodal currents without separate ADC/preprocessing — the spike pattern naturally encodes combined stimulus.

### Temporal Encoding for Sensor Fusion
```python
class NbOxVisuotactileNeuron:
    """
    Simplified model of NbOx self-oscillating multimodal neuron.
    """
    def __init__(self):
        self.state = "OFF"  # "OFF" = insulating, "ON" = metallic
        self.T_device = 300.0  # temperature in K
        self.V_device = 0.0
        
        # Device parameters (approximate for NbO2)
        self.T_mit = 1080.0      # MIT transition temperature
        self.R_off = 1e6         # Insulating resistance (Ω)
        self.R_on = 1e3          # Metallic resistance (Ω)
        self.C_thermal = 5e-13   # Thermal capacitance (J/K)
        self.R_thermal = 1e4     # Thermal resistance (K/W)
        self.T_ambient = 300.0   # Ambient temperature
        self.C_parasitic = 5e-15 # Parasitic electrical capacitance (F)
        
    def step(self, I_in, dt=1e-9):
        """Advance neuron state by dt nanoseconds."""
        # Current resistance
        R = self.R_on if self.state == "ON" else self.R_off
        
        # Power dissipation
        P = I_in**2 * R
        
        # Thermal dynamics
        dT = (P - (self.T_device - self.T_ambient) / self.R_thermal) / self.C_thermal
        self.T_device += dT * dt
        
        # State transition
        spiked = False
        if self.state == "OFF" and self.T_device >= self.T_mit:
            self.state = "ON"
            spiked = True  # First spike!
        elif self.state == "ON" and self.T_device < self.T_mit:
            self.state = "OFF"
        
        return spiked, self.T_device
    
    def run_stimulus(self, I_visual, I_pressure, duration_ns=1000):
        """Simulate neuron response to combined visuotactile stimulus."""
        I_total = I_visual + I_pressure
        spikes = []
        T_trace = []
        
        for t in range(duration_ns):
            spiked, T = self.step(I_total, dt=1e-9)
            if spiked:
                spikes.append(t)  # spike time in ns
            T_trace.append(T)
        
        return spikes, T_trace
```

## Key Performance Metrics

| Metric | NbOx Neuron | Standard CMOS IF | Biological Neuron |
|--------|-------------|------------------|-------------------|
| First spike latency | **260 ns** | ~μs | ~1–10 ms |
| Operating voltage | ~1–3 V | 1.8–3.3 V | ~70 mV |
| Energy/spike | ~10 pJ | ~1–100 pJ | ~10 pJ |
| Footprint | ~μm² | ~10 μm² | ~10 μm soma |
| Multimodal integration | **Native** | External ADC needed | Via dendrites |

## Integration with SNN Frameworks

### Interfacing Hardware Spikes with SpikingJelly
```python
import spikingjelly.activation_based as sj
import torch

class NbOxSpikeTrain(torch.utils.data.Dataset):
    """
    Wraps NbOx hardware spike output as input to SNN layers.
    """
    def __init__(self, raw_spike_times_ns, T_steps=100, dt_ms=1.0):
        """
        raw_spike_times_ns: list of spike times in nanoseconds
        T_steps: number of simulation timesteps
        dt_ms: timestep duration in ms
        """
        self.T = T_steps
        self.dt_ms = dt_ms
        self.spike_times_ms = [t * 1e-6 for t in raw_spike_times_ns]
        
    def to_binary_tensor(self):
        """Convert spike times to binary spike train tensor."""
        spike_train = torch.zeros(self.T)
        for t_ms in self.spike_times_ms:
            t_idx = int(t_ms / self.dt_ms)
            if 0 <= t_idx < self.T:
                spike_train[t_idx] = 1.0
        return spike_train
```

## Design Guidelines

### Choosing NbOx Device Parameters
1. **R_off / R_on ratio**: Higher ratio → sharper threshold switching → cleaner TTFS
2. **Thermal capacitance**: Lower C_thermal → faster response (lower latency) but less stability
3. **Parasitic capacitance**: Must be large enough to sustain oscillation; can be tuned via device geometry
4. **Load resistance**: Set R_load to ~√(R_on × R_off) for optimal oscillation amplitude

### Multi-layer Integration
```
Input layer: NbOx neurons (analog sensor → spikes)
     ↓ spike trains
Hidden layer: Digital SNN (e.g., LIF neurons on-chip)
     ↓ classified features
Output layer: Decision / actuation
```

## Pitfalls

1. **Temperature-dependent variability**: NbOx MIT temperature varies with oxide stoichiometry; device-to-device variation requires calibration
2. **Endurance**: Repeated phase transitions degrade NbOx — typical cycling endurance is 10⁷–10⁸ cycles
3. **Thermal crosstalk**: Densely packed devices may influence neighboring device temperature → spurious spikes
4. **Stochastic switching**: Threshold switching has inherent stochasticity — consider probabilistic spike models
5. **TTFS decoding**: Network must be designed to decode relative spike times, not just rate — requires careful SNN architecture choice

## Related Skills
- `vo2-mott-oscillator-spiking-neurons` — VO2-based Mott oscillator spiking neurons (closely related physics)
- `inhibitory-neuristor-mit` — inhibitory neuristor based on MIT
- `neuromorphic-spiking-ring-attractor-v2` — hardware neuromorphic ring attractor
- `spiking-neural-network-analysis` — general SNN paper analysis
- `analog-neuromorphic-plasticity` — analog neuromorphic hardware plasticity
