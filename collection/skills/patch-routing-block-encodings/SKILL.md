---
name: patch-routing-block-encodings
category: ai_collection
description: Use when block-encoding lattice Hamiltonians with patches.
version: "1.0.0"
source: arXiv:2610.32946
source_title: "Low-frustration block encodings by patch routing"
authors: "Minzhao Liu, Abeynaya Gnanasekaran, Ananth Kaushik, Siddharth Hariprakash, Alireza Marefat Khah, Martin Roetteler, Grant Salton (IonQ Inc.)"
author: qc-cron-2026-10-27
license: MIT
published: 2026-10-23
categories: quant-ph
metadata:
  hermes:
    tags: [quantum-computing, block-encoding, qubitization, lattice-hamiltonians, qet, frustrated-magnets]
    related_skills: [svd-thc-molecular-ensemble-block-encoding, fourier-lcu-quantum-optimization, tdp-resource-estimation-uncertainty-propagation, hamqasbench-hamiltonian-qas-benchmark]
arxiv_id: "2610.32946"
trigger_words:
  - block encoding
  - patch routing
  - lattice Hamiltonian simulation
  - qubitization QPE
  - LCU normalization
  - spectral block encoding
  - quantum eigenvalue transformation
  - frustrated Heisenberg model
  - Fermi-Hubbard simulation
  - Halmos dilation
---

# Low-Frustration Block Encodings by Patch Routing

## When to Use

- Block-encoding a translation-invariant lattice Hamiltonian (Heisenberg, Fermi-Hubbard, spin-liquid) for qubitized QPE / QSVT / eigenstate filtering, where Pauli-LCU normalization (L1 norm) or unary-iteration selection cost dominates.
- Choosing the patch size / interaction grouping that trades local circuit cost against query count (normalization).
- Routing patches coherently on spin OR fermionic (JW) encodings of periodic lattices, including long-range patches and general unit cells.
- Improving an existing block encoding's normalization via QET without rebuilding the full eigenbasis.

## Core Problem

Pauli LCU prepares H/Λ with Λ = Σ|λp| (L1 norm, often far above optimal (Emax−Emin)/2), and product-wise selection costs ~8f(Ns−1) T gates. Larger interaction patches give tighter spectral bounds (they absorb frustration locally), but a naive SEL copies the expensive local circuit to every patch site, multiplying cost by Ns. Patch routing removes that multiplication.

## Construction

### 1. Patch decomposition and normalization

- H = Σ_p H_p over translated patches (overlap allowed; weight interactions so the sum reconstructs H, e.g. each NN bond split J1/2 across its 2 plaquettes).
- Per-patch shift/normalization from exact (or rigorous) spectral bounds: δp = (up+lp)/2, λp = (up−lp)/2 with lp ≤ emin(Hp), up ≥ emax(Hp).
- Global: Δ = Σ_p δp, Λ = Σ_p λp (valid since Σ emin(Hp) ≤ Emin, Σ emax(Hp) ≥ Emax). Bigger patches → more frustration captured → tighter Λ. For frustration-free decompositions L is exact.
- PREP on the address register: |L⟩ = Σ_p √(λp/Λ)|p⟩; T_PREP ≤ 32⌈log2 M⌉ + 8.

### 2. Routing (the amortization trick)

SEL = R†(I ⊗ B_ref)R with R = Σ_p |p⟩⟨p| ⊗ Π_p (Π_p routes patch p to a FIXED location). The local encoding B_ref is applied ONCE, uncontrolled on the address. Cost per query:

```
T_BE = 2·T_PREP + T_R + T_BE^p     (local cost paid once, independent of Ns)
```

Verified routing bounds (fitz-recovered exact forms):
- 2×2 square spin plaquette: T_R□ ≤ 8Ns + 16⌈(log2 Ns)/2⌉ − 64; with order correction T_R□,ord ≤ 8Ns + 16⌈(log2 Ns)/2⌉ − 32. For Ns = M² both reduce to 8Ns + 16⌈log2 M⌉ + O(1).
- Fermionic (JW): T_R^FH ≤ 8Ns + 16⌈(log2 Ns − 1)/2⌉ − 32 (Ns = 2M² → same 8Ns + 16⌈log2 M⌉ + O(1)).
- U×U patches (U | M): T_R(U,q) ≤ 8Ns + 16qU·SU − 8qU² + DU(Ns) + 8(U−1)⌈(log2(Ns/q))/2 − log2 U + ⌈log2 U⌉ − 3⌉, SU = Σ_{j=0}^{⌈log2U⌉−1}[U − gcd(U, 2^j)].
- 3×3 spin patch: T_R ≤ 8N + 16⌈log2 M⌉ + 32⌈log2(M/3)⌉ − 24 (M multiple of 3).

