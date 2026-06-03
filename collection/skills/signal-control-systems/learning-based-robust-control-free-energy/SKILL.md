---
name: learning-based-robust-control-free-energy
description: Distributionally robust free energy principle for reliable robotic control. Jointly learns environment dynamics and rewards while ensuring robustness to epistemic uncertainties. Validated on Franka Research 3 arm manipulation tasks.
version: 1.0.0
metadata:
  hermes:
    tags: [free-energy-principle, robust-control, robotics, distributional-robustness, epistemic-uncertainty, sim-to-real]
    source_paper: "Learning-Based Robust Control: Unifying Exploration and Distributional Robustness for Reliable Robotics via Free Energy (arXiv:2603.06831)"
    citations: 0
---

# Learning-Based Robust Control via Free Energy Principle

## Overview

Paper: arXiv:2603.06831 (2026-03-05)
Authors: Jesawada, Hozefa; Russo, Giovanni; Swikir, Abdalla; Abu-Dakka, Fares

This work proposes a **distributionally robust free energy principle** for reliable robotic control. The model jointly learns environment dynamics and rewards while ensuring robustness to epistemic uncertainties. It modifies the maximum diffusion learning framework and validates on continuous-control benchmarks, including real-world Franka Research 3 arm manipulation.

## Key Contributions

1. **Distributionally Robust Free Energy Principle** — Extension of the free energy principle that explicitly accounts for distributional uncertainty
2. **Joint Dynamics + Reward Learning** — Simultaneously learns environment dynamics and reward functions
3. **Epistemic Uncertainty Robustness** — Policies are robust to uncertainties in both environment and reward models
4. **Sim-to-Real Transfer** — Narrows the sim-to-real gap with zero-shot deployment
5. **Real-World Validation** — Demonstrated on Franka Research 3 arm for tabletop manipulation

## Free Energy Principle in Control

### Background

The free energy principle (FEP) from computational neuroscience posits that biological systems minimize a variational free energy bound on surprise. In control:
- **Perception**: Inferring hidden states from observations
- **Action**: Selecting actions that minimize expected free energy
- **Exploration vs. Exploitation**: Naturally balances information gathering and goal achievement

### Distributionally Robust Extension

The proposed modification introduces distributional robustness:
- **Epistemic Uncertainty**: Uncertainty about the true model parameters
- **Distributional Robustness**: Policies perform well across a family of plausible distributions
- **Ambiguity Set**: Defines the set of distributions the policy must be robust against

## Maximum Diffusion Learning Modification

### Key Modification

The framework modifies maximum diffusion learning by:
1. **Explicit Robustness Characterization**: Proves policy robustness to epistemic uncertainties in dynamics and reward
2. **Joint Learning**: Learns dynamics model and reward function together
3. **Distributional Robustness**: Incorporates worst-case analysis over ambiguity sets

### Policy Computation

```
Observations → Joint Model Learning (dynamics + reward) → Free Energy Minimization → Robust Policy → Action
```

## Theoretical Guarantees

- **Robustness to Epistemic Uncertainty**: Explicit characterization of policy robustness bounds
- **Distributional Robustness**: Performance guarantees across distributional shifts
- **Convergence**: Theoretical convergence properties under the modified framework

## Experimental Validation

### Simulation Benchmarks
- Continuous control tasks (MuJoCo, etc.)
- Comparison with baselines (PPO, SAC, model-based methods)

### Real-World Experiments
- **Platform**: Franka Research 3 robotic arm
- **Task**: Tabletop manipulation
- **Results**: Repeatable manipulation without task-specific fine-tuning
- **Sim-to-Real**: Zero-shot deployment with narrowed sim-to-real gap

## Applications

- **Robotic Manipulation**: Reliable control with learned models
- **Sim-to-Real Transfer**: Bridging simulation-to-reality gap
- **Adaptive Control**: Systems that learn and maintain robustness
- **Autonomous Systems**: Reliable deployment in uncertain environments

## When to Use This Skill

- Developing robust learning-based controllers for robotics
- Addressing sim-to-real transfer challenges
- Working with systems where model uncertainty is significant
- Applying free energy principle to control problems

## Related Work

- **Free Energy Principle**: Karl Friston's active inference framework
- **Distributionally Robust Optimization**: Worst-case optimization over ambiguity sets
- **Model-Based RL**: Learning dynamics models for planning
- **Maximum Diffusion Learning**: Diffusion-based policy optimization

## References

- **Paper**: Jesawada, H., Russo, G., Swikir, A., Abu-Dakka, F. "Learning-Based Robust Control: Unifying Exploration and Distributional Robustness for Reliable Robotics via Free Energy," arXiv:2603.06831, Mar. 2026
- **Related**: Free energy principle, active inference, distributionally robust optimization, robotic control