---
name: nest-qldpc-spin-shuttling
description: Use when co-designing qLDPC with spin shuttling tracks.
category: ai_collection
arxiv_id: "2610.28538"
---

# NeST — Nested Shuttling Tracks: qLDPC Codes Co-Designed with Silicon Spin Qubits

**Source**: arXiv:2610.28538 (Siegel, Quantum Motion, Oct 2026). First code + spin-qubit
hardware co-design for ultra-high-rate qLDPC codes. All formulas below re-derived and
numerically verified in-session (group law, action formulas, shuttling budget arithmetic).

## Core Design Principle (the reusable idea)

Do NOT take an existing code and ask how to route its permutations through a track
network (that pays for generality in routing depth — the CABLECAR trap). Instead: **ask
which groups a track network can route for free, and build the code from those groups.**

A looped conveyor belt advances every qubit it carries by the same number of sites under
one global control signal → one loop implements multiplication in a cyclic group, with
control cost independent of loop length. Nest loops-within-loops → product of p cyclic
groups. Non-abelianness (needed to bypass distance caps) is FREE: the inversion r→r⁻¹ is
realised by the direction a qubit train enters its destination loop.

## The Implementable Group Family G(n⃗,σ)

Product of p cyclic groups with pairwise commutation-or-inversion relations:

```
G(n⃗,σ) = ⟨r1..rp | ri^ni = 1, ri rj ri⁻¹ = rj^σij⟩,  σij ∈ {+1,−1}, σij = −1 ⇒ ni even
```

- Contains EVERY finite abelian group (σ≡+1 ⇒ direct product) → all quasi-cyclic lifted
  products implementable, incl. 30%-rate distance-24 codes.
- Two-tier case G = Cn1 ⋊₋₁ Cn2, elements rⁱsʲ, law (i,j)·(k,l) = (i+(−1)^j k, j+l) (mod n1,n2):
  - LEFT action:  L(rⁱsʲ) rᵏsˡ = r^{i+(−1)^j k} s^{j+l}  → odd j ⇒ index reflection rᵏ→r⁻ᵏ
  - RIGHT action: R(rⁱsʲ) rᵏsˡ = r^{k+(−1)^l i} s^{j+l}  → l-dependence only sets loop spin direction
  - srs⁻¹ = r⁻¹ verified; n2=2 gives dihedral D2n natively (rotations + reflections).

## Hardware Mapping Rules (NeST layout)

- Square lattice of shuttling tracks, edge ℓe ≈ 1 µm, qubit pitch ℓqq = 4ℓe/n1; speed v=50 m/s.
- Tier-1 loops host n1 STATIC data qubits; ancillas ride the belts (CZ-only ⇒ shuttling
  dephasing stays Z-like, cannot spread to data through CZ).
- **Mode A/B chequerboard**: same-mode loops share relative rotation direction (collective
  control); different-mode loops co- or counter-rotate depending on left/right action.
- Tier-2 motion: ancillas exit a loop as a train in lockstep, wrap the destination loop;
  entry along the data ordering = rotation, entry opposite = reflection. Tier-2 arrival
  adds a quarter-loop tier-1 rotation for rotations (zero for reflections) — corner vs
  middle loop labelling differs; the labelling is what makes all motions synchronous.
- Buffer: 3 empty loops between hosting loops prevents train collisions (a 4× denser
  zigzag layout exists, Appendix B, at the price of scheduling complexity).
- p tiers: tier-k cells in a 2×(nk/2) array; reflections at tier k = row-swap of tier-(k−1)
  cells; device width ~ ℓqq|G|/2^{p−1} — per-move shuttling shrinks EXPONENTIALLY in tiers.

## Shuttling Budget (Eq 16, arithmetic verified exactly)

Worst-case 2-tier per-cycle distance: L ≤ ℓqq·(n1/4)·(2n2+5), dominated by n1n2ℓqq/2.
Mitten-code total (9 interactions + 3 inter-cell switches, n = 5|G|, w = 9):

```
L ≈ 9·ℓqq|G|/2^{p−1} + 3·ℓqq|G|/2^{p−2} = n·w·ℓqq / (3·2^{p−1})
```

Prefactor 1/(3·2^{p−1}) < 1 ⇒ inside the guideline budget n·w·ℓqq. Verified: the two-term
sum equals nwℓqq/(3·2^{p−1}) EXACTLY for all p, |G| (pdftotext had displaced the fraction —
re-derived from the two-term estimate).

## Mitten Codes on NeST (rate 20%)

A, B both 1×2 weight-3 ⇒ n = 5|G|, k = |G| (rate 1/5), check weight w = 9, five blocks
(4 left corners + 1 right centre) = five unit cells laid out as the protograph.

