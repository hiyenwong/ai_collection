---
name: reward-uncertainty-diverse-behaviour
description: "Reformulate RL objective using reward function distribution instead of scalar reward. Apply non-linear objective over action sets to induce calibrated behavioural diversity without sacrificing expected reward."
---

# Reward Uncertainty for Diversity in RL

## Core Concept
Diversity = rational response to **reward uncertainty**. When reward function is not perfectly known (ambiguous preferences, imperfect reward models), committing to single action is sub-optimal.

## Key Innovation
Replace scalar reward with **distribution over reward functions**. Apply **non-linear objective over action sets**.

## Result
- Calibrated behavioural diversity emerges **naturally**
- Controllable through reward distribution
- **No sacrifice** of expected reward

## Implementation
1. **Reward distribution modeling**: Capture uncertainty in reward function
2. **Non-linear objective**: Apply over sets of actions (not individual actions)
3. **Principled gradient estimator**: For contextual bandit setting
4. **Generalization**: Vanilla policy gradient + action-set approaches

## Theoretical Foundation
- Proves formulation generalizes vanilla policy gradient and action-set approaches
- Robust alternative for tasks where traditional formulation fails

## Applications
- Language model fine-tuning
- Scientific discovery
- Tasks demanding behavioural diversity

## Advantages vs Alternatives
| Method | Trade-off |
|--------|-----------|
| Entropy regularization | Fragile: sacrifices performance for stochasticity |
| Diversity bonuses | Heuristic metrics can misalign policy rankings |
| **Reward uncertainty** | **Natural diversity, no reward sacrifice** |

## Source
- arXiv: 2606.03962
- Title: Using Reward Uncertainty to Induce Diverse Behaviour in Reinforcement Learning
- Authors: Anthony GX-Chen, Ankit Anand, Doina Precup, André Barreto, Mark Rowland, et al.

## Activation Keywords
reward uncertainty, behavioural diversity, reward distribution, non-linear objective, action sets, contextual bandit, diversity without sacrifice