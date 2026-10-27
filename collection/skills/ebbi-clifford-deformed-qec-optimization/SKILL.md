---
name: ebbi-clifford-deformed-qec-optimization
description: Shot-efficient best-arm search for Clifford-deformed QEC codes.
category: ai_collection
---

# EBBI: Evolution-Based Best-arm Identification for Clifford-Deformed QEC Codes

> From "Decoder- and Noise-Aware Optimization Framework for Clifford-Deformed Quantum Error-Correcting Codes" (arXiv:2610.13589, Bønnelykke, Joecker, Krogstrup, Michal, Svendsen — Microsoft Quantum / Univ. Copenhagen, Oct 2026). Use when: optimizing Pauli-stabilizer QEC codes under biased circuit-level noise, searching exponentially large Clifford-deformation spaces, tailoring codes to hardware noise characteristics, or applying best-arm identification to combinatorial search with correlated neighbors.

## Core Insight

Clifford deformations (CDs) modify a QEC code's stabilizers — without changing code distance or connectivity — to lower logical error rate P_L at zero added hardware cost. But the CD space grows as |A|^n (6^n per-qubit deformations, reducible to 3^n under noise symmetry): exhaustive search is infeasible beyond trivial codes, and the optimal CD depends strongly on BOTH the noise model AND the decoder.

**Neighboring CDs are correlated** (Pearson ρ = 0.83 for single-qubit-deformation neighbors at distance 3, and ρ increases with code distance): small changes to a CD pattern produce similar P_L. This structure lets information from one simulation guide search toward promising regions — the key to shot efficiency.

## The Two Views of a Deformation

- **Heisenberg picture**: deformation U on data qubit maps stabilizer S → S′ = U S U†.
- **Schrödinger picture** (code-capacity/phenomenological only): stabilizers unchanged, per-qubit noise permuted. H gives (pZ, pY, pX). ⚠️ This view **breaks down under circuit-level noise** — compiled single-qubit gates transform Z-errors into X/Y errors (Appendix C/D of paper); the 6→3 reduction still holds but must be re-derived, not assumed.

The six single-qubit deformations: I, H, √Z, H√Z, √ZH, H√ZH (with A₆ full set; under pX = pY symmetry pairs merge: I ~ √Z, H ~ √ZH, H√ZH ~ H√Z, giving A₃ = {I, H, H√ZH}, 3^n space).

## EBBI Algorithm (three steps)

Treats circuit + noise model + decoder as a **black box** (works even with ML decoders whose internals are unknown).

### 1. Initialization
- Uniformly sample K random CDs from A^n.
- Warm up each: simulate until **W logical faults observed**.
- Model each CD's true P_L as a **Beta posterior**: α = #LogicalFaults + 1, β = #SuccessfulDecodings + 1.

### 2. Sampling (uncertainty reduction)
- Pick the candidate with the **largest posterior standard deviation** (most uncertain).
- Resample until its σ shrinks by factor 1.5 → needs S·(1.5² − 1) = **1.25S additional shots** (S = α + β − 2 shots already used). The 1.5 factor is tunable: too small → sampling churn; too large → wasted shots on later-pruned candidates.

### 3. Prune and re-populate
- Prune CD_k if its γ-quantile lower bound exceeds the (1−γ)-quantile upper bound of any other CD:
  `F⁻¹_Beta(αk,βk)(γ) > min_{j≠k} F⁻¹_Beta(αj,βj)(1 − γ)`
- γ = 2.5% (non-overlap of central 95% credible regions). Too small γ wastes shots; too large risks pruning good candidates.
- **Mutation-based repopulation**: identify CDbest by drawing one sample from each surviving posterior and taking the lowest (Thompson-sampling style). New candidate: per qubit, copy CDbest's deformation with probability 1−M, else pick uniformly from A. If the mutation already exists, increase M by 1% until unseen; if M > 1, continue with K−1 candidates.
- New candidate gets the same warmup; return to sampling step.
- **Termination**: return the CD minimizing **μ + σ** (mean + std), not min(μ) — biases toward well-estimated candidates and substantially reduces false positives.

## Results

- Rotated surface code, two strongly Z-biased circuit-level noise models (HBD + HBD-SI1000), PyMatching decoder, Stim simulation.
- Distance 3: EBBI finds optimal CD with up to **~1100× fewer shots** than random search.
- Distance 5 at target error rate: median EBBI run converges to optimal CDs; **random search never converges**.
- **B-XZZX discovery**: under Z-biased SI1000-like noise, EBBI found a new code differing from XZZX on only O(d⁻¹) of qubits, whose relative advantage *grows* with distance: ~5% at d=3 → ~12% at d=11. Low-distance discoveries scale systematically to large distances.
- P_L estimation trick: simulate/decode the same circuit in X- and Z-basis under the same noise seed (identical error locations) — comparison reveals which logical Pauli error occurred (P_LI, P_LX, P_LY, P_LZ); P_L = P_LX + P_LY + P_LZ. One "shot" = two seeded runs.

## Reusable Patterns

1. **Beta-posterior best-arm identification with warmup-to-faults**: model each candidate's success rate as Beta(α, β), warm up until W failures observed rather than fixed shots — adapts shot spend to candidate quality.
2. **Prune-by-credible-region-overlap**: prune when one candidate's lower γ-quantile exceeds another's upper (1−γ)-quantile — statistically principled elimination.
3. **Neighbor-correlation mutation**: when single-coordinate changes produce similar objective values (true for many combinatorial landscapes), repopulate pruned arms by mutating the current best rather than uniform sampling.
4. **Black-box decodability**: no assumptions on decoder internals — only requires simulate→decode→observe outcomes; applies to ML decoders, hardware-in-the-loop, or any expensive noisy evaluation.
5. **min(μ+σ) selection** at termination: robustness against under-sampled false positives.
6. **Symmetry reduction before search**: noise-model symmetry (pX = pY) merges deformation classes 6→3; always check before brute-force enumeration. But re-verify symmetry claims under the actual noise regime (circuit-level ≠ code-capacity).
