---
name: functional-representational-dissociation-linear-networks
description: Analytical dissociation of function vs representation in linear nets. Use for RSA or alignment claims.
category: ai_collection
version: "1.0.0"
source: arXiv:2609.38998
source_title: "Not all solutions are created equal: An analytical dissociation of functional and representational similarity in deep linear neural networks"
authors: "Lukas Braun, Erin Grant, Andrew M. Saxe (Oxford / UCL Gatsby)"
published: 2026-09-30
categories: "cs.LG, q-bio.NC"
trigger_words:
  - representational similarity analysis
  - RSA caveats
  - solution manifold
  - task-specific representations
  - task-agnostic representations
  - parameter noise robustness
  - linear predictivity
  - representational drift
  - brain model alignment
---

# Functional vs Representational Dissociation in Two-Layer Linear Networks

**arXiv**: 2609.38998 (30 Sep 2026) · Braun, Grant & Saxe — ICML. Code: github.com/lukas-braun/dissociating-similarity

## TL;DR

In two-layer linear networks (input X → h = W1x → W2h), the set of zero-error solutions forms a
**solution manifold** M = {Ω2Ω1 : Ω2Ω1Σxx = Σyx} that the paper characterizes *exactly* and partitions
into four nested solution types with sharply different representational properties:

| Type | Definition | Hidden reps H | RSM |
|---|---|---|---|
| **GLS** (general linear solution) | any global min | √Q SV^T X + Γ1 Pi X — nearly arbitrary (can spell "elephant") | **task-agnostic** (depends on arbitrary Q, Γ1) |
| **LSS** (least-squares / min function norm) | min ‖W2W1‖_F | same DOF as GLS | task-agnostic |
| **MRNS** (min representation-norm) | min ‖W1X‖²+‖W2‖² | R √N O^T X⁺X, unique up to orthogonal R | **unique & task-specific**: RSM = O N O^T N |
| **MWNS** (min weight-norm) | min ‖W1‖²+‖W2‖² | R √S V^T X, unique up to orthogonal R | **unique & task-specific**: RSM = X^T V √S V^T X |

**Function and representation are fully dissociable**: the same function can arise from wildly
different representations (GLS/LSS), and near-identical RSMs can support different functions. The
central practical result — *only one pressure forces task-specific representations*:

- Robustness to **input noise** → selects LSS (min ‖Ω2Ω1‖_F) → still task-agnostic. ✗
- Low **generalization/secondary error** → permits task-agnostic solutions. ✗
- Robustness to **parameter noise** → expected loss = ½P⁻¹(‖Ω1 X‖²_F + ‖Ω2‖²_F + c) → minimized
  **exclusively by MRNS/MWNS** → task-specific. ✓

Interpretation: parameter-noise robustness (implicit/explicit low-norm regularization) is the
plausible selection pressure behind brain–model representational alignment; alignment reflects a
computational advantage, **not** functional equivalence.

## Solution Manifold Anatomy (Theorem 3.1)

Input space partitions into: relevant (P_r = VV^T), observed-but-irrelevant (P_i = AA^T − VV^T),
unobserved-null (P_u = I − AA^T), where cSVD(X) = AB^T C^T, cSVD(Σyx Σxx⁺) = U √S V^T, rank r = rank(Σyx).

```
Ω1 = √Q S V^T + Γ1 P_i + Γ2 P_u          # Q: arbitrary full-column-rank; Γ1/Γ2 free (rank constraint)
Ω2 = √U S Q⁺ + Ψ + Γ3 (I − HH⁺)           # Ψ cancels interference of irrelevant inputs in the core
```
- First terms = **core** input-output mapping; Γ's project irrelevant/null directions into hidden space;
  Ψ/Φ correct the interference those projections create; rank constraints guarantee corrections exist.
- Q-transformations (Ω1→QΩ1, Ω2→Ω2Q⁻¹) redistribute computation across layers — they preserve rank and
  fully characterize the manifold only in the full-rank square case; the Γ machinery covers the rest.
- Nesting: MWNS ⊂ MRNS ⊂ LSS ⊂ GLS, each removing more freedom (null-space projections, irrelevant
  projections, then core imbalance).

## Consequences for Neural Data Analysis (Section 4)

