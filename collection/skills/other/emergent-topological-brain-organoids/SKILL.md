---
name: emergent-topological-brain-organoids
description: "Apply persistent homology to MEA recordings of spontaneous brain-organoid activity. Detects H1 loops and H2 voids in correlation networks, compares them to rate-preserving null models, and identifies non-redundant loop-carrying cores."
metadata:
  arxiv_id: "2607.16517"
  published: "2026-07-21"
  authors: "Eve Bodnia, Margaux Basart, Sofie Hai, Lenzie Ford, Nina Miolane, Kenneth S. Kosik, Dirk Bouwmeester, Lincoln D. Carr"
  tags: [neuroscience, brain-organoid, persistent-homology, topological-data-analysis, MEA, neural-dynamics, correlation-network]
license: Complete terms in LICENSE.txt
---

# Emergent Topological Structure in Brain-Organoid Activity

Apply persistent homology (Vietoris–Rips filtration) to microelectrode-array (MEA) recordings of spontaneous activity from human and mouse cortical organoids, to detect loops (H1) and voids (H2) that exceed a rate- and population-preserving null model.

## When to Use

- Analyzing spontaneous multi-unit spike recordings from organoids, slices, or dense in-vivo arrays.
- You want to test whether correlation networks carry structured topology beyond firing rate and population bursting.
- You need to identify the non-redundant core of units that carry topological features.
- You want to know how many nodes are required for persistent homology to resolve H1 and H2.

## Core Methodology

### 1. Build the Correlation Network

- Spike-sort MEA data; use sorted single units as network nodes.
- Gaussian-smooth spike trains with a 50 ms kernel.
- For each pair of units (a, b), compute the maximum normalized cross-correlation over a short lag window (0, 10, or 20 ms):

  C(a, b) = max_j  ( Σ_i a_i b_{i+j} ) / ( sqrt(Σ_i a_i²) * sqrt(Σ_i b²) )

- Convert to a dissimilarity: d_ij = 1 - C_ij.

### 2. Vietoris–Rips Filtration and Persistent Homology

- Build a Vietoris–Rips filtration on d_ij using Ripser (or similar).
- Report density-indexed Betti curves β0(ρ), β1(ρ), β2(ρ), where ρ is edge density.
- Integrate Betti curves (e.g., ∫β1(ρ)dρ) for a threshold-free summary.

### 3. Rate- and Population-Preserving Null Model

- Generate raster-marginals surrogates: preserve every unit’s total spike count and every time bin’s total population activity, while destroying higher-order co-firing.
- Use 10^5 binary swaps per surrogate; create ~100 surrogates.
- Recompute correlations and topology on each surrogate.
- Compare integrated β1 / β2 from data to the surrogate distribution; report empirical rank p-values.

### 4. Identify Non-Redundant Core

- Compute H1 cocycle representatives for the persistent loops.
- Randomly remove 10% of units and recompute topology (average over 100 trials).
- Targeted removal: remove the 10% of units most frequently appearing in H1 cocycle representatives.
- Compare retained integrated β1 and bottleneck distance between original and post-removal persistence diagrams.

### 5. Size-Scaling Analysis

- Repeat for networks with varying N (e.g., subsample units).
- H1 becomes resolvable above roughly N ≈ 100 in the organoid datasets.
- H2 emerges significantly only in larger networks (N ≥ 119 in the reported data).

## Key Findings

- H1 loops exceeded the null in 14 of 18 organoid datasets (p ≤ 0.05).
- Loops peak at low edge density (ρ ≲ 0.15) and are carried by strongly co-active units, not weak correlations.
- Random 10% removal retained 92.5% of integrated β1; targeted removal retained 72.6% and produced larger bottleneck distances (median ratio 1.48 vs random).
- H2 voids appeared in 6 datasets, all with N ≥ 119, suggesting larger recordings are needed to resolve higher-order structure robustly.
- Loop structure reflects co-firing, not electrode layout; geometry is topologically trivial in the datasets tested.

## Practical Workflow

1. Load spike-sorted MEA data; create spike trains and quality-control units.
2. Gaussian-smooth with 50 ms kernel; compute pairwise maximum cross-correlation at 0–20 ms lags.
3. Build correlation distance matrix d = 1 - C.
4. Run Ripser on d; obtain persistence diagrams and Betti curves indexed by density.
5. Generate 100 raster-marginals surrogates; compute null distribution of integrated β1 and β2.
6. Report p-values and z-scores for data vs null.
7. (Optional) Compute cocycle representatives and test robustness to random vs targeted node removal.
8. (Optional) Subsample units to estimate topology-resolvable node count.

## Parameters and Defaults

| Parameter | Default | Notes |
|-----------|---------|-------|
| Smoothing kernel | 50 ms Gaussian | Matches tens-of-ms synaptic timescale |
| Lag window | 0 ms (also 10, 20 ms) | Zero lag is symmetric for undirected VR |
| Surrogate swaps | 10^5 per surrogate | Sufficient for destroying higher-order co-firing |
| Surrogate count | 100 | For empirical null distribution |
| Removal fraction | 10% | For robustness / core analysis |
| Density range | ρ ∈ [0, 1] | Threshold-free comparison |

## Pitfalls

- **Small N**: networks below ~50 units may not resolve H1 above surrogate noise; report this as an insufficiency rather than absence of structure.
- **Smoothing too wide or narrow**: a kernel far from the synaptic timescale can suppress or distort co-firing structure.
- **Using Erdős–Rényi as null**: this only tests structure against random connectivity, not against rate/population effects. Use raster-marginals surrogates.
- **Directed vs undirected**: undirected VR is symmetric; for firing-order information, use directed flag complexes separately.
- **Loop count alone is misleading**: a hub deletion can create new loops. Use bottleneck distance to measure topological disruption.

## Activation Keywords

- brain organoid topology
- persistent homology neural recordings
- MEA correlation network loops
- H1 H2 neural topology
- rate-preserving null model
- loop-carrying core
- topological data analysis neuroscience

## References

- Giusti, Pastalkova, Curto, Itskov (2015). Clique topology reveals intrinsic geometric structure in neural correlations. *PNAS*.
- Schreiber et al. (2003). A new correlation-based measure of spike timing reliability. *Neurocomputing*.
- Okun et al. (2012). Diverse coupling of neurons to populations in sensory cortex. *Nature*.
- Ripser: https://ripser.scikit-tda.org
- Lancaster & Pasca organoid protocols (see paper references).
