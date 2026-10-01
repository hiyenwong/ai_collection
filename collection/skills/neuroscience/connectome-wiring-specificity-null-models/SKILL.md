---
name: connectome-wiring-specificity-null-models
description: Nested rewired nulls test connectome wiring specificity.
category: ai_collection
---

# Connectome Wiring Specificity via Nested Rewired Null Models

**Source**: arXiv:2609.38665 — "How much of fly walking is written in the wiring?" (Isabel Guan et al., HKUST / ZENBOT / NTU / PolyU HK; 29 Sep 2026, q-bio.NC/cs.NE)

**Use when**: testing whether a connectome-constrained model's behavior depends on its *specific* wiring versus generic network statistics; designing null-model controls for connectome simulations; analyzing Drosophila locomotor circuits; evaluating claims that "the connectome generates behavior X".

## Core Lesson

**A model that produces a behavior does not show that its specific wiring matters.** Recurrent networks oscillate readily, and degree/weight statistics fix much of the gross dynamics. Test wiring specificity on **coordination (pattern formation), not rhythm generation** — rhythm passes in any rewired network; antagonist coordination does not.

## The Experimental Design (methodological gold standard)

**System**: leg motor subnetworks of two *independently reconstructed* Drosophila connectomes:
- MaleCNS v1.0: 10,173 neurons (8,702 interneurons, 424 descending, 381 motor, 666 sensory), 462,650 connections (≥5 synapses)
- MANC v1.0: 10,440 neurons (8,951/498/396/595), 634,207 connections

**Fixed-weight rate model** (nothing trained or fitted):
```
τ ṙ = −r + tanh( g (W_E + β W_I) r₊ + I + ξ )₊ ,   τ = 20 ms
```
- Weights = signed synapse counts; glutamatergic synapses treated as inhibitory.
- Only 3 free global parameters: gain g, inhibition scale β, drive d — selected by a 132-setting scan per network, then frozen.
- Anatomical interface: input ONLY via DNg100 descending neurons (initiate forward walking); output ONLY from motor neurons grouped into extensor/flexor pools at 4 joints per leg (ThC, CTr, FTi, TiTa) → 20 antagonistic pool pairs per connectome.

**Primary readout — antagonist score**:
```
S_A = (1/|A|) Σ_p G_p · ( −corr(e_p, f_p) )
```
G_p = amplitude gate (1 only when both pools substantially modulated); ρ = Pearson correlation over scoring window. S > 0 ⇒ antagonists alternate. Rhythmicity measured separately (spectral concentration).

**Nested rewired null families** (5 networks each, preserving progressively more structure):
```
density (edge count) → cell role → degree (per-neuron in/out) → leg block (segment×side) → lineage block (hemilineage) → leg × lineage
```
Transmitter signs always preserved.

**Rigor features rare in connectome modeling**:
1. Claim levels + decision criteria pre-registered BEFORE results.
2. 60-s confirmation at frozen settings: 20 fresh-noise realizations × 3 noise-free inits × 4 time windows.
3. Confirmation runs regenerate exactly (4,692 run-window records reproduced to rounding error).
4. Replication in a second, independently reconstructed connectome.

## Key Findings

1. **Rhythm is generic**: 9/30 (MANC) and 14/30 (MaleCNS) rewired networks ≥ real in rhythmicity; at coordination-selected settings rewired MaleCNS reached 0.90 rhythmicity vs 0.32 real. Many rewired networks were MORE rhythmic than the real wiring.

2. **Antagonist coordination is wiring-specific**: real MaleCNS S = 0.312 in both main windows vs ≤ 0.144 for ANY of its 40 rewired networks; real MANC 0.173/0.128 vs ≤ 0.084. Real exceeded every rewired network in every window of both connectomes. MaleCNS "strong" (margins 0.26–0.40 over family medians); MANC "moderate" (0.134/0.086 vs 0.15 strong threshold).

3. **Mechanism — Sherrington's reciprocal innervation (c. 1900) is written into the connectome**: signed one/two-step influence between antagonistic pools. Real reciprocal-innervation index: 0.48 (MaleCNS), 0.38 (MANC); ALL rewired < 0. Two forms: excitatory neurons excite one pool and inhibit the antagonist via inhibitory interneurons; inhibitory neurons inhibit one pool and disinhibit the antagonist (13A/13B hemilineages).

4. **Causal reassignment test**: moving premotor inputs across antagonistic pools abolished coordination even when motor neurons' input strength changed little (median change < 4%) — coordination depends on WHICH pool each premotor input reaches, not on aggregate input strength.

5. **Where**: concentrated at the thorax–coxa (ThC) joint — the only joint "strong" in both connectomes in all four windows; matches the phase offset Pugliese et al. observed. Coordination persists for minutes and does not require noise (noise-free runs stable at 0.325/0.233/0.325 for 60 s).

## Implementation Recipe (generalizable)

1. Extract subnetwork from connectome with explicit rules (cell roles, synapse threshold, ≥50% neuropil criterion).
2. Build fixed-weight dynamical model; keep free parameters minimal (3 globals); scan on a pre-declared grid, freeze the best.
3. Define readouts separating rhythm (spectral concentration) from pattern (pairwise antagonist correlations with amplitude gating).
4. Generate nested null families preserving progressively more structure; keep signs fixed.
5. Pre-register claim levels; confirm with fresh-noise runs in multiple windows; ensure exact reproducibility of runs.
6. Replicate in an independent dataset.
7. Trace mechanism structurally (reciprocal-innervation index) and causally (input reassignment with strength-matched controls).

## Pitfalls & Limitations (from the paper)

- Results concern the **model, not the animal**. No body, no load, no sensory feedback.
- Glutamate-as-inhibitory assumption is load-bearing: treating glutamate as excitatory removed the real network's advantage over lineage-constrained rewires in earlier short-window sims.
- ~25% of motor-neuron joint assignments approximate; MANC ThC advantage driven mainly by hind-leg pairs with approximately assigned pools.
- Replication was directional but weaker in MANC (moderate not strong; coordinated state switched on minute timescales; dose-matched test fell short of criteria in primary window).
- 5 networks per family → smallest attainable within-family rank p = 1/6; finite parameter grid (MANC best at highest drive); first comparison's pre-registration only partly blind.
- Distributed implementation: cutting the 13A/13B motif alone did NOT reduce coordination more than weight-matched control cuts — the property is network-wide input allocation, not a single labeled circuit.

## Relation to Prior Work

- Pruning-based sufficiency tests (e.g., 3-neuron DNg100 rhythm circuit) and rewiring-based specificity tests answer **different questions**: sufficiency within real wiring vs dependence of output on the specific wiring.
- Degree/weight-matched rewiring of the larval connectome reproduced gross dynamics but broke input routing; apparent connectome-topology advantages in trained networks vanish under degree-preserving controls.

## Related Skills

- `connectome-synapse-flow-certified-mixing`, `connectome-wiring-statistics-control` — sibling connectome-control methodologies.
- `neuromodulated-synaptic-plasticity` — for when fixed weights are not the target.
