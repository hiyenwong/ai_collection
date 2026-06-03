---
name: stp-stabilizes-goal-conditioned-dynamics
description: "Short-Term Synaptic Plasticity (STP) stabilizes goal-conditioned dynamics in PFC-inspired reservoir computing models for multistep goal-directed action planning. Combines STP with basal-ganglia-inspired temporal-difference learning. Achieves 89.2% success under noise (vs 49.5% without STP). Activation: synaptic plasticity, reservoir computing, goal-conditioned dynamics, PFC model, action planning, goal-directed behavior, temporal-difference learning, effective connectivity, short-term plasticity, STP dynamics."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2606.03481"
  published: "2026-06-02"
  authors: "Jin Nakamura, Yuichi Katori"
  tags: [synaptic-plasticity, reservoir-computing, goal-conditioned, prefrontal-cortex, action-planning, temporal-difference-learning, effective-connectivity, computational-neuroscience]
---

# Short-Term Synaptic Plasticity Stabilizes Goal-Conditioned Dynamics

## Problem Statement

The prefrontal cortex (PFC) maintains goal information for action planning over behavioral timescales (seconds to minutes), but how recurrent circuits preserve this information in an **action-usable form** remains unclear. Traditional reservoir computing models suffer from noise sensitivity — goal information degrades under state perturbations.

## Core Contribution

**Short-Term Synaptic Plasticity (STP) stabilizes goal-conditioned dynamics through dynamic modulation of effective recurrent connectivity**, making goal information robust to noise and available for delayed action execution.

## Key Results

### Noise Robustness (Critical Finding)

| Model | Success (no noise) | Success (with noise) | Cohen's dz |
|-------|-------------------|---------------------|------------|
| **Without STP** | 75.8% | 49.5% | — |
| **With STP** | 91.8% | 89.2% | **1.31** |

- **STP provides ~40% performance gain** under noise conditions
- Paired Cohen's dz = 1.31 indicates **very large effect size**
- Goal information remains decodable even under perturbations

### Mechanism: Goal-Conditioned Dynamics

STP does NOT merely create a linearly readable goal representation (both models achieve this). Instead, STP preserves goal information as **action-relevant dynamics**:

1. **Time-resolved decoding**: STP maintains goal identity information throughout delay period
2. **State-space separability**: Goal-specific trajectories remain distinct under noise
3. **Action-value differences**: Goal-conditioned action values available at execution time

### Effective Connectivity Analysis

| Feature | Without STP | With STP |
|---------|-------------|----------|
| Temporal pattern | Time-invariant | Goal-specific patterning |
| Delay-period behavior | Static | Increases toward action opportunity |
| Interpretation | Fixed recurrent scaling | **History-dependent synaptic modulation** |

**Key insight**: STP creates goal- and task-state-conditioned effective connectivity patterns that evolve during the trial.

## Technical Framework

### Architecture

```
PFC-inspired Reservoir + Basal Ganglia TD Learning
├── Reservoir layer (recurrent network)
│   ├── Input layer (goal + task state)
│   ├── Recurrent connections with STP
│   └── Facilitation-dominant time constants
├── Basal ganglia module
│   ├── Temporal-difference learning
│   ├── Action-value computation
│   └── Goal-conditioned readout
└── Output layer (action selection)
```

### STP Implementation

- **Tsodyks-Markram model** (or similar short-term plasticity)
- **Facilitation-dominant range** of time constants (identified via grid search)
- **Online, history-dependent synaptic modulation** (not fixed scaling)

### Experimental Setup

- **100 independently generated networks** (paired comparison)
- **Multistep goal-directed action-selection task**
- **Delayed execution** (goal information must persist across delay)
- **State noise injection** (robustness test)

## Methodology Extracts

### 1. Goal Decoding Analysis

Goal identity decodability during delay period:
- Train linear decoder on reservoir states
- Measure accuracy over time
- STP models maintain >90% decoding accuracy under noise

