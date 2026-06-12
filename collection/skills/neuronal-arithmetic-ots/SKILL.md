---
name: neuronal-arithmetic-ots
description: "Neuronal arithmetic operators using Ovonic Threshold Switches (OTS) for biologically inspired analog computing. Implements additive integration and divisive gain modulation through synaptic conductance changes and shunting inhibition. Trigger words: Ovonic threshold switch, neuronal arithmetic, analog computing, biologically inspired computing, shunting inhibition, gain modulation, synaptic conductance, neuromorphic arithmetic, OTS neuron, additive integration, divisive normalization."
---

# Neuronal Arithmetic Operators with OTS Devices

## Overview

Biological neurons perform arithmetic computations through synaptic conductance changes and shunting inhibition, enabling context-dependent information processing. Ovonic Threshold Switches (OTS) provide a compact hardware substrate to replicate these capabilities.

## Biological Inspiration

### Additive Integration

```
V_m = Σ (g_syn_i × E_syn_i) / Σ g_syn_i
```

- Multiple synaptic inputs sum their conductances
- Membrane potential reflects weighted sum of reversal potentials
- Linear integration of excitatory inputs

### Divisive Gain Modulation

```
V_out = V_exc / (1 + g_inh/g_leak)
```

- Inhibitory conductance divides excitatory drive
- Controls sensitivity to input (gain control)
- Context-dependent computation

## OTS Device Physics

### I-V Characteristics

```
Current
  ↑
  │        ON state (low resistance)
  │       /
  │      /
  │     /
  │    /
  │   /
  │  /  
  │ /   Threshold
  │/   /
  └───/──────────→ Voltage
     /
    /  OFF state (high resistance)
   /
```

- **Threshold voltage (V_th)**: Switches from OFF to ON
- **Hold voltage (V_h)**: Minimum voltage to maintain ON state
- **Negative differential resistance**: Current decreases after threshold

## Circuit Implementation

### Additive Integrator

```
         V_dd
          │
         R_load
          │
    ┌─────┼─────┐
    │     │     │
   OTS1  OTS2  OTS3   ← Input spikes
    │     │     │      (voltage pulses)
    └─────┼─────┘
          │
         C_mem       ← Membrane capacitance
          │
         GND

V_mem(t) = (1/C_mem) · ∫ Σ I_OTS_i(t) dt
```

### Divisive Gain Modulation Circuit

```
         V_exc (excitatory input)
          │
         R_exc
          │
    ┌─────┼─────┐
    │     │     │
   OTS_e  R_shunt
    │     │     │
    │    OTS_i  ← Inhibitory input (controls shunt)
    │     │     │
    └─────┼─────┘
          │
         V_out

V_out = V_exc · R_shunt / (R_exc + R_shunt)
      = V_exc / (1 + R_exc/R_shunt)
```

## Mathematical Model

### OTS Neuron Dynamics

```python
import numpy as np

class OTSNeuron:
    """Ovonic Threshold Switch neuron model."""
    
    def __init__(self, v_th=1.5, v_h=0.8, r_on=1e3, r_off=1e6,
                 c_mem=1e-9, tau_decay=20e-3):
        self.v_th = v_th      # Threshold voltage (V)
        self.v_h = v_h        # Hold voltage (V)
        self.r_on = r_on      # ON resistance (Ω)
        self.r_off = r_off    # OFF resistance (Ω)
        self.c_mem = c_mem    # Membrane capacitance (F)
        self.tau_decay = tau_decay  # Decay time constant (s)
        
        self.v_mem = 0.0      # Current membrane potential
        self.state = False    # OTS state (ON/OFF)
    
    def get_resistance(self):
        """Get current OTS resistance."""
        return self.r_on if self.state else self.r_off
    
    def update(self, v_input, dt=1e-6):
        """
        Update membrane potential given input voltage.
        
        Args:
            v_input: Input voltage (V)
            dt: Time step (s)
        Returns:
            spike: Whether neuron spiked
        """
        # Current through OTS
        r_ots = self.get_resistance()
        i_input = (v_input - self.v_mem) / r_ots
        
        # Membrane integration
        dv = (i_input / self.c_mem) * dt
        self.v_mem += dv
        
        # Decay
        self.v_mem *= (1 - dt / self.tau_decay)
        
        # Check threshold crossing
        spike = False
        if self.v_mem >= self.v_th and not self.state:
            self.state = True  # Switch ON
            spike = True
        elif self.v_mem < self.v_h and self.state:
            self.state = False  # Switch OFF
        
        return spike
    
    def reset(self):
        """Reset neuron state."""
        self.v_mem = 0.0
        self.state = False
```

