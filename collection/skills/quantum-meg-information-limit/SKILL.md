---
name: quantum-meg-information-limit
description: "Quantum-limited information capacity analysis for magnetoencephalography (MEG) and brain imaging. Derives fundamental bounds combining Planck's constant, metabolic power, and geometric constraints. Use when analyzing quantum limits in neuroimaging, computing information-theoretic bounds for brain measurement systems, or determining optimal sensor configurations."
tags: ["quantum", "neuroscience", "meg", "information-theory", "brain-imaging"]
related_skills: ["metabolic-quantum-limit-meg", "quantum-neuroscience-analysis", "quantum-biomedical-sensors"]
---

# Quantum MEG Information Limit Methodology

## Overview

This methodology derives fundamental quantum-limited bounds on the information capacity of magnetoencephalography (MEG) by combining:
- Energy resolution limits of quantum magnetic sensors
- Metabolic power available to neural currents
- Geometric attenuation of external magnetic fields

Based on arXiv:2511.06401 (Nov 2025): "Metabolic quantum limit to the information capacity of magnetoencephalography"

## Core Formula

The maximum information rate (C) for MEG factorizes as:

C = f(geometry, metabolism, Planck's constant) ≈ 2.2 Mbit/s (for human brain)

### Key Findings

1. **Information-limited spatial scale**: ~1 cm
2. **High multipole components**: Geometrically attenuated below quantum-limited noise floor
3. **Accessible measurement space**: Effectively finite-dimensional
4. **Spatio-temporal trade-off**: Temporal and spatial bandwidths compete due to quantum-limited noise variance

## Implementation

### Step 1: Calculate Energy Resolution Limit

For SQUIDs or atomic magnetometers:
- Energy resolution: ε = ħ (Planck's constant / 2π)
- Bandwidth limitation: Δf_max = P_metabolic / ε

### Step 2: Compute Geometric Attenuation

External magnetic field multipole expansion:
- Higher-order multipoles attenuate as (r/R)^(l+2)
- Critical l where field < quantum noise floor determines effective dimensionality

### Step 3: Determine Information Capacity

C = (1/2) × N_effective × log2(1 + SNR)

Where:
- N_effective = finite number of measurable multipoles
- SNR limited by metabolic power and quantum noise

## Python Implementation

```python
import numpy as np
from scipy.special import sph_harm

class QuantumMEGLimit:
    """
    Calculate quantum-limited information capacity for MEG systems.
    """
    
    def __init__(self, brain_radius=0.08, sensor_distance=0.1):
        self.R = brain_radius  # Brain radius (m)
        self.r = sensor_distance  # Sensor distance (m)
        self.hbar = 1.054e-34  # Planck's constant / 2π
        self.P_metabolic = 20  # Typical brain metabolic power (W)
    
    def energy_resolution_limit(self):
        """Calculate fundamental energy resolution limit."""
        return self.hbar
    
    def geometric_attenuation(self, multipole_order):
        """Calculate geometric attenuation for multipole l."""
        return (self.R / self.r) ** (multipole_order + 2)
    
    def max_multipole_order(self, noise_floor=1e-15):
        """Find maximum multipole order above quantum noise floor."""
        l = 1
        while self.geometric_attenuation(l) > noise_floor:
            l += 1
        return l - 1
    
    def effective_dimensionality(self, noise_floor=1e-15):
        """Calculate effective measurement space dimensionality."""
        l_max = self.max_multipole_order(noise_floor)
        return (l_max + 1) ** 2  # Number of spherical harmonics
    
    def information_capacity(self, noise_floor=1e-15):
        """Calculate maximum information rate in bits/second."""
        N_eff = self.effective_dimensionality(noise_floor)
        # Simplified SNR based on metabolic power
        SNR = self.P_metabolic / (self.hbar * 1e9)  # Assuming 1 GHz bandwidth
        return 0.5 * N_eff * np.log2(1 + SNR)
    
    def spatio_temporal_tradeoff(self):
        """Analyze bandwidth trade-off between spatial and temporal resolution."""
        results = []
        for bandwidth in [1, 10, 100, 1000]:  # Hz
            noise_var = self.hbar * bandwidth
            l_max = self.max_multipole_order(np.sqrt(noise_var))
            results.append({
                'bandwidth_Hz': bandwidth,
                'max_multipole': l_max,
                'effective_dims': (l_max + 1) ** 2,
                'noise_variance': noise_var
            })
        return results

# Usage
if __name__ == "__main__":
    meg = QuantumMEGLimit()
    print(f"Information capacity: {meg.information_capacity():.1f} Mbit/s")
    print(f"Effective dimensionality: {meg.effective_dimensionality()}")
    print("\nSpatio-temporal tradeoff:")
    for result in meg.spatio_temporal_tradeoff():
        print(f"  {result['bandwidth_Hz']} Hz: {result['effective_dims']} dims")
```

## Application Scenarios

### 1. MEG System Design Optimization
- Determine optimal sensor array density
- Avoid oversampling beyond quantum-limited information content
- Balance spatial vs temporal resolution based on quantum constraints

### 2. Brain-Computer Interface Limits
- Calculate theoretical upper bounds on neural information extraction
- Inform BCI bandwidth expectations
- Guide signal processing algorithm design

### 3. Quantum Sensor Development
- Evaluate sensor performance against fundamental limits
- Identify when improvements require new measurement paradigms
- Guide sensor placement and array configuration

## Workflow

```
1. Define measurement parameters
   ├── Brain geometry (radius, cortical folding)
   ├── Sensor type (SQUID, atomic magnetometer)
   └── Metabolic power estimate

2. Calculate quantum limits
   ├── Energy resolution limit (ħ)
   ├── Geometric attenuation (multipole expansion)
   └── Effective dimensionality (finite measurable modes)

3. Derive information capacity
   ├── Maximum information rate
   ├── Spatio-temporal tradeoff curves
   └── Optimal operating points

4. Apply to system design
   ├── Sensor array optimization
   ├── Signal processing pipeline
   └── Performance validation
```

## Key Parameters

| Parameter | Symbol | Typical Value | Units |
|-----------|--------|---------------|-------|
| Brain radius | R | 0.08 | m |
| Sensor distance | r | 0.1 | m |
| Planck's constant | ħ | 1.054e-34 | J·s |
| Metabolic power | P | 20 | W |
| Info capacity | C | 2.2 | Mbit/s |
| Spatial scale | Δx | 1 | cm |

## References

- arXiv:2511.06401 - Metabolic quantum limit to the information capacity of magnetoencephalography
- Quantum-limited magnetic sensing theory
- Information-theoretic Nyquist scale derivation

## Activation Keywords

- quantum MEG
- MEG information capacity
- brain imaging quantum limits
- metabolic quantum limit
- magnetoencephalography
- neural information bounds
- quantum neuroimaging
- brain measurement limits
