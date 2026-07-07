---
name: resilient-output-containment-cps
description: "Resilient output containment control for heterogeneous multi-agent systems under actuator cyber-attacks. Two-layer adaptive control architecture combining virtual-actuator reconfiguration with network-level adaptive protocols. Handles undisclosed leader dynamics, directed network topologies, and multiple attack types (state-correlated, input-correlated, exogenous). Use when designing fault-tolerant multi-agent coordination, resilient CPS control systems, or distributed containment tracking under adversarial conditions."
metadata:
  arxiv_id: "2606.27257"
  published: "2026-06-25"
  authors: "Mohammadreza Nematollahi, Khashayar Khorasani, Nader Meskin"
  title: "Resilient Output Containment under Undisclosed Leader Dynamics and Actuator Attacks"
  tags: [cyber-physical systems, multi-agent systems, resilient control, containment tracking, actuator attacks, adaptive control, virtual actuator, directed graphs]
---

# Resilient Output Containment for Multi-Agent Systems Under Cyber-Attacks

## Core Methodology

### Two-Layer Control Architecture

The methodology separates **network-level coordination** from **local execution resilience**:

**Layer 1: Network Interface (Task-Space Commands)**
- Generates containment commands using only neighbor-exchanged network-interface states
- State dimensions match plant output dimensions (not full system state)
- No global graph knowledge required for parameter tuning
- No a priori knowledge of leader velocity bounds or motion envelopes
- Continuous adaptive protocol (eliminates chattering from sliding mode approaches)

**Layer 2: Virtual-Actuator Reconfiguration (Local Execution)**
- Compensates for actuator attacks in local tracking-error dynamics
- Uses partial state measurements (not full state)
- Inserts recovery block between nominal controller and compromised actuator
- Prevents attack propagation into coordination layer
- Ensures attacks remain local, non-propagating, and compensable

### Key Innovations

1. **Undisclosed Leader Dynamics**: Leaders generate bounded trajectories but their dynamics, velocity bounds, and motion envelopes are unknown to followers
2. **Comprehensive Attack Model**: Handles state-correlated + input-correlated + bounded exogenous actuator false-data simultaneously
3. **Nonsmooth Lyapunov Analysis**: Proves asymptotic command containment (not just ultimate boundedness)
4. **Directed Topology Support**: Works with leader-rooted united spanning trees (no symmetry requirements)
5. **Minimum-Phase Requirement**: Only requires stable zero dynamics (Assumption 2), avoiding vulnerabilities to zero-dynamic attacks

### Mathematical Foundation

**System Model** (per follower i):
```
ẋᵢ = Aᵢxᵢ + Bᵢ(Lᵢηᵢ + ψᵢuᵢ)
η̇ᵢ = Γᵢηᵢ + Λᵢyᵢ
yᵢ = Cᵢxᵢ
```
- xᵢ ∈ ℝ^(∑dₖᵢ): external state (outputs and derivatives up to order dₖᵢ-1)
- ηᵢ ∈ ℝ^(nᵢ-∑dₖᵢ): zero-dynamics coordinates
- ψᵢ ∈ ℝᵐˣᵐ: known invertible input matrix

**Attack Model** (per follower i):
```
uᵢᵃ = uᵢ + Kₐₓᵢ(xᵢ,t)xᵢ + Kₐᵤᵢ(t)uᵢ + wᵤᶜₐᵢ(t)
```
- Kₐₓᵢ(xᵢ,t)xᵢ: state-correlated attack (admissible growth structure via known envelope)
- Kₐᵤᵢ(t)uᵢ: input-correlated attack (bounded, preserves positive input authority)
- wᵤᶜₐᵢ(t): exogenous false-data injection (bounded)

