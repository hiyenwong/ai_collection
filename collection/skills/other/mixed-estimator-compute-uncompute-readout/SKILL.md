---
name: mixed-estimator-compute-uncompute-readout
description: Use when reading eigenvalues off prepared quantum states.
trigger: mixed estimator, compute-uncompute, vacuum test, sparse multiconfiguration reference, magnitude-only overlap, flagged compute-uncompute FCU, real Hadamard test, swap test 1/h2 penalty, classical shadows amplitude reconstruction, shot budget NISQ, measurement-efficient energy estimation, correlation energy readout, residual state overlap, reference size tradeoff, QSCI SQD reference support, photodynamic therapy quantum chemistry, radiodynamic therapy, Ru MOF excited state, MLCT MC state ordering, singlet oxygen generation rate, Marcus activation energy, trapped-ion energy validation, leakage detection postselection, parity check ratio design, direct expectation value vs overlap measurement
author: engineering-lion5
category: ai_collection
version: 1.0
license: MIT
related_skills: svd-thc-molecular-ensemble-block-encoding, qumvqd-quantum-chemistry, qsci-rbm-quantum-chemistry, ml-qem-variational-algorithms, shot-based-quantum-encoding
---

# Mixed Estimator + Compute-Uncompute: Measurement-Efficient Energy Readout

**Source**: arXiv 2610.26689 (Lenihan, Panchagnula, Erhart, Guhit, Gaggioli, Greene-Diniz, Laude, Rowe, Finger, Kalidindi, Rinaldi, Muuronen, Mulakala, Soini, Shishenina, Muñoz Ramo, Manrique — Quantinuum × Johnson & Johnson; 19 Oct 2026). Demonstrated on the H₂DBB–Ru model from a Ru-functionalized Hf–DBB–Ru metal–organic framework relevant to **photodynamic/radiodynamic cancer therapy**, validated on Quantinuum Helios trapped-ion hardware up to (10,10) active spaces incl. a 50-qubit circuit with AI-assisted state preparation and error detection. Extends the single-determinant/classical-shadow mixed estimator of Lenihan et al. (ref 23) to sparse multiconfiguration references + magnitude-only compute–uncompute, cutting the shot requirement by ~100× vs single-determinant CS and ~1700× vs grouped Pauli averaging.

## When to Use

- NISQ/early-FT energy readout where **direct Hamiltonian-term sampling (grouped Pauli averaging) is the bottleneck** — the state is preparable but mHa-precision readout needs millions of shots.
- You have a classical reference |Φ⟩ (selected-CI/SHCI truncation, CASCI subspace state, or a QSCI/SQD-sampled determinant subspace — the sampled subspace is directly usable as the ME reference).
- Target is the lowest state in the reference's symmetry sector (the magnitude-only sign trick needs the variational principle; excited states need phase reconstruction).
- You need **energy differences** between related systems/geometries (Marcus activation energies, reaction barriers, ΔE between geometries) where correlated readout noise can cancel.
- Any "eigenvalue off a prepared state" problem where operator-term measurement variance dominates — the classical-reference-projection pattern is chemistry-agnostic.

## Core Decomposition

E_ME = ⟨Ψ|H|Φ⟩/⟨Ψ|Φ⟩ = E_Φ + r_Φ·(h/s)  — exact when |Ψ⟩ is an eigenstate (non-variational; verified to machine precision on toy models)

- **Classical part** (all known exactly from H acting on the sparse expansion): E_Φ = ⟨Φ|H|Φ⟩ (reference energy), r_Φ = ‖Q_ΦH|Φ⟩‖ (residual norm), |Λ⟩ = Q_ΦH|Φ⟩/r_Φ (normalized residual state, ⟨Φ|Λ⟩=0)
- **Quantum part**: only two overlaps — h = ⟨Ψ|Λ⟩, s = ⟨Ψ|Φ⟩. h,s are complex in general but their **relative phase cancels** (the correction r_Φ·h/s is real).
- **Sign fix (Eq 4)**: for the lowest eigenstate in |Φ⟩'s symmetry sector, E_ME − E_Φ = r_Φ·h/s ≤ 0 → magnitude-only measurements suffice; no phase estimation, no Hadamard-test sign.
- Orthogonality of {Φ, Λ} gives h² + s² ≤ 1 (the overlaps are projections onto an orthonormal 2-frame).

