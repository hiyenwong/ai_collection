---
name: homological-percolation-monitored-qec
description: Homological percolation thresholds for randomly monitored QEC codes. Use when analyzing logical-survival transitions under random Pauli measurements.
category: ai_collection
---

# Homological Percolation in Randomly Monitored QEC Codes

**Source**: Watanabe, Sasamoto, Han, Trebst (Cologne/Tohoku), arXiv:2610.02310 (Oct 2026)

## Core Framework

Monitor a stabilizer code with ONE round of random single-qubit Pauli measurements: each qubit independently measured in X/Y/Z with probabilities (pX, pY, pZ), or left alone with pI = 1−r. **Logical information survives iff NO product of measured Pauli operators equals a nontrivial logical Pauli operator up to stabilizers.**

This is the *logical-support criterion* — the organizing principle that splits threshold behavior into two classes:

| Class | Example | Pure-Z threshold | ν | Mechanism |
|---|---|---|---|---|
| Geometric percolation | Toric code | pZ = 1/2 | 1.334(43) ≈ 4/3 | Stabilizer multiplications = local loop reroutings → reduces exactly to square-lattice bond percolation |
| Homological percolation | Color code | pZ = 1/2 | 1.2073(15) | Stabilizers allow string branching/recombination at trivalent junctions → NOT path connectivity; distinct universality class |

**Identical threshold locations need not imply identical critical behavior.** Color-code exponents (ν=1.2073, β/ν=0.11904, γ/ν=1.76049) satisfy hyperscaling H = 2β/ν + γ/ν = 1.99858(27) ≈ d = 2, evidence for a genuine new universality class.

## Key Results

1. **Coherent information as order parameter**: Entangle k logical qubits with k references; Ic(R|QC) = Σc pc·S(ρR(c)) counts surviving logical Bell pairs per realization. Average Ic → logical survival fraction. (Wen: full CI is conditional Shannon entropy of the logical sector.)
2. **Spherical phase diagrams** in (rX, rY, rZ): pure-axis thresholds (analytic where possible) give a semi-analytic boundary construction that matches numerics — "bites" along each axis where collapse dominates.
3. **Pure-Y toric code is special**: Y = XZ requires EVEN degree at every vertex AND even plaquette overlap → constrained percolation, transition only at pY = 1. Toric code has maximal Y-threshold = "infinite learning threshold" in weak-measurement analog.
4. **Wen plaquette (non-CSS)**: all three pure axes have threshold 1 (fully measured) — biased-noise robustness traced to diagonal repetition-code structure.
5. **3D codes**: string (Z) vs membrane (X) logicals give ordinary vs geometric-homological percolation on dual lattice; 3d color ν = 0.669→0.688.
6. **Gross code [[144,12,12]]** (BB(1̄,1̄,3,3)): mobility sublattice with 12×12 unit cell; multi-species fusion → slow approach to asymptotic scaling; practical threshold guidance for gross-code architectures.
7. **Anyon condensation view**: color-code "bites" = condensing Lagrangian subgroups Lp = {1, rp, gp, bp}; competing condensations → critical phase (purple region).

## Simulation Engine (the reusable pattern)

Scale to **1.4M qubits** — far beyond tableau (~20k):
- Work in face-syndrome space over F2: binary supports only, no destabilizers → N²/8 payload, ~32× storage reduction vs full tableau.
- Echelon-form basis + incremental elimination (reduce each incoming syndrome against existing basis, no full row updates).
- **Binomial convolution trick**: add measured qubits ONE at a time in random order → single run gives the entire probability curve (all r simultaneously). 26 sizes to L=840, 20k realizations each.
- Color-code face-only algebra: nfix(M) = |M| − rank(D_M) − rank(D) + rank(D_U); connectivity classes = coset labels of RM grouped per color.

## Threshold-Bound Theorems (practical payoff)

1. **Learning bound**: γc ≥ rc — weak-measurement (Nishimori/tunable-learning) threshold is LOWER-bounded by the easy-to-compute projective percolation threshold. Weak POVM F(γ) = γP + (1−γ)·(random sign) decomposes projective protocol as a coarse-graining → Ic_weak(γ) = H(Ξ|S) ≥ Ic_proj(r=γ).
2. **Decoding bounds**: minimum-weight decoding threshold ≥ qP(μlog) with μlog = exponential growth rate of irreducible logical operators; recorded Z-measurements ≡ detectable qubit loss (same threshold); (r,q) measurement–decoherence phase diagrams interpolate percolation endpoint ↔ Nishimori point.
3. **Wen/toric-Y maximal robustness**: q_eff = r/2 + (1−r)q < 1/2 whenever r<1, q<1/2 → optimal threshold 1/2 for ALL r — design principle for biased-noise decoders.
4. **Complexity dichotomy**: MW decoding poly-time (matching) for toric vs **NP-hard for (6,6,6) color code** — the branching string-net structure drives both the universality-class split and decoding hardness. Z3/MaxSAT used for color-code MW boundaries.

## Reuse Checklist

- Analyzing monitored/measurement-induced transitions in ANY stabilizer code → compute pure-axis thresholds first, build semi-analytic boundary, then verify with FSS.
- Large-scale stabilizer CI estimation → face-only binary elimination + binomial convolution, never full tableau.
- Estimating decoder thresholds cheaply → count irreducible logical operator growth (Peierls μlog) and apply qP bound.
- Cross-check universality claims → hyperscaling H = 2β/ν + γ/ν ≈ d.
