---
name: multi-timescale-conductance-snn
description: Multi-Timescale Conductance Spiking Networks (MTCSN) methodology. A gradient-trainable SNN framework where neural dynamics emerge from shaping the I-V curve by tuning fast, slow, and ultra-slow conductances. Enables direct backpropagation through time without surrogate gradients, supports rich firing regimes (tonic, phasic, bursting), and achieves superior temporal processing with high activity sparsity. Use when: designing conductance-based SNNs, building neuromorphic temporal processing systems, comparing SNN neuron models (LIF, AdLIF vs. conductance-based), implementing gradient-trainable spiking networks without surrogate gradients, energy-efficient spike-based computation, Mackey-Glass or chaotic time-series prediction.
  Activation: multi-timescale conductance, MTC SNN, conductance-based SNN, MTCSN, gradient-trainable spiking network, I-V curve shaping, spiking neuron dynamics, neuromorphic temporal processing.
  arXiv: 2605.11835 (2026 IEEE Neuro-Inspired Computational Elements Conference)
---

# Multi-Timescale Conductance Spiking Networks (MTCSN)

Gradient-trainable SNN framework using conductance-based neuron models with multi-timescale dynamics for enhanced temporal processing.

## Core Concept

Replace phenomenological neuron models (LIF, AdLIF) with biophysically grounded **conductance-based dynamics** that:
- Emerge from shaping the **current-voltage (I-V) curve** via tunable conductances
- Enable **direct backpropagation through time (BPTT)** without surrogate gradients
- Support rich firing regimes: tonic, phasic, and bursting within a single model
- Yield substantially **sparser activity** for energy-efficient computation

## Mathematical Framework

### Conductance-Based Neuron Dynamics

The MTC neuron models membrane potential U_m(t) through multiple conductance timescales:

```
τm · dUm/dt = I_in(t) - I_-s - I+_s - I+_us - I^-_s
```

Where:
- **Fast timescale (τm)**: Destabilizing element I⁻_s (negative conductance) drives rapid depolarization
- **Slow timescale (τs ≫ τm)**: Restorative element I⁺_s with positive conductance provides damping and refractory period
- **Ultra-slow timescale (τus ≫ τs)**: Higher-order temporal processing via slow-negative element balanced by positive ultra-slow conductance

### Signal Conditioning

Transform continuous membrane potential to standardized transmission signal:
```
s(t) = min(ReLU(Um(t) - Uth) / (Usat - Uth), 1)
```

This normalizes action potentials to [0,1], ensuring consistent inter-neuron communication.

### Discrete-Time Formulation

The continuous dynamics are discretized for direct BPTT, eliminating the forward-backward mismatch of surrogate gradients.

## Key Advantages vs. Baselines

| Dimension | LIF | AdLIF | MTCSN |
|-----------|-----|-------|-------|
| Trainability | Surrogate gradient | Surrogate gradient | **Direct BPTT** |
| Firing regimes | Single (tonic) | Limited | **Tonic, phasic, bursting** |
| Sparsity | Indirect control | Indirect control | **Emergent from conductance** |
| Temporal processing | Single timescale | Two timescales | **Multi-timescale** |
| Hardware mapping | Limited | Limited | **Analog circuit-ready** |

## Implementation Pattern

```python
# Pseudocode for MTC neuron forward pass
def mtc_neuron_forward(Um, g_slow, g_uslow, I_in, params):
    # Fast destabilizing current (drives spiking)
    I_fast = negative_conductance(Um, params)
    # Slow restorative current (damping)
    I_slow = positive_conductance(Um, g_slow, params)
    # Ultra-slow modulation (bursting/tonic transition)
    I_uslow = positive_conductance(Um, g_uslow, params)
    
    # Update membrane potential
    dUm = I_in - I_fast - I_slow - I_uslow
    Um_new = Um + dt * dUm / tau_m
    
    # Signal conditioning
    s = min(max(Um_new - Uth, 0) / (Usat - Uth), 1)
    return Um_new, s
```

## Evaluation Results

On **Mackey-Glass time-series regression** at the predictability horizon (~1 Lyapunov time):
- **MTC outperforms LIF and AdLIF** in prediction accuracy
- **Substantially sparser activity** in both rate and duty-cycle dimensions
- Feed-forward architecture (no recurrent connections) achieves temporal processing via intrinsic neuron memory

## When to Use

- Building SNNs for **temporal regression** or time-series forecasting
- Needing **multiple firing regimes** in a single neuron model
- **Neuromorphic hardware** implementation where conductance maps to analog circuits
- Replacing surrogate gradient training with **true gradient-based** optimization
- Seeking **high sparsity** for energy-efficient deployment

## Pitfalls

- Feed-forward evaluation only tested; recurrent MTC networks remain unexplored
- Mackey-Glass is canonical but limited; real-world temporal tasks need validation
- Conductance parameters require careful initialization to avoid numerical instability
- Signal conditioning (Saturated ReLU) is a design choice; alternatives may be needed for specific tasks

## References

- Fulleda-Garcia, Soldado-Magraner, Margarit-Taulé (2026). IEEE Neuro-Inspired Computational Elements Conference.
- Ribar & Sepulchre (conductance-based neuron model foundation)
- snnTorch framework (LIF/AdLIF baselines)
