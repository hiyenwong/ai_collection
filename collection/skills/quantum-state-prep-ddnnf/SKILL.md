---
name: quantum-state-prep-ddnnf
description: Use when preparing quantum states from compiled circuits.
category: ai_collection
---

# Quantum State Preparation for Weighted d-DNNF

**Paper**: Quantum state preparation for weighted d-DNNF (arXiv:2610.02094, Hegeman, Lee, Laarman — Leiden University, Oct 2026)

## Core Insight

The quantum state preparation problem (QSP) — building a circuit that prepares Σ_x D(x)|x⟩ from a classical description — is hard in general and can cancel a quantum algorithm's advantage. But when the state is described as a **weighted d-DNNF** (deterministic, decomposable pseudo-Boolean circuit), the preparation circuit can be obtained in **linear time** in the circuit size, up to complex arithmetic.

## Main Results

For a weighted d-DNNF D: {0,1}^n → ℂ representing state S₂(D) = Σ_x D(x)|x⟩:

- **Theorem 4/5**: For every normalized weighted 2-d-DNNF with S₂(D) a state, a quantum circuit computes it with **O(|D|) gates**, depth O(depth(D)), and 2|int(D)|−2 ancillas. Description computable in O(|D|) time (constant parallel time with poly(|D|) processors).
- **Corollary 6**: arbitrary weighted d-DNNF converts to 2-d-DNNF with size/depth/width trade-offs, preserving the linear-time claim.
- Weighted d-DNNF is **exponentially more succinct** than weighted FBDD (the previously prepared language, Phe 2025) and than #SAT model-counting internal languages.

## Algorithm Structure

1. **Normalize** the weighted 2-d-DNNF (weights absorbable in linear time; Section 8 shows normalization preserves the represented state).
2. **Certificate-based superposition**: each basis state |x⟩ with D(x) ≠ 0 has a *unique certificate* (determinism). Build a superposition over *partial* certificates, growing depth until a superposition over all certificates is reached.
3. **Gate construction**: an ancilla qubit c_g per internal gate g, plus n_g ancillas; CH-gates fire per certificate element — in every basis state of nonzero amplitude at most one CH fires per variable (partial certificates contain each variable at most once, by decomposability).
4. **Uncompute** ancillas. The uncomputation was the significant new challenge vs. FBDD (where each basis state has a unique *path* — here certificates form a DAG, not paths).

## Reusable Patterns

1. **Knowledge-compilation → quantum circuit compiler**: any classical KC language with determinism + decomposability (d-DNNF, SDD, FBDD families) admits a *linear-time* state-preparation compiler — structure exploitation beats generic QSP (worst-case exponential). When facing a QSP task, first ask "is the amplitude function compilable to d-DNNF?" (e.g., via #SAT/model-counting toolchains).
2. **Certificate superposition trick**: for DAG-structured decompositions, create superpositions over partial certificates and grow incrementally — analogous to branching programs but handles shared subgraphs.
3. **Fan-out-2 restriction (2-d-DNNF)**: reducing to bounded fan-in/fan-out costs only log factors and simplifies gate-level construction — a general pattern for circuit-compilation proofs.
4. **Succinctness ladder**: FBDD ⊂ d-DNNF ⊂ (weighted) — pick the most succinct representation you can still compile; succinctness directly shrinks the QSP circuit size.

## Relation to Informatics

d-DNNF is the canonical tractable knowledge-compilation language (Darwiche). This result makes KC languages a *front-end for quantum loading of structured distributions* — directly relevant to loading Bayesian networks, probabilistic databases, and weighted model counts (all d-DNNF-compilable) as quantum states.

## Activation

quantum state preparation, QSP, d-DNNF, knowledge compilation, pseudo-Boolean circuit, model counting, FBDD, succinct representation, circuit synthesis, Grover-Rudolph, quantum data loading, certificate superposition
