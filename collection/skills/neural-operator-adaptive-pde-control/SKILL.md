---
name: neural-operator-adaptive-pde-control
description: "Dual-learning architecture combining online adaptive control with offline neural operator approximation for backstepping control of nonlinear hyperbolic PDEs with unknown Volterra series. Use when controlling PDE systems where gain computation is prohibitively expensive for real-time, particularly for fluid dynamics, traffic flow, or heat transfer systems."
metadata:
  arxiv_id: "2607.06425"
  published: "2026-07-07"
  authors: "Miroslav Krstic"
  tags: [adaptive-control, neural-operator, backstepping, PDE-control, Volterra-series, Krstic]
---

# Neural Operator Adaptive PDE Control

## Core Concept

**Problem**: Adaptive backstepping for PDEs requires solving kernel PDEs on simplex domains in real-time — computationally prohibitive for nonlinear Volterra series with arbitrarily many kernels.

**Solution**: Two learning processes in series:
1. **Online**: Observer-based passive identifier learns Volterra kernel truncation
2. **Offline**: Neural operator approximates the infinite-dimensional backstepping kernel map

The closed-loop then uses online parameter estimates → feeds offline-trained neural operator → produces online control gains.

## Architecture

```
Plant (unknown Volterra PDE)
  ↓
Online Identifier (passive observer)
  ↓ [truncated kernel estimates]
Neural Operator (offline-trained)
  ↓ [backstepping gains]
Controller (real-time backstepping law)
```

## Stability Theorem

Single Lyapunov function absorbs three perturbations simultaneously:
1. Volterra series truncation error (vanishing)
2. Online identification error (vanishing)
3. Neural operator approximation error (vanishing)

**Result**: Closed-loop stability and asymptotic regulation on a basin that recovers the exact-kernel basin as NN accuracy → 1.

## Design Patterns

### Pattern 1: Neural Operator for Kernel PDEs
1. Identify the kernel PDE map: parameters → backstepping kernels
2. Generate training data offline by solving kernel PDEs for diverse parameter values
3. Train neural operator (DeepONet, FNO, or similar) to approximate the map
4. Deploy: online identifier → neural operator → control law

### Pattern 2: Passive Identifier Design
For Volterra series truncation:
- Construct observer with tunable gain
- Prove passivity of estimation error dynamics
- Ensure persistent excitation for parameter convergence

## Pitfalls

- **Neural operator extrapolation**: Offline training domain must cover the online parameter space — use adaptive enrichment if parameters drift
- **Volterra truncation order**: Too few kernels → modeling error; too many → identification difficulty
- **Basin of attraction**: The stability basin shrinks with NN approximation error; monitor Lyapunov derivative

## Related Skills

- `quantum-control-engineering` — quantum control robustness
- `amortized-nonlinear-mpc` — amortized control computation
- `dual-pathway-robust-learning-control` — dual-pathway learning control

## Activation Keywords

- neural operator backstepping
- adaptive PDE control
- Volterra series control
- Krstic neural operator
- online offline learning control
- 神经算子自适应PDE控制
- 反步法神经网络控制