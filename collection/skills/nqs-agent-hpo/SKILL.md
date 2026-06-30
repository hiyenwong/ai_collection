---
name: nqs-agent-hpo
description: "Health-aware agentic hyperparameter optimization for Neural-Network Quantum States (NQS). Open-source framework that monitors energy trajectories, detects destructive optimization events, stops unstable calculations, modifies learning-rate schedules, and resumes from safe checkpoints. Use when: optimizing NQS calculations, quantum many-body simulations, variational quantum state optimization, agentic HPO for quantum systems. Activation: nqs agent, neural network quantum states, health-aware hpo, hyperparameter optimization quantum, quantum state optimization, NQS-Agent, agentic quantum optimization."
---

## Overview

NQS-Agent (arXiv:2606.30464) is an open-source software framework for health-aware hyperparameter optimization (HPO) in Neural-Network Quantum States (NQS) calculations. NQS provide expressive variational representations for strongly correlated quantum many-body systems, but their practical accuracy depends sensitively on architecture-level hyperparameters and optimization schedules.

## Key Innovation

Instead of selecting only the lowest-energy calculation, NQS-Agent considers the **stability and recovery history** of optimization trajectories. It provides a reproducible tuning protocol that goes beyond simple energy minimization.

## Core Workflow

1. **Monitor energy trajectories** in real-time during NQS optimization
2. **Detect destructive optimization events** (energy divergence, oscillation)
3. **Stop unstable calculations early** to save compute
4. **Modify learning-rate schedule** dynamically when instability detected
5. **Resume optimization from safe checkpoints** automatically
6. **Rank candidates** with anomaly-aware scoring (not just lowest energy)

## Implementation Details

- Demonstrated on residual convolutional NQS for square-lattice Heisenberg J1-J2 model
- Parameter counts comparable to aCNN (reference architecture)
- Identifies structurally distinct wide-and-shallow competitive candidates
- Improves over human-tuned baselines

## Practical Steps

1. Define NQS architecture search space (CNN layers, widths, depths)
2. Set up energy trajectory monitoring hooks
3. Configure anomaly detection thresholds for energy divergence
4. Define checkpoint intervals for safe recovery points
5. Implement learning-rate modification rules:
   - Reduce LR by factor when energy diverges
   - Increase LR when convergence stable
6. Use anomaly-aware scoring function:
   - Score = f(energy, stability, recovery_count, convergence_rate)
7. Select candidates balancing energy quality and optimization stability

## Pitfalls

- Don't trust single lowest-energy result without checking optimization history
- Anomaly detection thresholds need calibration per problem type
- Wide-and-shallow architectures may compete with deep architectures at same parameter count
- Checkpoint frequency trades off memory vs recovery granularity

## Verification

- Compare against human-tuned baselines at matched parameter counts
- Verify anomaly detection catches known failure modes
- Check that anomaly-aware scoring selects robust candidates
- Reproduce results across multiple random seeds