---
name: activity-regeneration-transient-synaptic-memory
description: "A minimal neuronal network model with finite-lifetime synapses to study activity regeneration from silent states via transient synaptic memory. Use when modeling neuronal network dynamics, short-term memory, or silent-state reactivation."
metadata:
  arxiv_id: "2607.14000"
  authors: ["Mozhgan Khanjanianpak", "Alireza Valiadeh"]
  subjects: ["Neurons and Cognition (q-bio.NC)", "Disordered Systems and Neural Networks (cond-mat.dis-nn)", "Statistical Mechanics (cond-mat.stat-mech)"]
---

# Activity Regeneration from Transient Synaptic Memory Skill

This skill implements the model from arXiv:2607.14000 for studying activity regeneration in neuronal networks with transient synaptic memory.

## Core Methodology

The model introduces a minimal neuronal network with finite-lifetime synapses and investigates the mechanism underlying spontaneous activity regeneration following complete neuronal silence.

Key findings:
  - The residual synaptic configuration at the first silent state determines whether network activity terminates after a single activation cycle or spontaneously regenerates an additional cycle.
  - The Latent Excitatory Recruitment (LER) capacity, quantified by the cumulative number of fresh excitatory neurons, is a near-perfect predictor of multi-cycle dynamics.
  - Distinct dynamical outcomes emerge in an otherwise homogeneous neuronal network, demonstrating that transient synaptic memory alone is sufficient to generate diverse future dynamics.

## Implementation Steps

### 1. Define the Neuronal Network Model with Finite-Lifetime Synapses

```python
# Define neuronal and synaptic dynamics
def neuronal_dynamics(V, I_syn, I_ext):
    # Example: integrate-and-fire neuron
    dVdt = (-V + R*I_syn + I_ext) / tau_m
    return dVdt

def synaptic_dynamics(s, t, tau_s):
    # Synaptic variable with exponential decay
    dsdt = -s / tau_s
    return dsdt

# Finite-lifetime synapses: synapses have a lifetime after which they are reset
def update_synapses(synapses, t, lifetime):
    # Remove synapses older than lifetime
    active_synapses = [syn for syn in synapses if t - syn['birth_time'] < lifetime]
    return active_synapses
```

### 2. Simulate Network Activity and Silent States

```python
def simulate_network(N, T, stimulus_duration):
    # Initialize neurons and synapses
    # Apply stimulus for stimulus_duration
    # Then let network evolve in silence
    # Record activity and synaptic states
    pass
```

### 3. Compute Latent Excitatory Recruitment (LER) Capacity

```python
def calculate_LER(synaptic_states):
    # LER: cumulative number of fresh excitatory neurons that can be recruited
    # from the silent state synaptic configuration
    return sum([syn['weight'] for syn in synaptic_states if syn['type'] == 'excitatory' and syn['is_fresh']])
```

### 4. Predict Future Dynamics from Silent State Synaptic Configuration

```python
def predict_future_activity(silent_state_synapses):
    ler = calculate_LER(silent_state_synapses)
    if ler > threshold:
        return "activity_regeneration"
    else:
        return "activity_termination"
```

## Validation

Simulations should reproduce:
  - Activity termination after a single activation cycle for low LER
  - Spontaneous activity regeneration for high LER
  - The near-perfect predictive power of LER for multi-cycle dynamics

## Resources

### scripts/
  - `simulate_network.py` - Simulation of the neuronal network with transient synapses
  - `calculate_ler.py` - Calculation of Latent Excitatory Recruitment capacity
  - `predict_dynamics.py` - Prediction of future activity from silent state

### references/
  - `ornstein_uhlenbeck_process.md` - Mathematical details of the neuronal substrate model (if needed)
  - `finite_lifetime_synapses.md` - Model of synapses with finite lifetime

### assets/
  - `network_diagram.png` - Diagram of the neuronal network model
  - `ler_vs_activity.png` - Plot showing LER vs. activity regeneration

## Activation Keywords

  - activity-regeneration-transient-synaptic-memory
  - transient synaptic memory
  - silent state reactivation
  - latent excitatory recruitment
  - neuronal network dynamics

## Validation

After implementing this skill, verify that:
  1. The model shows activity termination for low LER and regeneration for high LER.
  2. LER is a near-perfect predictor of multi-cycle dynamics.
  3. The silent state synaptic configuration contains sufficient information to predict future evolution.

## References

  Khanjanianpak, M., & Valiadeh, A. (2026). Activity Regeneration from Silent States in Neuronal Networks with Transient Synaptic Memory. arXiv preprint arXiv:2607.14000.

---