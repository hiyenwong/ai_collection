---
name: plasticity-enhanced-mamoe
description: Plasticity-Enhanced Multi-Agent Mixture of Experts (PE-MAMoE) for dynamic objective adaptation in non-stationary environments. Combines sparsely gated MoE with phase-controlled plasticity injection for resilient multi-agent reinforcement learning. Use for UAV coordination, disaster response networks, and multi-agent systems under distribution shifts.
---

# Plasticity-Enhanced Multi-Agent Mixture of Experts

This skill implements PE-MAMoE, a framework that maintains learning plasticity in multi-agent systems facing abrupt environmental changes and non-stationarity.

## Overview

Deep reinforcement learning policies suffer from plasticity loss under distribution shifts, as representation collapse and neuron dormancy impair adaptation. PE-MAMoE addresses this through a mixture-of-experts architecture with controlled plasticity injection.

**Key Features:**
- Sparsely gated mixture of experts (MoE) actor
- Non-parametric Phase Controller for plasticity injection
- Centralized training with decentralized execution (CTDE)
- Dynamic regret bounds for tracking error

## When to Use This Skill

- Multi-agent systems in non-stationary environments
- UAV-assisted emergency networks
- Disaster response coordination
- Systems facing abrupt objective changes

## Problem Context

### Non-Stationarity Sources

- Abrupt user mobility changes
- Shifting traffic demands
- Quality of service trade-off variations

### Plasticity Loss Mechanisms

- **Representation Collapse**: Feature space degradation
- **Neuron Dormancy**: Inactive network components
- **Policy Entropy Collapse**: Loss of exploration

## Architecture

### PE-MAMoE Components

```
┌─────────────────────────────────────────┐
│     Centralized Training (CT)           │
│  - Multi-Agent Proximal Policy Opt.     │
└──────────────────┬──────────────────────┘
                   │
     ┌─────────────┼─────────────┐
     ↓             ↓             ↓
┌─────────┐  ┌─────────┐  ┌─────────┐
│  UAV 1  │  │  UAV 2  │  │  UAV N  │
│  MoE    │  │  MoE    │  │  MoE    │
│  Actor  │  │  Actor  │  │  Actor  │
└────┬────┘  └────┬────┘  └────┬────┘
     │            │            │
     └────────────┴────────────┘
                  │
         ┌────────┴────────┐
         ↓                 ↓
    Sparsely Gated    Phase Controller
    Router Selection  (Plasticity Injection)
```

### Phase Controller

- **Trigger**: Phase switches (environment changes)
- **Action**: Expert-only stochastic perturbations
- **Effects**: 
  - Reset action log-standard-deviation
  - Anneal entropy and learning rate
  - Schedule router temperature
- **Goal**: Re-plasticize policy without destabilizing safe behaviors

## Theoretical Results

### Dynamic Regret Bound

Tracking error scales with:
1. **Environment Variation**: Rate of non-stationarity
2. **Cumulative Noise Energy**: Stochastic perturbation magnitude

```
Regret ≤ f(Environment Variation) + g(Noise Energy)
```

## Implementation Guide

### Training Algorithm

1. **Initialize** MoE actors for each agent
2. **Observe** global state and local observations
3. **Select** expert via sparse gating
4. **Compute** actions and value estimates
5. **Inject** plasticity on phase switches
6. **Update** via MAPPO with annealed parameters

### Key Hyperparameters

| Parameter | Description | Typical Value |
|-----------|-------------|---------------|
| N_experts | Number of experts | 4-8 |
| Top_k | Experts per forward pass | 1-2 |
| Perturbation_duration | Plasticity injection length | 10-50 steps |
| Entropy_anneal_rate | Exploration decay | 0.995 |

## Performance Results

Simulations with mobile users and 3GPP-style channels show:

| Metric | Improvement |
|--------|-------------|
| Normalized Interquartile Mean Return | +26.3% vs baseline |
| Served-User Capacity | +12.8% |
| Collisions | -75% |

### Diagnostics

- Persistently higher expert feature rank
- Periodic dormant-neuron recovery at regime switches

## References

**Paper**: Plasticity-Enhanced Multi-Agent Mixture of Experts for Dynamic Objective Adaptation in UAVs-Assisted Emergency Communication Networks
- **Authors**: Wen Qiu, Zhiqiang He, Wei Zhao, Hiroshi Masui
- **arXiv**: 2604.09028
- **Date**: 2026-04-10
- **Categories**: cs.MA, cs.LG, cs.NI

## Related Skills

- `multi-agent-llm-peer-preservation`: Peer-preservation in multi-agent LLM systems
- `decentralized-optimization-smtpp`: Decentralized stochastic optimization
- `multi-agent-clinical-reasoning`: Multi-agent framework for clinical reasoning
