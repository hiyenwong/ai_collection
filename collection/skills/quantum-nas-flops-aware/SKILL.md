---
name: quantum-nas-flops-aware
category: quantum-systems-engineering
description: FLOPs-aware neural architecture search methodology for building hardware-efficient hybrid quantum-classical neural networks (HQNNs) that are both accurate and computationally deployable.
source: arXiv 2605.18345
trigger: quantum architecture search, HQNN design, hardware-aware quantum ML, FLOPs optimization, NISQ deployment, quantum-classical neural networks
---

# FLOPs-Aware Hybrid Quantum-Classical Neural Architecture Search

## Trigger Conditions
- Designing hybrid quantum-classical neural networks (HQNNs) for NISQ-era deployment
- Need to optimize quantum circuit architecture under hardware constraints
- Manual HQNN design becomes intractable with multiple architectural choices
- Must balance accuracy with computational efficiency and deployability

## Methodology Overview
Extends Neural Architecture Search (NAS) to quantum and hybrid settings by incorporating FLOPs-aware search as a proxy for computational complexity. Systematically explores data encoding, circuit structure, measurement design, and classical-quantum coupling to find architectures that are both accurate and practically deployable.

## Core Steps
1. **Define the search space**: data encoding strategies, circuit structures (ansatz), measurement observables, classical-quantum coupling patterns
2. **Set hardware constraints**: max qubit count, circuit depth, gate fidelity, connectivity topology
3. **Use FLOPs as proxy** for computational complexity during search evaluation
4. **Search strategy**: gradient-based NAS, evolutionary search, or reinforcement learning-based architecture sampling
5. **Evaluate candidates** on both accuracy and FLOPs, maintaining a Pareto frontier
6. **Select final architecture** based on accuracy-FLOPs trade-off for target deployment scenario

## Key Technical Details
- **Search dimensions**: data encoding, circuit ansatz, measurement design, classical-quantum coupling
- **FLOPs proxy**: counts quantum gate operations + classical neural network FLOPs
- **Hardware constraints**: qubit count, depth limits, native gate sets, connectivity
- **Output**: Pareto-optimal HQNN architectures ranked by accuracy-efficiency trade-off

## Pitfalls
- FLOPs is an imperfect proxy — actual wall-clock time depends on hardware-specific factors
- Quantum gate FLOPs don't capture decoherence and error rates
- Search space can be exponentially large — use hierarchical or progressive search strategies
- Classical-quantum coupling design significantly impacts end-to-end trainability
- Over-optimizing for FLOPs may sacrifice expressiveness — maintain accuracy threshold

## Verification
- Benchmark final architecture against manually designed baselines
- Verify hardware compatibility (circuit fits on target device)
- Measure actual inference/training time vs. FLOPs prediction
- Compare accuracy on hold-out datasets
