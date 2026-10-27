---
name: phase-edge-centric-coupling-eeg
description: Use when building edge-centric EEG nets via phase coupling.
category: ai_collection
trigger: EEG edge-centric connectivity, edge-to-edge coupling, phase synchronization network, overlapping brain communities, edge time series, link communities, differential identifiability, inter-brain hyperscanning
---

# Phase-based Edge-centric Coupling (PEC) for EEG Networks

**Source**: arXiv 2610.32286 — Wu, Shi, Xu, Tong, Guo (Shanghai Jiao Tong Univ., IEEE journal submission, Oct 2026). Code: `github.com/JAWu600/Phase-based-Edge-centricCoupling`.

## What it solves

Node-centric EEG connectivity (e.g., PLV matrices + node community detection) forces **hard-partitioned** modules and cannot represent **edge-to-edge (higher-order) interactions**. The edge-centric paradigm (Faskowitz/Betzel eFC, Ahn link communities) existed for DTI/fMRI only — PEC is the first EEG edge-centric method: it builds edge time series from **instantaneous phase differences** and quantifies edge-to-edge coupling with a complex normalized inner product, yielding overlapping functional modules, connector hubs, and cross-brain (hyperscanning) modules.

## Core algorithm

1. **Narrowband filter + Hilbert transform** per channel → instantaneous phases φ_i(t).
2. **Edge time series** (unit-modulus complex signal):
   `ε_ij(t) = exp(i·(φ_i(t) − φ_j(t)))` — the pointwise PLV integrand promoted to the fundamental dynamical unit.
3. **Edge-to-edge coupling** via normalized inner product (NIP), the complex analogue of cosine similarity:
   `NIP(ε_a, ε_b) = |Σ_t ε_a(t)·conj(ε_b(t))| / (‖ε_a‖·‖ε_b‖)` — since |ε|=1 this equals `|(1/N)·Σ_t ε_a(t)·conj(ε_b(t))|`, i.e. **PLV computed between edge series**.
4. **Undirected edges need two orientations**: same-direction `NIP(ε_ij, ε_kl)` (co-fluctuation of phase differences) vs crossed `NIP(ε_ij, ε_lk)` (mirror/anti-phase alignment, i.e. coupling of (i,l),(j,k)). Define
   `PEC((i,j),(k,l)) = max{ NIP(ε_ij, ε_kl), NIP(ε_ij, ε_lk) }`, range [0,1].
   (True identities: NIP(ε_ij,ε_kl)=NIP(ε_ji,ε_lk) and NIP(ε_ij,ε_lk)=NIP(ε_ji,ε_kl) — swapping both edges is the conjugate; swapping ONE edge gives a genuinely different quantity, so the max is substantive, verified numerically: 0.704 vs 0.386 in a controlled sim.)
5. **Community detection**: average trial-level PEC matrices → proportional threshold (keep top 20%, optimal band 10–30%) → Leiden on the edge network → edge (link) communities → **project edges onto nodes** (each node joins every community containing its edges) to get **overlapping** node modules. Connector hubs = nodes shared across ≥2 modules.
6. **Inter-brain (dual-EEG)**: PEC between all mother-edge × child-edge pairs → bipartite edge network → **BRIM** bipartite modularity → cross-brain modules (symmetric co-activation vs complementary role-specific modules).

## Ground-truth simulation design (reusable)

Generate edge pairs with controlled coupling: pick real EEG phases φ_i, φ_j; inject von Mises phase noise η(t) ~ VonMises(0, κ): `φ_k = φ_i + η/2, φ_l = φ_j − η/2` ⇒ `ε_kl = ε_ij · exp(i·η)`. The expected coupling is exactly **λ = I₁(κ)/I₀(κ)** (modified Bessel ratio = mean resultant length of von Mises). Numerically verified: |E[exp(iη)]| matches I₁/I₀ to ~1e-3 (MC error); PEC estimator reproduces λ with the expected small upward finite-sample bias of |mean| estimators. Negative controls: shuffle reference-target pairing for spurious-coupling AUROC analysis (threshold = p-th percentile of null distribution, FPR = 1−p).

