---
name: behavior-decomposed-lds
description: >
  Behavior-dLDS: decomposed linear dynamical systems model for neural activity partially
  constrained by behavior. Disentangles behavior-related neural dynamics from internal
  computations in large-scale neural recordings. Scales to tens of thousands of neurons.
  Use when modeling neural population dynamics, decomposing brain activity into behavioral
  vs. internal subsystems, or analyzing brain-wide recordings with behavioral correlates.
  Activation: behavior-dLDS, decomposed linear dynamical systems, neural dynamics decomposition,
  behavior-constrained neural modeling, brain-wide recordings, latent neural dynamics,
  zebrafish neural dynamics, positional homeostasis
---

# Behavior-dLDS: Decomposed Linear Dynamical Systems

Based on arXiv:2603.05612 (Yezerets et al., May 2026).

## Paper Overview

**Title:** Behavior-dLDS: A decomposed linear dynamical systems model for neural activity partially constrained by behavior

**Authors:** Eva Yezerets, En Yang, Misha B. Ahrens, Adam S. Charles

**Published:** Submitted Mar 2026, revised May 4, 2026 (v2)

**Categories:** q-bio.NC, cs.LG, stat.AP, stat.ML

## Core Problem

Brain-wide recordings contain both behavior-related information and internal computations.
Observable behavior is a coarse-grained product of neural activity executed by brain + spinal cord + PNS.
Existing models use behavior to supervise all dynamics, conflating behavioral and internal processes.
Need: disentangle behavior-generating networks from parallel internal computations.

## Key Contributions

### 1. Behavior-Decomposed Linear Dynamical Systems (b-dLDS)

- Decomposes neural activity into behavior-related and behavior-independent subsystems
- Models indirect relationship between behavior and neural dynamics
- Embodies parallel and distributed nature of large-scale neural populations
- Represents behavior via lower-dimensional latent neural dynamics

### 2. Subsystem Disentanglement

- Identifies how latent neural subsystems relate to behavior
- Separates behavior-generating networks from internal computations
- Outperforms models that use behavior to supervise all dynamics

### 3. Scalability

- Demonstrated on simulated data with controlled ground truth
- Applied to task-driven RNN dataset with nonlinear behavior-activation relationships
- Scaled to tens of thousands of neurons on zebrafish hindbrain recordings
- Revealed asymmetry in behavior-related dynamic connectivity networks

## Mathematical Framework

```
Neural State x(t) decomposed into:
├── x_behavior(t): behavior-related latent dynamics
│   └── Directly constrained by observed behavior
├── x_internal(t): behavior-independent latent dynamics
│   └── Captures parallel internal computations
└── Coupling: A_behavior→internal, A_internal→behavior

Linear dynamics:
  x(t+1) = A * x(t) + noise
  where A is block-structured to enable decomposition
```

## Validation Results

| Dataset | Key Finding |
|---------|-------------|
| Simulated data | b-dLDS outperforms behavior-supervised baselines |
| Task-driven RNN | Interpretability benefits on nonlinear behavior relationships |
| Zebrafish hindbrain | Asymmetry in behavior-related dynamic connectivity |

## Application Domains

- Brain-wide calcium imaging analysis
- Electrophysiology population recordings
- Neural decoding with behavioral correlates
- Distinguishing motor vs. cognitive neural activity
- Studying internal states not directly observable in behavior

## Key Insights

- Behavior is a coarse-grained proxy for neural dynamics
- Internal computations run in parallel with behavior generation
- Lower-dimensional latent dynamics best represent behavioral signals
- Decomposition reveals asymmetry in neural connectivity patterns
- Model scales to tens of thousands of recorded neurons

## Activation Keywords

- behavior-dLDS
- decomposed linear dynamical systems
- neural dynamics decomposition
- behavior-constrained modeling
- brain-wide recordings
- latent neural dynamics
- zebrafish neural analysis
- positional homeostasis
- neural subsystem disentanglement
- internal vs behavioral computation

## Related Skills

- neural-population-dynamics
- neural-dynamics-universal-translator
- brain-digital-twins-execution-semantics
- heteroclinic-cognitive-state-modeling