Routing mechanics (1D chain, M even): route pair (px, px+1) to (s, 1−s) with s = px mod 2 — even sites always land at 0, odd at 1, so the chain splits into two independent CSWAP trees on M/2 qubits each (addresses: even net uses (t+s) mod M/2, odd uses t; coherent modular increment then uncompute). 2D: route columns then rows; the destination block may be row/column-reflected — no correction needed iff the patch Hamiltonian is reflection-invariant (Heisenberg plaquette is; otherwise exchange destination columns/rows controlled on s,u and undo).

Fermionic routing: choose JW mode ordering so parity classes never cross (order: spin, then x-parity, then y-parity classes; a(σ,x,y) = σM² + (x mod 2)(M²/2) + (y mod 2)(M²/4) + ...). Replace each CSWAP by controlled-fswap: fswap,ij|...,ni,...,nj,...⟩ = (−1)^(ni·nj+(ni⊕nj)·Πij)|...,nj,...,ni,...⟩, Πij = Σ_{i<r<j} n_r. Gadget = 2 logical ANDs + interval-parity CNOTs; routed modes land non-adjacent → 8 extra fswaps gather them to modes 0..7 (negligible). General lattices: route whole unit cells (honeycomb: 2×2 cell block = 8 spins).

### 3. Local spectral block encoding

A = (Hp − δp I)/λp is a Hermitian contraction. Halmos dilation (1 signal qubit w):

```
B(A) = [[A, √(I−A²)], [√(I−A²), −A]] = Z_w⊗A + X_w⊗√(I−A²)
```

Hermitian AND unitary → a reflection (B² = I); signal block = A. Spectral/circuit form: B(A) = (I⊗V_p†)[Σ_j Ry(2 arccos a_j)⊗Q_j](I⊗V_p)(Z_w⊗I) — basis change V_p maps eigenspaces to computational states; ONE controlled rotation per DISTINCT eigenvalue (per degenerate eigenspace); eigenvalues at ±1 need no arbitrary rotation.

Cost-reduction structure to exploit:
1. Spin identities: σi·σj = 2·SWAPij − I, so the shifted/normalized isotropic bond (J σi·σj + JI)/2J IS the SWAP gate — no dilation needed (verified).
2. Commuting observables: express Hp via squared total spins (nested/disjoint subsets); Clebsch-Gordan transform gives the eigenbasis. Triangle example: H_△ = (J1/2)F² + (J2 − J1/2)L² − (3J1/8 + 3J2/2)I with L = Si+Sk, F = L+Sj; sectors (ℓ,f) ∈ {(0,½):e=−3J2/2, (1,½):e=−J1+J2/2, (1,3/2):e=(J1+J2)/2} with dims 2,2,4 (all numerically verified).
3. Coupling-matrix structure: real symmetric exchange → rotate to XYZ form, diagonal in the Bell basis.
4. Anticommuting Pauli groups: Σ cj Pj with pairwise anticommuting Pj has norm √(Σ cj²), beating the LCU value Σ|cj|.
5. Degeneracy + symmetry reduction: diagonalize symmetry blocks separately; eigenvalue ±1 endpoints are gate-free.

Triangle-level shift/normalization (branch at 2J2 vs J1): δ△ = (2J2−J1)/4, λ△ = 3J1/4 for 2J2 ≤ J1; else δ△ = (J1−2J2)/4, λ△ = (J1+4J2)/4. Middle eigenvalue ξ = (1−8r)/3 (r ≤ ½) or (4r−5)/(1+4r) (r > ½); at r = ½, ξ = −1 → A is itself a reflection = VCG† Zj Zk VCG (signal qubit omitted). Local cost T_BE,△^p = 40 + 6·Trot(ε) — the whole non-Clifford content is one logical AND + one controlled Ry.

### 4. QET normalization improvement (when the direct spectral encoding is too hard)

Given a source encoding U0p of A(0) = (Hp−δpI)/βp with λp < βp: rescale ρp = βp/λp; pick odd degree-d polynomial with |Pd(x)| ≤ 1 on [−1,1] and Pd(x) ≈ (1−s)ρp x on |x| ≤ ρp^(−1) (minimax/Chebyshev convex search). Effective local normalization λ̃p = λp/(1−s); improvement requires 0 < s < 1 − ρp^(−1). Cost: T_BE^p ≤ d★·T0p + (d★+1)·4(a−1) + Trot. Smaller s → better Λ but larger d★. Error split for QPE: ϵ_QET = r_QET·ΔE·(1−s)/K·(1/λp), remaining (1−r_QET) budget to phase estimation.

