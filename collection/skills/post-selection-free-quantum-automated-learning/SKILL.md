---
name: post-selection-free-quantum-automated-learning
description: Use when training quantum models without variational parameters. Coherent QAL.
category: quantum-computing
---

# Post-Selection-Free Quantum Automated Learning (FPAA-QAL)

**Source**: Post-Selection-Free Quantum Automated Learning (arXiv:2610.08219, Wang & Liu, Oct 2026)

## Core Insight

Quantum Automated Learning (QAL) trains a quantum **state** via data-conditioned projector-mixing contractions — no variational circuit parameters. But its measured implementation post-selects on every step succeeding: if the survival probability of a T-step path is `P_chain(T) = Π p_t`, the expected restart cost explodes as any p_t shrinks. This paper replaces measured restart with **coherent execution + fixed-point amplitude amplification (FPAA)**: keep all success flags unmeasured, amplify the joint success branch, and trace out flags to get an unconditional output with certified error.

## Reusable Methodology

### 1. Flagged unitary dilation of each contraction
- Each nonunitary training update (contraction K) is block-encoded as a unitary U_K on flag ⊗ system: `⟨0|F U_K |0⟩F = K`.
- Flags stay COHERENT (unmeasured) through the whole pre-declared training path ω = (s_1..s_T) — never collapse intermediate models.

### 2. Fixed-point amplitude amplification on the joint success space
- After the full path runs coherently, FPAA (not standard Grover — no known reflection needed, robust to imperfect reflections) raises the probability of the all-flags-good branch.
- Cost: coherent re-executions of the path + its adjoint + phase reflections about input and success spaces.
- The amplified good branch preserves the conditional QAL model EXACTLY; tracing flags yields an unconditional model whose state/loss error is controlled by the residual failure target δ.

### 3. Pathwise certificate BEFORE execution
- A joint certificate bounds survival probability AND learning loss for the same sampled example order — computed pre-execution to CHOOSE the amplification degree m.
- Proof anchors on an imaginary-time reference state, controlling an unnormalized loss margin; a low-energy spectral condition gives a positive survival floor s* > 0.
- This turns "how much amplification do I need?" from a guess into a computable design parameter: m ≈ O(δ^{-1/2} / s*).

### 4. Depth–success trade quantification
- Compare (a) measured global restart: discards failed partial paths, cost = E[prefixes] / survival; vs (b) coherent FPAA: cost = coherent path executions + reflections.
- A commuting-projector family gives a closed-form certificate identifying the regime where FPAA strictly beats restart on selected-filter calls (cost ratios < 1 verified numerically; e.g. survival floor 1e-6, unconditioned loss < 0.00242, ratio ≪ generic Theorem-3 bound).

## Transferable Patterns
1. **Flag-dilation + defer measurement**: any post-selected multi-step quantum pipeline (state prep, annealing readout, learned filters) can be made post-selection-free by dilating each filter with a success flag and amplifying the joint success space coherently.
2. **Pre-execution certificates**: derive a pathwise bound (survival × loss jointly) to size amplification BEFORE spending coherence — same philosophy as a-priori shot/circuit-budget allocation.
3. **FPAA over Grover when reflections are imperfect**: fixed-point search tolerates imperfect state/flag reflections, suited to learned (unknown) target spaces.
4. **Conditional-model preservation**: amplification acts on the success branch only, so the learned conditional model is untouched — errors enter only via the traced-out residual failure weight.

## Activation
quantum automated learning, QAL, post-selection, fixed-point amplitude amplification, FPAA, coherent training path, flag dilation, projector-mixing, survival probability, restart cost, imaginary-time reference
