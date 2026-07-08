---
name: stp-stabilizes-goal-conditioned-dynamics
description: "Short-Term Synaptic Plasticity (STP) stabilizes goal-conditioned dynamics in PFC-inspired reservoir model for multistep goal-directed action planning. Preserves action-relevant goal information under noise with 89.2% success rate vs 49.5% without STP. Activation: short-term synaptic plasticity, goal-conditioned dynamics, reservoir computing, PFC model, goal-directed planning, dynamic connectivity, facilitation-dominant STP."
category: neuroscience
---

## Context

The prefrontal cortex (PFC) maintains goal information for action planning, but how recurrent circuits preserve it in an action-usable form over behavioral timescales remains unclear. This paper demonstrates that short-term synaptic plasticity (STP) can stabilize goal information as action-usable, goal-conditioned dynamics through dynamic modulation of goal-dependent effective recurrent connectivity.

**Paper**: arXiv:2606.03481 (Submitted 2 Jun 2026)
**Authors**: Jin Nakamura, Yuichi Katori
**Categories**: Neurons and Cognition (q-bio.NC), Neural and Evolutionary Computing (cs.NE)
**Journal**: Submitted to Neural Networks (68 pages, 33 figures, 3 tables)

## Core Methodology

1. **STP-Enhanced Reservoir Model**: Incorporate STP into PFC-inspired reservoir computing model with basal-ganglia-inspired temporal-difference readout learning
2. **Goal-Conditioned Dynamics**: Preserve goal information in action-relevant form during delay periods
3. **Facilitation-Dominant STP**: Use STP time constants in facilitation-dominant range identified by grid search
4. **Effective Connectivity Analysis**: Analyze goal-specific patterning of effective connectivity during delay period
5. **Dynamic Recurrent Modulation**: History-dependent synaptic modulation stabilizes goal representations under noise

## Implementation Steps

1. **Build Reservoir Model**: Create PFC-inspired reservoir computing network with recurrent connections
2. **Add STP Dynamics**: Implement short-term synaptic plasticity with facilitation and depression mechanisms
3. **Temporal-Difference Readout**: Implement basal-ganglia-inspired learning for action value estimation
4. **Goal Representation**: Encode goal identity in reservoir state during delay period
5. **Evaluate Noise Robustness**: Test with state noise comparing models with and without STP
6. **Time-Resolved Decoding**: Analyze when and how goal information remains decodable
7. **Effective Connectivity Mapping**: Measure goal-specific connectivity patterns over time

## Key Results

- **Success Under Noise**: With STP: 91.8% (no noise) → 89.2% (noise); Without STP: 75.8% → 49.5% (paired Cohen's dz=1.31)
- **Goal Decodability**: Goal identity highly decodable during delay even without STP
- **Action-Relevance**: STP preserves goal information as action-relevant goal-conditioned dynamics
- **Dynamic Connectivity**: Delay-period goal-specific patterning increases toward later trial phase with STP
- **Time-Invariant vs Dynamic**: Without STP, effective connectivity is time-invariant; with STP, it's goal-conditioned and task-state-dependent

## Facilitation-Dominant Range

- Grid search identified facilitation-dominant range of STP time constants associated with high success rates
- STP state perturbation controls support online, history-dependent synaptic modulation
- Gain-matched controls argue against simple fixed recurrent-scaling explanation

## Pitfalls

- **STP Parameter Tuning**: STP time constants require grid search for facilitation-dominant range
- **Reservoir Initialization**: 100 independently generated networks needed for statistical significance
- **Delay Duration**: STP benefits most evident during longer delay periods with noise
- **Goal-Task Interaction**: Goal-conditioned patterning depends on both goal and task state
- **Temporal-Difference Learning**: Basal-ganglia-inspired readout requires proper action-value estimation

## Verification

- Compare success rates with vs without STP under noise (target: ~90% vs ~50%)
- Perform time-resolved decoding of goal information across delay period
- Analyze state-space separability between goals
- Measure action-value-difference availability at action opportunities
- Conduct STP-state perturbation and gain-matched controls
- Analyze effective connectivity patterns over time
- Grid search for facilitation-dominant STP time constants

## Activation

- short-term synaptic plasticity
- goal-conditioned dynamics
- reservoir computing
- PFC model
- goal-directed planning
- dynamic connectivity
- facilitation-dominant STP
- effective connectivity
- delay period
- noise robustness
- action-relevant representation