---
name: geometric-mean-field-lorentzian-ansatz
description: "Geometric origin of exact mean-field reductions for coupled oscillators and spiking neurons. Shows the Cauchy-Lorentz family is the unique connected 2D family of continuous probability densities invariant under Riccati transport. Unified geometric foundation for Ott-Antonsen and Montbrió-Pazó-Roxin reductions. Explains failure of Gaussian closures. Activation: mean-field reduction, Lorentzian ansatz, Ott-Antonsen, neural mass models, coupled oscillators, population dynamics, Riccati dynamics."
arxiv_id: "2605.23669"
published: "2026-05-22"
authors: "Hugues Berry, Leonardo Trujillo"
tags: [mean-field-reduction, coupled-oscillators, spiking-neurons, neural-mass-models, theoretical-neuroscience, dynamical-systems, geometric-methods]
---

# Geometric Origin of Exact Mean-Field Reductions: Möbius Symmetry and the Lorentzian Ansatz

> Groundbreaking theoretical result proving that the Lorentzian Ansatz — widely used in mean-field reductions of coupled oscillators and spiking neurons — is not heuristic but geometrically necessary. Unifies Ott-Antonsen and Montbrió-Pazó-Roxin reductions under a single geometric principle.

**Source**: arXiv: [2605.23669](https://arxiv.org/abs/2605.23669)

## Core Methodology

### Key Innovation
Low-dimensional descriptions of large systems of coupled oscillators and spiking neurons rely heavily on the Lorentzian Ansatz (used in Ott-Antonsen 2008 and Montbrió-Pazó-Roxin 2015 reductions). This paper proves that its privileged role is geometric rather than heuristic — the Cauchy-Lorentz family is the unique connected two-dimensional family of continuous probability densities invariant under the induced projective transport from Riccati dynamics.

### Technical Framework

1. **Problem Reformulation**: Reformulate the dynamics on the circle, where the problem reduces to finding the unique rotation-invariant probability measure
2. **Stereographic Projection**: Under stereographic projection, the rotation-invariant measure on the circle yields the standard Cauchy law
3. **Projective Action**: Under the full projective action (Möbius transformations), the invariant family extends naturally to the Lorentzian family
4. **Uniqueness Proof**: Prove that the Cauchy-Lorentz family is the unique connected 2D family of continuous densities invariant under Riccati-induced projective transport
5. **Unified Foundation**: Show that both Ott-Antonsen (Chaos 18, 2008) and Montbrió-Pazó-Roxin (Phys. Rev. X 5, 2015) reductions are special cases of this geometric principle
6. **Closure Failure Explanation**: Explain why Gaussian closures fail — the Gaussian family is not invariant under the projective transport induced by Riccati dynamics

### Key Results

- **Cauchy-Lorentz is geometrically necessary**: The Lorentzian Ansatz emerges naturally as the unique invariant family, not as an ad hoc heuristic
- **Unified geometric foundation** for both Ott-Antonsen and Montbrió-Pazó-Roxin reductions under a single Möbius symmetry principle
- **Explains the failure of Gaussian closures**: The Gaussian family is not invariant under projective Riccati transport, explaining why Gaussian moment-closure approaches fail for these systems
- **Identifies structural condition** underlying exact two-parameter reductions
- Provides a principled reason for the remarkable success of Lorentzian-based mean-field reductions in systems of coupled oscillators and spiking neurons

## Applications

- **Neural mass modeling**: Provides theoretical justification for Lorentzian-based neural mass models (QIF networks, theta neuron networks)
- **Population dynamics**: Understand when and why low-dimensional mean-field descriptions exist for large neural populations
- **Coupled oscillator theory**: Geometric foundation for the Ott-Antonsen ansatz widely used in synchronization research
- **Spiking network reductions**: Justifies the Montbrió-Pazó-Roxin approach for reducing spiking neural networks to mean-field equations
- **Closure scheme design**: Explains why Gaussian closures fail and guides the development of alternative closure schemes

## Related Skills

- cavity-method-rnn-analysis
- neural-mass-models-unified
- balanced-network-scaling-conductance
- chaos-synchrony-ei-networks
- dynamic-mean-field-nonlinear-noise
