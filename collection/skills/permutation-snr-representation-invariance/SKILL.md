---
name: permutation-snr-representation-invariance
description: Use when probing why models fail equivalent problems or analyzing internal representations of reasoning. Permutation SNR metric distinguishing answer invariance from representation invariance; higher SNR correlates with accuracy on reordered problems.
trigger: permutation SNR, answer invariance vs representation invariance, rule order sensitivity, mathematical reasoning representations, equivalence class probing, SNR rank correlation accuracy, multi-step function composition
category: ai_collection
---

# Permutation SNR: Answer Invariance ≠ Representation Invariance

**Source**: arXiv:2609.28442v1 (2026-09-23) — Zhixu Silvia Tao.

## The Question

Reordering a set of mathematical rules without changing meaning should preserve the correct answer — but must the model's **internal representations** stay invariant too?

## Setup

- Synthetic multi-step **function-composition problems**, each presented under **multiple rule orderings** with the same correct answer.
- Measures: accuracy + **permutation signal-to-noise ratio (SNR)** = how distinctly ordering patterns are represented relative to variation across problem instances.
- 16 language models, 1B–8B parameters.

## Core Finding

**Models that solve reordered problems more accurately represent different rule orderings MORE distinctly** — not less.

- Layer-averaged permutation SNR is **positively rank-correlated with accuracy in every synthetic setting**, Spearman ρ up to **0.86**.
- Successful mathematical rule composition can accompany **distinct internal representations between equivalent rule orderings** — answer invariance does NOT require representation invariance.

## Conceptual Distinction

- **Answer invariance**: correct output under semantic equivalence transformations.
- **Representation invariance**: identical internal states under those transformations.
- These come apart: high performers keep *order information* in representations even when the answer is order-invariant. Distinct encoding of the permutation is not noise — it appears functional.

## Usage

1. **Diagnostic probe**: for reasoning models, compute permutation SNR across equivalent problem presentations; low SNR with low accuracy suggests the model collapses equivalent structures too early (loses track of the actual computation order).
2. **Model selection beyond accuracy**: SNR adds a representational axis — useful when accuracies are similar but robustness to reformulation differs.
3. **Data augmentation rationale**: rule-ordering augmentation is not just regularization; it shapes whether representations encode order distinctly.

## Implementation Sketch

```
# For each problem instance p and ordering π:
h(p, π) = layer-averaged hidden state (or per-layer)
# Between-ordering variance (signal): Var_π[h(p,π)] per instance
# Between-instance variance (noise): Var_p[h(p,π̄)]
SNR = E_p[Var_π h] / (E_{p,π} Var within equivalence structure)
# Rank-correlate layer-averaged SNR with accuracy across models
```

## Related Skills

- `trajectory-geometry-transformer-representations` — representation geometry analysis
- `stimulus-symmetries-rsm-confound` — symmetry confounds in representations
- `same-brain-different-prediction` — reliability/consistency analysis
