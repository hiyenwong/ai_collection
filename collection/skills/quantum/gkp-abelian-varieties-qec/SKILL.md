---
name: gkp-abelian-varieties-qec
description: GKP-Abelian Varieties QEC methodology — mathematical framework connecting complex abelian varieties (algebraic geometry/number theory) to Gottesman-Kitaev-Preskill quantum error-correcting codes. Maps code space to theta functions, Pauli gates to theta groups, Clifford gates to automorphisms, stabilizer concatenation to isogeny. Proves encoding is asymptotically isometric and failure probability is governed by the systolic invariant of the polarization. Use when analyzing GKP codes, quantum error correction via algebraic geometry, theta function quantum computing, or systolic bounds on code performance.
---

# GKP-Abelian Varieties Quantum Error Correction

## Overview

GKP (Gottesman-Kitaev-Preskill) codes are continuous-variable quantum error-correcting codes built from symplectically integral lattices. The framework by Mayrand & Royer (arXiv:2605.28784) establishes a precise mathematical dictionary between GKP code theory and the classical theory of complex abelian varieties (algebraic geometry / number theory).

## Mathematical Dictionary

| GKP Concept | Abelian Varieties Concept |
|---|---|
| Symplectic lattice L | Polarized abelian variety (A, H) |
| Code space (finite-dim) | Space of theta functions |
| Logical Pauli gates | Theta group elements |
| Passive logical Clifford gates | Automorphisms of (A, H) |
| Concatenation with stabilizer codes | Isogeny |
| Encoding map | Asymptotically isometric embedding |
| Failure probability (small noise) | Shortest displacement in kernel of polarization isogeny (systolic invariant) |

## Key Results

1. **Asymptotic Isometry**: The encoding map from the code space to theta functions is asymptotically isometric, preserving inner products in the large-lattice limit.

2. **Clifford via Gaussian**: Every logical Clifford gate on the GKP code is realized by a Gaussian unitary operation — a consequence of the correspondence between Clifford gates and automorphisms of the polarized abelian variety.

3. **Systolic Error Bound**: For noise of small variance σ², the logical failure probability P_fail is governed to first order by:
   ```
   P_fail ∝ exp(-d_min² / (2σ²))
   ```
   where d_min is the shortest nontrivial displacement in the kernel of the polarization isogeny — a systolic invariant of the underlying polarization.

4. **Isogeny Concatenation**: Concatenating GKP codes with stabilizer codes corresponds to applying isogenies between abelian varieties, providing a geometric interpretation of code concatenation.

## Usage Patterns

### Analyzing GKP Code Properties
1. Identify the symplectic lattice defining the GKP code
2. Construct the associated polarized abelian variety (A, H)
3. Map quantum operations to geometric objects via the dictionary
4. Use algebraic geometry tools to analyze code properties

### Computing Error Bounds via Systolic Invariants
1. Determine the polarization isogeny φ: A → B
2. Find the kernel ker(φ) and its shortest nonzero element d_min
3. The systolic invariant d_min bounds the failure probability for small-variance noise
4. Optimize lattice choice to maximize d_min for given code parameters

### Designing Codes via Isogeny
1. Start with a base GKP code (base abelian variety)
2. Choose an isogeny corresponding to desired stabilizer code
3. The resulting code inherits properties from both varieties
4. Analyze via composition of isogenies

## Application Domains

- Continuous-variable quantum computing
- Quantum error correction with bosonic modes
- Algebraic geometry methods in quantum information
- Number theory applications to quantum codes
- Lattice-based quantum cryptography
- Geometric analysis of quantum codes

## Related Concepts

- **Theta functions**: Holomorphic functions on complex tori, correspond to code states
- **Symplectic geometry**: Framework for continuous-variable quantum mechanics
- **Polarization**: Additional structure on abelian variety encoding the symplectic form
- **Theta group**: Finite group extension encoding logical Pauli operators
- **Isogeny**: Surjective morphism with finite kernel, corresponds to code concatenation
- **Systole**: Shortest nontrivial cycle, bounds code performance

## Resources

- **Paper**: "Complex abelian varieties and quantum error correction: a mathematical framework for GKP codes" — Maxence Mayrand, Baptiste Royer (arXiv:2605.28784, May 2026)
- **GKP Original**: Gottesman, Kitaev, Preskill (2001) — original continuous-variable QEC codes
- **Abelian Varieties**: Mumford, "Abelian Varieties" — classical reference
- **Theta Functions**: Mumford, "Tata Lectures on Theta"