| [[n,k,d]] | Group (as G(n⃗,σ)) | dcirc | SE cycle |
|---|---|---|---|
| [[150,30,10]] | C3⋊C10 | ≤8 | 16.4 µs |
| [[200,40,12]] | C5×(C4⋊C2) | ≤10 | 17.5 µs |
| [[300,60,14]] | C6⋊C10 | ≤13 | 20.7 µs |
| [[480,96,≤16]] | (C3×C4)⋊C4⋊C2 | ≤15 | 26.1 µs |
| [[600,120,≤18]] | C5⋊C6⋊C4 | ≤17 | 29.3 µs |
| [[700,140,≤20]] | C7⋊C10⋊C2 | ≤20 | 30.1 µs |
| [[1400,280,≤28]] | C7⋊C10⋊C4 | — | ≈42 µs (est.) |

dcirc achieved with 3 inter-cell switches (2 switches degrade distance except
[[480]] which reaches dcirc=d−1 with the minimum 2). Timings: 200 ns CZ, 500 ns H,
1 µs meas, v=50 m/s.

## Noise Model & Idling Trick

- Uniform depolarising p on gates/meas (hardware-agnostic, CONSERVATIVE — a
  g-factor-specific model scores better at equal infidelity).
- Shuttling: dephasing psh × L per µm. Ancilla idle: pidle = ½(1−e^{−(t/T2*)²}), T2* = 20 µs.
- Data idling is Hahn-echoed: Rz(θ)·X·Rz(θ) = X, and since Rz commutes with CZ all waits
  between two Hadamards collapse to ONE accumulated rotation — X-then-Z (non-interleaved)
  circuit + CZ gates leaves each data qubit just TWO echo windows per cycle ⇒ data idle
  error reduces to pHahn = p (twice per cycle).
- Decoder: telescoping BP → Tesseract fallback (replaces Gurobi); at p=0.1% only ≤0.07%
  of shots reach the last stage.

## Headline Results

- Threshold > p = 0.1% for all shuttling assumptions up to psh = p/20 (≈10× better than
  the 99.95%/µm demonstrated; psh=p/2 at state-of-art). Mitten codes match/beat
  same-distance surface codes (which get NO shuttling noise in the comparison).
- Extrapolation (fit y = a·p^{dcirc/2}, conservative): distance-27 mitten ⇒ 1e-14 per
  logical per round at p=0.1%, psh=p/20. Cost: 9 physical per logical INCLUDING the
  4 ancilla check-blocks (5|G| data + 4|G| ancilla)/|G| = 9 — the bare n/k ratio is 5;
  surface code at comparable error needs 1457.
- Sub-50 µs stabiliser cycles — 2-3 orders of magnitude faster than neutral-atom qLDPC.

## Logic: NeST-Compatible Surgery Gadget

Graph-surgery for measuring logical X̄ (support S): vertex checks V (new X stabiliser per
 data qubit in S; their product holds X̄), edge ancillas E (init |0⟩, meas Z — randomise
 vertex checks, act as gadget data), cycle checks C (Z checks on E, gauge out extra DOFs).
Merged code: H_X^merged = [H_X; V E-block], H_Z^merged = [H_Z; C; Γᵀ-block] (Eq 19).
Gadget must be a good expander (Cheeger constant) for distance preservation. For
[[150,30,10]]: same qubit count as the unconstrained gadget, distance preserved,
+29% gate layers, every motion still a rigid belt motion.

## Reuse Patterns

1. **Geometry-mirrors-group co-design**: pick hardware-native group families first; the
   block structure of lifted codes (left sector = L(·) blocks, right = R(·) blocks) then
   maps unit cells onto the protograph layout, with inter-cell highways for A/B-mandated
   long-range links.
2. **Entry-direction duality**: same-direction entry = rotation, opposite = reflection —
   gives non-abelian actions at zero control cost.
3. **Mode A/B collective control**: partition loops so one global signal drives many.
4. **Generator decomposition with cancellation**: decompose transition x → hL x hR into
   tier generators, but search products of ≤3 collective motions for shortcuts (e.g. in
   C3⋊C10: s²·x·s² = x·s⁻² — shift 2 loops backward instead of 4 forward twice).
5. **Route planner hybrid**: tier-generator routes vs group-agnostic single-move planner;
   keep shortest mean per-ancilla distance; init/meas stations at every cell edge.

## Pitfalls

- n2 (and all ni for i≥2) must be EVEN (2×(ni/2) array layout); representation with
  coprime merging (Cp×Cq ≅ Cpq) gives optimisation freedom — choose (n⃗,σ) per code.
- pdftotext corrupts Eq(16)-(20) superscripts (fraction displacement, dropped ½/ν
  factors). Re-derive; this skill's formulas are the verified forms.
- Depolarising noise is the pessimistic baseline — platform-specific models can only
  improve the numbers, but keep it for cross-platform comparability.
- Ancilla trains collide if hosting loops are <3 empty loops apart (or use the zigzag
  compact layout with more intricate scheduling).
