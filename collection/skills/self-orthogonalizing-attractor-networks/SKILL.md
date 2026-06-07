---
name: self-orthogonalizing-attractor-networks
description: "Formalizes how attractor networks emerge from the free energy principle applied to universal partitioning of random dynamical systems. Results in self-orthogonalizing attractor representations, biologically plausible multi-level Bayesian active inference. Use when: studying attractor dynamics in neural networks, free energy principle applications, Bayesian active inference models, biologically plausible learning, Boltzmann Machine variants, self-organizing neural dynamics. Triggered by: free energy principle attractor networks, self-orthogonalizing attractors, Spisak Friston attractor, Bayesian active inference attractor, free energy landscape neural networks, attractor neural network emergence."
category: ai_collection
tags: [free-energy-principle, attractor-networks, bayesian-inference, active-inference, boltzmann-machine, self-organization, computational-neuroscience, friston]
---
# Self-Orthogonalizing Attractor Neural Networks Emerging from the Free Energy Principle

**arXiv:** [2505.22749](https://arxiv.org/abs/2505.22749) (v2, updated May 21, 2026)
**Authors:** Tamas Spisak, Karl Friston
**Journal:** Neurocomputing (2026), 133472
**Categories:** q-bio.NC, cs.AI, cs.LG, cs.NE

## Core Idea

Attractor networks — the backbone of many neural computation models — are shown to **emerge naturally from the free energy principle (FEP)** applied to a universal partitioning of random dynamical systems. No externally imposed learning or inference rules are needed; the dynamics self-organize into efficient, biologically plausible Bayesian active inference.

## Key Theoretical Framework

### From FEP to Attractors

1. **Universal Partitioning**: Any random dynamical system can be partitioned into internal, external, and blanket states (Markov blanket formalism)
2. **Free Energy Minimization**: Applying the FEP to this partitioned system yields variational free energy minimization dynamics
3. **Emergent Attractor Structure**: The resulting dynamics naturally form attractors on the free energy landscape — **attractors encode prior beliefs**

### Multi-Level Bayesian Active Inference

The framework produces three integrated levels:
- **Inference**: Sensory data integrated into posterior beliefs via attractor dynamics
- **Learning**: Couplings fine-tuned to minimize long-term surprise (prediction error)
- **Action**: Active inference selects actions that resolve uncertainty

### Self-Orthogonalization Property

**Key theoretical result**: The networks favor **approximately orthogonalized attractor representations** — a consequence of simultaneously optimizing:
- **Predictive accuracy** (fitting data)
- **Model complexity** (keeping representations distinct)

This orthogonalization:
- Efficiently spans the input subspace
- Enhances **generalization** to novel inputs
- Maximizes **mutual information** between hidden causes and observable effects

### Symmetric vs. Asymmetric Coupling Regimes

| Condition | Coupling Structure | Dynamics |
|-----------|-------------------|----------|
| Random data presentation | Symmetric, sparse | Equilibrium (Boltzmann Machine-like) |
| Sequential/temporal data | Asymmetric | Non-equilibrium steady-state |

This offers a **natural generalization of conventional Boltzmann Machines** to temporal domains.

## Analytical Results

The paper derives analytically (and validates via simulation):

1. **Free energy landscape**: Attractors correspond to local minima of variational free energy
2. **Orthogonalization gradient**: Learning dynamics push attractor representations toward orthogonality
3. **Mutual information bound**: Self-orthogonalizing attractors maximize a lower bound on mutual information
4. **Complexity-accuracy trade-off**: Explicit Pareto frontier between fit and model complexity

## Simulation Results

- Random data → symmetric sparse couplings (classical Hopfield/Boltzmann behavior)
- Sequential data → asymmetric couplings with non-equilibrium dynamics
- Self-orthogonalization verified across multiple network sizes and input dimensionalities
- Generalization performance improves with orthogonalization degree

## Implications

### For Computational Neuroscience
- Provides a **first-principles derivation** of attractor dynamics in neural circuits
- Explains why cortical representations tend toward **orthogonal/uncorrelated codes**
- Links **free energy minimization** to attractor network dynamics — unifying predictive coding and Hopfield networks
- Biologically plausible: no global objective, no backpropagation — only local free energy gradients

### For AI / Machine Learning
- New class of **self-organizing attractor networks** requiring no explicit training protocol
- Theoretical foundation for **biologically plausible alternatives to backprop**
- Natural extension to **temporal sequence processing** via asymmetric coupling regime
- Formal link between Boltzmann Machines, Hopfield Networks, and FEP

### For Active Inference Research
- Provides the missing **attractor dynamics microfoundation** for active inference
- Explains how **prior beliefs are encoded** as attractor states
- Framework for **multi-scale** Bayesian inference in hierarchical networks

## Key Equations (Conceptual)

1. **Free energy landscape**: F(s) = -log P(s) + KL[q(θ|s) || p(θ)] where s are system states
2. **Attractor dynamics**: ds/dt = -∇F(s) → relaxation to minima
3. **Orthogonalization objective**: min tr(W^T W - I)^2 + λ∥W∥₁ (sparsity + orthogonality)
4. **Mutual information bound**: I(z; x) ≥ H(z) - ⟨F(z, x)⟩

## Related Skills
- predictive-coding-light (related FEP-based framework)
- attractor-models-language-reasoning (attractor methods for LLMs)
- free-energy-moe-routing (FEP in mixture-of-experts)
- cornn-convex-rnn-optimization (alternative RNN attractor framework)

## Activation Keywords
- free energy principle attractor networks
- self-orthogonalizing attractors
- Spisak Friston attractor neural network
- Bayesian active inference attractor
- free energy landscape neural networks
- attractor neural network emergence
- FEP Boltzmann Machine
- orthogonal attractor representations
- Neurocomputing 133472
