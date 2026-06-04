---
name: scaling-laws-quantum-states
description: "Scaling laws methodology for Neural-Network Quantum States — power-law relations between loss, architecture size, and compute for characterizing the complexity of quantum many-body learning problems. Use when: analyzing NNQS complexity, benchmarking variational ansätze, transformer wave functions, frustrated quantum systems, scaling collapse in physics, variational quantum states."
metadata:
  arxiv_id: "2606.02794"
  published: "2026-06-03"
  tags: [quantum, scaling-laws, nnqs, transformer, frustrated-systems, variational]
---

# Scaling Laws for Neural-Network Quantum States

## Core Innovation

Scaling laws — power-law relations between loss, architecture size, and compute — are well-known in modern neural networks but unexplored for physical problems. This work establishes scaling laws as a general framework for benchmarking variational ansätze in quantum many-body systems using Neural-Network Quantum States (NNQS).

## Methodology

### V-Score as Loss Proxy
- Use the V-score (variational energy variance normalized by classical bounds) as the accuracy measure
- V-score decays as a power law in training compute: V ~ C^(-α)
- The exponent α reflects how rapidly additional compute translates into improved accuracy

### Scaling Collapse
- Under appropriate rescaling of compute, results for different system sizes collapse onto a single curve
- Analogous to scaling collapse in critical phenomena
- The power law exponent is approximately independent of system size — showing transformer ansatz is size-consistent

### Frustration as Difficulty Measure
- The exponent α decreases systematically with frustration
- Frustration level quantitatively measures representational difficulty of the ground state
- More frustrated systems require exponentially more compute for equivalent accuracy

## Key Findings

1. **Size consistency**: Transformer ansatz maintains power-law scaling across system sizes (up to 20×20 sites)
2. **Frustration scaling**: Triangular lattice (frustrated) shows lower α than square lattice (less frustrated)
3. **Universal curves**: Different system sizes collapse to single scaling curve under compute rescaling
4. **Benchmarking framework**: Scaling laws provide quantitative framework for comparing variational ansätze

## Application to Systems Engineering

- **Resource planning**: Predict compute needed for target accuracy in quantum simulation
- **Architecture selection**: Compare ansätze via their scaling exponents
- **Problem difficulty**: Quantify frustration/computational difficulty before committing resources
- **Transfer learning**: Scaling collapse suggests lessons from small systems transfer to large

## Pitfalls

- V-score is specific to variational quantum states — not directly applicable to all ML problems
- Scaling exponent depends on both model class and problem structure
- Frustration measure must be defined for the specific Hamiltonian
- Power-law regime may have different scaling at very small/large compute budgets

## Activation

scaling laws neural network quantum states, nnqs benchmarking, transformer wave function scaling, frustrated quantum systems, variational ansatz comparison, quantum many-body learning, scaling collapse physics, V-score power law

## Related Skills

- quantum-ml-patterns
- quantum-neural-architecture
- quantum-systems-engineering