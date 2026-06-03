---
name: quantum-linear-reservoir-bottleneck
description: "Analysis of hidden bottleneck in classical and quantum linear reservoir computing. Identifies fundamental information processing capacity limits when reservoir features and readout are both linear. Use when: reservoir computing design, quantum reservoir computing, linear system capacity analysis, information processing capacity bounds, echo state networks, quantum machine learning architecture design."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.29071"
  published: "2026-05-29"
  tags: [quantum, reservoir-computing, linear-systems, information-capacity, machine-learning]
---

# Hidden Bottleneck in Linear Reservoir Computing

## Core Methodology

Identifies a fundamental bottleneck in linear reservoir computers (both classical and quantum): when measured features evolve linearly in the reservoir and the output is formed by linear readout, the information processing capacity is severely limited regardless of reservoir size.

## Key Insights

1. **Linearity Bottleneck**: Linear reservoir + linear readout = fundamentally limited expressivity, even with infinite reservoir size
2. **Quantum Does Not Help**: Quantum linear reservoirs suffer from the same bottleneck—quantumness alone does not break the linearity limit
3. **Capacity Bound**: Derives explicit upper bounds on information processing capacity for linear reservoir systems
4. **Design Implication**: Nonlinear feature extraction is essential—either in the reservoir dynamics or the measurement/readout

## Mathematical Result

For a linear reservoir with state evolution x(t+1) = Ax(t) + Bu(t) and linear readout y(t) = Cx(t):
- The effective memory depth is bounded by the rank of the observability matrix
- Adding more reservoir dimensions does not increase capacity beyond this bound
- The bottleneck is structural, not a matter of training or optimization

## When to Use

- Designing reservoir computing systems (classical or quantum)
- Analyzing why a linear reservoir underperforms
- Deciding whether to add nonlinear features to a reservoir
- Understanding fundamental limits of linear dynamical systems for ML

## Practical Recommendations

1. **Add nonlinearity in measurement**: Use nonlinear observables/measurement operators
2. **Add nonlinearity in dynamics**: Introduce nonlinear state transitions
3. **Kernel trick**: Map linear features to nonlinear feature space before readout
4. **For quantum reservoirs**: Use nonlinear measurement bases, not just computational basis

## Related Approaches

- Echo State Networks (ESNs) with nonlinear activation
- Liquid State Machines
- Quantum reservoir computing with nonlinear readout
- Kernel methods for dynamical systems