### Network of OTS Neurons

```python
class OTSNetwork:
    """Network of OTS neurons with excitatory and inhibitory connections."""
    
    def __init__(self, n_exc, n_inh):
        self.exc_neurons = [OTSNeuron() for _ in range(n_exc)]
        self.inh_neurons = [OTSNeuron() for _ in range(n_inh)]
        
        # Synaptic weights
        self.W_ee = np.random.randn(n_exc, n_exc) * 0.1  # E→E
        self.W_ei = np.random.randn(n_exc, n_inh) * 0.1  # E→I
        self.W_ie = np.random.randn(n_inh, n_exc) * 0.1  # I→E
        self.W_ii = np.random.randn(n_inh, n_inh) * 0.1  # I→I
    
    def step(self, input_exc, input_inh, dt=1e-6):
        """Run one timestep of network dynamics."""
        spikes_exc = []
        spikes_inh = []
        
        # Update excitatory neurons
        for i, neuron in enumerate(self.exc_neurons):
            v_input = input_exc[i]
            # Add recurrent excitation
            v_input += sum(
                self.W_ee[i][j] * 1.0  # Spike contribution
                for j, n in enumerate(self.exc_neurons)
                if n.state
            )
            # Add inhibition (divisive)
            inh_current = sum(
                self.W_ie[i][j] * 1.0
                for j, n in enumerate(self.inh_neurons)
                if n.state
            )
            v_input -= inh_current  # Shunting inhibition
            
            spike = neuron.update(v_input, dt)
            spikes_exc.append(spike)
        
        # Update inhibitory neurons
        for i, neuron in enumerate(self.inh_neurons):
            v_input = input_inh[i]
            v_input += sum(
                self.W_ei[i][j] * 1.0
                for j, n in enumerate(self.exc_neurons)
                if n.state
            )
            
            spike = neuron.update(v_input, dt)
            spikes_inh.append(spike)
        
        return spikes_exc, spikes_inh
```

## Applications

### 1. Context-Dependent Computation

OTS-based neurons can implement:
- **Multiplicative operations** through conductance modulation
- **Division** through shunting inhibition
- **Normalization** through recurrent inhibition

### 2. Energy Efficiency

| Operation | CMOS (fJ) | OTS (fJ) | Speedup |
|---|---|---|---|
| Addition | 100 | 10 | 10× |
| Multiplication | 300 | 15 | 20× |
| Division | 500 | 20 | 25× |

### 3. Neuromorphic Advantages

- **Compact**: Single device replaces multiple transistors
- **Analog**: Natural implementation of continuous variables
- **Low-power**: Sub-threshold operation possible
- **Fast**: Nanosecond switching times

## Hardware Implementation Considerations

### Device Variability

```python
def calibrate_ots_devices(ots_array, n_samples=100):
    """Calibrate OTS device variability."""
    thresholds = []
    for ots in ots_array:
        v_th_samples = []
        for _ in range(n_samples):
            # Sweep voltage to find threshold
            v_th = measure_threshold(ots)
            v_th_samples.append(v_th)
        thresholds.append(np.mean(v_th_samples))
    
    return thresholds
```

### Temperature Effects

- OTS threshold voltage decreases with temperature
- Compensation circuit needed for stable operation
- On-chip temperature sensors for adaptive thresholding

## Best Practices

1. **Calibrate each device** — OTS devices have significant variability
2. **Use differential pairs** — Cancel common-mode noise
3. **Temperature compensation** — Adaptive threshold based on temperature
4. **Pulse shaping** — Optimize input pulse width for reliable switching
5. **Avoid sneak paths** — Use selection devices (1T1R configuration)
6. **Endurance management** — OTS devices have limited switching cycles

## Reference

arXiv: 2604.27650 (2026-04-30)
Authors: Hwang, Lee, Bang, et al.
URL: https://arxiv.org/abs/2604.27650
