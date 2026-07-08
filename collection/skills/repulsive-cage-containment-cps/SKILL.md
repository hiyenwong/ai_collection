---
name: repulsive-cage-containment-cps
description: "Distributed containment of compromised CPS agents using repulsive cages — Stackelberg game framework for UAV swarm security via collision-avoidance exploitation. Use when: designing secure multi-agent systems, UAV swarm safety, cyber-physical security, distributed containment, adversarial agent mitigation."
version: 1.0.0
created: 2026-07-08
source: arXiv:2607.01230
tags: [cyber-physical, multi-agent, security, UAV, distributed-control, Stackelberg-game]
---

# Repulsive Cage Containment for Compromised CPS Agents

## Overview

A distributed containment framework that neutralizes hijacked agents in cyber-physical multi-agent systems (e.g., UAV swarms) by exploiting their **uncompromised low-level collision-avoidance modules** as an indirect actuation channel. Instead of detecting/isolating the malicious agent, defender agents shape the repulsive field to keep it within a prescribed safe region.

**Paper**: "Distributed Containment of a Compromised Agent through Repulsive Cages"  
**Authors**: Luigi Petruzziello, Camilla Fioravanti, Gabriele Oliva  
**Submitted**: July 1, 2026 | **Category**: eess.SY

## Core Innovation

Traditional approaches focus on **detection and isolation** of compromised agents. This work exploits a structural property: autonomous platforms have independent safety layers (collision avoidance) that remain active even when high-level commands are adversarial. Defender agents use this as an **indirect actuation channel** — they position themselves to shape the repulsive field the compromised agent experiences, effectively "herding" it.

## Methodology

### 1. Problem Formulation
- **Setting**: N defender agents + 1 compromised agent in shared workspace
- **Assumption**: Compromised agent's low-level collision avoidance is intact and active
- **Goal**: Keep compromised agent within admissible region R ⊂ ℝ² (and optionally steer to destination)

### 2. Stackelberg Game Model
- **Leaders**: Defender agents (choose geometric configuration)
- **Follower**: Adversary (chooses target command after seeing defender positions)
- **Solution concept**: Robust one-step containment via minimax geometry

### 3. Geometric Characterization
- **Support functions**: h_R(d) = max_{x∈R} ⟨d, x⟩ characterize admissible region
- **Normal cones**: N_R(x) define feasible repulsive directions at boundary
- **Repulsive cage**: Configuration of defenders such that for ALL adversary commands, the collision-avoidance response keeps target inside R

### 4. Distributed Approximation
- Centralized Stackelberg oracle computes optimal cage (computationally expensive)
- **Distributed online approximation**: Each defender uses local communication + dynamic field estimation
- **Regret bound**: Sublinear dynamic regret O(√T) relative to centralized benchmark
- Accounts for: network-induced estimation errors, temporal variability of stage-wise optimum

## Implementation Pattern

```python
# Pseudocode for distributed repulsive cage
class DefenderAgent:
    def __init__(self, id, position, comm_radius):
        self.id = id
        self.pos = position
        self.neighbors = []  # within comm_radius
        
    def estimate_repulsive_field(self, target_pos, target_vel):
        """Local estimation of total repulsive field at target"""
        field = np.zeros(2)
        for neighbor in self.neighbors:
            r_vec = target_pos - neighbor.pos
            dist = np.linalg.norm(r_vec)
            if dist < avoidance_radius:
                field += repulsive_gain * r_vec / dist**3
        return field
    
    def compute_cage_action(self, target_pos, admissible_region):
        """Compute position update to maintain containment"""
        # Support function evaluation for boundary constraints
        h_support = compute_support(admissible_region, direction)
        # Normal cone check for feasibility
        feasible = check_normal_cone(target_pos, admissible_region)
        # Stackelberg response: minimize worst-case escape
        return minimax_position_update(feasible, h_support)
```

## Key Results

1. **Exact geometric characterization** of robust one-step containment using support functions
2. **Repulsive cage concept**: defender configuration guaranteeing containment against all adversary actions
3. **Sublinear dynamic regret** for distributed approximation vs. centralized oracle
4. **Practical applicability**: Works with standard collision-avoidance modules (no agent modification needed)

## Applications

- **UAV swarm security**: Contain hijacked drones without shooting them down
- **Robotics**: Safe handling of compromised robots in shared workspaces
- **Autonomous vehicles**: Contain vehicles with compromised navigation systems
- **Industrial CPS**: Contain malfunctioning agents in factory automation

## Pitfalls & Considerations

1. **Assumption dependency**: Requires collision avoidance to be independent and unmodifiable by adversary
2. **Communication overhead**: Distributed version needs neighbor information exchange at each step
3. **Conservative bounds**: Geometric characterization may be conservative for non-convex regions
4. **Dynamic regret vs. static**: Bounds are against dynamic oracle (changing optimum), not static

## Activation Keywords

`repulsive cage`, `compromised agent containment`, `UAV swarm security`, `Stackelberg containment`, `collision avoidance exploitation`, `distributed CPS security`, `adversarial agent mitigation`, `multi-agent safety`

## References

- Petruzziello, L., Fioravanti, C., & Oliva, G. (2026). Distributed Containment of a Compromised Agent through Repulsive Cages. arXiv:2607.01230.
