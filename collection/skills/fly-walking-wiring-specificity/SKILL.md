---
name: fly-walking-wiring-specificity
description: Use when testing whether a connectome model's specific wiring matters. Nested-rewired null families, antagonist-coordination score, and Sherrington reciprocal-innervation index. Fly walking case.
category: ai_collection
version: "1.0.0"
source: arXiv:2609.38665
source_title: "How much of fly walking is written in the wiring?"
authors: "Isabel Guan, Yuntian Zhao, Dingyuan Zhang, Shipeng Lyu, I-Ming Chen (HKUST, ZENBOT, NTU, PolyU)"
published: 2026-09-29
categories: "cs.NE, q-bio.NC"
trigger_words:
  - connectome specificity
  - wiring specificity
  - null model connectome
  - rewired control network
  - antagonist coordination
  - reciprocal innervation
  - central pattern generator
  - fly walking
  - ventral nerve cord
  - connectome simulation
  - degree-preserving rewiring
  - Maslov-Sneppen
---

# Wiring Specificity Testing for Connectome Models: Rhythm Is Generic, Coordination Is Written in the Wiring

**arXiv**: 2609.38665 (29 Sep 2026) · Guan et al.
**System**: leg motor subnetworks of two independent *Drosophila* connectomes — MaleCNS (10,173 neurons, 462,650 connections) and MANC (10,440 neurons, 634,207 connections).

## Core Claim

A connectome model that oscillates passes a test that rewired networks pass too. **Test wiring specificity on coordination/pattern formation, not on rhythm generation.** In fixed-weight models of the fly leg motor system, rhythm is generic (many rewired networks were MORE rhythmic than the real ones), while antagonist coordination is stronger in the real wiring than in all 30 rewired networks — traced to Sherrington's reciprocal innervation being written into the connectome.

## Methodology Pipeline (reusable)

### 1. Fixed-weight anatomical model
- Subnetwork: leg motor neurons + proprioceptive sensory neurons + descending/intrinsic neurons with ≥half their nerve-cord synapses in leg neuropils. Connections kept when ≥5 synapses; self-connections removed.
- Weights = **signed synapse counts**: acetylcholine +1; GABA and glutamate −1 (glutamate treated as inhibitory); histamine −1 (MaleCNS). No weight training or fitting.
- Rate dynamics (Pugliese-style, simplified to identical units):
  `τ·ṙ = −r + [tanh(g(W_E + βW_I)r + I + ξ)]₊`, τ=20 ms, Euler Δt=1 ms, input noise σ=0.01.
- Only **3 global parameters**: gain g, inhibition scale β, drive d (on DNg100 descending neurons). Same 132-setting grid scan (11 gains × 3 β × 4 d) applied to real and every control network; best setting frozen, then 60-s confirmation with 20 noise realizations + 3 noise-free initial states, scored in 4 windows (15–25 s primary, 50–60 s secondary).
- Interfaces are anatomical only: input through DNg100 (initiates forward walking), output read from motor neurons grouped by target muscle into extensor/flexor pools at 4 joints (ThC, CTr, FTi, TiTa) → 20 antagonistic pairs per connectome.

### 2. Readouts that dissociate rhythm from pattern
- **Antagonist score** (the wiring-sensitive readout): `S_A = mean_p G_p · (−ρ(e_p, f_p))` where e_p, f_p are demeaned mean rates of extensor/flexor pools and G_p is an amplitude gate (both pools modulated: min sd ≥ 0.001 and min/max sd ratio ≥ 0.2). Positive S = antagonists alternate; negative = co-active.
- **Rhythmicity** (the generic readout): median spectral concentration of oscillating motor neurons — power within ±1 bin of peak frequency / total power in 0.5–50 Hz. Eligible settings require >20% of motor neurons oscillating at 1–50 Hz.
- Pre-registered decision readouts: S over all 20 pairs, over the 16 exactly-assigned pairs, over the 14 non-ThC pairs (robustness to annotation).

### 3. Six nested rewired null families (progressively preserving structure)
1. **Density** — preserve only edge count
2. **Cell role** — + edge counts between sensory/descending/interneuron/motor roles
3. **Degree** — + every neuron's in- and out-degree (Maslov–Sneppen degree-preserving target exchanges, 10 attempts/edge; synapse counts travel with edges)
4. **Leg block** — + edge counts between role×leg-segment×side blocks
5. **Lineage block** — + developmental hemilineage blocks
6. **Leg × lineage** — both
Secondary families additionally preserve the number of reciprocally connected neuron pairs. Every neuron keeps its transmitter sign. 5 networks per family → 30 per connectome.

**Pitfall**: degree- and weight-matched rewiring reproduces gross dynamics — coarse nulls overstate connectome "function". The specific wiring only shows in *which antagonistic pool each premotor input reaches*.

