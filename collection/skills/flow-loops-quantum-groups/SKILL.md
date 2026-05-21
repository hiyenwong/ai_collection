---
name: flow-loops-quantum-groups
description: "Methodology connecting quantum group invariants with Morse flow dynamics for knot theory. Use when analyzing knot invariants, quantum groups, colored Jones polynomials, or BPS state counting. Keywords: flow loops, quantum groups, knot invariants, Morse flows, BPS q-series"
---

# Flow Loops and Quantum Groups

## Core Concepts

### Two Perspectives on Knots
1. **Quantum group invariants**: Algebraic approach using representation theory of quantum groups
2. **Morse flow dynamics**: Geometric approach using dynamical systems on knot complements

### Main Correspondence
For fibered knots, the dynamical series from Morse flow loops in the complement equals the BPS q-series from quantum group Verma modules:
```
Morse_flow_series(q, t) = BPS_q_series(q, t)
```
This encodes all colored Jones polynomials.

## Usage Patterns

### Pattern 1: Knot Invariant Computation via Flow Loops
For fibered knots:
1. Identify the fibration structure of the knot complement
2. Define Morse flow on the complement with appropriate boundary conditions
3. Count periodic flow loops (orbits) weighted by their topological data
4. Construct two-variable series invariant: `Σ (loop weight) · q^n · t^m`

### Pattern 2: BPS q-Series from Quantum Groups
For any knot with quantum group representation:
1. Construct Verma module for the quantum group at the knot's representation
2. Compute BPS state counting via the module's character
3. The resulting q-series encodes colored Jones polynomials

### Pattern 3: Proving Correspondence for Braid-Homogeneous Knots
For braid-homogeneous knots (subclass of fibered knots):
1. The correspondence between Morse flow series and BPS q-series is proven
2. Use this to translate between dynamical and algebraic computations
3. Advantage: dynamical computation may be simpler for certain invariants

## Mathematical Framework

### Key Definitions
- **Fibered knot**: A knot whose complement fibers over S^1 with surface fibers
- **Morse flow**: A gradient-like flow on the knot complement
- **BPS q-series**: Generating function for BPS states, arising from quantum group Verma modules
- **Braid-homogeneous knot**: Knots admitting braid representatives with homogeneous writhe

### The Correspondence Theorem
For all braid-homogeneous knots:
```
Flow_loop_invariant(q, t) ≅ BPS_q_series(q, t)
```
Conjecture: This holds for all fibered knots.

## Error Handling

### Non-Fibered Knots
- Methodology requires fibration structure
- For non-fibered knots, consider alternative invariants (e.g., Khovanov homology)

### Non-Homogeneous Braids
- Correspondence proof requires braid-homogeneous property
- For general fibered knots, the correspondence remains conjectural

## Resources
- Paper: arXiv:2605.21382 "Flow loops and quantum groups" by Sunghyuk Park
