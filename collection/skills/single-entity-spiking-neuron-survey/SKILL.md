---
name: single-entity-spiking-neuron-survey
description: "Comprehensive survey of single-entity spiking neuron models covering mathematical formulations, biological plausibility, and computational trade-offs. Covers integrate-and-fire variants (LIF, EIF, Izhikevich, AdEx), Hodgkin-Huxley models, FitzHugh-Nagumo, Morris-Lecar, and discrete/continuous analogs for membrane potential dynamics. Activation: spiking neuron model, neuron model survey, LIF, EIF, Izhikevich, AdEx, Hodgkin-Huxley, FitzHugh-Nagumo, Morris-Lecar, membrane potential, biologically plausible neuron, single neuron dynamics, computational neuroscience model"
metadata:
  arxiv_id: "2607.07429"
  published: "2023-10-15"
  authors: "Leon Parepko, Danila Shulepin, Albert Nasybullin"
  venue: "DCNA 2023 (7th Scientific School Dynamics of Complex Networks)"
  tags: [spiking-neural-network, neuron-models, computational-neuroscience, mathematical-modeling, biologically-plausible]
---

# Single-Entity Spiking Neuron Models: Survey

## Overview

Comprehensive survey of mathematical models for biologically plausible single-neuron dynamics. Classifies models by computational complexity, biological fidelity, and use cases. Covers spiking models (integrate-and-fire variants, conductance-based), subthreshold models, and discrete/continuous analogs.

## Core Model Taxonomy

### 1. Integrate-and-Fire (IF) Family

**Leaky Integrate-and-Fire (LIF)**
- Simplest spiking model: RC circuit with threshold
- τ_m dV/dt = -(V - V_rest) + RI(t), spike when V ≥ V_th
- Computationally efficient, analytically tractable
- Limitation: no adaptation, no subthreshold oscillations

**Exponential Integrate-and-Fire (EIF)**
- Adds exponential spike initiation: τ_m dV/dt = -(V-V_rest) + Δ_T exp((V-V_T)/Δ_T) + RI
- Captures sharp spike onset (Na+ channel activation)
- Better fit to cortical neuron data than LIF

**Adaptive Exponential IF (AdEx)**
- EIF + adaptation current w: τ_w dw/dt = a(V-V_rest) - w + bδ(t-t_spike)
- Reproduces adaptation, bursting, regular spiking
- 4-parameter model fits diverse cortical neuron types

**Izhikevich Model**
- 2D ODE: dv/dt = 0.04v² + 5v + 140 - u + I, du/dt = a(bv - u)
- With reset: v ≥ 30 → v=c, u=u+d
- 4 parameters (a,b,c,d) reproduce 8+ firing patterns
- Best trade-off: biological realism + computational efficiency

### 2. Conductance-Based Models

**Hodgkin-Huxley (HH)**
- Gold standard: models Na+, K+, leak conductances
- 4D ODE system with gating variables (m, h, n)
- Biophysically detailed but computationally expensive
- Foundation for all conductance-based models

**Morris-Lecar**
- 2D reduction of HH: V + one recovery variable w
- Captures excitability types I and II
- Bifurcation analysis reveals saddle-node/Hopf transitions

**FitzHugh-Nagumo (FHN)**
- 2D simplification: v' = v - v³/3 - w + I, w' = ε(v + a - bw)
- Qualitative excitability, not quantitatively accurate
- Best for theoretical analysis of excitability

### 3. Discrete/Analog Hybrid Models

**Theta Neuron (Ermentrout-Kopell)**
- Phase model: dθ/dt = 1 - cos(θ) + (1 + cos(θ))I
- Exact reduction from saddle-node on invariant circle
- Analytically tractable for network analysis

**Spike Response Model (SRM)**
- Linear superposition of post-synaptic potentials
- V(t) = Σ η(t-t_i) + Σ ε(t-t_i) * I(t)
- Efficient for large-scale network simulation

## Key Classification Dimensions

### Biological Fidelity vs. Computational Cost

| Model | Dimensions | Firing Patterns | Cost |
|-------|-----------|-----------------|------|
| LIF | 1 | Regular only | Very Low |
| EIF | 1 | Regular + sharp onset | Low |
| AdEx | 2 | 6+ patterns | Low |
| Izhikevich | 2 | 8+ patterns | Low |
| Morris-Lecar | 2 | Type I/II | Medium |
| FHN | 2 | Qualitative | Medium |
| HH | 4 | Full biophysical | High |

### Use Case Selection

- **Large-scale networks (>10⁴ neurons)**: LIF, Izhikevich
- **Small circuits with adaptation**: AdEx, EIF
- **Theoretical analysis**: FHN, theta neuron
- **Biophysical detail**: HH, Morris-Lecar
- **Hardware implementation**: LIF, EIF (simple dynamics)

## Membrane Potential Dynamics

### Subthreshold Regime
- LIF: exponential decay to rest
- AdEx/EIF: subthreshold resonance possible
- HH: complex ion channel interactions

### Spike Initiation
- LIF: instantaneous threshold (unbiological)
- EIF: smooth exponential onset (matches Na+ activation)
- HH: explicit channel dynamics

### After-Spike Dynamics
- LIF: hard reset (no refractory period)
- AdEx: adaptation current creates refractory period
- Izhikevich: reset parameters control refractory behavior

## Applications

### SNN Training
- LIF: surrogate gradient methods (most common)
- AdEx: more realistic but harder to train
- Izhikevich: good for neuromorphic hardware

### Neuromorphic Computing
- LIF/EIF: FPGA, Loihi, TrueNorth implementations
- Hardware constraints drive model simplification

### Computational Neuroscience
- HH: detailed single-neuron modeling
- AdEx: population-level cortical dynamics
- FHN: theoretical excitability analysis

## Pitfalls

- **LIF threshold is unbiological**: real neurons have smooth spike onset; use EIF/AdEx for realistic onset dynamics
- **Izhikevich parameter selection**: wrong (a,b,c,d) combinations produce non-physical behavior; validate against target neuron type
- **HH stiffness**: explicit Euler unstable; use adaptive solvers (RK45, CVODE) for multi-compartment models
- **AdEx adaptation timescale**: τ_w must match biological data; default values may not fit all neuron types
- **Discrete-time simulation**: spike timing errors accumulate; use event-driven simulation or small dt (<0.1ms)

## References

- Paper: arXiv:2607.07429 (Parepko, Shulepin, Nasybullin, DCNA 2023)
- Izhikevich (2003) "Simple model of spiking neurons" - IEEE TNN
- Brette & Gerstner (2005) "Adaptive exponential integrate-and-fire model" - J Neurophysiol
- Hodgkin & Huxley (1952) "A quantitative description of membrane current" - J Physiol
