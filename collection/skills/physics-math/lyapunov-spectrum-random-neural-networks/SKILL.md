---
name: lyapunov-spectrum-random-neural-networks
description: "Full N→∞ Lyapunov spectrum of Sompolinsky chaotic random rate network via minimum-norm tangent response + cavity method, solving 1988 open problem. Establishes extensive chaos analytically."
tags: [lyapunov-spectrum, chaos, random-neural-networks, cavity-method, extensive-chaos, dynamical-systems]
source: "arXiv:2610.12426"
utility_score: 0.88
---

# Lyapunov Spectrum of Random Neural Networks

## Paper Metadata

- **arXiv ID**: 2610.12426
- **Title**: Lyapunov spectrum of random neural networks
- **Authors**: David G. Clark
- **Published**: 2026-10-08
- **Categories**: cond-mat.dis-nn, q-bio.NC
- **Link**: https://arxiv.org/abs/2610.12426
- **Note**: Done in collaboration with AI models GPT-6 Astra and Claude Opus 5.5

## Abstract Summary

The Lyapunov spectrum of a nonlinear recurrent neural network with random asymmetric couplings is calculated in the limit N→∞. The calculation is based on a finite-N identity that expresses the cumulative distribution of Lyapunov exponents as a response function of the tangent-space dynamics, with the tangent trajectory selected by a minimum-norm condition rather than by an initial condition. A cavity method then determines this response function at large N through a self-consistent single-site problem. This result establishes that the chaos in this network is extensive and gives access to diffeomorphism-invariant properties of the dynamics.

## Key Contributions

1. **Full Lyapunov spectrum**: Calculates complete N→∞ spectrum for Sompolinsky chaotic random rate network
2. **Minimum-norm tangent response**: Novel identity using minimum-norm condition rather than initial condition
3. **Cavity method application**: Reduces to self-consistent single-site problem over gain trajectories
4. **Extensive chaos**: Establishes analytically that D_KY/N = 1 − F(s_KY) and h_KS/N are O(1)
5. **Solves 1988 open problem**: First complete analytical solution to this long-standing problem

## Research Implications

- **Chaos theory**: Provides complete characterization of chaos in random neural networks
- **Dynamical systems**: Access to diffeomorphism-invariant properties of network dynamics
- **Neural computation**: Understanding how chaos relates to computational capacity
- **AI-derived results**: First frontier-AI-derived long-open physics result (GPT-6 Astra 100-min autonomous derivation)
- **Validation**: Confirmed against QR simulations (N=4096, g=3/5, δ=0.05–0.5)

## Practical Applications

- Analyze stability and chaos in large neural networks
- Design networks with controlled chaotic dynamics
- Understand relationship between chaos and computational power
- Validate numerical simulations against analytical predictions
- Guide training of recurrent networks to operate near criticality

## Related Work

- Sompolinsky chaotic dynamics (1988)
- Random matrix theory
- Cavity methods in statistical physics
- Edge of chaos hypothesis
- Neural network dynamical systems
