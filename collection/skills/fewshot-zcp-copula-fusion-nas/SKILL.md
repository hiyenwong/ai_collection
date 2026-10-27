---
name: fewshot-zcp-copula-fusion-nas
description: Fuse weak zero-cost NAS proxies into robust few-shot rankings via CAST copula alignment. Use when ranking models/candidates from noisy training-free signals.
category: ai_collection
---

# FENAS: Few-Shot Meta-Ensembling of Zero-Cost Proxies via CAST (Copula Alignment + Synergy Transformation)

**Paper**: "FENAS: A Few-Shot Meta-Ensembling Framework for Efficient Neural Architecture Search with Synergized Zero-Cost Proxies" — Yifeng Mao, Yuze Feng, Yutong Shen, Liyang Gao, Zhixiang He (Beijing University of Technology), arXiv:2610.15307 (11 Oct 2026).

## Core Idea

Individual zero-cost proxies (ZCPs) are cheap but unreliable — each captures only one physical property of an architecture (expressivity, trainability, connectivity, capacity), and rankings swing wildly across datasets/search spaces. Topology-aware GNN predictors are more accurate but need many labeled architectures, graph encoders, and costly representation learning. FENAS's insight: **don't spend model capacity on topology learning; instead model the intrinsic physical priors directly and learn only how to combine them with minimal supervision**. A tiny feature-engineering pipeline (CAST) + a shallow meta-learner (linear regression / random forest / XGBoost) beats GCN/Transformer predictors at ≤1% labels.

## The CAST Pipeline (reusable core)

**Step 1 — Extract 4 complementary scalar proxies per candidate** (one forward/backward pass each, at initialization):

| Dimension | Proxy | Formula |
|-----------|-------|---------|
| Expressivity z_E | NASWOT | z_E = log det(K + εI), K = binarized activation kernel matrix |
| Trainability z_T | Fisher trace | z_T = Σ_{w∈α} ‖∇_w L‖² |
| Connectivity z_C | SynFlow | z_C = Σ_{w∈α} |w| ⊙ ∂R/∂w (data-free path integral) |
| Capacity z_P | #Params | z_P = Σ_l |w_l| |

**Step 2 — Copula Alignment via ECDF (the key trick):** raw proxy scores live on incommensurable scales. Map each feature to its percentile rank against a reference set A_ref of candidates:

```
u_k = F̂_k(v_k) = (1/|A_ref|) Σ_{α'∈A_ref} I(v_k(α') ≤ v_k)
```

This is the empirical copula transform — after it, all 4 features live on [0,1] with margin-free (rank) semantics. It alone lifts linear-regression ranking from τ=0.491 → 0.545 on NAS-Bench-201 CIFAR-10.

**Step 3 — Synergy Transformation (2 high-order features):**
- Efficiency: p_E = u_E / log(1 + u_P) — expressivity per unit capacity
- Synergy: p_S = u_T × u_C — joint trainability×connectivity effect

Final feature vector: Φ(α) = [u_E, u_T, u_C, u_P, p_E, p_S] ∈ R^6.

**Step 4 — Meta-predictor on 6 features:** any off-the-shelf regressor (default: Random Forest / XGBoost; linear also works). Point-wise MSE loss. Train on 78–500 labeled candidates, rank the whole space. No graph construction, no message passing, no pretraining.

## Key Results

- NAS-Bench-201 CIFAR-10: τ=0.695 with only 78 labels (0.5%) vs DCL-ENAS 0.610, CAP 0.600 — +13.9%/+15.8% over topology-based few-shot predictors. τ=0.731 at 1%.
- NAS-Bench-101 (diverse topology): τ=0.616 at 0.02% labels (100 archs) — still beats Arch2Vec (0.435) and TNASP (0.600); PINAT wins at higher budgets (0.679 vs 0.641 at 0.04%).
- vs individual ZCPs: Fisher alone τ=−0.190 on NB101 (worse than random); FENAS fuses it to 0.658. On NB201-C10: ρ=0.907.
- End-to-end: NAS-Bench-201 full-space ranking in ~1138 s (vs ~3800–12000 s for baselines); 94.08% test (optimum 94.37%). DARTS space: 0.3 GPU days → 97.25%±0.09 after 600-epoch retrain (comparable to PINAT 97.33 but no graph pretraining).
- Inference: ~166.7 ms/arch, topology-agnostic, ~0.3% labels sufficient.