## Compute–Uncompute (Vacuum Test) Protocol

Prepare U_Ψ|0⟩, apply U_Ω† (Ω ∈ {Φ, Λ}), measure all-zero: **p_Ω = |⟨Ψ|Ω⟩|²** (Eq 6). One system register, no ancilla, no controlled target preparation. Then

E_ME = E_Φ − r_Φ·√(p_Λ/p_Φ)  (Eq 7)

**Shot ladder** (target standard error ε, high-quality-reference regime s→1, |h|≪|s|):

| Protocol | Shots N | Factor vs CU | Notes |
|---|---|---|---|
| CU / FCU | (1/4)(r_Φ/ε)² | 1× | σ = r_Φ/(2√N) — MC-verified within 0.6–3% |
| RHT / RIST | (r_Φ/ε)² | 4× | signed overlap Re⟨Ψ|Ω⟩; σ ratio √4 = 2 (MC 2.01) |
| CS (global Clifford) | 3(r_Φ/ε)² | 12× | amplitude reconstruction, per-amplitude var ~3/N (MC ~14× crude) |
| SST / DST | (1/4h²)(r_Φ/ε)² | 4× + 1/h² | swap tests statistically unfavourable as residual overlap shrinks |

**FCU (flagged compute-uncompute, introduced here)**: one flag qubit projects |Ψ⟩ onto |Φ⟩ first; flag event → p_Φ = |s|², disjoint all-zero unflagged event → p_Λ = |h|² from the SAME shots. Covariance-accounted variance ≤ optimally allocated separate CU. Costs circuit depth (reference restoration + flag); runtime win via **mid-circuit early termination** when τ_Φ + τ_flag < τ_Λ (flagged shots exit before residual uncomputation).

**CS vs CU trade**: one classical-shadow dataset contracts against MANY references/observables (free m-scans, reusable); CU wins for a few precise targeted energies (sub-1σ at equal submitted shots). Choose by how many readouts you need from one dataset.

## Reference-Quality Law (the compounding effect)

The quantum correction magnitude is |E_ME − E_Φ| = r_Φ·|h|/s. Growing the reference (m determinants, |Φ_m⟩ = lowest eigenstate within the m largest-amplitude determinants) shrinks **both factors simultaneously** (verified monotone): r_Φ↓ AND |h|/s↓. Reference improvement and protocol efficiency **compound multiplicatively** — m=1→8 with CU: 40,000 → ~400 shots to 1.6 mHa (100×); vs grouped PA baseline ~1700×. PA needs 2.5–3.8M shots/geometry at (10,10) for the same precision; Helios CU reached 1.66–1.73 mHa std with 10k submitted shots.

- **(m, k, l) notation**: reference determinants m / residual truncation k / target size l (tUPS layers or sMCS determinants). The three sizes are coupled; optimize jointly.
- **Residual truncation bound (Eq 5, conservative)**: r_Φm·‖|Λm,k⟩ − |Λm⟩‖/|s_m,l| < ε guarantees truncation-induced error < ε (worst-case alignment of discarded determinants; verified bound ≥ actual error on toy models).
- Larger m deepens |Φ⟩/|Λ⟩ circuits (residual worst-case support scales O(mn⁴) over n spin orbitals) — shot savings trade against circuit synthesis. AI-assisted truncation + circuit optimization used resource metric **2G(Ψ_l) + G(Λ_1,k)** (G = compiled ZZPhase gate count) with energy-accuracy and spin-symmetry constraints; cut combined ZZPhase 857→755 (~12%).
- ME tolerates approximate targets (pp-tUPS, sMCS): reaches a given accuracy with **simpler state prep than direct expectation-value estimation** — e.g. (10,10) chemical accuracy at 27/23 determinants (224/159 two-qubit gates) vs 96/100+ determinants (>1600 gates) for direct readout.

