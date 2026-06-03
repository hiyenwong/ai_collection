---
name: stp-stabilizes-goal-conditioned-dynamics
description: Short-Term Synaptic Plasticity (STP) stabilizes goal-conditioned dynamics in PFC-inspired reservoir models — computational neuroscience methodology showing STP preserves goal information as action-relevant dynamics under noise.
tags:
  - short-term synaptic plasticity
  - prefrontal cortex
  - reservoir computing
  - goal-conditioned dynamics
  - action planning
  - neural dynamics
  - brain network
  - computational neuroscience
version: 1.0.0
arxiv_id: 2606.03481
arxiv_url: https://arxiv.org/abs/2606.03481
pdf_url: https://arxiv.org/pdf/2606.03481
published: 2026-06-02
authors: Jin Nakamura, Yuichi Katori
categories: q-bio.NC, cs.NE
---

# Short-Term Synaptic Plasticity Stabilizes Goal-Conditioned Dynamics

## Overview

This skill documents the computational neuroscience discovery that **Short-Term Synaptic Plasticity (STP)** in prefrontal cortex (PFC) circuits stabilizes goal information as **goal-conditioned dynamics**, enabling robust multistep goal-directed action planning under noise.

## Core Discovery

### Problem: Goal Information Preservation

The prefrontal cortex (PFC) maintains goal information for action planning, but fundamental question remains:

- **How do recurrent circuits preserve goal information in action-usable form over behavioral timescales?**
- Traditional reservoir models: Goal decodable during delay, but **performance collapses under noise**
- Without STP: Success drops from 75.8% to 49.5% under state noise
- Challenge: Need mechanism to stabilize goal representations across temporal delays

### Solution: Short-Term Synaptic Plasticity

Key finding: **STP stabilizes goal information as action-relevant goal-conditioned dynamics**:

- With STP: Success remains essentially unchanged (91.8% → 89.2% under noise)
- Paired Cohen's dz = 1.31 (very large effect)
- STP preserves goal information available at **later action opportunities**
- Dynamic modulation of goal-dependent effective recurrent connectivity

## Mathematical Framework

### Reservoir Computing Model

```python
# PFC-inspired reservoir with basal ganglia TD readout
class PFCReservoirModel:
    """
    Reservoir computing model with STP for goal-conditioned dynamics.
    
    Components:
    - PFC reservoir (recurrent network with STP)
    - Basal ganglia-inspired TD learning readout
    - Multistep goal-directed action selection task
    """
    
    def __init__(self, n_neurons, stp_type='facilitation'):
        self.reservoir = ReservoirNetwork(n_neurons)
        self.stp = ShortTermPlasticity(stp_type)
        self.readout = TDReadout()  # Temporal difference learning
        
    def forward(self, goal_input, state_noise=0.0):
        """
        Process goal information through reservoir with STP.
        
        Returns action values conditioned on goal.
        """
        # Goal encoding with STP-modulated recurrent dynamics
        reservoir_state = self.reservoir(goal_input)
        
        # STP modulation of effective connectivity
        modulated_state = self.stp(reservoir_state)
        
        # Action value readout (goal-conditioned)
        action_values = self.readout(modulated_state)
        
        return action_values
```

### Short-Term Plasticity Dynamics

```python
class ShortTermPlasticity:
    """
    STP model: Facilitation-dominant dynamics.
    
    Dynamics:
    - Facilitation: Increases synaptic efficacy with activity
    - Depression: Decreases synaptic efficacy with activity
    - Recovery: Synaptic resources restore over time
    """
    
    def __init__(self, tau_f=0.5, tau_d=0.3, U=0.2):
        self.tau_f = tau_f  # Facilitation time constant
        self.tau_d = tau_d  # Depression time constant
        self.U = U          # Utilization parameter
        
    def forward(self, spike_train):
        """
        Compute STP-modulated synaptic weights.
        
        Effective weight: w_eff = w * F * D
        
        F (facilitation): Increases with spikes
        D (depression): Decreases with spikes
        """
        F = 1.0  # Facilitation factor
        D = 1.0  # Depression factor
        
        for t, spike in enumerate(spike_train):
            if spike:
                # Facilitation dynamics
                F += self.U * (1 - F) * spike
                F = F * np.exp(-dt/self.tau_f) + (1 - np.exp(-dt/self.tau_f))
                
                # Depression dynamics
                D -= self.U * F * D * spike
                D = D * np.exp(-dt/self.tau_d) + (1 - np.exp(-dt/self.tau_d))
        
        return F * D  # STP modulation factor
```