## Why It Works (mechanistic evidence)

1. **Proxy complementarity**: off-diagonal Kendall correlations among the 4 proxies are low-to-moderate (Fisher×NASWOT ≈ 0.018; SynFlow×NASWOT ≈ 0.37) — they genuinely capture different physics, so fusion has information to add.
2. **Cumulative ablation**: τ rises monotonically z_T (0.598) → +z_E (0.604) → +z_C (0.656) → +z_P (0.731) on CIFAR-10.
3. **Task-adaptive weighting (SHAP)**: the meta-learner shifts dominant feature across datasets — p_S dominates on CIFAR-100, NASWOT on ImageNet16-120 — explaining cross-dataset robustness without re-engineering.
4. **CAST ablation** (1% labels, CIFAR-10): raw→ECDF→synergy→full lifts LR τ 0.491→0.545→0.560; RF gains are smaller (0.718→0.731) — CAST is a *linear-learner rescue* mechanism; tree ensembles partially learn the transform themselves.

## Reusable Methodology (beyond NAS)

The pattern **"ECDF-align heterogeneous weak signals → add designed interaction features → shallow meta-learner"** applies wherever you must rank candidates from multiple noisy, differently-scaled, training-free metrics:

1. **Hypothesis/model screening** (e.g., research-idea triage from cheap proxy scores).
2. **Hyperparameter/candidate pre-ranking** before expensive evaluation.
3. **Any few-shot regression on tabular features** where scales are incomparable — the empirical-copula transform is free, deterministic, and leak-safe when A_ref is the unlabeled candidate pool itself (transductive: rank is relative to the pool, which is exactly what ranking needs).
4. Ensemble design: when individual weak rankers disagree (low τ among them), fusion via percentile alignment + interactions beats any single ranker; when they agree, fusion is neutral — check inter-proxy correlation first.

**Pitfalls**: (a) ECDF ranks are pool-relative — a candidate's feature changes if the reference pool changes; keep A_ref fixed or include all evaluation candidates. (b) The synergy features (p_E, p_S) are hand-designed for NAS; re-derive domain-appropriate interactions rather than copying them. (c) On structurally diverse spaces (NB101), topology-aware predictors still win at higher label budgets — know when the topology-free shortcut stops paying. (d) DARTS-style searches need a structural-validity constraint (skip-op collapse) before proxy-based selection.

## Implementation Sketch

```python
import numpy as np
from sklearn.ensemble import RandomForestRegressor

def cast_features(raw, ref):  # raw, ref: (n, 4) arrays of [zE, zT, zC, zP]
    U = np.stack([np.searchsorted(np.sort(ref[:, k]), raw[:, k]) / len(ref)
                  for k in range(4)], axis=1)          # ECDF alignment
    pE = U[:, 0] / np.log1p(U[:, 3])                     # efficiency
    pS = U[:, 1] * U[:, 2]                               # synergy
    return np.hstack([U, pE[:, None], pS[:, None]])      # (n, 6)

def rank_candidates(candidates, labeled, scores):
    X_all = cast_features(candidates, candidates)        # transductive ECDF
    idx = np.arange(len(candidates))
    lab_mask = np.zeros(len(candidates), bool); lab_mask[labeled] = True
    rf = RandomForestRegressor().fit(X_all[lab_mask], scores)
    return np.argsort(-rf.predict(X_all))
```

## Related Skills

- `ml-benchmark-factor-analysis` — psychometric view of weak benchmark signals
- `backtest-live-parity-defects` — another "cheap proxy vs ground truth validity" audit pattern

**Source**: [arXiv:2610.15307](https://arxiv.org/abs/2610.15307)
