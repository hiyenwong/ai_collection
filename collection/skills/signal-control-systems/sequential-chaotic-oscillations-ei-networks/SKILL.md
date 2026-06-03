---
name: sequential-chaotic-oscillations-ei-networks
description: "Sequential chaotic oscillations (SCOs) in excitatory-inhibitory threshold-linear networks - dynamical mechanism for sequential metastability in brain dynamics. Activation: sequential metastability, chaotic itinerancy, E-I oscillation, SCO, threshold-linear network, brain dynamics, metastable states."
---

## Sequential Chaotic Oscillations in E-I Threshold-Linear Networks

**arXiv:2606.00373** - Submitted May 29, 2026

**Authors**: Jie Zang, Carina Curto

**Core Innovation**: Proposes **Sequential Chaotic Oscillations (SCOs)** as a candidate dynamical mechanism for sequential metastability observed in healthy brain function, providing a dynamical-systems framework for the balance between integration and segregation.

## Key Concepts

### Sequential Chaotic Oscillations (SCOs)

- **Definition**: A simple form of chaotic itinerancy occurring in excitatory-inhibitory threshold-linear networks (E-I TLNs) under constant input
- **Characteristics**:
  - Sequence of metastable states with predictable transition order determined by underlying graph structure
  - Requires **unstable singleton fixed points** and **sufficiently strong inhibition**
  - Captures sequential metastability phenomenon observed in brain dynamics

### Graph Rules for E-I TLNs

- Developed new graph rules to characterize fixed point structure
- Applied to paths and cycles networks
- Identified parameter regime for SCO emergence:
  1. Unstable singleton fixed points required
  2. Strong inhibition necessary
  3. Network topology determines transition sequence

### E-I Oscillation Modes

- **Z-mode**: Captures excitatory differences between neurons
- **Mean mode**: Represents overall network activity
- Decomposition enables distinction of attractors associated with full-support fixed points
- E-I oscillations need NOT be synchronized - novel finding

## Methodology

### Threshold-Linear Network (TLN) Framework

Mathematical formulation for E-I TLN dynamics:
```
ẋ_i = -x_i + [∑_j W_ij x_j + b_i]_+  (excitatory neurons)
ẋ_i = -x_i + [-∑_j W_ij x_j + b_i]_+  (inhibitory neurons)
```

Where `[·]_+` denotes threshold-linear function (ReLU-like).

### Fixed Point Analysis

- **Singleton fixed points**: Single active neuron state
- **Full-support fixed points**: All neurons active
- Instability of singleton fixed points is **necessary condition** for SCOs

### Graph-Theoretic Characterization

- Transition sequence predictable from graph topology
- Paths → directed transition sequences
- Cycles → periodic-like behavior with chaotic modulation

## Theoretical Significance

### Sequential Metastability Mechanism

- Bridges gap between empirical brain observations and dynamical systems theory
- Provides mechanistic explanation for metastable state transitions
- Predictable transition order → structured chaos

### Integration-Segregation Balance

- Metastable states reflect balance between:
  - **Integration**: Network-wide coordination (mean mode)
  - **Segregation**: Local specialization (z-mode)
- SCOs provide formal framework for this balance

### Non-Synchronized E-I Oscillations

- Counterintuitive finding: E-I populations can oscillate independently
- Traditional assumption: E and I populations synchronized
- Novel insight: Different modes capture distinct aspects of network dynamics

## Applications

### Brain Dynamics Modeling

- Framework for understanding metastable dynamics in:
  - Resting state networks
  - Cognitive state transitions
  - Task-related activity sequences

### Neural Network Architecture

- Insights for designing E-I balanced networks with:
  - Predictable state transition dynamics
  - Controlled chaotic behavior
  - Structured metastability

### Computational Neuroscience

- Graph rules enable:
  - Predicting network dynamics from connectivity
  - Characterizing fixed point landscapes
  - Designing networks with specific oscillation patterns

## Key Findings

1. **SCO Emergence Conditions**:
   - Unstable singleton fixed points (necessary)
   - Strong inhibition (sufficient)
   - Specific network topology (predicts transitions)

2. **Graph Rules Validation**:
   - Characterization works for paths and cycles
   - Transition sequence predictable from graph
   - Fixed point structure determines dynamics

3. **Mode Decomposition**:
   - Z-mode + Mean mode = complete dynamics description
   - Enables attractor classification
   - Separates local and global activity patterns

## Connection to Existing Research

- **Metastability**: Links to empirical findings in fMRI, EEG studies
- **Chaotic Itinerancy**: Provides simplified realization of complex phenomenon
- **E-I Balance**: Extends classical E-I oscillation framework
- **Network Dynamics**: Complements attractor network theories

## Mathematical Framework

### State Space

- Metastable states as saddle points or transient attractors
- Transition dynamics governed by:
  - Inhibition strength
  - Graph topology
  - Initial conditions

### Predictability

- Transition sequence deterministic given graph
- Timing chaotic (unpredictable)
- Order predictable → "sequential" character

## Limitations & Future Directions

- Current work focuses on paths and cycles
- Extension to general graphs needed
- Biological validation pending
- Comparison with empirical brain data required

## Practical Implications

- Design principles for neuromorphic circuits with structured chaos
- Framework for analyzing metastability in neural recordings
- Graph-based network design for specific dynamic regimes

## References

- Carina Curto's work on fixed points in neural networks
- Chaotic itinerancy literature
- Brain metastability empirical studies

## Activation Keywords

sequential metastability, chaotic itinerancy, E-I oscillation, threshold-linear network, SCO, metastable states, brain dynamics, excitatory-inhibitory network, graph rules, fixed point analysis, neural oscillation modes, integration-segregation balance