### 5. Reflection property → one call per walk step

Qubitization needs SEL² = I; ensured because every local construction is a Hermitian unitary and LCU/routing combinations of reflections remain reflections (QET: symmetric phases + real-part completion). Consequence: walk W = (2|0⟩⟨0|−I)·PREP†R†(I⊗B_ref)R·PREP uses ONE call per step (not encoding+inverse), and a CONTROLLED walk costs ≤ T_BE + 92 T gates (< 0.1% overhead: uncontrolled subcircuits cancel; signal reflection = multi-controlled Z on ≤23 signal qubits ≤ 84 T).

## Cost Model for Comparing Encodings

```
Λeff = √(Λ² − (E0 − Δ)²) = √((Emin − L)(U − Emin))    (per-site version: √(λ² − (e0 − δ)²))
N_QPE ≈ π·Λeff / (2ΔE)
Trot(ε) = 0.53·log2(1/ε) + 4.86   (repeat-until-success; ε=1e-10 → ~22.5 T)
T_QPE ≈ N_QPE · T_BE ;  time evolution: T_sim ≈ |t|·Λ·T_BE
```

## Verified Results (120×120 lattices, qubitized QPE at extensive accuracy ΔE = 0.01·J1·N)

Heisenberg J1−J2 near maximal frustration — 3×3 patch vs product-wise Pauli-LCU baseline (T-gate totals at M=120): 15.32× (r=0.4), 16.58× (r=0.5), 16.78× (r=0.6) [reproduced from Table V]. 3×3 vs triangular: 31.9%/29.8%/43.1% fewer T at M=120. Fermi-Hubbard half-filling: ~3.1× (U/t = 2,4,8). Honeycomb spin-liquid time evolution: 5×.

3×3 hierarchical patch: H3×3 = (1/4)Σ_q H_□(p+q) over the 4 overlapping subplaquettes (orbit weights c_per=1/8, c_in=c_rad=c_cyc=1/4; constraints 4c_per+2c_in=1, 2c_rad+2c_cyc=1). Exact 9-spin ED (independently reproduced to 1e-6): (δ3,λ3)/J1 = (0.176685, 2.623315) @r=0.4, (0.333576, 2.666424) @0.5, (0.470423, 2.729577) @0.6; upper edge pinned at δ3+λ3 = 2(J1+J2) (fully-polarized state) — the normalization gain comes entirely from the higher ground energy (inter-plaquette frustration). QET amplification ratio ρ3 = 2λ2/λ3 − 1.

Ground-energy operating points (σ-convention, 4× the spin-operator convention): e0 = −2.0942 (r=0.4), −1.9872 (r=0.5), −1.9092 (r=0.6). Bond-wise per-site Λeff: 5.5553/5.9139/6.2685 → N_QPE 873/929/985; triangular per-site Λeff: 2.3264/2.2475/2.9392 → 365/353/462 (all reproduced exactly).

## Recipe

1. Decompose H into translation classes of patches; weight overlaps so Σ H_p = H exactly.
2. Compute per-patch (δp, λp) from exact sector spectra (CG basis / ED / rigorous bounds); set Δ, Λ.
3. Build B_ref: try spin identities first (SWAP = free), then CG/Bell-basis spectral encodings; fall back to LCU-of-groups; apply QET if βp > λp.
4. Build the routing network for your lattice/patch (parity-split trees; fermionic fswap + parity-class JW ordering if needed); check reflection invariance to skip order correction.
5. Verify SEL² = I, then cost = 2T_PREP + T_R + T_BE^p per query; optimize (patch size, headroom s, QET degree) against total T ≈ (πΛeff/2ΔE)·T_BE.

## Verification Notes (2026-10-27 run)

All committed math numerically verified (33 checks, script verify_patchroute_20261027.py): Halmos dilation unitary+reflection+signal-block identity; SWAP bond identity; triangle sector eigenvalues/δ△/λ△/ξ vs 8×8 ED at r∈{0.4,0.5,0.6}; 3×3 (δ3,λ3) vs Table IV via independent 9-spin ED; per-site Λeff and N_QPE vs Table III; 15.3–16.9× improvement factors vs Table V. pdftotext scrambled eq (16) block layout and the T_R ceiling forms — recovered via PyMuPDF; the [[S,A],[−A,S]] reading of eq (16) is WRONG, the correct Halmos form [[A,S],[S,−A]] follows from eq (18) B = Z⊗A + X⊗S.
