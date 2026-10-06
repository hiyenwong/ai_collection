---
name: adaptive-single-copy-stabilizer-learning
description: Adaptive single-copy learning of stabilizer states in Θ(n).
category: ai_collection
trigger_words: [stabilizer learning, stabilizer testing, single-copy measurements, adaptive measurements, Bell sampling, Bell difference sampling, Clifford measurements, stabilizer nullity, T-doped states, sample complexity]
source: arXiv:2610.02031
source_title: "Adaptivity is all you need: Optimal stabilizer learning using just single-copy measurements"
authors: Lennart Bittel, Jens Eisert, Weiyuan Gong, Antonio Anna Mele, Louis Schatzki
published: 2026-10-01
arxiv_categories: [quant-ph]
---

# Adaptive Single-Copy Stabilizer Learning

## Overview

Methodology from arXiv:2610.02031 (Bittel, Eisert, Gong, Mele, Schatzki — FU Berlin/Harvard/IBM, Oct 2026). Closes the adaptivity gap in stabilizer-state learning: an n-qubit stabilizer state needs Θ(n) copies via two-copy Bell sampling (Montanaro) but Ω(n²) copies via NON-adaptive single-copy measurements. This paper shows **adaptive single-copy Clifford measurements achieve Θ(n)** — classical feedback alone matches Bell sampling with no coherent multi-copy access.

## Core Results

1. **Algorithm 1 (exact learning)**: Learns any pure n-qubit stabilizer state with probability ≥ 1−δ in poly time, using N = O(n + log(1/δ)) copies, T = 2n + O(√(n log(1/δ)) + log(1/δ)) rounds, O(nT²) classical time. Optimal up to constants even against collective measurements.
2. **Tolerant tester**: Same ideas give a sample-optimal single-copy tolerant tester for stabilizer fidelity F_stab.
3. **Memory-bounded tradeoff (Algorithm 2)**: With k qubits of quantum memory, optimal testing cost Θ(n − k + 1/ε) at infidelity ε — partial Bell difference sampling interpolates between single-copy (k=0) and full Bell sampling (k=n).
4. **Beyond stabilizers (nullity extension)**: Pure states with stabilizer nullity ≤ r (incl. t-T-doped Clifford circuits, nullity ≤ 2t) are learnable with O(n·2^r) single-copy measurements at constant accuracy — improves prior t-doped bounds.

## Methodology

### The Adaptive Compression Loop (Algorithm 1)

Goal: build Clifford C with C|ψ⟩ = |z⟩ (computational basis state), then read off z and return |ψ⟩ = C†|z⟩.

Key object: D(ϕ) = {s : (0,s) ∈ L_ψ} — the Z-type (diagonal) stabilizer subspace of the current transformed state ϕ = C|ψ⟩; ℓ = dim D. State is computational-basis iff D = F₂ⁿ. The loop monotonically grows ℓ (never decreases) until ℓ = n:

```
C ← I
for t = 1..T:
  1. Measure TWO copies of C|ψ⟩ separately in computational basis → x, y   # single-copy ops, no joint measurement
  2. u ← x + y (XOR)                       # computational difference sampling
     # u is uniform over D(ϕ)⊥ = X-projection of stabilizer space; if (u,v) is a
     # stabilizer label for some v, u ≠ 0 gives a handle to diagonalize one more generator
  3. if u = 0: continue                    # happens with prob 2^−(n−ℓ)
  4. i ← first index with u_i = 1 (pivot)
     C ← F_u · C   where F_u = ∏_{j≠i, u_j=1} CNOT_{i→j}   # maps (u,v) → (e_i, v′);
     # pivot qubit i is now untouched by ALL pre-existing diagonal stabilizers
     # (their labels get s′_i = ⟨u,s⟩ = 0 since u ⊥ D)
  5. Draw uniform bit b; C ← H_i·S_i^b·C   # (e_i,v′) acts as X_i or Y_i on qubit i;
     # one of {H_i, H_i S_i} maps it to Z-type — random guess succeeds w.p. 1/2
  6. ℓ ← ℓ + 1 on success; pre-existing Z-stabilizers are preserved either way
Final: measure C|ψ⟩ → z; return (C, z) as classical description; state = C†|z⟩
```

### Why it works (analysis pattern)
- Success per round: p_r = (1 − 2^−r)/2 where r = n − ℓ (codimension). Stopping time is a sum of independent Geometric(p_r) variables; E[T_stop] = Σ 1/(1−2^−r) < 2n + 4. Janson-style upper-tail bound gives the √(n log(1/δ)) tail in T.
- The CNOT-layer F_u is the crucial trick: it concentrates the sampled X-type stabilizer onto one pivot qubit while provably not disturbing any already-diagonalized generator (⟨u,s⟩ = 0 for s ∈ D).
- Random H vs HS choice avoids needing to know whether the pivot carries X or Y — a 2-wise guess that costs only a factor 2.

### Nullity-r extension (sketch)
At nullity r, only a 2^−O(r) fraction of sampled differences are X-parts of stabilizers; the rest are harmless (still ⊥ to diagonal stabilizer space, so updates never destroy progress). Compression slows by factor 2^O(r); then random-Clifford tomography on the residual ≤ r-dimensional logical subsystem → total O(n·2^r) single-copy measurements.

## When To Use
- Learning/certifying stabilizer states with hardware that cannot jointly measure two copies (no Bell-basis apparatus, no coherent two-copy memory)
- Sample-optimal benchmarking of stabilizer prep (magic state factories, QEC logical states)
- Estimating stabilizer fidelity of T-doped / low-magic circuits from single-copy data
- Designing experiments where adaptivity budget matters: use this as the reference point that adaptive = Bell-sampling-optimal, non-adaptive = quadratically worse

## Pitfalls
- **Adaptivity is essential**: the Ω(n²) lower bound applies to non-adaptive single-copy strategies (quadratic phase states). Dropping the feedback loop silently costs a quadratic factor.
- **Two copies per round, measured separately**: "single-copy" means no JOINT measurement — the algorithm still consumes 2 copies per round for difference sampling (N = 2T + 1 total).
- **Exact learning assumes a pure exact stabilizer state**: for noisy/approximate states use the tolerant tester variant; the exact loop can stall or misidentify if the state has non-stabilizer components (nullity > 0 — use the nullity-r extension).
- **The H/HS guess fails half the time by design**: expected rounds double vs an oracle correction; this is accounted in E[T] < 2n + 4, not a bug.
- Distinct from arXiv:2607.02444 (limited-memory testing skill): that work bounds TESTING with bounded quantum memory via Bell difference sampling; this work supplies the adaptive LEARNING algorithm and shows adaptivity closes the single-copy gap.

## Related Skills
- [[optimal-stabilizer-testing-limited-memory]] — memory-bounded stabilizer testing (arXiv:2607.02444)
- [[sample-optimal-gaussian-state-learning]] — analogous single-copy learning question for bosonic Gaussian states
- [[mle-toolbox-eeg-meg]] — unrelated domain, same adaptive-measurement budget thinking
