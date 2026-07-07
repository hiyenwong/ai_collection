---
name: quantum-rl-scuc-qsample
description: "Hybrid quantum-classical reinforcement learning for Security-Constrained Unit Commitment (SCUC). Uses Bernoulli hybrid soft actor-critic (HSAC) with quantum-sampled feature augmentation for economic dispatch in power systems. Activation: quantum RL SCUC, unit commitment optimization, quantum-sampled features, hybrid soft actor-critic, economic dispatch quantum, power grid optimization quantum"
metadata:
  arxiv_id: "2606.26345"
  published: "2026-06-24"
  authors: "George Dimas, Amin Masoumi, Mert Korkali"
  tags: [quantum, reinforcement-learning, economics, power-systems, unit-commitment]
---

# Quantum-RL SCUC with Quantum-Sampled Features

## Description
Hybrid quantum-classical RL framework for Security-Constrained Unit Commitment (SCUC). Couples a Bernoulli hybrid soft actor-critic (HSAC) policy for binary commitment decisions with quantum-sampled auxiliary feature augmentation, then recovers dispatch/security via native SCUC MILP solver. Tested on 14-, 57-, 118-bus power systems.

## Activation Keywords
- quantum RL SCUC
- unit commitment quantum
- quantum-sampled features
- hybrid soft actor-critic
- economic dispatch quantum
- power system quantum optimization
- SCUC reinforcement learning
- 安全约束机组组合量子
- 量子采样特征

## Core Concepts

### SCUC-to-RL Interface
SCUC couples binary commitment, economic dispatch, reserves, and network security over multiperiod horizon. The RL agent proposes hourly commitments; a limited enforcement cap fixes subset of binaries; MILP recovers remaining variables.

### Three-Layer Architecture
1. **Bernoulli HSAC Policy**: Proposes hourly unit commitments via exploratory Bernoulli actor
2. **Quantum-Sampled Auxiliary Channel**: Augments state representation with quantum-sampled features
3. **Native SCUC MILP Recovery**: Solves dispatch/security after partial commitment enforcement

### Key Findings
- **14-bus**: Stable, low-cost recovery
- **57-bus**: Very low screen-rejection rate → learned feasibility generalization
- **118-bus**: Coverage bottleneck when enforcement cap spans < complete commitment period; accepted episodes show tightly clustered runtimes → policy captures repeatable recovery pattern

### Feasibility-Optimality Trade-off
The dominant limitation: amount of useful commitment information reaching recovery model under exploratory Bernoulli actor + small enforcement cap governs scalability.

## Methodology

### Step 1: Formulate SCUC as MDP
- State: system load forecasts, unit availability, network conditions + quantum-sampled features
- Action: binary commitment decisions per unit per hour (Bernoulli distribution)
- Reward: negative of total cost (fuel + startup + shutdown) if feasible, large penalty if infeasible

### Step 2: Quantum-Sampled Feature Augmentation
- Generate auxiliary features via quantum sampling process
- Concatenate with classical state features before policy network input
- Purpose: enhance policy expressiveness for capturing complex feasibility patterns

### Step 3: HSAC Policy Training
- Use hybrid soft actor-critic with Bernoulli output layer for discrete commitments
- Maximize expected reward + entropy regularization for exploration
- Train on smaller systems (14-bus) first, transfer to larger (57-, 118-bus)

### Step 4: MILP Recovery
- Fix subset of commitment decisions from RL policy (enforcement cap)
- Solve remaining SCUC variables via native MILP solver
- Screen for feasibility; reject and re-sample if infeasible

## Usage Patterns

### Pattern 1: Economic Dispatch Optimization
Use when optimizing generator commitment schedules with quantum-enhanced RL for improved feasibility generalization.

### Pattern 2: Scalable Unit Commitment
Apply to multi-period unit commitment problems where classical solvers are expensive at realistic system sizes.

### Pattern 3: Quantum Feature Augmentation
Use quantum-sampled features to augment classical RL states for any constrained combinatorial optimization problem.

## Pitfalls

### Enforcement Cap Size
- Enforcement cap must span at least one complete commitment period for scalability
- 118-bus case shows clear bottleneck when cap is too small
- Increase cap or use more informed (less exploratory) actor for larger systems

### Bernoulli Actor Exploration
- Pure Bernoulli exploration may propose infeasible commitments frequently
- Consider informed initialization or curriculum learning for large systems
- Screen-rejection rate increases with system size under small cap

### Quantum Sampling Overhead
- Quantum-sampled features add computational overhead
- Validate that augmentation improves policy quality vs. classical-only baseline
- Feature dimension should be tuned to avoid overfitting

### Transfer Learning Limits
- Policy trained on 14-bus generalizes to 57-bus but not directly to 118-bus
- Retrain or fine-tune on intermediate system sizes for best results

## References
- arXiv: 2606.26345 - "Feasibility-Aware Security-Constrained Unit Commitment via Hybrid Soft Actor-Critic with Quantum-Sampled Features"
- Related: `distributionally-robust-control` (DRDDPC for building energy management)
- Related: `vqa-dynamic-portfolio-optimization` (VQA for dynamic portfolio optimization)
