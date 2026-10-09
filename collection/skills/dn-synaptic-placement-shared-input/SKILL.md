---
name: dn-synaptic-placement-shared-input
description: Use when linking connectome topology to subcellular synapse placement.
category: ai_collection
tags: [neuroscience, connectomics, drosophila, synaptic-placement, shared-input, feedforward-motif, descending-neurons, brain-networks, physical-network-models]
arxiv_id: 2610.00690
paper_title: "Synaptic placement reflects shared input in Drosophila descending neurons"
paper_url: https://arxiv.org/abs/2610.00690
authors: Xizhe Zhang
published: 2026-09-30
---

# Synaptic Placement Reflects Shared Input: Topology ↔ Subcellular Geometry Correspondence

**Zhang (arXiv:2610.00690 [q-bio.NC] 30 Sep 2026).** First large-scale demonstration that a **three-neuron topological relationship** (feed-forward triad) is mirrored in the **relative spatial placement of synapses inside a receiving neuron** — connecting graph-level connectivity to subcellular organization.

## Core Finding

In Drosophila descending neurons (DNs), inputs from a source neuron that ALSO contacts the DN's partner lie **~8–10 μm nearer** that partner's inputs along the receiver's neurites than inputs from other sources.

The triad: source A → partner B and receiver C; B → C (feed-forward configuration). Question answered: are A's synapses on C placed near B's synapses on C?

## Data & Robustness

| Dataset | Between-source Δ | Within-source Δ | % receivers consistent |
|---------|-----------------|----------------|----------------------|
| MaleCNS (male) | **−9.42 μm** (95% CI −10.52..−8.31), n=13,318 one-way DN connections | −9.14 μm, 81.2% of 922 receivers | 82.7% of 1,079 DNs |
| FlyWire (female, independent) | **−7.98 μm** (−9.27..−6.70), n=5,807 | −10.15 μm, 82.0% of 589 | 80.7% |
| C. elegans adults (exploratory) | negative in both | −9.88 / −5.39 μm | 10/10, 11/13 receivers |

Held in TWO independent reconstructions (male + female fly), with two complementary comparison designs (between-source and within-source), path-distance AND Euclidean, all 17 regional groups same direction. This is not a single-species artifact.

## The Two Comparisons (methodological template)

1. **Between-source** (fix B→C connection): partition C's non-DN inputs by whether the source also innervates B; measure distance from each source input to nearest B-input site on C (same endpoint region, path along C's skeleton).
2. **Within-source** (fix source A and receiver C): compare A-input distance to sites supplied by partners that DO receive A input (≥5 synapses) vs partners with ZERO recorded A input. Controls for the confound that nearest-neighbor distance shrinks with reference-set size via **expected distance to three uniformly sampled distinct partner sites**:

```
d₀³(x) = (1 / C(K,3)) · Σ_{3-subsets} mean(d(ℓ) sorted)   — exact expectation over all 3-site subsets
```

Edge threshold: ≥5 brain synapses. DN–DN edges removed from input graphs. Synapse coordinates projected to nearest skeleton vertex (8nm→μm; path lengths via lowest-common-ancestor on skeleton forest).

## Key Secondary Results

- **Shared input predicts DN interconnection beyond spatial overlap** — and vice versa (logistic models, held-out cell types): adding shared-input to spatial-overlap models cut held-out log loss 2.9% (BANC) / 3.4% (MaleCNS); adding spatial overlap to shared-input models cut it 10.0/10.5%. **Complementary, not redundant, information channels.**
- Shared sources are concentrated: top-5 upstream cells account for ~91.3% (BANC) / 87.7% (MaleCNS) of shared-input cosine overlap.
- Identified circuit AN19B014 → {DNge006, DNge072}, DNge006 → DNge072: source contacts the two DNs via **distinct presynaptic sites** (21/159 sites joint) — the placement effect is postsynaptic-organization, not one axon touching both at one bouton.
- The interconnected DN pair **differs in cord outputs** (DNge072 ~half output direct to motor neurons; DNge006 more interneuron-mediated, broader motor reach) — shared input ≠ shared function.

## Mechanistic Candidates (from Discussion)

1. **Local branch accessibility**: nearby neurites ease both triad wiring and spatially proximate contacts (geometric overlap → functional connectivity, cf. cortical studies).
2. **Activity-dependent refinement**: coactive direct + partner-mediated routes could drive synaptic clustering during development (testable with developmental series).

## Why It Matters

- Adjacency matrices record *whether/how many* connections but discard *where* contacts sit on the arbor. Same topology, infinitely many placements — this paper shows placement is **systematically non-random and topology-predictive**.
- Provides a new observable for generative connectome models: whether source–partner connectivity predicts relative input placement (physical-network models with structured internal nodes).
- Extends C. elegans three-neuron/local-organization results to a different neuronal population with much larger n and cross-sex/species replication.

## Analysis Recipes (reusable)

1. **Skeleton path distance pipeline**: SWC → undirected weighted graph → project synapses to nearest vertex → pairwise shortest paths (LCA on forest) → nearest-site distance per (source-input, partner-site-set).
2. **Reference-set-size standardization**: when comparing nearest-neighbor distances between groups with different site counts, use exact expectation over k-site subsets (k=3, fixed a priori) instead of raw min — eliminates the trivial "more sites ⇒ nearer" bias.
3. **Topology-vs-geometry predictive test**: logistic models with (a) spatial overlap only, (b) shared input only, (c) both; report held-out log-loss reduction from each addition with complete-type-excluded cross-validation (both endpoint types withheld).
4. **Stratification discipline**: same endpoint brain region, same skeleton component, equal receiver weighting, exact-type clustered intervals; prevalence-retained evaluation pairs.

## When to Use

- Analyzing any connectome with synapse-coordinate resolution (MaleCNS, FlyWire/FAFB, BANC, MICrONS, C. elegans, Platynereis)
- Building generative network models that should reproduce subcellular placement, not just topology
- Designing experiments on dendritic integration: converging shared-input routes land near each other ⇒ potential local integration/multiplicative effects
- Critiquing adjacency-matrix-only analyses: contact counts without placement discard predictive structure

## Limitations (author's own)

- Observational/associational — no causal manipulation (cf. larval dendrite-shift experiments as future direction)
- Receivers within specimens are observations, not independent animals; intervals clustered by type
- Platynereis extension underpowered (4 pairs)
- Mechanism (geometry vs activity) unresolved
