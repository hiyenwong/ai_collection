---
name: nqs-agent-hpo
description: "NQS-Agent: Health-Aware Hyperparameter Optimization for Neural-Network Quantum States. Monitors energy trajectories, detects destructive optimization events, manages learning-rate schedules with safe checkpoint recovery, and ranks candidates with anomaly-aware scoring. Use when: neural-network quantum states hyperparameter optimization, NQS tuning, quantum many-body variational optimization, health-aware HPO, quantum state optimization agent, energy trajectory monitoring, 神经网络量子态超参数优化, 量子多体变分优化."
metadata:
  arxiv_id: "2606.30464"
  published: "2026-06-29"
  authors: "Jia-Qi Wang, Xiao-Qi Han, Ze-Feng Gao, Rong-Qiang He, Zhong-Yi Lu"
---

# NQS-Agent Health-Aware HPO

## Description

Framework for health-aware hyperparameter optimization (HPO) in Neural-Network Quantum States (NQS) calculations. Goes beyond selecting a single lowest-energy calculation by monitoring optimization trajectory stability and recovery history.

## Activation Keywords
- nqs hyperparameter optimization
- health-aware HPO quantum
- neural-network quantum states tuning
- quantum many-body variational optimization
- NQS-Agent
- energy trajectory monitoring
- quantum state optimization
- 神经网络量子态超参数优化
- 量子多体变分优化

## Core Concepts

### The Problem
NQS variational accuracy depends sensitively on:
- Architecture-level hyperparameters (depth, width, connectivity)
- Optimization schedules (learning rate, momentum, batch size)
- Random initialization seeds

Single lowest-energy runs are unreliable — destructive optimization events (gradient explosion, oscillation divergence) can mask good architectures.

### Health-Aware HPO Methodology

**Four-Phase Pipeline:**

1. **Energy Trajectory Monitoring**: Continuously track energy curves during optimization
2. **Destructive Event Detection**: Identify gradient explosion, oscillation divergence, NaN/Inf
3. **Safe Checkpoint Recovery**: Roll back to stable checkpoints and modify learning-rate schedule
4. **Anomaly-Aware Scoring**: Rank candidates using stability + recovery history, not just final energy

### Key Insight

> The stability and recovery history of an optimization trajectory should be considered when assessing an NQS result. Health-aware HPO provides a reproducible tuning protocol that goes beyond selecting a single lowest-energy calculation.

## Usage Patterns

### Pattern 1: NQS Architecture Search
When comparing NQS architectures (e.g., residual CNN vs aCNN):
1. Run multiple hyperparameter configurations per architecture
2. Apply health monitoring during each run
3. Score candidates by: final energy + trajectory stability + recovery count
4. Select architectures that consistently converge, not just lucky low-energy runs

### Pattern 2: Learning Rate Schedule Optimization
When tuning learning rates for quantum many-body models:
1. Start with conservative schedule
2. Monitor energy derivative for instability signals
3. Automatically reduce LR when instability detected
4. Resume from checkpoint before instability
5. Record recovery history as part of candidate evaluation

### Pattern 3: Reproducible NQS Benchmarking
For reproducible quantum state calculations:
1. Fix parameter count across architecture comparison
2. Run HPO with health monitoring for each candidate
3. Report both best energy AND optimization reliability metrics
4. Document all recovery events and schedule modifications

## Methodology

### Step 1: Define Search Space
- Architecture parameters: layers, filters, activation functions
- Optimization parameters: initial LR, decay schedule, batch size
- Physics constraints: symmetry, boundary conditions

### Step 2: Run Health-Monitored Optimization
For each candidate configuration:
```
while not converged:
    energy = compute_energy(params)
    monitor(energy_trajectory)
    if detect_instability(trajectory):
        checkpoint = rollback_to_stable()
        modify_lr_schedule(checkpoint)
        resume_optimization(checkpoint, new_lr)
    if detect_divergence(trajectory):
        abort_candidate()
        record("unstable")
```

### Step 3: Anomaly-Aware Scoring
Score = α × (normalized energy) + β × (stability score) - γ × (recovery count)

Where:
- Stability score: fraction of steps without instability
- Recovery count: how many times rollback was needed
- Lower score = better candidate

### Step 4: Candidate Selection
- Reject candidates with >N recovery events
- Rank remaining by composite score
- Verify selected candidate on holdout physics benchmarks

## Pitfalls

- **Single-run selection trap**: Picking the configuration with lowest final energy ignores whether it achieved that through luck or genuine convergence. Always use multiple runs per configuration.
- **Checkpoint granularity**: Too-frequent checkpoints waste memory; too-sparse checkpoints lose too much progress on rollback. Checkpoint every 10-50 steps for NQS calculations.
- **Instability threshold tuning**: The energy derivative threshold for "instability" depends on the physics model. Calibrate on a known-good configuration first.
- **Parameter count matching**: When comparing architectures, ensure fair comparison by matching parameter counts (e.g., wide-and-shallow vs deep-and-narrow).

## Resources
- arXiv: 2606.30464 — "NQS-Agent: Health-Aware Agentic Hyperparameter Optimization for Neural-Network Quantum States" (Wang et al., 2026)
