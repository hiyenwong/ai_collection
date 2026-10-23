---
name: quantum-convolution-submodular-entropy
description: Use when proving quantum entropy growth inequalities.
category: ai_collection
---

# Submodularity of Entropy under Quantum Convolution

**Paper**: Submodularity of entropy under quantum convolution (arXiv:2609.40211, Milad M. Goodarzi — Centre for Quantum Technologies, NUS, Sep 2026)

## Core Insight

A submodular framework for von Neumann entropy of discrete quantum convolutions — the noncommutative counterpart of the *direct side* of entropic additive combinatorics. The entropy gains of compatible convolution families carry a **polymatroidal geometry**, which mechanically yields convolutional strong subadditivity, quantum Ruzsa triangle inequality, and quantum Plünnecke–Ruzsa inequalities.

## Setup

- **Globally weighted quantum convolutions**: compatible families indexed by admissible subsets of a fixed input collection (weights generalized via admissible kernels).
- **Main Theorem (4.1)**: relative to any fixed nonempty admissible block R, the physical entropy gains
  `g(J) = S(C_{R∪J}) − S(C_R)`
  extend to a **normalized, monotone, submodular** function on the full subset lattice of remaining inputs — defined even where the physical convolution C_{R∪J} is NOT admissible.
- Fractional subadditivity then yields the whole hierarchy of convolutional entropy inequalities.

## Derived Inequalities

1. **Convolutional strong subadditivity**: S(C_{R∪M}) − S(C_R) ≤ Σ_j [S(C_{R∪{j}}) − S(C_R)] for admissible sets.
2. **Quantum Ruzsa triangle inequality** for arbitrary input states.
3. **Quantum entropic Plünnecke–Ruzsa inequalities**: for repeated inputs, entropy growth of an admissible m-fold convolution is at most δ_q[ρ]^(m−1), where **δ_q[ρ] is the quantum doubling constant**. The exponent m−1 is **optimal**, already among states diagonal in the computational basis.
4. **Doubling-constant control**: δ_q[ρ] alone controls all higher admissible convolution entropies with optimal exponents.

## Proof Method

Representation connecting convolution entropy with **marginal entropies of a single auxiliary state** — reduce the quantum-convolution claim to ordinary submodularity of marginal entropy on a constructed state, making the arithmetic requirements explicit while the entropy argument runs on the entire subset lattice.

## Reusable Patterns

1. **Submodular-extension template**: to prove an entropy-inequality family, (a) define physical gains on admissible subsets, (b) prove/assume a submodular extension to the full subset lattice (even where the physical object is undefined), (c) apply fractional subadditivity / polymatroid machinery to harvest all inequalities at once. Directly transferable to other noncommutative settings (free probability, operator algebras).
2. **Auxiliary-state marginalization**: encode multi-input convolution entropy as marginal entropies of ONE auxiliary state — turns convolution questions into standard SSA applications.
3. **Doubling constant as master invariant**: one 2-fold quantity governs all m-fold growth (Plünnecke-style) — look for the analogue in any resource-growth problem.
4. **Direct-side quantum additive combinatorics**: the paper completes the quantum picture of the *direct side* (sumset growth bounds); inverse-side analogues (structure from small growth) remain open — a research direction.

## Activation

quantum convolution, von Neumann entropy, submodular, polymatroid, Ruzsa triangle inequality, Plünnecke-Ruzsa, additive combinatorics, doubling constant, entropy inequalities, strong subadditivity, noncommutative entropy, auxiliary state