**Containment Objective**: 
- Command-level: Asymptotic containment (followers' commands converge to leader convex hull)
- Physical-level: Ultimate boundedness (physical outputs converge to leader convex hull up to residual)

## Implementation Pattern

### When to Apply

Use this methodology when designing:
- Multi-agent coordination under adversarial actuator attacks
- Resilient CPS systems with undisclosed leader dynamics
- Fault-tolerant distributed control over directed networks
- Containment tracking with heterogeneous agents (different relative degrees)

### Design Workflow

1. **Verify Assumptions**:
   - United spanning tree rooted at leaders (Assumption 1)
   - Minimum-phase zero dynamics: Γᵢ Hurwitz (Assumption 2)
   - Partial state measurements available: xᵢ accessible (Assumption 3)
   - Leader trajectories bounded and locally absolutely continuous (Assumption 4)

2. **Characterize Attack Envelopes**:
   - State-correlated: Define admissible growth via RKHS kernel kₓᵢ or polynomial envelope
   - Input-correlated: Verify Δᵤᵢ(t) = Iₘ + ψᵢKₐᵤᵢ(t)ψᵢ⁻¹ satisfies sᵀΔᵤᵢ(t)s ≥ χᵢ‖s‖²
   - Exogenous: Establish bounded envelope for wᵤᶜₐᵢ(t)

3. **Design Network Interface**:
   - Define task-space command variables matching output dimensions
   - Implement continuous adaptive protocol using neighbor information only
   - Avoid discontinuous terms (prevents chattering)
   - No global graph Laplacian eigenvalue information needed

4. **Design Virtual-Actuator Layer**:
   - Insert recovery block between controller and actuator
   - Use partial state feedback (xᵢ only, not ηᵢ)
   - Compensate for all three attack components simultaneously
   - Ensure local stability without propagating to network layer

5. **Stability Analysis**:
   - Apply nonsmooth Lyapunov analysis for command containment
   - Prove asymptotic convergence at command level
   - Establish ultimate boundedness at physical output level
   - Quantify residual based on command-tracking controller performance

## Critical Pitfalls

1. **Do NOT require full state measurements**: The methodology specifically uses partial state (xᵢ) to avoid needing zero-dynamics state ηᵢ. Full-state designs are more vulnerable and less practical.

2. **Do NOT use discontinuous protocols**: Sliding mode approaches introduce chattering. Continuous adaptive protocols recover asymptotic convergence.

3. **Do NOT assume leader model knowledge**: The strength is handling undisclosed leader dynamics. Requiring exosystem models or velocity bounds defeats the purpose.

4. **Do NOT neglect zero-dynamic attack vulnerabilities**: Unstable zero dynamics (non-minimum-phase) create attack surfaces. Verify Γᵢ is Hurwitz.

5. **Do NOT confuse command vs. physical containment**: Command containment is asymptotic; physical containment has residual due to heterogeneous relative degrees and attack compensation limits.

6. **Do NOT require symmetric graphs**: The methodology works with directed graphs (united spanning tree condition), not just undirected or detailed-balanced topologies.

## Validation & Testing

### Simulation Benchmarks
- **Quadrotor networks with damped suspended loads**: Demonstrates attack recovery and containment tracking
- **Heterogeneous relative degrees**: Test with different dᵢ vectors across followers
- **Combined attacks**: Simultaneous state-correlated + input-correlated + exogenous attacks
- **Directed topology**: Verify with non-symmetric adjacency matrices

### Metrics
- Command containment error: Should converge to zero asymptotically
- Physical output containment error: Should be ultimately bounded with small residual
- Attack compensation: Virtual-actuator should isolate attacks from network layer
- Chattering: Continuous protocols should eliminate high-frequency oscillations

## Related Patterns

- **Layered Defense in Depth**: Network layer + local execution layer separation
- **Fault-Hiding Virtual Actuators**: Recovery block insertion without controller redesign
- **Adaptive Robust Control**: Continuous adaptation without discontinuous switching
- **Distributed Observer-Free Design**: Avoid leader model reconstruction entirely

## Applications

- **Resilient drone swarms**: Containment under GPS spoofing or actuator hijacking
- **Microgrid coordination**: Distributed energy resources under cyber-attacks
- **Autonomous vehicle platooning**: Leader-follower containment with compromised actuators
- **Industrial multi-robot systems**: Task-space coordination under local faults/attacks
- **Satellite formation flying**: Undisclosed leader maneuvers with actuator degradation

## References

- Paper: arXiv:2606.27257
- Key concepts: Virtual actuators, fault-hiding, adaptive containment, directed graphs, cyber-physical security
- Mathematical tools: Nonsmooth Lyapunov analysis, normal-form coordinates, M-matrix theory
