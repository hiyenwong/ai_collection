---
name: quantum-state-isomorphism-groups
description: >
  Quantum state isomorphism problems for groups methodology. Studies computational complexity
  of determining whether two quantum states are related by group actions. Covers pure-state
  (BQP-hard, QCMA∩QCSZK), mixed-state (QSZK-complete), and infinite group variants. Includes
  reductions for abelian, Clifford, Pauli, and bosonic linear optical groups. arXiv: 2605.12615.
---

# Quantum State Isomorphism for Groups

Computational complexity framework for quantum state isomorphism under group actions. Source: arXiv:2605.12615.

## Problem Definition

Given two quantum circuits preparing states |ψ₁⟩ and |ψ₂⟩, decide if ∃g ∈ G such that U_g|ψ₁⟩ = |ψ₂⟩.

## Complexity Results

### Pure-State Version
- **All nontrivial groups**: BQP-hard, contained in QCMA ∩ QCSZK
- **Abelian groups**: Reduces to state hidden subgroup over generalized dihedral group
- **Clifford group**: ≥ Graph Isomorphism (polynomial-time reduction)
- **Pauli group**: BQP-complete

### Mixed-State Version
- **Nontrivial, finite, efficiently representable groups**: QSZK-complete

### Infinite Groups
- **Bosonic linear optical unitaries**: ≥ Graph Isomorphism, contained in NP ∩ SZK
- Uses stellar representation for wave function description

## Key Results

1. Resolves open question [HEC25]: abelian state hidden subgroup on mixed states is QSZK-hard
2. Rules out efficient quantum algorithm unless QSZK = BQP
3. First study beyond symmetric group [LG17]

## Complexity Class Reference

| Class | Description |
|-------|-------------|
| BQP | Bounded-error Quantum Polynomial time |
| QCMA | Quantum Classical Merlin-Arthur |
| QCSZK | Quantum Computational Statistical Zero Knowledge |
| QSZK | Quantum Statistical Zero Knowledge |

## Relationship to Hidden Subgroup Problem

State isomorphism ⊂ Hidden Shift ⊂ Hidden Subgroup hierarchy:
- State isomorphism: given circuits, are states G-equivalent?
- Hidden shift: given oracles f, f∘s, find shift s
- Hidden subgroup: given f constant on cosets, find H

## Activation Keywords

- quantum state isomorphism
- state hidden subgroup problem
- quantum group actions
- quantum isomorphism complexity
- BQP-hard quantum problems
- QSZK-complete
- 量子态同构, 群作用

## Related Skills

- `quantum-complexity-math-structure`: Quantum computing complexity theory
- `quantum-algebraic-structures`: Quantum algebraic structures methodology
- `quantum-learning-theory`: Quantum learning theory methodology

## Resources

- arXiv: [2605.12615](https://arxiv.org/abs/2605.12615)
- PDF: [Download](https://arxiv.org/pdf/2605.12615)
