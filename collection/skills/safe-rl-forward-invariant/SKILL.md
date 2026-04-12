---
name: safe-rl-forward-invariant
description: Learning over Forward-Invariant Policy Classes: Reinforcement Learning without Safety Concerns. Novel safe RL framework embedding safety directly into action representation via forward-invariance-induced action-space design. Finite admissible actions correspond to stabilizing feedback laws preserving forward invariance of safe state set. Decouples safety assurance from performance optimization. Use for: (1) Safe reinforcement learning, (2) forward-invariant set design, (3) safety-by-construction policies, (4) nonlinear system safety control.
---

# Safe RL via Forward-Invariant Policy Classes

## Overview

Traditional safe reinforcement learning uses runtime shielding or penalty-based constraints, which may fail or introduce computational overhead.

This framework **embeds safety directly into action representation** via forward-invariance-induced action-space design, ensuring RL agent only explores safe-by-construction policies.

**Key Innovation**: Finite admissible action set where each action corresponds to a stabilizing feedback law that preserves forward invariance of prescribed safe state set.

## Key Concepts

### Forward Invariance

**Definition**: A set `S` is forward invariant if:
```
x(t) ∈ S → x(t') ∈ S for all t' > t
```

**Safety Interpretation**:
- Safe state set: `S_safe = {states satisfying safety constraints}`
- Forward invariance: once safe, always safe
- Trajectories never leave `S_safe`

### Safe Action Space Design

**Traditional RL Action Space**:
```
A = {all possible actions} (unsafe)
```

**Safe-by-Construction Action Space**:
```
A_safe = {actions that preserve forward invariance}
```

**Design Process**:
1. Define safe state set `S_safe`
2. Identify stabilizing feedback laws
3. Map each law to a discrete action
4. Create finite admissible action set `A_safe`

### Policy Class Construction

**Admissible Policy Class**:
```
π ∈ Π_safe = {policies over A_safe}
```

**Properties**:
- **Finite**: Discrete action set
- **Stabilizing**: Each action is a stabilizing feedback law
- **Forward-invariant**: All policies preserve safety

**RL Optimization**:
```
π_optimal = argmax_{π ∈ Π_safe} J(π)
```

Where `J(π)` is performance objective (reward accumulation).

## Mathematical Framework

### Safe State Set

**Set Definition**:
```
S_safe = {x : h(x) ≥ 0}
```

Where `h(x)` is safety barrier function.

**Forward Invariance Condition**:
```
∇h(x) · f(x, a) ≥ 0 for all x ∈ S_safe, a ∈ A_safe
```

### Stabilizing Feedback Laws

**Feedback Law**: `a = k(x)` where `k` is stabilizing.

**Design**:
1. Compute control Lyapunov function `V(x)`
2. Find stabilizing controllers `k(x)`
3. Verify forward invariance preservation

### Action Mapping

**Discrete Actions**:
```
A_safe = {a_1, ..., a_N}
a_i ↔ k_i(x) (stabilizing feedback law)
```

**Implementation**:
- Each action is a pre-computed controller
- RL agent selects which controller to apply
- All controllers guarantee forward invariance

### Markov Decision Process Formulation

**State**: `x ∈ S_safe`

**Action**: `a ∈ A_safe` (discrete, safe)

**Transition**:
```
x' = f(x, a) with a = k(x)
```

**Reward**: `r(x, a)` (performance objective)

**Policy**: `π(x) → a ∈ A_safe`

## Applications

### 1. Quadcopter Hover Control

**Scenario**: Hover-regulation under disturbance
- State: position, velocity, orientation
- Safe set: bounded region around hover point
- Disturbance: wind gusts

**Implementation**:
- Define safe hover region
- Compute stabilizing controllers
- RL optimizes controller switching
- All trajectories remain in safe region

### 2. Autonomous Vehicle Control

**Scenario**: Safe navigation
- State: position, velocity, heading
- Safe set: lane boundaries, collision avoidance
- Controllers: steering, braking feedback laws

**Implementation**:
- Forward-invariant lane region
- Safe braking/steering actions
- RL optimizes path following

### 3. Industrial Process Control

**Scenario**: Chemical process regulation
- State: temperature, pressure, concentration
- Safe set: operating limits
- Controllers: stabilizing feedback laws

**Implementation**:
- Forward-invariant operating region
- Safe process control actions
- RL optimizes efficiency

## Implementation Guidelines

### Safe Set Definition

1. Identify safety constraints
2. Define barrier function `h(x)`
3. Verify set compactness and connectivity

### Controller Design

1. Compute control Lyapunov functions
2. Design stabilizing feedback laws
3. Verify forward invariance preservation
4. Map to discrete actions

### RL Training

1. Initialize policy over `A_safe`
2. Train with standard RL algorithm (e.g., Q-learning)
3. Policy restricted to safe actions
4. No safety violations during training

### Performance Optimization

1. Define reward function
2. Optimize policy within safe class
3. Balance performance vs. safety
4. Validate closed-loop behavior

## Advantages

1. **Safety Guaranteed**: All policies are safe-by-construction
2. **No Runtime Shielding**: Safety embedded in action space
3. **Decoupled Design**: Safety and performance separated
4. **Efficient Training**: Finite action space simplifies RL
5. **Provably Safe**: Forward invariance guarantees

## Theoretical Contributions

- Constructs forward-invariant safe action space
- Maps stabilizing laws to discrete actions
- Decouples safety assurance from performance optimization
- Provides safe RL framework for nonlinear systems

## Experimental Results

**Testbed**: Quadcopter hover-regulation
- Nonlinear dynamics
- Disturbance scenarios
- Performance metrics

**Findings**:
- Learned policy improves performance
- All trajectories remain safe
- No safety violations during training
- Efficient switching behavior

## References

- Paper: "Learning over Forward-Invariant Policy Classes: Reinforcement Learning without Safety Concerns" (arxiv:2604.07875)
- Authors: Chieh Tsai, Muhammad Junayed Hasan Zahed, Salim Hariri, Hossein Rastgoftar
- PDF: ~/.openclaw/workspace/papers/safe-rl-forward-invariant.pdf

## Related Skills

- `resilience-dynamics-cpsos`: Safety and resilience connection
- `cognitive-flexibility-bayesian-estimation`: Adaptive safe policies
- `karma-mechanisms-mapf`: Safe multi-agent coordination

## Description

This skill provides specialized capabilities for its domain.

## Activation Keywords

- keyword1
- keyword2
- keyword3

## Tools Used

- read: Read files
- write: Write files
- exec: Execute commands

## Instructions for Agents

When this skill is activated:

1. Identify the user's specific need
2. Apply the specialized knowledge
3. Provide clear guidance

## Examples

```
User: How do I use this skill?
Agent: I'll help you with this skill...
```