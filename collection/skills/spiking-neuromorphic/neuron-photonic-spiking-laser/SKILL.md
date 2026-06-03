---
name: neuron-photonic-spiking-laser
description: "Photonic spiking neurons using multi-junction VCSELs (NeuronSEL) with negative differential resistance. Neuromorphic photonics for ultra-fast optical information processing. Triggers: photonic neuron, VCSEL, neuromorphic photonics, spiking laser, optical computing."
---

# Neuron Surface Emitting Laser (NeuronSEL): Photonic Spiking Neurons

> Compact, scalable photonic spiking neurons using multi-junction Vertical Cavity Surface Emitting Lasers (VCSELs) exhibiting negative differential resistance and diverse neuro-mimetic spiking regimes.

## Metadata
- **Source**: arXiv:2604.12893v1
- **Authors**: Maria Duque-Gijon, Joshua Robertson, Dafydd Owen-Newns, et al.
- **Published**: 2026-04-14
- **Institution**: University of Strathclyde, University of Manchester

## Core Methodology

### Key Innovation
NeuronSEL introduces a compact photonic neuron architecture based on solitary multi-junction VCSELs that generate neuro-mimetic optical spikes through intrinsic negative differential resistance (NDR). Unlike previous approaches requiring external electrical circuits or multiple coupled devices, NeuronSEL achieves all spiking regimes—Class I/II excitability, bursting, mixed-mode oscillations, and chaotic firing—within a single laser device, enabling highly scalable and energy-efficient neuromorphic photonic systems.

### Physical Mechanism

#### Multi-Junction VCSEL Structure
```
[DBR Mirror] - [Active Region 1] - [Tunnel Junction] - [Active Region 2] - [DBR Mirror]
              ↓                      ↓                    ↓
         Gain section           Current control        Modulation section
```

#### Negative Differential Resistance
The series connection of two active regions creates an S-shaped current-voltage characteristic:
- **Low current state**: Only Active Region 1 lases
- **Transition region**: Negative differential resistance as carrier distribution redistributes
- **High current state**: Both regions lase, increased optical output

This NDR enables excitable dynamics analogous to biological neuron's voltage-gated ion channels.

#### Spiking Generation
```
Input current pulse → Charge accumulation → Threshold crossing → 
Fast optical spike emission → Refractory period → Reset
```

### Spiking Regimes

| Regime | Characteristics | Application |
|--------|----------------|-------------|
| **Class I** | Continuous firing rate increase with input strength | Rate coding, analog computation |
| **Class II** | Discontinuous onset of firing at threshold | Event detection, coincidence detection |
| **Bursting** | Packets of spikes separated by quiescence | Packet coding, feature binding |
| **Mixed-Mode** | Alternating single spikes and bursts | Multiplexed coding |
| **Chaotic** | Irregular, aperiodic spike trains | Reservoir computing, random number generation |

### Device Characteristics
- **Size**: < 100 μm diameter
- **Power consumption**: 1-10 mW
- **Spike duration**: ~100 ps (picoseconds)
- **Refractory period**: ~1 ns
- **Speed**: 1000× faster than biological neurons
- **Wavelength**: 850-980 nm (GaAs quantum wells)

## Implementation Guide

### Prerequisites
- Optical testing setup: fast photodetectors (>10 GHz), oscilloscope
- Current drivers: high-bandwidth (>1 GHz), low noise
- Temperature control: thermoelectric cooler, ±0.01°C stability
- Optical coupling: lensed fibers, micropositioning stages

### Step-by-Step: Device Characterization

1. **DC Characterization**
```python
import numpy as np
import matplotlib.pyplot as plt

def characterize_neuronsel(device, current_range):
    """Measure L-I curve and identify NDR region"""
    currents = np.linspace(0, current_range, 1000)
    voltages = []
    optical_powers = []
    
    for I in currents:
        device.set_current(I)
        time.sleep(0.01)  # Settling time
        voltages.append(device.read_voltage())
        optical_powers.append(device.read_optical_power())
    
    # Find NDR region (dV/dI < 0)
    differential_resistance = np.diff(voltages) / np.diff(currents)
    ndr_start = np.where(differential_resistance < 0)[0][0]
    
    return {
        'I': currents,
        'V': voltages,
        'P_opt': optical_powers,
        'NDR_region': (currents[ndr_start], currents[ndr_start+100])
    }
```

