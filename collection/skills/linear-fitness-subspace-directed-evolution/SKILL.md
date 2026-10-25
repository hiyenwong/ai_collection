---
name: linear-fitness-subspace-directed-evolution
description: "Linear Fitness Subspace (LFS) + Subspace-Guided Evolutionary Search (SGES) methodology for sample-efficient ML-guided protein directed evolution. Recovers a compact assay-specific linear subspace from few labeled variants, then performs surrogate + uncertainty + acquisition inside it. Use when optimizing protein/drug candidates under tight oracle budgets, or when zero-shot PLM scores misalign with target assays."
category: ai_collection
activation:
  - directed evolution
  - protein language model
  - fitness landscape
  - sample-efficient optimization
  - oracle budget
  - surrogate model
  - uncertainty estimation
  - drug discovery
  - protein engineering
  - PLM
---

# Linear Fitness Subspace Directed Evolution (LFS + SGES)

**Source**: arXiv:2610.07607 (2026-10-06, q-bio.QM/cs.AI/cs.LG) — Ma, Xiao, Xiao, Gao, He, Wang.

## Core Idea

Model-guided directed evolution must find high-fitness protein variants under **limited oracle budgets**. Two failure modes of current approaches:

1. **Zero-shot PLM scores** (task-agnostic) can be **misaligned** with the target assay.
2. **Supervised search in full embedding space** (high-dim) makes surrogate modeling and uncertainty estimation sample-inefficient.

**LFS hypothesis**: within mutation-induced **residue-level representation changes** (site-deltas), a compact, **assay-specific set of directions** makes fitness variation **linearly accessible** from few labeled variants.

⚠️ Scope discipline: this is a **local, supervision-recoverable** statement — it does NOT claim protein fitness landscapes or global PLM geometry are universally linear.

## Method (SGES pipeline)

```
1. Seed: small initial sample of labeled variants (few oracle calls)
2. Site-deltas: compute mutation-induced residue-level PLM representation changes
   Δh_i = h_i(mutant) - h_i(wildtype)   for mutated positions
3. LFS estimation: recover compact assay-specific subspace B from labeled
   site-deltas via regression (fitness ~ linear in projected deltas)
4. Surrogate + uncertainty: fit GP/regressor INSIDE subspace B (low-dim)
5. Acquisition: select next variants by optimistic/UCB-style rule in B
6. Loop: query oracle → update B, surrogate → repeat until budget exhausted
```

**Key design choice — fitness-aligned site-delta coordinates**: controlled comparisons against PCA, random projections, label-shuffled PLS (partial least squares), and classical mutation features show the benefit comes specifically from the fitness-aligned site-delta coordinate, not merely from any dimensionality reduction.

## Evidence & Results

| Benchmark | Result |
|-----------|--------|
| 10 core ProteinGym assays | SGES improves fitness prediction over zero-shot PLMs |
| 87 extended static-validation assays | consistent gains across diverse assays |
| 18-assay budgeted-search evaluation | better search efficiency vs recent ML-guided baselines |
| Controlled ablations | PCA / random proj / label-shuffled PLS / classical features all underperform → LFS-specific benefit |

## Reusable Patterns

### Pattern 1: Local Linearity from Residue Deltas
When a global model is nonlinear but task-relevant variation concentrates in a low-dim subspace of **change vectors** (not absolute embeddings), recover that subspace with few labels. Generalizes beyond proteins: applies to any PLM/LFM-guided optimization where mutation = localized perturbation.

### Pattern 2: Budget-Aware Subspace Search Loop
`estimate subspace → surrogate in subspace → acquisition → oracle query → re-estimate`. The subspace shrinks the hypothesis space so each label does double duty (fits surrogate AND sharpens subspace estimate).

### Pattern 3: Misalignment Correction via Few Labels
Zero-shot scores drift from assays; a compact supervised readout on top of the same backbone corrects misalignment at ~O(labels × dim) cost instead of fine-tuning the whole backbone.

## When to Use / Not Use

**Use when:**
- Optimizing biological sequences (protein, peptide, promoter) with expensive assays
- Oracle budget: 10²–10³ evaluations
- PLM available but zero-shot scores misaligned with the target metric
- Need uncertainty-aware exploration (avoid wasting oracle calls)

**Do not use when:**
- Fully linear global relationship already known (use direct regression)
- Zero labels available (subspace unrecoverable — fall back to zero-shot + diversity)
- Oracle is cheap (brute-force or massive parallel screening is simpler)

## Implementation Notes

- Backbone PLM: ESM-2 class models are sufficient; site-deltas only need mutated residues' hidden states.
- Subspace dim: small (rank of B ≈ # labeled variants upper bound); regularize to avoid overfit.
- Acquisition: UCB or expected-improvement inside subspace; both work, UCB more robust early.
- Negative control to always run: **label-shuffled PLS** — if it matches SGES, the subspace is spurious.

## Related Skills

- `quantum-biomedicine-mechanisms` — quantum approaches to drug mechanisms
- `model-guided-design` patterns — general oracle-bounded design loops

## References

- arXiv:2610.07607 — Linear Fitness Subspace in Protein Language Models Enables Sample-Efficient Directed Evolution
- ProteinGym benchmark suite for fitness prediction validation
