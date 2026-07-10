---
name: multiscale-brain-dynamics-analysis
description: "Unified framework for multi-scale brain dynamics analysis combining criticality scaling, fixed point compositionality, and representation diagnostics. Integrates renormalization group methods, inhibition-dominated network theory, and EEG foundation model audit protocols."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2606.06290,2606.07336,2606.06647"
  published: "2026-06-04 to 2026-06-05"
  authors: "Irem Topal et al., Juliana Londono Alvarez, Jun-You Lin et al."
  tags: ["neuroscience", "brain-dynamics", "criticality", "compositionality", "representation-analysis", "renormalization-group", "EEG", "fMRI"]
---

# Multi-Scale Brain Dynamics Analysis Framework

Unified framework synthesizing three complementary approaches to studying brain dynamics across spatial and representational scales (arXiv:2606.06290, 2606.07336, 2606.06647).

## Synthesis Rationale

These three papers from June 2026 reveal a convergent theme: **brain dynamics must be analyzed at multiple scales simultaneously** — from microscopic network connectivity to macroscopic collective behavior to learned representation structure.

| Scale | Paper | Method | Key Insight |
|-------|-------|--------|-------------|
| **Collective/Macroscopic** | 2606.06290 | PRG + PSD + DFA | Psychosis reorganizes scaling regime, doesn't destroy it |
| **Mesoscopic/Network** | 2606.07336 | Low-rank gluing in TLNs | Structural modularity enables functional compositionality |
| **Representational** | 2606.06647 | FMScope diagnostics | Subject identity is dominant linear axis in EEG FMs |

## Core Components

### 1. Criticality Scaling Analysis (from 2606.06290)

Study how brain activity organizes across scales using statistical physics methods:

- **Phenomenological Renormalization Group (PRG)**: coarse-grain fMRI data iteratively, track (alpha, tau) evolution
- **Power Spectral Density (PSD)**: measure 1/f scaling exponent beta
- **Detrended Fluctuation Analysis (DFA)**: quantify long-range temporal correlations (Hurst exponent)

**Key finding**: Pathological states often show **systematic exponent shifts within preserved scaling regime**, not loss of critical dynamics.

### 2. Fixed Point Compositionality (from 2606.07336)

Understand how structural modularity supports flexible computation:

- **Low-rank gluing rules**: connect inhibition-dominated threshold-linear network modules via specific low-rank couplings
- **Fixed point decomposition**: global attractors constrained to combinations of local module attractors
- **Rank-1 gluing characterization**: complete rules for which local fixed point combinations yield global ones

**Key finding**: Brains generate complex behaviors on stable structure by composing simple reusable primitives through modular assembly.

### 3. Representation Diagnostic Framework (from 2606.06647)

Audit learned neural representations before downstream use:

- **FMScope protocol**: five diagnostics for frozen representations
  1. Variance decomposition (subject vs. label variance)
  2. Subject-axis erasure (remove dominant identity axis)
  3. Aperiodic 1/f ablation (test spectral carrier contribution)
  4. Layer-wise label probing (identify which layers encode what)
  5. Within-subject direction consistency (verify biomarker stability)

**Key finding**: Subject identity variance dominates 13-89x over random null; erasing it improves label decoding by 6-12 pp.

## Unified Analysis Workflow

```
Step 1: Data Collection
  ├── fMRI/EEG time series from patient + control groups
  ├── Network connectivity matrices (functional + structural)
  └── Pretrained model representations (if using ML models)

Step 2: Multi-Scale Characterization
  ├── Macroscopic: PRG coarse-graining + PSD + DFA scaling exponents
  ├── Mesoscopic: network modularity analysis + fixed point decomposition
  └── Representational: variance decomposition + axis erasure + layer probing

Step 3: Cross-Scale Integration
  ├── Map scaling exponents to network modularity structure
  ├── Identify which representation axes correspond to which dynamical scales
  └── Test whether compositionality holds across pathological states

Step 4: Diagnostic Inference
  ├── Compare exponent distributions (not just means) between groups
  ├── Identify which module compositions break down in pathology
  └── Quantify representation shortcut learning via FMScope protocol
```

## Activation Keywords

brain dynamics analysis, multi-scale neuroscience, criticality scaling, renormalization group fMRI, fixed point compositionality, inhibition-dominated networks, EEG foundation model audit, subject identity trap, representation diagnostics, PRG analysis, threshold-linear networks, shortcut learning neuroscience

## Related Skills

- `psychosis-scaling-critical-regime` — PRG + scaling analysis for brain criticality
- `fixed-point-compositionality-low-rank-gluing` — network modularity and attractor compositionality
- `identity-trap-eeg-foundation-models` — representation audit for EEG models
- `renormalization-scaling-brain-activity` — RG framework for brain activity
- `brain-network-controllability` — network control theory for brain state transitions
- `complex-brain-hypothesis` — theoretical framework for brain criticality

## When to Use This Framework

1. **Studying psychiatric disorders** where both collective dynamics and network structure may be altered
2. **Auditing neural network models** trained on brain data before downstream use
3. **Designing interventions** that target specific scales (microscopic network vs. macroscopic dynamics)
4. **Comparing healthy vs. pathological brains** across multiple complementary observables
5. **Understanding compositionality** in biological and artificial neural networks

## Pitfalls

1. **Single-scale analysis is insufficient**: pathology may preserve dynamics at one scale while altering another
2. **Mean comparisons miss distribution shifts**: use full distribution comparisons for scaling exponents
3. **Subject-disjoint CV doesn't prevent shortcut learning**: FMScope diagnostics required at representation level
4. **Network modularity != functional compositionality**: only specific low-rank couplings guarantee decomposability
