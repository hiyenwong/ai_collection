---
name: mrqpe-memory-reduced-quantum-probability
description: Memory-reduced quantum estimation of rare-event probabilities.
category: ai_collection
---

# MRQPE: Memory-Reduced Quantum Probability Estimation (arXiv:2610.10756)

Chen, Gupta, Yang, Neufeld, Thompson, Elliott, Gu (NTU CQT / U Manchester, Oct 2026). Quantum-enhanced inference of conditional future probabilities P(f(x_{0:L})=1 | past) with BOTH reduced sampling cost AND reduced memory — solving the state-preparation blocker that makes QAE impractical near-term.

## Core Insight

QAE's quadratic speedup (O(1/ε²)→O(1/ε) samples) is nullified by state preparation: loading P(X_{0:L}|x⁻) needs a circuit A whose brute-force synthesis is exponential in L, and the bit-to-qubit translation of even a memory-minimal classical model needs one qubit per tracked bit — saturating near-term devices. Meanwhile any memory-truncated classical model (D̃ < D_c) has an irreducible systematic bias floor that no number of samples can cross.

Resolution: quantum models with memory dimension D̃ are strictly more expressive than classical models of the same D̃ (D_q < D_c possible; non-orthogonal quantum memory states {|s_j⟩} need not be linearly independent). Truncating the QUANTUM model to D̃ states yields far lower bias than truncating the classical one — so amplitude estimation runs on a cheaper, less-biased sampler.

## Algorithm (MRQPE)

Inputs: classical model M_c=(S,T_jk^x) of process P; binary event predicate f; horizon L; observed past x_{-r:0}; memory budget D̃.

1. **QuantumModel**: map M_c to quantum model — unitaries U_s with U_s|s_i⟩|0⟩ = Σ_j Σ_x √T_{i,j}^x |s_j⟩|x⟩ (Eq. 3). Exact statistical replication.
2. **Truncate** (if D̃<|S|): reduce memory dimension to D̃ quantum states (Alg. 4).
3. **EncodePast**: U_ini prepares |s_j⟩ consistent with observed past (Alg. 3).
4. Build A = U_{s(L-1)}···U_{s(0)}·U_ini (Eq. 4). Output registers: L blocks of ⌈log₂|X|⌉ qubits; memory: n=⌈log₂ D̃⌉ qubits.
5. Oracle S_χ marks strings where f=1 (multi-controlled gate); reflection S_0 on all-zero. NOTE: S_χ acts ONLY on output registers; A, A†, S_0 act on memory+output both — the entangled memory tail must be carried through the Grover operator or QAE fails.
6. Grover Q = −A S_0 A† S_χ; estimate p̂ via iterative/maximum-likelihood QAE variants (LIS/EIS schedules — no phase estimation, shallow circuits for NISQ).

Output: p̂ with reduced variance (1/ε scaling) AND reduced bias vs any classical D̃-state model.

## Key Results

- Cyclic random walk (8-state target, memory capped at D̃=4): classical 4-state model has RMSE bias floor ~10⁻⁶ on rare events (p∈[10⁻⁹,10⁻⁸]) even at N→∞; quantum 4-state model crosses BELOW the classical bound at N≈2×10⁴ samples.
- 16-state target, same D̃=4: classical floor 8×10⁻⁴; quantum undercuts it with ~3000 samples (>6× fewer).
- Gate cost of A: O(L·D²·|X|²) CNOTs — D̃=4 means 2 qubits vs 3 (8-state) or 4 (16-state) qubits for exact models. Under Quantinuum-like noise, the truncated 2-qubit model often beats the exact 3-qubit one in total bias (fewer gates → less accumulated noise).
- Advantage persists toward the continuum limit (k→∞) and for non-Markovian processes (discretized AR models, App. H).

## Reusable Patterns

1. **Bias-variance decomposition under memory constraints**: total error ε = ε_rand(N) + ε_bias(D̃); classical truncation fixes ε_bias>0 forever — check whether a quantum/complex-valued/generalized-state representation of the SAME memory dimension lowers the bias floor before optimizing sample count.
2. **Non-orthogonal memory states**: classical causal states demand distinguishability; quantum memory states may overlap — superposition encodes more predictive structure per qubit. Generalizes to any model-reduction setting: compress in a richer state space, not a poorer one.
3. **Entangled-tail Grover construction**: when the sampler leaves residual entanglement (memory register), reflections A S_0 A† must act on the FULL register including the tail; only the oracle is output-restricted. Reusable in any QAE over recurrent/sequential samplers.
4. **NISQ-realistic advantage accounting**: smaller D̃ → smaller U_s → fewer gates → less noise; a deliberately truncated model can win end-to-end even against an exact one. Always price memory reduction in gate-noise, not just bias.

## When to Use

- Rare-event probability estimation (risk, black swans, earthquake onset) where classical memory truncation caps accuracy.
- Quantum finance / quantum Monte Carlo state-preparation design.
- Any QAE application blocked by data loading (the 'A operator' problem) for sequential/stochastic models.
- Model compression studies: quantum representations of RNN/Transformer predictive states as provably-low-bias low-memory replacements.

## Key References

- Quantum-enhanced dimensional reduction: Gu et al. [10]; provable advantage in dimensionally reduced q-models [27]; unbounded quantum memory advantage for quantized predictive models [40].
- Causal states / topological state complexity D_c: computational mechanics literature [8,9].
- Iterative Amplitude Estimation (LIS/EIS): shallow-circuit QAE without phase estimation [15–18].

**Activation**: quantum amplitude estimation state preparation, conditional probability future inference, memory bias variance tradeoff, rare event quantum Monte Carlo, quantum model compression expressive advantage, entangled memory Grover, stochastic process simulation quantum
