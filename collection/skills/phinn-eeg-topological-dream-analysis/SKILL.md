---
name: phinn-eeg-topological-dream-analysis
description: "Topological time-series (TDA) framework for EEG analysis — sliding-window Takens delay embeddings + Vietoris-Rips filtrations to extract Dynamic Betti Curves, then topology-conditioned flow matching / rectified flow for neural signal synthesis and rare-event (dream-state) detection. Use when analyzing multichannel EEG/EMG time series where spectral-energy features (PSD, catch22) plateau, when building EEG foundation/synthesis models, or when studying dream-state / consciousness / sleep neural signatures. Activation: PHINN-EEG, persistent homology EEG, Betti curve, topological time series, dream EEG, Takens embedding, Vietoris-Rips, topology-conditioned flow, neural signal synthesis."
---

# PHINN-EEG: Topological Time-Series Analysis of EEG

Methodology distilled from arXiv:2607.09662 (Takahashi, Yusuf, Bhaduri, 2026). The core insight: **spectral-energy features (PSD, statistical moments) saturate around AUC≈0.70 for rare neural events; phase-space *geometry* captured by persistent homology breaks past that ceiling (target AUC 0.82–0.90).**

## When to Use This Skill

- EEG/EMG/LFP classification where power-spectral and catch22 baselines underperform.
- Detecting **rare neural events** (dream mentation, microsleep, seizures, pre-awakening signatures).
- Conditional synthesis of physiological signals (data augmentation, BCI simulation, privacy).
- Any multichannel time series where you suspect structure lives in *embedding geometry*, not energy.

## Pipeline (5 stages)

1. **Sliding-window epoching** — Take multichannel pre-awakening (or task) EEG; non-overlapping or hopped windows of length `T` (e.g. 2–10 s at 100–256 Hz). Keep channel × time tensors.
2. **Takens delay embedding** — For each channel window, build delay-coordinate vectors `v_i = [x_i, x_{i+τ}, …, x_{i+(m-1)τ}]` (embedding dimension `m`, delay `τ` from mutual-information / first zero of autocorrelation). This reconstructs the phase-space attractor from a single scalar channel.
3. **Vietoris–Rips filtration + Dynamic Betti Curves** — Stack delay-embedded point clouds across channels/windows; compute VR filtrations over increasing scale `ε`. Track Betti numbers `β₀(ε), β₁(ε), β₂(ε)` → **Dynamic Betti Curves** (Betti value vs ε per window). These are the topological invariants (connected components, loops, voids) that encode geometric architecture.
4. **Topology-conditioned classifier** — Feed Dynamic Betti Curves (or their summary stats: persistent entropy, total persistence, lifecycle moments) into a lightweight NN head. Projected to beat PSD + catch22 on DREAM-style databases.
5. **Topology-conditioned flow synthesis** — Train a rectified-flow / flow-matching model whose conditioning vector is the Betti curve (NOT a spectral summary). Ablate against a spectral-conditioned flow of equal dimensionality to isolate the value of topological conditioning.

## Reference Implementation (Python)

```python
import numpy as np
from functools import partial

# --- Stage 2: Takens embedding (single channel window) ---
def takens_embed(x, m=3, tau=8):
    n = len(x) - (m - 1) * tau
    return np.column_stack([x[i:i + n] for i in range(0, (m - 1) * tau + 1, tau)])

# --- Stage 3: VR filtration Betti curve (ripser-based) ---
# pip install ripser
from ripser import ripser
from persim import plot_diagrams

def betti_curve(pointcloud, maxdim=2, n_eps=50, eps_max=None):
    dgms = ripser(pointcloud, maxdim=maxdim)['dgms']
    if eps_max is None:
        all_f = np.concatenate([d[:,1] for d in dgms if len(d)])
        eps_max = np.nanmax(all_f)
    eps = np.linspace(0, eps_max, n_eps)
    curves = []
    for d in dgms:
        if len(d) == 0:
            curves.append(np.zeros(n_eps)); continue
        birth, death = d[:,0], d[:,1]
        death = np.where(np.isinf(death), eps_max, death)
        # Betti_k(eps) = # features alive at scale eps
        betti = np.array([((birth <= e) & (death > e)).sum() for e in eps])
        curves.append(betti)
    return np.stack(curves)  # (maxdim+1, n_eps)

# --- Stage 4: conditioning vector ---
def topology_conditioning(window, m=3, tau=8, n_eps=50):
    curves = []
    for ch in range(window.shape[0]):
        pc = takens_embed(window[ch], m, tau)
        curves.append(betti_curve(pc, n_eps=n_eps))
    return np.concatenate(curves, axis=1)  # (maxdim+1, n_eps * n_channels)
```

## Key Design Decisions / Pitfalls

- **Window length matters**: too short → noisy point clouds; too long → topological averaging erases transient events. Tune `T` to the event timescale.
- **Embedding params**: `m` and `τ` are not free — estimate per dataset. Bad `τ` collapses the attractor.
- **Dynamic** Betti curves (per window) > static (per recording) — preserves temporal localization needed for rare-event detection.
- **Ablation discipline**: always compare topology-conditioned vs spectral-conditioned flow at *equal feature dimensionality*; otherwise you confound conditioning quality with capacity.
- **Baselines to beat**: PSD (Welch), catch22, masked-reconstruction EEG foundation models. PHINN targets AUC 0.82–0.90 vs ~0.70.
- **Dataset**: DREAM database (3,191 awakenings, 263 participants, 20 labs) is the canonical benchmark; 1,462-awakening open-access subset.

## Extensions

- Replace VR with **alpha-complex / witness complexes** for large point clouds (ripser scales poorly past ~2k points — subsample or use greedy landmarks).
- Betti **transition archetypes**: candidate topological "signatures" linked to phenomenological report categories — useful as a hypothesis-generation space, not a classifier.
- Apply to seizure onset, anesthesia depth, or motor-imagery geometry where spectral features plateau.

## References

- arXiv:2607.09662 — PHINN-EEG (primary source)
- Wong et al. 2025, Nature Communications — DREAM database, SOTA PSD baseline (AUC≈0.70)
- ripser / persim — VR filtration + persistence-diagram tooling
- Takens 1981 — delay-embedding theorem