### Goal-Conditioned Dynamics

```python
def goal_conditioned_dynamics(reservoir_state, goal_id):
    """
    Goal-conditioned dynamics: Neural dynamics depend on goal identity.
    
    Key property: Goal information is preserved in action-relevant form.
    
    Mechanism: STP creates goal-specific effective connectivity patterns.
    """
    # Effective connectivity depends on goal through STP history
    # Different goals → different STP states → different effective weights
    
    goal_specific_weights = compute_effective_connectivity(
        reservoir_state,
        goal_id,
        stp_state
    )
    
    # Goal-conditioned dynamics: Trajectories depend on goal
    dynamics = reservoir_state @ goal_specific_weights
    
    return dynamics
```

## Experimental Validation

### Task: Multistep Goal-Directed Action Planning

**Task Design**:
- Goal identity provided at trial start
- Delay period (behavioral timescale)
- Multiple action opportunities during delay
- Goal-conditioned action selection at execution time
- State noise added to test robustness

### Results Summary

| Model | Noise-Free Success | Under Noise Success | Effect Size |
|-------|-------------------|---------------------|-------------|
| **Without STP** | 75.8% | 49.5% | Large degradation |
| **With STP** | 91.8% | 89.2% | Cohen's dz=1.31 (stable) |

**Key Metrics**:

1. **Goal Decoding**: High accuracy during delay for both models
   - STP not required for linearly readable goal representation
   - Goal identity decodable in both cases

2. **Noise Robustness**: STP preserves performance under noise
   - Without STP: 26.3% performance drop
   - With STP: Only 2.6% performance drop
   - STP provides dramatic stabilization

3. **Action-Value Availability**: Goal information available at later action times
   - Time-resolved decoding analysis
   - STP preserves goal information toward later trial phases
   - Goal information accessible when needed for action

### Analyses Performed

#### 1. Time-Resolved Decoding

```python
# Goal decoding accuracy over time
time_resolved_accuracy = []

for t in range(trial_duration):
    # Decode goal identity from reservoir state at time t
    decoded_goal = decode_goal(reservoir_state[t])
    accuracy = compute_accuracy(decoded_goal, true_goal)
    time_resolved_accuracy.append(accuracy)

# STP maintains high decoding accuracy toward later trial phases
# Without STP: Accuracy decays under noise
```

#### 2. State-Space Separability

```python
# Goal-specific state space trajectories
goal_trajectories = {}

for goal_id in goals:
    trajectory = compute_trajectory(reservoir, goal_id, stp_state)
    goal_trajectories[goal_id] = trajectory

# Separability analysis: Distance between goal trajectories
separability = compute_trajectory_separability(goal_trajectories)

# STP increases separability toward later trial phases
# Goal-conditioned dynamics become more distinct with STP
```

#### 3. Action-Value Difference Analysis

```python
# Action value differences reflect goal conditioning
action_values = model.compute_action_values(goal_id)

# Difference between best and second-best action
value_diff = max(action_values) - sorted(action_values)[-2]

# STP preserves large action-value differences under noise
# Goal information remains action-relevant
```

#### 4. Effective Connectivity Analysis

```python
# Goal-specific effective connectivity patterns
effective_connectivity = compute_effective_weights(
    reservoir,
    goal_id,
    stp_state
)

# Time evolution of effective connectivity
for t in trial:
    ec_t = effective_connectivity[t]
    pattern = extract_pattern(ec_t)
    
# STP creates delay-period goal-specific patterning
# Pattern increases toward later trial phases
# Without STP: Time-invariant effective connectivity
```

## Key Insights

### Mechanism: Dynamic Recurrent Modulation

**STP Mechanism**:
- STP modulates effective recurrent connectivity dynamically
- **History-dependent synaptic weights**: Effective weights depend on spike history
- **Goal-specific patterns**: Different goals → different STP states → different connectivity
- **Online modulation**: STP operates continuously, not fixed scaling

### Why STP Stabilizes Goal Dynamics

1. **Goal-Conditioned Connectivity**: STP creates goal-dependent effective weights
2. **Temporal Preservation**: STP state evolves toward later trial phases
3. **Noise Filtering**: STP dynamics smooth noise perturbations
4. **Action-Relevance**: Goal information preserved in action-relevant form
5. **History Dependence**: Synaptic state encodes goal history

