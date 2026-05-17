---
name: balanced-network-scaling-conductance
description: >
  Empirical scaling laws in balanced networks with conductance-based synapses.
  Reveals that conductance-based synapses + spike time correlations cancel to produce
  realistic membrane potential variability — neither alone suffices. Use when: studying
  balanced network models, conductance vs current-based synapses, cortical variability
  modeling, spike time correlations, E/I balanced networks, membrane potential variability.
---

# Balanced Network Scaling with Conductance-Based Synapses

## Paper Reference

- **Title:** Empirical scaling laws in balanced networks with conductance-based synapses
- **Authors:** Vicky Zhu, Gabriel Ocker, Robert Rosenbaum
- **arXiv:** 2605.12404 (May 2026)
- **Categories:** q-bio.NC

## Core Problem

Balanced network models are successful in describing cortical neural recordings, but:
- **Current-based synapses** with spike time correlations → unrealistically **large** membrane potential variability
- **Conductance-based synapses** alone → unrealistically **small** membrane potential variability
- **Neither assumption alone** produces realistic dynamics

## Key Finding: Cancellation Effect

When **both** realistic assumptions are combined:
- Conductance-based synapses + spike time correlations
- The two effects **cancel** each other
- Result: **moderate, realistic** membrane potential variability

This demonstrates that including more realistic modeling assumptions produces more
realistic dynamics, but **only when multiple assumptions are included together**.

## Synapse Model Comparison

### Current-Based Synapses
$$I_{syn}(t) = w \cdot \sum_k \delta(t - t_k)$$
- Simple, analytically tractable
- Overestimates variability with correlations

### Conductance-Based Synapses
$$I_{syn}(t) = g(t) \cdot (V - E_{rev})$$
$$\tau_g \dot{g} = -g + \sum_k \delta(t - t_k)$$
- More biophysically realistic
- Voltage-dependent current
- Underestimates variability alone

## Scaling Laws

The paper establishes empirical scaling relationships for:
1. Membrane potential variance vs. network size
2. Membrane potential variance vs. coupling strength
3. Membrane potential variance vs. spike time correlation strength

These scaling laws show that the cancellation effect persists across network sizes.

## Practical Implications

### Model Selection
- Use conductance-based synapses when spike correlations are present
- Use current-based synapses only for uncorrelated activity regimes
- Combined assumptions are needed for cortical-scale simulations

### Balanced Network Design
- E/I balance + conductance synapses + correlations = realistic Vm variability
- Avoid mixing assumptions (e.g., conductance synapses + no correlations)

### Theoretical Analysis
- The cancellation provides a principled justification for using simpler models
- In some regimes, current-based models with correlations approximate the full model

## Activation Keywords

- balanced network conductance synapse, conductance-based synapse scaling
- membrane potential variability balanced network, E/I balanced network
- current-based vs conductance synapse, spike time correlation variability
- cortical variability modeling, balanced network scaling laws
