---
name: iddmbse-integrated-data-model-based-se
description: "IDDMBSE: Integrating Data-Driven and Model-Based Systems Engineering for Trusted Autonomous Cyber-Physical Systems (arXiv:2606.06727). Three-tool open-source chain (PERFECT, TRADES-X, VERITAS) extending MBSE V-process with data-driven loops for autonomous CPS design and verification."
activation:
  - MBSE
  - cyber-physical systems
  - data-driven systems engineering
  - SysML
  - autonomous CPS
  - V-process
  - conformal prediction
  - behavior trees
  - design-space exploration
  - SysML v2
---

# IDDMBSE: Integrated Data-Driven and Model-Based Systems Engineering

> arXiv: 2606.06727 — June 2026 — John S. Baras et al., University of Maryland

## Core Problem
Autonomous CPS interleave model-based components (kinematics, planners) with learned ones (perception networks, RL policies). MBSE lacks native ML/AI integration; ML/AI lacks formal traceability. IDDMBSE bridges this.

## Three-Tool Chain

### PERFECT (Performance Evaluation)
- Maps SysML system architectures → executable ROS autonomy stacks
- Enables scalable performance evaluation from formal models
- Interop: SysML model ↔ ROS nodes

### TRADES-X (Design-Space Exploration)
- Two-stage decomposition:
  1. Model-based optimization (physics/kinematic constraints)
  2. Data-driven evaluation (surrogate/learned models where physics fails)
- Hybrid trade-off: formal prior + empirical coverage

### VERITAS (Verification)
- Three-layer assurance workflow:
  1. Formal verification (temporal logic, safety invariants)
  2. Data-driven verification (learned bounds, conformal prediction)
  3. Runtime verification (monitoring during execution)
- Convergence: formal guarantees + statistical coverage

## Key Patterns

### Data-Driven Loop Augmentation
Every MBSE V-process step gets a data-driven augmentation:
- Structure → learned component models
- Behavior → data-driven simulation where physics insufficient
- Requirements → data-driven gap analysis where model under-satisfies
- Trade-off → hybrid model+data optimization
- Verification → conformal prediction for robust perception

### Conformal Prediction for Robust Perception
- Use conformal prediction to bound perception uncertainty at runtime
- Guarantees: coverage probability ≥ 1-α without distributional assumptions
- Practical: wraps any learned perception network with valid uncertainty bands

### Behavior-Tree Task Verification
- Behavior trees provide compositional task specification
- VERITAS checks tree execution against formal task properties
- Enables modular verification of complex autonomy behaviors

### SysML v2 / KerML Forward Path
- Re-formulating on SysML v2 foundations for language-native composability
- KerML (Kernel Modeling Language) enables tighter ML/AI integration
- Future: native ML component modeling within SysML type system

## Implementation Checklist
1. Model system in SysML (blocks, interfaces, requirements)
2. PERFECT: export to ROS2 autonomy stack
3. TRADES-X: run hybrid optimization (model → data refinement)
4. VERITAS: apply 3-layer verification (formal → data-driven → runtime)
5. Instrument with conformal prediction for perception uncertainty
6. Use behavior trees for compositional task verification
7. Target SysML v2 for future-proof ML integration

## Pitfalls
- Do NOT treat ML as black box — IDDMBSE requires ML components to expose interfaces
- Conformal prediction needs calibration data representative of deployment distribution
- TRADES-X two-stage is sequential, not parallel — model stage MUST complete before data stage
- VERITAS formal verification scales poorly — limit scope to safety-critical properties
- Isaac Sim test range required for realistic CPS validation

## Activation
Use when designing autonomous CPS that combine model-based and ML/AI components, when MBSE rigor is needed for learned systems, or when verification of hybrid architectures is required.