## Error Structure & Hardware Practice

- **Two conditional cancellations** (design for them): (1) similar relative errors in p_Φ and p_Λ cancel in the ratio √(p_Λ/p_Φ); (2) similar errors at two geometries cancel in ΔE = E_Rx − E_R0. Matched-circuit pairs (same reference sizes, same shot allocations) maximize both.
- **Parity checks (CPC/MBPC) did NOT consistently improve ΔE**: even when an individual overlap improved, unequal changes in p_Φ vs p_Λ could WORSEN the ratio or hit the two geometries differently. → optimize error detection for the **overlap ratio**, not either circuit separately.
- Ternary **leakage detection + postselection** retained ~78–86% of shots on the 50-qubit AI-selected sMCS circuits on Helios-1.
- Hardware absolute deviations from CASCI spanned 0.5–13 mHa (individual energies) / 0.2–9 mHa (differences) — finite-shot precision ≠ central-value accuracy; report both.

## Application: PDT/RDT Materials (Medicine)

- Photodynamic/radiodynamic therapy = spatially controlled, minimally invasive cancer treatment via sensitized reactive-oxygen-species production; MOF photosensitizers tunable modularly.
- H₂DBB–Ru model reproduces the full MOF's absorption/phosphorescence; different DFAs predict singlet-O₂ generation rates spanning **>5 orders of magnitude** (qualitative MLCT/MC state-ordering flips) — the correlated quantum readout targets ΔE_Rx−R0, the dominant Marcus-activation-energy term entering rates exponentially.
- CASCI benchmarks with SHCISCF natural orbitals: ΔE_Rx−R0 ≈ −6.3 mHa at (6,6)/(8,8), +0.1 mHa at (10,10) (NEVPT2 shifts to +35–47 mHa) — AS-size sensitivity is itself a benchmark-design lesson.
- (N_α,N_β) = (4,2)/(5,3)/(6,4) triplet-sector targeting; R0 = ³MLCT (Ru d + ligand π*), Rx = ³MC (t₂g/e_g) — state character read off the active orbitals.

## Reusable Pattern (beyond chemistry)

"**Classical reference + quantum overlaps**" readout: when eigenvalue/property extraction from a prepared quantum state is shot-limited, (1) project onto classically-known states instead of sampling operator terms; (2) exploit known sign structure (variational principle) to drop phase estimation entirely; (3) improve classical reference and measurement protocol **together** — their savings multiply; (4) shape error mitigation around the final ratio/difference, not per-circuit estimates. The same structure applies to QSCI/SQD energy extraction, shadow-based property estimation, and any two-overlap nonlinear readout.

## Numerical Verification (this session, 16-determinant toy model)

- V1 exactness: E_ME reproduces exact eigenvalue at machine precision (m=1..8) ✓
- V2 sign: h/s ≤ 0 for ground state ✓ V3 orthogonality: h²+s² ≤ 1 ✓
- V4 CU scaling: MC σ matches r_Φ/(2√N) within 0.6–2.8% at N=500–8000 ✓
- V5 protocol ladder: RHT σ-ratio 2.01 (√4 shots), CS σ-ratio ~3.7–3.8 (≈√12–14 shots) ✓
- V6 truncation bound: r_Φ‖Λ_k−Λ‖/|s| ≥ actual ME shift error at k=2/4/6 (conservative) ✓
- V7 compounding: r_Φ and |h|/s both monotone ↓ in m; |E_ME−E_Φ| 0.275→0.043 (m=1→8) ✓

## Activation

mixed estimator, compute-uncompute, vacuum test, sparse multiconfiguration reference, magnitude-only overlap, FCU, classical shadows, shot budget, measurement-efficient, correlation energy readout, NISQ energy estimation, QSCI/SQD reference, photodynamic/radiodynamic therapy quantum chemistry
