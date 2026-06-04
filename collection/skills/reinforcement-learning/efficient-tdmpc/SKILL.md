---
name: efficient-tdmpc
description: EfficientTDMPC improves model-based RL for continuous control with ensemble dynamics, uncertainty-penalized planning, and data freshness optimizations. Achieves SOTA sample efficiency on HumanoidBench-Hard and DMC hard, with benefits from higher update-to-data ratios.
---

# EfficientTDMPC: Improved MPC Objectives for Sample-Efficient Continuous Control

## Core Methodology

EfficientTDMPC builds on the TD-MPC family of model-based RL algorithms, addressing two key sources of error in return estimation:

### Key Contributions

#### 1. Ensemble Dynamics Modeling
- Maintains an ensemble of dynamics models (multiple learned transition functions)
- Averages return estimates across models AND different rollout depths
- Reduces variance from single-model prediction errors

#### 2. Uncertainty-Penalized Planning
- Adds option to apply uncertainty penalty to the planner objective
- Planner actively avoids actions with uncertain return estimates
- Risk-aware exploration during planning phase

#### 3. Practical Improvements
- Increased buffer data freshness (prioritizes recent experience)
- Reduced compute requirements
- Enables benefits from higher update-to-data (UTD) ratio
  - More frequent policy updates per data point
  - Further improves sample efficiency

## Implementation Notes

1. **Ensemble size**: Typically 3-5 dynamics models for good uncertainty estimates
2. **Rollout depth averaging**: Average value estimates across different planning horizons
3. **Uncertainty penalty**: Penalize actions where ensemble predictions diverge significantly
4. **UTD ratio**: Higher ratios (more updates per data point) are more effective with these improvements

## Performance
- State-of-the-art sample efficiency on HumanoidBench-Hard (low data regime)
- State-of-the-art sample efficiency on DMC hard (low data regime)
- Matches SOTA on DMC easy
- Particularly strong in low-data scenarios

## Applications
- Sample-efficient continuous control tasks
- High-dimensional robotics (humanoid, manipulation)
- Environments where data collection is expensive
- Any TD-MPC based agent can benefit from these enhancements

## Activation Keywords
efficient tdmpc, model-based RL, ensemble dynamics, uncertainty planning, sample efficiency, continuous control, update-to-data ratio, TD-MPC
