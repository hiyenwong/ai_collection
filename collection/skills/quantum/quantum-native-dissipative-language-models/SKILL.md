---
name: quantum-native-dissipative-language-models
description: Use when building quantum-native recurrent LMs with dissipative memory, Born-rule readout, or hardware validation.
category: ai_collection
metadata:
  arxiv_id: "2610.12806"
  published: "2026-10-08"
  authors: "Deniz Yunus Göğüş"
  tags: [quantum-language-model, dissipative-memory, CPTP-channel, Holevo-bound, NISQ-hardware]
---

# Quantum-Native Dissipative Language Models (UMW/UMW-D/UMW-G)

Source: arXiv:2610.12806 (quant-ph, 8 Oct 2026) — byte-level autoregressive LM whose hidden state is a
density matrix ρ_t on n qubits, transitions are learned token-conditioned CPTP maps, next-byte
probabilities are Born-rule POVM readout (no softmax, no classical vocabulary projection).

## Core architecture (three memory dynamics)

| Variant | Update E_x(ρ) | Property |
|---------|---------------|----------|
| UMW (unitary) | W_x ρ W_x† | Norm-preserving, injective — **cannot contract or reset** |
| UMW-D | D(W_x ρ W_x†) — fixed learned dissipation | Work qubit coupled via V, traced out — forgetting learnable |
| UMW-G | Σ_k K_k^(x) ρ K_k^(x)† — one CPTP map per token | Write + forget jointly, token-conditioned (analogous to GRU gate) |

Readout (all rows): p(y|context) = Tr(M_y ρ_t), 256-outcome POVM with M_y = S G_y S,
S = (Σ_y G_y)^(-1/2); sampled y is fed back autoregressively.

## Key results (pre-registered, falsification-first protocol)

1. **Unitary recurrence loses to its own retrained one-token control** (2.5167 vs 2.3705 nats/byte at n=4).
   Trace-distance invariance under W means closed unitary dynamics cannot implement many-to-one contraction
   (forgetting). Width, context curriculum, replay-mixing, per-position POVMs all fail to close the gap.
2. **UMW-D: +0.101±0.008 nats over channel-matched h1; UMW-G: +0.196±0.025 nats** (more than doubles
   memory value). Spectral analysis: 1 conserved mode + slow modes (6/256 half-life >4 steps) +
   fast-damped remainder — a learned forgetting schedule.
3. **Never beats retrained two-token control** (h2) at 4–8 qubits; consistent with Holevo accessible-information
   bottleneck (n qubits → ≤n bits/readout; text unigram entropy 4.7 bits/byte, two bytes ≈ 9 bits).
4. **Key-value recall ladder (4–7 qubits)**: K*=1,1,2,2 — one stored pair at n=4–5, two pairs at n=6–7,
   three unsolved. Nayak's bound: n ≥ (1−H2(p))·m excludes perfect 3-value recall at n≤9.
5. **Hardware (IBM Heron 156-qubit, ibm_marrakesh)**: memory-register TVD 0.156±0.041 tracks simulator
   through 12-token context (12/12 circuits beat uniform null); next-bit |Δp| median 0.075 at 4-token
   prefixes; autoregressive generation with every bit sampled from measured probabilities.
   Line entangler (96–576 two-qubit gates) beat ring entangler (354–1452, only 4/9 circuits) —
   topology-aware compilation decided hardware pass/fail.
6. **Distillation economics**: operator-level distillation fails (fidelity 0.25–0.44); task-aware
   distillation succeeds at 10–17× compression (depth-12, 120 params/channel vs 2048), ≈0.12–0.15 nats cost.
   Rule: *statistical structure is depth-cheap; sharp memory is depth-hungry* — and on hardware, depth is coherence.
7. **Purification-factor training**: track A with ρ=AA† (rank ≤ 2^n) instead of ρ; exact at full rank,
   enables controlled low-rank training at n=7–8 (discarded weight <10⁻⁶); straight-through truncation
   with no decomposition in the autograd graph.
8. **Memory-entropy separation (perturbed coin)**: gradient-trained 1-qubit models land below the attacked
   classical entropy-error frontier at matched prediction error (median margin 0.04 nats emergent,
   0.44–0.66 with annealed S(ρ̄) penalty) — quantum statistical complexity regime reachable by training.

## Implementation guidance

- Recurrent state: never measure memory register between tokens; measure only a work/ancilla register.
- CPTP parameterization: E_x(ρ) = Tr_W[V_x(ρ⊗|0⟩⟨0|_W)V_x†] guarantees complete positivity by construction.
- Controls must be **retrained from scratch** with same parameterization/count (h1: ρ_t+1=E_x(ρ_0);
  h2: two-token) — never truncate a trained recurrent model at inference.
- Width scaling negative: byte NLL does not improve 4→8 qubits (2.15→2.30); context scaling negative beyond 12.
  Corpus structure (two-byte dominance) dominates at these scales.
- Pre-registration discipline: hypotheses with quantitative bars committed before runs; every negative
  reported (delay curriculum needed for UMW; DD+twirling made hardware worse; depth-30 recall broke).

## Pitfalls

- Unitary RNN lore ("norm preservation stabilizes gradients") does not transfer to quantum-native byte LMs:
  the failure is structural (no contraction), not optimization (gradients healthy, low SNR — not barren plateau).
- Hardware DD + Pauli twirling can WORSEN per-bit accuracy (median 0.103→0.137) — measure, don't assume.
- Ring-entangler circuits transpile ~3× design count on heavy-hex; line entanglers with identical simulated
  quality cost 3.7× fewer gates — entangler topology is a first-class experimental variable.
- A single 256-outcome POVM is too deep for NISQ; a distilled binary-tree readout (8 stages, each conditional
  bit probability physically measured) approximates it with ~0.09 nats cost and is back-action-free.

## Applications

- Quantum-native sequence models beyond feature-extractor hybrids (state, dynamics, sampling all quantum).
- Capacity accounting for small quantum memories via Holevo/Nayak framing of recall tasks.
- Pre-registered falsification protocol as methodology for QML claims with honest negative results.

## Related skills

- `qds-snn-quantum-spiking`, `qtn-rqnn` family, `hybrid-quantum-classical-feature-fusion-medical`
