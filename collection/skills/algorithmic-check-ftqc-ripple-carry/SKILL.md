---
name: algorithmic-check-ftqc-ripple-carry
description: FTQC below-threshold execution using algorithmic checks. Trigger: EFTQC, fault-tolerant arithmetic.
category: ai_collection
---

# Algorithmic-Check FTQC: Below-Threshold Ripple-Carry Addition

**Source**: Nelson, Landahl, Baczewski (Sandia/UNM), "Below-threshold execution of fault-tolerant ripple-carry addition on a trapped-ion quantum computer" (arXiv:2610.14202, Oct 2026). Deployed on Quantinuum Helios-1 (98-qubit trapped-ion).

## Core Result

Logical 1-bit adder failure rate **(6.0±5.9)×10⁻⁵** vs physical **(3.5±1.3)×10⁻³** — >50× below-threshold improvement, using distance-2 error-detecting codes ONLY, achieved by co-designing the algorithm's own "gauge" qubit into the error-detection stack. Logical beats physical through m=3; m=4–5 sit just above threshold.

## Methodology Patterns

### 1. Algorithmic Check (AC) — free error detection from algorithm invariants
The Cuccaro ripple-carry adder seeds computation with carry qubit c₀=|0⟩, which the algorithm MUST restore to |0⟩ at the end (uncomputation). Measuring c₀ is an **algorithm-level check independent of any QEC code**:
- Any single logical-Z error between the H–CCZ–H pair conjugates to logical-X, flips outputs, AND propagates to c₀ → detected.
- Effective fault distance at those locations: **2 → 4** (three-qubit errors detectable) with distance-2 codes.
- **Rule**: reversible algorithms with ancillas that must uncompute to a known state carry a free post-selection resource — never optimize it away (Takahashi's "improved" adder removing c₀ destroys this).

### 2. Distance-asymmetry co-design
[[8,3,2]] code: distance 2 overall but **X-distance 4**. Terminating measurements are all Z-basis → only logical-X errors flip outcomes → X-distance governs output failures. Logical-Z errors either stay harmless or get conjugated to X by H pairs and land on the AC qubit.
- **Rule**: match measurement basis to the code's asymmetric distance; route the harmful error sector into an algorithm-level detector.

### 3. Transversal code-switching for universality
- [[8,3,2]] ("smallest interesting colour code"): logical CCZ via transversal T/T†.
- [[4,2,2]] ("iceberg"): logical (H⊗H)SWAP via transversal H.
- Universality from CCZ + H + prep/measure. Both codes are "phantom codes": intra-block CNOT = passive physical relabeling (free).
- Toffoli = H–CCZ–H with 3 teleportations between code blocks; teleportation is the **performance-limiting primitive**.

### 4. Proxy Clifford simulation for implementation selection
Replace each transversal CCZ with 2×CZ → circuit becomes Clifford → classically simulable on the hardware emulator (Helios-1E with Quantinuum's noise model). Iterate among functionally equivalent implementations (qubit reuse, prep/measurement scheduling) cheaply, then run only the winner on hardware. Note: vendor compilers are sensitive to program expression — simulate several equivalent programs, keep the best performer.

### 5. Burst-error job filtering
Track per-circuit-layer survival rates per job (~10³–10⁴ shots each). Jobs whose survival decays far faster than same-circuit siblings = burst errors (atypical hardware operation). Discard ENTIRE jobs (not individual shots) and report failure rates both with and without flagged jobs. Failure counts per m: keep submitting until ≥3 failures observed.

### 6. Syndrome-extraction scheduling tradeoff
NO active syndrome extraction on idling logical qubits: O(m²) logical identities go unchecked, raising effective physical error rate — deliberate trade because (a) each extra check multiplies post-selection yield loss exponentially, (b) hardware lacks parallel syndrome extraction across code blocks; serial extraction would cascade idle steps. Post-selection rate: ~60% at m=1 → ~1% at m=5 (yield, not qubit count, is the binding constraint).

### 7. Three-level resource accounting
| Level | Qubits | Key ops |
|---|---|---|
| Algorithmic | 2m+2 | m Toffolis, 2m+2 CNOTs |
| Logical | 3m+4 | 8m−2 teleportations, 6m+1 transversal gates, 2m MX |
| Physical (guppy) | ≥8m+10 | 120m−33 1Q gates, 56m−12 measurements |

Always report all three — architectural overheads live in the logical→physical gap.

## Failure-Analysis Honesty Notes
- m=4 encoded runs slightly WORSE than physical: attributed to unchecked O(m²) idling identities.
- m=5 defied extrapolation from m=1–4; reproduced across days/inputs; no complete theory — reported as-is.
- Classical-input-only results: on-demand state prep and early measurement (V-shaped schedule, 4-qubit teleportation buffer reuse) exploit this; quantum-superposition inputs would force different choices. They deliberately did NOT verify input a bits round-trip (would inflate performance unfairly vs quantum-input use).

## Transferable Checklist (for any EFTQC algorithm deployment)
1. Identify algorithm invariants (uncomputed ancillas, conserved registers) → algorithmic checks.
2. Check code distance asymmetry vs terminating measurement basis.
3. Build proxy Clifford circuits → emulator-driven implementation selection.
4. Schedule syndrome extraction against post-selection yield, not error rate alone.
5. Track job-level survival curves for burst-error filtering.
6. Count resources at algorithmic/logical/physical levels.
7. Co-design algorithm variant and architecture together (the paper's closing thesis).

## Related Skills
- `fault-counting-logical-sensitivity` — QEC sensitivity analysis
- `quantum-ordinal-optimization-fixed-budget` — same-day quantum/SE crossover
- `entanglement-capability-circuit-cutting` — distributed QC resource constraints