### Grid Search: Optimal STP Parameters

```python
# Hyperparameter grid search for STP time constants
best_params = grid_search(
    tau_f_range=[0.1, 0.5, 1.0, 2.0],
    tau_d_range=[0.05, 0.3, 0.6, 1.0],
    U_range=[0.1, 0.2, 0.3, 0.4]
)

# Result: Facilitation-dominant range associated with high success
# tau_f ~ 0.5-1.0 (facilitation time constant)
# tau_d ~ 0.3-0.6 (depression time constant)
# U ~ 0.2 (utilization)
```

**Optimal Regime**: Facilitation-dominant STP time constants yield best performance.

## Control Experiments

### Gain-Matched Control

```python
# Control 1: Fixed recurrent scaling (no STP dynamics)
gain_matched_model = ReservoirNetwork(fixed_gain=stp_effective_gain)

# Result: Fixed scaling does not reproduce STP benefits
# STP advantage is NOT due to simple recurrent scaling increase
```

### STP-State Perturbation Control

```python
# Control 2: Perturb STP state during delay
stp_state_perturbed = perturb_stp_state(stp_state, noise_level)

# Result: Perturbation degrades performance
# STP state is critical for goal preservation
# Supports online, history-dependent modulation hypothesis
```

## Practical Applications

### 1. Computational Neuroscience Models

**Use Cases**:
- Modeling PFC goal maintenance in cognitive tasks
- Simulating working memory dynamics with STP
- Designing goal-conditioned neural circuits

### 2. Neuromorphic Computing

**Hardware Implementation**:
- Implement STP dynamics in neuromorphic chips
- STP-based working memory circuits
- Goal-conditioned action selection systems

### 3. Reservoir Computing

**Architecture Enhancement**:
```python
class STPReservoir:
    """
    Reservoir computing with STP for robust goal conditioning.
    
    Advantages:
    - Noise-robust goal maintenance
    - Goal-conditioned dynamics
    - Temporal preservation of information
    """
    
    def __init__(self, reservoir_size, stp_params):
        self.reservoir = RandomReservoir(reservoir_size)
        self.stp = ShortTermPlasticity(**stp_params)
        
    def forward(self, goal_input, noise_level=0.0):
        # STP-modulated reservoir dynamics
        state = self.reservoir(goal_input)
        stp_state = self.stp(state)
        
        # Goal-conditioned output
        output = self.readout(stp_state)
        
        # Robust under noise (STP stabilizes)
        return output
```

### 4. Cognitive AI Systems

**Goal Maintenance Systems**:
- AI agents maintaining goal information over time
- Goal-conditioned decision making under uncertainty
- Robust goal-directed planning systems

## Research Extensions

### Potential Studies

1. **Different STP Models**: Tsodyks-Markram, Maass model variants
2. **Multi-Goal Tasks**: Multiple simultaneous goals
3. **Longer Delays**: Extended temporal preservation
4. **Biological Validation**: Compare with PFC recordings
5. **Hierarchical Goals**: Goal hierarchy with STP

### Open Questions

1. STP role in other cortical areas?
2. Interaction between STP and long-term plasticity?
3. Optimal STP parameters for different tasks?
4. STP-based vs. other working memory mechanisms?
5. Scaling to larger networks?

## Related Skills

- [[reservoir-computing-methods]] — Reservoir computing fundamentals
- [[working-memory-neural-mechanisms]] — Neural working memory
- [[short-term-plasticity-models]] — STP models (Tsodyks-Markram)
- [[goal-directed-behavior]] — Goal-conditioned action selection
- [[pfc-circuit-dynamics]] — Prefrontal cortex circuit models

## Activation Keywords

`short-term synaptic plasticity`, `STP`, `goal-conditioned dynamics`, `prefrontal cortex`, `reservoir computing`, `goal maintenance`, `working memory`, `action planning`, `noise robustness`, `effective connectivity`, `computational neuroscience`, `brain network`

## References

- arXiv:2606.03481 — Primary source (Nakamura & Katori, 2026)
- Reservoir computing literature
- Basal ganglia TD learning models
- Tsodyks-Markram STP model

## Version History

- v1.0.0 (2026-06-03): Initial skill creation from arXiv:2606.03481