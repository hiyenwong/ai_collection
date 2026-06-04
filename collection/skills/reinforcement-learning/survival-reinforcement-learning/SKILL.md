---
name: survival-reinforcement-learning
description: Survival Reinforcement Learning (SRL) - online classification-based self-supervised RL that maximizes agent dwell time at target goals, extending survival value learning framework. Bypasses contrastive RL constraints and mitigates "bang-bang" control issues.
---

# Survival Reinforcement Learning (SRL)

**Paper**: arXiv:2605.31273 | Submitted: 29 May 2026

**Authors**: Franki Nguimatsia-Tiofack, Fabian Schramm, Théotime Le Hellard, Justin Carpentier

## Core Concept

SRL is an **online classification-based alternative** to Contrastive Reinforcement Learning (CRL) that extends the survival value learning framework. Instead of contrastive losses, SRL maximizes the agent's **dwell time at target goals**, providing a scalable approach to self-supervised RL.

### Key Innovation

- **Classification-based formulation** - bypasses structural constraints of contrastive losses
- **Survival value learning** - maximizes time spent at goals rather than distance minimization
- **Mitigates "bang-bang" control** - addresses undesirable behaviors in complex dynamical systems
- **Depth-scalable** - supports networks over 64 layers (like CRL)
- **Long-horizon capable** - outperforms CRL on stable, long-horizon locomotion tasks

## Implementation Framework

### 1. Survival Value Objective

```
V_survival(s, g) = max E[∫_0^T 1_{at_goal} dt]
```

Maximize expected dwell time at goal state g starting from state s.

### 2. Classification Formulation

Instead of contrastive loss comparing goal vs non-goal states:

```
L_SRL = -log P(τ reaches goal | τ from policy)
```

Online classification: "Does trajectory reach/sustain goal?"

### 3. Key Differences from CRL

| Aspect | CRL | SRL |
|--------|-----|-----|
| Loss Type | Contrastive (pull goal, push non-goal) | Classification (goal reach prediction) |
| Scaling | Uniformity-tolerance dilemma | No contrastive constraints |
| Control | Can induce "bang-bang" behavior | Smooth, stable control |
| Long-horizon | Struggles | 2x-8x improvement |

### 4. Training Procedure

1. **Goal conditioning**: Sample goal states g
2. **Trajectory generation**: Roll out policy π(a|s,g)
3. **Survival prediction**: Classify trajectory success (reached/sustained goal)
4. **Update**: Maximize survival probability via gradient

## Performance Results

- **Manipulation tasks**: Matches state-of-the-art CRL
- **Locomotion tasks**: 2x to 8x improvement over CRL
- **Long-horizon planning**: Stable, sustained goal achievement
- **Depth scaling**: Works with 64+ layer networks

## Applications

### Primary Use Cases

1. **Self-supervised RL** - no reward engineering required
2. **Goal-conditioned planning** - long-horizon tasks
3. **Robotic locomotion** - stable, continuous control
4. **Robotic manipulation** - goal-reaching tasks

### When to Use SRL

- Long-horizon goal-conditioned tasks
- When contrastive RL struggles with uniformity
- Stable locomotion with sustained goals
- Self-supervised learning without explicit rewards

## Technical Details

### Mitigation of "Bang-Bang" Control

Traditional survival frameworks induce "bang-bang" solutions (extreme control switching). SRL's classification formulation smooths this:

- Soft goal prediction instead of hard distance minimization
- Continuous survival probability estimation
- Gradual policy adaptation

### Sufficient Statistics

SRL computes survival value as sufficient statistic for:
- Optimal policy learning
- Goal-conditioned decision making
- Long-horizon planning

## Activation Keywords

- survival reinforcement learning
- SRL self-supervised
- goal dwell time
- classification-based RL
- contrastive RL alternative
- long-horizon goal conditioning
- stable locomotion RL

## Related Skills

- [[model-based-diffusion-policy-optimization]] - Diffusion-based policy optimization
- [[efficient-tdmpc]] - Model-based RL
- [[sbsrl-sampling-based-safe-rl]] - Safe RL methods
- [[lilac-safe-continual-rl]] - Continual safe RL

## References

- Paper: arXiv:2605.31273 - "Survival Reinforcement Learning: Toward Scalable Self-Supervised RL"
- Contrastive RL: prior depth-scaling work
- Survival value theory: foundational RL theory

---

**Category**: reinforcement-learning, self-supervised-RL, goal-conditioned
