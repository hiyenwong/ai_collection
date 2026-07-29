---
name: physics-aware-quadcopter-drl-control
description: Physics-aware end-to-end deep reinforcement learning methodology for quadcopter control with actuator dynamics modeling.
paper_id: "2607.25985"
---

# Physics-Aware End-to-End Deep Reinforcement Learning for Quadcopter Control

## Overview
This methodology investigates physics-aware, end-to-end deep reinforcement learning for quadcopter control that acts directly on low-level body inputs (total thrust and body torques) and integrates high-fidelity actuator dynamics.

## Key Contributions
- Integrates 12-state rigid-body model with Action2RPM allocation using Moore-Penrose pseudo-inverse
- Models first-order actuator dynamics for each motor (time constant T_m = 0.076s) including rotor gyroscopic coupling
- Implements shaped reward balancing goal-reaching and stability using exponential position well, attitude penalties, and quadratic velocity costs
- Provides reproducible benchmark comparing DDPG, TD3, PPO, and SAC algorithms for quadcopter control

## Implementation Guidelines
1. **Environment Setup**: Use high-fidelity Simulink environment with MATLAB Level-2 S-Function for 12-state rigid-body model
2. **Actuator Modeling**: 
   - Implement Action2RPM allocation based on Moore-Penrose pseudo-inverse of coefficient matrix
   - Include first-order actuator dynamics with time constant T_m = 0.076s
   - Model rotor gyroscopic coupling effects
3. **Reward Shaping**: Combine exponential position well, attitude penalties, and quadratic velocity costs
4. **Algorithm Selection**: TD3 and SAC show superior stability and exploration efficiency; PPO is less sample-efficient
5. **Training Stages**: 
   - Stage 1: Thrust-only hover control
   - Stage 2: Hover with pitch torque and translated goal

## Use Cases
- Unmanned aerial vehicle (UAV) autonomous control
- Underactuated systems with limited control inputs
- Applications requiring low-level actuator dynamics modeling
- Robotics control with physical constraints

## Activation Keywords
physics-aware DRL, quadcopter control, actuator dynamics, UAV control, end-to-end DRL, rigid-body modeling

## References
- arXiv:2607.25985 [cs.RO]
- Aeronautical and Astronautical Society of the Republic of China Conference, 2025