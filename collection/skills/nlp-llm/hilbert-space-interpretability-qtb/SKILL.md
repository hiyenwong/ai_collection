---
name: hilbert-space-interpretability-qtb
description: "Hilbert-space interpretability framework for Quantum Transformer Blocks: track quantum mutual information, entanglement entropy, participation ratio, and inter-layer fidelity through circuit layers to watch a quantum model think. Use when interpreting variational quantum circuits, building intrinsically interpretable QML, or diagnosing quantum model failures."
---

# Hilbert-Space Interpretability for Quantum Transformer Blocks

**Source**: arXiv:2609.23016 (Gasparini & Iacopetta, Query Machines B.V., 2026-09-19) —
quant-ph, cs.AI, cs.LG. Accepted at IEEE QCE 2026.

## Core Thesis

Quantum models need not be opaque. The mathematical structure of quantum mechanics supplies
**exact, basis-independent interpretability metrics** computed directly from the quantum state
during computation — no post-hoc reverse engineering of activations. A fully-coherent circuit
(no classical bypass) makes every metric a genuine window into the computation.

## The Three Questions → Four Metrics

| Question | Metric | Definition |
|----------|--------|-----------|
| **What** does the model attend to? | Quantum Mutual Information | MI(i,j) = S(ρ_i) + S(ρ_j) − S(ρ_ij), von Neumann entropies of partial traces → n×n "quantum attention map" |
| **When** are correlations formed? | Layer-wise MI snapshots | Statevector snapshots at each layer boundary show when routing forms |
| **How much** state is used? | Participation ratio | Effective Hilbert-space dimension |
| **Why** did a prediction fail? | Entanglement entropy S_A + inter-layer fidelity F(ψ_l, ψ_{l+1}) | Correct vs incorrect MI diagnosis; fidelity separates layers doing real unitary work from near-identity layers |

## Architecture: Quantum Transformer Block (QTB)

- n qubits partitioned into P position registers × k qubits each (paper: 4 registers × 3 qubits = 12 qubits, Hilbert space dim 4096)
- **Three stages per layer**:
  1. *Encoding*: input-dependent rotations embed classical features
  2. *Feedforward* (intra-register): variational rotations + entangling gates within each position register
  3. *Attention* (inter-register): parameterized entangling gates between causally connected pairs (i>j) — learned parameters control inter-position information flow
- **Full-coherence design principle (CRITICAL)**: no classical bypass/residual paths. In
  hybrid designs, classical residuals absorb most information flow and quantum-state
  interventions have no measurable effect — the #1 failure mode of quantum interpretability
- Vocabulary 8 tokens, 2 circuit layers; readout from measurement statistics

## Validated Findings (with numbers)

1. **MI aligns with ground-truth task structure**: AUC = 0.69 on lookup task. Four tasks with
   known dependency structure: Copy (all↔pos1), Lookup (pos0↔target position — data-dependent
   attention), Conditional (branch on token value vs threshold), Repeat (negative control — no
   inter-position dependency)
2. **Entanglement is causally necessary**: disabling attention (entangling) gates collapses
   accuracy 100% → 15% while MI → 0; on hardware 98.6% MI reduction (ibm_kingston)
3. **MI co-evolves with accuracy during training**: Spearman ρ = 0.92 on lookup, every seed
   individually significant
4. **Per-sample MI predicts prediction correctness**: ROC AUC = 0.84 on conditional task —
   a built-in confidence signal
5. **Negative-control nuance**: Repeat develops non-zero MI unless readout exposes the
   computational basis directly — MI tracks information-theoretic structure, not task necessity

## Hardware-Ready Estimation (Shot-Based Counterparts)

Every exact metric has a measurement-count counterpart:
- MI → marginal + joint Shannon entropies with **Miller–Madow bias correction**
- Entanglement entropy → Rényi-2 purity
- Inter-layer fidelity → destructive SWAP test or shadow tomography
- Shot-based MI is Shannon MI over outcome distribution, NOT von Neumann MI — absolute values
  differ between simulation and hardware, but **ordinal structure (which pairs are most
  correlated) is preserved**

## Validation Protocol (Copy This)

1. Design tasks with known ground-truth attention patterns BEFORE training
2. Compute exact metrics in simulation (statevector + partial traces)
3. Ablation: disable entangling (attention) gates → confirm accuracy collapse + MI→0
4. Track MI vs accuracy across training epochs (Spearman per seed)
5. Per-sample MI as correctness predictor (ROC AUC)
6. Re-estimate all metrics from shot counts on hardware; verify ordinal structure survives
7. Bootstrap 95% CIs (1000 resamples); Mann–Whitney U, Kendall τ, permutation tests (10k)

## When to Use

- Interpreting what a trained variational quantum circuit learned (design-time expressibility
  metrics do NOT capture this)
- Quantum architecture search with interpretability feedback
- Debugging QML failures: wrong-pair vs diffuse-routing diagnosis from MI matrices
- Confidence estimation on quantum models (per-sample MI)
- Any claim that "quantum models are black boxes" — this framework is the rebuttal

## Pitfalls

- Hybrid circuits with classical bypass: quantum-state analysis is uninformative — enforce
  full coherence first
- Do not compare absolute MI between simulation (von Neumann) and hardware (Shannon) —
  compare ordinal structure only
- Post-hoc methods (Q-LIME, quantum SHAP, gradient saliency) discard the intermediate
  quantum state; this framework uses the state itself
- Small synthetic tasks only — scale persistence unproven (authors' own limitation)

## Key Contrasts

- Classical interpretability (attention maps, probing, activation patching) = post-hoc on
  opaque activations; Hilbert-space metrics = exact properties of the state during computation
- Entanglement-as-expressibility (design-time) vs this work: interpretability of the LEARNED
  representation on a specific task
