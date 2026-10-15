---
name: quasistim-nonpauli-qec-simulation
description: Exact non-Pauli QEC noise simulation at Stim speed via QPD.
category: ai_collection
version: "1.0.0"
source: arXiv:2610.15975
source_title: "Scalable Exact Non-Pauli Noise Simulation for Fault-Tolerant Quantum Circuits"
authors: "Yuewen Hou, Gokul Subramanian Ravi (University of Michigan)"
published: 2026-10-11
categories: quant-ph
trigger_words:
  - non-pauli noise
  - pauli twirling approximation
  - quasiprobability decomposition
  - QEC simulation
  - stim simulator
  - coherent noise
  - thermal relaxation
  - logical error rate bias
---

# QuasiStim: Exact Non-Pauli Noise Simulation for QEC

## Overview

Stim-class stabilizer simulators only support stochastic Pauli noise, so realistic device noise (coherent over-rotation, thermal relaxation) is routinely replaced by its Pauli twirl (PTA) — fast, but biased. QuasiStim keeps the **original non-Pauli channel exact** (via quasiprobability decomposition, QPD) while restoring near-Stim throughput. Result: exact QEC simulation at QEC scale + the first systematic measurement of how much PTA biases logical error rates.

## The Two QPD Bottlenecks and Their Fixes

### Bottleneck 1: shot count ∝ Γ², Γ = ∏γᵢ (channel one-norms)
**QuasiFold** (compiler frontend) — three greedy passes, each accepted only if it leaves the QPD-weighted measurement distribution unchanged AND lowers Γ or removes a site:
1. **Coherent fusion**: rotations sharing a common-frame axis (mapped through inverse Clifford prefix P̃ᵢ = C†<ᵢ Pᵢ C<ᵢ) joined by transparent paths fuse into Θ_G = Σ sⱼθⱼ; opposing angles partially cancel → one-norm of sum < product of one-norms (submultiplicativity γ(E2∘E1) ≤ γ(E1)γ(E2))
2. **Observability pruning**: delete rotation outright if its common-frame axis commutes with every reachable measured observable, or an intervening reset removes its support — removes a Γ factor ENTIRELY (strongest rewrite)
3. **Noise folding**: absorb a Pauli-noise chunk into a neighboring site when branches cancel negative weights → combined one-norm < 1+old; useful only because cancellation beats the Pauli channel's own γ=1
- Channels represented as signed coefficient tables; compose = multiply tables, add coinciding branches BEFORE evaluating one-norm (cancellation of opposite signs is where the saving lives)
- Transparent-path tests: Cliffords always transparent; Pauli channel transparent if commuting past rotation is identity; rotations transparent if axes commute; damping needs per-BRANCH tests (channels can commute while branch pairs don't)

### Bottleneck 2: one tableau simulation per shot
**DeltaFrame** (sampling backend) — Stim's reference/frame split breaks under QPD because each branch pattern selects a different stabilizer circuit → different reference. Fix:
1. Reference basis: r₀ (all-zero pattern) + per-site offsets Δᵢ(a) = r^(i=a) ⊕ r₀ (one tableau run per site digit)
2. **Pair sweep**: test Δᵢⱼ(a,b) ≠ Δᵢ(a)⊕Δⱼ(b) → interaction edge; union-find → conflict blocks
3. Enumerate joint configurations per block exactly: r̂(p) = r₀ ⊕ ⊕_B Δ_B(p_B) — exponential cost paid per block (≤5 sites in practice; thermal relaxation = zero conflicts), not per pattern space |Ω| = ∏(1+kᵢ)
4. Batched sampling: lanes with different patterns share one circuit traversal; per-lane masks + block lookups + XOR — all O(1) Pauli-frame ops, no tableau
- Interactions are LOCAL (cut by measurement/reset layers) — that locality is what makes the whole scheme work

## Performance Results
- QuasiFold shot reduction: 1.16×–38.3× on surface/color codes; **>100× on bivariate-bicycle (BB) memory** (higher encoding rate → more instrumented gates); grows with distance (Γ is a product over sites — each removed site is multiplicative)
- DeltaFrame per-trajectory: **166×–1331× faster** than per-shot tableau on rotated surface d=5→35 under coherent R_Z; 297×–3702× under damping (damping's non-Pauli branch is a RESET → O(n²) tableau cost for baseline vs O(1) frame update for DeltaFrame)
- Flat per-gate cost in distance (frame updates touch fixed words; tableau grows O(n)–O(n²))
- Precompute overhead: O(M²) pair sweep, negligible vs million-shot runs
- Accuracy: mispredict rates orders of magnitude below LER; silent-error rate (mispredict flipping observable with no detector) lower still, decreasing with d; **exactly zero** for all thermal-relaxation benchmarks

## PTA Bias Findings (the systems lesson)
- **The gap is not a simple function of noise strength** — sign AND magnitude depend on decoder, circuit schedule, code, and Pauli/non-Pauli mix:
  - Surface memory + PyMatching: PTA systematically UNDERestimates LER, growing with coherent angle
  - BB memory: coherent crosstalk accumulates constructively at amplitude level → superlinear LER growth PTA misses entirely (twirl removes phase coherence → only probabilistic accumulation)
  - Color memory + Tesseract/BP+OSD: PTA OVERestimates (opposite sign); Tesseract ~order-of-magnitude better LER but MORE sensitive to relaxation
  - Thermal relaxation: gap grows as noise WEAKENS (counterintuitive)
  - Magic-state cultivation: gap largest at low background noise, ~6× at lowest setting; grows with attempts-per-kept-shot (post-selection makes correlated error paths matter more)
  - Logical S gate (lattice surgery): twirling error is NOT uniform — merge segment worst, pre-rounds next, boundary rounds ≈ exact; per-segment gaps roughly multiply
- Conclusion for FTQC design: twirling accuracy cannot be predicted in advance → exact simulation is a systems requirement, not a nicety. Biased gadget error rates get extrapolated across distances and composed into resource estimates

## Noise Models Used
- Coherent: RZZ after every 2-qubit gate (Zhou et al. crosstalk) or RZ on idling qubits (trapped-ion laser control); twirl prob p_Z = sin²(θ/2)
- Thermal relaxation: sweep τ/T₁ (T₁=T₂); decomposition positive when T₂≤T₁ (no extra shots), non-Pauli branch = reset
- Defect-qubit model for high-d benchmarks (compute-budget artifact, not method limit): instrument only gates touching selected defective data qubits

## Activation

Use when: QEC decoder/protocol evaluation under realistic noise, questioning whether Pauli twirling is safe for a resource estimate, designing QPD-based simulators, compiling noisy circuits for shot-count reduction, or benchmarking logical operations (lattice surgery) and magic-state cultivation under coherent noise.

## Pitfalls
- Γ multiplies over ALL noise sites — unrestricted per-gate instrumentation at high distance can exceed any compute budget; segment-wise exactness (twirl the rest, exact one segment, multiply per-segment gaps) is the practical workaround
- DeltaFrame Eq.(4) not universally exact: >pairwise interactions and cross-block interactions escape the pair sweep — always measure mispredict rate against direct tableau on your circuit
- Pairwise site sweep is O(M²) — fine for QEC circuits, the cost that matters is block enumeration
- Clifft exact cross-check only available at low distance (memory footprint)
- Leakage and qubit-loss channels out of scope (future work) — use PPVM-class loss modeling for those
