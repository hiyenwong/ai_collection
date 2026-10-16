---
name: vqc-entanglement-structure-audit
description: Audit VQC entanglement structure vs clinical performance.
---

# VQC Entanglement Structure Audit for Medical Classification

**Source**: arXiv:2609.34617 (Hazmoun, Sakhi, Bennai — Hassan II Univ. Casablanca, 2026-09-28)
Benchmark: Wisconsin Diagnostic Breast Cancer (WDBC), 3-qubit VQC, noiseless statevector.

## Core Question

Does the *entangling structure* of a variational quantum classifier (VQC) causally
improve medical classification — or is any observed gain confounded with circuit
expressivity/depth? This skill is a **controlled audit protocol** answering that
question honestly, without over-claiming quantum advantage.

## Controlled Entanglement Ladder (the key design)

Hold EVERYTHING fixed except entangling structure:
- Same EfficientSU2 ansatz, COBYLA optimizer (150 iters), stratified 5-fold CV,
  same PCA→3-components encoding (1 qubit per component), same SMOTE (train-fold only),
  same seed protocol.
- Vary ONLY the feature-map entangling topology in a 3-step ladder:

| Config | Feature map | Connectivity | Reps | Mean EE | Mean Conc | Acc | F1 |
|--------|------------|--------------|------|---------|-----------|-----|-----|
| A | Ising ZZ | linear nearest-neighbor | 1 | 0.4026 | 0.2054 | 92.98% | 0.9032 |
| B | Ising ZZ | linear nearest-neighbor | 2 | 0.6370 | 0.3182 | 93.50% | 0.9092 |
| C | Heisenberg XX+YY+ZZ | all-to-all | 2 | 0.7118 | 0.3224 | 93.68% | 0.9128 |

**Even config A is not zero-entanglement** (its map + ansatz keep one NN ZZ layer);
A is the low end of the ladder, not a separable control.

## Dual Entanglement Metrics (never use just one)

1. **von Neumann entropy** S(ρ_A) = −Tr ρ_A log₂ ρ_A, averaged over ALL single-qubit
   bipartitions of the trained-circuit output state. Captures global multipartite structure.
2. **Wootters concurrence** C(ρ) = max(0, λ₁−λ₂−λ₃−λ₄) with λᵢ = sqrt-eigenvalues of
   ρρ̃, ρ̃ = (σy⊗σy)ρ*(σy⊗σy); average over ALL qubit pairs. Captures pairwise entanglement.

**Divergence is informative**: here entropy kept rising B→C (0.637→0.712) while
concurrence plateaued (0.318→0.322) — the two measures are NOT interchangeable;
a single metric would hide the saturation of pairwise correlations.

Measure on the FULL trained pipeline (feature map + optimized ansatz), on test points.

## Statistical Analysis Protocol

- Report mean ± std over folds for acc/precision/recall/F1/specificity AND EE/Conc.
- **Fold-level correlation** (n = configs × folds = 15): Pearson r between entanglement
  and performance. Here: r(EE, acc)=0.215 (p=0.44), r(Conc, acc)=0.368 (p=0.18) —
  positive but NOT significant. Association ≠ causation.
- State explicitly that fold-level observations are not independent; no multiple-comparison
  correction → p-values are exploratory only.

## Confounding Disclosure Checklist (report ALL of these)

- [ ] Connectivity, interaction type (Ising vs Heisenberg), and depth change TOGETHER —
      entanglement cannot be isolated as the single variable.
- [ ] Entanglement and expressivity are confounded (richer topology ⇒ both rise).
- [ ] Single seed, no seed-averaging; std reflects fold variance only.
- [ ] Noiseless simulator — no hardware-noise transferability claim.
- [ ] One dataset, one qubit count — no generalization claim.

## Clinical Metric Interpretation (medical QML specific)

- VQC configs beat LR/SVM-RBF/RF baselines by ~1.2pp accuracy (93.7% vs 92.3–92.5%)
  — but **this is NOT evidence of quantum advantage** (needs computational,
  statistical, and resource-level controls).
- Trade-off profile matters more than accuracy: VQCs gave higher **specificity/precision**
  (fewer false positives — config B best: spec 0.969), classical models higher **recall**
  (SVM-RBF 0.925). Which config is "best" depends on the clinical cost of
  FN vs FP — never rank on accuracy alone.
- All classical and quantum models must share identical fold-specific preprocessing
  (correlation filter → standardize → PCA → SMOTE inside train fold only) so differences
  cannot come from data preparation.

## Implementation Recipe (Qiskit)

1. Preprocess per fold: Pearson-correlation filter → StandardScaler → PCA(n=3) → SMOTE(train only).
2. ZZ feature map: U_Φ(x) = exp(i Σⱼ x_j Z_j + i Σ_{j<k} (π−x_j)(π−x_k) Z_jZ_k)·H^⊗n;
   choose connectivity ladder (A/B/C above); Heisenberg variant adds XX+YY+ZZ terms.
3. EfficientSU2 ansatz (linear vs full entanglement, reps 1–2) + COBYLA, 150 iters.
4. After training: statevector of full circuit on test samples → reduced density
   matrices per bipartition → entropy; per-pair 2-qubit ρ → concurrence.
5. Log per-fold: all 5 clinical metrics + EE + Conc; then fold-level Pearson analysis.

## Reusable Insights

- **Structure–correlation link is robust**: entangling topology monotonically maps to
  measured EE/Conc (order A<B<C held in all folds) — the circuit-level knob works.
- **Correlation→performance link is weak**: don't claim entanglement causes accuracy;
  the honest result is "association, moderate, not significant at n=15".
- **Richer entangling structure also stabilized training**: config C had the lowest
  fold-to-fold std (±0.0093 acc) — an oft-ignored secondary benefit.
- **Measure both EE and Concurrence** — they saturate at different points of the ladder.
- **For small biomedical datasets** (n≈569), architecture, representation geometry, and
  data variability all co-determine the outcome; report the full confounding picture.

## When to Use

- Auditing any variational/quantum classifier claim that "entanglement helps".
- Designing VQC feature maps for tabular medical data (few features after PCA).
- Reviewing QML-for-medicine papers: demand the ladder + dual metrics + fold-level
  stats + confounding disclosure before accepting performance claims.