### 2. State-Space Separability

Compute separability of goal-specific trajectories:
- Without STP: trajectories merge under noise
- With STP: trajectories remain distinct

### 3. Action-Value Difference Analysis

Quantify goal-conditioned action availability:
- Compute action-value differences for each goal
- STP preserves goal-specific action rankings at execution time

### 4. Effective Connectivity Computation

Track goal-dependent connectivity patterns:
- **Without STP**: connectivity remains static (fixed recurrent weights)
- **With STP**: connectivity evolves based on goal + trial history

### 5. Control Experiments

- **Gain-matched controls**: ruled out fixed recurrent scaling
- **STP-state perturbation**: confirmed online synaptic modulation
- **Grid search**: identified facilitation-dominant time constant range

## Connections to Existing Literature

### Reservoir Computing & Attractor Dynamics
- Reservoir networks typically use **fixed recurrent weights**
- STP introduces **dynamic, history-dependent connectivity**
- Related to **attractor stabilization** (but different mechanism)

### Basal Ganglia & Action Selection
- TD learning for action-value computation
- Goal-conditioned readout (similar to basal ganglia action selection)
- Integration with cortical dynamics

### Synaptic Plasticity Literature
- **Short-term facilitation** (seconds-scale) vs **long-term plasticity** (minutes/hours)
- **Working memory stabilization** via STP
- **Dynamic gating** through synaptic state modulation

## Practical Applications

### 1. Goal-Directed BCI Systems

Brain-Computer Interfaces requiring:
- Goal maintenance across delays
- Robust action planning under noise
- Dynamic task-state adaptation

### 2. Neuromorphic Action Planning

Hardware implementations:
- **PFC-inspired chips** with STP circuits
- **Goal-conditioned reservoir computing**
- **Noise-robust action selection**

### 3. Continual Learning Systems

Goal-conditioned dynamics for:
- **Task-state maintenance** in continual learning
- **Delayed decision-making** in RL agents
- **Robust goal representation** under perturbations

## Activation Keywords

- `synaptic plasticity`, `short-term plasticity`, `STP dynamics`
- `reservoir computing`, `goal-conditioned dynamics`
- `PFC model`, `prefrontal cortex`, `action planning`
- `goal-directed behavior`, `temporal-difference learning`
- `effective connectivity`, `goal-dependent connectivity`
- `noise robustness`, `action-usable representation`
- `delayed execution`, `multistep planning`

## Pitfalls

### 1. STP ≠ Long-Term Plasticity

- STP operates on **seconds-scale** (facilitation/depression)
- Different from **LTP/LTD** (minutes to hours)
- Cannot replace long-term learning mechanisms

### 2. Facilitation-Dominant Range

- Grid search identified specific time constant range
- **Not all STP configurations work**
- Depression-dominant STP may destabilize dynamics

### 3. Goal Decodable ≠ Action-Usable

- Goal information decodable without STP (linear decoder works)
- But **not available for action selection** under noise
- STP's contribution is **action-relevance**, not mere representation

### 4. Online vs Fixed Modulation

- Gain-matched controls show STP is NOT simple scaling
- Requires **history-dependent synaptic states**
- Cannot implement with fixed recurrent weights

## References

- Original paper: arXiv:2606.03481
- Reservoir computing literature: Maass et al., Jaeger
- STP models: Tsodyks-Markram, facilitation/depression
- Basal ganglia action selection: TD learning frameworks
- PFC goal maintenance: Working memory models

---

**Summary**: STP provides a biologically plausible mechanism for stabilizing goal-conditioned dynamics through dynamic modulation of effective recurrent connectivity. The key innovation is **history-dependent synaptic states** that evolve during goal maintenance, creating goal-specific connectivity patterns robust to noise. This bridges synaptic plasticity (seconds-scale) with goal-directed action planning (behavioral timescales).
