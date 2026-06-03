---
skill_name: stp-stabilizes-goal-conditioned-dynamics
description: Short-Term Synaptic Plasticity (STP) stabilizes goal-conditioned dynamics methodology for multistep goal-directed action planning using PFC-inspired reservoir models.
arxiv_id: 2606.03481
authors: Jin Nakamura, Yuichi Katori
date: 2026-06-02
category: neuroscience
tags: [short-term-synaptic-plasticity, reservoir-computing, goal-conditioned-dynamics, PFC, action-planning, computational-neuroscience]
activation_keywords: [STP, synaptic plasticity, goal-conditioned, reservoir model, PFC, action planning, goal-directed]
---

# Short-Term Synaptic Plasticity Stabilizes Goal-Conditioned Dynamics

## Background

The prefrontal cortex (PFC) maintains goal information for action planning, but how recurrent circuits preserve it in an action-usable form over behavioral timescales remains unclear. This research investigates whether short-term synaptic plasticity (STP) can stabilize goal information as action-usable, goal-conditioned dynamics.

## Core Methodology

### Model Architecture

1. **PFC-Inspired Reservoir Computing Model**
   - Incorporates STP into recurrent neural network
   - Basal-ganglia-inspired temporal-difference (TD) readout learning
   - Evaluates paired models with and without STP across 100 independently generated networks

2. **Task Design**
   - Multistep goal-directed action-selection task
   - Delayed execution paradigm
   - Tests goal representation stability under state noise

### Key Findings

**Robustness Under Noise:**
- Without STP: success falls from 75.8% to 49.5% under state noise
- With STP: success remains stable (91.8% → 89.2%, paired Cohen's dz=1.31)
- STP provides robust goal-conditioned dynamics preservation

**Mechanistic Insights:**
- STP preserves goal information as action-relevant goal-conditioned dynamics
- Effective connectivity analysis shows delay-period goal-specific patterning
- STP creates time-varying effective connectivity; without STP is time-invariant
- Facilitation-dominant STP time constants associated with high success rates

### Analysis Methods

1. **Time-Resolved Decoding**: Tracks goal representation stability over delay period
2. **State-Space Separability**: Measures distinguishability of goal-conditioned dynamics
3. **Action-Value-Difference Analysis**: Quantifies action-relevance of goal representations
4. **Effective Connectivity Analysis**: Reveals goal-specific connectivity patterning

## Technical Implementation

### STP Parameters

```python
# Tsodyks-Markram model parameters for STP
class STPSynapse:
    def __init__(self):
        # Depression parameters
        self.U = 0.5  # Utilization factor
        self.D = 0.1s  # Depression time constant
        
        # Facilitation parameters
        self.F = 1.0s  # Facilitation time constant
        
    def update(self, spike, dt):
        # Update STP state variables
        self.R = self.R - self.U * self.R * spike + (1 - self.R) * dt / self.D
        self.u = self.u + self.U * (1 - self.u) * spike - self.u * dt / self.F
```

### Reservoir Network Setup

```python
class PFCReservoir:
    def __init__(self, n_neurons, STP_enabled=True):
        self.n = n_neurons
        self.W = generate_random_weights(n_neurons)  # Recurrent weights
        self.STP = STPSynapse() if STP_enabled else None
        
    def forward(self, input, goal):
        # Goal-conditioned dynamics
        for t in range(delay_period):
            if self.STP:
                # Apply STP-modulated effective connectivity
                W_eff = self.W * self.STP.get_factor()
            else:
                W_eff = self.W
            
            state = W_eff @ state + input
```

## Practical Applications

### Use Cases

1. **Goal Maintenance in Neural Networks**
   - Implement robust goal representations in recurrent networks
   - Useful for tasks requiring delayed action execution

2. **PFC Computational Models**
   - Build biologically-inspired PFC models
   - Incorporate STP for improved robustness

3. **Reservoir Computing Enhancement**
   - Add STP to reservoir models for stability
   - Applicable to goal-directed reinforcement learning

### When to Apply

- **Goal-directed planning tasks** with temporal delays
- **Robustness requirements** under noisy conditions
- **PFC-inspired models** for cognitive tasks
- **Action selection** requiring goal memory

## Key Insights

### Theoretical Contributions

1. **STP as Dynamic Connectivity Modulator**: STP creates time-varying effective connectivity patterns that adapt based on neural history

2. **Goal-Conditioned Dynamics**: Goal information is preserved not just as static memory, but as action-relevant dynamical patterns

3. **Robustness Mechanism**: STP provides online, history-dependent synaptic modulation that stabilizes representations

### Experimental Validation

- 100 independent network trials showing consistent STP benefit
- Gain-matched controls ruling out simple scaling explanations
- STP-state perturbation confirming synaptic modulation role

## Limitations & Considerations

- Model uses simplified STP dynamics (Tsodyks-Markram)
- Task-specific results may not generalize to all goal maintenance scenarios
- Facilitation-dominant regime identified; other regimes need exploration

## References

- Nakamura, J. & Katori, Y. (2026). Short-Term Synaptic Plasticity Stabilizes Goal-Conditioned Dynamics. arXiv:2606.03481
- Tsodyks, M. & Markram, H. (1997). The neural code between neocortical pyramidal neurons.
- Katori, Y. et al. (2021). Reservoir computing models for action planning.

## Related Skills

- [[reservoir-computing]] - Reservoir computing framework
- [[short-term-synaptic-plasticity]] - STP mechanisms
- [[goal-conditioned-rl]] - Goal-conditioned reinforcement learning
- [[pfc-models]] - Prefrontal cortex computational models