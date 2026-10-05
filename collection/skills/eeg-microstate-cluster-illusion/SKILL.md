---
name: eeg-microstate-cluster-illusion
description: Use when analyzing EEG microstates or validating cluster numbers. TDA shows GFP peaks form one connected structure, not clusters.
category: ai_collection
---

# EEG Microstate Cluster Illusion (Meta-Criterion Falsification)

**Paper**: "Clustering without clusters: the meta-criterion and centroid reliability mistake continuous dynamics for discrete states" — von Wegner & Hermann (UNSW / Kiel), arXiv:2610.02220, q-bio.NC, Sep 2026.

## Core Thesis

The two standard arguments for discrete EEG microstates are both falsifiable artifacts of the clustering pipeline itself:
1. **A1 (centroid reproducibility)**: K-means centroids land in highly reproducible attractor regions **even on single connected structures** — reproducibility ≠ clusters.
2. **A2 (meta-criterion peak)**: The Cartool 7-criterion meta-criterion reports spurious optimal K\*=4–8 with high confidence on attractors that provably contain **no clusters**.

**Implication**: Resting-state EEG GFP-peak data form a **single connected structure** in sensor space. "Optimal microstate number" may be an ill-posed question; microstate segmentation is better justified as **symbolic dynamics** (partitioning a continuum), not as recovering discrete ground-truth states.

## Validation Methodology (the reusable part)

### 1. Negative-control dynamical systems (known non-clustered geometry)
Run the full microstate pipeline on four systems whose attractors are known to be single connected structures:
- **Lorenz** (σ=10, ρ=28, β=8/3; two-lobe butterfly): dt=0.01, tmax=100, discard t<5
- **Rössler** (a=0.2, b=0.2, c=5.7; single-lobe spiral): dt=0.1, tmax=600, discard t<100
- **Hindmarsh-Rose** (a=1,b=3,c=1,d=5,r=0.005,s=4,x_rest=−1.6,I=3.25; chaotic bursting): dt=1.0, tmax=5000
- **Wilson-Cowan E/I** (c1=16,c2=12,c3=15,c4=3, sigmoid gains 1.3/2, θ 4/3.7, P=1.25; limit cycle ring): dt=0.05, tmax=250
- Integrate with RK45 (rtol=atol=1e−9), discard transients, N=50 random-init realizations.

**Finding**: meta-criterion peak lands at K\*=4–8 for ALL four systems → the "magic four microstates" can be produced by any continuous attractor.

### 2. Meta-criterion implementation details (Cartool version)
- 7 criteria: Davies-Bouldin, DB robust derivative (on rank-transformed curve), modified Krzanowski-Lai, Point-Biserial, PB robust derivative, Silhouettes, Silhouette derivative.
- Each criterion direction-corrected → rank-transformed (dense rank, k≥4 floor applied per-criterion) → per-criterion argmax k\* → **K\* = round(median of 7 peaks)**.
- EEG distance is polarity-invariant: d(u,v) = 2(1−|r|) on average-referenced topographies.
- Pairwise-matrix criteria computed on one fixed 600-point subsample reused across all k.

### 3. Centroid reproducibility null test
- Statistic: mean cross-run nearest-neighbor distance of pooled centroids (K-means fit once per realization).
- Null: 2,000 resamples drawing K points uniformly from the SAME attractor trajectories (critical — attractors occupy tiny lower-dimensional volumes).
- Result: strong negative z-scores (centroids non-random) on every system → reproducibility argument is uninformative about cluster existence.

### 4. Topological data analysis (the decisive test)
- **HDBSCAN** with min-cluster-size sweep (0.25–12% of n), cluster-selection ε = 0.35 × median pairwise distance (prevents splitting near-1D manifolds). Can return K=1 or K=0.
- **Persistent homology H0** via Vietoris-Rips (ripser.py), n=800 subsamples: count connected components β0(ε) vs threshold.
- **Signature of true clusters**: β0 plateau at K across a range of ε. **Signature of a continuum**: monotone smooth decay, no plateau.
- Applied to LEMON dataset (203 subjects, 61-ch, 2–20 Hz, eyes-closed, 8.4k–13.7k GFP peaks/subject): HDBSCAN → single cluster, 0% noise; H0 → smooth decay. EEG behaves exactly like the non-clustered attractors.
- **Sanity controls**: (a) single HDBSCAN cluster centroid back-projected to sensor space = alpha-band topography / microstate C (neurophysiologically meaningful); (b) synthetic 61-dim Gaussian blobs (K=4–8) are correctly recovered with plateaus → the TDA instruments work.

## Practical Guidance for Microstate Studies

1. **Do not treat the meta-criterion K\* as ground truth**; it lacks a statistical model, p-value, and external validity. Report cluster-count sensitivity across K rather than a single optimum.
2. Reproducible centroids are expected from ANY continuous attractor — never cite centroid stability alone as evidence of discrete states.
3. Before clustering, run the HDBSCAN sweep + H0 persistence curve on GFP-peak data. A β0 plateau justifies discrete-state modeling; smooth decay supports a continuum interpretation.
4. If data are a continuum, frame microstate analysis as **symbolic dynamics** (Daw et al 2003): partitioning is a measurement choice, state counts are scale-dependent, and syntax statistics remain interpretable.
5. Negative-control pipeline (run microstate tooling on Lorenz/Rössler) is a cheap falsification harness for ANY new cluster-number criterion.

## Key Numbers

| System | Meta-criterion K\* | HDBSCAN | H0 shape |
|---|---|---|---|
| Lorenz / Rössler / Hindmarsh-Rose / Wilson-Cowan | spurious 4–8 peak | 1 cluster (+noise) | smooth decay |
| LEMON resting EEG (203 subj) | K\*=5 | 1 cluster, 0% noise | smooth decay |
| Synthetic Gaussian blobs K=4–8 | (fails on 2017 version: 10–12) | correct K, 0% noise | plateau at K |

## Related

- Complements [[atoms-of-thought-eeg-microstates]], [[eeg-microstate-tokenizer-representation]], [[eeg-microstate-variational-embedding]] — those build models assuming discrete states; this skill supplies the falsification test that should precede them.
- Symbolic-dynamics framing aligns with [[neutral-theory-neural-dynamics]] (scale-free without criticality) and manifold-flow views ([[platonic-representations-brain]] Fousek symmetry-breaking manifold).
