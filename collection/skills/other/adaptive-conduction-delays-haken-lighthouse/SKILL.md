---
name: adaptive-conduction-delays-haken-lighthouse
description: "Adaptive conduction delays and phase locking in spiking Haken Lighthouse networks. Theory of phase-locked activity in delayed spiking networks using analytically tractable event-based neural dynamics. Introduces activity-dependent white matter plasticity with myelination-modulated axonal conduction speed. Activation: Haken Lighthouse, phase locking, conduction delays, myelin plasticity, spike-time perturbations, circulant symmetry, Fourier modes."
---

## Methodology Overview

Analytically tractable theory of phase-locked activity in delayed spiking networks using the Haken Lighthouse model. Derives self-consistency conditions for phase-locked states and linear stability theory formulated directly in spike-time perturbations. Introduces activity-dependent myelination plasticity.

### Key Innovation Points

1. **Haken Lighthouse Model**
   - Event-based description of neural dynamics
   - Analytically tractable (exact solutions possible)
   - Spike-time based framework
   - Phase dynamics approach to spiking networks

2. **Delayed Network Theory**
   - Self-consistency conditions for phase-locked states
   - Linear stability theory in spike-time perturbations
   - Fixed delay networks: analytical solutions
   - Distance-dependent coupling and conduction delays

3. **Circulant Symmetry**
   - Spatially structured ring networks
   - Fourier mode decomposition of stability
   - Distance-dependent delays
   - Ring topology with circulant structure

4. **White Matter Plasticity Rule**
   - Activity-dependent myelination
   - Modulates axonal conduction speed
   - Dynamic communication delays
   - Learning-based delay adaptation

### Activation Keywords

- Haken Lighthouse model, event-based spiking
- Phase locking, phase-locked states
- Conduction delays, axonal delays
- Myelin plasticity, white matter plasticity
- Spike-time perturbations
- Circulant symmetry, Fourier modes
- Delayed autapse, reciprocally coupled networks
- Activity-dependent myelination

### Technical Details

#### Haken Lighthouse Dynamics

```
Event-based formulation:
- Phase variable θ evolves continuously
- Spike occurs when θ reaches threshold
- Reset mechanism after spike
- Analytical solutions for fixed delays
```

#### Self-Consistency Conditions

```
For phase-locked states:
θ_i(t) = θ_0 + ω*t + φ_i
where φ_i satisfies:
φ_i = Σ_j W_ij * sin(φ_j - φ_i - τ_ij)
```

#### Stability Theory

```
Linear stability via spike-time perturbations:
δ(t) = Σ_n A_n * exp(λ_n * t)
where λ_n are eigenvalues of Jacobian
```

#### Myelination Plasticity Rule

```
Delay adaptation:
τ_ij → τ_ij - η * (activity - target)
Conduction speed proportional to myelin thickness
Activity-dependent white matter remodeling
```

### Network Examples

1. **Delayed Autapse**
   - Single neuron with self-feedback
   - Fixed delay loop
   - Phase-locked solutions

2. **Two-Cell Reciprocal Network**
   - Two neurons with reciprocal coupling
   - Distance-dependent delays
   - Phase locking conditions

3. **Ring Networks**
   - N-neuron ring with circulant symmetry
   - Fourier mode decomposition
   - Stability analysis by modes

### Biological Significance

**Myelin Plasticity**
- White matter adapts to activity patterns
- Axonal speed increases with usage
- Learning modifies communication delays
- Dynamic rewiring via myelination

**Delay Adaptation Mechanism**
- Activity → myelin thickness → conduction speed
- Local plasticity rule
- Global network reorganization
- Spike-timing dependent changes

### Applications

1. **Delayed Neural Networks**
   - Phase locking analysis
   - Delay-based computation
   - Synchronization with conduction delays

2. **White Matter Modeling**
   - Activity-dependent myelination
   - Dynamic delay networks
   - Learning-induced connectivity changes

3. **Spike-Time Perturbation Theory**
   - Stability analysis framework
   - Event-based dynamics
   - Analytical tractability

4. **Neuromorphic Engineering**
   - Delay plasticity in hardware
   - Phase-based synchronization
   - Circulant architectures

### Implementation Notes

**Haken Lighthouse Model**
```
θ'(t) = ω - Σ_j W_ij * δ(t - t_j - τ_ij)
where δ is Dirac delta (event-based)
```

**Phase-Locked Solutions**
```
Self-consistency equation:
φ_i = Σ_j W_ij * sin(φ_j - φ_i - τ_ij * ω)
```

**Fourier Stability Analysis**
```
For ring with N neurons:
λ_k = Σ_j W_j * cos(k * 2π/N) * exp(-λ_k * τ_j)
k = 0, 1, ..., N-1
```

### Key Equations

**Event-Based Dynamics**
```
Spike time equation:
t_i^{n+1} = t_i^n + Δ where Δ = 2π/ω (baseline)
with perturbations from incoming spikes
```

**Delay Perturbation**
```
δτ_ij = -η * (r_ij - r_target)
where r_ij is activity on connection i→j
```

**Stability Matrix**
```
J_ij = W_ij * cos(φ_j - φ_i - τ_ij) for fixed delays
Eigenvalue problem for stability
```

### Experimental Observations

- Phase locking emerges for appropriate delays
- Myelination speeds up high-activity pathways
- Plasticity leads to network-wide delay reorganization
- Circulant symmetry enables analytical stability

### Related Skills

- kuramoto-brain-network
- complex-valued-kuramoto-control
- kuramoto-control-theory
- spiking-oscillation-mapping
- adaptive-bistable-qubit-control

### Source

arXiv:2606.21508 - "Adaptive conduction delays and phase locking in spiking Haken Lighthouse networks"
Authors: Stephen Coombes, Rüdiger Thul, Stefan Ruschel, Rachel Nicks
Published: 2026-06-19
Link: http://arxiv.org/abs/2606.21508v1