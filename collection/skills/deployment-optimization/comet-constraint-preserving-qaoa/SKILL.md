---
name: comet-constraint-preserving-qaoa
description: "Constraint-preserving QAOA using XY-mixer for multiplex CRISPR gene editing optimization. Systematically compares structural constraint enforcement (XY-mixer) vs penalty-based approaches across simulator and real hardware. XY-mixer achieves >95% optimum probability by p=3 vs <6% for penalty variants. Activation: constraint-preserving QAOA, XY-mixer, CRISPR optimization, QUBO constraint enforcement, quantum gene editing, 约束保持QAOA"
metadata:
  arxiv_id: "2607.02622"
  published: "2026-07-02"
  authors: "COMET authors"
  tags: [qaoa, constraint-preservation, xy-mixer, crispr, combinatorial-optimization]
---

# COMET: Constraint-Preserving QAOA

## Core Methodology

**Problem**: Multiplex CRISPR-Cas9 gene editing requires selecting one guide RNA per target gene — a constrained combinatorial problem. Conventional QAOA uses quadratic penalty terms to enforce constraints, but penalty coefficient selection is heuristic and penalties amplify hardware noise.

**Solution**: Enforce constraints structurally via XY-mixer instead of penalty terms.

## Key Results (3-gene, 12-qubit instance)

| Method | Simulator (p=3) | Hardware Gap |
|---|---|---|
| XY-mixer | >95% optimum prob | |ΔE| ≤ 0.8 |
| Penalty (best λ) | <6% optimum prob | |ΔE| up to +53.9 |

**Findings**:
- XY-mixer preserves feasibility by construction — no penalty tuning needed
- Penalty variants span order of magnitude in coefficient, all underperform
- On real hardware (ibm_kingston, Heron r2): XY-mixer simulator-hardware gap stays within |0.8|
- Structural guarantee partially breaks under gate-level noise — honest accounting provided

## Usage Patterns

### Pattern 1: Constraint-Preserving QAOA Design
When formulating constrained QUBO problems for QAOA:
1. Identify one-hot constraints (e.g., exactly-one-per-group)
2. Replace penalty Hamiltonian with XY-mixer
3. Mixer preserves feasible subspace by construction — no penalty coefficient tuning
4. Compare against penalty baseline across λ values

### Pattern 2: Penalty vs Mixer Comparison
When evaluating constraint enforcement strategies:
1. Test penalty method across order of magnitude in penalty coefficient (λ)
2. Test XY-mixer with same QAOA depth
3. Measure: optimum probability, simulator-hardware energy gap
4. Note: penalty tuning is heuristic; mixer is principled

### Pattern 3: Hardware Validation
When validating on real quantum hardware:
1. Run both penalty and mixer variants at same depths
2. Measure simulator-hardware energy gap
3. Account for gate-level noise breaking structural guarantees
4. Report honest hardware performance, not just simulator results

## Activation Keywords
- constraint-preserving QAOA
- XY-mixer quantum optimization
- CRISPR gene editing optimization
- QUBO constraint enforcement
- penalty-free quantum optimization
- quantum combinatorial optimization
- 约束保持QAOA
- XY混合器

## Related Skills
- `qaoa-xy-mixers-portfolio` — XY-mixers for portfolio optimization (same constraint technique)
- `penalty-free-quantum-annealing-portfolio` — penalty-free optimization
- `qaoa-optimization` — general QAOA methodology
- `qaoa-manifold-optimization` — QAOA optimization techniques
- `qaoa-zne-portfolio` — QAOA with error mitigation
