---
description: Use when designing quantum self-attention via QBM circuits.
name: fc-qbm-quantum-attention-lm
category: ai_collection
version: 1.0
author: cs-cron-2026-10-27
license: MIT
metadata:
  hermes:
    tags: [quantum-language-model, quantum-boltzmann-machine, self-attention, amplitude-encoding, ising-hamiltonian, phase-attention, qcbm, quantum-machine-learning, born-rule-normalization, parameter-shift, generative-model]
    source: arXiv:2610.34492
    related_skills: [quantum-native-dissipative-language-models, spectral-born-machines, iqp-circuit-trainability, quantum-jepa-born-prior-world-models, equilibrium-propagation-lif-snn]
---

# FC-QBM Quantum Self-Attention Language Model (Wave Is All You Need)

Methodology from arXiv:2610.34492 — "Wave Is All You Need: A Quantum Language Model Based on Fully Connected Quantum Boltzmann Machine" (Liu Jun, Hunan University of Finance and Economics; quant-ph, 25 Oct 2026).

## One-Line Summary

Replace classical self-attention's explicit QKV matrix pipeline with ONE unitary evolution: amplitude-encode the concatenated token stream, phase-modulate with a fully connected quantum Boltzmann machine (diagonal Ising Hamiltonian), read out with per-qubit RY gates — bias phases act as positional encoding, pairwise-coupling phase differences `cos(φ(r')−φ(r))` act as attention scores, and measurement probabilities are Born-normalized so softmax disappears entirely.

## When to Use / Activation

- Designing a quantum language model or quantum self-attention mechanism (not hybrid plug-in quantum layers inside a classical transformer).
- Encoding token positions + pairwise interactions implicitly in phase space instead of explicit matrix multiplication.
- Building an energy-based generative LM trainable by backprop with only O(N²) circuit parameters (44 params at 8 qubits).
- Replaying/validating FC-QBM-LM claims or designing similar phase-attention circuits.

## Core Mechanism (equation-level)

1. **Amplitude encoding pipeline (Eqs. 31-38):** concatenate n token embeddings → shift by min (non-negative) → L1 normalize → sqrt → amplitudes `a_r` on 2^N basis states, `N = ⌈log2(n·d_model)⌉`, zero-pad the slack (paper: n=10, d=25 → 250 dims → N=8, 6 padded). Constraint: 2^N ≥ n·d_model.
2. **FC-QBM Hamiltonian (Eqs. 14-17):** `H = Σ_i b_i σZ_i + Σ_{i<j} w_ij σZ_iσZ_j` — the quantum sibling of the classical FC-BM energy `E = Σ b_i unit_i + Σ w_ij unit_i unit_j` over units ∈ {−1,+1}. H is **diagonal**, so `U_H = e^{−iHt}` acts per basis state: `H|r⟩ = ω(r)|r⟩` with
   `ω(r) = Σ_i b_i(−1)^{r_i} + Σ_{i<j} w_ij (−1)^{r_i+r_j}`, giving phase `φ(r) = ω(r)·t` (Eq. 19-21).
3. **Phase semantics (Eq. 29):** the global phase factor splits into a **bias phase factor** (single-qubit phase combos → positional encoding of token order) and a **weight phase factor** (two-qubit interaction phases → pairwise attention strengths).
4. **RY readout (Eqs. 22-28):** `U_R = ∏_i RY(2θ_i)`; measurement probability
   `p_l = Σ_r β_{l,r}² a_r² + 2 Σ_{r<r'} β_{l,r}β_{l,r'} a_r a_r' cos(φ(r')−φ(r))`
   where `β_{l,r} = ∏_i ⟨l_i|RY(2θ_i)|r_i⟩`. The `cos(Δφ)` term is exactly the geometric dot-product interpretation — Eq. 30 shows any two token-embedding basis vectors interact via `a_r a_r' cos(φ(r')−φ(r))`, mathematically equivalent to classical self-attention's `q·k`. RY(2θ_i) combos give per-basis-vector biased (adaptive) encoding instead of uniform representation.
5. **Free normalization:** measurement probabilities sum to 1 by the Born rule — no softmax in the quantum layer.
6. **Circuit implementation:** single-qubit terms via `RZ(2b_i)`; ZZ couplings via CNOT–`RZ(2w_ij)`–CNOT; trainable params: N biases + N(N−1)/2 weights + N RY angles (8 qubits → 8+28+8 = **44 parameters** implementing the full positional-encoding+self-attention pipeline).
7. **Classical head (Eqs. 39-42):** probability vector P → Linear(2^N→M) → GELU → Linear(M→d_model) → predicted next-token embedding. Loss = MSE(ê_n, e_n); **analytic backprop flows through the quantum layer** (positive/negative phases of FC-BM training mapped onto forward/backward pass).
8. **Generation (Eqs. 60-64):** predicted embedding → dot product with all V vocab vectors → scale by √d_model → top-m → rule filter (poetry constraints) → max-shifted softmax over filtered candidates → sample → autoregressive append.

## Empirical Calibration (paper, 8-qubit Tang-poetry model)

- Corpus: Three Hundred Tang Poems, skip-gram word2vec, V=2481, d_model=25, n=10 tokens/window; quantum layer = 44 params of 36,165 total.
- RY-terminal circuit converges better than RX-terminal control.
- Noise robustness: retains >99% of noiseless convergence across 8 noise intensity levels (small-sample regime).
- Emergent capabilities in quatrain generation: associative/divergent continuation, cross-imagery content, human-aligned word ordering.
- Claim scope: mathematical equivalence to classical self-attention is at the level of the dot-product/interaction computation; the paper does NOT claim end-to-end LLM-beating results — it is an 8-qubit feasibility architecture.

## Validation Replay (5/5 passed, numpy-only statevector, this workspace)

- T1 amplitude pipeline: N=⌈log2 250⌉=8, 6 zero-padded basis vectors, unit-norm amplitudes ✓
- T2 spectrum: H is diagonal and ALL 16 eigenvalues equal ω(r) formula ✓
- T3 closed form vs simulation: Eq. 28 vectorized as `p = diag(B D Bᵀ)`, D[r,r'] = a_r a_r' cos(φ_r'−φ_r); max deviation from exact statevector |⟨l|∏RY·e^{−iHt}|ψ0⟩|² = **1.4e-16** ✓
- T4 normalization: Σp_l = 1 exactly without softmax ✓
- T5 toy 3-qubit FC-QBM-LM (Linear-GELU-Linear head, MSE): 150 finite-diff gradient steps 0.4976 → 0.0190 (96% drop) on an AR(1) next-token task; closed-form gradient matches exact-simulation gradient ✓

## Pitfalls (learned from replay)

- **Sign convention trap:** `s_i = (−1)^{r_i}` means **+1 when bit=0** — write `1 − 2·bit`, never `bit·2 − 1`. The flipped version passes closed-form-vs-statevector self-checks (cos is even) and only fails against the true H matrix spectrum — always keep an explicit Hamiltonian check.
- **RY on non-trivial states:** must mix BOTH components (`new[r] = c·ψ[r] − s·ψ[r1]`, `new[r1] = s·ψ[r] + c·ψ[r1]`). Writing only `new[r1] = s·ψ[r]` silently drops the existing |1⟩ amplitude — normalization breaks only when a second layer exists.
- **Vectorized Eq. 28:** `p = diag(B @ D @ B.T)` with `D = outer(a,a)·cos(φ'−φ)`; the naive double sum is O(4^N) Python-loop slow.
- **Amplitude capacity:** toy tasks must satisfy 2^N ≥ n·d_model; random targets make MSE floor = target variance (unlearnable) — use a real recursive next-token task.
- **FC-QBM ≠ RBM:** keep ALL pairwise couplings (no bipartite restriction); the O(N²) ZZ terms are the attention-score carrier.
- **FC-BM training-phase analogy is structural:** positive phase = forward pass, negative phase (contrastive divergence) = backprop update — do not import Gibbs-sampling machinery; gradients are analytic.

## Relation to Prior Art

- vs HyQuT/hybrid quantum transformers: FC-QBM-LM redefines the attention computation itself rather than compressing subcomponents.
- vs Diffusion-LM/Difformer/ELF: keeps semantic continuity (no discrete matrix decomposition) AND attacks the O(L²) attention cost — under SETH, subquadratic approximate classical self-attention with rigorous error guarantees is impossible; the quantum route sidesteps via parallelism/entanglement.
- vs classical FC-BM (1985): inherits the universal-fitting power of full pairwise coupling while evading the exponential partition function — no Gibbs sampling, training is backprop.