2. **Spiking Response Measurement**
```python
def measure_spiking_response(device, pulse_amplitudes, pulse_width=100e-12):
    """Map input-output relationship for different spiking regimes"""
    results = {}
    
    for amp in pulse_amplitudes:
        # Apply current pulse
        device.pulse_current(amp, pulse_width)
        
        # Capture optical response
        response = device.capture_optical_trace(duration=10e-9)
        
        # Analyze spiking pattern
        spike_times = detect_spikes(response, threshold=0.5)
        
        results[amp] = {
            'trace': response,
            'spike_times': spike_times,
            'spike_count': len(spike_times),
            'firing_rate': len(spike_times) / 10e-9
        }
    
    return results

def detect_spikes(trace, threshold):
    """Detect spike times from optical trace"""
    above_threshold = trace > threshold * np.max(trace)
    crossings = np.diff(above_threshold.astype(int)) > 0
    return np.where(crossings)[0] * trace['dt']
```

3. **Neuromorphic Synapse Implementation**
```python
class PhotonicSynapse:
    """Optical synapse using SOA or MZM"""
    
    def __init__(self, weight=1.0, delay=1e-9):
        self.weight = weight
        self.delay = delay
        self.soa_gain = 10 ** (weight / 10)  # Convert dB to linear
    
    def process(self, input_spike_train):
        """Apply weighted delay to spike train"""
        output = []
        for spike_time in input_spike_train:
            if self.weight > 0:  # Excitatory
                output.append({
                    'time': spike_time + self.delay,
                    'amplitude': self.soa_gain
                })
            else:  # Inhibitory - requires interferometric setup
                output.append({
                    'time': spike_time + self.delay,
                    'amplitude': -abs(self.soa_gain),
                    'phase_shift': np.pi
                })
        return output
```

4. **Simple SNN with NeuronSEL**
```python
class NeuronSELLayer:
    """Layer of NeuronSEL devices"""
    
    def __init__(self, n_neurons, connectivity_matrix):
        self.neurons = [NeuronSELDevice() for _ in range(n_neurons)]
        self.connectivity = connectivity_matrix
        self.synaptic_weights = np.random.randn(n_neurons, n_neurons) * 0.1
    
    def simulate_step(self, input_currents, dt=1e-12):
        """Simulate one timestep"""
        # Update each neuron
        for i, neuron in enumerate(self.neurons):
            # Sum synaptic inputs
            synaptic_input = sum(
                self.synaptic_weights[j, i] * spike 
                for j, spike in enumerate(self.last_spikes)
            )
            
            # Total input current
            I_total = input_currents[i] + synaptic_input
            
            # Update neuron state
            neuron.step(I_total, dt)
            
            # Check for spike
            if neuron.voltage > neuron.threshold:
                self.spike_times[i].append(self.current_time)
                self.last_spikes[i] = 1
                neuron.reset()
            else:
                self.last_spikes[i] = 0
        
        self.current_time += dt
```

## Applications

### 1. Ultra-Fast Optical Neural Networks
- **Inference acceleration**: 1000× speedup over electronic SNNs
- **High-frequency signal processing**: RF spectrum analysis, radar
- **Real-time video processing**: Frame rates >100 kHz

### 2. Optical Reservoir Computing
- **Time series prediction**: Chaotic systems, financial data
- **Speech recognition**: Ultra-fast phoneme classification
- **Optical channel equalization**: Compensation for fiber dispersion

### 3. Spike-Based Optical Computing
- **Event-based vision**: DVS camera processing at optical speeds
- **Neuromorphic sensing**: Lidar, radar signal processing
- **Optical AI accelerators**: Matrix-vector multiplication in photonics

### 4. Secure Communications
- **Chaotic encryption**: Physical layer security through chaotic carriers
- **Spike-based coding**: Covert optical communications
- **Random number generation**: True randomness from quantum noise

## Pitfalls

### Thermal Stability
- **Problem**: NDR characteristics are temperature-sensitive
- **Solution**: Active temperature control; calibrate for operating temperature; use feedback stabilization

### Variability Between Devices
- **Problem**: Manufacturing tolerances cause parameter spread
- **Solution**: On-chip calibration circuits; adaptive learning rules; device selection/binning

### Optical Crosstalk
- **Problem**: Light coupling between closely spaced devices
- **Solution**: Optical isolation trenches; angled emission; wavelength multiplexing

### Electrical Interconnect Bottleneck
- **Problem**: Electrical I/O limits system bandwidth
- **Solution**: All-optical networks; wavelength routing; on-chip integration with silicon photonics

## Related Skills
- vo2-mott-oscillator-spiking-neurons: VO2 Mott oscillators for spiking neurons
- neuromorphic-photonic-reservoir: Quantum photonic reservoir computing
- event-driven-neuromorphic-transceiver: Event-driven optical communications

## References
```bibtex
@article{duquegijon2026neuronsel,
  title={Neuron Surface Emitting Laser (NeuronSEL): Spiking Regimes and Negative Differential Resistance in Solitary Multi-junction VCSELs},
  author={Duque-Gijon, Maria and Robertson, Joshua and Owen-Newns, Dafydd and others},
  journal={arXiv preprint arXiv:2604.12893},
  year={2026}
}
```
