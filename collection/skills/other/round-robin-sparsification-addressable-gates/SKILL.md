---
name: round-robin-sparsification-addressable-gates
description: Fault-tolerant addressable transversal logical CZ gates for 2DTI qLDPC codes via round-robin sparsification. Use when designing addressable logical gates.
category: ai_collection
---

# Round-Robin Sparsification for Addressable FT Logical Gates

**Source**: Sahay (Google Quantum AI/Yale) & Jones (Google Quantum AI), arXiv:2610.03594 (Oct 2026)

## Problem

qLDPC codes encode many logical qubits, but transversal gates usually act on ALL logicals simultaneously. Addressability (gating ONE chosen logical pair without disturbing others) has relied on code surgery — O(d) measurement rounds, slow, error-prone. Unitary addressable transversal gates existed only for narrow code subclasses.

## Method: Sparsify the Round-Robin

**Round-robin (RR) circuit** between qubit sets Λ1, Λ2: RRCZ(Λ1,Λ2) = ∏i∈Λ1 ∏j∈Λ2 CZij.
- Case I: both sets = Z-logical supports → logical CZ (but NOT fault-tolerant: every qubit sits in ≥d gates → one error spreads to d locations).
- Case II: one set = Z-stabilizer support → **logical identity** ("stabilizer deformation").

**Sparsification**: conjugate the RR logical circuit by stabilizer deformations pivoted on each qubit:
U ← U · ∏q RR(q, Sq), where Sq = L(v,*,j)·L(v,*,j+1)·∏plaquette stabilizers (product of TWO equivalent logicals + stabilizer generators = stabilizer element spanning the lattice height).

Walk across columns j = 0..d−1 with α↔β alternating pivots; each pass cancels CZ² = I pairs and pushes support into the bulk. After d−1 columns: **max gate depth 3 per qubit, independent of code size** → transversal AND fault-tolerant AND addressable.

## Key Ingredients

1. **Cylinder trick** (from Ref. [17]) for general codes: find Z-symmetries (global check redundancies, ∏c = I) by Gaussian elimination on the parity-check matrix; take the product of all stabilizer generators inside a selection cylinder spanning half the lattice (width > stabilizer radius) → decomposes into TWO disjoint equivalent logicals L(·,·,∼0)·L(·,·,∼M/2). Slide the cylinder → **O(d) disjoint balanced-weight logical representatives** — exactly what sequential sparsification consumes.
2. **2DTI polynomial machinery**: stabilizers via A(x,y), B(x,y) monomial supports on M×N torus; codes = toric, cHGP2 [[18l²,8,2l]], cHGP3 [[98l²,18,4l]], color [[18l²,4,3l]], gross [[288,16,12]], directional NE3N [[36l²,4,4l]].
3. **Fault-distance analysis**: CZ spreads only X→Z. Connectivity anti-aligned with least-weight logicals → distance preserved natively; aligned connectivity gives weight-2 along a logical BUT extra detection events from the original X error identify the mechanism → fault distance d maintained without extra rounds.
4. **Full addressability**: symmetries related by translations Σi = x^h y^g Σj → sparsify once, then translate gate supports to target arbitrary (αi, βj). Intra-code + simultaneous multi-logical CZs compile from inter-code circuits.

## Surprising Empirical Finding

cHGP3 naive tCZ has reduced fault distance d/2 (stabilizer elements span ~2× wider when representatives skip). Distance-optimized variant (insert ONE Z-stabilizer SE round mid-circuit, carefully ordered gate subset → SE → rest) restores full d — **but LERs of naive d/2 and optimized d versions are near-identical at practical physical error rates**: combinatorial multiplicity of higher-weight errors dominates, and the optimized circuit's higher volume/decoding complexity can make the NAIVE degraded version better in practice. → Lesson: asymptotic distance ≠ practical LER; always simulate before "fixing" distance.

## Performance vs Code Surgery (gross code)

Addressable tCZ: **~4× lower space-time overhead, ~5× lower logical-error-rate impact** than the best in-module XX-measurement surgery primitive. Memory-like LER scaling O(p^d) verified d=3..9 across code families.

## Reuse Checklist

- Need unitary addressable 2-qubit Clifford on a 2DTI qLDPC code → build RR circuit on Z-logical supports, extract O(d) representatives via cylinder trick, sparsify column-by-column with stabilizer deformations, depth-3 result.
- Generalize: sparsify C^r_Z on r-dimensional TI codes (→ low-overhead magic-state prep where non-Clifford transversal); higher-degree polynomial codes open.
- Limits: requires coarse-grained 2D locality; non-local code families unclear.
- When a gadget loses asymptotic distance, simulate first — constant-factor volume may swamp the theoretical gain.
