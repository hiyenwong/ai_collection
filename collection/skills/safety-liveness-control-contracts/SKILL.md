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
+------------------------------------------+
|  Discrete-Time Planner (Liveness)        |
|  - MPC planner                           |
|  - Long-horizon objectives               |
|  - Vertical refinement contracts          |
+------------------------------------------+
|  Reference Governor Bridge               |
|  - Timing compatibility                  |
|  - Inter-layer coordination              |
+------------------------------------------+
|  Continuous-Time Executor (Safety)       |
|  - ISS low-level controller              |
|  - Invariance enforcement                |
|  - Safety constraints                    |
+------------------------------------------+
```

## Safety-Liveness Decomposition

- **Safety**: enforced by invariance at continuous-time layer
- **Liveness**: achieved through refinement at discrete-time layer

## Assume-Guarantee Contracts

Each layer specifies: (1) Assumptions, (2) Guarantees, (3) Refinement conditions

## Vertical Refinement
Discrete planner outputs refined to continuous inputs via timing-compatibility.

## Implementation Pattern

```python
class SafetyLivenessController:
    def __init__(self, mpc_planner, iss_controller, reference_governor):
        self.planner = mpc_planner
        self.controller = iss_controller
        self.bridge = reference_governor
    
    def step(self, state, goal):
        ref_traj = self.planner.plan(state, goal)
        safe_ref = self.bridge.filter(ref_traj, state)
        control = self.controller.compute(state, safe_ref)
        return control
```

## Key Design Principles

1. Compositional separation: Each layer designed independently
2. Specification preservation: Contracts guarantee properties when interconnected
3. Heterogeneous time scales: Discrete + continuous coexist
4. No naive input filtering: Use structured refinement

## Pitfalls

- Do not use naive input-filtering — breaks compositional guarantees
- Timing compatibility must be verified
- Safety sets must be control-invariant
- Liveness requires progress metrics
