---
name: jeffreys-flow-sampling
description: "Jeffreys Flow framework for robust Boltzmann generators and rare event sampling. Addresses mode collapse in multi-modal distributions using Jeffreys divergence + Parallel Tempering distillation. Use when: sampling rough energy landscapes, Boltzmann generators, rare events, quantum thermal states, path integral Monte Carlo, avoiding KL divergence mode collapse."
---

# Jeffreys Flow Sampling

Robust generative framework for sampling physical systems with rough energy landscapes, based on the Jeffreys Flow method that mitigates mode collapse in Boltzmann generators.

## Core Problem

**Mode Collapse in Boltzmann Generators:**
- Standard Boltzmann generators use reverse KL divergence
- KL divergence causes catastrophic mode collapse
- Missing modes in multi-modal distributions
- Problem in: rough energy landscapes, metastable states, rare events

**Solution: Jeffreys Flow**

Uses symmetric Jeffreys divergence instead of KL divergence, combined with Parallel Tempering trajectory distillation.

## Key Methods

### 1. Jeffreys Divergence

```
J(P, Q) = D_KL(P|Q) + D_KL(Q|P)  (symmetric)
```

- Balanced: local target-seeking + global mode coverage
- Prevents mode collapse by symmetric formulation
- Corrects inherent inaccuracies through distillation

### 2. Parallel Tempering Distillation

1. Run Parallel Tempering to collect empirical samples
2. Distill PT trajectory data using Jeffreys divergence
3. Train generator on distilled empirical reference
4. Achieve robust mode coverage

### 3. Application Domains

| Domain | Use Case |
|--------|----------|
| Statistical Mechanics | Rare event sampling in rough landscapes |
| Quantum Systems | Path Integral Monte Carlo for thermal states |
| Machine Learning | Multi-modal distribution generation |
| Molecular Dynamics | Metastable state sampling |
| Stochastic Optimization | Replica Exchange SGLD bias correction |

## Activation Keywords

- Jeffreys Flow
- Boltzmann generator
- rare event sampling
- mode collapse
- Parallel Tempering
- multi-modal sampling
- quantum thermal states
- 稀有事件采样
- 多模态分布

## Tools Used

- exec: Run Python simulation scripts
- write: Create analysis scripts, save results
- read: Load reference materials, existing models

## Instructions for Agents

### Step 1: Problem Identification

Identify sampling challenges:
1. Is energy landscape rough/multi-modal?
2. Are rare events critical?
3. Is mode collapse observed with KL divergence?
4. Is Parallel Tempering feasible?

### Step 2: Framework Setup

```python
# Basic Jeffreys Flow structure
class JeffreysFlow:
    def __init__(self, energy_fn, temperatures):
        self.energy = energy_fn
        self.temps = temperatures
        
    def parallel_tempering(self, n_steps):
        """Collect empirical samples via PT"""
        # Run replica exchange at multiple temperatures
        # Store trajectory data
        pass
        
    def jeffreys_divergence(self, p_samples, q_samples):
        """Compute symmetric J divergence"""
        # D_KL(P|Q) + D_KL(Q|P)
        pass
        
    def train_generator(self, empirical_data):
        """Distill PT data with Jeffreys divergence"""
        pass
```

### Step 3: Implementation Considerations

**Temperature Selection:**
- Use geometric progression: T_i = T_0 * r^(i)
- Ensure sufficient overlap between replicas
- Higher T for barrier crossing, lower T for precision

**Distillation Process:**
- Collect sufficient PT trajectory samples
- Use Jeffreys divergence as training objective
- Monitor mode coverage during training

**Validation:**
- Check all modes are captured
- Verify importance sampling weights
- Compare with ground truth where available

### Step 4: Quantum Systems Application

For Path Integral Monte Carlo:

```python
# Quantum thermal state sampling
def quantum_thermal_sampling(potential, temperature, n_particles):
    """
    Jeffreys Flow for quantum thermal states
    
    Key: Sample configurations in imaginary time path integral
    """
    # Path discretization
    # Ring polymer representation
    # Jeffreys Flow for multi-modal path distribution
    pass
```

## Error Handling

### Mode Collapse Still Occurs
- Increase temperature range in PT
- Increase empirical sample count
- Check energy landscape connectivity
- Consider hierarchical tempering

### Slow Mixing
- Optimize replica exchange rate
- Adjust temperature spacing
- Use adaptive tempering schedules

### Importance Sampling Bias
- Use Replica Exchange SGLD with Jeffreys correction
- Apply systematic bias correction from PT reference

## Examples

### Example 1: Multi-modal Distribution

```
User: "Sample from a 2D potential with 5 deep wells, Boltzmann generator keeps missing 2 wells"

Agent:
1. Identify: multi-modal with mode collapse risk
2. Setup: Jeffreys Flow with PT at 5 temperatures
3. Run: PT to collect empirical samples
4. Train: generator with Jeffreys divergence
5. Verify: all 5 wells captured
```

### Example 2: Quantum Thermal State

```
User: "Sample quantum thermal states for a double-well potential at low temperature"

Agent:
1. Identify: quantum system, rare tunneling events
2. Setup: Path Integral representation + Jeffreys Flow
3. Run: PT across imaginary time configurations
4. Train: generator for path distribution
5. Extract: tunneling rate from importance weights
```

## Related Papers

- Jeffreys Flow: Robust Boltzmann Generators (arxiv:2604.05303)
- Boltzmann Generators (Noé et al.)
- Parallel Tempering methods
- Path Integral Monte Carlo literature

## Related Skills

- statistical-sampling-methods
- quantum-monte-carlo
- generative-models-physics

## Notes

- Jeffreys divergence = symmetrized KL divergence
- Key innovation: distillation from PT empirical data
- Prevents catastrophic mode collapse
- Scalable to high-dimensional systems
- Applicable to quantum and classical systems