### 4. Pre-registered claim levels (avoid post-hoc flexibility)
- **strong**: S_real > every one of the 30 rewired networks AND S_real − max family median ≥ 0.15
- **moderate**: exceeds every network in ≥5 of 6 families AND above every family median
- **weak**: otherwise. Replication = second connectome reaches ≥moderate.
Confirmation runs must regenerate exactly (independent re-simulation reproduced all 4,692 run-window records).

### 5. Structural signature: reciprocal-innervation index
For each neuron k and pool P, combine one- and two-step signed influence:
`u_k^(P) = w̄_k^(1,P)/max_k' w̄_k'^(1,P) + w̄_k^(2,P)/max_k' w̄_k'^(2,P)` (mean signed one- and two-step weights from k onto pool motor neurons, W² for two-step).
`RI_p = −corr_k(u_k^(E_p), u_k^(F_p))` — positive when neurons driving one pool suppress its antagonist.
- Real networks: RI = 0.48 (MaleCNS), 0.38 (MANC); **every** rewired network negative.
- Opposite-signed influence requires an intervening neuron: excitatory neurons excite one pool and inhibit the antagonist via inhibitory interneurons (45%/42%), inhibitory neurons inhibit one pool and disinhibit the antagonist (55%/58%) — 88%/83% of shared influence opposite-signed vs 16–49% rewired.
- 96–97% of influence comes from neurons hitting BOTH pools (not segregated targeting) — the index measures opposite-signed drive, not separate neurons.

### 6. Causal test: premotor input reassignment
Exchange edge targets onto motor neurons (degree-preserving; each MN keeps input count, each presynaptic neuron keeps outputs):
- **cross-pool** (ext↔flx of same leg/joint) vs **within-pool control**.
- **Strength-matched**: restrict exchanges to same-sign, same synapse-count-decile edges (median MN input change 1.2–1.9%).
- **Dose-matched** (pre-registered after a structural audit): move as much input as original (~27%) while changing MN input by median 2.0–3.9%.
Result: cross-pool reassignment drives S below zero (antagonists co-active) while rhythm, oscillating-MN fraction and 7–8 of 8–9 contributing pairs are retained; within-pool controls keep 81–96% of real S. Coordination depends on **allocation of premotor input across pools**, not on input strength.

## Key Results
- 9/30 and 14/30 rewired networks ≥ real rhythmicity (up to 0.90 vs 0.32); 0/30 reach real coordination (0.312 vs max 0.144; 0.173 vs max 0.084).
- Coordination concentrated at **thorax–coxa joint** (mean pair score 0.71 ThC vs 0.09 FTi in MaleCNS) — the only "strong" readout in both connectomes, all 4 windows.
- Coordinated state persists: MaleCNS never left it in 92 run-windows and 300-s trajectories; MANC ~4.2 min mean episodes vs 11–16 s for strongest rewired.
- Rhythm generation may still run through the 3-neuron DNg100 CPG circuit (Pugliese et al.) — pruning finds sufficient circuits *within* real wiring; rewired nulls ask which output features *depend* on the wiring. Different questions, both valid.

## Pitfalls & Limitations
- **Glutamate sign matters**: treating glutamate as excitatory removed the real network's advantage over lineage-constrained nulls.
- Rate-neuron model, synapse-count weights, predicted transmitter signs, no body/sensory feedback; ~quarter of MN joint assignments approximate; MANC replicates in direction with smaller margins (moderate not strong; dose-matched test missed 80% activity-retention criterion).
- 5 networks/family → smallest attainable within-family rank p = 1/6.
- First pre-registration only partly blind (real MaleCNS + density family already scanned).
- Cutting the 13A/13B inhibition–disinhibition motif did NOT reduce coordination more than weight-matched control cuts → reciprocal innervation is a **distributed, network-wide input pattern**, expressible only where pools are recruited, not a single-instance motif.

## Reuse Checklist (for any connectome specificity claim)
1. Freeze weights at synapse counts; keep learned components out of the interface.
2. Scan a small global parameter grid identically for real + nulls; freeze per-network best; confirm with fresh noise in multiple windows.
3. Use ≥2 independently reconstructed connectomes; pre-register claim levels before scanning.
4. Score a *pattern* readout (phase relations between identified functional groups), not just oscillation.
5. Build nested nulls from density → role → degree → functional/developmental blocks; preserve signs.
6. Verify a structural signature of the claimed mechanism (e.g., RI index) that all nulls fail.
7. Causal perturbation: reassign the mechanism-relevant inputs while matching strength/dose; require selective loss (6-condition pre-registration: control retention ≥0.8R, collapse ≤0.5R with margin ≥0.10, ordering of every network, rhythm retention ≥0.8, pair/MN retention ≥0.8).

## Related Skills
- `connectome-wiring-statistics-control` (nested rewired nulls for wiring specificity)
- `dn-synaptic-placement-shared-input` (synaptic placement in Drosophila descending neurons)
- `topological-sensitivity-connectome-constraints`