### 1. Linear predictivity (Yamins-style regression R²)
Driven by **solution type, not functional alignment**: task-agnostic (higher-rank, mixed
relevant+irrelevant) sources predict targets well; task-specific (low-rank, relevant-only) sources
predict task-agnostic targets *worst* (within-function R² can be lower than across-function R² when
types differ). High predictivity ≠ same computation.

### 2. RSA
- Comparisons involving GLS/LSS fluctuate unpredictably (RSM changes along any random walk on M).
- Task-specific ↔ task-specific: static, consistent r — but **imperfect similarity even within the
  same function** when types differ (MRNS vs MWNS give different unique RSMs).
- RSA reflects functional similarity only when representational constraints enforce unique RSMs.

### 3. Representational drift
Decoders trained at t=0 degrade rapidly during a random walk that keeps the function *exactly fixed*
(Fig 4C). Drift need not signal functional change — it can be reparametrization within the functionally
equivalent class. Bounds "stable perception ⇒ stable representations" (Rule et al. 2019) are unfounded.

### 4. Stability-plasticity
Many distinct synaptic configurations implement one function → isolated synaptic/representational
changes cannot license inferences about learning or function at the network level.

## Nonlinear Extension (Section 6)

ReLU nets admit exact function-preserving invariances: permutation, rescaling (α/α homogeneity),
**nuisance neurons** (insert with zero outgoing weights), **duplication** (copy a hidden neuron,
halve both outgoing weights), **input-nullspace perturbations**. A trained MNIST net's hidden
activations can be reshaped (augmented-Lagrangian) into "two elephants" while preserving every
training-set label — and even while preserving the exact I/O map (stricter).
Empirics mirror the linear theory: input-null expansions hurt under input noise; scaled/nuisance/
duplicate expansions degrade under parameter noise (duplicate least, noise averaging); none inflate
test error at zero noise.

## Methodology Checklist (when you compare representations)

1. **Classify solution type before comparing**: which norm is (implicitly) minimized? Weight decay →
   MWNS-like; SGD from small init → task-specific "rich" regime; lazy/NTK-like → task-agnostic-ish.
2. Never interpret linear predictivity or RSA r as evidence of shared computation without
   establishing representational uniqueness (or comparing like types).
3. For drift analyses: first rule out reparametrization drift (decode with a *fixed* decoder across
   time; report function-relevant metrics alongside).
4. Parameter-noise robustness is the alignment-forcing pressure — low-norm/regularized training is a
   mechanistic hypothesis for why brains and ANNs align, testable via noise-injection experiments.
5. Beware benchmarks (Brain-Score, NSD predictivity) that mix solution types across models —
   variability in R² may be parametrization variability, not functional difference.

## Pitfalls

- All exact results are for **two-layer linear** nets; nonlinearity adds invariances but the
  partition (task-specific vs agnostic) is validated only empirically there.
- MRNS vs MWNS both "task-specific" but yield *different* RSMs (input-statistics vs LS solution
  geometry) — cross-type RSA is imperfect even at identical function.
- Non-identifiability means structure claims ("the network represents hierarchy X") are underdetermined
  without specifying which subregion the trained solution actually occupies.
- The analysis is at global minima of convex-equivalent loss; transitional dynamics (lazy→rich) only
  touch the picture via implicit regularization arguments.

## Applications

- Interpreting brain–ANN alignment (RSA, predictivity, Brain-Score-style benchmarks).
- Designing continual-learning/drift experiments that separate functional vs parametric change.
- Theory-grounded regularization choices: if you want comparable representations, train toward
  minimum-norm submanifolds.
- Degenerate biological systems (Prinz/Marder-style) — same function, different circuits — now have a
  linear-network analogue with exact geometry.

## Related Skills

- [[untrained-cnns-match-backpropagation-v1-rsa]] (RSA methodology)
- [[stimulus-symmetries-rsm-confound]] (RSM confounds)
- [[snr-sample-size-representational-alignment]] (alignment data scaling)
- [[gain-vs-off-manifold-decomposition]] (on/off-manifold dynamics)
- [[platonic-representations-brain]] (universal geometry claims)

## Source

arXiv:2609.38998 — Braun, L., Grant, E., Saxe, A.M. (2026). *Not all solutions are created equal: An
analytical dissociation of functional and representational similarity in deep linear neural networks.*
ICML (PMLR 267).
