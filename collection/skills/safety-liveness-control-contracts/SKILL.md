---
name: safety-liveness-control-contracts
description: >
  Design layered control architectures (LCAs) using safety-liveness decomposition
  via heterogeneous assume-guarantee contracts. Use when: (1) designing hierarchical
  control systems with discrete planning + continuous execution, (2) enforcing safety
  constraints while achieving long-horizon objectives, (3) co-designing multi-layer
  controllers with formal guarantees, (4) building reference governor bridges between
  MPC planners and low-level controllers. Based on arXiv:2605.04222.
---

# Safety-Liveness Control Contracts

Design hierarchical layered control architectures using the safety-liveness
decomposition framework from arXiv:2605.04222.

## Core Architecture

```
┌─────────────────────────────────────────┐
│  Discrete-Time Planner (Liveness)       │
│  - MPC planner                          │
│  - Long-horizon objectives              │
│  - Vertical refinement contracts         │
├─────────────────────────────────────────┤
│  Reference Governor Bridge              │
│  - Timing compatibility                 │
│  - Inter-layer coordination             │
├─────────────────────────────────────────┤
│  Continuous-Time Executor (Safety)      │
│  - ISS low-level controller             │
│  - Invariance enforcement               │
│  - Safety constraints                   │
└─────────────────────────────────────────┘
```

## Safety-Liveness Decomposition

- **Safety**: enforced by invariance at continuous-time layer
  - System states remain within safe sets
  - Input-to-state stability (ISS) guarantees
  - Continuous-time constraint satisfaction

- **Liveness**: achieved through refinement at discrete-time layer
  - Progress toward goals
  - Finite-time convergence properties
  - Discrete planning with feasibility guarantees

## Assume-Guarantee Contracts

Each layer specifies:
1. **Assumptions**: What it expects from other layers/environment
2. **Guarantees**: What it promises to deliver
3. **Refinement conditions**: How outputs map to inputs of adjacent layers

### Vertical Refinement
Discrete planner outputs refined to continuous inputs via timing-compatibility:
- Sample rate alignment
- Input magnitude bounds
- Transition smoothness constraints

## Implementation Pattern

```python
class SafetyLivenessController:
    def __init__(self, mpc_planner, iss_controller, reference_governor):
        self.planner = mpc_planner        # Discrete-time (liveness)
        self.controller = iss_controller   # Continuous-time (safety)
        self.bridge = reference_governor   # Inter-layer coordination
    
    def step(self, state, goal):
        # 1. Planner computes reference trajectory
        ref_traj = self.planner.plan(state, goal)
        
        # 2. Bridge ensures timing compatibility
        safe_ref = self.bridge.filter(ref_traj, state)
        
        # 3. Controller enforces safety invariance
        control = self.controller.compute(state, safe_ref)
        
        return control
```

## Key Design Principles

1. **Compositional separation**: Each layer can be designed independently
2. **Specification preservation**: Contracts guarantee properties hold when interconnected
3. **Heterogeneous time scales**: Discrete planning + continuous execution coexist
4. **No naive input filtering**: Use structured refinement, not simple clipping

## Validated Application

Hybrid Energy Storage System (HESS):
- Battery + supercapacitor coordination
- MPC handles long-term energy management (liveness)
- ISS controller ensures voltage/current limits (safety)
- Reference governor manages power split dynamics

## Pitfalls

- Do not use naive input-filtering between layers — breaks compositional guarantees
- Timing compatibility must be verified, not assumed
- Safety sets must be control-invariant, not just feasible
- Liveness requires progress metrics, not just feasibility