## Data-length requirement (the key pitfall)

- PEC **needs ≥16 oscillatory cycles** (≥1600 ms in alpha for superiority; ≥8000 ms for AUROC>0.7 even at λ=0.02). Below ~1200 ms it is significantly **WORSE** than node-centric PLV: pointwise phase differentiation yields truncated high-variance edge series, whereas PLV's temporal averaging acts as smoothing (needs only ~3 cycles).
- Accuracy: <10% relative error across δ/θ/α/β bands, SNR≥5 dB; AUROC>0.7 for λ≥0.1; >0.9 for λ≥0.2 (≥1 s).

## Identifiability evaluation recipe (differential identifiability, Amico & Goñi)

- Per-trial PEC (or PLV) upper-triangle vectors → Pearson corr of all pairs → within-subject mean I_within vs between-subject mean I_between → `Idiff = (I_within − I_between) × 100`.
- Bootstrap 1000× (30% subjects, with replacement) + paired t-tests for significance.
- **PCA denoising**: concatenate matrices, reconstruct with top-k PCs; identifiability peaks when **#PCs = #subjects** (top PCs encode subject-specific signatures). PEC keeps its advantage at every reconstruction level.
- 1-NN identification accuracy as the operational metric.
- Anchors (41 mothers, dual-EEG tangram task, alpha): PEC Idiff 14.97 vs PNC 13.68 (d=0.65); PCA peak 21.60 vs 14.63; 1-NN 83.3% vs 78.4%; cognitive-state (acting vs observing) Idiff 0.23 vs 0.15, 1-NN 85.3% vs 78.5%.

## Interpretation patterns

- Overlapping modules map onto Yeo-type systems (SMN+FPCN integration, medial-frontal limbic, SMN+VN dorsal-stream, bilateral FPCN) — hard partitions split these into hemispheric fragments and miss FPCN entirely.
- Connector hubs: SMN electrodes shared between motor-planning and visual-motor modules; FPCN shared between integration and control modules.
- Inter-brain: symmetric modules (IoU≈0.7, shared posterior visual/motor-imagery) encode shared stimulus processing; asymmetric modules (IoU<0.09, child-posterior↔mother-anterior and vice versa) encode complementary actor/observer roles.

## Complexity & limitations

- Edges scale O(N²), edge pairs O(N⁴) — storage/compute burden at source level; unsuitable for real-time or brief event-related windows.
- Phase-only coupling (no amplitude co-modulation); extend by swapping the edge-series construction to amplitude envelopes.
- Sensor-level: community→Yeo mapping is scalp projection, not source localization (volume conduction — consider empty-room/orthogonal rebuilds before source-level use).

## Implementation sketch

```python
import numpy as np
from scipy.signal import hilbert

def pec_matrix(X, band=None):
    # X: (n_ch, n_times) narrowband-filtered EEG
    ph = np.angle(hilbert(X, axis=-1))            # (n_ch, T)
    n = ph.shape[0]
    tri = [(i, j) for i in range(n) for j in range(i+1, n)]
    E = np.array([np.exp(1j*(ph[i]-ph[j])) for i, j in tri])  # (n_edges, T)
    # same-direction: |mean(E_a * conj(E_b))|; crossed: |mean(E_a * E_b)|
    G_same = np.abs(E @ E.conj().T) / E.shape[1]
    G_cross = np.abs(E @ E.T) / E.shape[1]
    PEC = np.maximum(G_same, G_cross)
    return PEC, tri   # Leiden on PEC (keep top 20%) -> link communities
```

## Related skills
- `functional-connectome-fingerprint` — differential identifiability framework PEC builds on
- `topological-effective-connectivity-hodge` — complementary directed-flow decomposition of brain networks
- `eeg-brain-connectivity-bci` — connectivity-based BCI context
- `hypergraph-functional-brain-network` — alternative higher-order network view
